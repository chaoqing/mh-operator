# type: ignore[attr-defined]
from typing import Annotated, List, Optional

from enum import Enum
from pathlib import Path
from random import choice

import typer
from rich.console import Console

from mh_operator import version
from mh_operator.utils.common import logger
from mh_operator.utils.ironpython27 import (
    __DEFAULT_MH_BIN_DIR__,
    __DEFAULT_PY275_EXE__,
    CaptureType,
    run_ironpython_script,
)


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="mh-operator",
    help="Awesome `mh-operator` provide interfaces and common routines for the Agilent MassHunter official SDK.",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]mh-operator[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="install")
def install_legacy_import_helper(
    mh: Annotated[
        Path,
        typer.Option(
            help="The bin path of the installed Mass Hunter",
        ),
    ] = __DEFAULT_MH_BIN_DIR__,
    ipy: Annotated[
        Path,
        typer.Option(
            help="The ipy.exe path of the installed Python2.7",
        ),
    ] = __DEFAULT_PY275_EXE__,
    symlink: Annotated[
        bool,
        typer.Option(
            help="Do symlink instead of copy",
        ),
    ] = False,
):
    """Install the mh_operator.legacy into Python2.7 environment"""

    legacy_script = Path(__file__).parent / "legacy" / "__init__.py"

    assert Path(mh).exists()

    mh_exe_path = {
        "UAC": Path(mh) / "UnknownsAnalysisII.Console.exe",
        "LEC": Path(mh) / "LibraryEdit.Console.exe",
        "QC": Path(mh) / "QuantConsole.exe",
    }

    def install_to(tgt, src):
        if tgt.exists():
            tgt.unlink()

        logger.debug(f"{'Symlink' if symlink else 'Copy'} `{src}` to `{tgt}`")
        if symlink:
            tgt.symlink_to(src)
        else:
            tgt.write_bytes(src.read_bytes())

    logger.info(f"Install mh-operator legacy for {ipy}")
    install_to(
        Path(ipy).parent / "Lib" / "site-packages" / "mh_operator_legacy.py",
        legacy_script,
    )

    for interpreter, exe_path in mh_exe_path.items():
        logger.info(f"Install mh-operator legacy for {interpreter}: {exe_path}")
        _, stdout, _ = run_ironpython_script(
            legacy_script,
            exe_path,
            python_paths=[str(Path(__file__).parent / "..")],
            extra_envs=["MH_CONSOLE_COMMAND_STRING=print(sys.path)"],
            capture_type=CaptureType.SEPERATE,
        )
        import ast

        tgt_path = next(
            p for p in ast.literal_eval(stdout.splitlines()[-1]) if "MassHunter" in p
        )

        install_to(Path(tgt_path) / "mh_operator_legacy.py", legacy_script)


@app.command(name="extract-uaf")
def extract_mass_hunter_analysis_file(
    uaf: Annotated[
        Path,
        typer.Argument(
            help="The Mass Hunter analysis file (.uaf)",
        ),
    ],
    mh: Annotated[
        Path,
        typer.Option(
            help="The bin path of the installed Mass Hunter",
        ),
    ] = __DEFAULT_MH_BIN_DIR__,
    processed: Annotated[
        bool,
        typer.Option(
            help="Do processing on the tables inside MassHunter script",
        ),
    ] = False,
    output: Annotated[
        str,
        typer.Option(
            "-o",
            "--output",
            help="The output file path or '-' for stdout",
        ),
    ] = "-",
):
    """Export all data tables from Mass Hunter analysis file to json/xlsx"""
    legacy_script = Path(__file__).parent / "legacy" / "__init__.py"

    uac_exe = Path(mh) / "UnknownsAnalysisII.Console.exe"
    assert Path(uac_exe).exists()
    assert Path(uaf).exists()

    commands = ";".join(
        (
            "from mh_operator.legacy.common import global_state",
            "global_state.UADataAccess = UADataAccess",
            "from mh_operator.legacy.UnknownsAnalysis import export_analysis",
            f"print(export_analysis(r'{Path(uaf).absolute()}').to_json({processed}))",
        )
    )
    logger.debug(f"use {legacy_script} to exec code '{commands}'")

    returncode, stdout, stderr = run_ironpython_script(
        legacy_script,
        uac_exe,
        python_paths=[str(uac_exe.parent), str(Path(__file__).parent / "..")],
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


@app.command(name="analysis")
def analysis_samples(
    samples: Annotated[
        list[Path],
        typer.Argument(
            help="The Mass Hunter analysis file name (.D)",
        ),
    ],
    analysis_method: Annotated[
        Path,
        typer.Option(
            "-m",
            "--method",
            help="The Mass Hunter analysis method path (.m)",
        ),
    ] = "Process.m",
    output: Annotated[
        str,
        typer.Option(
            "-o",
            "--output",
            help="The Mass Hunter analysis file name (.uaf)",
        ),
    ] = "batch.uaf",
    report_method: Annotated[
        Path,
        typer.Option(
            "--report-method",
            help="The Mass Hunter report method path (.m)",
        ),
    ] = None,
    mh: Annotated[
        Path,
        typer.Option(
            help="The bin path of the installed Mass Hunter",
        ),
    ] = __DEFAULT_MH_BIN_DIR__,
):
    """Analysis samples with Mass Hunter"""
    legacy_script = Path(__file__).parent / "legacy" / "__init__.py"

    uac_exe = Path(mh) / "UnknownsAnalysisII.Console.exe"
    assert Path(uac_exe).exists()

    commands = ";".join(
        (
            "from mh_operator.legacy.common import global_state",
            "global_state.UADataAccess = UADataAccess",
            "from mh_operator.legacy.UnknownsAnalysis import analysis_samples, Sample",
            "analysis_samples(r'{}', [{}], r'{}', istd=None, report_method={})".format(
                output,
                ", ".join([f"Sample(r'{s.absolute()}')" for s in samples]),
                analysis_method,
                f"r'{report_method}'" if report_method else None,
            ),
        )
    )
    logger.debug(f"use {legacy_script} to exec code '{commands}'")

    returncode, _, _ = run_ironpython_script(
        legacy_script,
        uac_exe,
        python_paths=[str(uac_exe.parent), str(Path(__file__).parent / "..")],
        extra_envs=[f"MH_CONSOLE_COMMAND_STRING={commands}", f"MH_BIN_DIR={mh}"],
        capture_type=CaptureType.NONE,
    )
    if returncode != 0:
        logger.info(f"UAC return with {returncode}")


if __name__ == "__main__":
    app()
