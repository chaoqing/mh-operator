from typing import List, Optional, Tuple

import os
import subprocess
import sys
from collections.abc import Iterable
from enum import Enum, auto
from pathlib import Path
from tempfile import NamedTemporaryFile

from ..legacy.common import __DEFAULT_MH_BIN_DIR__ as _DEFAULT_MH_BIN_DIR
from .common import logger, set_logger_level

# fmt: off
__DEFAULT_MH_BIN_DIR__ = Path(_DEFAULT_MH_BIN_DIR)
__DEFAULT_PY275_EXE__ = Path("C:/") / "Program Files (x86)" / "IronPython 2.7" / "ipy.exe"
# fmt: on


def get_absolute_executable_path(
    interpreter: Path,
    cwd: Path | None = None,
) -> Path:
    exe_path = Path(interpreter)

    if exe_path.exists():
        logger.debug("direct found executable")
        return exe_path.absolute()
    if (
        cwd is not None
        and not exe_path.is_absolute()
        and (Path(cwd) / interpreter).exists()
    ):
        logger.debug("found executable under relative path")
        return (Path(cwd) / interpreter).absolute()

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
    }
    # fmt: on
    exe_path = alias.get(str(interpreter), None)
    if exe_path is not None and exe_path.exists():
        logger.debug("found executable with alias")
        return exe_path
    raise SystemError(f"Error: IronPython executable not found at '{interpreter}'")


class CaptureType(Enum):
    NONE = auto()
    STDOUT = auto()
    STDERR = auto()
    BOTH = auto()
    SEPERATE = auto()


def run_ironpython_script(
    script_path: Path,
    interpreter: Path = __DEFAULT_PY275_EXE__,
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
        interpreter (Path): Path to the IronPython-like executable (e.g., ipy.exe).
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
    script_abs_path = str(Path(script_path).absolute())
    if not Path(interpreter).exists():
        raise SystemError(f"Error: IronPython interpreter not found at '{interpreter}'")
    interpreter_abs_path = str(Path(interpreter).absolute())

    # relative executable path can be infered by specified cwd when not found under current directory
    cwd = Path("." if cwd is None else cwd).absolute()
    assert Path(cwd).is_dir()

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
    if interpreter.parts[-5:-1] == __DEFAULT_MH_BIN_DIR__.parts[-4:]:
        command = [interpreter_abs_path, f"-script={script_abs_path}"]
        assert env.setdefault(f"MH_CONSOLE_ARGS_0", script_abs_path) == script_abs_path
        for i, arg in enumerate(script_args):
            # One would better not specify environment MH_CONSOLE_ARGS_* from outside
            assert env.setdefault(f"MH_CONSOLE_ARGS_{i+1}", arg) == arg
        script_args = []
    else:
        command = [interpreter_abs_path, script_abs_path, *script_args]

    if python_paths:
        env["PYTHONPATH"] = os.pathsep.join(
            [*python_paths, env.get("PYTHONPATH", "")]
        ).strip(os.pathsep)

    command = [str(c) for c in command]
    logger.debug(
        "\n".join(
            (
                f"--- Running IronPython Script ---",
                f"Executable: {interpreter_abs_path}",
                f"Script:     {script_abs_path}",
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


@click.command()
@click.argument(
    "script_args",
    type=str,
    nargs=-1,
)
@click.option(
    "--command",
    help="The temporary script contents, the first arg will no longer be treated as script pass.",
)
@click.option(
    "--interpreter",
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
    script_args: list[str],
    command: str | None = None,
    interpreter: Path = __DEFAULT_PY275_EXE__,
    cwd: Path | None = None,
    python_path: list[str] | None = None,
    env: list[str] | None = None,
    log_level: str = "INFO",
):
    """Runs an IronPython script using the subprocess module.
    Command text must be provided or the first argument will be treated as the script path.
    Script path `-` will be read from stdin.

    Example:

        shebang --interpreter LEC --command "import sys; print sys.version"

        shebang - <<< "import sys; print sys.version"
    """
    set_logger_level(log_level)

    if command is None and script_args:
        script, *script_args = script_args
    else:
        script = "-"

    is_temp_script = script == "-"

    if is_temp_script:
        with NamedTemporaryFile("w", suffix=".py", delete=False) as fp:
            script = fp.name
            if command is None:
                click.secho(
                    f"Reading from stdin into {script}",
                    fg="green",
                )
                fp.write(sys.stdin.read())
            else:
                fp.write(command)

    try:
        returncode, _, _ = run_ironpython_script(
            interpreter=get_absolute_executable_path(interpreter, cwd),
            script_path=Path(script),
            cwd=cwd,
            python_paths=python_path,
            extra_envs=env,
            script_args=script_args,
            capture_type=CaptureType.NONE,
        )

        if returncode != 0:
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
