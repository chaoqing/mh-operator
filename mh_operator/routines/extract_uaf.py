# type: ignore[attr-defined]
from typing import Annotated, Optional

import json
import os
from pathlib import Path

from pydantic import Field

from mh_operator.utils.code_generator import function_to_string
from mh_operator.utils.common import logger
from mh_operator.utils.ironpython27 import (
    __DEFAULT_MH_BIN_DIR__,
    __DEFAULT_PY275_EXE__,
    CaptureType,
    run_ironpython_script,
)


def extract_mass_hunter_analysis_file(
    uaf: Annotated[
        Path,
        Field(
            description="The Mass Hunter analysis file (.uaf)",
        ),
    ],
    mh_bin_path: Annotated[
        Path,
        Field(
            description="The bin path of the installed Mass Hunter",
        ),
    ] = __DEFAULT_MH_BIN_DIR__,
    processed: Annotated[
        bool,
        Field(
            description="Do processing on the tables to give the final compounds list table",
        ),
    ] = True,
) -> Annotated[
    str,
    Field(
        description="The dumped json string of the data contained inside the uaf file"
    ),
]:
    """Export all data tables from Mass Hunter analysis file to json/xlsx"""
    legacy_script = Path(__file__).parent.parent / "legacy" / "__init__.py"

    uac_exe = Path(mh_bin_path) / "UnknownsAnalysisII.Console.exe"
    assert Path(uac_exe).exists()
    assert Path(uaf).exists()

    @function_to_string(return_type="asis", oneline=True)
    def _commands(_uaf: str, _processed: bool):
        from mh_operator.legacy.common import global_state

        global_state.UADataAccess = UADataAccess
        from mh_operator.legacy.UnknownsAnalysis import export_analysis

        return export_analysis(_uaf).to_json(_processed)

    commands = _commands(str(Path(uaf).absolute()), processed)
    logger.debug(f"use {legacy_script} to exec code '{commands}'")

    return_code, stdout, stderr = run_ironpython_script(
        legacy_script,
        uac_exe,
        python_paths=[str(uac_exe.parent), str(Path(__file__).parent.parent / "..")],
        extra_envs=[f"MH_CONSOLE_COMMAND_STRING={commands}"],
        capture_type=CaptureType.SEPERATE,
    )
    if return_code != 0:
        logger.warning(f"UAC return with {return_code} and stderr:\n{stderr}")

    logger.debug(f"UAC return stdout:\n {stdout}")
    return stdout.strip().rsplit("\n", maxsplit=1)[-1]
