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

from . import QuantChromSpecControl, QuantitationDataSet

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromSpecData

class CachedPeak:  # Class
    def __init__(self) -> None: ...

    Area: float  # readonly
    Base1End: Optional[float]
    Base1Start: Optional[float]
    Base2End: Optional[float]
    Base2Start: Optional[float]
    BaselineEndX: float  # readonly
    BaselineEndY: float  # readonly
    BaselineOffset: Optional[float]
    BaselineStandardDeviation: Optional[float]
    BaselineStartX: float  # readonly
    BaselineStartY: float  # readonly
    CalculatedConcentration: Optional[float]
    Center: float  # readonly
    CenterY: float  # readonly
    CompoundGroup: str
    CompoundName: str
    ConcentrationUnits: str
    ExpectedRetentionTime: Optional[float]  # readonly
    FinalConcentration: Optional[float]
    Height: float  # readonly
    IsPrimary: bool  # readonly
    ManualIntegrated: bool  # readonly
    PeakStatus: Agilent.MassSpectrometry.DataAnalysis.PeakStatus  # readonly
    QValueComputed: Optional[int]
    SignalToNoise: Optional[float]

    @overload
    def Initialize(
        self,
        fxData: Agilent.MassSpectrometry.DataAnalysis.IFXData,
        peak: Agilent.MassSpectrometry.DataAnalysis.IChromPeak,
        expectedRetentionTime: Optional[float],
        primary: bool,
        manualIntegrated: bool,
    ) -> bool: ...
    @overload
    def Initialize(
        self, peakRow: QuantitationDataSet.PeakRow, centerY: float
    ) -> bool: ...
    @overload
    def Initialize(
        self,
        peakRow: QuantitationDataSet.PeakQualifierRow,
        centerY: float,
        primary: bool,
    ) -> bool: ...
    def InitializeOriginal(
        self, sx: float, sy: float, ex: float, ey: float
    ) -> bool: ...

class CompoundMathChromData(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromSpecData.SeriesDataBase
):  # Class
    ...

class FXDataSeries(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromSpecData.SeriesDataBase
):  # Class
    @staticmethod
    def GetYFromX(
        data: Agilent.MassSpectrometry.DataAnalysis.IFXData, x: float
    ) -> float: ...

class PatternRefSpecData(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromSpecData.SeriesDataBase
):  # Class
    ...

class RefSpecData(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromSpecData.SeriesDataBase
):  # Class
    ...

class SeriesDataBase:  # Class
    ...

class SpecData(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromSpecData.FXDataSeries
):  # Class
    @staticmethod
    def GetFitToPeakMZRange(
        compoundRow: QuantitationDataSet.TargetCompoundRow,
        patternLibraryPath: str,
        control: QuantChromSpecControl,
        minMZ: Optional[float],
        maxMZ: Optional[float],
    ) -> None: ...
