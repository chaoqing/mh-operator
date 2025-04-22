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

from .Agilent.MassSpectrometry.DataAnalysis import (
    IFunction,
    IModificationSpecies,
    IModificationUnit,
    SpectralPeak,
    SpectralPeakFinderParameters,
)
from .Agilent.MassSpectrometry.DataAnalysis.MassHunter import (
    IChemicalAndIonizationParameters,
    IDataRangeParameters,
    IIonSpeciesGroupingRules,
    IProteinFinderParameters,
    IRetentionTimePeakFinderParameters,
    ITargetedMassList,
    SpectrumSetMetadata,
)
from .BasicTypes import (
    ICompoundPrecursorProductDataSet,
    MSProfile,
    PeakList,
    PrecursorIsotopeClusterExtractor,
)
from .Definitions import IMass_TimeSeparatedObject

# Stubs for namespace: Mfe

class Bucket:  # Class
    def __init__(
        self,
        sampleCount: int,
        standardType: Mfe.ObjectCorrelator.StandardUsage,
        time: float,
    ) -> None: ...

    IsStandard: bool  # readonly
    Mass: float  # readonly
    MassSigma: float  # readonly
    NonemtySampleCount: int  # readonly
    ObjectList: List[Mfe.INormalizedObject]  # readonly
    SampleCount: int  # readonly
    StandardTime: float  # readonly
    StandardType: Mfe.ObjectCorrelator.StandardUsage  # readonly

    def GetTime(self, corrected: bool) -> float: ...
    def GetTimeSigma(self, corrected: bool) -> float: ...
    def GetAverageAbundance(
        self, start: int, end: int, treatNullAsZero: bool, normalized: bool
    ) -> float: ...
    def GetMass(self, startSampleIndex: int, endSampleIndex: int) -> float: ...
    def SetObject(self, sampleIndex: int, compound: Mfe.INormalizedObject) -> None: ...
    def GetAbundanceSigma(
        self, start: int, end: int, treatNullAsZero: bool, normalized: bool
    ) -> float: ...

class CefCompound:  # Class
    def __init__(self) -> None: ...

    Formula: str
    IsotopeClusters: Sequence[Mfe.CefIsotopeCluster]
    Name: str
    RetentionTime: float

class CefFile2:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def Read(
        filePath: str,
        extractor: PrecursorIsotopeClusterExtractor,
        setChargeCarrierToProton: bool,
    ) -> List[ICompoundPrecursorProductDataSet]: ...
    @staticmethod
    def ReadCompounds(filePath: str) -> Sequence[Mfe.CefCompound]: ...

class CefIsotopeCluster:  # Class
    def __init__(self) -> None: ...

    IonSpecies: IModificationSpecies
    PeakList: List[SpectralPeak]

class ChromatographyParameters(IRetentionTimePeakFinderParameters):  # Class
    def __init__(self) -> None: ...

    RetentionTimePeakWidth: float
    SmoothingStrength: float

class CompoundFormationParameters(
    Mfe.IEngineBlockUserParameters,
    Mfe.ICompoundFormationParameters,
    IChemicalAndIonizationParameters,
):  # Class
    def __init__(self) -> None: ...

    IonizationInstruction: Mfe.IonizationInstruction  # readonly
    IonizationInstructionNegativeCase: Mfe.IonizationInstruction  # readonly
    IonizationInstructionPositiveCase: Mfe.IonizationInstruction  # readonly
    IsotopeCharacter: Mfe.IsotopeCharacter
    MaxChargeCount: int
    NeutralModifiers: List[IModificationUnit]
    TargetedMassList: Mfe.TargetedMassList  # readonly

    def SetEffectiveChargeAssignmentInstruction(
        self, polarity: SpectrumSetMetadata.MSPolarity
    ) -> None: ...
    def IsEquivalent(self, another: Mfe.CompoundFormationParameters) -> bool: ...
    def FromXml(self, siblings: System.Xml.XmlNodeList) -> None: ...
    def Clone(self) -> Mfe.CompoundFormationParameters: ...
    def ToXml(self, document: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class DataRangeParameters(IDataRangeParameters):  # Class
    def __init__(self) -> None: ...

    MaxMZ: float  # readonly
    MaxRetentionTime: float  # readonly
    MinMZ: float  # readonly
    MinRetentionTime: float  # readonly

    def SetMZRange(self, min: float, max: float) -> None: ...
    def SetRetentionTimeRange(self, min: float, max: float) -> None: ...

class Event:  # Class
    ApexCount: int  # readonly
    def __getitem__(self, localIndex: int) -> float: ...
    Length: int  # readonly
    StartIndex: int  # readonly

    def GetApexHeight(self, apexIndex: int) -> float: ...
    def GetApexLocalLocation(self, apexIndex: int) -> int: ...

class ICompoundFormationParameters(Mfe.IEngineBlockUserParameters):  # Interface
    IsotopeCharacter: Mfe.IsotopeCharacter
    MaxChargeCount: int

class IDataSelectionParameters(object):  # Interface
    MaxMZ: float  # readonly
    MaxRetentionTime: float  # readonly
    MinMZ: float  # readonly
    MinRetentionTime: float  # readonly
    RTSmoothingHalfTaperSpan: float

    def SetMZRange(self, min: float, max: float) -> None: ...
    def SetRetentionTimeRange(self, min: float, max: float) -> None: ...

class IEngineBlockUserParameters(object):  # Interface
    ...

class IMfeCompoundParameters(Mfe.IMfeUserParameters):  # Interface
    CompoundFormationParameters: Mfe.ICompoundFormationParameters  # readonly
    Peak3DDetectionParameters: Mfe.IPeak3DDetectionParameters  # readonly

class IMfeProteinParameters(Mfe.IMfeUserParameters):  # Interface
    Peak3DDetectionParameters: Mfe.IPeak3DDetectionParameters  # readonly
    ProteinFormationParameters: Mfe.IProteinFormationParameters  # readonly

class IMfeUserParameters(object):  # Interface
    PeakFindParameters: Mfe.IPeakFindParameters  # readonly

    def Clone(self) -> Mfe.IMfeUserParameters: ...

class INormalizedObject(object):  # Interface
    InputObject: IMass_TimeSeparatedObject  # readonly
    Mass: float  # readonly
    NormalizationFactor: float  # readonly

    def GetTime(self, corrected: bool) -> float: ...
    def GetAbundance(self, useNormalized: bool) -> float: ...

class IPeak3DDetectionParameters(Mfe.IEngineBlockUserParameters):  # Interface
    MaxNumberOfSpectralPeaks: int

class IPeakFindParameters(Mfe.IEngineBlockUserParameters):  # Interface
    ChromatographyParameters: Mfe.ChromatographyParameters  # readonly
    DataRangeParameters: Mfe.DataRangeParameters  # readonly
    SpectralPeakFinderParameters: SpectralPeakFinderParameters  # readonly

class IProteinFormationParameters(Mfe.IEngineBlockUserParameters):  # Interface
    ...

class ISpectralPeakPicker(object):  # Interface
    def FindPeaks(
        self,
        spectrum: List[float],
        events: List[Mfe.Event],
        peakWidthModel: IFunction,
        minDistance: float,
        maxValleyHeightForDecoupled: float,
        heightThreshold: IFunction,
        rejectOverlappingPeaks: bool,
    ) -> List[PeakAdapter]: ...

class IonizationInstruction(IIonSpeciesGroupingRules):  # Class
    def __init__(self, polarity: SpectrumSetMetadata.MSPolarity) -> None: ...

    Adducts: List[Mfe.IonizationInstruction.Adduct]
    DefaulChargeUnit: IModificationUnit

    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(self, another: Mfe.IonizationInstruction) -> bool: ...
    def GetHashCode(self) -> int: ...
    def FromXml(self, data: System.Xml.XmlElement) -> None: ...
    def Clone(self) -> Mfe.IonizationInstruction: ...
    def ToXml(
        self, document: System.Xml.XmlDocument, title: str
    ) -> System.Xml.XmlElement: ...

    # Nested Types

    class Adduct:  # Struct
        def __init__(self, ChargeUnit: IModificationUnit, isAncher: bool) -> None: ...

        ChargeUnit: IModificationUnit  # readonly
        IsAnchor: bool

        def Clone(self) -> Mfe.IonizationInstruction.Adduct: ...

class IsotopeCharacter(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AllElements: Mfe.IsotopeCharacter = ...  # static # readonly
    Averagine: Mfe.IsotopeCharacter = ...  # static # readonly
    Biological: Mfe.IsotopeCharacter = ...  # static # readonly
    C_Halogen: Mfe.IsotopeCharacter = ...  # static # readonly
    C_OneLi: Mfe.IsotopeCharacter = ...  # static # readonly
    Glycan: Mfe.IsotopeCharacter = ...  # static # readonly

class MS2File:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def ReadData(
        filePath: str,
        precursorPeaks: List[SpectralPeak],
        precursorZ: int,
        precursorIonSpecies: IModificationSpecies,
        productPeaks: List[SpectralPeak],
    ) -> bool: ...

class MfeCompoundParameters(
    Mfe.IMfeCompoundParameters, Mfe.IMfeUserParameters
):  # Class
    def __init__(self) -> None: ...

    CompoundFormationParameters: Mfe.ICompoundFormationParameters
    Peak3DDetectionParameters: Mfe.IPeak3DDetectionParameters
    PeakFindParameters: Mfe.IPeakFindParameters

    def Clone(self) -> Mfe.IMfeUserParameters: ...

class MfeInfusionParameters(Mfe.IMfeUserParameters):  # Class
    def __init__(self) -> None: ...

    CompoundFormationParameters: Mfe.ICompoundFormationParameters
    PeakFindParameters: Mfe.IPeakFindParameters

    def Clone(self) -> Mfe.IMfeUserParameters: ...

class MfeProteinParameters(Mfe.IMfeProteinParameters, Mfe.IMfeUserParameters):  # Class
    def __init__(self) -> None: ...

    Peak3DDetectionParameters: Mfe.IPeak3DDetectionParameters
    PeakFindParameters: Mfe.IPeakFindParameters
    ProteinFormationParameters: Mfe.IProteinFormationParameters

    def Clone(self) -> Mfe.IMfeUserParameters: ...

class MmcFile:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def Read(
        filePath: str, extractor: PrecursorIsotopeClusterExtractor
    ) -> ICompoundPrecursorProductDataSet: ...

class ObjectCorrelator:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def Run(
        objectLists: List[Sequence[IMass_TimeSeparatedObject]],
        customerNormalizationFactors: List[float],
        parameters: Mfe.ObjectCorrelator.UserParameters,
    ) -> List[Mfe.Bucket]: ...

    # Nested Types

    class CalibrationStandard:  # Struct
        Mass: float
        StandardUsage: Mfe.ObjectCorrelator.StandardUsage
        Time: float

    class IntensityNormalizationChoice(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        UseCustomerFactor: Mfe.ObjectCorrelator.IntensityNormalizationChoice = (
            ...
        )  # static # readonly
        UseOverallAbundance: Mfe.ObjectCorrelator.IntensityNormalizationChoice = (
            ...
        )  # static # readonly
        UseOverallHeight: Mfe.ObjectCorrelator.IntensityNormalizationChoice = (
            ...
        )  # static # readonly
        UseStandardsByAbundance: Mfe.ObjectCorrelator.IntensityNormalizationChoice = (
            ...
        )  # static # readonly
        UseStandardsByHeight: Mfe.ObjectCorrelator.IntensityNormalizationChoice = (
            ...
        )  # static # readonly

    class StandardUsage(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        AbundanceOnly: Mfe.ObjectCorrelator.StandardUsage = ...  # static # readonly
        TimeAndAbundance: Mfe.ObjectCorrelator.StandardUsage = ...  # static # readonly
        TimeOnly: Mfe.ObjectCorrelator.StandardUsage = ...  # static # readonly

    class TimeCorrectionChoice(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        Auto: Mfe.ObjectCorrelator.TimeCorrectionChoice = ...  # static # readonly
        UseStandards: Mfe.ObjectCorrelator.TimeCorrectionChoice = (
            ...
        )  # static # readonly

    class UserParameters:  # Class
        def __init__(self) -> None: ...

        CustomerSampleNormalizationFactors: List[float]
        IntensityNormalizationChoice: Mfe.ObjectCorrelator.IntensityNormalizationChoice
        MassToleranceFunction: IFunction
        Standards: List[Mfe.ObjectCorrelator.CalibrationStandard]
        TimeCorrectionChoice: Mfe.ObjectCorrelator.TimeCorrectionChoice
        TimeToleranceFunctionForCorrection: IFunction
        TimeToleranceFunctionForCorrelation: IFunction

        def FromXml(self, siblings: System.Xml.XmlNodeList) -> None: ...
        @staticmethod
        def CreateRtInsensitiveParameters(
            userInput: Mfe.ObjectCorrelator.UserParameters,
        ) -> Mfe.ObjectCorrelator.UserParameters: ...
        def ToXml(self, document: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class PeakFindParameters(
    Mfe.IPeakFindParameters, Mfe.IEngineBlockUserParameters
):  # Class
    def __init__(self) -> None: ...

    ChromatographyParameters: Mfe.ChromatographyParameters  # readonly
    DataRangeParameters: Mfe.DataRangeParameters  # readonly
    SpectralPeakFinderParameters: SpectralPeakFinderParameters  # readonly

    def Clone(self) -> Mfe.PeakFindParameters: ...

class PeakFinder:  # Class
    def __init__(
        self,
        userParameters: SpectralPeakFinderParameters,
        peakWidthInMZ: IFunction,
        tofDataTimeInterval: float,
    ) -> None: ...

    NoninterestingMZ: float  # static # readonly

    def PeakFullyProcessedData(self) -> MSProfile: ...
    def PeekBaseline(self) -> MSProfile: ...
    def FindPeaks(self, raw: MSProfile) -> PeakList: ...
    def PeakIntensityThresholdLevel(self) -> MSProfile: ...
    def PeekSmoothedData(self) -> MSProfile: ...
    def PeekBaselineRemovedData(self) -> MSProfile: ...

class ProteinFormationParameters(
    IProteinFinderParameters,
    Mfe.IEngineBlockUserParameters,
    Mfe.IProteinFormationParameters,
):  # Class
    def __init__(self) -> None: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(self, another: Mfe.ProteinFormationParameters) -> bool: ...
    def GetHashCode(self) -> int: ...
    def Clone(self) -> Mfe.ProteinFormationParameters: ...

class TargetedMassList(ITargetedMassList):  # Class
    def __init__(self) -> None: ...

    Length: int  # readonly
    ToleranceFunction: IFunction  # readonly

    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(self, another: Mfe.TargetedMassList) -> bool: ...
    def GetHashCode(self) -> int: ...
    def Clone(self) -> Mfe.TargetedMassList: ...
