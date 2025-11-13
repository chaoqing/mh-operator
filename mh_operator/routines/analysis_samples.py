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
        list[SampleInfo],
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
        Path | None,
        Field(
            description="The Mass Hunter report method path (.m)",
        ),
    ] = None,
    istd: Annotated[ISTDOptions | None, Field(description="The ISTD options")] = None,
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


SAMPLE_META_FIELDS = "".join(
    f"'{f}', s.{f}, "
    for f in [
        "BatchID",
        "SampleID",
        "SampleName",
        "AcqDateTime",
        "DataFileName",
        "AcqMethodFileName",
        "AcqOperator",
        "Comment",
        "Dilution",
        "InstrumentName",
        "PlateCode",
        "PlatePosition",
        "RackCode",
        "RackPosition",
        "Vial",
        "SamplePosition",
        "SampleType",
        "TuneFileName",
        "TuneFileLastTimeStamp",
    ]
).rstrip(", ")

UAF_JSON_MERGE_SQL_COMMAND = f"""
WITH
    -- 1. Aggregate Ion Peaks for each Component
    ion_peaks_agg AS (SELECT BatchID,
                             SampleID,
                             DeconvolutionMethodID,
                             ComponentID,
                             JSON_GROUP_ARRAY(
                                     JSON_OBJECT(
                                             'MZ', MZ,
                                             'Area', Area,
                                             'Height', Height,
                                             'RetentionTime', RetentionTime,
                                             'StartX', StartX,
                                             'EndX', EndX,
                                             'Symmetry', Symmetry,
                                             'FullWidthHalfMaximum', FullWidthHalfMaximum,
                                             'IonPolarity', IonPolarity,
                                             'Sharpness', Sharpness,
                                             'SignalToNoiseRatio', SignalToNoiseRatio,
                                             'B64Encoded_RetentionTimeSeries', XArray,
                                             'B64Encoded_RetentionTimeAbundances', YArray
                                     ) -- ORDER BY MZ
                             ) AS peaks_json
                      FROM (SELECT * FROM IonPeak ORDER BY MZ)
                      GROUP BY BatchID,
                               SampleID,
                               DeconvolutionMethodID,
                               ComponentID),

    -- 2. Aggregate Library Search Hits (Candidates) for each Component
    hit_agg AS (SELECT BatchID,
                       SampleID,
                       DeconvolutionMethodID,
                       ComponentID,
                       JSON_GROUP_ARRAY(
                               JSON_OBJECT(
                                       'HitID', HitID,
                                       'LibraryEntryID', LibraryEntryID,
                                       'LibraryMatchScore', LibraryMatchScore,
                                       'LibraryCompoundDescription', LibraryCompoundDescription,
                                       'CompoundName', CompoundName,
                                       'EstimatedConcentration', EstimatedConcentration,
                                       'CASNumber', CASNumber,
                                       'Formula', Formula,
                                       'MolecularWeight', MolecularWeight
                               ) -- ORDER BY LibraryMatchScore DESC
                       ) AS candidates_json
                FROM (SELECT * FROM Hit ORDER BY LibraryMatchScore DESC)
                GROUP BY BatchID,
                         SampleID,
                         DeconvolutionMethodID,
                         ComponentID),

    -- 3. Build Component JSON objects, joining aggregated peaks and hits,
    --    AND joining again to get the Primary Hit's details
    component_json AS (SELECT c.BatchID,
                              c.SampleID,
                              c.PrimaryHitID AS HitID,
                              c.RetentionTime,
                              JSON_OBJECT(
                                      'RetentionTime', c.RetentionTime,
                                      'StartX', c.StartX,
                                      'EndX', c.EndX,
                                      'ShapeQuality', c.ShapeQuality,
                                      'IsAccurateMass', c.IsAccurateMass,
                                      'Area', c.Area,
                                      'Height', c.Height,
                                      'LibraryEntryID', COALESCE(primary_hit.LibraryEntryID, NULL),
                                      'CompoundName', COALESCE(primary_hit.CompoundName, 'Unknown'),
                                      'CASNumber', COALESCE(primary_hit.CASNumber, 'N/A'),
                                      'Formula', COALESCE(primary_hit.Formula, 'N/A'),
                                      'LibraryMatchScore', COALESCE(primary_hit.LibraryMatchScore, NULL),
                                      'EstimatedConcentration', COALESCE(primary_hit.EstimatedConcentration, NULL),
                                      'LibraryCompoundDescription', COALESCE(primary_hit.LibraryCompoundDescription, ''),
                                      'IsManuallyIntegrated', c.IsManuallyIntegrated,
                                      'B64Encoded_RetentionTimeSeries', c.XArray,
                                      'B64Encoded_RetentionTimeAbundances', c.YArray,
                                      'B64Encoded_SpectrumMZs', c.SpectrumMZs,
                                      'B64Encoded_SpectrumAbundances', c.SpectrumAbundances,
                                      -- Use COALESCE with JSON() to handle potential NULLs from LEFT JOIN and ensure valid JSON array
                                      'LibraryCandidates', COALESCE(JSON(ha.candidates_json), JSON_ARRAY()),
                                      'IonPeaks', COALESCE(JSON(ipa.peaks_json), JSON_ARRAY())
                              ) AS component_data
                       FROM Component c
                                LEFT JOIN Hit primary_hit -- Join specifically to get the primary hit details
                                          ON c.BatchID = primary_hit.BatchID
                                              AND c.SampleID = primary_hit.SampleID
                                              AND c.DeconvolutionMethodID = primary_hit.DeconvolutionMethodID
                                              AND c.ComponentID = primary_hit.ComponentID
                                              AND c.PrimaryHitID = primary_hit.HitID -- Link via PrimaryHitID
                                LEFT JOIN hit_agg ha -- Join pre-aggregated hits
                                          ON c.BatchID = ha.BatchID
                                              AND c.SampleID = ha.SampleID
                                              AND c.DeconvolutionMethodID = ha.DeconvolutionMethodID
                                              AND c.ComponentID = ha.ComponentID
                                LEFT JOIN ion_peaks_agg ipa -- Join pre-aggregated ion peaks
                                          ON c.BatchID = ipa.BatchID
                                              AND c.SampleID = ipa.SampleID
                                              AND c.DeconvolutionMethodID = ipa.DeconvolutionMethodID
                                              AND c.ComponentID = ipa.ComponentID
                       WHERE c.BestHit = 1),

    -- 4. Aggregate all Component JSON objects for each Sample
    sample_components_agg AS (SELECT BatchID,
                                     SampleID,
                                     JSON_GROUP_ARRAY(component_data -- ORDER BY JSON_EXTRACT(component_data, '$.RetentionTime')
                                     ) AS components_json
                              FROM (SELECT * FROM component_json ORDER BY RetentionTime)
                              GROUP BY BatchID,
                                       SampleID)

-- 5. Final Select: Combine Sample info with aggregated Components array
SELECT JSON_OBJECT({SAMPLE_META_FIELDS}, 
                   'JSONEncoded_Components', COALESCE(JSON(sca.components_json), JSON_ARRAY())
           ) AS JSONEncoded
FROM Sample s
         LEFT JOIN sample_components_agg sca
                   ON s.BatchID = sca.BatchID
                       AND s.SampleID = sca.SampleID
;"""  # nosec

UAF_JSON_MERGE_META_SQL_COMMAND = f"""
SELECT JSON_OBJECT({SAMPLE_META_FIELDS}, 
                   'JSONEncoded_Components', JSON_ARRAY()
           ) AS JSONEncoded
FROM Sample s
;"""  # nosec


def recursive_decoding(dct: dict[str, Any], b64decode=True) -> dict[str, Any]:
    """
    An object_hook for json.loads that handles B64Encoded_* and JSONEncoded_* keys.
    """
    processed_dct = {}

    for key, value in dct.items():
        # --- Handle Base64 Encoded Fields ---
        if b64decode and key.startswith("B64Encoded_"):
            import numpy as np

            processed_dct[key[len("B64Encoded_") :]] = np.frombuffer(
                base64.b64decode(value), dtype=np.float64
            ).tolist()
        # --- Handle JSON Encoded Fields ---
        elif key.startswith("JSONEncoded_"):
            processed_dct[key[len("JSONEncoded_") :]] = [
                json.loads(
                    v, object_hook=partial(recursive_decoding, b64decode=b64decode)
                )
                for v in value
            ]
        else:
            processed_dct[key] = value

    return processed_dct


def merge_uaf_tables(
    uaf_json: dict,
    *more_uaf_jsons,
    tmp_db: str | Path = ":memory:",
    b64decode: bool = False,
) -> list:
    """merge the raw exported uaf_json_path into one"""
    tables_iter = chain.from_iterable(
        zip(cycle([batch]), j.items())
        for batch, j in enumerate([uaf_json, *more_uaf_jsons])
    )
    with sqlite3.connect(tmp_db) as conn:

        for batch, (table_name, contents) in tables_iter:
            if not contents:
                continue
            try:
                import pandas as pd

                table = pd.DataFrame(contents)  # dropna(axis="columns", how="all")
                import numpy as np

                assert "BatchID" not in table or np.all(table["BatchID"] == 0)
                table["BatchID"] = batch

                table.to_sql(table_name, conn, index=False, if_exists="append")
            except ImportError:
                raise NotImplementedError(
                    "merging without database support is pending development"
                )

        check_table_exist = (
            "SELECT name FROM sqlite_master WHERE type='table' AND name='{}'"
        )
        components_exist = (
            conn.execute(check_table_exist.format("Component")).fetchone() is not None
        )

        return [
            json.loads(r, object_hook=partial(recursive_decoding, b64decode=b64decode))
            for r, in conn.cursor()
            .execute(
                UAF_JSON_MERGE_SQL_COMMAND
                if components_exist
                else UAF_JSON_MERGE_META_SQL_COMMAND
            )
            .fetchall()
        ]
