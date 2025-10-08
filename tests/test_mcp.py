import asyncio

from mcp.types import TextContent

from mh_operator.core.mcp_client import MCPClient
from mh_operator.utils.common import logger


def test_mcp_client():
    async def main():
        MCP_SERVER_URL = "https://mcp.context7.com/mcp"
        client = MCPClient()

        async def search_doc(session):
            response = await session.call_tool(
                "resolve-library-id", {"libraryName": "context7"}
            )
            assert not response.isError

            (text_content,) = response.content
            assert isinstance(text_content, TextContent)
            logger.debug(text_content.text)
            import random

            library_id = random.choice(
                [
                    l.split(": ", maxsplit=1)[-1]
                    for l in text_content.text.split("\n")
                    if l.startswith("- Context7-compatible library ID: ")
                ]
            )

            logger.info(f"Searching {library_id}\n")

            response = await session.call_tool(
                "get-library-docs", {"context7CompatibleLibraryID": library_id}
            )
            assert not response.isError

            (text_content,) = response.content
            assert isinstance(text_content, TextContent)
            logger.warning(text_content.text)

        try:
            await client.connect_to_server(MCP_SERVER_URL)
            await client.list_tools()
            await client.list_resources()
            await search_doc(client.session)
        finally:
            await client.cleanup()

    asyncio.run(main())
