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

from . import ChromatographyType, ComponentInfo, DoubleRange

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant

class CalibrationLevels:  # Class
    INVALID_LEVEL_INDEX: int  # static

    IsGCData: bool  # readonly
    LevelCount: int  # readonly
    MaxLevelIndex: int  # readonly
    MinLevelIndex: int  # readonly
    SampleCount: int  # readonly
    StartingLevelIndex: int  # readonly

    def GetSamplesAtLevelIndex(
        self, levelIndex: int
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    ]: ...
    def GetSamplesByLevelConcentration(
        self, levelConcentration: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    ]: ...
    def GetLevelIndexByConcentration(self, conc: float) -> int: ...
    def GetLevelIndexForSample(
        self,
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
    ) -> int: ...
    def GetSamplesByLevel(
        self, level: str
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    ]: ...
    def GetSampleByPath(
        self, sampleDataPath: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    ): ...
    def GetReplicatesForSample(
        self,
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    ]: ...
    def GetLevelIndexByLevel(self, level: str) -> int: ...
    def GetConcentrationByLevelIndex(self, levelIndex: int) -> float: ...
    def GetLevelByIndex(self, levelIndex: int) -> str: ...

class CalibrationSample:  # Class
    def __init__(
        self, sampleDirPath: str, level: str, concentration: float
    ) -> None: ...

    ChromType: ChromatographyType  # readonly
    Concentration: float  # readonly
    CurrentScanConditions: (
        Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    )  # readonly
    DataDirPath: str  # readonly
    FeatureDataAccess: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.TofFeatureDataAccess
    )  # readonly
    IsAllIonsData: bool  # readonly
    IsGCData: bool  # readonly
    Level: str  # readonly
    ScanConditionList: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    ]  # readonly

    def GetFeatureSet(
        self,
        refSpectrumScanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.IFeatureSet: ...
    def Open(self) -> bool: ...
    def GetFeaturesInRange(
        self,
        scanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions,
        targetMz: float,
        rtRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD,
        mzRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    def GetFeatureByID(
        self,
        scanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions,
        featureID: int,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FD.Feature: ...
    def Close(self) -> None: ...
    def ContainsDataForScanConditions(
        self, refScanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    ) -> bool: ...
    def GetFeaturesInMzRange(
        self,
        scanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions,
        targetMz: float,
        mzRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FD.Feature
    ]: ...
    def GetNoiseFactor2(
        self, scanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions
    ) -> float: ...

class CalibrationSampleList(
    Iterable[Any],
    Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    ],
):  # Class
    def __init__(self, sampleListFilePath: str) -> None: ...

    BatchDirectory: str  # readonly
    Count: int  # readonly
    IsAllIonsData: bool  # readonly
    IsGCData: bool  # readonly
    Levels: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationLevels
    )  # readonly
    SampleListFile: str  # readonly
    Samples: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    ]  # readonly

    def GetSampleListSortedByConcentration(
        self, reverse: bool
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    ]: ...

    # Nested Types

    class ReverseConcentrationComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
            b: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
        ) -> int: ...

class CoelutingFeatureGroup(
    Iterable[Any],
    Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ],
):  # Class
    @overload
    def __init__(
        self,
        cpdFeaturesInSample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CompoundFeaturesInSample,
        component: Agilent.MassSpectrometry.DataAnalysis.Component,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cpdFeaturesInSample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CompoundFeaturesInSample,
        largestFeature: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature,
    ) -> None: ...

    AssignedRT: float  # readonly
    FeatureCount: int  # readonly
    LibraryMatchScore: float  # readonly
    RTRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD  # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    )  # readonly
    ShapeQualityScore: float  # readonly
    TargetCompound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly

    def GetFeatureByReferenceIon(
        self,
        refIon: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ): ...
    def Add(
        self,
        feature: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature,
    ) -> bool: ...
    def SatisfiesAbundanceScalingConstraint(
        self,
        lowerLevelGroup: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CoelutingFeatureGroup,
    ) -> bool: ...
    def AddFeatureNoCheck(
        self,
        feature: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature,
    ) -> None: ...
    @overload
    def IsAlignedWith(
        self,
        feature: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature,
    ) -> bool: ...
    @overload
    def IsAlignedWith(
        self,
        featureGroup: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CoelutingFeatureGroup,
    ) -> bool: ...
    def ComputeLibraryMatchScore(
        self,
        refLibrary: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrumLibrary,
    ) -> None: ...
    def GetFeatureSpectrum(
        self, mzValues: List[float], abundanceValues: List[float]
    ) -> None: ...

class CompoundFeaturesInSample:  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
        spectra: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum
        ],
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
        maParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.MethodAssistantParameters,
    ) -> None: ...

    CoelutingFeatureGroups: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CoelutingFeatureGroup
    ]  # readonly
    NCoelutingGroups: int  # readonly
    NFeatures: int  # readonly
    RefSpectra: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum
    ]  # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    )  # readonly
    TargetCompound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly

    def FilterCoelutingGroupsByLibraryMatchScore(
        self, minScore: float, maxGroupCount: int, minGroupCount: int
    ) -> None: ...
    def GetFeatureByID(
        self, featureID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ): ...
    def GetFeaturesByReferenceSpectrum(
        self,
        refSpectrum: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrumFeaturesInSample
    ): ...
    def GetRefIonFeatures(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ]: ...
    def ComputeLibraryMatchScores(
        self,
        refLibrary: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrumLibrary,
    ) -> None: ...
    def FindCoelutingFeatureGroups(self) -> None: ...
    def GetFeaturesInSampleByReferenceIon(
        self,
        refIon: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.FeatureListForRefIonInSample
    ): ...

class CompoundMethodAssistant:  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
        refSpectra: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum
        ],
        levels: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationLevels,
        maParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.MethodAssistantParameters,
    ) -> None: ...

    AlternativeGroupClusters: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleFeatureGroupCluster
    ]  # readonly
    BestTargetGroupCluster: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleFeatureGroupCluster
    )  # readonly
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    CrossSampleTargetSearch_Combined: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetSearch
    )  # readonly
    CrossSampleTargetSearch_Separate: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetSearch
    )  # readonly
    HasAltClusters: bool  # readonly
    HasIsomers: bool  # readonly
    IsomerCount: int  # readonly
    ProcessedSampleCount: int  # readonly
    RefSpectra: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum
    ]  # readonly
    ReferenceSpectrumLibrary: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrumLibrary
    )  # readonly

    def DebugWriteTargetCompoundCandidates(
        self, sw: System.IO.StreamWriter
    ) -> None: ...
    def DebugWriteTargetCompoundCandidates_AllIons(
        self, sw: System.IO.StreamWriter
    ) -> None: ...
    def FindCrossSampleTargetHitGroups(self, resolveTargetAmbiguity: bool) -> None: ...
    def GetCrossSampleTargetSearch(
        self, separateScanConditions: bool
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetSearch
    ): ...
    def ExtractCompoundFeatures(
        self,
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CompoundFeaturesInSample
    ): ...
    def FindTargetHitsInSample(
        self,
        cpdFeaturesInSample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CompoundFeaturesInSample,
        resolveTargetAmbiguity: bool,
    ) -> None: ...
    @overload
    def CollectBestAndAltTargetHitGroups(
        self,
        targetSelector: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitGroupSelector,
    ) -> None: ...
    @overload
    def CollectBestAndAltTargetHitGroups(
        self,
        targetSelector_Separate: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitGroupSelector,
        targetSelector_Combined: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitGroupSelector,
    ) -> None: ...
    def DebugWriteTargetHitGroups(self, sw: System.IO.StreamWriter) -> None: ...
    def GetCompoundFeaturesForSample(
        self,
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CompoundFeaturesInSample
    ): ...

class CrossSampleFeatureGroup:  # Class
    def __init__(
        self,
        refIonFeature: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature,
        levels: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationLevels,
    ) -> None: ...

    AverageMzErrorPpm: float  # readonly
    AverageRT: float  # readonly
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    FeatureRTRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD  # readonly
    IsContiguous: bool  # readonly
    IsGCData: bool  # readonly
    IsNonMonotonic: bool  # readonly
    LevelCount: int  # readonly
    MaxLevelIndex: int  # readonly
    MedianMzErrorPpm: float  # readonly
    MinLevelIndex: int  # readonly
    QualityMetric: float  # readonly
    RefIon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon
    )  # readonly
    RelativeDynamicRange: float  # readonly
    ScalingQualityMetric: float  # readonly
    TotalFeatureCount: int  # readonly
    TotalLevelCount: int  # readonly

    def GetAverageMzErrorPpmByLevelIndex(self, levelIndex: int) -> float: ...
    def GetAverageMzByLevelIndex(self, levelIndex: int) -> float: ...
    def AddRefIonFeature(
        self,
        refIonFeature: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature,
    ) -> bool: ...
    def ContainsFeatureAtLevel(self, levelIndex: int) -> bool: ...
    def OverlapsFeatureInRT(
        self,
        feature: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature,
    ) -> bool: ...
    def GetResponseVsConcentrationTable(
        self, nLowestLevels: int, concentrations: List[float], responses: List[float]
    ) -> None: ...
    def GetAverageRTByLevelIndex(self, levelIndex: int) -> float: ...
    def GetFeaturesByLevelIndex(
        self, levelIndex: int
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ]: ...
    def GetFirstPopulatedLevelIndexAbove(self, levelIndex: int) -> int: ...
    def CanContainFeature(
        self,
        feature: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature,
    ) -> bool: ...
    def GetAverageCoelutionCountByLevelIndex(self, levelIndex: int) -> float: ...
    def GetAverageAreaByLevelIndex(self, levelIndex: int) -> float: ...
    def GetFirstPopulatedLevelIndexBelow(self, levelIndex: int) -> int: ...
    def FindFeatureFromSample(
        self,
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ): ...
    def GetAverageHeightByLevelIndex(self, levelIndex: int) -> float: ...
    def GetAverageResponseFactorByLevelIndex(self, levelIndex: int) -> float: ...

class CrossSampleFeatureGroupCluster:  # Class
    def __init__(
        self,
        firstGroup: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleFeatureGroup,
    ) -> None: ...

    AssignedRT: float  # readonly
    AverageGroupMassAccuracyPpm: float  # readonly
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    FeatureGroups: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleFeatureGroup
    ]  # readonly
    GroupCount: int  # readonly
    GroupRTs: List[float]  # readonly
    MassAccuracyMetric: float  # readonly
    MaxDynamicRangeGroup: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleFeatureGroup
    )  # readonly
    MaxGroupDynamicRangeInLevels: int  # readonly
    MedianGroupMassAccuracyPpm: float  # readonly
    QualityMetric: float  # readonly
    QualityMetricNoGroupCount: float  # readonly
    RTRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD  # readonly

    def AddGroup(
        self,
        group: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleFeatureGroup,
    ) -> None: ...
    def Overlaps(
        self,
        group: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleFeatureGroup,
    ) -> bool: ...
    def SortGroupsByDynamicRange(self) -> None: ...
    def CheckReferenceSpectrumConsistency(self, allSpectraMustPass: bool) -> bool: ...
    def GetFeatureGroupByRank(
        self, rankIndex: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleFeatureGroup
    ): ...
    def SortGroupsByQualityMetric(self) -> None: ...
    def SortGroupsByDynamicRangeAndQuality(self) -> None: ...
    def GetFeatureGroupByRefIon(
        self,
        refIon: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleFeatureGroup
    ): ...

class CrossSampleTargetHitGroup:  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
        samples: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
        ],
        levels: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationLevels,
        firstTargetHit: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitInfo,
    ) -> None: ...

    AssignedRT: float  # readonly
    AverageLMS: float  # readonly
    AverageRT: float  # readonly
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    DynamicRangeInLevels: int  # readonly
    DynamicRangeScore: float  # readonly
    FeatureGroupCluster: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleFeatureGroupCluster
    )  # readonly
    ID: int  # readonly
    LMSStdError: float  # readonly
    MassScore: float  # readonly
    MaxLMS: float  # readonly
    MaxLevelIndex: int  # readonly
    MaxRT: float  # readonly
    MaxRTRange: DoubleRange  # readonly
    MedianLMS: float  # readonly
    MedianRT: float  # readonly
    MinLMS: float  # readonly
    MinLevelIndex: int  # readonly
    MinRT: float  # readonly
    QualityScore: float  # readonly
    RT3SigmaRange: DoubleRange  # readonly
    RTStdError: float  # readonly
    SampleCount: int  # readonly
    ScalingQualityMetric: float  # readonly
    TotalLevelCount: int  # readonly

    def AddTargetHit(
        self,
        targetHit: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitInfo,
    ) -> None: ...
    def GetAverageLMSByLevelIndex(self, levelIndex: int) -> float: ...
    @overload
    @staticmethod
    def ComputeCrossCorrelationScore(
        targetHit: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitInfo,
        dotProduct: Agilent.MassSpectrometry.DataAnalysis.DotProductSearch,
    ) -> float: ...
    @overload
    @staticmethod
    def ComputeCrossCorrelationScore(
        tgt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitInfo,
        rfs: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitInfo,
        dotProduct: Agilent.MassSpectrometry.DataAnalysis.DotProductSearch,
    ) -> float: ...
    def GetAverageRTByLevelIndex(self, levelIndex: int) -> float: ...
    def ContainsTargetHitsAtLevel(self, levelIndex: int) -> bool: ...
    def ConvertToTargetFeatureGroupCluster(self) -> None: ...
    def GetAverageIonCountByLevelIndex(self, levelIndex: int) -> float: ...
    def ContainsTargetHitInSample(
        self,
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
    ) -> bool: ...
    def GetAverageAreaByLevelIndex(self, levelIndex: int) -> float: ...
    def GetAverageHeightByLevelIndex(self, levelIndex: int) -> float: ...
    def OverlapsInRT(
        self,
        targetHit: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitInfo,
    ) -> bool: ...

class CrossSampleTargetSearch:  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
        levels: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationLevels,
        refLibrary: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrumLibrary,
        separateScanConditions: bool,
    ) -> None: ...

    BestGroupByDynamicRange: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    )  # readonly
    BestGroupByLMS: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    )  # readonly
    BestGroupByMass: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    )  # readonly
    BestGroupByQuality: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    )  # readonly
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    HitGroupCount: int  # readonly
    IsUnambiguous: bool  # readonly
    IsUnique: bool  # readonly
    NoGroupsFound: bool  # readonly
    SecondBestGroupByQuality: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    )  # readonly
    SeparateScanConditions: bool  # readonly
    TargetHitGroups: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    ]  # readonly

    def DebugWriteTargetHitGroupSummary(self, sw: System.IO.StreamWriter) -> None: ...
    def FilterTargetHitGroupsByMinDynamicRange(self, minLevels: int) -> None: ...
    def FindTargetCandidatesInRange(
        self, rtSearchRange: DoubleRange
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCandidatesInRTRange
    ): ...
    def FindTargetHitGroups(self) -> None: ...
    def EvaluateTargetHits(self) -> None: ...
    def FindTargetHitsInSample(
        self,
        cpdFeaturesInSample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CompoundFeaturesInSample,
    ) -> None: ...
    def ComputeMassAccuracyMetrics(self) -> None: ...
    def DebugWriteGroupSummary(self, sw: System.IO.StreamWriter) -> None: ...
    def DebugWriteTargetHitGroups(self, sw: System.IO.StreamWriter) -> None: ...
    def PopulateTargetHitGroups(self) -> None: ...

class FeatureListForRefIonInSample(
    Iterable[Any],
    Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ],
):  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
        refIon: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon,
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
        maParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.MethodAssistantParameters,
    ) -> None: ...

    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    FeatureCount: int  # readonly
    ReferenceIon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon
    )  # readonly

    def Contains(
        self,
        f: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature,
    ) -> bool: ...
    def GetFeaturesInRange(
        self, mzDeltaPpm: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ]: ...
    def AppendRefIonFeaturesToList(
        self,
        featureList: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
        ],
    ) -> None: ...

class IsomerSet:  # Class
    Compounds: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    ]  # readonly
    Count: int  # readonly
    Formula: str  # readonly
    HasImplicitOrder: bool  # readonly
    Name: str  # readonly

    def GetImplicitOrderIndexForIsomerCompound(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
    ) -> int: ...
    def ContainsCompound(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
    ) -> bool: ...
    def AddIsomerCompound(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
    ) -> bool: ...
    def FinalizeIsomerSet(self) -> None: ...
    def GetIsomerByName(
        self, cpdName: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    ): ...
    def GetIsomerByIndexInImplicitOrder(
        self, index: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    ): ...

class MethodAssistantParameters:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, xmlFilePath: str) -> None: ...

    DEFAULT_ADDUCTS: List[str]  # static # readonly
    DEFAULT_MZ_EXTRACTION_DELTA_PPM: float = ...  # static # readonly
    DEFAULT_XML_PARAM_FILE: str = ...  # static # readonly
    HIGH_MZ_EXTRACTION_DELTA_PPM: float = ...  # static # readonly
    H_PLUS_ADDUCT: str = ...  # static # readonly
    K_PLUS_ADDUCT: str = ...  # static # readonly
    LOW_MZ_EXTRACTION_DELTA_PPM: float = ...  # static # readonly
    MAX_IONS_IN_ISOTOPE_PATTERN: int = ...  # static # readonly
    MAX_IONS_PER_SPECTRUM: int = ...  # static # readonly
    MIN_IONS_PER_SPECTRUM: int = ...  # static # readonly
    MIN_REF_ION_RELATIVE_ABUNDANCE: float = ...  # static # readonly
    MIN_RELATIVE_ISOTOPE_ABUNDANCE: float = ...  # static # readonly
    NH4_PLUS_ADDUCT: str = ...  # static # readonly
    NUM_QUALIFIERS_DESIRED: int = ...  # static # readonly
    Na_PLUS_ADDUCT: str = ...  # static # readonly
    QUANT_METHOD_RT_EXTRACTION_DELTA_GC: float = ...  # static # readonly
    QUANT_METHOD_RT_EXTRACTION_DELTA_LC: float = ...  # static # readonly
    RESOLVE_TARGET_RT_AMBIGUITY: bool = ...  # static # readonly
    RT_TARGET_SEARCH_RANGE_DELTA: float = ...  # static # readonly
    SEARCH_ENTIRE_CHROMATOGRAPHIC_RANGE: bool = ...  # static # readonly

    AdductFormulas: List[str]
    DefaultMzDeltaPpm: float
    HasUnrecognizedAdducts: bool  # readonly
    HighMzDeltaPpm: float
    LowMzDeltaPpm: float
    MaxIonsInIsotopePattern: int
    MaxIonsPerSpectrum: int
    MethodRTExtractionDelta: float
    MinIonsPerSpectrum: int
    MinRefIonRelativeAbundance: float
    MinRelativeIsotopeAbundance: float
    NQualifiers: int
    OutputMethodFilePath: str
    RTTargetSearchRangeDelta: float
    ResolveTargetRTAmbiguity: bool
    SearchEntireChromatographicRange: bool
    UnrecognizedAdducts: List[str]  # readonly

class MethodAssistantRunCompleted(
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

class MethodAssistantRunStarting(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        nSamples: int,
        nCompounds: int,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, nSamples: int, nCompounds: int) -> None: ...

class QuantMethodAssistant(System.IDisposable):  # Class
    @overload
    def __init__(
        self, sampleListFilePath: str, compoundListFilePath: str, refLibraryPath: str
    ) -> None: ...
    @overload
    def __init__(
        self,
        sampleListFilePath: str,
        compoundListFilePath: str,
        refLibraryPath: str,
        optParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.MethodAssistantParameters,
    ) -> None: ...

    CalibrationLevels: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationLevels
    )  # readonly
    CompoundList: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompoundList
    )  # readonly
    NCompounds: int  # readonly
    Parameters: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.MethodAssistantParameters
    )  # readonly
    SampleList: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSampleList
    )  # readonly

    def CreateQuantMethod(self) -> None: ...
    def Dispose(self) -> None: ...
    def FindQuantTargets(self) -> None: ...

    RunCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.MethodAssistantRunCompleted
    )  # Event
    RunStarting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.MethodAssistantRunStarting
    )  # Event
    SampleProcessed: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.SampleProcessed
    )  # Event
    SampleProcessingStarting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.SampleProcessingStarting
    )  # Event

class RefIonFeature:  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
        refIon: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon,
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
        feature: Agilent.MassSpectrometry.DataAnalysis.FD.Feature,
    ) -> None: ...

    Area: float  # readonly
    CoelutingFeatureGroupInSample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CoelutingFeatureGroup
    )  # readonly
    CoelutionCount: int  # readonly
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    FWHM: float  # readonly
    Feature: Agilent.MassSpectrometry.DataAnalysis.FD.Feature  # readonly
    FeatureID: int  # readonly
    Height: float  # readonly
    IsSaturated: bool  # readonly
    MZ: float  # readonly
    MzErrorPpm: float  # readonly
    RT: float  # readonly
    RTRange: Agilent.MassSpectrometry.DataAnalysis.DoubleRangeD  # readonly
    RefIon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon
    )  # readonly
    ResponseFactor: float  # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    )  # readonly

    def ReleaseFeature(self) -> None: ...
    def OverlapsInRT(
        self,
        otherFeature: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature,
    ) -> bool: ...

class ReferenceIon:  # Class
    def __init__(
        self,
        parentSpectrum: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum,
        mz: float,
        abundance: float,
    ) -> None: ...

    Abundance: float  # readonly
    IntegerMZ: int  # readonly
    MZ: float  # readonly
    Polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity  # readonly
    Spectrum: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum
    )  # readonly

class ReferenceSpectrum(
    Iterable[Any],
    Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon
    ],
    System.IEquatable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum
    ],
):  # Class
    def __init__(
        self,
        library: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrumLibrary,
        spectrumRow: Agilent.MassSpectrometry.DataAnalysis.LibraryDataSet.SpectrumRow,
        maxRefIons: int,
        minRefIons: int,
        minRelativeAbundance: float,
    ) -> None: ...

    Adduct: Agilent.MassSpectrometry.DataAnalysis.MFS.IAdductIon  # readonly
    BaseIon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon
    )  # readonly
    CollisionEnergy: float  # readonly
    FragmentorVoltage: float  # readonly
    HasRetentionTime: bool  # readonly
    IonCount: int  # readonly
    IonsSortedByAbundance: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon
    ]  # readonly
    Polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity  # readonly
    RT: float  # readonly
    ScanConditions: Agilent.MassSpectrometry.DataAnalysis.FD.ScanConditions  # readonly
    ScanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType  # readonly
    SelectedMZ: float  # readonly

    def Equals(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum,
    ) -> bool: ...
    def GetTopReferenceIonsByAbundance(
        self, nIons: int
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon
    ]: ...
    def GetReferenceIonByIndex(
        self, index: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon
    ): ...
    def GetReferenceIonByMz(
        self, mz: float
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon
    ): ...
    @staticmethod
    def MapSpeciesToAdduct(
        spectrum: Agilent.MassSpectrometry.DataAnalysis.LibraryDataSet.SpectrumRow,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.IAdductIon: ...
    def ContainsIonAtIntegerMZ(self, integerMz: int) -> bool: ...

class ReferenceSpectrumFeaturesInSample:  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
        spectrum: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum,
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample,
        maParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.MethodAssistantParameters,
    ) -> None: ...
    def GetFeaturesForAllRefIonsInSpectrum(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ]: ...
    def GetFeatureListForRefIon(
        self,
        refIon: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.FeatureListForRefIonInSample
    ): ...

class ReferenceSpectrumLibrary:  # Class
    @overload
    def __init__(
        self,
        libraryPath: str,
        compoundList: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompoundList,
        maParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.MethodAssistantParameters,
    ) -> None: ...
    @overload
    def __init__(
        self,
        compoundList: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompoundList,
        maParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.MethodAssistantParameters,
    ) -> None: ...

    Library: Agilent.MassSpectrometry.DataAnalysis.ILibrary  # readonly
    LibraryPath: str  # readonly

    def GetSpectraForCompound(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum
    ]: ...
    def ComputeBestReverseMatchScore(
        self,
        featureGroup: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CoelutingFeatureGroup,
    ) -> float: ...
    def CloseLibrary(self) -> None: ...
    def GetSpectraByName(
        self, cpdName: str
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum
    ]: ...
    def ComputeReverseMatchScores(
        self,
        featureGroup: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CoelutingFeatureGroup,
    ) -> Dict[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum,
        float,
    ]: ...
    def ComputeMatchScores(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
        component: Agilent.MassSpectrometry.DataAnalysis.Component,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.CandidateHit
    ]: ...
    def GetSpectraByCAS(
        self, casNumber: str
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrum
    ]: ...
    def ComputeForwardMatchScores(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
        component: Agilent.MassSpectrometry.DataAnalysis.Component,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.CandidateHit
    ]: ...

class RetentionTimeAlignment:  # Class
    def __init__(
        self,
        samples: List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
        ],
    ) -> None: ...

    SampleCount: int  # readonly

    def RunTICBasedAlignment(self) -> None: ...

class SampleProcessed(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        sampleDataPath: str,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, sampleDataPath: str) -> None: ...

class SampleProcessingStarting(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        sampleDataPath: str,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, sampleDataPath: str) -> None: ...

class TargetCandidatesInRTRange:  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
        targetHitGroups: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
        ],
        rtSearchRange: DoubleRange,
    ) -> None: ...

    BestCandidateByLMS: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    )  # readonly
    BestCandidateByQualityScore: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    )  # readonly
    CandidateHitGroups: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    ]  # readonly
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    CountInRange: int  # readonly
    FirstRT: float  # readonly
    HitGroupsInRange: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    ]  # readonly
    LastRT: float  # readonly
    LibraryMatchScores: System.Collections.Generic.List[float]  # readonly
    MaxLMS: float  # readonly
    MaxQuality: float  # readonly
    MaxUniqueness: float  # readonly
    QualityScores: System.Collections.Generic.List[float]  # readonly
    RTSearchRange: DoubleRange  # readonly
    RTValues: System.Collections.Generic.List[float]  # readonly
    ScalingScores: System.Collections.Generic.List[float]  # readonly
    TotalHitCount: int  # readonly
    UniquenessScores: System.Collections.Generic.List[float]  # readonly

    def SortCandidatesByRT(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    ]: ...
    def SortCandidatesByQualityScore(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    ]: ...
    def SortCandidatesByLMS(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    ]: ...

class TargetCompound:  # Class
    @overload
    def __init__(
        self,
        cpdList: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompoundList,
        index: int,
        name: str,
        cas: str,
    ) -> None: ...
    @overload
    def __init__(
        self,
        cpdList: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompoundList,
        index: int,
        name: str,
        cas: str,
        formula: str,
        rt: float,
    ) -> None: ...

    CAS: str  # readonly
    CompoundList: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompoundList
    )  # readonly
    Formula: str  # readonly
    HasIsomers: bool  # readonly
    HasRT: bool  # readonly
    Index: int  # readonly
    IsomerSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.IsomerSet
    )  # readonly
    Name: str  # readonly
    ParsedFormula: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula
    )  # readonly
    RT: float  # readonly

class TargetCompoundList(
    Iterable[Any],
    Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    ],
):  # Class
    def __init__(self, cpdListFilePath: str) -> None: ...

    CompoundListFile: str  # readonly
    Count: int  # readonly

    def GetCompoundByName(
        self, cpdName: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    ): ...
    def GetCompoundByIndex(
        self, index: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    ): ...
    def GetCompoundByCAS(
        self, cas: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    ): ...

class TargetHitGroupSelector:  # Class
    NAssignedCpds: int  # readonly
    NCompounds: int  # readonly
    SeparateScanConditions: bool  # readonly

    def GetAltHitGroupsForCompound(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    ]: ...
    def GetSelectedHitGroupForCompound(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CrossSampleTargetHitGroup
    ): ...
    def SelectTargetHitGroups(self) -> None: ...

class TargetHitInfo:  # Class
    Component: Agilent.MassSpectrometry.DataAnalysis.Component  # readonly
    ComponentInfo: ComponentInfo  # readonly
    ComponentRT: float  # readonly
    HitIndex: int  # readonly
    IsIsomer: bool  # readonly
    IsTopHit: bool  # readonly
    IsomerCompound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    IsomerName: str  # readonly
    MatchScore: float  # readonly
    RTRange: DoubleRange  # readonly
    RefIonFeatureCount: int  # readonly
    RefIonFeatures: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ]  # readonly
    ReferenceIons: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon
    ]  # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    )  # readonly
    TargetCompound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    TargetName: str  # readonly

    def ContainsRefIon(
        self,
        refIon: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon,
    ) -> bool: ...
    def GetRefIonFeature(
        self,
        refIon: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceIon,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
    ): ...

class TargetHitSearchInSample:  # Class
    def __init__(
        self,
        cpdFeaturesInSample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CompoundFeaturesInSample,
        refLibrary: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.ReferenceSpectrumLibrary,
    ) -> None: ...

    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetCompound
    )  # readonly
    NumResolutions: int  # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.CalibrationSample
    )  # readonly
    TargetHits: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitInfo
    ]  # readonly

    @overload
    def FindTargetHits(
        self, separateScanConditions: bool
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitInfo
    ]: ...
    @overload
    def FindTargetHits(
        self,
        refIonFeatures: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.RefIonFeature
        ],
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodAssistant.TargetHitInfo
    ]: ...
