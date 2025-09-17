# type: ignore[attr-defined]
from typing import Annotated

import json
import os
from pathlib import Path

from mh_operator.utils.code_generator import function_to_string
from mh_operator.utils.common import logger
from mh_operator.utils.ironpython27 import (
    __DEFAULT_MH_BIN_DIR__,
    __DEFAULT_PY275_EXE__,
    CaptureType,
    run_ironpython_script,
)


def extract_mass_hunter_analysis_file(
    uaf: Path,
    mh_bin_path: Path,
    processed: bool,
    output: str,
):
    """Export all data tables from Mass Hunter analysis file to json/xlsx"""
    legacy_script = Path(__file__).parent.parent / "legacy" / "__init__.py"

    uac_exe = Path(mh_bin_path) / "UnknownsAnalysisII.Console.exe"
    assert Path(uac_exe).exists()
    assert Path(uaf).exists()

    @function_to_string(return_type="asis", oneline=True)
    def _commands(uaf: str, processed: bool):
        from mh_operator.legacy.common import global_state

        global_state.UADataAccess = UADataAccess
        from mh_operator.legacy.UnknownsAnalysis import export_analysis

        return export_analysis(uaf).to_json(processed)

    commands = _commands(str(Path(uaf).absolute()), processed)
    logger.debug(f"use {legacy_script} to exec code '{commands}'")

    returncode, stdout, stderr = run_ironpython_script(
        legacy_script,
        uac_exe,
        python_paths=[str(uac_exe.parent), str(Path(__file__).parent.parent / "..")],
        extra_envs=[f"MH_CONSOLE_COMMAND_STRING={commands}"],
        capture_type=CaptureType.SEPERATE,
    )
    if returncode != 0:
        logger.info(f"UAC return with {returncode} and stderr:\n{stderr}")

    logger.debug(f"UAC return stdout:\n {stdout}")
    import json

    json_data = json.loads(stdout.split("\n", maxsplit=2)[-1])
    if output == "-":
        print(json.dumps(json_data, indent=2))
    elif output.endswith(".json"):
        with open(output, "w") as fp:
            json.dump(json_data, fp)
    elif output.endswith(".sqlite"):
        import sqlite3

        import pandas as pd

        with sqlite3.connect(output) as conn:
            for t, v in json_data.items():
                pd.DataFrame(v).to_sql(t, con=conn, if_exists="replace")
    elif output.endswith(".xlsx"):
        import pandas as pd

        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            for t, v in json_data.items():
                pd.DataFrame(v).to_excel(writer, sheet_name=t, index=False)
