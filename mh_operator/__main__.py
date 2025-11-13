# type: ignore[attr-defined]
from typing import Annotated, Optional

import json
import os
from pathlib import Path

import typer
from rich.console import Console

from mh_operator import version
from mh_operator.core.config import settings
from mh_operator.core.constants import SampleType
from mh_operator.utils.common import logger
from mh_operator.utils.ironpython27 import (
    __DEFAULT_MH_BIN_DIR__,
    __DEFAULT_PY275_EXE__,
    CaptureType,
)

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
            extra_envs=["MH_CONSOLE_COMMAND_STRING=print(repr(sys.path))"],
            capture_type=CaptureType.SEPERATE,
        )
        import ast

        tgt_path = next(
            p for p in ast.literal_eval(stdout.splitlines()[-1]) if "MassHunter" in p
        )

        install_to(Path(tgt_path) / "mh_operator_legacy.py", legacy_script)


@app.command(name="mcp")
def mcp_server(
    host: Annotated[
        str,
        typer.Option(
            help="The mcp server listen host",
        ),
    ] = "127.0.0.1",
    port: Annotated[
        int,
        typer.Option(
            help="The mcp server listen port",
        ),
    ] = 3000,
    ftp_port: Annotated[
        int | None,
        typer.Option(
            help="The ftp server listen port (3021 or default None means disabled)",
        ),
    ] = None,
):
    """Serve the MCP server for mh-operator"""
    try:
        from mh_operator.core.config import settings

        if settings.mcp_server_url is None:
            settings.mcp_server_url = f"http://{host}:{port}"

        if ftp_port is not None:
            try:
                import aioftp
            except ImportError:
                logger.warning("aioftp not found, run `pip install aioftp` to install")
                raise typer.Exit(1)

            if settings.ftp_uri is None:
                settings.ftp_uri = f"ftp://{host}:{ftp_port}"

            import asyncio

            from mh_operator.core.mcp_server import launch_combined_server

            asyncio.run(
                launch_combined_server(host=host, http_port=port, ftp_port=ftp_port)
            )
        else:
            import uvicorn

            from mh_operator.core.mcp_server import create_http_server

            uvicorn.run(app=create_http_server(), host=host, port=port)

    except ImportError:
        logger.fatal("pip install mh-operator[mcp] to enable the mcp service")
        raise typer.Exit(1)


@app.command(name="uploader-mcp")
def mcp_client(
    endpoint: Annotated[
        str | None,
        typer.Option(
            help="The remote storage endpoint",
        ),
    ] = None,
):
    """Serve the Uploader MCP to help upload test.D to the MCP server"""
    try:
        from mh_operator.core.mcp_client import create_uploader_mcp_server

        mcp = create_uploader_mcp_server(endpoint)
        mcp.run()

    except ImportError:
        logger.fatal("pip install mh-operator[mcp] to enable the mcp service")
        raise typer.Exit(1)


@app.command(name="extract-samples")
def extract_samples_command(
    samples: Annotated[
        list[Path],
        typer.Argument(
            help=f"The Mass Hunter sample data folder (sample.D) path",
        ),
    ],
    mh: Annotated[
        Path,
        typer.Option(
            help="The bin path of the installed Mass Hunter",
        ),
    ] = __DEFAULT_MH_BIN_DIR__,
    output: Annotated[
        str,
        typer.Option(
            "-o",
            "--output",
            help="The output file path or '-' for stdout",
        ),
    ] = "-",
):
    from mh_operator.routines.extract_samples import (
        dump_chromatogram_spectrum,
        extract_samples,
    )

    results = extract_samples(samples, mh)
    if output == "-":
        print(results)
    elif output.endswith(".json"):
        with open(output, "wb") as fp:
            fp.write(dump_chromatogram_spectrum(*results, indent=2))
    else:
        raise NotImplementedError(f"not supported type for {output}")


@app.command(name="extract-uaf")
def extract_mass_hunter_analysis_file_command(
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
    import json

    from mh_operator.routines.extract_uaf import extract_mass_hunter_analysis_file

    json_data = json.loads(extract_mass_hunter_analysis_file(uaf, mh, processed))
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
def analysis_samples_command(
    samples: Annotated[
        list[str],
        typer.Argument(
            help=f"The Mass Hunter analysis file name (.D), maybe suffix with ':SampleType' to set the sample type (e.g. {'|'.join(i.name for i in SampleType)})",
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
    istd_rt: Annotated[
        float,
        typer.Option(
            "--istd-rt",
            help="The ISTD compound retention time (min.)",
        ),
    ] = None,
    istd_name: Annotated[
        str,
        typer.Option(
            "--istd-name",
            help="The ISTD compound name",
        ),
    ] = None,
    istd_value: Annotated[
        float,
        typer.Option(
            "--istd-value",
            help="The ISTD compound concentration",
        ),
    ] = None,
    mode: Annotated[
        str,
        typer.Option(
            "--mode",
            callback=(
                lambda m: {
                    k: n
                    for n, *a in (("x", "c", "create"), ("w", "write"), ("a", "append"))
                    for k in (n, *a)
                }[m.lower()]
            ),
            help="""The mode while open the analysis file,\n\n
            x/c/create: create new uaf file, raise error when uaf already exist;\n
            w/write: create new uaf file, old uaf removed at first;\n
            a/append: append to old uaf file, create new one if not exist;
            """,
        ),
    ] = "x",
    mh: Annotated[
        Path,
        typer.Option(
            help="The bin path of the installed Mass Hunter",
        ),
    ] = __DEFAULT_MH_BIN_DIR__,
):
    """Analysis samples with Mass Hunter"""
    from mh_operator.routines.analysis_samples import (
        FileOpenMode,
        ISTDOptions,
        SampleInfo,
        analysis_samples,
    )

    analysis_samples(
        [SampleInfo.from_cli(s) for s in samples],
        analysis_method,
        output,
        report_method,
        (
            None
            if all(v is None for v in [istd_rt, istd_name, istd_value])
            else ISTDOptions(
                rt=istd_rt,
                name=istd_name,
                value=istd_value,
            )
        ),
        {"x": FileOpenMode.CREATE, "w": FileOpenMode.WRITE, "a": FileOpenMode.APPEND}[
            mode
        ],
        mh,
    )


if __name__ == "__main__":
    app()
