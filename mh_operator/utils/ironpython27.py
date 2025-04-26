from typing import List, Optional, Tuple

import os
import subprocess
import sys
from collections.abc import Iterable
from pathlib import Path
from tempfile import NamedTemporaryFile

from .common import logger, set_logger_level

# fmt: off
__DEFAULT_MH_BIN_DIR__ = Path("C:/") / "Program Files" / "Agilent" / "MassHunter" / "Workstation" / "Quant" / "bin"
__DEFAULT_PY275_EXE__ = Path("C:/") / "Program Files (x86)" / "IronPython 2.7" / "ipy.exe"
# fmt: on


def get_absolute_executable_path(
    ipy_path: Path,
    cwd: Path | None = None,
) -> Path:
    exe_path = Path(ipy_path)

    if exe_path.exists():
        logger.debug("direct found executable")
        return exe_path.absolute()
    if (
        cwd is not None
        and not exe_path.is_absolute()
        and (Path(cwd) / ipy_path).exists()
    ):
        logger.debug("found executable under relative path")
        return (Path(cwd) / ipy_path).absolute()

    # fmt: off
    alias = {
        "ipy": __DEFAULT_PY275_EXE__,
        "ipy.exe": __DEFAULT_PY275_EXE__,
        "python2": Path("/usr/bin/python2") if sys.platform == 'linux' else __DEFAULT_PY275_EXE__,

        "UAC": __DEFAULT_MH_BIN_DIR__ / "UnknownsAnalysisII.Console.exe",
        "UnknownsAnalysisII.Console": __DEFAULT_MH_BIN_DIR__ / "UnknownsAnalysisII.Console.exe",
        "UnknownsAnalysisII.Console.exe": __DEFAULT_MH_BIN_DIR__ / "UnknownsAnalysisII.Console.exe",

        "LEC": __DEFAULT_MH_BIN_DIR__ / "LibraryEdit.Console.exe",
        "LibraryEdit.Console": __DEFAULT_MH_BIN_DIR__ / "LibraryEdit.Console.exe",
        "LibraryEdit.Console.exe": __DEFAULT_MH_BIN_DIR__ / "LibraryEdit.Console.exe",

        "QC": __DEFAULT_MH_BIN_DIR__ / "QuantConsole.exe",
        "QuantConsole": __DEFAULT_MH_BIN_DIR__ / "QuantConsole.exe",
        "QuantConsole.exe": __DEFAULT_MH_BIN_DIR__ / "QuantConsole.exe",

        "CBFC": __DEFAULT_MH_BIN_DIR__ / "CheckBatchFilesConsole.exe",
        "CheckBatchFilesConsole": __DEFAULT_MH_BIN_DIR__ / "CheckBatchFilesConsole.exe",
        "CheckBatchFilesConsole.exe": __DEFAULT_MH_BIN_DIR__ / "CheckBatchFilesConsole.exe",

        "TDACC": __DEFAULT_MH_BIN_DIR__ / "TDAConverterConsole.exe",
        "TDAConverterConsole": __DEFAULT_MH_BIN_DIR__ / "TDAConverterConsole.exe",
        "TDAConverterConsole.exe": __DEFAULT_MH_BIN_DIR__ / "TDAConverterConsole.exe",

        "TDC": __DEFAULT_MH_BIN_DIR__ / "TofFeatureDetectorConsole.exe",
        "TofFeatureDetectorConsole": __DEFAULT_MH_BIN_DIR__ / "TofFeatureDetectorConsole.exe",
        "TofFeatureDetectorConsole.exe": __DEFAULT_MH_BIN_DIR__ / "TofFeatureDetectorConsole.exe",
    }
    # fmt: on
    exe_path = alias.get(str(ipy_path), None)
    if exe_path is not None and exe_path.exists():
        logger.debug("found executable with alias")
        return exe_path
    raise SystemError(f"Error: IronPython executable not found at '{ipy_path}'")


from enum import Enum, auto


class CaptureType(Enum):
    NONE = auto()
    STDOUT = auto()
    STDERR = auto()
    BOTH = auto()
    SEPERATE = auto()


def run_ironpython_script(
    script_path: Path,
    ipy_path: Path = __DEFAULT_PY275_EXE__,
    cwd: Path | None = None,
    python_paths: Iterable[str] | None = None,
    extra_envs: Iterable[str] | None = None,
    script_args: Iterable[str] | None = None,
    capture_type: CaptureType = CaptureType.STDOUT,
) -> tuple[int, str | None, str | None]:
    """
    Runs an IronPython script using the subprocess module.

    Args:
        script_path (Path): Path to the IronPython script (.py) to execute.
        ipy_path (Path): Path to the IronPython executable (e.g., ipy.exe).
        cwd (str, optional): The working directory for the subprocess.
                             Defaults to the current working directory.
        python_paths (list, optional): A list of additional paths to add to
                                       IronPython's sys.path (like PYTHONPATH).
        extra_envs (list, optional): A list of additional envrionments to prepend to
                                       copy of os.environ.
        script_args (list, optional): A list of command-line arguments to pass
                                      to the IronPython script itself.
        capture_type (CaptureType): The stdout/stderr capture for returned values.

    Returns:
        tuple: A tuple containing (return_code, stdout, stderr).

    Raises:
        SystemError: Usually because of FileNotFoundError on interperater/script

    """

    # The script_path do not respect cwd specified, always use current real working directory
    if not Path(script_path).exists():
        raise SystemError(f"Error: IronPython script not found at '{script_path}'")
    script_path = Path(script_path).absolute()

    # relative executable path can be infered by specified cwd when not found under current directory
    cwd = Path("." if cwd is None else cwd).absolute()
    assert Path(cwd).is_dir()
    ipy_path = get_absolute_executable_path(ipy_path, cwd)

    env = os.environ.copy()

    # extra environment have higher priority than those specified from outside in current process
    if extra_envs:
        for e in extra_envs:
            k, v = e.split("=", maxsplit=1)
            assert str.isidentifier(k)
            env[k] = v

    if script_args is None:
        script_args = []
    # For MassHunter executable, passing args as envrionments
    if ipy_path.parts[-5:-1] == __DEFAULT_MH_BIN_DIR__.parts[-4:]:
        command = [ipy_path, f"-script={script_path}"]
        for i, arg in enumerate(script_args):
            # One would better not specify environment MH_CONSOLE_ARGS_* from outside
            assert env.setdefault(f"MH_CONSOLE_ARGS_{i}", arg) == arg
        script_args = []
    else:
        command = [ipy_path, script_path, *script_args]

    if python_paths:
        env["PYTHONPATH"] = os.pathsep.join(
            [*python_paths, env.get("PYTHONPATH", "")]
        ).strip(os.pathsep)

    command = [str(c) for c in command]
    logger.debug(
        "\n".join(
            (
                f"--- Running IronPython Script ---",
                f"Executable: {ipy_path}",
                f"Script:     {script_path}",
                f"Arguments:  {script_args}",
                f"CWD:        {cwd}",
                f"Command:    {' '.join(command)}",
            )
        )
    )

    capture_args = {
        CaptureType.NONE: dict(),
        CaptureType.STDOUT: dict(stdout=subprocess.PIPE),
        CaptureType.STDERR: dict(stderr=subprocess.PIPE),
        CaptureType.BOTH: dict(stdout=subprocess.PIPE, stderr=subprocess.STDOUT),
        CaptureType.SEPERATE: dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE),
    }.get(capture_type, {})

    process = subprocess.run(
        command, cwd=cwd, env=env, text=True, check=False, **capture_args
    )

    result = (
        process.returncode,
        (process.stdout if "stdout" in capture_args else None),
        (process.stderr if "stderr" in capture_args else None),
    )

    logger.debug(
        "\n".join(
            (
                f"--- IronPython Output (stdout) ---",
                f"{result[1]}",
                f"--- IronPython Output (stderr) ---",
                f"{result[2]}",
                f"--- IronPython process finished with exit code: {result[0]} ---",
            )
        )
    )

    return result


import click


@click.command(help="Runs an IronPython script using the subprocess module.")
@click.argument(
    "script",
    type=str,
)
@click.argument(
    "script_args",
    nargs=-1,
)
@click.option(
    "--ipy",
    default="python2",
    type=str,
    help="Path to the IronPython executable (e.g., ipy.exe or /usr/bin/ipy).",
)
@click.option(
    "--cwd",
    default=Path(".").absolute(),
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    show_default=False,
    help="Working directory for the IronPython process.",
)
@click.option(
    "--python-path",
    type=click.Path(exists=True, resolve_path=True),
    default=[Path(".").absolute()],
    multiple=True,
    help="Additional paths to add to the IronPython environment's PYTHONPATH.",
)
@click.option(
    "--env",
    multiple=True,
    type=str,
    help="Additional envrionments",
)
@click.option(
    "--log-level",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR"], case_sensitive=False),
    default="INFO",
    help="Set the logging verbosity",
)
def main(
    script: str,
    ipy: Path = __DEFAULT_PY275_EXE__,
    cwd: Path | None = None,
    python_path: list[str] | None = None,
    env: list[str] | None = None,
    script_args: list[str] | None = None,
    log_level: str = "INFO",
):
    click.secho("Starting CLI execution...", fg="green")  # Use click.echo for output
    set_logger_level(log_level)
    is_temp_script = script == "-"

    if is_temp_script:
        with NamedTemporaryFile("w", suffix=".py", delete=False) as fp:
            fp.write(sys.stdin.read())
            script = fp.name

    try:
        returncode, _, _ = run_ironpython_script(
            ipy_path=ipy,
            script_path=Path(script),
            cwd=cwd,
            python_paths=python_path,
            extra_envs=env,
            script_args=script_args,
            capture_type=CaptureType.NONE,
        )

        if returncode == 0:
            click.secho(f"Processing completed successfully for {script}", fg="green")
        else:
            click.secho(
                f"Processing failed for {script} with return code {returncode}",
                fg="red",
                err=True,
            )
            raise click.Abort()
    finally:
        if is_temp_script:
            Path(script).unlink()


if __name__ == "__main__":
    main()
