from typing import Annotated, Optional

import asyncio
import json
import uuid
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


class InMemoryFS:
    def __init__(self):
        self._data = {}

    def write(self, path: str, data: bytes):
        self._data[path] = data

    def read(self, path: str) -> Optional[bytes]:
        return self._data.get(path)

    @staticmethod
    def generate_uuid_path() -> str:
        return str(uuid.uuid4())


def create_mcp_server(**kwargs) -> FastMCP:
    mcp = FastMCP("mh-operator MCP server", **kwargs)
    in_memory_fs = InMemoryFS()

    @mcp.resource("{drive}://{data_path}")
    def save_resource(
        data: Annotated[
            bytes,
            Field(
                description="The binary data to save.",
            ),
        ],
        data_path: Annotated[
            Optional[str],
            Field(
                description="Optional: The desired path to save the data. If not provided, a UUID will be generated.",
            ),
        ] = None,
        drive: Annotated[
            str, Field(description="The location of the uploaded data to be saved")
        ] = "inmemory",
    ) -> Annotated[
        str,
        Field(
            description="The path (UUID or user-provided) where the data was saved.",
        ),
    ]:
        """Save binary data to the in-memory filesystem."""
        if drive != "inmemory":
            raise NotImplementedError

        if data_path is None:
            data_path = in_memory_fs.generate_uuid_path()
        in_memory_fs.write(data_path, data)
        return f"inmemory:{data_path}"

    @mcp.resource("{drive}://{data_path}")
    def read_resource(
        data_path: Annotated[
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
        return in_memory_fs.read(data_path)

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
            mh_bin_path=settings.mh_bin_path,
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
