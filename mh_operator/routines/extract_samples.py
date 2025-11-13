# type: ignore[attr-defined]
from typing import Annotated, Any, Dict, List, Optional

import base64
import json
import os
import sqlite3
from ast import literal_eval
from enum import Enum
from functools import cached_property, partial
from itertools import chain, cycle
from pathlib import Path

from pydantic import BaseModel, Field, TypeAdapter
from pydantic.dataclasses import dataclass

from mh_operator.utils.code_generator import function_to_string
from mh_operator.utils.common import logger
from mh_operator.utils.ironpython27 import (
    __DEFAULT_MH_BIN_DIR__,
    CaptureType,
    run_ironpython_script,
)


class ChromatogramSpectrumRecord(BaseModel):
    ScanID: int
    ScanMethodID: int
    # TimeSegmentID:int # seems to be always the same
    # CalibrationID:int # seems to be always the same
    # CycleNumber : int # seems to be the same as ScanID
    ScanTime: float
    ScanType: int
    TIC: float
    AbundanceLimit: float
    BasePeakAbundance: float
    CollisionEnergy: float
    FragmentorVoltage: float
    IonPolarity: int
    MassCalOffset: int
    MzOfInterest: float
    MZs: list[float]
    Abundances: list[float]


@dataclass
class ChromatogramSpectrum:
    Source: str
    Records: list[ChromatogramSpectrumRecord]


def extract_samples(
    samples: Annotated[
        list[Path],
        Field(
            description=f"The Mass Hunter tests (.D) to analysis",
        ),
    ],
    mh_bin_path: Annotated[
        Path,
        Field(
            description="The bin path of the installed Mass Hunter",
        ),
    ] = __DEFAULT_MH_BIN_DIR__,
) -> Annotated[
    list[ChromatogramSpectrum],
    Field(description="The Chromatogram and Spectrum data for all samples"),
]:
    samples = [str(s.absolute().resolve()) for s in samples]
    legacy_script = Path(__file__).parent.parent / "legacy" / "__init__.py"

    qc_exe = Path(mh_bin_path) / "QuantConsole.exe"
    assert Path(qc_exe).exists()

    @function_to_string(return_type="json", oneline=False)
    def _commands(
        _sample_paths: list[str],
    ) -> str:
        from mh_operator.legacy.QuantAnalysis import export_sample

        return [export_sample(sample) for sample in _sample_paths]

    commands = _commands(samples)
    logger.debug(f"use {legacy_script} to exec code '{commands}'")

    return_code, stdout, _ = run_ironpython_script(
        legacy_script,
        qc_exe,
        python_paths=[str(qc_exe.parent), str(Path(__file__).parent.parent / "..")],
        extra_envs=[
            f"MH_CONSOLE_COMMAND_STRING={commands}",
            f"MH_BIN_DIR={mh_bin_path}",
        ],
        capture_type=CaptureType.STDOUT,
    )
    if return_code != 0:
        logger.warning(f"QC return with {return_code}")

    try:
        *_, json_content = stdout.strip().rsplit("\n", maxsplit=1)
        return [
            ChromatogramSpectrum(
                Source=d,
                Records=[ChromatogramSpectrumRecord.model_validate(r) for r in data],
            )
            for d, data in zip(samples, json.loads(json_content))
        ]
    except (SyntaxError, AssertionError) as e:
        logger.info(f"QC return stdout:\n {stdout}")
        raise RuntimeError(f"Failed to exec code '{commands}': {e}")


def dump_chromatogram_spectrum(
    cs: ChromatogramSpectrum, *more: list[ChromatogramSpectrum], **kwargs
) -> bytes:
    if more:
        return TypeAdapter(list[ChromatogramSpectrum]).dump_json([cs, *more], **kwargs)
    else:
        return TypeAdapter(list[ChromatogramSpectrumRecord]).dump_json(
            cs.Records, **kwargs
        )
