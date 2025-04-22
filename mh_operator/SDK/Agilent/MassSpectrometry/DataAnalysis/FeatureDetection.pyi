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

from . import Component
from .Quantitative.IndexedData import ScanSpace

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection

class DropoutState(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DropoutLeft: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.DropoutState = (
        ...
    )  # static # readonly
    DropoutRecovered: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.DropoutState
    ) = ...  # static # readonly
    DropoutRight: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.DropoutState
    ) = ...  # static # readonly
    Normal: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.DropoutState = (
        ...
    )  # static # readonly

class Feature:  # Class
    @overload
    def __init__(
        self,
        featureID: int,
        scanSpace: ScanSpace,
        firstScanIndex: int,
        apexMzIndex: int,
        shape: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.FeatureShape,
        mergeState: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.MergeState,
        dropoutState: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.DropoutState,
    ) -> None: ...
    @overload
    def __init__(
        self,
        featureID: int,
        scanSpace: ScanSpace,
        firstScanIndex: int,
        apexMzIndex: int,
        shape: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.FeatureShape,
        restoredShape: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.FeatureShape,
        mergeState: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.MergeState,
        dropoutState: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.DropoutState,
    ) -> None: ...

    ApexMzIndex: int  # readonly
    ApexScanIndex: int  # readonly
    ApexSegment: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment
    )  # readonly
    Baseline: int  # readonly
    DropoutState: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.DropoutState
    )  # readonly
    FeatureID: int  # readonly
    FirstScanIndex: int  # readonly
    FirstSegment: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment
    )  # readonly
    Height: int  # readonly
    IsAssigned: bool  # readonly
    IsDropout: bool  # readonly
    IsMerged: bool  # readonly
    IsSaturated: bool  # readonly
    LastScanIndex: int  # readonly
    LastSegment: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment
    )  # readonly
    MZ: float  # readonly
    MaxAbundance: int  # readonly
    MergeState: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.MergeState
    )  # readonly
    RT: float  # readonly
    RestoredShape: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.FeatureShape
    )  # readonly
    SaturationState: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SaturationState
    )  # readonly
    ScanCount: int  # readonly
    ScanSpace: ScanSpace  # readonly
    SegmentCount: int  # readonly
    Shape: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.FeatureShape
    )  # readonly

    # Nested Types

    class HeightComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature,
            b: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature,
        ) -> int: ...

    class MzIndexComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature,
            b: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature,
        ) -> int: ...

class FeatureDetector:  # Class
    def __init__(self, scanSpace: ScanSpace) -> None: ...

    NoiseModel: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.NoiseModel
    )  # readonly
    ScanSpace: ScanSpace  # readonly

    def GetFeatureByID(
        self, featureID: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature: ...
    def UpdateFeatures(
        self, components: System.Collections.Generic.List[Component]
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
    ]: ...
    def FindFeatures(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
    ]: ...
    def GetFeatures(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
    ]: ...

class FeatureGroup:  # Class
    def __init__(
        self,
        f1: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature,
        f2: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature,
    ) -> None: ...

    AssignedRT: float  # readonly
    Count: int  # readonly
    LargestFeature: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
    )  # readonly

    def GetSpectrum(self, mzValues: List[float], abundances: List[float]) -> None: ...
    def AddFeature(
        self, feature: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
    ) -> None: ...

    # Nested Types

    class XComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.FeatureGroup
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.FeatureGroup,
            b: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.FeatureGroup,
        ) -> int: ...

class FeatureShape:  # Class
    @overload
    def __init__(
        self,
        abundance: List[int],
        apexOffset: int,
        interpolatedX: float,
        interpolatedY: float,
        sharpness: float,
        width: float,
        asymmetry: float,
        snr: float,
        flatTop: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        f: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature,
        abundance: List[int],
        noiseModel: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.NoiseModel,
    ) -> None: ...

    AbundanceProfile: List[int]  # readonly
    ApexAbundance: int  # readonly
    ApexOffset: int  # readonly
    Asymmetry: float  # readonly
    Baseline: int  # readonly
    FirstAbundance: int  # readonly
    FlatEndOffset: int  # readonly
    FlatExtent: int  # readonly
    FlatStartOffset: int  # readonly
    InterpolatedX: float  # readonly
    InterpolatedY: float  # readonly
    IsFlatTop: bool  # readonly
    LastAbundance: int  # readonly
    Length: int  # readonly
    SNR: float  # readonly
    Sharpness: float  # readonly
    Width: float  # readonly

    @staticmethod
    def DoParabolicFit(
        index: int, y1: float, y2: float, y3: float, a0: float, a1: float, a2: float
    ) -> bool: ...
    def FitTo(
        self,
        u: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.FeatureShape,
        yOffset: float,
        yScale: float,
    ) -> None: ...

class GaussianRandomSample:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, seed: int) -> None: ...
    def Next(self) -> float: ...

class MergeState(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Merged: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.MergeState = (
        ...
    )  # static # readonly
    Residual: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.MergeState = (
        ...
    )  # static # readonly
    Shoulder: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.MergeState = (
        ...
    )  # static # readonly
    Unmerged: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.MergeState = (
        ...
    )  # static # readonly

class NoiseModel:  # Class
    def __init__(self) -> None: ...

    NoiseFactor2: int  # readonly

    def AddNoiseBlip(
        self, blip: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment
    ) -> None: ...
    def GetNoiseEstimate(self, abundanceLevel: float) -> float: ...
    def ComputeNoiseStats(self) -> bool: ...
    def IsSignificantDelta(self, aDelta: int, baselineAbundance: int) -> bool: ...

class ProtoComponent:  # Class
    def __init__(self, scanSpace: ScanSpace, _apexIndex: int) -> None: ...

    ApexCycleIndex: int  # readonly
    FeatureCount: int  # readonly
    Height: int  # readonly
    HighestFeature: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
    )  # readonly
    LongestFeature: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
    )  # readonly
    RetentionTime: float  # readonly

    def ContainsMz(self, mz: int) -> bool: ...
    def GetMzList(self) -> System.Collections.Generic.List[int]: ...
    def GetSpectrum(self, mzValues: List[float], abundances: List[float]) -> None: ...
    def GetFeatureByMz(
        self, mz: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature: ...
    def ApplyFilter(self, relHeightThreshold: float, minPoints: int) -> None: ...
    def GetFeatureList(
        self, sortByHeight: bool
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
    ]: ...
    def GetUnsaturatedAbundanceProfile(self, startScanIndex: int) -> List[float]: ...
    def AddFeature(
        self, feature: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature
    ) -> None: ...

    # Nested Types

    class HeightComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.ProtoComponent
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.ProtoComponent,
            b: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.ProtoComponent,
        ) -> int: ...

class SaturationState(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Saturated: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SaturationState
    ) = ...  # static # readonly
    Unsaturated: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SaturationState
    ) = ...  # static # readonly

class SegmentType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    FallingEdge: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SegmentType = (
        ...
    )  # static # readonly
    Flat: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SegmentType = (
        ...
    )  # static # readonly
    OnePointValley: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SegmentType
    ) = ...  # static # readonly
    RisingEdge: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SegmentType = (
        ...
    )  # static # readonly
    Spike: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SegmentType = (
        ...
    )  # static # readonly
    TrueApex: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SegmentType = (
        ...
    )  # static # readonly
    Zero: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SegmentType = (
        ...
    )  # static # readonly

class ShapeFit2:  # Class
    ...

class ShapeFitType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Constrained: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.ShapeFitType = (
        ...
    )  # static # readonly
    OffsetOnly: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.ShapeFitType = (
        ...
    )  # static # readonly
    Unconstrained: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.ShapeFitType
    ) = ...  # static # readonly

class Slice:  # Class
    ...

class SliceSegment:  # Class
    @overload
    def __init__(
        self,
        slice: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Slice,
        start: int,
        end: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        slice: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Slice,
        start: int,
        apex: int,
        end: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        parent: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment,
        splitOffRightValley: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        slice: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Slice,
        point: int,
    ) -> None: ...

    Apex: int  # readonly
    ApexAbundance: int  # readonly
    End: int  # readonly
    IsLeftEdgeProcessed: bool  # readonly
    IsNoise: bool  # readonly
    IsProcessed: bool  # readonly
    IsRightEdgeProcessed: bool  # readonly
    IsSpike: bool  # readonly
    IsZero: bool  # readonly
    IsZeroLeftEdge: bool  # readonly
    IsZeroRightEdge: bool  # readonly
    Length: int  # readonly
    ShapeType: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SegmentType
    )  # readonly
    Slice: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Slice  # readonly
    SliceIndex: int  # readonly
    Start: int  # readonly

    # Nested Types

    class AbundanceComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment,
            b: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment,
        ) -> int: ...

class SliceWindow:  # Class
    def __init__(
        self,
        sliceArray: List[Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Slice],
        centerSliceIndex: int,
        halfWidth: int,
    ) -> None: ...

    BottomSliceIndex: int  # readonly
    Size: int  # readonly

    def ExtendRisingEdge(
        self,
        feature: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature,
        firstSeg: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment: ...
    def ExtendFallingEdge(
        self,
        feature: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.Feature,
        lastSeg: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment: ...
    def ExtendTowardsApexFromRisingEdge(
        self,
        lastSeg: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment,
        foundApex: bool,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment: ...
    def ExtendTowardsApexFromFallingEdge(
        self,
        firstSeg: Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment,
        foundApex: bool,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureDetection.SliceSegment: ...

class XSTable:  # Class
    @overload
    def __init__(self, seed: int) -> None: ...
    @overload
    def __init__(self, readOK: bool) -> None: ...

    NIterations: int  # readonly

    def Read(self) -> bool: ...
    def Write(self) -> None: ...
    def AccumulatePTable(self, nIterations: int) -> None: ...
    def GetXPValue(
        self, noiseToSignal: float, xCenter: float, sharpness: float, xOffset: float
    ) -> float: ...
    def GetSPValue(
        self,
        noiseToSignal: float,
        xCenter: float,
        sharpness: float,
        targetSharpness: float,
    ) -> float: ...

    # Nested Types

    class GetBins(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> List[float]: ...
        def BeginInvoke(
            self,
            nIndex: int,
            sIndex: int,
            xIndex: int,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(self, nIndex: int, sIndex: int, xIndex: int) -> List[float]: ...
