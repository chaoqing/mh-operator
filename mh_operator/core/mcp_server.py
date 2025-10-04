from typing import Annotated, Optional

import asyncio
import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from pydantic import Field

from ..routines.analysis_samples import (
    __DEFAULT_MH_BIN_DIR__,
    FileOpenMode,
    SampleInfo,
    SampleType,
    analysis_samples,
)
from ..routines.extract_uaf import extract_mass_hunter_analysis_file
from ..utils.common import logger


def create_mcp_server(**kwargs) -> FastMCP:
    mcp = FastMCP("mh-operator MCP server", **kwargs)

    mcp.tool()(extract_mass_hunter_analysis_file)

    @mcp.tool()
    def analysis_sample(
        sample: Annotated[
            Path,
            Field(
                description=f"The Mass Hunter tests (.D) to analysis",
            ),
        ],
        analysis_method: Annotated[
            Path,
            Field(
                description="The Mass Hunter analysis method path (.m)",
            ),
        ] = Path("Process.m"),
        output: Annotated[
            str,
            Field(
                description="The Mass Hunter analysis file name (.uaf)",
            ),
        ] = "batch.uaf",
        report_method: Annotated[
            Optional[Path],
            Field(
                description="The Mass Hunter report method path (.m)",
            ),
        ] = None,
        mh_bin_path: Annotated[
            Path,
            Field(
                description="The bin path of the installed Mass Hunter",
            ),
        ] = __DEFAULT_MH_BIN_DIR__,
    ) -> Annotated[
        Path, Field(description="The exported json file path of the generated UAF file")
    ]:
        """Analysis sample with Mass Hunter"""
        return analysis_samples(
            [SampleInfo(path=Path(sample), type=SampleType.Sample)],
            analysis_method=analysis_method,
            output=output,
            report_method=report_method,
            mode=FileOpenMode.WRITE,
            mh_bin_path=mh_bin_path,
            istd=None,
        )

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
