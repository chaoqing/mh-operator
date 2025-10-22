from typing import Annotated, List, Optional

import asyncio
import base64
import json
import os
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

from ..utils.common import logger
from .config import settings


def zip_and_upload(dir_path: Path, target_url: str) -> bytes:
    assert urlparse(target_url).scheme in ("http", "https")
    with BytesIO() as fp:
        parent_path = dir_path / ".."
        with ZipFile(fp, "w") as zip_fp:
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_fp.write(file_path, os.path.relpath(file_path, parent_path))

        data_bytes = fp.getvalue()
    resp = httpx.put(
        target_url,
        content=data_bytes,
        headers={"Content-Type": "application/octet-stream"},
    )
    resp.raise_for_status()
    return resp.content


def create_uploader_mcp_server() -> FastMCP:
    mcp = FastMCP("test.D upload server")

    @mcp.tool()
    def upload_test_zip(
        test_path: Annotated[
            str,
            Field(
                description="The Agilent test.D path",
            ),
        ],
        endpoint: Annotated[
            str,
            Field(
                description="The uri where the zip files will be upload to",
            ),
        ] = settings.mcp_server_url,
    ) -> Annotated[
        str,
        Field(description="The URI of the zipped file returned by the endpoint"),
    ]:
        """Compress the Agilent GCMS test.D files into zip and upload to"""
        test_dir = Path(test_path)
        response_bytes = zip_and_upload(
            test_dir, f"{endpoint}/file/{test_dir.name}.zip"
        )
        res = json.loads(response_bytes.decode())
        assert res["status"] == "ok"

        return f"{endpoint}/file/{res['key']}"

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
        assert not response.isError
        (res,) = response.content
        return res

    async def analysis_sample(self, test_D: Path, raw=True) -> str:
        response_bytes = zip_and_upload(
            test_D, f"{self.server_url}/file/{test_D.name}.zip"
        )
        res = json.loads(response_bytes.decode())
        logger.debug(f"test {test_D} uploaded to {self.server_url}")
        assert res["status"] == "ok"
        res = await self.call_tool(
            "analysis_sample",
            uri=res["uri"],
            raw=raw,
        )
        logger.debug(f"remote analysis_sample complete with {res.text}")
        if raw:
            return await self.get_resource(res.text)
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
):
    async def main():
        client = MCPClient(mcp_server_url=mcp_server_url)
        results = []

        try:
            await client.connect_to_server()
            for sample_batch in batched(samples, batch):
                results.extend(
                    await asyncio.gather(
                        *[client.analysis_sample(s, raw=raw) for s in sample_batch]
                    )
                )
            return results
        finally:
            await client.cleanup()

    return asyncio.run(main())
