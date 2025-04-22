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

from . import (
    AppCommandContext,
    ChromatographyType,
    CurveFit,
    DoubleRange,
    IntRange,
    QuantitationDataSet,
    SampleType,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant

class BatchFileInfo:  # Class
    BatchDataPath: str  # readonly
    BatchFileName: str  # readonly
    BatchID: int  # readonly
    BatchSamples: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchSampleInfo
    ]  # readonly
    CalibrationLevelInfo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.CalibrationLevelInfo
    )  # readonly
    CorrelationWindow: float  # readonly
    HighestLevelSample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchSampleInfo
    )  # readonly
    NSamples: int  # readonly
    NTargetCompounds: int  # readonly
    TargetCompounds: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.TargetCompoundInfo
    ]  # readonly

    def GetCalibrationSamplesByLevel(
        self,
    ) -> System.Collections.Generic.SortedList[
        float,
        System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchSampleInfo
        ],
    ]: ...
    def GetSampleByFileName(
        self, sampleFileName: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchSampleInfo
    ): ...

class BatchGlobalFeatureAnalysis(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IDynamicQuant
):  # Class
    @overload
    def __init__(self, batchDataPath: str, batchFileName: str) -> None: ...
    @overload
    def __init__(
        self,
        batchDataPath: str,
        batchFileName: str,
        dqParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.DynamicQuantParams,
    ) -> None: ...
    @overload
    def __init__(self, context: AppCommandContext) -> None: ...
    @overload
    def __init__(
        self,
        context: AppCommandContext,
        dqParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.DynamicQuantParams,
    ) -> None: ...

    BatchFileInfo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchFileInfo
    )  # readonly
    DynamicQuantParameters: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.DynamicQuantParams
    )  # readonly
    TargetCompoundIDs: List[int]  # readonly

    def GetDynamicTargetsInRange(
        self, compoundID: int, lowLevelConc: float, highLevelConc: float
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IDynamicQuantTarget
    ]: ...
    def IsTargetCompoundSaturated(self, compoundID: int) -> bool: ...
    def GetDynamicTargetIonGroups(
        self, compoundID: int
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ICrossSampleIonGroup
    ]: ...
    def FindCrossSampleIonGroups(self) -> None: ...
    def GetDynamicTargets(
        self, compoundID: int
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IDynamicQuantTarget
    ]: ...

    CrossSampleAnalysisDone: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchGlobalFeatureAnalysis.CrossSampleAnalysisFinishedEventHandler
    )  # Event
    CrossSampleAnalysisStarting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchGlobalFeatureAnalysis.CrossSampleAnalysisStartingEventHandler
    )  # Event
    SampleProcessingDone: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchGlobalFeatureAnalysis.SampleProcessingDoneEventHandler
    )  # Event

    # Nested Types

    class CrossSampleAnalysisFinishedEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            args: System.EventArgs,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(self, sender: Any, args: System.EventArgs) -> None: ...

    class CrossSampleAnalysisStartingEventArgs(System.EventArgs):  # Class
        NSamples: int  # readonly

    class CrossSampleAnalysisStartingEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            args: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchGlobalFeatureAnalysis.CrossSampleAnalysisStartingEventArgs,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            args: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchGlobalFeatureAnalysis.CrossSampleAnalysisStartingEventArgs,
        ) -> None: ...

    class SampleProcessingDoneEventArgs(System.EventArgs):  # Class
        SampleFileName: str  # readonly
        SampleIndex: int  # readonly

    class SampleProcessingDoneEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            args: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchGlobalFeatureAnalysis.SampleProcessingDoneEventArgs,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            args: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchGlobalFeatureAnalysis.SampleProcessingDoneEventArgs,
        ) -> None: ...

class BatchSampleInfo:  # Class
    BatchInfo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchFileInfo
    )  # readonly
    CalLevelInfo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.CalibrationLevelInfo
    )  # readonly
    ChromatographyType: ChromatographyType  # readonly
    Index: int  # readonly
    LevelConcentration: float  # readonly
    LevelIndex: int  # readonly
    LevelName: str  # readonly
    SampleDataPath: str  # readonly
    SampleDataSet: QuantitationDataSet  # readonly
    SampleFileName: str  # readonly
    SampleID: int  # readonly
    SampleType: SampleType  # readonly

    def GetTargetCompoundRow(
        self, compoundID: int
    ) -> QuantitationDataSet.TargetCompoundRow: ...

class CalibrationLevelInfo:  # Class
    LevelCount: int  # readonly

    def GetLevelIndexByConcentration(self, levelConcentration: float) -> int: ...
    def GetConcentrationForSample(self, sampleFileName: str) -> float: ...
    def GetLevelIndexForSample(self, sampleFileName: str) -> int: ...

class ComponentIonFeature(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IIonGroupFeature
):  # Class
    FeatureInfo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.FeatureInfo
    )  # readonly
    IsDerivedFromComponent: bool  # readonly
    IsUserDefinedTargetIon: bool  # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchSampleInfo
    )  # readonly
    TargetIon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ITargetIon
    )  # readonly

    # Nested Types

    class ReverseHeightComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ComponentIonFeature
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ComponentIonFeature,
            b: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ComponentIonFeature,
        ) -> int: ...

class CrossSampleIonGroup(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ICrossSampleIonGroup
):  # Class
    AverageMz: float  # readonly
    CompoundName: str  # readonly
    CompoundRT: float  # readonly
    ConcentrationRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD  # readonly
    IsUserDefinedTargetIonGroup: bool  # readonly
    LevelCount: int  # readonly
    LinearFit: CurveFit  # readonly
    MaxDeviationFromScalingRatio: float  # readonly
    SampleAreaResponses: List[float]  # readonly
    SampleConcentrations: List[float]  # readonly
    SampleHeightResponses: List[float]  # readonly
    SampleIonMZs: List[float]  # readonly
    SampleIonRTs: List[float]  # readonly
    TargetCompoundID: int  # readonly
    TotalIonCount: int  # readonly
    TotalLevelCount: int  # readonly
    UnsaturatedIonCount: int  # readonly
    UnsaturatedLevelCount: int  # readonly
    UnsaturatedRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD  # readonly
    UserDefinedTargetIon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ITargetIon
    )  # readonly

    def ContainsUnsaturatedIonInSample(self, sampleIndex: int) -> bool: ...
    def GetAverageAreaResponseAtLevel(self, levelIndex: int) -> float: ...
    def GetLevelIndexByLevelName(self, levelName: str) -> int: ...
    def GetSampleIndexListAtLevel(
        self, levelIndex: int
    ) -> System.Collections.Generic.List[int]: ...
    def ContainsUnsaturatedIonAtLevel(self, levelName: str) -> bool: ...
    def HasIonInSample(self, sampleIndex: int) -> bool: ...

class DynamicQuantParams:  # Class
    @overload
    def __init__(self, separationType: ChromatographyType) -> None: ...
    @overload
    def __init__(self, paramFile: str, separationType: ChromatographyType) -> None: ...

    CONFINE_TO_LINEAR_RANGE: bool = ...  # static # readonly
    CONTIGUOUS_LEVELS: bool = ...  # static # readonly
    DIMER_REJECTION_THRESHOLD: float = ...  # static # readonly
    FEATURE_GROUP_ALIGNMENT: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.FeatureGroupAlignment
    ) = ...  # static # readonly
    MAX_SCALING_RATIO_DEVIATION: float = ...  # static # readonly
    MAX_SCALING_RATIO_DEVIATION2: float = ...  # static # readonly
    MIN_FIT_R2: float = ...  # static # readonly
    MIN_LEVELS_PER_ION_GROUP: int = ...  # static # readonly
    MIN_TARGET_IONS_PER_COMPOUND: int = ...  # static # readonly
    MZ_TOLERANCE_PPM: float = ...  # static # readonly
    QUANTIFIER_METRIC: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.QuantifierMetricType
    ) = ...  # static # readonly

    ChromType: ChromatographyType  # readonly
    ConfineToLinearRange: bool
    ContiguousLevels: bool
    DimerRejectionThreshold: float
    FeatureGroupAlignment: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.FeatureGroupAlignment
    )
    MaxScalingRatioDeviation: float
    MaxScalingRatioDeviation2: float
    MinFitR2: float
    MinLevelsPerIonGroup: int
    MinTargetIonsPerCompound: int
    MzTolerancePpm: float
    NumThreads: int
    QuantifierMetric: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.QuantifierMetricType
    )
    RefLibraryPath: str
    UseDeconvolution: bool  # readonly
    UseReferenceSpectrum: bool  # readonly

class FeatureGroupAlignment(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Deconvolution: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.FeatureGroupAlignment
    ) = ...  # static # readonly
    DeconvolutionAndReferenceSpectrum: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.FeatureGroupAlignment
    ) = ...  # static # readonly
    ReferenceSpectrum: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.FeatureGroupAlignment
    ) = ...  # static # readonly

class FeatureInfo:  # Class
    ...

class ICrossSampleIonGroup(object):  # Interface
    AverageMz: float  # readonly
    CompoundName: str  # readonly
    CompoundRT: float  # readonly
    ConcentrationRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD  # readonly
    IsUserDefinedTargetIonGroup: bool  # readonly
    LevelCount: int  # readonly
    LinearFit: CurveFit  # readonly
    MaxDeviationFromScalingRatio: float  # readonly
    SampleAreaResponses: List[float]  # readonly
    SampleConcentrations: List[float]  # readonly
    SampleHeightResponses: List[float]  # readonly
    SampleIonMZs: List[float]  # readonly
    SampleIonRTs: List[float]  # readonly
    TargetCompoundID: int  # readonly
    TotalIonCount: int  # readonly
    TotalLevelCount: int  # readonly
    UnsaturatedIonCount: int  # readonly
    UnsaturatedLevelCount: int  # readonly
    UnsaturatedRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD  # readonly
    UserDefinedTargetIon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ITargetIon
    )  # readonly

    def ContainsUnsaturatedIonInSample(self, sampleIndex: int) -> bool: ...
    def GetAverageAreaResponseAtLevel(self, levelIndex: int) -> float: ...
    def GetLevelIndexByLevelName(self, levelName: str) -> int: ...
    def GetSampleIndexListAtLevel(
        self, levelIndex: int
    ) -> System.Collections.Generic.List[int]: ...
    def ContainsUnsaturatedIonAtLevel(self, levelName: str) -> bool: ...
    def HasIonInSample(self, sampleIndex: int) -> bool: ...

class IDynamicQuant(object):  # Interface
    BatchFileInfo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchFileInfo
    )  # readonly

    def GetDynamicTargetsInRange(
        self, compoundID: int, lowLevelConc: float, highLevelConc: float
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IDynamicQuantTarget
    ]: ...
    def IsTargetCompoundSaturated(self, compoundID: int) -> bool: ...
    def GetDynamicTargetIonGroups(
        self, compoundID: int
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ICrossSampleIonGroup
    ]: ...
    def FindCrossSampleIonGroups(self) -> None: ...
    def GetDynamicTargets(
        self, compoundID: int
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IDynamicQuantTarget
    ]: ...

class IDynamicQuantTarget(object):  # Interface
    AreaResponseRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD  # readonly
    CalibratedConcentrationRange: (
        Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD
    )  # readonly
    IsUserDefinedTarget: bool  # readonly
    QualifierCount: int  # readonly
    Qualifiers: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IDynamicTargetIon
    ]  # readonly
    Quantifier: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IDynamicTargetIon
    )  # readonly

    def GetQualifierByIndex(
        self, qualIndex: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IDynamicTargetIon
    ): ...
    def ContainsQualifier(
        self,
        qualifierIonGroup: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IDynamicTargetIon,
    ) -> bool: ...
    def Equals(
        self,
        otherTarget: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.IDynamicQuantTarget,
    ) -> bool: ...

class IDynamicTargetIon(object):  # Interface
    AreaResponseRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD  # readonly
    CrossSampleIonGroup: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ICrossSampleIonGroup
    )  # readonly
    DynamicRange: IntRange  # readonly
    ID: int  # readonly
    MZ: float  # readonly
    SampleAreaResponses: List[float]  # readonly
    SampleHeightResponses: List[float]  # readonly

    def ContainsUnsaturatedIonInSample(self, sampleIndex: int) -> bool: ...

class IIonGroupFeature(object):  # Interface
    FeatureInfo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.FeatureInfo
    )  # readonly
    IsDerivedFromComponent: bool  # readonly
    IsUserDefinedTargetIon: bool  # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchSampleInfo
    )  # readonly
    TargetIon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ITargetIon
    )  # readonly

class IRefIon(object):  # Interface
    Adduct: Agilent.MassSpectrometry.DataAnalysis.MFS.IAdductIon  # readonly
    IsLossOfWater: bool  # readonly
    IsotopeComposition: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IsotopeComposition
    )  # readonly
    Mass: float  # readonly
    RelativeAbundance: float  # readonly

class ITargetIon(object):  # Interface
    Index: int  # readonly
    MZ: float  # readonly
    MzRange: DoubleRange  # readonly
    SelectedMZ: float  # readonly
    TargetCompound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.TargetCompoundInfo
    )  # readonly

class LinearRangeExtensionType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    All: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.LinearRangeExtensionType
    ) = ...  # static # readonly
    UserDefinedTargetIonsOnly: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.LinearRangeExtensionType
    ) = ...  # static # readonly

class QuantifierMetricType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Heuristic: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.QuantifierMetricType
    ) = ...  # static # readonly
    MaxAreaResponse: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.QuantifierMetricType
    ) = ...  # static # readonly
    MaxDynamicRange: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.QuantifierMetricType
    ) = ...  # static # readonly
    MinConcentrationRSD: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.QuantifierMetricType
    ) = ...  # static # readonly

class TargetCompoundInfo:  # Class
    CASNumber: str  # readonly
    CompoundID: int  # readonly
    CompoundName: str  # readonly
    Formula: str  # readonly
    Index: int  # readonly
    LeftRTDelta: float  # readonly
    NTargetIons: int  # readonly
    Quantifier: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.TargetIonInfo
    )  # readonly
    RTRange: DoubleRange  # readonly
    RetentionTime: float  # readonly
    RightRtDelta: float  # readonly
    TargetIons: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.TargetIonInfo
    ]  # readonly

    def IsTargetMatch(
        self, mz: float, mzTolerancePpm: float, targetMzDelta: float
    ) -> bool: ...
    def GetTargetIonByIndex(
        self, ionIndex: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.TargetIonInfo
    ): ...
    def Equals(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.TargetCompoundInfo,
    ) -> bool: ...

class TargetIonInfo(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ITargetIon
):  # Class
    Index: int  # readonly
    MZ: float  # readonly
    MzRange: DoubleRange  # readonly
    SelectedMZ: float  # readonly
    TargetCompound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.TargetCompoundInfo
    )  # readonly

    def Equals(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.TargetIonInfo,
    ) -> bool: ...
