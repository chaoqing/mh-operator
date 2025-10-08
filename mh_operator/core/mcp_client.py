from typing import List, Optional

import json
from contextlib import AsyncExitStack

from mcp import ClientSession, types
from mcp.client.streamable_http import streamablehttp_client
from pydantic import AnyUrl

from ..utils.common import logger


class MCPClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None
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

        available_resources: List[types.Resource] = response.resources
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
