from typing import Annotated, Dict, List, Optional

import asyncio
import json
from functools import cache
from io import BytesIO
from pathlib import Path
from tarfile import TarFile
from tempfile import TemporaryDirectory
from urllib.parse import urlparse
from urllib.request import url2pathname
from zipfile import ZipFile

from asyncer import asyncify
from mcp.server.fastmcp import FastMCP
from pydantic import Field
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import (
    JSONResponse,
    PlainTextResponse,
    Response,
    StreamingResponse,
)

from ..routines.analysis_samples import SampleInfo, analysis_samples, merge_uaf_tables
from ..routines.extract_samples import dump_chromatogram_spectrum, extract_samples
from ..routines.extract_uaf import extract_mass_hunter_analysis_file
from ..utils.common import SingletonABCMeta, logger
from ..utils.in_memory_storage import (
    InMemoryStorage,
    InMemoryStorageSingleton,
    StorageBackend,
    async_read_bytes,
)
from .config import settings


def load_uri_bytes(uri: str) -> bytes:
    if uri.startswith("resource://sample/"):
        return InMemoryStorageSingleton().read_bytes(uri[len("resource://sample/") :])

    parsed_url = urlparse(uri)
    if uri.startswith(settings.mcp_server_url):
        return InMemoryStorageSingleton().read_bytes(
            parsed_url.path.removeprefix("/file/")
        )

    from fsspec import open

    with open(uri, "rb") as fp:
        return fp.read()


def extract_files_to_temp(uri: str, temp_dir: str) -> list[Path]:
    parsed_url = urlparse(uri)

    suffix = Path(parsed_url.path).suffix
    if parsed_url.scheme == "file" and suffix == ".D":
        # sample tests on remote OS file system `file://C:/MassHunter/sample.D`
        return [Path(url2pathname(f"{parsed_url.netloc}{parsed_url.path}"))]

    if suffix.lower() == ".zip":
        with ZipFile(BytesIO(load_uri_bytes(uri))) as fp:
            fp.extractall(temp_dir)
    else:

        from fsspec import FSMap, get_mapper, url_to_fs

        if parsed_url.scheme in ("http", "https"):
            uri = "simplecache::" + uri
        if suffix.lower() in (
            ".7z",
            ".gz",
            ".tar",
            ".tgz",
            ".bz2",
            ".tbz",
            ".xz",
            ".lzma",
            ".tlz",
            ".txz",
            ".tbz2",
            ".rar",
            ".iso",
        ):
            uri = "libarchive::" + uri

        src_fs, src_root = url_to_fs(uri)
        src: FSMap = src_fs.get_mapper(src_root)
        dst: FSMap = get_mapper(temp_dir)

        from multiprocessing.pool import ThreadPool

        with ThreadPool(32) as p:
            n = sum(
                (
                    1
                    for _ in p.imap_unordered(
                        lambda k: dst.__setitem__(k, src[k]), src.keys()
                    )
                ),
                0,
            )
            logger.debug(f"Copied {n} files from {uri} to {temp_dir}")

    return list(Path(temp_dir).glob("*.D"))


@cache
def create_mcp_server(storage: InMemoryStorage, file_service=True, **kwargs) -> FastMCP:
    mcp = FastMCP("mh-operator MCP server", **kwargs)

    @mcp.resource("resource://workspace/{key}")
    async def uaf_project(
        key: Annotated[
            str,
            Field(
                description="The path (UUID or user-provided) of the resource to read.",
            ),
        ],
    ) -> Annotated[
        bytes | None,
        Field(
            description="The binary data of the resource, or None if not found.",
        ),
    ]:
        """Read binary data from the in-memory filesystem."""
        return storage.read_bytes(key)

    @mcp.resource("resource://report/{key}")
    async def uaf_full_json(
        key: Annotated[
            str,
            Field(
                description="The path (UUID or user-provided) of the resource to read.",
            ),
        ],
    ) -> Annotated[
        str | None,
        Field(
            description="The text data of the resource, or None if not found.",
        ),
    ]:
        """Read binary data from the in-memory filesystem."""
        return storage.read_bytes(key).decode()

    @mcp.tool()
    async def read_analysis_file(
        uaf: Annotated[
            str,
            Field(
                description="The URI of the MassHunter analysis file (.uaf) to be read. This can be a local file path or a resource URI.",
            ),
        ],
    ) -> Annotated[
        str,
        Field(
            description="A JSON string representing the extracted and processed data from the .uaf file."
        ),
    ]:
        """Reads a MassHunter analysis file (.uaf) and extracts its contents into a structured JSON format.

        The .uaf file is processed to extract relevant analysis results, which are then returned as a JSON string.
        """
        return await asyncify(extract_mass_hunter_analysis_file)(
            Path(uaf), mh_bin_path=settings.mh_bin_path, processed=True
        )

    @mcp.tool()
    async def analysis_sample(
        uri: Annotated[
            str,
            Field(
                description=(
                    "The full URI of the MassHunter test (.D) to analyze. Zipped test (.D.zip) will be unzipped automatically. Scheme must be set accordingly. "
                    "Supports `resource://` and `file://` for in-memory storage and OS files on the remote server where this MCP is hosted respectively, and other general URI like `https://`, `ftp://` and `s3://`(for S3 service). "
                ),
            ),
        ],
        raw: Annotated[
            bool,
            Field(
                description="If true, returns the URI of the raw JSON resource generated from the UAF file. If false, returns a human-readable summary of the detected compounds."
            ),
        ] = False,
    ) -> Annotated[
        str,
        Field(
            description="The URI of the raw JSON resource (if `raw` is true) or a natural language summary of the analysis (if `raw` is false)."
        ),
    ]:
        """Analyzes a MassHunter sample (.D) from a given URI, processes it, and returns either a raw JSON resource URI or a human-readable summary.

        The local file path on MCP client OS is generally not accessiable to this tool (usual case user asks to analysis `/path/to/test.D`).
        You can use MCP tool like `upload_test_zip` to pack and upload the it into third-party storage or this MCP provided in-memory storage.
        **Important**: When user ask to analysis files without specify the schema (includeing no `file://` case), **always upload first** and then call this tool with the resource URI.

        The sample is first extracted/copied to a temporary directory, then analyzed using MassHunter, and the results are stored.
        The MassHunter processing can take minutes to analyze one test.D, so be patient. Fortunately, this tool support simultaneous analysis requests.

        When user do not clearly state whether they want raw JSON or a summary, you should not set the raw option and this tool will take proper default action.
        If you got a `resource://report/` URI back, you should read the resource (a full json string) from this MCP server and do the next steps as user asked.
        """
        logger.debug(f"got request to analysis {uri}")
        with TemporaryDirectory() as tmpdir:
            (sample,) = await asyncify(extract_files_to_temp)(uri, tmpdir)
            logger.debug(f"got sample {sample} from {uri}")
            is_tmp_workspace = sample.is_relative_to(tmpdir)

            res = await asyncify(analysis_samples)(
                [SampleInfo(path=sample)],
                analysis_method=settings.analysis_method,
                output=(
                    settings.output
                    if is_tmp_workspace
                    else sample.with_suffix(".uaf").name
                ),
                report_method=settings.report_method,
                mode=settings.mode,
                mh_bin_path=settings.mh_bin_path,
                istd=settings.istd,
            )
            logger.debug(f"analysis {sample} result in {res}")
            assert res.name.endswith(
                ".uaf.json"
            ), "Internal error: unexpected result file"

            (cs_data,) = await asyncify(extract_samples)(
                [sample],
                mh_bin_path=settings.mh_bin_path,
            )
            chromatogram_spectrum_json_bytes = dump_chromatogram_spectrum(cs_data)
            cs_data_path = res.with_suffix(".cs.json")
            cs_data_path.write_bytes(chromatogram_spectrum_json_bytes)
            logger.debug(f"dump {sample} chromatogram_spectrum in {cs_data_path}")

            resource_key = storage.create_unique_key(
                Path(urlparse(uri).path).with_suffix(".json")
            )
            logger.debug(f"result will be saved as key {resource_key}")

            if not is_tmp_workspace:
                tmp_res_path = (
                    Path(tmpdir) / "UnknownsResults" / settings.output
                ).with_suffix(".uaf.json")
                tmp_res_path.parent.mkdir(parents=True, exist_ok=True)
                tmp_res_path.write_bytes(res.read_bytes())
                tmp_res_path.with_suffix("").write_bytes(
                    res.with_suffix("").read_bytes()
                )
                tmp_res_path.with_suffix(".cs.json").write_bytes(
                    chromatogram_spectrum_json_bytes
                )

            await asyncio.gather(
                storage.put(
                    resource_key.removesuffix(".json") + ".tar.gz",
                    async_read_bytes(Path(tmpdir) / "UnknownsResults"),
                ),
                storage.put(resource_key, async_read_bytes(res)),
            )

            if raw:
                return f"resource://report/{resource_key}"
            else:
                (uaf,) = merge_uaf_tables(json.loads(res.read_text()))

                components = "\n".join(
                    (
                        f"- Detected '{c['CompoundName']}' (CAS: '{c['CASNumber']}', Formula: '{c['Formula']}')"
                        f" around retention time {c['RetentionTime']:.2f}min"
                        f" with library match score {c['LibraryMatchScore']:.2f}%,"
                        f" estimated concentration to be {round(c['EstimatedConcentration'], 2) if c['EstimatedConcentration'] else 'Unknown'}."
                    )
                    for c in uaf["Components"]
                )

                return (
                    f"-- Sample '{uaf['SampleName'] or 'Unknown'}' "
                    f"acquired at {uaf['AcqDateTime']} "
                    f"with instrument {uaf['InstrumentName']} "
                    f"by {uaf['AcqOperator'] or 'anonymous'} --"
                    f"\n{uaf['Comment']}"
                    f"\nList of detected components:\n"
                    f"{components}\n"
                    f"\nThe full report can be found with resource://report/{resource_key}\n"
                )

    if file_service:
        attach_file_service(mcp, storage)

    return mcp


def attach_file_service(mcp: FastMCP, storage: InMemoryStorage) -> FastMCP:
    @mcp.custom_route("/file/{key:path}", methods=["GET"])
    async def get_object(request: Request) -> Response:
        key = request.path_params["key"]
        try:
            return StreamingResponse(storage.get(key))
        except FileNotFoundError:
            return Response(status_code=404)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)

    @mcp.custom_route("/file/{key:path}", methods=["PUT"])
    async def put_object(request: Request) -> Response:
        key = storage.create_unique_key(request.path_params["key"])
        try:
            await storage.put(key, request.stream())
            return PlainTextResponse(f"resource://sample/{key}", status_code=201)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)

    @mcp.custom_route("/file/{key:path}", methods=["DELETE"])
    async def delete_object(request: Request) -> Response:
        key = request.path_params["key"]
        try:
            await storage.delete(key)
            return Response(status_code=204)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)

    @mcp.custom_route("/file/{key:path}", methods=["HEAD"])
    async def head_object(request: Request) -> Response:
        key = request.path_params["key"]
        try:
            headers = await storage.head(key)
            return Response(headers=headers)
        except FileNotFoundError:
            return Response(status_code=404)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)

    return mcp


def create_http_server() -> Starlette:
    storage = InMemoryStorageSingleton(
        InMemoryStorage,
        max_size_mb=settings.in_memory_storage_max_size_mb,
        ttl_seconds=settings.in_memory_storage_ttl_seconds,
    )

    return create_mcp_server(storage=storage).streamable_http_app()


async def launch_combined_server(
    host: str = "127.0.0.1", http_port: int = 3000, ftp_port: int = 3021
):
    import aioftp
    import uvicorn

    class _FTPStorage(aioftp.MemoryPathIO):
        """This class is for making sure _FTPStorage work with InMemoryStorage
        For now the storage is actually seperated"""

        # TODO: make FTP and HTTP share the same cache pool
        # TODO: Maybe support lazy initialize in InMemoryFTP to skip the first one inside InMemoryStorageSingleton
        #  and make the one `aioftp.Server(path_io_factory=InMemoryFTP)` really works
        def __init__(self, max_size_mb=None, ttl_seconds=None, **kwargs):
            super().__init__(**kwargs)

    class InMemoryFTP(InMemoryStorage, _FTPStorage, metaclass=SingletonABCMeta):
        # _FTPStorage must follow InMemoryStorage because aioftp.MemoryPathIO breaks the super().__init__ chain
        pass

    storage = InMemoryStorageSingleton(
        InMemoryFTP,
        max_size_mb=settings.in_memory_storage_max_size_mb,
        ttl_seconds=settings.in_memory_storage_ttl_seconds,
    )
    assert isinstance(
        storage, InMemoryFTP
    ), "There must be call to InMemoryStorageSingleton before here"

    mcp = create_mcp_server(storage=storage)

    for tool in await mcp.list_tools():
        logger.debug(
            f"MCP tool `{tool.name}`\n"
            f"- Description: {tool.description}\n\n"
            f"- Input Schema: >|\n"
            f"{json.dumps(tool.inputSchema, indent=2)}\n\n"
            f"- Output Schema: >|\n"
            f"{json.dumps(tool.outputSchema, indent=2)}\n\n"
            f"{'-' * 40}"
        )

    http_server = uvicorn.Server(
        uvicorn.Config(app=mcp.streamable_http_app(), host=host, port=http_port)
    )

    ftp_server = aioftp.Server(
        users=(
            aioftp.User(login="anonymous"),
            aioftp.User(login="mh", password="operator"),
        ),
        path_io_factory=InMemoryFTP,
    )

    await asyncio.gather(
        http_server.serve(), ftp_server.start(host=host, port=ftp_port)
    )
