# type: ignore[attr-defined]
from typing import Annotated, List, Optional

import os
from ast import literal_eval
from enum import Enum
from functools import cached_property
from pathlib import Path

from pydantic import Field
from pydantic.dataclasses import dataclass

from mh_operator.core.constants import SampleType
from mh_operator.utils.code_generator import function_to_string
from mh_operator.utils.common import logger
from mh_operator.utils.ironpython27 import (
    __DEFAULT_MH_BIN_DIR__,
    CaptureType,
    run_ironpython_script,
)


@dataclass
class ISTDOptions:
    rt: float = Field(
        description="The ISTD compound retention time (min.)",
    )
    name: str = Field(
        description="The ISTD compound name",
    )
    value: float = Field(
        description="The ISTD compound concentration",
    )

    @cached_property
    def valid(self) -> bool:
        if any(v is not None for v in self.__dict__.values()):
            assert not any(
                v is None for v in self.__dict__.values()
            ), "rt, name, and value must be all set for ISTD to work"
            return True
        return False


@dataclass
class SampleInfo:
    path: Path = Field(description="The path of the Mass Hunter test .D")
    type: SampleType = Field(
        default=SampleType.Sample, description="The sample type of the test"
    )

    @cached_property
    def name(self):
        _, name = os.path.split(self.path)
        return name

    @cached_property
    def parent(self):
        folder, _ = os.path.split(os.path.abspath(self.path))
        return folder

    @staticmethod
    def from_cli(s: str) -> "SampleInfo":
        folder, name = os.path.split(s)
        name, *t = name.rsplit(":", maxsplit=1)
        return SampleInfo(
            path=os.path.join(folder, name),
            type=SampleType(t[0]) if t else SampleType.Sample,
        )

    def to_legacy(self) -> tuple[str, str, dict[str, str]]:
        return self.parent, self.name, {"type": self.type.name}


class FileOpenMode(str, Enum):
    """The mode while open the analysis file:
    - x/c/create: create new uaf file, raise error when uaf already exist;
    - w/write: create new uaf file, old uaf removed at first;
    - a/append: append to old uaf file, create new one if not exist;
    """

    CREATE = "create"
    WRITE = "write"
    APPEND = "append"


def analysis_samples(
    samples: Annotated[
        List[SampleInfo],
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
    istd: Annotated[
        Optional[ISTDOptions], Field(description="The ISTD options")
    ] = None,
    mode: Annotated[
        FileOpenMode, Field(description="The mode while open the analysis file")
    ] = FileOpenMode.WRITE,
    mh_bin_path: Annotated[
        Path,
        Field(
            description="The bin path of the installed Mass Hunter",
        ),
    ] = __DEFAULT_MH_BIN_DIR__,
) -> Annotated[
    Path, Field(description="The exported json file path of the generated UAF file")
]:
    """Analysis samples with Mass Hunter"""
    legacy_script = Path(__file__).parent.parent / "legacy" / "__init__.py"

    uac_exe = Path(mh_bin_path) / "UnknownsAnalysisII.Console.exe"
    assert Path(uac_exe).exists()

    samples_info = [s.to_legacy() for s in samples]
    (batch_folder,) = {f for f, *_ in samples_info}

    analysis_file = Path(batch_folder) / "UnknownsResults" / output
    if mode == FileOpenMode.CREATE:
        assert not analysis_file.exists()
    elif mode == FileOpenMode.WRITE:
        logger.info(f"Cleaning existing analysis {analysis_file}")
        analysis_file.unlink(missing_ok=True)

    @function_to_string(return_type="repr", oneline=False)
    def _commands(
        _uaf_name: str,
        _sample_paths: list[tuple[tuple, dict]],
        _analysis_method: str,
        _report_method: str | None = None,
        _istd_params: dict | None = None,
    ) -> str:
        from mh_operator.legacy.common import global_state

        global_state.UADataAccess = UADataAccess
        from mh_operator.legacy.UnknownsAnalysis import ISTD, Sample, analysis_samples

        if _istd_params is not None:
            _istd = ISTD(**_istd_params)
        else:
            _istd = None

        return analysis_samples(
            _uaf_name,
            [Sample(*args, **kwargs) for args, kwargs in _sample_paths],
            _analysis_method,
            istd=_istd,
            report_method=_report_method,
        )

    if istd is not None and istd.valid:
        istd_params = dict(
            istd_rt=istd.rt,
            istd_name=istd.name,
            istd_value=istd.value,
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
        _report_method=(
            str(Path(report_method).absolute()) if report_method is not None else None
        ),
        _istd_params=istd_params,
    )
    logger.debug(f"use {legacy_script} to exec code '{commands}'")

    return_code, stdout, _ = run_ironpython_script(
        legacy_script,
        uac_exe,
        python_paths=[str(uac_exe.parent), str(Path(__file__).parent.parent / "..")],
        extra_envs=[
            f"MH_CONSOLE_COMMAND_STRING={commands}",
            f"MH_BIN_DIR={mh_bin_path}",
        ],
        capture_type=CaptureType.STDOUT,
    )
    if return_code != 0:
        logger.warning(f"UAC return with {return_code}")

    try:
        *_, uaf_json_path = stdout.strip().rsplit("\n", maxsplit=1)
        uaf_json_path = Path(literal_eval(uaf_json_path))
        assert uaf_json_path.exists()
        return uaf_json_path
    except (SyntaxError, AssertionError) as e:
        logger.info(f"UAC return stdout:\n {stdout}")
        raise RuntimeError(f"Failed to exec code '{commands}': {e}")
