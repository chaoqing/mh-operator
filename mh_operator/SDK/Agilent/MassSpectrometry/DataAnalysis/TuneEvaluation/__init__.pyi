# -*- coding: utf-8 -*-
import typing

# Import specific members from typing used in hints
from typing import (
    Any,
    Callable,
    Dict,
    FrozenSet,
    Generic,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    TypeVar,
    Union,
    overload,
)

import datetime
from enum import Enum

from mh_operator.SDK import Agilent, System

from . import UI, IChromatogram, IChromPeak, IDataAccess, IPSetExtractChrom, ISpectrum
from .Quantitative import Signal

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation

class AppException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class BackgroundSubtractionOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    BestScanWithinRange: (
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.BackgroundSubtractionOption
    ) = ...  # static # readonly
    Front: (
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.BackgroundSubtractionOption
    ) = ...  # static # readonly
    HigherOfTwoEnds: (
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.BackgroundSubtractionOption
    ) = ...  # static # readonly
    Rear: (
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.BackgroundSubtractionOption
    ) = ...  # static # readonly

class BreakdownCompound(
    Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.Compound
):  # Class
    def __init__(self) -> None: ...

    BreakdownLimit: float
    IsParentCompound: bool
    ParentCompoundName: str

class BreakdownCompoundResult(
    Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.CompoundResult
):  # Class
    def __init__(self) -> None: ...

    BreakdownLimit: float
    BreakdownPercentage: float
    TicArea: float

class Compound:  # Class
    def __init__(self) -> None: ...

    CompoundName: str
    DeltaRT: float
    ExpectedRT: float
    QualIons: List[float]
    QuantIon: float
    SignalInstance: str
    SignalName: str
    SignalType: str
    _QualIons: str

class CompoundResult:  # Class
    def __init__(self) -> None: ...

    CompoundName: str
    EICs: List[IChromatogram]
    ExpectedRT: float
    ObservedRT: float
    Pass: bool
    Signal: Signal
    Spectrum: ISpectrum
    TICPeak: IChromPeak

class CriteriaEntry:  # Class
    def __init__(self) -> None: ...

    AltBaseOK: bool
    RatioHigherLimit: float
    RatioLowerLimit: float
    RelToMass: float
    TargetMass: float

class ResultEntry:  # Class
    def __init__(self) -> None: ...

    Pass: bool
    RatioHigherLimit: float
    RatioLowerLimit: float
    RawAbundance: float
    RelAbundance: float
    RelToMass: float
    TargetMass: float

class SampleDataNavigator(System.IDisposable):  # Class
    def __init__(self, sampleDataDir: str) -> None: ...

    CurrentRT: float  # readonly
    DataAccess: IDataAccess  # readonly
    SampleDataDir: str  # readonly

    def GetAcquiredSignals(self) -> List[Signal]: ...
    def Dispose(self) -> None: ...
    @overload
    def GetTIC(self) -> System.Collections.Generic.List[IChromatogram]: ...
    @overload
    def GetTIC(self, signal: Signal) -> IChromatogram: ...

class SampleInfo:  # Class
    def __init__(self) -> None: ...

    AcqMethodPath: str
    AcqTime: System.DateTime
    Comment: str
    InstrumentName: str
    Mulitplier: str
    Operator: str
    SampleName: str
    Vial: str

class SampleInfoFile:  # Class
    def __init__(self, sampleFilePath: str) -> None: ...

    AcqDateTime: str
    AcqMethodPath: str
    Comment: str
    InstrumentName: str
    Multiplier: str
    OperatorName: str
    SampleName: str
    Vial: str

class SpectrumExtractionOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Apex: (
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.SpectrumExtractionOption
    ) = ...  # static # readonly
    AverageOfEntirePeak: (
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.SpectrumExtractionOption
    ) = ...  # static # readonly
    ThreeScanAverage: (
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.SpectrumExtractionOption
    ) = ...  # static # readonly

class TailingCompound(
    Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.Compound
):  # Class
    def __init__(self) -> None: ...

    TailingFactorLimit: float

class TailingCompoundResult(
    Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.CompoundResult
):  # Class
    def __init__(self) -> None: ...

    PeakGaussianFactor: float
    TailingFactor: float
    TailingLimit: float

class TuneEvaluationMethod:  # Class
    def __init__(self) -> None: ...

    SCHEMA_VERSION: int = ...  # static # readonly

    AltBaseMZ: float
    BackgroundScanOffsetLeft: int
    BackgroundScanOffsetRight: int
    BackgroundSubtractionOption: str
    BaseMZ: float
    Breakdown: bool
    BreakdownCompounds: List[
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.BreakdownCompound
    ]
    CriteriaEntries: List[
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.CriteriaEntry
    ]
    SchemaVersion: int
    SpectrumAutoEvaluation: bool
    SpectrumExtractionOption: str
    Tailing: bool
    TailingCompounds: List[
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.TailingCompound
    ]
    TuneCompound: str
    TuneEvaluation: bool

    @staticmethod
    def Load(
        path: str,
    ) -> Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.TuneEvaluationMethod: ...
    def Save(self, path: str) -> None: ...

class TuneEvaluationResult:  # Class
    def __init__(self) -> None: ...

    BackgroundSubtractUsed: str
    BreakdownResults: List[
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.BreakdownCompoundResult
    ]
    ResultEntries: List[
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.ResultEntry
    ]
    SampleInfo: Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.SampleInfo
    SamplePath: str
    Spectrum: ISpectrum
    SpectrumAutoEvaluation: bool
    SpectrumExtractionUsed: str
    TailingResults: List[
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.TailingCompoundResult
    ]

    @staticmethod
    def Load(
        path: str,
    ) -> Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.TuneEvaluationResult: ...
    def Save(self, path: str) -> None: ...

class TuneEvaluator:  # Class
    def __init__(
        self,
        samplePath: str,
        method: Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.TuneEvaluationMethod,
    ) -> None: ...

    MZEXTRACTIONWINDOW_LEFT: float = ...  # static # readonly
    MZEXTRACTIONWINDOW_RIGHT: float = ...  # static # readonly

    def Evaluate(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.TuneEvaluationResult: ...
    def GetPSetForTotalSignal(self, signal: Signal) -> IPSetExtractChrom: ...
