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

from . import Component, IonPolarity, IRange, MSScanType, RangeCollection
from .AgileIntegrator import Peak
from .Quantitative import (
    ChromatographyType,
    IFeature,
    ITimeToMassConversion,
    ScanRecord,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.FD

class Apex:  # Class
    @overload
    def __init__(
        self,
        xApexIndex: int,
        yApexIndex: int,
        xAxis: Agilent.MassSpectrometry.DataAnalysis.FD.IAxisGrid,
        y: List[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        xApexIndex: int,
        yApexIndex: int,
        xAxis: Agilent.MassSpectrometry.DataAnalysis.FD.IAxisGrid,
        y: System.Collections.Generic.List[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        xApexIndex: int,
        yApexIndex: int,
        xAxis: Agilent.MassSpectrometry.DataAnalysis.FD.IAxisGrid,
        y1: int,
        y2: int,
        y3: int,
    ) -> None: ...

    Index: int  # readonly
    InterpolatedX: float  # readonly
    InterpolatedY: float  # readonly
    IsInterpolated: bool  # readonly
    X: float  # readonly
    Y: float  # readonly

    @staticmethod
    def DoParabolicFit(
        x1: float,
        x2: float,
        x3: float,
        y1: float,
        y2: float,
        y3: float,
        a0: float,
        a1: float,
        a2: float,
    ) -> bool: ...

class CentroidType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    GC_2GHzData: Agilent.MassSpectrometry.DataAnalysis.FD.CentroidType = (
        ...
    )  # static # readonly
    GC_4GHzData: Agilent.MassSpectrometry.DataAnalysis.FD.CentroidType = (
        ...
    )  # static # readonly
    LC_2GHzData: Agilent.MassSpectrometry.DataAnalysis.FD.CentroidType = (
        ...
    )  # static # readonly
    LC_4GHzData: Agilent.MassSpectrometry.DataAnalysis.FD.CentroidType = (
        ...
    )  # static # readonly

class DoubleRange:  # Class
    def __init__(self, min: float, max: float) -> None: ...

    Center: float  # readonly
    Max: float  # readonly
    Min: float  # readonly
    Width: float  # readonly

    def Overlaps(
        self, range: Agilent.MassSpectrometry.DataAnalysis.FD.DoubleRange
    ) -> bool: ...
    def Contains(self, value_: float) -> bool: ...

class Feature(IFeature):  # Class
    @overload
    def __init__(
        self, scanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace
    ) -> None: ...
    @overload
    def __init__(
        self,
        ridge: Agilent.MassSpectrometry.DataAnalysis.FD.Ridge,
        peak: Peak,
        fd: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetector,
    ) -> None: ...
    @overload
    def __init__(
        self,
        ridge: Agilent.MassSpectrometry.DataAnalysis.FD.Ridge,
        peakFinderRangeStartOffset: int,
        peak: Peak,
        fd: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetector,
    ) -> None: ...
    @overload
    def __init__(
        self,
        ridge: Agilent.MassSpectrometry.DataAnalysis.FD.Ridge,
        peakFinderRangeStartOffset: int,
        peak: Peak,
        fd: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetector,
        manuallyIntegratedFeature: bool,
    ) -> None: ...

    Abundance: List[float]  # readonly
    ApexInterpolatedMz: float  # readonly
    ApexOffset: int  # readonly
    ApexPointIndex: int  # readonly
    ApexScanIndex: int  # readonly
    Area: float  # readonly
    AssignedFlightTime: float  # readonly
    AssignedMz: float  # readonly
    AssignedRT: float  # readonly
    AssignedScanAxisLocation: float  # readonly
    BaselineEnd: float  # readonly
    BaselineSlope: float  # readonly
    BaselineStart: float  # readonly
    BaselineYIntercept: float  # readonly
    CentroidMz: float  # readonly
    EndX: float  # readonly
    FWHM: float  # readonly
    FWHMPoints: float  # readonly
    FeatureID: int  # readonly
    FirstSaturatedScanIndex: int  # readonly
    FirstScanIndex: int  # readonly
    FlightTimeVariation: float  # readonly
    HasUnsaturatedPoints: bool  # readonly
    Height: float  # readonly
    InterpolatedApexAbundance: float  # readonly
    IsRestored: bool  # readonly
    IsSaturated: bool  # readonly
    LastSaturatedScanIndex: int  # readonly
    LastScanIndex: int  # readonly
    LeftBaselineEnd: float  # readonly
    LeftBaselineStart: float  # readonly
    Length: int  # readonly
    Noise: float  # readonly
    RestoredAbundance: List[float]  # readonly
    RestoredArea: float  # readonly
    RestoredHeight: float  # readonly
    RidgeID: int  # readonly
    RightBaselineEnd: float  # readonly
    RightBaselineStart: float  # readonly
    SaturatedRegionCount: int  # readonly
    SaturatedScanCount: int  # readonly
    SaturationRecoveryStatus: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedFeatureRecoveryStatus
    )  # readonly
    ScanAxisPeakLocations: List[float]  # readonly
    ScanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace  # readonly
    SignalToNoise: float  # readonly
    StartX: float  # readonly
    Symmetry: float  # readonly

    def Read(self, br: System.IO.BinaryReader, version: int) -> None: ...
    @overload
    def FitTo(
        self,
        f: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        yOffset: float,
        yScale: float,
    ) -> None: ...
    @overload
    def FitTo(
        self,
        f: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        yOffset: float,
        slope: float,
        yScale: float,
    ) -> None: ...
    def Write(self, bw: System.IO.BinaryWriter) -> None: ...
    def ApplyRecoveryResult(
        self,
        recovery: Agilent.MassSpectrometry.DataAnalysis.FD.SaturationRecoveryResult,
    ) -> None: ...
    def ApplyDynamicMassCalibration(self, recalibratedMz: float) -> None: ...
    def DebugWrite(self, sw: System.IO.StreamWriter) -> None: ...
    def RestoreDefaultMassCalibration(self) -> None: ...
    def RecoverSaturatedAbundance(
        self,
        template: Agilent.MassSpectrometry.DataAnalysis.FD.SaturationRecoveryTemplate,
        fd: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetector,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.SaturationRecoveryResult: ...

    # Nested Types

    class ApexComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
            b: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        ) -> int: ...

    class FlightTimeComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
            b: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        ) -> int: ...

    class MzComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
            b: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        ) -> int: ...

    class RTComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
            b: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        ) -> int: ...

    class ReverseAbundanceComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
            b: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        ) -> int: ...

    class ReverseHeightComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
            b: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        ) -> int: ...

    class ReverseLengthComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
            b: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        ) -> int: ...

    class ReverseSaturatedScanCountComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
            b: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        ) -> int: ...

class FeatureDetectionCompleted(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self, sender: Any, callback: System.AsyncCallback, object: Any
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any) -> None: ...

class FeatureDetectionParams:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, xmlFilePath: str) -> None: ...
    @overload
    def __init__(
        self, other: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams
    ) -> None: ...

    PARAMETER_FILE: str = ...  # static # readonly

    ApplyRingFilter: bool
    EnablePhase1Recovery: bool
    EnablePhase2Recovery: bool
    FeatureSmoothingMaxSNR: float
    MassAssignmentType2GHz: Agilent.MassSpectrometry.DataAnalysis.FD.MassAssignmentType
    MassAssignmentType4GHz: Agilent.MassSpectrometry.DataAnalysis.FD.MassAssignmentType
    MinFeatureSNR: float
    MinFitPointsForX100Recovery: int
    MinFitPointsForX10Recovery: int
    MinLeftUnsaturatedPoints: int
    MinRightUnsaturatedPoints: int
    MinTotalUnsaturatedPoints: int
    RemovePrecursor: bool
    RemoveTrailer: bool
    SaturationRecovery: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturationRecoveryTemplateType
    )
    SmoothingGaussianWidthInPoints: int
    SmoothingType: Agilent.MassSpectrometry.DataAnalysis.FD.SmoothingType

    def Equals(
        self, other: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams
    ) -> bool: ...
    def Clone(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams: ...

class FeatureDetectionStarted(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self, sender: Any, callback: System.AsyncCallback, object: Any
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any) -> None: ...

class FeatureDetector:  # Class
    def __init__(
        self,
        scanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace,
        spectrumDataAccess: Agilent.MassSpectrometry.DataAnalysis.FD.SpectrumDataAccess,
        fdParams: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams,
    ) -> None: ...

    ScanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace  # readonly
    UseComponentBasedSaturationRecovery: bool  # readonly

    def GetMassCal(self, scanIndex: int) -> ITimeToMassConversion: ...
    def RecoverSaturatedFeatures(
        self,
        featureSet: Agilent.MassSpectrometry.DataAnalysis.FD.IFeatureSet,
        components: System.Collections.Generic.List[Component],
    ) -> None: ...
    def ApplyRingFilter(
        self,
        detectedFeatures: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ],
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    def DetectFeaturesInRidges(
        self,
        ridgeSet: Agilent.MassSpectrometry.DataAnalysis.FD.IRidgeSet,
        featureSet: Agilent.MassSpectrometry.DataAnalysis.FD.IFeatureSet,
    ) -> None: ...

class GaussianSmoothingKernel:  # Class
    @overload
    def __init__(self, widthInPoints: int) -> None: ...
    @overload
    def __init__(self, sigma: float) -> None: ...
    @overload
    def __init__(self, sigma: float, npts: int) -> None: ...
    def Smooth(self, data: List[float]) -> List[float]: ...

class IAxisGrid(object):  # Interface
    PointCount: int  # readonly

    def GetIndexOfNearestPointAbove(self, value_: float) -> int: ...
    def GetPointByIndex(self, index: int) -> float: ...
    def GetIndexOfNearestPointBelow(self, value_: float) -> int: ...
    def GetIndexOfNearestPoint(self, value_: float) -> int: ...

class IFeatureSet(
    Agilent.MassSpectrometry.DataAnalysis.FD.IFeatureSetQuery
):  # Interface
    FeatureDetectionParams: (
        Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams
    )  # readonly
    ScanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace  # readonly

    def Add(self, f: Agilent.MassSpectrometry.DataAnalysis.FD.Feature) -> None: ...

class IFeatureSetQuery(object):  # Interface
    Count: int  # readonly
    SaturatedCount: int  # readonly

    @overload
    def GetFeatures(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    @overload
    def GetFeatures(
        self, minScanIndex: int, maxScanIndex: int
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    @overload
    def GetFeatures(
        self, rtStart: float, rtEnd: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    def GetCoelutingFeatures(
        self, apexScanIndex: int
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    @overload
    def GetFeaturesInRange(
        self, minScanIndex: int, maxScanIndex: int, mzLow: float, mzHigh: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    @overload
    def GetFeaturesInRange(
        self, rtStart: float, rtEnd: float, mzLow: float, mzHigh: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    def GetFeatureByID(
        self, featureID: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.Feature: ...
    def GetFeaturesInFlightTimeRange(
        self, rtStart: float, rtEnd: float, lowFlightTime: float, highFlightTime: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    def GetFeaturesInMzRange(
        self, mzLow: float, mzHigh: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...

class IProcessedSpectrum(object):  # Interface
    ApexList: List[int]  # readonly
    ApexMap: List[int]  # readonly
    FilteredApexList: System.Collections.Generic.List[int]  # readonly
    IsSaturated: bool  # readonly
    NoiseStatistics: (
        Agilent.MassSpectrometry.DataAnalysis.FD.ISpectrumNoiseStatistics
    )  # readonly
    PartialSaturationThreshold: int  # readonly
    PeakFinder: (
        Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrumPeakFinder
    )  # readonly
    ProfileSpectrum: (
        Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrum
    )  # readonly
    SaturatedRanges: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedRange
    ]  # readonly

    def IsApexAbovePartialSaturatedThreshold(self, apexIndex: int) -> bool: ...
    def FindStartOfPeak(self, apexIndex: int) -> int: ...
    def SortApexListByAbundance(self) -> List[int]: ...

class IProfileSpectrum(System.IDisposable):  # Interface
    CycleNumber: int  # readonly
    IntAbundanceArray: List[int]  # readonly
    IsTimeOfFlightSpectrum: bool  # readonly
    PointCount: int  # readonly
    SaturationLimit: int  # readonly
    ScanID: int  # readonly
    ScanIndex: int  # readonly
    ScanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace  # readonly
    TimeToMassConversion: ITimeToMassConversion  # readonly

    def ReleaseSpectrumAbundanceValues(self) -> None: ...

class IProfileSpectrumPeakFinder(object):  # Interface
    def GetSaturatedRanges(
        self,
        abundance: List[int],
        saturationThreshold: int,
        fullSaturationThreshold: int,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedRange
    ]: ...
    @overload
    def GetApexList(
        self, spectrum: Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrum
    ) -> List[int]: ...
    @overload
    def GetApexList(
        self,
        spectrum: Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrum,
        threshold: int,
    ) -> List[int]: ...
    @overload
    def GetApexList(self, abundance: List[int]) -> List[int]: ...
    @overload
    def GetApexList(self, abundance: List[int], threshold: int) -> List[int]: ...

class IRidgeSet(object):  # Interface
    Count: int  # readonly
    NoiseFactor2: float  # readonly
    RidgeDetectionParams: (
        Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionParams
    )  # readonly
    RidgeList: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Ridge
    ]  # readonly
    SaturationLimit: float  # readonly
    ScanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace  # readonly

    @overload
    def GetRidgesInRange(
        self, rtMin: float, rtMax: float, mzMin: float, mzMax: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Ridge
    ]: ...
    @overload
    def GetRidgesInRange(
        self, minScanIndex: int, maxScanIndex: int, mzMin: float, mzMax: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Ridge
    ]: ...
    def GetRidgeByID(
        self, ridgeId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.Ridge: ...

class ISampleFeatures(object):  # Interface
    ScanConditionCount: int  # readonly
    ScanConditionList: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    ]  # readonly

    def GetFeatureSet(
        self, scanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.IFeatureSet: ...
    def GetScanSpace(
        self, scanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace: ...
    def CreateFeatureSet(
        self,
        scanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace,
        fdParams: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.IFeatureSet: ...
    def GetFeatureSets(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.IFeatureSet
    ]: ...
    def AddFeatureSet(
        self,
        scanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace,
        featureSet: Agilent.MassSpectrometry.DataAnalysis.FD.IFeatureSet,
    ) -> None: ...

class ISampleRidges(object):  # Interface
    ScanConditionCount: int  # readonly
    ScanConditionList: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    ]  # readonly

    def AddRidgeSet(
        self,
        scanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace,
        ridgeSet: Agilent.MassSpectrometry.DataAnalysis.FD.IRidgeSet,
    ) -> None: ...
    def GetScanSpace(
        self, scanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace: ...
    def GetRidgeSets(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.IRidgeSet
    ]: ...
    def GetRidgeSet(
        self, scanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.IRidgeSet: ...
    def AddDetectedRidgeSet(
        self, rd: Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetector
    ) -> None: ...

class IScanSpace(object):  # Interface
    IsOpen: bool  # readonly
    RTAxis: Agilent.MassSpectrometry.DataAnalysis.FD.RTAxis  # readonly
    ScanAxis: Agilent.MassSpectrometry.DataAnalysis.FD.ScanAxis  # readonly
    ScanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions  # readonly

class ISpectrumNoiseStatistics(object):  # Interface
    NoiseBaseline: int  # readonly
    NoiseDeviation: int  # readonly
    NoiseMultiplier: int
    NoiseSignalThreshold: int  # readonly

class IntRange:  # Class
    def __init__(self, min: int, max: int) -> None: ...

    Max: int  # readonly
    Min: int  # readonly
    NumberOfPoints: int  # readonly

    @overload
    def Overlaps(
        self, range: Agilent.MassSpectrometry.DataAnalysis.FD.IntRange
    ) -> bool: ...
    @overload
    def Overlaps(self, min: int, max: int) -> bool: ...
    def Contains(self, value_: int) -> bool: ...
    @overload
    def GetOverlap(
        self, range: Agilent.MassSpectrometry.DataAnalysis.FD.IntRange
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.IntRange: ...
    @overload
    def GetOverlap(
        self, start: int, end: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.IntRange: ...

class InterferenceDetector:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def ComputeFlightTimeVariation(
        f: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
    ) -> float: ...

class MassAssignmentType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ApexInterpolated: Agilent.MassSpectrometry.DataAnalysis.FD.MassAssignmentType = (
        ...
    )  # static # readonly
    Centroid: Agilent.MassSpectrometry.DataAnalysis.FD.MassAssignmentType = (
        ...
    )  # static # readonly
    CentroidBiasCorrected: (
        Agilent.MassSpectrometry.DataAnalysis.FD.MassAssignmentType
    ) = ...  # static # readonly
    MzDependentCentroidBiasCorrected: (
        Agilent.MassSpectrometry.DataAnalysis.FD.MassAssignmentType
    ) = ...  # static # readonly

class ProcessedSpectrum(
    Agilent.MassSpectrometry.DataAnalysis.FD.IProcessedSpectrum
):  # Class
    def __init__(
        self,
        spectrum: Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrum,
        peakFinder: Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrumPeakFinder,
        chromType: ChromatographyType,
    ) -> None: ...
    @staticmethod
    def FilterSortedApexList(
        abundance: List[int], apexList: List[int], abundanceThreshold: int
    ) -> System.Collections.Generic.List[int]: ...
    def FilterApexListBySpacing(
        self,
        pointCount: int,
        apexList: System.Collections.Generic.List[int],
        minApexSpacing: int,
        maxAbundance: int,
    ) -> System.Collections.Generic.List[int]: ...
    @staticmethod
    def FilterApexList(
        abundance: List[int], apexList: List[int], abundanceThreshold: int
    ) -> System.Collections.Generic.List[int]: ...

class ProfileSpectrum(
    Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrum, System.IDisposable
):  # Class
    @overload
    def __init__(self, scanRecord: ScanRecord) -> None: ...
    @overload
    def __init__(
        self, scanRecord: ScanRecord, timeToMass: ITimeToMassConversion
    ) -> None: ...
    @overload
    def __init__(
        self,
        scanRecord: ScanRecord,
        useRunTimeMassCal: bool,
        timeToMass: ITimeToMassConversion,
    ) -> None: ...

    CycleNumber: int  # readonly
    IntAbundanceArray: List[int]  # readonly
    IsTimeOfFlightSpectrum: bool  # readonly
    PointCount: int  # readonly
    SaturationLimit: int  # readonly
    ScanID: int  # readonly
    ScanIndex: int  # readonly
    ScanRecord: ScanRecord  # readonly
    ScanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace  # readonly
    TimeToMassConversion: ITimeToMassConversion  # readonly

    def ReleaseSpectrumAbundanceValues(self) -> None: ...
    def Dispose(self) -> None: ...

class ProfileSpectrumPeakFinder(
    Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrumPeakFinder
):  # Class
    def __init__(self) -> None: ...
    def GetSaturatedRanges(
        self,
        abundance: List[int],
        saturationThreshold: int,
        fullSaturationThreshold: int,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedRange
    ]: ...
    def GetApexSpacingHistogram(self, apexList: List[int]) -> List[int]: ...
    @overload
    def GetApexList(
        self, spectrum: Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrum
    ) -> List[int]: ...
    @overload
    def GetApexList(
        self,
        spectrum: Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrum,
        threshold: int,
    ) -> List[int]: ...
    @overload
    def GetApexList(self, abundance: List[int]) -> List[int]: ...
    @overload
    def GetApexList(self, abundance: List[int], noiseThreshold: int) -> List[int]: ...

class RTAxis(Agilent.MassSpectrometry.DataAnalysis.FD.IAxisGrid):  # Class
    @overload
    def __init__(
        self,
        scanIDs: System.Collections.Generic.List[int],
        cycleNumbers: System.Collections.Generic.List[int],
        scanTimes: System.Collections.Generic.List[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        scanIdArray: List[int],
        cycleNumberArray: List[int],
        scanTimeArray: List[float],
    ) -> None: ...

    CycleNumberArray: List[int]  # readonly
    GridStep: float  # readonly
    PointCount: int  # readonly
    ScanIDArray: List[int]  # readonly
    ScanTimeArray: List[float]  # readonly

    def GetIndexOfNearestPointAbove(self, value_: float) -> int: ...
    def GetPointByIndex(self, index: int) -> float: ...
    def GetIndexOfNearestPoint(self, value_: float) -> int: ...
    def GetCycleNumberByIndex(self, index: int) -> int: ...
    def GetScanIDByIndex(self, index: int) -> int: ...
    def GetScanTimeRange(self, firstScanIndex: int, nPoints: int) -> List[float]: ...
    def GetIndexOfNearestPointBelow(self, value_: float) -> int: ...
    def GetCycleNumberRange(self, firstScanIndex: int, nPoints: int) -> List[int]: ...

class Ridge:  # Class
    def __init__(
        self, scanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace
    ) -> None: ...

    ComputedNoise: float  # readonly
    FirstScanIndex: int  # readonly
    HasCentroidFlightTimeInfo: bool  # readonly
    IsSaturated: bool  # readonly
    LastScanIndex: int  # readonly
    Length: int  # readonly
    LengthExPrecursorAndTrailer: int  # readonly
    MaxAbundancePointIndex: int  # readonly
    MaxPointIndex: int  # readonly
    MinPointIndex: int  # readonly
    NoiseFactor2: float  # readonly
    PrecursorLength: int  # readonly
    RidgeID: int  # readonly
    ScanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace  # readonly
    TrailerLength: int  # readonly

    def Read(self, br: System.IO.BinaryReader) -> None: ...
    def Write(self, bw: System.IO.BinaryWriter) -> None: ...
    def GetFlightTimeRange(self, startOffset: int, nPoints: int) -> List[float]: ...
    def GetCentroidFlightTime(self, offsetFromRidgeStart: int) -> float: ...
    def Overlaps(
        self, other: Agilent.MassSpectrometry.DataAnalysis.FD.Ridge
    ) -> bool: ...
    def GetFlightTime(self, offsetFromRidgeStart: int) -> float: ...
    def GetCentroidFlightTimeRange(
        self, startOffset: int, nPoints: int
    ) -> List[float]: ...
    @overload
    def FindPeaks(
        self, fd: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetector
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    @overload
    def FindPeaks(
        self,
        fd: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetector,
        smoothingKernel: Agilent.MassSpectrometry.DataAnalysis.FD.GaussianSmoothingKernel,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    def IsSaturatedAtScan(self, scanIndex: int) -> bool: ...
    def GetAbundance(self, offsetFromRidgeStart: int) -> float: ...
    def GetApexIndex(self, offsetFromRidgeStart: int) -> int: ...
    def GetAbundanceRange(self, startOffset: int, nPoints: int) -> List[float]: ...
    def ComputeQuartileBasedSignificanceRatio(self) -> float: ...
    def GetSaturatedRange(
        self, scanIndex: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedRange: ...

    # Nested Types

    class LengthComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FD.Ridge
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FD.Ridge,
            b: Agilent.MassSpectrometry.DataAnalysis.FD.Ridge,
        ) -> int: ...

class RidgeDetectionCancelled(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self, sender: Any, callback: System.AsyncCallback, object: Any
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any) -> None: ...

class RidgeDetectionCompleted(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self, sender: Any, callback: System.AsyncCallback, object: Any
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any) -> None: ...

class RidgeDetectionParams:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, xmlFilePath: str) -> None: ...
    @overload
    def __init__(
        self, other: Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionParams
    ) -> None: ...

    PARAMETER_FILE: str = ...  # static # readonly

    ExtendedRange: bool
    MinDynamicRangeInNoiseUnits: float
    MinDynamicRangeInNoiseUnitsLC: float
    MinPrecursorLength: int
    MinRidgeLength: int
    MinTrailerLength: int
    NSlicesToSearch: int
    RidgeMapType: Agilent.MassSpectrometry.DataAnalysis.FD.RidgeMappingType
    ScanModeOnly: bool

    def Equals(
        self, other: Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionParams
    ) -> bool: ...
    def Clone(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionParams: ...

class RidgeDetectionStarted(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        nScanRecords: int,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, nScanRecords: int) -> None: ...

class RidgeDetectionStepDone(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        scanRecordIndex: int,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, scanRecordIndex: int) -> None: ...

class RidgeDetector(System.IDisposable):  # Class
    def __init__(
        self,
        scanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace,
        fd: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetector,
        rdParams: Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionParams,
    ) -> None: ...

    FeatureDetector: (
        Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetector
    )  # readonly
    NoiseFactor2: float  # readonly
    RidgeDetectionParams: (
        Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionParams
    )  # readonly
    RidgeList: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Ridge
    ]  # readonly
    SaturationLimit: float  # readonly
    ScanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace  # readonly

    def KeepOnlyRidgesWithFeatures(
        self,
        features: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ],
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Ridge
    ]: ...
    def CompleteRidgeDetection(self) -> None: ...
    def DebugWriteRidgeStats(
        self,
        features: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ],
    ) -> None: ...
    @staticmethod
    def GetRidgeLengthHistogram(
        ridges: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.FD.Ridge
        ],
        nBins: int,
    ) -> List[int]: ...
    def ProcessSpectrum(
        self, spectrum: Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrum
    ) -> None: ...
    def Dispose(self) -> None: ...

class RidgeMappingType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Latest: Agilent.MassSpectrometry.DataAnalysis.FD.RidgeMappingType = (
        ...
    )  # static # readonly
    LatestOverMax: Agilent.MassSpectrometry.DataAnalysis.FD.RidgeMappingType = (
        ...
    )  # static # readonly
    MaxAbundance: Agilent.MassSpectrometry.DataAnalysis.FD.RidgeMappingType = (
        ...
    )  # static # readonly
    MaxOverLatest: Agilent.MassSpectrometry.DataAnalysis.FD.RidgeMappingType = (
        ...
    )  # static # readonly

class SampleFeatureDetector:  # Class
    @overload
    def __init__(self, sampleDataPath: str) -> None: ...
    @overload
    def __init__(
        self,
        sampleDataPath: str,
        rdParams: Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionParams,
        fdParams: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams,
    ) -> None: ...

    DefaultMassCal: ITimeToMassConversion  # readonly
    FeatureDetectionParams: (
        Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams
    )  # readonly
    IsRidgeDetectionCancelled: bool  # readonly
    RidgeDetectionParams: (
        Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionParams
    )  # readonly

    def CancelRidgeDetection(self) -> None: ...
    def GetSpectrumDataAccessForMassCal(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.SpectrumDataAccess: ...
    def GetRidgeDetector(
        self, scanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetector: ...
    def DetectFeaturesInRidges(
        self,
        sampleRidges: Agilent.MassSpectrometry.DataAnalysis.FD.ISampleRidges,
        sampleFeatures: Agilent.MassSpectrometry.DataAnalysis.FD.ISampleFeatures,
    ) -> None: ...
    def GetFeatureDetector(
        self, scanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetector: ...
    def DetectRidges(
        self, sampleRidges: Agilent.MassSpectrometry.DataAnalysis.FD.ISampleRidges
    ) -> bool: ...
    def OnRidgeDetectionCancelled(self) -> None: ...

    FeatureDetectionCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionCompleted
    )  # Event
    FeatureDetectionStarted: (
        Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionStarted
    )  # Event
    RidgeDetectionCancelled: (
        Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionCancelled
    )  # Event
    RidgeDetectionCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionCompleted
    )  # Event
    RidgeDetectionStarted: (
        Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionStarted
    )  # Event
    RidgeDetectionStepDone: (
        Agilent.MassSpectrometry.DataAnalysis.FD.RidgeDetectionStepDone
    )  # Event

class SaturatedFeatureRecoveryStatus(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Bootstrapped: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedFeatureRecoveryStatus
    ) = ...  # static # readonly
    Cancelled: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedFeatureRecoveryStatus
    ) = ...  # static # readonly
    CrossSample: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedFeatureRecoveryStatus
    ) = ...  # static # readonly
    HighRSD: Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedFeatureRecoveryStatus = (
        ...
    )  # static # readonly
    InvalidStatus: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedFeatureRecoveryStatus
    ) = ...  # static # readonly
    NonSmoothTemplate: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedFeatureRecoveryStatus
    ) = ...  # static # readonly
    Normal: Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedFeatureRecoveryStatus = (
        ...
    )  # static # readonly

class SaturatedRange:  # Class
    @overload
    def __init__(
        self,
        abundance: List[int],
        satThreshold: float,
        pointRange: Agilent.MassSpectrometry.DataAnalysis.FD.IntRange,
        apexPointIndex: int,
        maxAbundance: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        pointRange: Agilent.MassSpectrometry.DataAnalysis.FD.IntRange,
        xRange: Agilent.MassSpectrometry.DataAnalysis.FD.DoubleRange,
        apexPointIndex: int,
        maxAbundance: int,
    ) -> None: ...

    ApexPointIndex: int  # readonly
    InterpolatedRange: Agilent.MassSpectrometry.DataAnalysis.FD.DoubleRange  # readonly
    MaxAbundance: int  # readonly
    PointRange: Agilent.MassSpectrometry.DataAnalysis.FD.IntRange  # readonly

    def Overlaps(self, minPtIndex: int, maxPtIndex: int) -> bool: ...
    def Contains(self, pointIndex: int) -> bool: ...

class SaturationRecoveryRequest:  # Class
    @overload
    def __init__(
        self,
        satFeature: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        templateCandidateFeatures: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ],
        fdParams: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams,
    ) -> None: ...
    @overload
    def __init__(
        self,
        satFeature: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        templateFeature: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
        templateScaleFactor: float,
        fdParams: Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams,
    ) -> None: ...

    FeatureDetectionParams: (
        Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams
    )  # readonly
    IsCrossSampleRecovery: bool  # readonly
    SaturatedFeature: Agilent.MassSpectrometry.DataAnalysis.FD.Feature  # readonly
    TemplateCandidateFeatures: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]  # readonly
    TemplateScaleFactor: float  # readonly

class SaturationRecoveryResult:  # Class
    IsSuccessful: bool  # readonly
    RestoredAbundance: List[float]  # readonly
    RestoredApexOffset: int  # readonly
    Template: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturationRecoveryTemplate
    )  # readonly

class SaturationRecoveryTemplate:  # Class
    def __init__(
        self,
        req: Agilent.MassSpectrometry.DataAnalysis.FD.SaturationRecoveryRequest,
        useIsotopesOnly: bool,
        allowKinks: bool,
        useSaturatedFeatures: bool,
        minFrontPoints: int,
        minTailPoints: int,
    ) -> None: ...

    ApexScanOffset: int  # readonly
    EndScanIndex: int  # readonly
    FeatureCount: int  # readonly
    FeatureDetectionParams: (
        Agilent.MassSpectrometry.DataAnalysis.FD.FeatureDetectionParams
    )  # readonly
    FitRSD: float  # readonly
    FitYOffset: float  # readonly
    FitYScale: float  # readonly
    IsotopeCount: int  # readonly
    Length: int  # readonly
    NumberOfFitPoints: int  # readonly
    Request: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturationRecoveryRequest
    )  # readonly
    SatFeature: Agilent.MassSpectrometry.DataAnalysis.FD.Feature  # readonly
    StartScanIndex: int  # readonly
    Status: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturatedFeatureRecoveryStatus
    )  # readonly
    TotalIsotopeCount: int  # readonly

class SaturationRecoveryTemplateType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    All: Agilent.MassSpectrometry.DataAnalysis.FD.SaturationRecoveryTemplateType = (
        ...
    )  # static # readonly
    ComponentBased: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturationRecoveryTemplateType
    ) = ...  # static # readonly
    IsotopesOnly: (
        Agilent.MassSpectrometry.DataAnalysis.FD.SaturationRecoveryTemplateType
    ) = ...  # static # readonly

class ScanAxis(Agilent.MassSpectrometry.DataAnalysis.FD.IAxisGrid):  # Class
    def __init__(self, xArray: List[float]) -> None: ...

    Is2GHzData: bool  # readonly
    IsMass: bool  # readonly
    PointCount: int  # readonly
    XArray: List[float]  # readonly
    XStart: float  # readonly
    XStep: float  # readonly

    def GetIndexOfNearestPointAbove(self, value_: float) -> int: ...
    def GetPointByIndex(self, index: int) -> float: ...
    def GetIndexOfNearestPointBelow(self, value_: float) -> int: ...
    def GetIndexOfNearestPoint(self, value_: float) -> int: ...

class ScanConditions(
    System.IEquatable[Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions]
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, scanRecord: ScanRecord) -> None: ...
    @overload
    def __init__(
        self, scanType: MSScanType, polarity: IonPolarity, mzOfInterest: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        scanType: MSScanType,
        polarity: IonPolarity,
        mzOfInterest: float,
        collisionEnergy: float,
        fragmentorVoltage: float,
    ) -> None: ...

    CollisionEnergy: float  # readonly
    FragmentorVoltage: float  # readonly
    IonPolarity: IonPolarity  # readonly
    MzOfInterest: float  # readonly
    ScanAxis: Agilent.MassSpectrometry.DataAnalysis.FD.ScanAxis  # readonly
    ScanType: MSScanType  # readonly

    @staticmethod
    def Read(
        br: System.IO.BinaryReader, readCEFV: bool
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions: ...
    def Equals(
        self, other: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    ) -> bool: ...
    def OverlapsFragmentorVoltageRange(self, fvRange: IRange) -> bool: ...
    def OverlapsPolarityFilter(self, polarityFilter: IonPolarity) -> bool: ...
    def Write(self, bw: System.IO.BinaryWriter) -> None: ...
    def ConsistentWith(self, scanRecord: ScanRecord) -> bool: ...
    @overload
    def OverlapsMzOfInterestRange(self, mzOfInterestRange: IRange) -> bool: ...
    @overload
    def OverlapsMzOfInterestRange(
        self, mzOfInterestRanges: RangeCollection
    ) -> bool: ...
    def OverlapsCollisionEnergyRange(self, ceRange: IRange) -> bool: ...
    def OverlapsScanTypeFilter(self, scanTypeFilter: MSScanType) -> bool: ...
    def ToString(self) -> str: ...

class ScanSpace(Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace):  # Class
    def __init__(
        self,
        scanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions,
        rtAxis: Agilent.MassSpectrometry.DataAnalysis.FD.RTAxis,
        scanAxis: Agilent.MassSpectrometry.DataAnalysis.FD.ScanAxis,
        nScans: int,
    ) -> None: ...

    IsNull: bool  # readonly
    IsOpen: bool  # readonly
    RTAxis: Agilent.MassSpectrometry.DataAnalysis.FD.RTAxis  # readonly
    ScanAxis: Agilent.MassSpectrometry.DataAnalysis.FD.ScanAxis  # readonly
    ScanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions  # readonly

    @staticmethod
    def Read(
        scanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions,
        br: System.IO.BinaryReader,
        readCycleNumbers: bool,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace: ...
    @staticmethod
    def Write(
        scanSpace: Agilent.MassSpectrometry.DataAnalysis.FD.IScanSpace,
        bw: System.IO.BinaryWriter,
    ) -> None: ...

class SmoothingType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    SmoothFeatures: Agilent.MassSpectrometry.DataAnalysis.FD.SmoothingType = (
        ...
    )  # static # readonly
    SmoothRidges: Agilent.MassSpectrometry.DataAnalysis.FD.SmoothingType = (
        ...
    )  # static # readonly

class SpectrumApex:  # Class
    @overload
    def __init__(
        self,
        xApexIndex: int,
        xAxis: Agilent.MassSpectrometry.DataAnalysis.FD.ScanAxis,
        y: List[int],
    ) -> None: ...
    @overload
    def __init__(
        self,
        xApexIndex: int,
        xAxis: Agilent.MassSpectrometry.DataAnalysis.FD.ScanAxis,
        y: List[int],
        centroidType: Agilent.MassSpectrometry.DataAnalysis.FD.CentroidType,
    ) -> None: ...

    CentroidType: Agilent.MassSpectrometry.DataAnalysis.FD.CentroidType  # readonly
    CentroidX: float  # readonly
    Index: int  # readonly
    InterpolatedX: float  # readonly
    InterpolatedY: float  # readonly
    IsInterpolated: bool  # readonly
    Y: int  # readonly

    @staticmethod
    def MedianFilter(a0: float, a1: float, a2: float) -> float: ...
    @overload
    @staticmethod
    def DoParabolicFit(
        x1: float,
        x2: float,
        x3: float,
        y1: float,
        y2: float,
        y3: float,
        a0: float,
        a1: float,
        a2: float,
    ) -> bool: ...
    @overload
    @staticmethod
    def DoParabolicFit(
        apexIndex: int, y1: int, y2: int, y3: int, a0: float, a1: float, a2: float
    ) -> bool: ...

class SpectrumDataAccess:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, scanModeOnly: bool) -> None: ...

    DefaultMassCal: ITimeToMassConversion  # readonly
    GotProfileData: bool  # readonly
    IsOpen: bool  # readonly
    IsTofData: bool  # readonly
    SampleDataPath: str  # readonly
    ScanRecordCount: int  # readonly

    def Open(self, sampleDataPath: str) -> None: ...
    def GetTimeToMassConversion(self, scanIndex: int) -> ITimeToMassConversion: ...
    def GetProfileSpectrum(
        self, scanNumber: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.IProfileSpectrum: ...
    def Close(self) -> None: ...
    @staticmethod
    def GetDefaultMassCal(sampleDataPath: str) -> ITimeToMassConversion: ...
