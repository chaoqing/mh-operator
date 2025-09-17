# type: ignore[attr-defined]
import os
from pathlib import Path

from mh_operator.core.constants import SampleType
from mh_operator.utils.code_generator import function_to_string
from mh_operator.utils.common import logger
from mh_operator.utils.ironpython27 import (
    __DEFAULT_MH_BIN_DIR__,
    CaptureType,
    run_ironpython_script,
)


def analysis_samples(
    samples: list[str],
    analysis_method: Path,
    output: str,
    report_method: Path | None,
    istd_rt: float | None,
    istd_name: str | None,
    istd_value: float | None,
    mode: str,
    mh_bin_path: Path,
):
    """Analysis samples with Mass Hunter"""
    legacy_script = Path(__file__).parent.parent / "legacy" / "__init__.py"

    uac_exe = Path(mh_bin_path) / "UnknownsAnalysisII.Console.exe"
    assert Path(uac_exe).exists()

    def get_sample_info(s: str) -> tuple[str, str, dict[str, str]]:
        folder, name = os.path.split(s)
        name, *t = name.rsplit(":", maxsplit=1)
        t = SampleType(t[0]).name if t else SampleType.Sample.name
        return os.path.abspath(folder), name, {"type": t}

    samples_info = list(map(get_sample_info, samples))

    (batch_folder,) = {f for f, *_ in samples_info}
    analysis_file = Path(batch_folder) / "UnknownsResults" / output
    if mode == "x":
        assert not analysis_file.exists()
    elif mode == "w":
        logger.info(f"Cleaning existing analysis {analysis_file}")
        analysis_file.unlink(missing_ok=True)

    @function_to_string(return_type="none", oneline=False)
    def _commands(
        uaf_name: str,
        sample_paths: list[tuple[tuple, dict]],
        analysis_method: str,
        report_method: str | None = None,
        istd_params: dict | None = None,
    ):
        from mh_operator.legacy.common import global_state

        global_state.UADataAccess = UADataAccess
        from mh_operator.legacy.UnknownsAnalysis import ISTD, Sample, analysis_samples

        if istd_params is not None:
            istd = ISTD(**istd_params)
        else:
            istd = None

        analysis_samples(
            uaf_name,
            [Sample(*args, **kwargs) for args, kwargs in sample_paths],
            analysis_method,
            istd=istd,
            report_method=report_method,
        )

    if istd_rt is not None:
        assert (
            istd_name is not None and istd_value is not None
        ), "rt, name, and value must be all set for ISTD to work"
        istd_params = dict(
            istd_rt=istd_rt,
            istd_name=istd_name,
            istd_value=istd_value,
        )
    else:
        istd_params = None

    commands = _commands(
        output,
        [
            ((os.path.join(folder, name), *args), kwargs)
            for folder, name, *args, kwargs in samples_info
        ],
        str(Path(analysis_method).absolute()),
        report_method=(
            str(Path(report_method).absolute()) if report_method is not None else None
        ),
        istd_params=istd_params,
    )
    logger.debug(f"use {legacy_script} to exec code '{commands}'")

    returncode, _, _ = run_ironpython_script(
        legacy_script,
        uac_exe,
        python_paths=[str(uac_exe.parent), str(Path(__file__).parent.parent / "..")],
        extra_envs=[
            f"MH_CONSOLE_COMMAND_STRING={commands}",
            f"MH_BIN_DIR={mh_bin_path}",
        ],
        capture_type=CaptureType.NONE,
    )
    if returncode != 0:
        logger.info(f"UAC return with {returncode}")
