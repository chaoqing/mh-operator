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
    IIonSpeciesDetails,
    IIsotopeClusterBase,
    IModificationSpecies,
    PeakFinderAlgorithmName,
    SpectralPeak,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.MassHunter

class CompoundFilterParameters(
    CompoundFilters.IProteinFilterParameters,
    Agilent.MassSpectrometry.DataAnalysis.MassHunter.MfeFilterParameters,
    CompoundFilters.ICompoundFilterParameters,
    CompoundFilters.IGenericCompoundFilterParameters,
):  # Class
    def __init__(self) -> None: ...

    ChargeStateParameters: CompoundFilters.ChargeStateFilter.Parameter  # readonly
    IsotopePatternParameters: CompoundFilters.IsotopePatternFilter.Parameter  # readonly
    MinIonCountParamters: CompoundFilters.MinIonCountFilter.Parameter  # readonly
    NeutralModificationParameters: (
        CompoundFilters.NeutralModificationFilter.Parameter
    )  # readonly
    QualityScoreParameters: CompoundFilters.QualityScoreFilter.Parameter  # readonly
    TimePeakWidthParameters: CompoundFilters.PeakRtWidthFilter.Parameter  # readonly
    UunknownMassParameters: CompoundFilters.UnknownMassFilter.Parameter  # readonly

    def SetUnknownMassParameters(
        self, status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus
    ) -> None: ...
    def GetNeutralModificationParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        modificationList: List[str],
    ) -> None: ...
    def GetChargeStateParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        minChargeCount: int,
        maxChargeCount: int,
        fullRangeRequired: bool,
    ) -> None: ...
    def GetIsotopePatternParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        templateFormula: str,
        massAccuracyCoefficients: List[float],
        relativeIntensityUncertainty: float,
        intensityPattern: List[float],
        intensityPatternUncertainty: List[float],
    ) -> None: ...
    def SetNeutralModificationParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        modificationList: List[str],
    ) -> None: ...
    def GetMinIonCountParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        minIonCount: int,
    ) -> None: ...
    def GetUnknownMassParameters(
        self, status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus
    ) -> None: ...
    def SetChargeStateParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        minChargeCount: int,
        maxChargeCount: int,
        fullRangeRequired: bool,
    ) -> None: ...
    def SetIsotopePatternParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        templateFormula: str,
        massAccuracyCoefficients: List[float],
        relativeIntensityUncertainty: float,
        intensityPattern: List[float],
        intensityPatternUncertainty: List[float],
    ) -> None: ...
    def GetQualityScoreParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        minScore: float,
        maxScore: float,
    ) -> None: ...
    def GetPeakTimeWidthParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        minWidth: float,
        maxWidth: float,
    ) -> None: ...
    def SetMinIonCountParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        minIonCount: int,
    ) -> None: ...
    def SetQualityScoreParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        minScore: float,
        maxScore: float,
    ) -> None: ...
    def SetPeakTimeWidthParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        minWidth: float,
        maxWidth: float,
    ) -> None: ...

class FilterStatus(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Block: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus = (
        ...
    )  # static # readonly
    NotApplied: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus = (
        ...
    )  # static # readonly
    PassOnlyThese: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus = (
        ...
    )  # static # readonly

class IChargeState(object):  # Interface
    Abundance: float  # readonly
    HasPeak: bool  # readonly
    MZ: float  # readonly
    MaxHeight: float  # readonly
    PredictedMass: float  # readonly
    RetentionTime: float  # readonly
    Saturated: bool  # readonly
    Signal3Ds: List[
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.ISignal3D
    ]  # readonly
    Z: int  # readonly

class IChemicalAndIonizationParameters(object):  # Interface
    IonSpeciesGroupingRulesNegative: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IIonSpeciesGroupingRules
    )  # readonly
    IonSpeciesGroupingRulesPositive: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IIonSpeciesGroupingRules
    )  # readonly
    IsotopeCharacteristics: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IsotopeCharacteristics
    )
    MaxChargeCount: int
    NeutralModifications: List[str]
    TargetedMassList: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.ITargetedMassList
    )  # readonly

class ICoelutedProteinGroup(object):  # Interface
    Proteins: List[
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IProtein
    ]  # readonly
    RetentionTime: float  # readonly

class ICoelutionGroup(object):  # Interface
    Compounds: List[
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.ICompound
    ]  # readonly
    RetentionTime: float  # readonly
    Saturated: bool  # readonly

class ICompound(object):  # Interface
    Abundance: float  # readonly
    AverageMass: float  # readonly
    AverageMassStandardDeviation: float  # readonly
    IsotopeClusters: List[
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IIsotopeCluster
    ]  # readonly
    LowestIsotopeMass: float  # readonly
    MassStandardDeviation: float  # readonly
    MaxHeight: float  # readonly
    MostReliableIsotopeCluster: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IIsotopeCluster
    )  # readonly
    QualityScore: float  # readonly
    RetentionTime: float  # readonly
    RetentionTimePeakWidth: float  # readonly
    Saturated: bool  # readonly

class IDataRangeParameters(object):  # Interface
    MaxMZ: float  # readonly
    MaxRetentionTime: float  # readonly
    MinMZ: float  # readonly
    MinRetentionTime: float  # readonly

    def SetMZRange(self, min: float, max: float) -> None: ...
    def SetRetentionTimeRange(self, min: float, max: float) -> None: ...

class IIonSpeciesGroupingRules(object):  # Interface
    ChargeCarrierList: List[
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.UnitChargeCarrier
    ]
    DefaultUnitCharge: str

class IIsotope(object):  # Interface
    Abundance: float  # readonly
    MZ: float  # readonly
    MaxHeight: float  # readonly
    QualityScore: float  # readonly
    RetentionTime: float  # readonly
    RetentionTimePeakWidth: float  # readonly
    Saturated: bool  # readonly

class IIsotopeCluster(IIsotopeClusterBase):  # Interface
    Abundance: float  # readonly
    IonSpecies: IModificationSpecies  # readonly
    IonSpeciesDetails: IIonSpeciesDetails  # readonly
    Isotopes: List[
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IIsotope
    ]  # readonly
    LowestIsotopeMZ: float  # readonly
    MaxHeight: float  # readonly
    QualityScore: float  # readonly
    RetentionTime: float  # readonly
    RetentionTimePeakWidth: float  # readonly
    Saturated: bool  # readonly
    SaturationCorrectedIsotopePattern: List[SpectralPeak]  # readonly

class IProtein(object):  # Interface
    Abundance: float  # readonly
    IonSet: List[
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IChargeState
    ]  # readonly
    Mass: float  # readonly
    MassStandardDeviation: float  # readonly
    MaxHeight: float  # readonly
    RetentionTime: float  # readonly
    RetentionTimePeakWidth: float  # readonly
    Saturated: bool  # readonly

class IProteinFinderParameters(object):  # Interface
    ...

class IRawSpectrumAccessor(object):  # Interface
    FullSaturationLevel: float  # readonly
    Metadata: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata
    )  # readonly
    ScanCalibCoefficients: List[float]  # readonly
    ScanFirstXValue: float  # readonly
    ScanProfileIntensities: List[float]  # readonly
    ScanRetentionTimes: List[float]  # readonly
    SpectraType: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectraType
    )  # readonly
    TicIntensities: List[float]  # readonly

    def Close(self) -> None: ...
    def GetPeakList(
        self, mz: List[float], heights: List[float], errorCode: List[int]
    ) -> None: ...
    def Open(self) -> None: ...
    def UpdateScan(self, scanIndex: int, minMZ: float, maxMZ: float) -> None: ...

class IRetentionTimePeakFinderParameters(object):  # Interface
    RetentionTimePeakWidth: float
    SmoothingStrength: float

class ISignal3D(object):  # Interface
    Intensity: float  # readonly
    MZ: float  # readonly
    RetentionTime: float  # readonly
    Saturated: bool  # readonly
    ScanIndex: int  # readonly

class ISpectralPeakFinderParameters(object):  # Interface
    BaselineToleranceLength: float
    HeightThresholdTypeForProfileData: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectralPeakThresholdType
    )
    HeightThresholdValueForProfileData: float
    MaxPeakWidth: float  # readonly
    MinHeightForPeakDetectedData: float
    MinPeakWidth: float  # readonly
    PreferredAlgorithm: PeakFinderAlgorithmName
    SmoothingStrength: float

    def SetPeakWidthRange(self, min: float, max: float) -> None: ...

class ITargetedMassList(object):  # Interface
    MassList: List[float]
    MassToleranceCoefficients: List[float]
    UseMonoisotopicMass: bool

class IsotopeCharacteristics(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AllElements: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IsotopeCharacteristics
    ) = ...  # static # readonly
    Averagine: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IsotopeCharacteristics
    ) = ...  # static # readonly
    Biological: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IsotopeCharacteristics
    ) = ...  # static # readonly
    CommonCompound: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.IsotopeCharacteristics
    ) = ...  # static # readonly
    Glycan: Agilent.MassSpectrometry.DataAnalysis.MassHunter.IsotopeCharacteristics = (
        ...
    )  # static # readonly

class MfeFilterParameters(CompoundFilters.IGenericCompoundFilterParameters):  # Class
    def __init__(self) -> None: ...

    AbundanceParameters: CompoundFilters.AbundanceFilter.Parameter  # readonly
    LocationRangeParameters: CompoundFilters.LocationRangeFilter.Parameter  # readonly
    MassDefectParameters: CompoundFilters.MassDefectFilter.Parameter  # readonly
    SpecialMassParameters: CompoundFilters.SpecialMassFilter.Parameter  # readonly
    SpecialTimeParameters: CompoundFilters.SpecialTimeFilter.Parameter  # readonly
    TimeMassParameters: CompoundFilters.TimeMassFilter.Parameter  # readonly

    def SetSpecialMassParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        massList: List[float],
        massToleranceCoefficients: List[float],
        lowerLimitsForMassRanges: List[float],
        upperLimitsForMassRanges: List[float],
    ) -> None: ...
    def SetAbundanceParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        largestNCompounds: int,
        minAbsoluteAbundance: float,
        minRelativeAbundance: float,
        useHeightAsMetric: bool,
    ) -> None: ...
    def GetAbundanceParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        largestNCompounds: int,
        minAbsoluteAbundance: float,
        minRelativeAbundance: float,
        useHeightAsMetric: bool,
    ) -> None: ...
    def GetMassDefectParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        peptideLike: bool,
        targetDefectIntercept: float,
        targetDefectSlope: float,
        toleranceInterceptForPositiveDeviation: float,
        toleranceSlopeForPositiveDeviation: float,
        toleranceInterceptForNegativeDeviation: float,
        toleranceSlopeForNegativeDeviation: float,
    ) -> None: ...
    def SetSpecialTimeParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        timeList: List[float],
        timeToleranceCoefficients: List[float],
        lowerLimitsForTimeRanges: List[float],
        upperLimitsForTimeRanges: List[float],
    ) -> None: ...
    def SetMassDefectParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        peptideLike: bool,
        targetDefectIntercept: float,
        targetDefectSlope: float,
        toleranceInterceptForPositiveDeviation: float,
        toleranceSlopeForPositiveDeviation: float,
        toleranceInterceptForNegativeDeviation: float,
        toleranceSlopeForNegativeDeviation: float,
    ) -> None: ...
    def GetSpecialTimeParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        timeList: Sequence[float],
        timeToleranceCoefficients: List[float],
        lowerLimitsForTimeRanges: List[float],
        upperLimitsForTimeRanges: List[float],
    ) -> None: ...
    def GetSpecialMassParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        massList: Sequence[float],
        massToleranceCoefficients: List[float],
        lowerLimitsForMassRanges: List[float],
        upperLimitsForMassRanges: List[float],
    ) -> None: ...
    def GetLocationRangeParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        minRetentionTime: float,
        maxRetentionTime: float,
        minMass: float,
        maxMass: float,
    ) -> None: ...
    def SetLocationRangeParameters(
        self,
        status: Agilent.MassSpectrometry.DataAnalysis.MassHunter.FilterStatus,
        minRetentionTime: float,
        maxRetentionTime: float,
        minMass: float,
        maxMass: float,
    ) -> None: ...

class ProteinFilterParameters(
    CompoundFilters.IProteinFilterParameters,
    Agilent.MassSpectrometry.DataAnalysis.MassHunter.MfeFilterParameters,
    CompoundFilters.IGenericCompoundFilterParameters,
):  # Class
    def __init__(self) -> None: ...

    QualityScoreParameters: CompoundFilters.QualityScoreFilter.Parameter  # readonly
    TimePeakWidthParameters: CompoundFilters.PeakRtWidthFilter.Parameter  # readonly

class SpectraType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    PeakDected: Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectraType = (
        ...
    )  # static # readonly
    Profile: Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectraType = (
        ...
    )  # static # readonly
    Unspecified: Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectraType = (
        ...
    )  # static # readonly

class SpectralPeakThresholdType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Absolute: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectralPeakThresholdType
    ) = ...  # static # readonly
    SNRatio: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectralPeakThresholdType
    ) = ...  # static # readonly
    Unknown: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectralPeakThresholdType
    ) = ...  # static # readonly

class SpectrumSetMetadata:  # Class
    def __init__(self) -> None: ...

    CalibCoeffecientCount: int
    InstrumentType: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSInstrumentType
    )
    InstrumentVersion: str
    MZBinWidthInNS: float
    MaxAcqMZ: float
    MaxCalibratedTimeRangeInNS: float
    MinAcqMZ: float
    MinCalibratedTimeRangeInNS: float
    Polarity: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSPolarity
    )
    SourceType: (
        Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSSourceType
    )

    # Nested Types

    class MSInstrumentType(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        IonTrap: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSInstrumentType
        ) = ...  # static # readonly
        QQQ: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSInstrumentType
        ) = ...  # static # readonly
        QTOF: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSInstrumentType
        ) = ...  # static # readonly
        QUAD: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSInstrumentType
        ) = ...  # static # readonly
        TOF: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSInstrumentType
        ) = ...  # static # readonly
        Unknown: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSInstrumentType
        ) = ...  # static # readonly

    class MSPolarity(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        Negative: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSPolarity
        ) = ...  # static # readonly
        Positive: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSPolarity
        ) = ...  # static # readonly
        Unknown: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSPolarity
        ) = ...  # static # readonly

    class MSSourceType(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        EI: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSSourceType
        ) = ...  # static # readonly
        ESI: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSSourceType
        ) = ...  # static # readonly
        MALDI: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSSourceType
        ) = ...  # static # readonly
        Unkonwn: (
            Agilent.MassSpectrometry.DataAnalysis.MassHunter.SpectrumSetMetadata.MSSourceType
        ) = ...  # static # readonly

class UnitChargeCarrier:  # Struct
    def __init__(self, formula: str, isAnchor: bool) -> None: ...

    Formula: str  # readonly
    IsAnchor: bool  # readonly
