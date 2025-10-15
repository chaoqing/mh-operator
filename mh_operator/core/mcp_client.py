from typing import Annotated, List, Optional

import json
import os
import urllib.error
import urllib.request
from contextlib import AsyncExitStack
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse
from zipfile import ZipFile

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
    req = urllib.request.Request(target_url, data=data_bytes, method="PUT")

    req.add_header("Content-Type", "application/octet-stream")
    req.add_header("Content-Length", str(len(data_bytes)))

    with urllib.request.urlopen(req) as response:  # nosec B310
        return response.read()


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
            str | None,
            Field(
                description="The uri where the zip files will be upload to",
            ),
        ] = None,
    ) -> Annotated[
        str,
        Field(description="The URI of the zipped file returned by the endpoint"),
    ]:
        """Compress the Agilent GCMS test.D files into zip and upload to"""
        endpoint = endpoint or settings.mcp_server_url
        test_dir = Path(test_path)
        response_bytes = zip_and_upload(
            test_dir, f"{endpoint}/file/{test_dir.name}.zip"
        )
        res = json.loads(response_bytes.decode())
        assert res["status"] == "ok"

        return f"{endpoint}/file/{res['key']}"

    return mcp


class MCPClient:
    def __init__(self):
        self.session: ClientSession | None = None
        self.exit_stack = AsyncExitStack()

    async def connect_to_server(self, mcp_server_url: str):
        """Connect to an MCP server

        Args:
            mcp_server_url: Path to the server script (.py or .js)
        """
        read_stream, write_stream, _ = await self.exit_stack.enter_async_context(
            streamablehttp_client(mcp_server_url)
        )
        self.session = await self.exit_stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )

        await self.session.initialize()

    async def list_tools(self):
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

    async def list_resources(self):
        response: types.ListResourcesResult = await self.session.list_resources()

        available_resources: list[types.Resource] = response.resources
        for resource in available_resources:
            logger.info(
                f"- Resource: {resource.name}\n"
                f"  URI: {resource.uri}\n"
                f"  MIMEType: {resource.mimeType}\n"
            )

            resource_content_result: types.ReadResourceResult = (
                await self.session.read_resource(AnyUrl(resource.uri))
            )

            if isinstance(
                content_block := resource_content_result.contents,
                types.TextResourceContents,
            ):
                logger.debug(f"  Content Block: >|\n{content_block.text}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()
