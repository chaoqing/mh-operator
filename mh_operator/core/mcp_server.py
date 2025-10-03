import asyncio
import json

from mcp.server.fastmcp import FastMCP

from ..routines.analysis_samples import analysis_samples
from ..routines.extract_uaf import extract_mass_hunter_analysis_file
from ..utils.common import logger


def create_mcp_server(**kwargs) -> FastMCP:
    mcp = FastMCP("mh-operator MCP server", **kwargs)

    mcp.tool()(extract_mass_hunter_analysis_file)
    mcp.tool()(analysis_samples)

    for tool in asyncio.run(mcp.list_tools()):
        logger.debug(
            f"MCP tool `{tool.name}`\n"
            f"- Description: {tool.description}\n\n"
            f"- Input Schema: >|\n"
            f"{json.dumps(tool.inputSchema, indent=2)}\n\n"
            f"- Output Schema: >|\n"
            f"{json.dumps(tool.outputSchema, indent=2)}\n\n"
            f"{'-' * 40}"
        )

    return mcp
