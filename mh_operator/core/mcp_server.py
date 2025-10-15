from typing import Annotated, Dict, List, Optional

import asyncio
import json
from functools import cache
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlparse

import aioftp
import fs.opener
from asyncer import asyncify
from fs import open_fs
from fs.copy import copy_fs
from fs.tarfs import TarFS
from fs.zipfs import ZipFS
from mcp.server.fastmcp import FastMCP
from pydantic import Field
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response, StreamingResponse
from starlette.routing import Mount, Route

from ..routines.analysis_samples import SampleInfo, analysis_samples
from ..routines.extract_uaf import extract_mass_hunter_analysis_file
from ..utils.common import logger
from ..utils.in_memory_storage import InMemoryFTP, StorageBackend, async_read_bytes
from .config import settings

try:
    from fs_s3fs.opener import S3FSOpener

    fs.opener.registry.install(S3FSOpener)
except ImportError:
    logger.warning(
        "S3FS not found, run`pip install fs-s3fs` to enable 's3://' protocol"
    )
try:
    from webdavfs.opener import WebDAVOpener

    fs.opener.registry.install(WebDAVOpener)
except ImportError:
    logger.warning(
        "WebDAV not found, run`pip install fs-webdavfs` to enable 'webdav://' protocol"
    )


def load_uri_bytes(uri: str) -> bytes:
    parsed_url = urlparse(uri)
    if uri.startswith(settings.mcp_server_url):
        return InMemoryFTP().read_bytes(parsed_url.path.removeprefix("/file/"))
    try:
        from smart_open import open as smart_open

        with smart_open(uri, "rb") as fp:
            file_bytes = fp.read()
    except ImportError:
        raise NotImplementedError("we need to use fs to read the file contents")

    return file_bytes


def extract_files_to_temp(uri: str, temp_dir: str) -> List[Path]:
    parsed_url = urlparse(uri)
    *_, suffix = parsed_url.path.rsplit(".", maxsplit=1)

    if suffix in ("zip",):
        src_fs = ZipFS(BytesIO(load_uri_bytes(uri)))
    elif suffix in ("tar",):
        src_fs = TarFS(BytesIO(load_uri_bytes(uri)))
    else:
        src_fs = open_fs(uri)

    copy_fs(src_fs, temp_dir)

    return list(Path(temp_dir).glob("*.D"))


def create_storage() -> StorageBackend:
    return InMemoryFTP(
        max_size_mb=settings.in_memory_storage_max_size_mb,
        ttl_seconds=settings.in_memory_storage_ttl_seconds,
    )


def create_ftp_server(path_io_factory=InMemoryFTP, **kwargs) -> aioftp.Server:
    return aioftp.Server(
        users=(
            aioftp.User(login="anonymous"),
            aioftp.User(login="mh", password="operator"),
        ),
        path_io_factory=path_io_factory,
        **kwargs,
    )


def create_http_server() -> Starlette:
    return create_mcp_server(
        storage=InMemoryFTP(
            max_size_mb=settings.in_memory_storage_max_size_mb,
            ttl_seconds=settings.in_memory_storage_ttl_seconds,
        )
    ).streamable_http_app()


@cache
def create_mcp_server(storage: StorageBackend, file_service=True, **kwargs) -> FastMCP:
    mcp = FastMCP("mh-operator MCP server", **kwargs)

    @mcp.resource("resource://{key}")
    async def uaf_full_json(
        key: Annotated[
            str,
            Field(
                description="The path (UUID or user-provided) of the resource to read.",
            ),
        ],
    ) -> Annotated[
        Optional[bytes],
        Field(
            description="The binary data of the resource, or None if not found.",
        ),
    ]:
        """Read binary data from the in-memory filesystem."""
        return await storage.get(key)

    @mcp.tool()
    async def read_analysis_file(
        uaf: Annotated[
            str,
            Field(
                description="The Mass Hunter analysis file (.uaf)",
            ),
        ],
    ) -> Annotated[
        str,
        Field(
            description="The dumped json string of the data contained inside the uaf file"
        ),
    ]:
        """Read the Mass Hunter analysis result from its project file(.uaf)"""
        return await asyncify(extract_mass_hunter_analysis_file)(
            Path(uaf), mh_bin_path=settings.mh_bin_path, processed=True
        )

    @mcp.tool()
    async def analysis_sample(
        sample: Annotated[
            str,
            Field(
                description=f"The Mass Hunter tests (.D) to analysis, support `osfs://` for os local files(by default if no URL protocal specified), `s3fs://` for S3 service, `mem://` for inmemory storage",
            ),
        ],
        resource_key: Annotated[
            Optional[str],
            Field(
                description="The key of the resource results, usually in format of `sample_name.json`"
            ),
        ] = None,
    ) -> Annotated[
        str, Field(description="The exported json file path of the generated UAF file")
    ]:
        """Analysis sample with Mass Hunter"""
        with TemporaryDirectory() as tmpdir:
            (sample,) = await asyncify(extract_files_to_temp)(sample, tmpdir)

            res = await asyncify(analysis_samples)(
                [SampleInfo(path=sample)],
                analysis_method=settings.analysis_method,
                output=settings.output,
                report_method=settings.report_method,
                mode=settings.mode,
                mh_bin_path=settings.mh_bin_path,
                istd=settings.istd,
            )
            key = f"{sample.name}/res.json" if resource_key is None else resource_key
            await asyncio.gather(
                storage.put(
                    key.removesuffix(".json") + ".uaf",
                    async_read_bytes(res.with_suffix("")),
                ),
                storage.put(key, async_read_bytes(res)),
            )

            return key

    if file_service:
        attach_file_service(mcp, storage)

    return mcp


def attach_file_service(mcp: FastMCP, storage: StorageBackend) -> FastMCP:
    @mcp.custom_route("/file/{key:path}", methods=["GET"])
    async def get_object(request: Request) -> Response:
        key = request.path_params["key"]
        try:
            return StreamingResponse(storage.get(key))
        except FileNotFoundError:
            return JSONResponse({"error": "Not Found"}, status_code=404)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)

    @mcp.custom_route("/file/{key:path}", methods=["PUT"])
    async def put_object(request: Request) -> Response:
        key = request.path_params["key"]
        try:
            await storage.put(key, request.stream())
            return JSONResponse({"status": "ok", "key": key}, status_code=201)
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
            return JSONResponse({"error": "Not Found"}, status_code=404)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)

    return mcp


async def launch_combined_server(
    host: str = "127.0.0.1", http_port: int = 3000, ftp_port: int = 3021
):
    import uvicorn

    mcp = create_mcp_server(
        storage=InMemoryFTP(
            max_size_mb=settings.in_memory_storage_max_size_mb,
            ttl_seconds=settings.in_memory_storage_ttl_seconds,
        )
    )
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
    ftp_server = create_ftp_server(path_io_factory=InMemoryFTP)

    await asyncio.gather(
        http_server.serve(), ftp_server.start(host=host, port=ftp_port)
    )
