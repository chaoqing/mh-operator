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
    CeCompositeSpectraMakingScheme,
    IFunction,
    IIonSpeciesDetails,
    IIsotopeClusterBase,
    IModificationSpecies,
    IModificationUnit,
    IsolationWindowType,
    SpectralPeak,
)
from .Agilent.MassSpectrometry.DataAnalysis.MassHunter import (
    CompoundFilterParameters,
    IChargeState,
    ICoelutionGroup,
    ICompound,
    IIsotope,
    IIsotopeCluster,
    IProtein,
    IRawSpectrumAccessor,
    ISignal3D,
    IsotopeCharacteristics,
    SpectrumSetMetadata,
)
from .Biochemistry import CompositionModel
from .CompoundFilters import IFilterable, IFilterableMfe
from .Definitions import IMass_TimeSeparatedObject
from .Mathematics import ClusteringSequential, RangeDouble, RangeInt, Regression, Vector
from .Mfe import IsotopeCharacter

# Stubs for namespace: BasicTypes

class AlternativeIonSpecies:  # Class
    @staticmethod
    def Parse(
        expression: str,
        multimerNumber: int,
        adducts: str,
        isProtonated: bool,
        neutralModification: str,
    ) -> None: ...

class CXY(BasicTypes.OrderedXY):  # Class
    def __init__(self) -> None: ...

class CalibReader:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def ReadCalib(spectrumAccessor: IRawSpectrumAccessor) -> BasicTypes.TOFCalib: ...

class ChromMetadata:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        ionization: BasicTypes.Ionization,
        instrumentInfo: BasicTypes.ChromMetadata.InstrumentInfo,
    ) -> None: ...
    @overload
    def __init__(
        self, accessor: IRawSpectrumAccessor, highResolutino: bool
    ) -> None: ...

    AcqRTRange: RangeDouble
    AcqSpectralXRange: RangeDouble
    CalibratedTimeRangeInNS: RangeDouble
    CurrentRTRange: RangeDouble  # readonly
    CurrentScanCount: int  # readonly
    CurrentSpectralXRange: RangeDouble
    FullSaturationLevel: float
    Ionization: BasicTypes.Ionization
    IsotopesUnresovled: bool
    MSLevel: int
    MZErrorFunction: BasicTypes.ChromMetadata.MZError  # readonly
    MZPeakWidthFunction: IFunction  # readonly
    ProfileSpectraAvailable: bool
    RTPeakWidth: float
    ScanRate: float  # readonly
    ScanTimes: List[float]
    ScanWidths: List[float]  # readonly
    TheInstrumentInfo: BasicTypes.ChromMetadata.InstrumentInfo

    def GetNearestScanIndex(self, rt: float) -> int: ...
    def GetScanRange(self, rtRange: RangeDouble) -> RangeInt: ...
    def TruncateScanRange(self, scanRange: RangeInt) -> None: ...
    def Clone(self) -> BasicTypes.ChromMetadata: ...

    # Nested Types

    class InstrumentInfo:  # Class
        def __init__(self, type: SpectrumSetMetadata.MSInstrumentType) -> None: ...

        Type: SpectrumSetMetadata.MSInstrumentType
        Version: str

    class MZError:  # Class
        def __init__(
            self, coeffHighSNRCase: List[float], coeffLowSNRCase: List[float]
        ) -> None: ...
        def LowSNRCase(self, mz: float, scalingFactor: float) -> float: ...
        def HighSNRCoeff(self, scalingFactor: float) -> List[float]: ...
        def Clone(self) -> BasicTypes.ChromMetadata.MZError: ...
        def LowSNRCoeff(self, scalingFactor: float) -> List[float]: ...
        def HighSNRCase(self, mz: float, scalingFactor: float) -> float: ...

class Chromatogram(BasicTypes.CXY):  # Class
    @overload
    def __init__(self, rt: List[float]) -> None: ...
    @overload
    def __init__(self, rt: List[float], intensities: List[float]) -> None: ...
    def __getitem__(self, i: int) -> float: ...
    def __setitem__(self, i: int, value_: float) -> None: ...
    Length: int  # readonly
    RTRange: RangeDouble  # readonly
    ScanTimes: List[float]  # readonly

    def RT2Scan(self, rt: float) -> float: ...
    def ApplyTimeShiftCorrection(
        self, shiftModel: Regression, factor: float
    ) -> None: ...
    @staticmethod
    def NewCalculatePeakWidth(
        centroid: float, data: List[BasicTypes.Signal3D]
    ) -> float: ...
    def GetX(self, index: int) -> float: ...
    def GetY(self, index: int) -> float: ...
    def GetNearestScan(self, rt: float) -> int: ...
    @staticmethod
    def CalculatePeakWidth(
        centroid: float, data: List[BasicTypes.Signal3D]
    ) -> float: ...

class CoelutionGroup(ICoelutionGroup):  # Class
    @overload
    def __init__(self, compounds: List[Any]) -> None: ...
    @overload
    def __init__(self) -> None: ...

    AllPeaks: System.Collections.Generic.List[BasicTypes.Peak]  # readonly
    Compounds: List[ICompound]  # readonly
    ID: int
    MaxVolume: float  # readonly
    RT: float  # readonly
    RetentionTime: float  # readonly
    Saturated: bool  # readonly

    def Split(
        self, maxRTSpread: float, penalityCompoundCount: float
    ) -> System.Collections.Generic.List[BasicTypes.CoelutionGroup]: ...
    @staticmethod
    def GetCoelutionGroups(
        compounds: List[BasicTypes.MfeCompound],
        filterParameters: CompoundFilterParameters,
        maxGroupSpread: float,
    ) -> List[BasicTypes.CoelutionGroup]: ...
    def SortCompoundsByAbundance(self) -> None: ...

class CompoundInfo(BasicTypes.ICompoundInfo):  # Class
    def __init__(
        self, compoundName: str, formula: str, molfile: str, retentionTime: float
    ) -> None: ...

    CompoundName: str  # readonly
    Formula: str  # readonly
    IonSource: SpectrumSetMetadata.MSSourceType  # readonly
    Molfile: str  # readonly
    RetentionTime: float  # readonly

class EICCollection:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        template: BasicTypes.EICCollection,
        signals: System.Collections.Generic.List[BasicTypes.Signal3D],
    ) -> None: ...
    @overload
    def __init__(
        self,
        resolutionBinStarts: List[float],
        signalBinBoundaries: List[float],
        signals: System.Collections.Generic.List[BasicTypes.Signal3D],
    ) -> None: ...
    @overload
    def __init__(
        self,
        resolutionBinStarts: List[float],
        mzSortedBins: List[BasicTypes.EICCollection.SignalBin],
    ) -> None: ...

    BinCount: int  # readonly
    IsBinned: bool  # readonly
    ResolutionBinStarts: List[float]  # readonly
    SignalBinBoundaries: List[float]  # readonly
    SignalBins: List[BasicTypes.EICCollection.SignalBin]  # readonly

    def FindResolutionBinRange(self, spectralXRange: RangeDouble) -> RangeInt: ...
    def RoundupRange(
        self, mzRange: RangeDouble, binChoice: BasicTypes.XYCollection.EICBinChoice
    ) -> RangeDouble: ...
    def SetBinningInfo(
        self,
        resulotionBinStarts: List[float],
        signalBins: List[BasicTypes.EICCollection.SignalBin],
    ) -> None: ...
    def GetResolutionBinUpperBoundary(self, mz: float) -> float: ...
    @overload
    def GetMZRange(self, binIndex: int) -> RangeDouble: ...
    @overload
    def GetMZRange(self, binRange: RangeInt) -> RangeDouble: ...
    def GetNoiseLevel(self, bin: int, scan: int) -> float: ...
    def GetBinRange(self, mz: float) -> RangeDouble: ...
    def SetNoiseLevels(
        self, noiseLevels: System.Collections.Generic.List[Vector]
    ) -> None: ...
    def GetBinCenter(self, bin: int) -> float: ...
    def FindBin(self, mz: float) -> int: ...
    def ClearSegment(self, binRange: RangeInt) -> None: ...
    def FindResolutionBin(self, mz: float) -> int: ...

    # Nested Types

    class SignalBin:  # Class
        def __init__(self) -> None: ...

        Centroid: float
        NoiseLevel: Vector
        NonZeroSignals: System.Collections.Generic.List[BasicTypes.Signal3D]
        StartingLoc: float
        StorageOffset: int

        SignalCount: int

        def SetSignalInfo(
            self, storageOffset: int, qualifiedSignalCount: int
        ) -> None: ...
        def EIC(self, scanCount: int) -> List[float]: ...

class FragmentDataInfo:  # Class
    def __init__(self) -> None: ...

    CeCompositeScheme: CeCompositeSpectraMakingScheme
    FragmentInfo: BasicTypes.FragmentSpectraInfo
    UseFormulasInFiles: bool

    def Clone(self) -> BasicTypes.FragmentDataInfo: ...
    def BinaryWrite(self, writer: System.IO.BinaryWriter) -> None: ...
    def BinaryRead(self, reader: System.IO.BinaryReader) -> None: ...

class FragmentIon:  # Class
    def __init__(
        self,
        isotopePeaks: List[SpectralPeak],
        z: int,
        trueFrgament: bool,
        hasIsotopeData: bool,
        isotopePatternIntact: bool,
    ) -> None: ...

    HasIsotopeData: bool  # readonly
    Height: float  # readonly
    Intensity: float  # readonly
    IonMass: float  # readonly
    IsotopePatternIntact: bool  # readonly
    NeutralizedMass: float  # readonly
    SpectralPeaks: List[SpectralPeak]  # readonly
    TrueFragment: bool  # readonly
    Z: int  # readonly

class FragmentSpectraInfo:  # Class
    def __init__(self) -> None: ...

    FragmentHeightAccuracy: float  # static
    FragmentMassAccuracy: List[float]  # static
    HeightAccuracy: float
    IsolationWindow: IsolationWindowType
    IsotopeCharacteristics: IsotopeCharacteristics
    MassAccurancyCoefficients: List[float]
    MaxFragmentIonCount: int
    MaxIonMass: float
    MinSNRatio: float
    ParentIsPortonated: bool
    TreatHeavestIonAsParent: bool

    def Clone(self) -> BasicTypes.FragmentSpectraInfo: ...
    def BinaryWrite(self, writer: System.IO.BinaryWriter) -> None: ...
    def BinaryRead(self, reader: System.IO.BinaryReader) -> None: ...

class GenericCompound(IFilterable, IMass_TimeSeparatedObject):  # Class
    def __init__(self, time: float, mass: float, abundance: float) -> None: ...

    Abundance: float  # readonly
    Height: float  # readonly
    ID: str  # readonly
    Mass: float  # readonly
    RetentionTime: float  # readonly
    SeparationTime: float  # readonly

class IChromatographyObject(object):  # Interface
    RT: float  # readonly

class ICompoundInfo(object):  # Interface
    CompoundName: str  # readonly
    Formula: str  # readonly
    IonSource: SpectrumSetMetadata.MSSourceType  # readonly
    Molfile: str  # readonly
    RetentionTime: float  # readonly

class ICompoundPrecursorProductDataSet(object):  # Interface
    CompoundInfo: BasicTypes.ICompoundInfo  # readonly
    PrecursorDataSets: Sequence[BasicTypes.IPrecursorDataSet]  # readonly

    def GetTotalProductSpectraCount(self) -> int: ...

class IIntensity2D(BasicTypes.ILocation2D):  # Interface
    Intensity: float  # readonly

class ILocation2D(object):  # Interface
    XLocation: float  # readonly
    YLocation: float  # readonly

class IPrecursorDataSet(object):  # Interface
    EIData: bool  # readonly
    IonSpecies: IModificationSpecies  # readonly
    IsolationWindow: IsolationWindowType  # readonly
    PrecursorFullSaturation: float  # readonly
    PrecursorIsotopePeaks: List[SpectralPeak]  # readonly
    PrecursorMz: float  # readonly

    def GetPrecursorZ(self, zValueNeedsConfirm: bool) -> int: ...
    def GetCollisionEnergies(self) -> Sequence[float]: ...
    def GetProductSpectraFullSaturation(self, collisionEnergy: float) -> float: ...
    def GetProductSpectrum(self, collisionEnergy: float) -> List[SpectralPeak]: ...
    def GetProductCompositeSpectrum(
        self,
        scheme: CeCompositeSpectraMakingScheme,
        productMassErrorCoefficients: List[float],
    ) -> List[SpectralPeak]: ...
    def ConfirmZValue(self) -> None: ...

class IRTShiftable(BasicTypes.IIntensity2D, BasicTypes.ILocation2D):  # Interface
    def ShiftRT(self, shiftModel: Regression, factor: float) -> None: ...

class ISpectrum(object):  # Interface
    Calib: BasicTypes.TOFCalib
    RT: float
    SignalCount: int  # readonly
    SummedHeight: float  # readonly

    def CalculateSummmedHeight(
        self, XRange: RangeDouble, searchStartSignalIndex: int
    ) -> float: ...
    def GetImage(self, binRange: RangeInt) -> List[float]: ...

class IonSpeciesAdapter(IIonSpeciesDetails):  # Class
    def __init__(self, species: IModificationSpecies) -> None: ...

    BaseCount: int
    ElectronCount: int
    ModifierCount: int
    ModifierFormula: str
    NeutralLoss: str
    ShorthandSpeciesFormula: str  # readonly

class Ionization:  # Class
    @overload
    def __init__(
        self,
        type: SpectrumSetMetadata.MSSourceType,
        polarity: SpectrumSetMetadata.MSPolarity,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    BaseChargeUnit: IModificationUnit  # readonly
    ThePolarity: SpectrumSetMetadata.MSPolarity
    TheSourceType: SpectrumSetMetadata.MSSourceType

class IonizationChargeType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Electron: BasicTypes.IonizationChargeType = ...  # static # readonly
    Proton: BasicTypes.IonizationChargeType = ...  # static # readonly
    Unkonwn: BasicTypes.IonizationChargeType = ...  # static # readonly

class IsotopeCluster(IIsotopeClusterBase, IIsotopeCluster):  # Class
    @overload
    def __init__(
        self,
        peaks: BasicTypes.PeakList,
        lowestIsotopeMZ: float,
        ionSpecies: IModificationSpecies,
        rtWidth: float,
        isotopeCharacter: IsotopeCharacter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        peaks: BasicTypes.PeakList,
        missingLeadingPeakCount: int,
        lowestIsotopeMZ: float,
        ionSpecies: IModificationSpecies,
        rtWidth: float,
        isotopeCharacter: IsotopeCharacter,
        qScore: float,
    ) -> None: ...
    @overload
    def __init__(
        self, chargeCount: int, isotopeCharacter: IsotopeCharacter
    ) -> None: ...
    @overload
    def __init__(
        self, p: BasicTypes.Peak, chargeCount: int, isotopeCharacter: IsotopeCharacter
    ) -> None: ...
    @overload
    def __init__(
        self,
        pks: BasicTypes.PeakList,
        chargeCount: int,
        isotopeCharacter: IsotopeCharacter,
    ) -> None: ...
    @overload
    def __init__(self, cluster: BasicTypes.IsotopeCluster) -> None: ...
    @overload
    def __init__(self, cluster: BasicTypes.IsotopeCluster, scale: float) -> None: ...
    @overload
    def __init__(
        self, cluster: BasicTypes.IsotopeCluster, isotopeCharacter: IsotopeCharacter
    ) -> None: ...
    @overload
    def __init__(
        self, pks: BasicTypes.PeakList, ionSpeciesExpression: str, z: int
    ) -> None: ...

    Abundance: float  # readonly
    AverageMZ: float  # readonly
    AverageMass: float  # readonly
    ChargeCount: int
    ContiguousPeakLength: int  # readonly
    IonSpecies: IModificationSpecies
    IonSpeciesDetails: IIonSpeciesDetails  # readonly
    IonSpeciesExpression: str  # readonly
    IsProtonated: bool  # readonly
    IsotopeCharacter: IsotopeCharacter  # readonly
    Isotopes: List[IIsotope]  # readonly
    Length: int  # readonly
    LowestIsotopeMZ: float  # readonly
    MassSpread: float  # readonly
    MaxEicSNRatio: float  # readonly
    MaxHeight: float  # readonly
    MissingLeadingPeakCount: int
    MonomerLowestIsotopeMass: float  # readonly
    MultimerNumber: int  # readonly
    NeutralModifications: List[IModificationUnit]  # readonly
    Peaks: BasicTypes.PeakList  # readonly
    PredictedM0FromEachIon: List[float]  # readonly
    QScore: float
    QualityScore: float
    RT: float  # readonly
    RTDeviation: float  # readonly
    RTWidth: float  # readonly
    RetentionTime: float  # readonly
    RetentionTimePeakWidth: float  # readonly
    Saturated: bool  # readonly
    SaturationCorrectedIsotopePattern: List[SpectralPeak]  # readonly
    SpectralPeaks: List[SpectralPeak]  # readonly
    SummedIntensity: float  # readonly
    TotalVolumeExcludingSaturatePart: float  # readonly
    Volume: float  # readonly
    Z: int  # readonly

    def DropInfoLevelTo(self, infoLevel: BasicTypes.MfeCompound.InfoLevel) -> None: ...
    def RedoStatistics(self) -> None: ...
    @staticmethod
    def Merge(
        clusterA: BasicTypes.IsotopeCluster, clusterB: BasicTypes.IsotopeCluster
    ) -> BasicTypes.IsotopeCluster: ...
    @staticmethod
    def ConstructGapPeaks(
        anchor1: BasicTypes.Peak,
        anchor2: BasicTypes.Peak,
        gap: int,
        templete: BasicTypes.Peak,
    ) -> List[BasicTypes.Peak]: ...
    def CalculateRTTruncationBias(self) -> float: ...
    def IsPeakSaturated(self, peakIndex: int) -> bool: ...
    @staticmethod
    def SimplyMerge(
        cluster1: BasicTypes.IsotopeCluster, cluster2: BasicTypes.IsotopeCluster
    ) -> BasicTypes.IsotopeCluster: ...
    def GetSaturationCorrectedIsotopePattern(self) -> BasicTypes.PeakList: ...
    def TrimExtraLeadingPeakIfNeccessary(self) -> None: ...
    @staticmethod
    def EstimateMissingLeadingPeakCount(
        model: CompositionModel,
        mass: float,
        clusters: Sequence[Dict[int, BasicTypes.Peak]],
    ) -> int: ...

    # Nested Types

    class Comparer(
        System.Collections.Generic.IComparer[BasicTypes.IsotopeCluster]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self, c1: BasicTypes.IsotopeCluster, c2: BasicTypes.IsotopeCluster
        ) -> int: ...

class MSProfile(BasicTypes.CXY, BasicTypes.ISpectrum):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        spectrumAccessor: IRawSpectrumAccessor,
        scanIndex: int,
        mzRange: RangeDouble,
    ) -> None: ...
    @overload
    def __init__(self, spectrumAccessor: IRawSpectrumAccessor, rt: float) -> None: ...
    @overload
    def __init__(
        self, spectrumAccessor: IRawSpectrumAccessor, rt: float, mzRange: RangeDouble
    ) -> None: ...
    @overload
    def __init__(
        self,
        spectrumAccessor: IRawSpectrumAccessor,
        rtRange: RangeDouble,
        mzRange: RangeDouble,
        requiredType: BasicTypes.XYCollection.SpectrumType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        spectrumAccessor: IRawSpectrumAccessor,
        centerScanIndex: int,
        taper: List[float],
        taperStartIndex: int,
        mzRange: RangeDouble,
    ) -> None: ...
    @overload
    def __init__(
        self, intensities: List[float], x0: float, deltaT: float, rt: float
    ) -> None: ...

    Calib: BasicTypes.TOFCalib
    DataArray: List[float]  # readonly
    FullSaturationLevel: float  # readonly
    Length: int  # readonly
    Peaks: BasicTypes.PeakList
    RT: float
    SignalCount: int  # readonly
    SummedHeight: float  # readonly
    X0: float

    def GetIndex(self, mz: float) -> int: ...
    @staticmethod
    def SpectraCompatible(
        s1: BasicTypes.MSProfile, s2: BasicTypes.MSProfile
    ) -> bool: ...
    def GetImage(self, binRange: RangeInt) -> List[float]: ...
    def GetX(self, index: int) -> float: ...
    def GetY(self, index: int) -> float: ...
    def CreatePeakWidthProportionalModelInIndex(
        self, widthInMZ: IFunction, scalingFactor: float
    ) -> IFunction: ...
    def Clone(self, intensities: List[float]) -> BasicTypes.MSProfile: ...
    @staticmethod
    def CreateStackedSpectrum(
        spectrumAccessor: IRawSpectrumAccessor,
        rtRange: RangeDouble,
        mzRange: RangeDouble,
        doAveraging: bool,
    ) -> BasicTypes.MSProfile: ...
    def CalculateSummmedHeight(
        self, xRange: RangeDouble, searchStartSignalIndex: int
    ) -> float: ...

class MSProfileCompressed(BasicTypes.ISpectrum, BasicTypes.MSProfile):  # Class
    def __init__(self) -> None: ...

    HighSignals: List[int]
    Length: int  # readonly
    LowSignals: List[int]
    MediumSignals: List[int]

    def SetData(self, rawData: List[int]) -> int: ...
    def GetData(self, requiredLength: int) -> List[int]: ...
    def GetImage(self, binRange: RangeInt) -> List[float]: ...

class MfeCompound(
    BasicTypes.IChromatographyObject,
    ICompound,
    IMass_TimeSeparatedObject,
    IFilterableMfe,
    IFilterable,
):  # Class
    @overload
    def __init__(self, main: BasicTypes.IsotopeCluster) -> None: ...
    @overload
    def __init__(self) -> None: ...

    Abundance: float  # readonly
    AllPeaks: BasicTypes.PeakList  # readonly
    AverageMass: float  # readonly
    AverageMassStandardDeviation: float  # readonly
    Clusters: System.Collections.Generic.List[BasicTypes.IsotopeCluster]
    HasOnlySingleIon: bool  # readonly
    Height: float  # readonly
    Intensity: float  # readonly
    IsotopeCharacter: IsotopeCharacter  # readonly
    IsotopeClusters: List[IIsotopeCluster]  # readonly
    LightestCluster: BasicTypes.IsotopeCluster  # readonly
    LowestIsotopeMass: float
    Mass: float  # readonly
    MassSpread: float  # readonly
    MassStandardDeviation: float  # readonly
    MaxHeight: float  # readonly
    MaxVolume: float  # readonly
    MostReliableCluster: BasicTypes.IsotopeCluster
    MostReliableIsotopeCluster: IIsotopeCluster  # readonly
    QScore: float
    QualityScore: float
    RT: float
    RTDeviation: float  # readonly
    RTWidth: float
    RetentionTime: float  # readonly
    RetentionTimePeakWidth: float  # readonly
    Saturated: bool  # readonly
    SeparationTime: float  # readonly
    Volume: float
    XLocation: float  # readonly
    YLocation: float  # readonly
    ZRange: RangeInt
    ZStateCount: int  # readonly
    ZStates: List[int]  # readonly

    def DropInfoLevelTo(self, infoLevel: BasicTypes.MfeCompound.InfoLevel) -> None: ...
    def RedoStatistics(self) -> None: ...
    def Add(self, cluster: BasicTypes.IsotopeCluster) -> None: ...
    @overload
    @staticmethod
    def SortListBy(
        compounds: List[Any],
        sortingType: BasicTypes.MfeCompound.SortingType,
        ascending: bool,
    ) -> None: ...
    @overload
    @staticmethod
    def SortListBy(
        compounds: List[BasicTypes.MfeCompound],
        sortingType: BasicTypes.MfeCompound.SortingType,
        ascending: bool,
    ) -> None: ...
    def SetIsotopeClusters(
        self, clusters: System.Collections.Generic.List[BasicTypes.IsotopeCluster]
    ) -> None: ...

    # Nested Types

    class Comparer(
        System.Collections.Generic.IComparer[ICompound],
        System.Collections.IComparer,
        System.Collections.Generic.IComparer[BasicTypes.MfeCompound],
    ):  # Class
        def __init__(
            self, type: BasicTypes.MfeCompound.SortingType, ascending: bool
        ) -> None: ...
        @overload
        def Compare(self, o1: Any, o2: Any) -> int: ...
        @overload
        def Compare(
            self, c1: BasicTypes.MfeCompound, c2: BasicTypes.MfeCompound
        ) -> int: ...
        @overload
        def Compare(self, c1: ICompound, c2: ICompound) -> int: ...

    class InfoLevel(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        MostDetailed: BasicTypes.MfeCompound.InfoLevel = ...  # static # readonly
        WithoutIonRTProfiles: BasicTypes.MfeCompound.InfoLevel = (
            ...
        )  # static # readonly
        WithoutIsotopeClusterInfo: BasicTypes.MfeCompound.InfoLevel = (
            ...
        )  # static # readonly

    class SortingType(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        ByMass: BasicTypes.MfeCompound.SortingType = ...  # static # readonly
        ByRT: BasicTypes.MfeCompound.SortingType = ...  # static # readonly
        ByVolume: BasicTypes.MfeCompound.SortingType = ...  # static # readonly

class ModificationSpecies(IModificationSpecies):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, baseCount: int, modifications: BasicTypes.ModificationUnitCollection
    ) -> None: ...
    @overload
    def __init__(
        self, modificationUnit: str, zPerUnit: int, unitCount: int
    ) -> None: ...
    @overload
    def __init__(self, modificationUnit: IModificationUnit, unitCount: int) -> None: ...
    @overload
    def __init__(self, oldStyle: IIonSpeciesDetails) -> None: ...

    ElectronGain: IModificationSpecies  # static
    ElectronLoss: IModificationSpecies  # static
    ProtonGain: IModificationSpecies  # static
    ProtonLoss: IModificationSpecies  # static
    UnknownSpeciesMessage: str  # static # readonly

    BaseCount: int  # readonly
    IsInUndeterminedState: bool  # readonly
    Modifications: Dict[IModificationUnit, int]  # readonly

    @staticmethod
    def ParseCefFormat(
        CefFormat: str, z: int, isotopeIndex: int
    ) -> IModificationSpecies: ...
    def BinaryWrite(self, writer: System.IO.BinaryWriter) -> None: ...
    @overload
    @staticmethod
    def CreateDefaultIonSpecies(
        z: int, ionSource: SpectrumSetMetadata.MSSourceType
    ) -> IModificationSpecies: ...
    @overload
    @staticmethod
    def CreateDefaultIonSpecies(
        z: int, chargeType: BasicTypes.IonizationChargeType
    ) -> IModificationSpecies: ...
    def BinaryRead(self, reader: System.IO.BinaryReader) -> None: ...

class ModificationUnitCollection:  # Class
    def __init__(self) -> None: ...
    def Add(self, unit: IModificationUnit, count: int) -> None: ...

class OrderedXY:  # Class
    def __init__(self) -> None: ...

    Length: int  # readonly
    SummedIntensity: float  # readonly
    XRange: RangeDouble  # readonly

    def GetIndexLeftOf(self, x: float) -> int: ...
    def GetX(self, index: int) -> float: ...
    def GetY(self, index: int) -> float: ...
    def GetNearestIndex(self, x: float) -> int: ...
    def SumIntensity(self, range: RangeDouble, intialStartingIndex: int) -> float: ...

class ParentFragmentData:  # Class
    @overload
    def __init__(
        self,
        parentLowestMZ: float,
        parentZ: int,
        deisotopedFragmentPeaks: List[SpectralPeak],
        fragmentZs: List[int],
        parameter: BasicTypes.ParentFragmentData.Parameter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        parentClusterPeaks: List[SpectralPeak],
        parentZ: int,
        fragmentSpectra: List[SpectralPeak],
        parameter: BasicTypes.ParentFragmentData.Parameter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        parentMz: float,
        parentZ: int,
        fragmentSpectra: List[SpectralPeak],
        parameter: BasicTypes.ParentFragmentData.Parameter,
    ) -> None: ...
    @overload
    def __init__(
        self,
        parentZ: int,
        fragmentSpectra: List[SpectralPeak],
        parameter: BasicTypes.ParentFragmentData.Parameter,
        parentMz: float,
    ) -> None: ...

    FragmentIons: List[BasicTypes.FragmentIon]  # readonly

    @staticmethod
    def FilterByIntensity(
        ions: List[BasicTypes.FragmentIon], maxIonToKeep: int
    ) -> List[BasicTypes.FragmentIon]: ...
    @staticmethod
    def GetDeisotopedData(
        productPeaks: List[SpectralPeak],
        productMassAccuray: List[float],
        precursorMZ: float,
        precursorZ: int,
        parameter: BasicTypes.ParentFragmentData.Parameter,
    ) -> BasicTypes.ParentFragmentData: ...

    # Nested Types

    class Parameter:  # Class
        def __init__(self) -> None: ...

        FragmentInfo: BasicTypes.FragmentSpectraInfo
        ParentMassAccurancyCoefficients: List[float]

        def FromXml(self, siblings: System.Xml.XmlNodeList) -> None: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...
        def Clone(self) -> BasicTypes.ParentFragmentData.Parameter: ...

class Peak:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, loc: float, height: float, qualityCode: BasicTypes.Peak.Tag
    ) -> None: ...

    Height: float
    Intensity: float  # readonly
    Location: float  # readonly
    Overlapping: bool  # readonly
    QualityCode: BasicTypes.Peak.Tag  # readonly
    Saturated: bool  # readonly

    @staticmethod
    def CodeForSaturated(code: BasicTypes.Peak.Tag) -> bool: ...
    def CreatePeakAt(self, location: float) -> BasicTypes.Peak: ...
    @staticmethod
    def CodeForOverlapping(code: BasicTypes.Peak.Tag) -> bool: ...
    def PutTag(self, tag: BasicTypes.Peak.Tag) -> None: ...
    def RemoveTag(self, tag: BasicTypes.Peak.Tag) -> None: ...

    # Nested Types

    class Tag(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
        Forbiden: BasicTypes.Peak.Tag = ...  # static # readonly
        MzOverlapping: BasicTypes.Peak.Tag = ...  # static # readonly
        Normal: BasicTypes.Peak.Tag = ...  # static # readonly
        PotentialDetectorRing: BasicTypes.Peak.Tag = ...  # static # readonly
        Saturated: BasicTypes.Peak.Tag = ...  # static # readonly
        SoftwareIntroduced: BasicTypes.Peak.Tag = ...  # static # readonly
        StatisticsOnConstituentNeeded: BasicTypes.Peak.Tag = ...  # static # readonly

class Peak2D(IIsotope, BasicTypes.Peak):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        loc: float,
        alternativeLocation: float,
        height: float,
        errorCode: BasicTypes.Peak.Tag,
    ) -> None: ...
    @overload
    def __init__(self, p: BasicTypes.Peak2D, abundanceScale: float) -> None: ...

    AlternativeLocation: float  # readonly
    Area: float

    def SetLocation(self, value_: float) -> None: ...
    def CreatePeakAt(self, location: float) -> BasicTypes.Peak: ...

class Peak3D(
    BasicTypes.Peak2D,
    BasicTypes.ILocation2D,
    BasicTypes.IIntensity2D,
    System.IComparable,
    IIsotope,
    BasicTypes.IChromatographyObject,
):  # Class
    @overload
    def __init__(self, scanWidths: List[float]) -> None: ...
    @overload
    def __init__(
        self, signals: List[BasicTypes.Signal3D], scanWidths: List[float]
    ) -> None: ...
    @overload
    def __init__(
        self,
        mz: float,
        rt: float,
        volume: float,
        rtWidth: float,
        scanWidths: List[float],
    ) -> None: ...
    @overload
    def __init__(self, mz: float, rt: float, volume: float, height: float) -> None: ...
    @overload
    def __init__(self, p: BasicTypes.Peak3D) -> None: ...
    @overload
    def __init__(self, p: BasicTypes.Peak3D, abundanceScale: float) -> None: ...

    Abundance: float  # readonly
    Centroid: Vector  # readonly
    Gaussianness: float  # readonly
    Height: float  # readonly
    Intensity: float  # readonly
    LocalEIC: List[float]  # readonly
    Location: float  # readonly
    MZ: float  # readonly
    MZBounds: RangeDouble  # readonly
    MaxHeight: float  # readonly
    NewRtWidth: float  # readonly
    PotentialOtherHalf: BasicTypes.Peak3D  # readonly
    QScore: float
    QualityCode: BasicTypes.Peak.Tag  # readonly
    QualityScore: float
    RT: float  # readonly
    RTBounds: RangeDouble  # readonly
    RTSolidness: float  # readonly
    RTWidth: float  # readonly
    RetentionTime: float  # readonly
    RetentionTimePeakWidth: float  # readonly
    SNRatio: float
    SaturateScanRange: RangeInt  # readonly
    ScanBounds: RangeInt  # readonly
    ScanIndexAtApex: int  # readonly
    ScanIndexAtCentroid: int  # readonly
    ScanWidths: List[float]  # readonly
    ShapeQuality: float  # readonly
    Signal3Ds: List[ISignal3D]  # readonly
    Signals: List[BasicTypes.Signal3D]
    SpanOfScan: int  # readonly
    Volume: float
    XLocation: float  # readonly
    YLocation: float  # readonly

    def CalculateRTTruncationBias(self) -> float: ...
    @staticmethod
    def AreaGap(pk1: BasicTypes.Peak3D, pk2: BasicTypes.Peak3D) -> float: ...
    @staticmethod
    def Split(
        localDividingIndex: int,
        pk: BasicTypes.Peak3D,
        questionableSplit: bool,
        peak1: BasicTypes.Peak3D,
        peak2: BasicTypes.Peak3D,
    ) -> None: ...
    def RefineMass(self) -> None: ...
    def RefineRT(self) -> None: ...
    def CalculateRTTruncationIndex(self) -> float: ...
    def GetMzAtScan(self, scanIndex: int) -> float: ...
    def Merge(self, pk: BasicTypes.Peak3D) -> None: ...
    def IsSpiky(self, snRatio: float) -> bool: ...
    @staticmethod
    def GetRtDifferenceOfApexes(
        p1: BasicTypes.Peak3D, p2: BasicTypes.Peak3D
    ) -> float: ...
    def GetHeightAtScan(self, scanIndex: int) -> float: ...
    @overload
    @staticmethod
    def CalculateRTSolidness(startPoint: int, endPoint: int) -> float: ...
    @overload
    @staticmethod
    def CalculateRTSolidness(
        eic: List[float], startPoint: int, endPoint: int
    ) -> float: ...
    def ResetSignals(self, signals: List[BasicTypes.Signal3D]) -> None: ...
    def GetRTTrimLines(self) -> List[int]: ...
    def ApplyTimeShiftCorrection(
        self, shiftModel: Regression, factor: float
    ) -> None: ...
    def SetSNForNoise(self, noise: float) -> None: ...
    def ResetData(
        self, signals: List[BasicTypes.Signal3D], scanWidths: List[float]
    ) -> None: ...
    def CalculateVolumeExcludingRange(self, excludedScanRange: RangeInt) -> float: ...
    @overload
    @staticmethod
    def CalculatedEicCorrelationCoefficient(
        p1: BasicTypes.Peak3D, p2: BasicTypes.Peak3D, overlappingPartCC: float
    ) -> float: ...
    @overload
    @staticmethod
    def CalculatedEicCorrelationCoefficient(
        r1: RangeInt,
        r2: RangeInt,
        eic1: List[float],
        eic2: List[float],
        overlappingPartCC: float,
    ) -> float: ...
    def TrimInRT(self, trimLines: List[int]) -> None: ...
    def DropRTProfile(self) -> None: ...
    def Clone(self) -> BasicTypes.Peak3D: ...
    def CompareTo(self, obj: Any) -> int: ...
    def GetAverageScanWidth(self) -> float: ...
    def SetQualityCode(self, qualityCode: BasicTypes.Peak.Tag) -> None: ...

    # Nested Types

    class Comparer(
        System.Collections.Generic.IComparer[BasicTypes.Peak3D],
        System.Collections.IComparer,
    ):  # Class
        @overload
        def __init__(self, type: BasicTypes.Peak3D.Comparer.Type) -> None: ...
        @overload
        def __init__(
            self, type: BasicTypes.Peak3D.Comparer.Type, asc: bool
        ) -> None: ...
        @overload
        def Compare(self, o1: Any, o2: Any) -> int: ...
        @overload
        def Compare(self, p1: BasicTypes.Peak3D, p2: BasicTypes.Peak3D) -> int: ...

        # Nested Types

        class Type(
            System.IConvertible, System.IComparable, System.IFormattable
        ):  # Struct
            ByHight: BasicTypes.Peak3D.Comparer.Type = ...  # static # readonly
            ByM_z: BasicTypes.Peak3D.Comparer.Type = ...  # static # readonly
            ByRT: BasicTypes.Peak3D.Comparer.Type = ...  # static # readonly
            ByVolume: BasicTypes.Peak3D.Comparer.Type = ...  # static # readonly

class PeakList(Iterable[Any], BasicTypes.OrderedXY, BasicTypes.ISpectrum):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, size: int, rt: float) -> None: ...
    @overload
    def __init__(self, peaks: List[SpectralPeak]) -> None: ...

    Calib: BasicTypes.TOFCalib
    def __getitem__(self, i: int) -> BasicTypes.Peak: ...
    Length: int  # readonly
    LocationSpan: float  # readonly
    MaxHeight: float  # readonly
    Peaks: System.Collections.ArrayList  # readonly
    RT: float
    SignalCount: int  # readonly
    SummedHeight: float  # readonly

    def GetEnumerator(self) -> Iterator[Any]: ...
    def Sort(self, type: BasicTypes.PeakList.SortingType) -> None: ...
    @overload
    def Add(self, p: BasicTypes.Peak) -> None: ...
    @overload
    def Add(self, peaks: BasicTypes.PeakList) -> None: ...
    def TrimToSize(self) -> None: ...
    def GetImage(self, binRange: RangeInt) -> List[float]: ...
    def SetBins(self, binStarts: List[float]) -> None: ...
    def GetX(self, index: int) -> float: ...
    def GetY(self, index: int) -> float: ...
    def AddRange(self, peaks: List[Any]) -> None: ...
    def KeepRange(self, startIndex: int, count: int) -> None: ...
    def Remove(self, pk: BasicTypes.Peak) -> None: ...
    def GetDifference(self, subList: BasicTypes.PeakList) -> BasicTypes.PeakList: ...
    def CalculateSummmedHeight(
        self, xRange: RangeDouble, searchStartSignalIndex: int
    ) -> float: ...

    # Nested Types

    class Comparer(
        System.Collections.Generic.IComparer[BasicTypes.Peak],
        System.Collections.IComparer,
    ):  # Class
        def __init__(self, type: BasicTypes.PeakList.SortingType) -> None: ...
        @overload
        def Compare(self, o1: Any, o2: Any) -> int: ...
        @overload
        def Compare(self, p1: BasicTypes.Peak, p2: BasicTypes.Peak) -> int: ...

    class SortingType(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        ByIntensity: BasicTypes.PeakList.SortingType = ...  # static # readonly
        ByLocation: BasicTypes.PeakList.SortingType = ...  # static # readonly

class PrecursorDataSet(BasicTypes.IPrecursorDataSet):  # Class
    def __init__(
        self,
        mzOfInterest: float,
        precursorZ: int,
        zValueNeedsConfirm: bool,
        precursorIonSpecies: IModificationSpecies,
        isolationWindow: IsolationWindowType,
        EIData: bool,
    ) -> None: ...

    IonSpecies: IModificationSpecies  # readonly
    IsolationWindow: IsolationWindowType  # readonly
    PrecursorFullSaturation: float  # readonly
    PrecursorIonSpecies: IModificationSpecies  # readonly
    PrecursorIsotopePeaks: List[SpectralPeak]  # readonly
    PrecursorMz: float  # readonly

    def GetPrecursorZ(self, zValueNeedsConfirm: bool) -> int: ...
    def GetCollisionEnergies(self) -> Sequence[float]: ...
    def GetProductSpectraFullSaturation(self, collisionEnergy: float) -> float: ...
    def AddProductLineSpectrum(
        self,
        collisionEnergy: float,
        spectrum: List[SpectralPeak],
        timeRange: RangeDouble,
        fullSaturation: float,
        addDuplication: bool,
    ) -> None: ...
    def GetProductSpectrum(self, collisionEnergy: float) -> List[SpectralPeak]: ...
    def ConfirmZValue(self) -> None: ...
    def GetProductCompositeSpectrum(
        self,
        scheme: CeCompositeSpectraMakingScheme,
        productMassErrorCoefficients: List[float],
    ) -> List[SpectralPeak]: ...

class PrecursorIsotopeClusterExtractor:  # Class
    def __init__(
        self, precursorMassCoefficients: List[float], character: IsotopeCharacter
    ) -> None: ...
    def GetIsotopePeaks(
        self, precursorMZ: float, precursorZ: int, rawPeaks: List[SpectralPeak]
    ) -> List[SpectralPeak]: ...

class Protein(
    IMass_TimeSeparatedObject,
    Iterable[Any],
    IProtein,
    BasicTypes.ILadder,
    BasicTypes.IChromatographyObject,
    IFilterable,
):  # Class
    @overload
    def __init__(self, polarity: SpectrumSetMetadata.MSPolarity) -> None: ...
    @overload
    def __init__(
        self,
        polarity: SpectrumSetMetadata.MSPolarity,
        peak1: BasicTypes.Peak,
        peak2: BasicTypes.Peak,
        chargeCount: int,
    ) -> None: ...
    @overload
    def __init__(self, undertone: BasicTypes.Protein, undertoneFactor: int) -> None: ...
    @overload
    def __init__(
        self, polarity: SpectrumSetMetadata.MSPolarity, peak: BasicTypes.Peak
    ) -> None: ...
    @overload
    def __init__(
        self,
        rt: float,
        mass: float,
        volume: float,
        chargeStates: List[BasicTypes.Protein.ChargeState],
    ) -> None: ...

    Abundance: float
    ChargeStateSpan: int  # readonly
    ChargeStates: List[BasicTypes.Protein.ChargeState]
    EmptyStateCountAtBeginning: int  # readonly
    EmptyStateCountAtEnd: int  # readonly
    GapCount: int  # readonly
    Height: float  # readonly
    IonSet: List[IChargeState]  # readonly
    Mass: float
    MassStandardDeviation: float  # readonly
    MaxChargeCount: int  # readonly
    MaxHeight: float  # readonly
    MinChargeCount: int  # readonly
    NetProtonMass: float  # readonly
    NextPeakChargeCount: int  # readonly
    OverlappingPeakCount: int  # readonly
    PeakCount: int  # readonly
    PeakList: BasicTypes.PeakList  # readonly
    QScore: float
    QualityScore: float
    RT: float
    RTDeviation: float  # readonly
    RetentionTime: float  # readonly
    RetentionTimePeakWidth: float  # readonly
    Saturated: bool  # readonly

    def GetEnumerator(self) -> Iterator[Any]: ...
    def Add(self, p: BasicTypes.Peak) -> None: ...
    def Merge(self, another: BasicTypes.Protein) -> None: ...
    @staticmethod
    def LocationError(
        mzError: BasicTypes.ChromMetadata.MZError, mz: float
    ) -> float: ...
    def AddLast(self, p: BasicTypes.Peak) -> None: ...
    def TrimEmptyStatesAtEnds(self) -> None: ...
    @staticmethod
    def PredictIntensityRangeByExpolating(
        intensity1: float,
        intensity2: float,
        chargeCount1: int,
        chargeCount2: int,
        chargeCount: int,
    ) -> RangeDouble: ...
    @staticmethod
    def DeterminNetProtonMass(polarity: SpectrumSetMetadata.MSPolarity) -> float: ...
    @staticmethod
    def SortListBy(
        proteins: List[BasicTypes.Protein],
        sortingType: BasicTypes.MfeCompound.SortingType,
        ascending: bool,
    ) -> None: ...
    def AddFirst(self, p: BasicTypes.Peak) -> None: ...
    @staticmethod
    def PredictIntensityRangeByIntrapolating(
        intensity1: float,
        intensity2: float,
        chargeCount1: int,
        chargeCount2: int,
        chargeCount: int,
    ) -> RangeDouble: ...

    # Nested Types

    class ChargeState(IChargeState):  # Class
        def __init__(self, z: int, peak: BasicTypes.Peak) -> None: ...

        Abundance: float  # readonly
        ChargeCount: int  # readonly
        HasPeak: bool  # readonly
        MZ: float  # readonly
        MaxHeight: float  # readonly
        Peak: BasicTypes.Peak  # readonly
        PredictedMass: float  # readonly
        RetentionTime: float  # readonly
        Saturated: bool  # readonly
        Signal3Ds: List[ISignal3D]  # readonly
        Z: int  # readonly

    class Comparer(
        System.Collections.Generic.IComparer[BasicTypes.Protein],
        System.Collections.IComparer,
    ):  # Class
        def __init__(
            self, type: BasicTypes.MfeCompound.SortingType, ascending: bool
        ) -> None: ...
        @overload
        def Compare(self, o1: Any, o2: Any) -> int: ...
        @overload
        def Compare(self, c1: BasicTypes.Protein, c2: BasicTypes.Protein) -> int: ...

class QualSpeciesExpressionUtilities:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def ParseMultimerNumberAndAdducts(
        s: str, multimerNumber: int, adducts: str
    ) -> None: ...
    @overload
    @staticmethod
    def Parse(
        expression: str, multimerNumber: int, adducts: str, neutralModification: str
    ) -> None: ...
    @overload
    @staticmethod
    def Parse(expression: str) -> IModificationSpecies: ...
    @overload
    @staticmethod
    def Parse(complexFormula: str, z: int, unitCount: int) -> IModificationUnit: ...
    @staticmethod
    def FormatQualSpecies(species: IModificationSpecies) -> str: ...

class SampleChemistryInfo:  # Class
    def __init__(self) -> None: ...

    Averagine: bool
    MaxChargeCount: int

    CombinedAdducts: System.Collections.Generic.List[IModificationUnit]  # readonly
    NegativeAdducts: System.Collections.Generic.List[IModificationUnit]  # readonly
    PositiveAdducts: System.Collections.Generic.List[IModificationUnit]  # readonly
    SaltDominated: bool  # readonly

    @overload
    def Equals(self, p: BasicTypes.SampleChemistryInfo) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    def SetPositiveAdducts(self, adducts: List[str], saltDominated: bool) -> None: ...
    def GetAdductsForPolarity(
        self, polarity: SpectrumSetMetadata.MSPolarity
    ) -> System.Collections.Generic.List[IModificationUnit]: ...
    def SetNegativeAdducts(self, adducts: List[str]) -> None: ...
    @staticmethod
    def Validate(adducts: List[IModificationUnit]) -> str: ...
    def GetHashCode(self) -> int: ...
    @overload
    def SetAdducts(
        self,
        saltDominated: bool,
        positiveAdducts: System.Collections.Generic.List[IModificationUnit],
        negativeAdducts: System.Collections.Generic.List[IModificationUnit],
    ) -> None: ...
    @overload
    def SetAdducts(
        self, saltDominated: bool, combinedAdducts: List[IModificationUnit]
    ) -> None: ...
    def Clone(self) -> BasicTypes.SampleChemistryInfo: ...

class Signal3D(ISignal3D, ClusteringSequential.IElement):  # Class
    @overload
    def __init__(self, sig: BasicTypes.Signal3D) -> None: ...
    @overload
    def __init__(self, sig: BasicTypes.Signal3D, abundanceScale: float) -> None: ...
    @overload
    def __init__(
        self,
        hight: float,
        mz: float,
        time: float,
        rtIndex: int,
        qualityCode: BasicTypes.Peak.Tag,
    ) -> None: ...

    m_mz: float

    Height: float
    Intensity: float  # readonly
    MZ: float  # readonly
    Noise: float
    Overlapping: bool  # readonly
    QualityCode: BasicTypes.Peak.Tag  # readonly
    RT: float
    RetentionTime: float  # readonly
    Saturated: bool  # readonly
    ScanIndex: int  # readonly

    # Nested Types

    class Comparer(
        System.Collections.IComparer,
        System.Collections.Generic.IComparer[BasicTypes.Signal3D],
    ):  # Class
        def __init__(
            self, type: BasicTypes.Signal3D.Comparer.Type, ascent: bool
        ) -> None: ...
        @overload
        def Compare(self, o1: Any, o2: Any) -> int: ...
        @overload
        def Compare(self, s1: BasicTypes.Signal3D, s2: BasicTypes.Signal3D) -> int: ...

        # Nested Types

        class Type(
            System.IConvertible, System.IComparable, System.IFormattable
        ):  # Struct
            ByHight: BasicTypes.Signal3D.Comparer.Type = ...  # static # readonly
            ByM_z: BasicTypes.Signal3D.Comparer.Type = ...  # static # readonly
            ByRT: BasicTypes.Signal3D.Comparer.Type = ...  # static # readonly

class TOFCalib:  # Class
    def __init__(
        self,
        polynomialCoeff: List[float],
        minCalibratedTime: float,
        maxCalibratedTime: float,
    ) -> None: ...

    Coeffiecients: List[float]  # readonly

    def GetTime(self, mz: float) -> float: ...
    def GetMZ(self, t: float) -> float: ...
    @staticmethod
    def GetCalibreatedRange(metadata: SpectrumSetMetadata) -> RangeDouble: ...
    def Clone(self) -> BasicTypes.TOFCalib: ...
    def Derivative(self, t: float) -> float: ...

class XYCollection:  # Class
    def __init__(self, metaData: BasicTypes.ChromMetadata) -> None: ...

    AverageSpectrum: BasicTypes.ISpectrum  # readonly
    BinCount: int  # readonly
    Metadata: BasicTypes.ChromMetadata  # readonly
    RTRange: RangeDouble  # readonly
    ScanCount: int  # readonly
    ScanTimes: List[float]  # readonly
    SpectralXRange: RangeDouble  # readonly
    TIC: BasicTypes.Chromatogram  # readonly
    TOFCalibrations: List[BasicTypes.TOFCalib]  # readonly

    @overload
    def GetEIC(
        self, mzRange: RangeDouble, binChoice: BasicTypes.XYCollection.EICBinChoice
    ) -> BasicTypes.Chromatogram: ...
    @overload
    def GetEIC(self, mz: float) -> BasicTypes.Chromatogram: ...
    def ApplyTimeShiftCorrection(
        self, shiftModel: Regression, factor: float
    ) -> None: ...
    @overload
    def GetSpectrum(
        self, scanRange: RangeInt, type: BasicTypes.XYCollection.SpectrumType
    ) -> BasicTypes.ISpectrum: ...
    @overload
    def GetSpectrum(self, scan: int) -> BasicTypes.ISpectrum: ...
    @overload
    def GetSpectrum(self, rt: float) -> BasicTypes.ISpectrum: ...
    def GetAverageSpectrum(self, rtRange: RangeDouble) -> BasicTypes.ISpectrum: ...
    def GetNearestScan(self, rt: float) -> int: ...
    def GetTOFCalib(self, rt: float) -> BasicTypes.TOFCalib: ...
    def GetSpectralLoc(self, bin: int) -> float: ...
    @overload
    def GetSummedSpectrum(
        self, rt: float, rtPeakWidth: float
    ) -> BasicTypes.ISpectrum: ...
    @overload
    def GetSummedSpectrum(self, rtRange: RangeDouble) -> BasicTypes.ISpectrum: ...

    # Nested Types

    class EICBinChoice(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        FillBins: BasicTypes.XYCollection.EICBinChoice = ...  # static # readonly
        FillWhenCentroidCovered: BasicTypes.XYCollection.EICBinChoice = (
            ...
        )  # static # readonly
        NoBinning: BasicTypes.XYCollection.EICBinChoice = ...  # static # readonly

    class SpectrumType(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        Averaged: BasicTypes.XYCollection.SpectrumType = ...  # static # readonly
        Summed: BasicTypes.XYCollection.SpectrumType = ...  # static # readonly

class XYCollectionLine(BasicTypes.XYCollection):  # Class
    @overload
    def __init__(self, metaData: BasicTypes.ChromMetadata) -> None: ...
    @overload
    def __init__(
        self,
        metaData: BasicTypes.ChromMetadata,
        peaks: List[BasicTypes.Peak3D],
        scanTimes: List[float],
        shiftModel: Regression,
        factor: float,
    ) -> None: ...
    @overload
    def __init__(
        self, metaData: BasicTypes.ChromMetadata, compounds: List[ICompound]
    ) -> None: ...
    @overload
    def __init__(
        self, template: BasicTypes.XYCollectionLine, peaks: List[BasicTypes.Peak3D]
    ) -> None: ...
    @overload
    def __init__(
        self,
        template: BasicTypes.XYCollectionLine,
        peakLists: System.Collections.Generic.List[
            System.Collections.Generic.List[BasicTypes.Peak]
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        template: BasicTypes.XYCollectionLine,
        groups: List[BasicTypes.CoelutionGroup],
        shiftModel: Regression,
        factor: float,
    ) -> None: ...

    BinCount: int  # readonly
    IsBinned: bool  # readonly
    PeakLists: List[BasicTypes.PeakList]  # readonly
    TheEICCollection: BasicTypes.EICCollection

    @overload
    def GetEIC(
        self, mzRange: RangeDouble, binChoice: BasicTypes.XYCollection.EICBinChoice
    ) -> BasicTypes.Chromatogram: ...
    @overload
    def GetEIC(self, mz: float) -> BasicTypes.Chromatogram: ...
    def FindResolutionBinRange(self, spectralXRange: RangeDouble) -> RangeInt: ...
    @overload
    def Add(self, peaks: BasicTypes.PeakList, massRange: RangeDouble) -> None: ...
    @overload
    def Add(self, peaks: BasicTypes.PeakList) -> None: ...
    def GetSpectrum(
        self, scanRange: RangeInt, type: BasicTypes.XYCollection.SpectrumType
    ) -> BasicTypes.ISpectrum: ...
    def TrimToSize(self) -> None: ...
    def GetAllSignal3D(
        self,
    ) -> System.Collections.Generic.List[BasicTypes.Signal3D]: ...
    def FindResolutionBin(self, mz: float) -> int: ...
    def GetSpectralLoc(self, bin: int) -> float: ...
    def GetScanImages(
        self, scanRange: RangeInt, binRange: RangeInt
    ) -> List[List[float]]: ...

class XYCollectionProfile(BasicTypes.XYCollection):  # Class
    @overload
    def __init__(
        self, metadata: BasicTypes.ChromMetadata, scanCount: int, mzBinWidth: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        metadata: BasicTypes.ChromMetadata,
        scanCount: int,
        binCount: int,
        mzBinWidth: float,
    ) -> None: ...
    @overload
    def __init__(self, metaData: BasicTypes.ChromMetadata) -> None: ...
    @overload
    def __init__(
        self, metadata: BasicTypes.ChromMetadata, mzBinWidth: float
    ) -> None: ...

    BinCount: int  # readonly
    MZBinWidth: float

    @overload
    def GetEIC(
        self, mzRange: RangeDouble, binChoice: BasicTypes.XYCollection.EICBinChoice
    ) -> BasicTypes.Chromatogram: ...
    @overload
    def GetEIC(self, mz: float) -> BasicTypes.Chromatogram: ...
    def GetSpectrum(
        self, scanRange: RangeInt, type: BasicTypes.XYCollection.SpectrumType
    ) -> BasicTypes.ISpectrum: ...
    @overload
    def SetData(
        self,
        scan: int,
        rt: float,
        rawData: List[int],
        x0: float,
        calib: BasicTypes.TOFCalib,
    ) -> int: ...
    @overload
    def SetData(
        self,
        scan: int,
        rt: float,
        calib: BasicTypes.TOFCalib,
        x0: float,
        lowSignals: List[int],
        mediumSignals: List[int],
        highSignals: List[int],
    ) -> None: ...
    def GetScans(self, scanRange: RangeInt) -> List[List[int]]: ...
    def GetSpectralLoc(self, bin: int) -> float: ...
