from typing import Annotated, Optional

import asyncio
import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from pydantic import Field

from ..routines.analysis_samples import (
    __DEFAULT_MH_BIN_DIR__,
    SampleInfo,
    analysis_samples,
)
from ..routines.extract_uaf import extract_mass_hunter_analysis_file
from ..utils.common import logger
from .config import settings


def create_mcp_server(**kwargs) -> FastMCP:
    mcp = FastMCP("mh-operator MCP server", **kwargs)

    @mcp.tool()
    def read_analysis_file(
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
        return extract_mass_hunter_analysis_file(
            Path(uaf), mh_bin_path=settings.mh_bin_path, processed=True
        )

    @mcp.tool()
    def analysis_sample(
        sample: Annotated[
            str,
            Field(
                description=f"The Mass Hunter tests (.D) to analysis",
            ),
        ]
    ) -> Annotated[
        str, Field(description="The exported json file path of the generated UAF file")
    ]:
        """Analysis sample with Mass Hunter"""

        res = analysis_samples(
            [SampleInfo(path=Path(sample))],
            analysis_method=settings.analysis_method,
            output=settings.output,
            report_method=settings.report_method,
            mode=settings.mode,
            mh_bin_path=__DEFAULT_MH_BIN_DIR__,
            istd=settings.istd,
        )
        return str(res)

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
