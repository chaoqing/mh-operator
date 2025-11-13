from typing import Annotated, List, Optional

import asyncio
import base64
import json
import os
import tarfile
from collections.abc import Iterable
from contextlib import AsyncExitStack
from io import BytesIO

try:
    from itertools import batched
except ImportError:
    from itertools import islice

    def batched(iterable, n):
        it = iter(iterable)
        while batch := list(islice(it, n)):
            yield batch


from pathlib import Path
from urllib.parse import urlparse
from zipfile import ZipFile

import httpx
from mcp import ClientSession, types
from mcp.client.streamable_http import streamablehttp_client
from mcp.server import FastMCP
from pydantic import AnyUrl, Field

from ..utils.common import logger, map_concurrent
from .config import settings


def zip_and_upload(dir_path: Path, target_url: str) -> str:
    parsed_url = urlparse(target_url)
    assert Path(parsed_url.path).suffix.lower() == ".zip"
    try:
        if parsed_url.scheme in ("http", "https"):
            raise TypeError("inline http/https upload not supported in fsspec")
        import fsspec

        bytes_io = fsspec.open(target_url, "wb")
    except (ImportError, TypeError):
        bytes_io = BytesIO()

    parent_path = dir_path / ".."
    with bytes_io as fp:
        with ZipFile(fp, "w") as zip_fp:
            for root, _, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_fp.write(file_path, os.path.relpath(file_path, parent_path))

        if isinstance(bytes_io, BytesIO):
            resp = httpx.put(
                target_url,
                content=fp.getvalue(),
                headers={"Content-Type": "application/octet-stream"},
                follow_redirects=True,
            )
            resp.raise_for_status()
            # We assume the http server will return the uploaded file URI in the response content
            return resp.text or target_url
        else:
            return target_url


def create_uploader_mcp_server(default_endpoint: str = None) -> FastMCP:
    mcp = FastMCP("test.D upload server")

    @mcp.tool()
    def upload_test_zip(
        test_path: Annotated[
            str,
            Field(
                description="The path to the Agilent MassHunter test.D directory.",
            ),
        ],
        endpoint: Annotated[
            str,
            Field(
                description="The URI endpoint where the zipped test.D file will be uploaded.",
            ),
        ] = (
            default_endpoint
            or ((settings.mcp_server_url or "http://127.0.0.1:3000") + "/file")
        ),
    ) -> Annotated[
        str,
        Field(
            description="The URI of the uploaded zipped file, as returned by the endpoint."
        ),
    ]:
        """Compresses an Agilent MassHunter test.D directory into a zip file and uploads it to a specified endpoint.

        This tool facilitates the transfer of MassHunter test data by zipping the .D directory and uploading it,
        returning the URI of the uploaded resource.
        """
        test_dir = Path(test_path)
        return zip_and_upload(test_dir, f"{endpoint}/{test_dir.name}.zip")

    return mcp


class MCPClient:
    def __init__(self, mcp_server_url: str | None = None):
        self.session: ClientSession | None = None
        self.exit_stack = AsyncExitStack()
        self.server_url = mcp_server_url or settings.mcp_server_url

    async def connect_to_server(self):
        """Connect to an MCP server"""
        logger.debug(f"Connecting MCP server {self.server_url}/mcp")
        read_stream, write_stream, _ = await self.exit_stack.enter_async_context(
            streamablehttp_client(self.server_url + "/mcp")
        )
        self.session = await self.exit_stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )

        await self.session.initialize()

    async def show_tools(self):
        if self.session is None:
            await self.connect_to_server()

        response = await self.session.list_tools()
        for tool in response.tools:
            logger.info(
                f"- {tool.name}\n"
                f"  description: >|\n"
                f"{tool.description}\n"
                f"  inputs: >|\n"
                f"{json.dumps(tool.inputSchema, indent=2)}\n"
                f"  outputs: >|\n"
                f"{json.dumps(tool.outputSchema, indent=2)}\n\n"
            )

    async def get_resource(self, uri: str) -> bytes | str:
        if self.session is None:
            await self.connect_to_server()

        response = await self.session.read_resource(uri)
        (res,) = response.contents
        if isinstance(res, types.BlobResourceContents):
            return base64.b64decode(res.blob)
        else:
            assert isinstance(res, types.TextResourceContents)
            return res.text

    async def call_tool(self, tool: str, **kwargs):
        if self.session is None:
            await self.connect_to_server()

        logger.debug(f"Call tool {tool} with args {kwargs}")
        response = await self.session.call_tool(tool, arguments=kwargs)
        logger.debug(f"Got response {response}")
        assert not response.isError, response.content
        (res,) = response.content
        return res

    async def analysis_sample(self, test_D: Path, raw=True, full=False) -> str:
        uri = zip_and_upload(test_D, f"{self.server_url}/file/{test_D.name}.zip")
        logger.debug(f"test {test_D} uploaded to {self.server_url} with uri {uri}")
        res = await self.call_tool(
            "analysis_sample",
            uri=uri,
            raw=raw,
        )
        logger.debug(f"remote analysis_sample complete with {res.text}")
        if raw and not full:
            return await self.get_resource(res.text)
        elif raw and full:
            worksapce_resource_uri = (
                res.text.replace("report", "workspace", 1).removesuffix(".json")
                + ".tar.gz"
            )
            logger.debug(f"remote workspace served under {worksapce_resource_uri}")
            bytes_buffer = BytesIO(await self.get_resource(worksapce_resource_uri))
            with tarfile.open(fileobj=bytes_buffer, mode="r:gz") as tar:
                res_json = next(
                    f for f in tar.getmembers() if f.name.endswith(".uaf.json")
                )
                logger.debug(f"result json under {res_json}")
                cs_json = next(
                    f for f in tar.getmembers() if f.name.endswith(".uaf.cs.json")
                )
                logger.debug(f"cs json under {cs_json}")
                return (
                    "[\n"
                    + tar.extractfile(res_json).read().decode()
                    + ",\n"
                    + tar.extractfile(cs_json).read().decode()
                    + "\n]"
                )
        else:
            return res.text

    async def show_resources(self):
        response: types.ListResourcesResult = await self.session.list_resources()

        available_resources: list[types.Resource] = response.resources
        for resource in available_resources:
            logger.info(
                f"- Resource: {resource.name}\n"
                f"  URI: {resource.uri}\n"
                f"  MIMEType: {resource.mimeType}\n"
                f"  Description: {resource.description}\n"
            )

            resource_content_result: types.ReadResourceResult = (
                await self.session.read_resource(AnyUrl(resource.uri))
            )

            if isinstance(
                content_block := resource_content_result.contents,
                types.TextResourceContents,
            ):
                logger.debug(f"  Content Block: >|\n{content_block.text}")

    async def show_resource_templates(self):
        response: types.ListResourceTemplatesResult = (
            await self.session.list_resource_templates()
        )

        available_resources: list[types.ResourceTemplate] = response.resourceTemplates
        for resource in available_resources:
            logger.info(
                f"- ResourceTemplate: {resource.name}\n"
                f"  URI: {resource.uriTemplate}\n"
                f"  Description: {resource.description}\n"
            )

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()


def analysis_examples(
    samples: Iterable[Path],
    mcp_server_url: str | None = None,
    batch: int = 5,
    raw: bool = True,
    full: bool = False,
):
    async def main():
        client = MCPClient(mcp_server_url=mcp_server_url)

        try:
            await client.connect_to_server()
            results = []

            @map_concurrent(batch)
            async def _analysis_examples(s):
                return await client.analysis_sample(s, raw=raw, full=full)

            async for result, error in _analysis_examples(samples):
                if error is not None:
                    e, msg = error
                    logger.error(f"Error processing sample: {msg}")
                    results.append(
                        "{}" if raw else f"Error encountered: {e}"
                    )  # give an empty json string for errored samples
                else:
                    results.append(result)
            return results
        finally:
            await client.cleanup()

    return asyncio.run(main())
