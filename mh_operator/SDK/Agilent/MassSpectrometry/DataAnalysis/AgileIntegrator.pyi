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

# Discovered Generic TypeVars:
T = TypeVar("T")
from . import IChromatogram, IChromPeak, IMsMsChromPeak, IPeakList

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator

class AgileConfig:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, timeSegments: List[float], smoothingKernelSize: int) -> None: ...
    @overload
    def __init__(
        self,
        timeSegments: List[float],
        smoothingKernelSize: int,
        resolvePeaksByShape: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeSegments: List[float],
        dataHasGaps: bool,
        smoothingKernelSize: int,
        resolvePeaksByShape: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeSegments: List[float],
        smoothingKernelSize: int,
        peakShape: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakShape,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeSegments: List[float],
        dataHasGaps: bool,
        smoothingKernelSize: int,
        peakShape: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakShape,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeSegments: List[float],
        smoothingKernelSize: int,
        peakShape: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakShape,
        noiseFactor2: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        timeSegments: List[float],
        smoothingKernelSize: int,
        peakShape: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakShape,
        noiseFactor2: float,
        keepEdgeApexInMedianFilter: bool,
    ) -> None: ...

    VERSION_1: int = ...  # static # readonly
    VERSION_2: int = ...  # static # readonly

    DataHasGaps: bool  # readonly
    KeepEdgeApexInMedianFilter: bool
    NoiseFactor2: float  # readonly
    PeakShape: (
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakShape
    )  # readonly
    ResolvePeaksByShape: bool  # readonly
    SmoothingKernelSize: int  # readonly
    TimeSegments: List[float]  # readonly
    Version: int  # readonly

class AgilePeakShape:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, peak: IChromPeak, chrom: IChromatogram) -> None: ...

    ApexIndex: int  # readonly
    FWHM: float  # readonly
    InterpolatedApexX: float  # readonly
    InterpolatedApexY: float  # readonly
    IsEquallySpaced: bool  # readonly
    PointCount: int  # readonly
    XArray: List[float]  # readonly
    XAverageStep: float  # readonly
    YArray: List[float]  # readonly

    @staticmethod
    def Base64ToDoubleArray(str: str) -> List[float]: ...
    def Parse(self, str: str) -> None: ...
    def DebugWrite(self, sw: System.IO.StreamWriter) -> None: ...
    def ToCsvString(self) -> str: ...
    def AlignApexAndInterpolateShape(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakShape: ...
    @staticmethod
    def DoubleArrayToBase64(dValues: List[float]) -> str: ...

class AgilePeakStatus(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    HeightProblem: (
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakStatus
    ) = ...  # static # readonly
    InterferenceProblem: (
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakStatus
    ) = ...  # static # readonly
    MergeProblem: (
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakStatus
    ) = ...  # static # readonly
    OK: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakStatus = (
        ...
    )  # static # readonly
    Spiky: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakStatus = (
        ...
    )  # static # readonly
    SymmetryProblem: (
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakStatus
    ) = ...  # static # readonly
    WidthProblem: (
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakStatus
    ) = ...  # static # readonly

class BaselineRegionInfo:  # Class
    End: int  # readonly
    LowestIndex: int  # readonly
    Merged: bool  # readonly
    Start: int  # readonly

class BaselineSegment:  # Class
    CenterX: float  # readonly
    End: int  # readonly
    HighestIndex: int  # readonly
    Index: int  # readonly
    IsOutlier: bool  # readonly
    Length: int  # readonly
    LowestIndex: int  # readonly
    MaxY: float  # readonly
    MinY: float  # readonly
    NRuns: int  # readonly
    Start: int  # readonly
    YMean: float  # readonly
    YVariance: float  # readonly

    def Contains(self, index: int) -> bool: ...
    def SetOutlier(self) -> None: ...

class CompatibleSort:  # Class
    @staticmethod
    def Sort40(
        list: System.Collections.Generic.List[T],
        comparer: System.Collections.Generic.IComparer[T],
    ) -> None: ...

class CompatibleSort40(Generic[T]):  # Class
    ...

class IPeakListProvider(object):  # Interface
    def SetBaselineOffset(self, peakList: IPeakList, baselineOffset: float) -> None: ...
    def SetSaturationFlag(self, peak: IMsMsChromPeak, saturated: bool) -> None: ...
    def MakeChromPeak(self) -> IMsMsChromPeak: ...
    def MakeChromPeakList(self) -> IPeakList: ...
    def SetBaselineStdDev(self, peakList: IPeakList, baselineStdDev: float) -> None: ...

class LocalIntegrator:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, config: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgileConfig
    ) -> None: ...

    AssumeNoisyTSBoundaries: bool  # static
    BaselineNoiseAmplitude: float  # readonly
    LeftTailingFactor: float  # static
    LowTailingFactor: float  # static
    NoiseAnalysis: (
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.NoiseAnalysis
    )  # readonly
    NoiseFactorSquared: float  # readonly
    PrettyTails: bool  # static
    ScaledBaselineNoiseAmplitude2: float  # readonly
    ScaledNoiseFactorSquared: float  # readonly
    TailingFactor: float  # static
    YMax: float  # readonly
    YMin: float  # readonly

    def GetBaselineSegments(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.BaselineSegment
    ]: ...
    def GetNoiseFactor(self, xArray: List[float], yArray: List[float]) -> float: ...
    @overload
    def SplitPeaks(
        self,
        xArray: List[float],
        yArray: List[float],
        peakListProvider: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.IPeakListProvider,
    ) -> IPeakList: ...
    @overload
    def SplitPeaks(
        self,
        xArray: List[float],
        yArray: List[float],
        timeSegments: List[float],
        smoothingKernelSize: int,
        peakListProvider: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.IPeakListProvider,
    ) -> IPeakList: ...
    @overload
    def FindPeaks(
        self,
        xArray: List[float],
        yArray: List[float],
        timeSegments: List[float],
        smoothingKernelSize: int,
        peakListProvider: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.IPeakListProvider,
    ) -> IPeakList: ...
    @overload
    def FindPeaks(
        self,
        xArray: List[float],
        yArray: List[float],
        config: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgileConfig,
        peakListProvider: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.IPeakListProvider,
    ) -> IPeakList: ...
    @overload
    def FindPeaks(
        self,
        xArray: List[float],
        yArray: List[float],
        timeSegments: List[float],
        smoothingKernelSize: int,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.Peak
    ]: ...
    @overload
    def FindPeaks(
        self,
        xArray: List[float],
        yArray: List[float],
        config: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgileConfig,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.Peak
    ]: ...

class MedianFilter:  # Class
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def Apply3PointFilter(signal: List[float]) -> None: ...
    @overload
    @staticmethod
    def Apply3PointFilter(signal: List[int]) -> None: ...
    @overload
    @staticmethod
    def Apply3PointFilter(signal: List[T]) -> None: ...
    @staticmethod
    def KeepMaxApexAtEdge(
        yInput: List[float], yFiltered: List[float], yMax: float
    ) -> None: ...
    @staticmethod
    def KeepEdgeApex(yInput: List[float], yFiltered: List[float]) -> None: ...

class NoiseAnalysis:  # Class
    Runs: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.Run
    ]  # readonly

    def FindRunByEndPosition(self, endPointIndex: int) -> int: ...
    def GetRunByIndex(
        self, runIndex: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.Run: ...

class Peak:  # Class
    AgilePeakStatus: (
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.AgilePeakStatus
    )  # readonly
    Apex: int  # readonly
    Area: float  # readonly
    Base1End: float  # readonly
    Base1Start: float  # readonly
    Base2End: float  # readonly
    Base2Start: float  # readonly
    BaselineSlope: float  # readonly
    CenterX: float  # readonly
    EndBaselineY: float  # readonly
    EndIndex: int  # readonly
    EndX: float  # readonly
    EndY: float  # readonly
    FullWidthHalfMaximum: float  # readonly
    Height: float  # readonly
    IsSaturated: bool  # readonly
    LeftBaselineRegion: (
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.BaselineRegionInfo
    )  # readonly
    LeftEdgeIndex: int  # readonly
    MaxY: float  # readonly
    RightBaselineRegion: (
        Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.BaselineRegionInfo
    )  # readonly
    RightEdgeIndex: int  # readonly
    StartBaselineY: float  # readonly
    StartIndex: int  # readonly
    StartX: float  # readonly
    StartY: float  # readonly
    Symmetry: float  # readonly
    YBaselineOffset: float  # readonly
    YIntercept: float  # readonly

    @overload
    @staticmethod
    def DoManualIntegration(
        manualPeak: IMsMsChromPeak,
        xArray: List[float],
        yArray: List[float],
        x1: float,
        x2: float,
        y1: float,
        y2: float,
        integrator: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.LocalIntegrator,
        peakListProvider: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.IPeakListProvider,
        peakList: IPeakList,
    ) -> None: ...
    @overload
    @staticmethod
    def DoManualIntegration(
        xArray: List[float],
        yArray: List[float],
        x1: float,
        x2: float,
        y1: float,
        y2: float,
        integrator: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.LocalIntegrator,
        peakListProvider: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.IPeakListProvider,
        peakList: IPeakList,
    ) -> IMsMsChromPeak: ...
    @overload
    @staticmethod
    def DoManualIntegration(
        xArray: List[float],
        yArray: List[float],
        x1: float,
        x2: float,
        y1: float,
        y2: float,
        integrator: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.LocalIntegrator,
        peakList: IPeakList,
    ) -> Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.Peak: ...
    def ConvertToChromPeak(self, chromPeak: IMsMsChromPeak) -> None: ...
    @staticmethod
    def UpdateMIBaselineRegions(
        xArray: List[float],
        yArray: List[float],
        x1: float,
        x2: float,
        y1: float,
        y2: float,
        manualPeak: IMsMsChromPeak,
        peakList: IPeakList,
    ) -> None: ...
    @staticmethod
    def ComputeChromatographicMetrics(
        xArray: List[float],
        yArray: List[float],
        startIndex: int,
        apexIndex: int,
        endIndex: int,
        baselineSlope: float,
        yIntercept: float,
        fullWidthHalfMaximum: float,
        symmetry: float,
    ) -> None: ...

class Run:  # Class
    End: int  # readonly
    Length: int  # readonly
    RunType: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.RunType  # readonly
    Start: int  # readonly
    YBottom: float  # readonly
    YDelta: float  # readonly
    YMidPoint: float  # readonly
    YTop: float  # readonly

class RunType(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Down: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.RunType = (
        ...
    )  # static # readonly
    Flat: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.RunType = (
        ...
    )  # static # readonly
    Up: Agilent.MassSpectrometry.DataAnalysis.AgileIntegrator.RunType = (
        ...
    )  # static # readonly
