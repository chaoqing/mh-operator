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
    GUI,
    MIDAC,
    Acquisition,
    CommandModel,
    DataAnalysis,
    ErrorReporting,
    EventManipulating,
    MSDChem,
    Utilities,
)
from .DataAnalysis import (
    AcqStatus,
    BaseDataWriter,
    CompressionScheme,
    DefaultCalibCoeff,
    Device,
    IBaseDataWriter,
    IBaseNonMSDataWriter,
    IImsFrameMethod,
    ILwMsPeakList,
    IonPolarity,
    LwMsPeak,
    MeasurementType,
    MSActualInfo,
    MSScanType,
    MSTimeSegments,
    RunTimeCalibCoeff,
    ScanDetails,
    ScanHeader,
    SeparationTechnique,
    SpectralPeak,
    SpectrumParams,
    XSamplingType,
)
from .DataAnalysis.IMS import FrameData
from .MIDAC import AbundanceMeasure
from .MSDChem import MSDChemDataMSFile, SpectralRecordType

# Stubs for namespace: Agilent.MassSpectrometry

class AdvancedParamWrapper(System.IDisposable):  # Class
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.AdvancedParamWrapper) -> None: ...
    @overload
    def __init__(self, src: System.IntPtr) -> None: ...
    @overload
    def __init__(self) -> None: ...

    EP1: float
    EP10: float
    EP2: float
    EP3: float
    EP4: float
    EP5: float
    EP6: float
    EP7: float
    EP8: float
    EP9: float

    def Dispose(self) -> None: ...

class AmrtMatch(
    List[Any],
    Sequence[Any],
    Iterable[Any],
    System.Collections.Generic.List[Agilent.MassSpectrometry.IIonMatch],
    Iterable[Agilent.MassSpectrometry.IIonMatch],
    List[Agilent.MassSpectrometry.IIonMatch],
    Sequence[Agilent.MassSpectrometry.IIonMatch],
    Agilent.MassSpectrometry.IAmrtMatch,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.IAmrtMatch) -> None: ...
    def SetMzShiftData(
        self,
        signedZ: int,
        lowestCalcMz: float,
        mzShiftFromCalc: float,
        ionShiftFromNeutral: float,
    ) -> None: ...
    def SetScaleFactor(self, scaleFactor: float) -> None: ...
    def SetIonScores(
        self, mass: float, abund: float, spacing: float, combinedIon: float
    ) -> None: ...
    def SetOverallScore(self, score: float) -> None: ...
    def SetRtScore(self, rtScore: float) -> None: ...

class AmrtScoreCalculator:  # Class
    def __init__(self) -> None: ...
    def ObservedClusterMatchingAPattern(
        self,
        obsSpectrum: Agilent.MassSpectrometry.IMsXyData,
        expIsoPattern: Agilent.MassSpectrometry.IMsXyData,
        groupingParameters: Agilent.MassSpectrometry.IIonGroupingParameters,
        peakExtractParameters: Agilent.MassSpectrometry.IMsPeakExtractParamters,
        keyPeakIdx: int,
    ) -> ILwMsPeakList: ...
    @staticmethod
    def CalculateMassScore(
        measuredMz: float,
        refMz: float,
        deviations: Agilent.MassSpectrometry.IExpectedDeviationParameters,
    ) -> float: ...
    def CombineIonAndRtScores(
        self,
        match: Agilent.MassSpectrometry.IAmrtMatch,
        rtScore: float,
        weightingParameters: Agilent.MassSpectrometry.IScoreWeightingParameters,
    ) -> None: ...
    @overload
    def CalculateAmMatchScores(
        self,
        obsSpectrum: Agilent.MassSpectrometry.IMsXyData,
        calcSpectrum: Agilent.MassSpectrometry.IMsXyData,
        ionFormula: str,
        ionAdducts: str,
        ionLosses: str,
        signedChargeState: int,
        groupingParameters: Agilent.MassSpectrometry.IIonGroupingParameters,
        expectedDeviations: Agilent.MassSpectrometry.IExpectedDeviationParameters,
        weightingParameters: Agilent.MassSpectrometry.IScoreWeightingParameters,
    ) -> Agilent.MassSpectrometry.IAmrtMatch: ...
    @overload
    def CalculateAmMatchScores(
        self,
        obsCluster: ILwMsPeakList,
        calcCluster: Agilent.MassSpectrometry.IMsXyData,
        ionAdducts: str,
        ionLosses: str,
        signedChargeState: int,
        groupingParameters: Agilent.MassSpectrometry.IIonGroupingParameters,
        expectedDeviations: Agilent.MassSpectrometry.IExpectedDeviationParameters,
        weightingParameters: Agilent.MassSpectrometry.IScoreWeightingParameters,
    ) -> Agilent.MassSpectrometry.IAmrtMatch: ...
    def CalculateRtMatchScore(
        self, observedRt: float, expectedRt: float, expectedRtDeviation: float
    ) -> float: ...

class BaselineParamWrapper(System.IDisposable):  # Class
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.BaselineParamWrapper) -> None: ...
    @overload
    def __init__(self, src: System.IntPtr) -> None: ...
    @overload
    def __init__(self) -> None: ...

    ChunkSize: int
    FastBaseline: bool
    FracSkip: float
    FracUse: float
    MinChunks: int
    NumZeroes: int
    Tolerance: float

    def Dispose(self) -> None: ...

class CS_Algorithm(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CS_Latest: Agilent.MassSpectrometry.CS_Algorithm = ...  # static # readonly

class ChargeStateAssignmentWrapper(
    System.IDisposable, Agilent.MassSpectrometry.IIsotopeGrouper
):  # Class
    def __init__(self) -> None: ...
    @overload
    def SetParameters(
        self,
        grouperAlgorithm: Agilent.MassSpectrometry.CS_Algorithm,
        isotopeModel: Agilent.MassSpectrometry.IsotopeModel,
        minZ: int,
        maxZ: int,
        doDeisotope: bool,
        accuracyC0: float,
        accuracyC1: float,
    ) -> None: ...
    @overload
    def SetParameters(
        self,
        isotopeModel: Agilent.MassSpectrometry.IsotopeModel,
        minZ: int,
        maxZ: int,
        doDeisotope: bool,
        accuracyC0: float,
        accuracyC1: float,
    ) -> None: ...
    @overload
    def AssignChargeStates(
        self, pkId: List[int], pkMz: List[float], pkHt: List[float], pkCs: List[int]
    ) -> int: ...
    @overload
    def AssignChargeStates(
        self,
        pkId: List[int],
        pkMz: List[float],
        pkHt: List[float],
        pkCs: List[int],
        pkCl: List[int],
    ) -> int: ...
    def Dispose(self) -> None: ...
    def SetAllowGapFlag(self, allowGap: bool) -> None: ...

class ContentsXmlReader(Agilent.MassSpectrometry.IContentsXmlWriter):  # Class
    def __init__(self, dataFilePath: str) -> None: ...

    AcqDateTime: System.DateTime  # readonly
    AcqSoftwareVersion: str  # readonly
    AcqStatus: AcqStatus  # readonly
    InstrumentName: str  # readonly
    LockedMode: bool  # readonly
    MeasurementType: MeasurementType  # readonly
    SeparationTechnique: SeparationTechnique  # readonly

    def AcquireLock(self) -> bool: ...
    def ReleaseLock(self) -> None: ...

class DeisotopeOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    NoDeisotoping: Agilent.MassSpectrometry.DeisotopeOption = ...  # static # readonly
    RemoveHigherMzIons: Agilent.MassSpectrometry.DeisotopeOption = (
        ...
    )  # static # readonly
    SumIonAbundance: Agilent.MassSpectrometry.DeisotopeOption = ...  # static # readonly

class ExpectedDeviationParameters(
    Agilent.MassSpectrometry.IExpectedDeviationParameters
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, forMsMs: bool) -> None: ...
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.IExpectedDeviationParameters
    ) -> None: ...

class IAmrtMatch(
    List[Agilent.MassSpectrometry.IIonMatch],
    Sequence[Agilent.MassSpectrometry.IIonMatch],
    Iterable[Agilent.MassSpectrometry.IIonMatch],
    Iterable[Any],
):  # Interface
    AbundanceScaleFactor: float  # readonly
    CombinedIonScore: float  # readonly
    HasRtScore: bool  # readonly
    IonAbundanceScore: float  # readonly
    IonSpacingScore: float  # readonly
    MassDiffFromCalcMDa: float  # readonly
    MassDiffFromCalcPpm: float  # readonly
    MassDiffFromObsMDa: float  # readonly
    MassDiffFromObsPpm: float  # readonly
    MassScore: float  # readonly
    OverallScore: float  # readonly
    RtScore: float  # readonly

    def Clone(self) -> Agilent.MassSpectrometry.IAmrtMatch: ...

class IExpectedDeviationParameters(object):  # Interface
    AbundanceDeviationPct: float
    MzDeviationMDa: float
    MzDeviationPpm: float
    RtDeviationMin: float

    def Clone(self) -> Agilent.MassSpectrometry.IExpectedDeviationParameters: ...

class IImsDataWriter(IBaseDataWriter):  # Interface
    SkipWritingProfileTfs: bool

    def WriteFrameMethods(self) -> None: ...
    def WriteScanAndFrameHeaders(self, scanHeader: ScanHeader) -> None: ...
    def WriteDataCom(
        self,
        frameData: FrameData,
        frameActuals: List[MSActualInfo],
        defaultCalibration: DefaultCalibCoeff,
        runtimeMassCalibration: RunTimeCalibCoeff,
        nextScanId: int,
    ) -> None: ...
    def AddFrameMethod(self, frameMethod: IImsFrameMethod) -> None: ...
    def CreateImsDataFile(
        self,
        dataFileName: str,
        imsFrameSchemaFile: str,
        msScanSchemaFile: str,
        bOverwrite: bool,
    ) -> None: ...
    def WriteData(
        self,
        frameData: FrameData,
        frameActuals: List[MSActualInfo],
        defaultCalibration: Agilent.MassSpectrometry.ITofCal,
        runtimeMassCalibration: Agilent.MassSpectrometry.ITofCal,
        nextScanId: int,
    ) -> None: ...
    def UpdateFrameMethod(self, frameMethod: IImsFrameMethod) -> None: ...

class IIonGroupingParameters(object):  # Interface
    IsotopeModel: Agilent.MassSpectrometry.IsotopeModel
    MzSpacingToleranceMDa: float
    MzSpacingTolerancePpm: float

    def Clone(self) -> Agilent.MassSpectrometry.IIonGroupingParameters: ...

class IIonGroupingParametersEx(
    Agilent.MassSpectrometry.IIonGroupingParameters
):  # Interface
    DeisotopeOption: Agilent.MassSpectrometry.DeisotopeOption
    MaxZ: int
    MinZ: int

    def Clone(self) -> Agilent.MassSpectrometry.IIonGroupingParametersEx: ...

class IIonMatch(object):  # Interface
    AbundanceCalc: float
    AbundanceObs: float
    MzCalc: float
    MzDiffFromCalcMDa: float  # readonly
    MzDiffFromCalcPpm: float  # readonly
    MzDiffFromObsMDa: float  # readonly
    MzDiffFromObsPpm: float  # readonly
    MzObs: float

    def Clone(self) -> Agilent.MassSpectrometry.IIonMatch: ...

class IIsotopeGrouper(object):  # Interface
    def SetParameters(
        self,
        isotopeModel: Agilent.MassSpectrometry.IsotopeModel,
        minZ: int,
        maxZ: int,
        doDeisotope: bool,
        accuracyC0: float,
        accuracyC1: float,
    ) -> None: ...
    def AssignChargeStates(
        self,
        pkId: List[int],
        pkMz: List[float],
        pkHt: List[float],
        pkCs: List[int],
        pkCl: List[int],
    ) -> int: ...

class IMsPeakExtractParamters(object):  # Interface
    KeyPeakAbsMzTolerance: float
    KeyPeakAbsThreshold: float
    KeyPeakMzRangeExpansion: float
    MinProfilePeakValley: float

class IMsXyData(object):  # Interface
    AbundArray: List[float]
    CalA: float
    CalTo: float
    IsProfileData: bool
    MaxMz: float  # readonly
    MinMz: float  # readonly
    MzArray: List[float]
    XSamplingType: XSamplingType  # readonly

    def SetTofCalibration(self, tofCal: Agilent.MassSpectrometry.ITofCal) -> None: ...

class IRlzArrayIterator(object):  # Interface
    def FirstBin(self) -> int: ...
    def Reset(self) -> None: ...
    def FullLength(self) -> int: ...
    def Next(self, bin: int, value_: int) -> bool: ...

class IScoreWeightingParameters(object):  # Interface
    IonAbundanceScoreWeight: float
    IonSpacingScoreWeight: float
    MassScoreWeight: float
    RtScoreWeight: float

    def Clone(self) -> Agilent.MassSpectrometry.IScoreWeightingParameters: ...

class ITofCal(object):  # Interface
    def TimeToMass(self, time: float) -> float: ...
    def Equals(self, other: Agilent.MassSpectrometry.ITofCal) -> bool: ...
    def AppendStep(self, step: Agilent.MassSpectrometry.ITofCalStep) -> None: ...
    def FullRecalMinMass(self) -> float: ...
    def MassesToTimes(self, masses: List[float], times: List[float]) -> None: ...
    def Recalibrate(self, times: List[float], masses: List[float]) -> None: ...
    def SetFullRecalibrationLimits(
        self, minMass: float, minMassRange: float
    ) -> None: ...
    def StepCount(self) -> int: ...
    def ClearSteps(self) -> None: ...
    def UpdateStep(
        self, index: int, step: Agilent.MassSpectrometry.ITofCalStep
    ) -> None: ...
    def TimesToMasses(self, times: List[float], masses: List[float]) -> None: ...
    def MassToTime(self, mass: float) -> float: ...
    def NewTradStep(self) -> Agilent.MassSpectrometry.ITofCalStepTrad: ...
    @overload
    def Calibrate(
        self,
        times: List[float],
        masses: List[float],
        calOption: Agilent.MassSpectrometry.TofCalAutomation,
    ) -> None: ...
    @overload
    def Calibrate(self, times: List[float], masses: List[float]) -> None: ...
    def Clone(self) -> Agilent.MassSpectrometry.ITofCal: ...
    def FullRecalMinMassRange(self) -> float: ...
    def GetStep(self, index: int) -> Agilent.MassSpectrometry.ITofCalStep: ...
    def NewPolyStep(self) -> Agilent.MassSpectrometry.ITofCalStepPoly: ...

class ITofCalStep(object):  # Interface
    ...

class ITofCalStepPoly(Agilent.MassSpectrometry.ITofCalStep):  # Interface
    Coefficients: List[float]
    PowerFlags: int
    TMax: float
    TMin: float
    Weighting: Agilent.MassSpectrometry.TofCalWtEnum

    def Clone(self) -> Agilent.MassSpectrometry.ITofCalStepPoly: ...

class ITofCalStepTrad(Agilent.MassSpectrometry.ITofCalStep):  # Interface
    A: float
    To: float
    Weighting: Agilent.MassSpectrometry.TofCalWtEnum

    def Clone(self) -> Agilent.MassSpectrometry.ITofCalStepTrad: ...

class ImsDataWriter(
    IBaseDataWriter,
    System.IDisposable,
    Agilent.MassSpectrometry.IImsDataWriter,
    BaseDataWriter,
    IBaseNonMSDataWriter,
):  # Class
    def __init__(self) -> None: ...
    def WriteTimeSegments(self, msTimeSegments: MSTimeSegments) -> None: ...
    def EndWritingData(self) -> None: ...
    def EndStoringData(self) -> None: ...

class IonGroupingParameters(
    Agilent.MassSpectrometry.IIonGroupingParametersEx,
    Agilent.MassSpectrometry.IIonGroupingParameters,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.IIonGroupingParametersEx
    ) -> None: ...
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.IIonGroupingParameters
    ) -> None: ...

class IonMatch(Agilent.MassSpectrometry.IIonMatch):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.IIonMatch) -> None: ...

class IsotopeDistributionCalculator:  # Class
    def __init__(self) -> None: ...

    NominalMassResolution: float

    def PeakDistribution(
        self, neutralFormula: str, signedCharge: int
    ) -> Agilent.MassSpectrometry.IMsXyData: ...
    def ProfileDistribution(
        self, neutralFormula: str, signedCharge: int
    ) -> Agilent.MassSpectrometry.IMsXyData: ...

class IsotopeModel(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Biological: Agilent.MassSpectrometry.IsotopeModel = ...  # static # readonly
    CommonOrganic: Agilent.MassSpectrometry.IsotopeModel = ...  # static # readonly
    Glycan: Agilent.MassSpectrometry.IsotopeModel = ...  # static # readonly
    Peptidic: Agilent.MassSpectrometry.IsotopeModel = ...  # static # readonly
    Unbiased: Agilent.MassSpectrometry.IsotopeModel = ...  # static # readonly

class LzfCompression(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def CompressToBuffer(
        self, inputArray: List[int], bytesToCompress: int, outputArray: List[int]
    ) -> int: ...
    def DecompressToBuffer(
        self, inputArray: List[int], bytesToDecompress: int, outputArray: List[int]
    ) -> int: ...
    def Dispose(self) -> None: ...

class MSDChemToArcher:  # Class
    def __init__(
        self,
        iWriter: IBaseDataWriter,
        msdchemScanDataFile: MSDChemDataMSFile,
        msdchemSIMDataFile: MSDChemDataMSFile,
    ) -> None: ...
    @staticmethod
    def FindAcquisitionMethodGroups(
        strFullPathToMethod: str,
        acqMSTimesForSIMGroups: System.Collections.Generic.List[float],
        actualTimesForSIMGroups: System.Collections.Generic.List[float],
        ionsForSIMGroups: System.Collections.Generic.List[
            System.Collections.Generic.List[float]
        ],
        labelsForIonsForSIMGroups: System.Collections.Generic.List[
            System.Collections.Generic.List[str]
        ],
    ) -> None: ...
    @staticmethod
    def NewScanDetails(
        i32ScanID: int,
        i32CycleID: int,
        dSpectrumRetentionTime: float,
        spectrumParams: SpectrumParams,
        dBasePeakMZ: float,
        dBasePeakValue: float,
        dTIC: float,
        scanType: MSScanType,
        ionPolarity: IonPolarity,
        actualTimesForSIMGroups: System.Collections.Generic.List[float],
    ) -> ScanDetails: ...
    def TranslateScanByScan(
        self, ionPolarity: IonPolarity, bDataFileHasProfileSpectra: bool
    ) -> None: ...
    @staticmethod
    def TranslateSpectralRecordTypeToMSScanType(
        spectralRecordType: SpectralRecordType,
    ) -> MSScanType: ...
    @staticmethod
    def NewSpectrumParams(
        dMinX: float, dMaxX: float, dMaxY: float
    ) -> SpectrumParams: ...
    @staticmethod
    def NewDevice() -> Device: ...
    @staticmethod
    def NewScanHeader(bDataFileHasProfileSpectra: bool) -> ScanHeader: ...

class MsPeakExtractParameters(
    Agilent.MassSpectrometry.IMsPeakExtractParamters
):  # Class
    def __init__(self) -> None: ...

class MsXyData(Agilent.MassSpectrometry.IMsXyData):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        mzArray: List[float],
        abundArray: List[float],
        isProfile: bool,
        xSamplingType: XSamplingType,
        tofCal: Agilent.MassSpectrometry.ITofCal,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mzArray: List[float],
        abundArray: List[float],
        isProfile: bool,
        xSamplingType: XSamplingType,
        calA: float,
        calTo: float,
    ) -> None: ...
    @overload
    def __init__(self, pkList: ILwMsPeakList) -> None: ...
    @overload
    def __init__(self, pkList: List[SpectralPeak]) -> None: ...

class PeakFilterParamWrapper(System.IDisposable):  # Class
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.PeakFilterParamWrapper
    ) -> None: ...
    @overload
    def __init__(self, src: System.IntPtr) -> None: ...
    @overload
    def __init__(self) -> None: ...

    MaxPeakCount: int
    PkHtThresholdAbs: float
    PkHtThresholdDisplay: float
    PkHtThresholdPct: float
    PkSNRThreshold: float
    SummedSpectra: int

    def Clear(self) -> None: ...
    def Dispose(self) -> None: ...

class PeakFinderAlgorithm(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    PF_Latest: Agilent.MassSpectrometry.PeakFinderAlgorithm = ...  # static # readonly

class PeakInfoWrapper(System.IDisposable):  # Class
    @overload
    def __init__(self, src: System.IntPtr) -> None: ...
    @overload
    def __init__(self) -> None: ...

    ApexIdx: int
    ApexY: float
    Area: float
    Center: float
    EndIdx: int
    EndY: float
    Height: float
    StartIdx: int
    StartY: float
    Suspect: int
    Width: float

    def Dispose(self) -> None: ...

class PeakLocateParamWrapper(System.IDisposable):  # Class
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.PeakLocateParamWrapper
    ) -> None: ...
    @overload
    def __init__(self, src: System.IntPtr) -> None: ...
    @overload
    def __init__(self) -> None: ...

    MaxSpikeWidth: int
    RequiredValley: float

    def Dispose(self) -> None: ...

class RlzAccumulator:  # Class
    @overload
    def __init__(self, abundMeasure: AbundanceMeasure) -> None: ...
    @overload
    def __init__(
        self,
        abundMeasure: AbundanceMeasure,
        firstArray: Agilent.MassSpectrometry.IRlzArrayIterator,
    ) -> None: ...

    ArrayCount: int  # readonly
    BaseAbundance: int  # readonly
    BaseBin: int  # readonly
    FirstNzBin: int  # readonly
    LastNzBin: int  # readonly
    NumNzPoints: int  # readonly
    Result: Agilent.MassSpectrometry.IRlzArrayIterator  # readonly
    TotalAbund: int  # readonly

    def Add(self, addend: Agilent.MassSpectrometry.IRlzArrayIterator) -> None: ...

class RlzArrayMetrics(System.IDisposable):  # Class
    @overload
    def __init__(
        self,
        firstBin: int,
        firstNzBin: int,
        lastNzBin: int,
        maxValue: int,
        maxValueBin: int,
        numCompactedBytes: int,
        numNzValues: int,
        numValues: int,
        tic: int,
    ) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.RlzArrayMetrics) -> None: ...
    @overload
    def __init__(self) -> None: ...

    FirstBin: int
    FirstNzBin: int
    LastNzBin: int
    MaxValue: int
    MaxValueBin: int
    NumCompactedBytes: int
    NumNzValues: int
    NumValues: int
    Tic: int

    def Dispose(self) -> None: ...

class RlzArrayMetricsL(
    System.IDisposable, Agilent.MassSpectrometry.RlzArrayMetrics
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.RlzArrayMetricsL) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.RlzArrayMetrics) -> None: ...
    @overload
    def __init__(
        self,
        firstBin: int,
        firstNzBin: int,
        lastNzBin: int,
        maxValue: int,
        maxValueBin: int,
        numCompactedBytes: int,
        numNzValues: int,
        numValues: int,
        tic: int,
    ) -> None: ...

    Tic: int

class RlzByteCompression(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def DecompressToBuffer(
        self,
        inputArray: List[int],
        inputArrayOffset: int,
        inputBytes: int,
        outputArray: List[int],
    ) -> int: ...
    def DecompressedSize(self, inputArray: List[int], inputArrayOffset: int) -> int: ...
    def Compress(
        self, firstBin: int, inputArray: List[int], outputArray: List[int]
    ) -> Agilent.MassSpectrometry.RlzArrayMetrics: ...
    def DecompressSpecRecord(
        self, inputArray: List[int], inputArrayOffset: int
    ) -> List[int]: ...
    def CompressToBuffer(
        self, firstBin: int, inputArray: List[int], outputArray: List[int]
    ) -> Agilent.MassSpectrometry.RlzArrayMetrics: ...
    def Dispose(self) -> None: ...
    def Decompress(self, inputArray: List[int], inputOffset: int) -> List[int]: ...

class RlzByteIterator(
    System.IDisposable, Agilent.MassSpectrometry.IRlzArrayIterator
):  # Class
    def __init__(
        self, firstBin: int, compressedArray: List[int], arrayOffsetBytes: int
    ) -> None: ...
    def Reset(self) -> None: ...
    def FirstBin(self) -> int: ...
    def Next(self, bin: int, value_: int) -> bool: ...
    def FullLength(self) -> int: ...
    def Dispose(self) -> None: ...

class RlzIntCompression(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def DecompressToBuffer(
        self, inputArray: List[int], inputBytes: int, outputArray: List[int]
    ) -> int: ...
    def DecompressedSize(self, inputArray: List[int]) -> int: ...
    def Compress(
        self, firstBin: int, inputArray: List[int], outputArray: List[int]
    ) -> Agilent.MassSpectrometry.RlzArrayMetrics: ...
    def CompressToBuffer(
        self, firstBin: int, inputArray: List[int], outputArray: List[int]
    ) -> Agilent.MassSpectrometry.RlzArrayMetrics: ...
    def Dispose(self) -> None: ...
    def Decompress(self, inputArray: List[int]) -> List[int]: ...

class RlzIntIterator(
    System.IDisposable, Agilent.MassSpectrometry.IRlzArrayIterator
):  # Class
    def __init__(
        self, hdrInts: int, firstBin: int, compressedArray: List[int]
    ) -> None: ...
    def Reset(self) -> None: ...
    def FirstBin(self) -> int: ...
    def Next(self, bin: int, value_: int) -> bool: ...
    def FullLength(self) -> int: ...
    def Dispose(self) -> None: ...

class RlzIntIteratorOnByteArray(
    System.IDisposable, Agilent.MassSpectrometry.IRlzArrayIterator
):  # Class
    def __init__(
        self,
        hdrInts: int,
        firstBin: int,
        compressedArray: List[int],
        arrayOffsetBytes: int,
    ) -> None: ...
    def Reset(self) -> None: ...
    def FirstBin(self) -> int: ...
    def Next(self, bin: int, value_: int) -> bool: ...
    def FullLength(self) -> int: ...
    def Dispose(self) -> None: ...

class RlzUtilities:  # Class
    @overload
    @staticmethod
    def RlzScheme(byteArray: List[int], arrayOffsetBytes: int) -> CompressionScheme: ...
    @overload
    @staticmethod
    def RlzScheme(compressedArray: List[int]) -> CompressionScheme: ...
    @overload
    @staticmethod
    def RlzIterator(
        firstBin: int, byteArray: List[int], arrayOffsetBytes: int
    ) -> Agilent.MassSpectrometry.IRlzArrayIterator: ...
    @overload
    @staticmethod
    def RlzIterator(
        firstBin: int, rlzCompressedArray: List[int]
    ) -> Agilent.MassSpectrometry.IRlzArrayIterator: ...

class ScoreWeightingParameters(
    Agilent.MassSpectrometry.IScoreWeightingParameters
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.IScoreWeightingParameters
    ) -> None: ...

class SharedMSStrings:  # Class
    A4_Paper_Size: str = ...  # static # readonly
    AcqData_Dir: str = ...  # static # readonly
    AcqMethod_Dir: str = ...  # static # readonly
    Acquisition_DirName: str = ...  # static # readonly
    Calibration_Masslist_SchemaFileName: str = ...  # static # readonly
    ChromDirectory_FileExtn: str = ...  # static # readonly
    Chromatogram_FileExtn: str = ...  # static # readonly
    Contents_FileName: str = ...  # static # readonly
    Contents_SchemaFileName: str = ...  # static # readonly
    CustomerHome_Location: str = ...  # static # readonly
    CustomerHome_Location_64: str = ...  # static # readonly
    CustomerHome_RegKeyName: str = ...  # static # readonly
    DAMethod_Dir: str = ...  # static # readonly
    DefaultCalib_FileName: str = ...  # static # readonly
    DefaultCalib_SchemaFileName: str = ...  # static # readonly
    DeviceConfig_FileName: str = ...  # static # readonly
    Devices_FileName: str = ...  # static # readonly
    Devices_SchemaFileName: str = ...  # static # readonly
    IMS_Browser_Dir: str = ...  # static # readonly
    IMS_DefaultCal_InstallLocation: str = ...  # static # readonly
    ImsDefaultCal_FileName: str = ...  # static # readonly
    ImsFrameMeth_FileName: str = ...  # static # readonly
    ImsFrame_BinaryFileName: str = ...  # static # readonly
    ImsFrame_SchemaFileName: str = ...  # static # readonly
    ImsOverrideCal_FileName: str = ...  # static # readonly
    InstallHome_Location: str = ...  # static # readonly
    InstallHome_RegKeyName: str = ...  # static # readonly
    Letter_Paper_Size: str = ...  # static # readonly
    MSActualsDefinition_FileName: str = ...  # static # readonly
    MSActualsDefinition_SchemaFileName: str = ...  # static # readonly
    MSCalibration_FileName: str = ...  # static # readonly
    MSPeak_DataFileName: str = ...  # static # readonly
    MSPeriodicActuals_FileName: str = ...  # static # readonly
    MSProfile_DataFileName: str = ...  # static # readonly
    MSScanActuals_FileName: str = ...  # static # readonly
    MSScan_BinaryFileName: str = ...  # static # readonly
    MSScan_SchemaFileName: str = ...  # static # readonly
    MSScan_XSpecific_FileName: str = ...  # static # readonly
    MSScan_XSpecific_SchemaFileName: str = ...  # static # readonly
    MSTS_XSpecific_FileName: str = ...  # static # readonly
    MSTS_XSpecific_SchemaFileName: str = ...  # static # readonly
    MSTimeSegments_FileName: str = ...  # static # readonly
    MSTimeSegments_SchemaFileName: str = ...  # static # readonly
    MetID_Dir: str = ...  # static # readonly
    MethodAcq_Dir: str = ...  # static # readonly
    MethodDA_Dir: str = ...  # static # readonly
    MethodParamChange_FileName: str = ...  # static # readonly
    MethodParamDefinition_FileName: str = ...  # static # readonly
    MethodParamDefinition_SchemaFileName: str = ...  # static # readonly
    Method_LogName: str = ...  # static # readonly
    Methods_Dir: str = ...  # static # readonly
    MetlinDB_FileExtn: str = ...  # static # readonly
    Pcdl_FileExtn: str = ...  # static # readonly
    Profinder_dir: str = ...  # static # readonly
    QTOF_Default_Calibration_Masslist_FileName: str = ...  # static # readonly
    QTOF_MassLists_InstallLocation: str = ...  # static # readonly
    Qual_Dir: str = ...  # static # readonly
    Quant_Dir: str = ...  # static # readonly
    ReportOutput_DirName: str = ...  # static # readonly
    ReportTemplates_DirName: str = ...  # static # readonly
    Reprocessing_Dir: str = ...  # static # readonly
    Result_Dir: str = ...  # static # readonly
    SpecDirectory_FileExtn: str = ...  # static # readonly
    Spectrum_FileExtn: str = ...  # static # readonly
    UserCalBin_FileName: str = ...  # static # readonly
    UserCalIndex_FileName: str = ...  # static # readonly
    Worklist_FileName: str = ...  # static # readonly

class SharedMSStrings:  # Class
    A4_Paper_Size: str = ...  # static # readonly
    AcqData_Dir: str = ...  # static # readonly
    AcqMethod_Dir: str = ...  # static # readonly
    Acquisition_DirName: str = ...  # static # readonly
    Calibration_Masslist_SchemaFileName: str = ...  # static # readonly
    ChromDirectory_FileExtn: str = ...  # static # readonly
    Chromatogram_FileExtn: str = ...  # static # readonly
    Contents_FileName: str = ...  # static # readonly
    Contents_SchemaFileName: str = ...  # static # readonly
    CustomerHome_Location: str = ...  # static # readonly
    CustomerHome_RegKeyName: str = ...  # static # readonly
    DAMethod_Dir: str = ...  # static # readonly
    DefaultCalib_FileName: str = ...  # static # readonly
    DefaultCalib_SchemaFileName: str = ...  # static # readonly
    DeviceConfig_FileName: str = ...  # static # readonly
    Devices_FileName: str = ...  # static # readonly
    Devices_SchemaFileName: str = ...  # static # readonly
    InstallHome_Location: str = ...  # static # readonly
    InstallHome_RegKeyName: str = ...  # static # readonly
    Letter_Paper_Size: str = ...  # static # readonly
    MSActualsDefinition_FileName: str = ...  # static # readonly
    MSActualsDefinition_SchemaFileName: str = ...  # static # readonly
    MSCalibration_FileName: str = ...  # static # readonly
    MSPeak_DataFileName: str = ...  # static # readonly
    MSPeriodicActuals_FileName: str = ...  # static # readonly
    MSProfile_DataFileName: str = ...  # static # readonly
    MSScanActuals_FileName: str = ...  # static # readonly
    MSScan_BinaryFileName: str = ...  # static # readonly
    MSScan_SchemaFileName: str = ...  # static # readonly
    MSScan_XSpecific_FileName: str = ...  # static # readonly
    MSScan_XSpecific_SchemaFileName: str = ...  # static # readonly
    MSTS_XSpecific_FileName: str = ...  # static # readonly
    MSTS_XSpecific_SchemaFileName: str = ...  # static # readonly
    MSTimeSegments_FileName: str = ...  # static # readonly
    MSTimeSegments_SchemaFileName: str = ...  # static # readonly
    MetID_Dir: str = ...  # static # readonly
    MethodAcq_Dir: str = ...  # static # readonly
    MethodDA_Dir: str = ...  # static # readonly
    MethodParamChange_FileName: str = ...  # static # readonly
    MethodParamDefinition_FileName: str = ...  # static # readonly
    MethodParamDefinition_SchemaFileName: str = ...  # static # readonly
    Method_LogName: str = ...  # static # readonly
    Methods_Dir: str = ...  # static # readonly
    MetlinDB_FileExtn: str = ...  # static # readonly
    Pcdl_FileExtn: str = ...  # static # readonly
    QTOF_Default_Calibration_Masslist_FileName: str = ...  # static # readonly
    QTOF_MassLists_InstallLocation: str = ...  # static # readonly
    Qual_Dir: str = ...  # static # readonly
    Quant_Dir: str = ...  # static # readonly
    ReportOutput_DirName: str = ...  # static # readonly
    ReportTemplates_DirName: str = ...  # static # readonly
    Reprocessing_Dir: str = ...  # static # readonly
    Result_Dir: str = ...  # static # readonly
    SpecDirectory_FileExtn: str = ...  # static # readonly
    Spectrum_FileExtn: str = ...  # static # readonly
    Worklist_FileName: str = ...  # static # readonly

class SharedMSStrings:  # Class
    A4_Paper_Size: str = ...  # static # readonly
    AcqData_Dir: str = ...  # static # readonly
    AcqMethod_Dir: str = ...  # static # readonly
    Acquisition_DirName: str = ...  # static # readonly
    Calibration_Masslist_SchemaFileName: str = ...  # static # readonly
    ChromDirectory_FileExtn: str = ...  # static # readonly
    Chromatogram_FileExtn: str = ...  # static # readonly
    Contents_FileName: str = ...  # static # readonly
    Contents_SchemaFileName: str = ...  # static # readonly
    CustomerHome_Location: str = ...  # static # readonly
    CustomerHome_Location_64: str = ...  # static # readonly
    CustomerHome_RegKeyName: str = ...  # static # readonly
    DAMethod_Dir: str = ...  # static # readonly
    DefaultCalib_FileName: str = ...  # static # readonly
    DefaultCalib_SchemaFileName: str = ...  # static # readonly
    DeviceConfig_FileName: str = ...  # static # readonly
    Devices_FileName: str = ...  # static # readonly
    Devices_SchemaFileName: str = ...  # static # readonly
    IMS_Browser_Dir: str = ...  # static # readonly
    IMS_DefaultCal_InstallLocation: str = ...  # static # readonly
    ImsDefaultCal_FileName: str = ...  # static # readonly
    ImsFrameMeth_FileName: str = ...  # static # readonly
    ImsFrame_BinaryFileName: str = ...  # static # readonly
    ImsFrame_SchemaFileName: str = ...  # static # readonly
    ImsOverrideCal_FileName: str = ...  # static # readonly
    InstallHome_Location: str = ...  # static # readonly
    InstallHome_RegKeyName: str = ...  # static # readonly
    Letter_Paper_Size: str = ...  # static # readonly
    MSActualsDefinition_FileName: str = ...  # static # readonly
    MSActualsDefinition_SchemaFileName: str = ...  # static # readonly
    MSCalibration_FileName: str = ...  # static # readonly
    MSPeak_DataFileName: str = ...  # static # readonly
    MSPeriodicActuals_FileName: str = ...  # static # readonly
    MSProfile_DataFileName: str = ...  # static # readonly
    MSScanActuals_FileName: str = ...  # static # readonly
    MSScan_BinaryFileName: str = ...  # static # readonly
    MSScan_SchemaFileName: str = ...  # static # readonly
    MSScan_XSpecific_FileName: str = ...  # static # readonly
    MSScan_XSpecific_SchemaFileName: str = ...  # static # readonly
    MSTS_XSpecific_FileName: str = ...  # static # readonly
    MSTS_XSpecific_SchemaFileName: str = ...  # static # readonly
    MSTimeSegments_FileName: str = ...  # static # readonly
    MSTimeSegments_SchemaFileName: str = ...  # static # readonly
    MetID_Dir: str = ...  # static # readonly
    MethodAcq_Dir: str = ...  # static # readonly
    MethodDA_Dir: str = ...  # static # readonly
    MethodParamChange_FileName: str = ...  # static # readonly
    MethodParamDefinition_FileName: str = ...  # static # readonly
    MethodParamDefinition_SchemaFileName: str = ...  # static # readonly
    Method_LogName: str = ...  # static # readonly
    Methods_Dir: str = ...  # static # readonly
    MetlinDB_FileExtn: str = ...  # static # readonly
    Pcdl_FileExtn: str = ...  # static # readonly
    Profinder_dir: str = ...  # static # readonly
    QTOF_Default_Calibration_Masslist_FileName: str = ...  # static # readonly
    QTOF_MassLists_InstallLocation: str = ...  # static # readonly
    Qual_Dir: str = ...  # static # readonly
    Quant_Dir: str = ...  # static # readonly
    ReportOutput_DirName: str = ...  # static # readonly
    ReportTemplates_DirName: str = ...  # static # readonly
    Reprocessing_Dir: str = ...  # static # readonly
    Result_Dir: str = ...  # static # readonly
    SpecDirectory_FileExtn: str = ...  # static # readonly
    Spectrum_FileExtn: str = ...  # static # readonly
    UserCalBin_FileName: str = ...  # static # readonly
    UserCalIndex_FileName: str = ...  # static # readonly
    Worklist_FileName: str = ...  # static # readonly

class SharedMSStrings:  # Class
    A4_Paper_Size: str = ...  # static # readonly
    AcqData_Dir: str = ...  # static # readonly
    AcqMethod_Dir: str = ...  # static # readonly
    Acquisition_DirName: str = ...  # static # readonly
    Calibration_Masslist_SchemaFileName: str = ...  # static # readonly
    ChromDirectory_FileExtn: str = ...  # static # readonly
    Chromatogram_FileExtn: str = ...  # static # readonly
    Contents_FileName: str = ...  # static # readonly
    Contents_SchemaFileName: str = ...  # static # readonly
    CustomerHome_Location: str = ...  # static # readonly
    CustomerHome_RegKeyName: str = ...  # static # readonly
    DAMethod_Dir: str = ...  # static # readonly
    DefaultCalib_FileName: str = ...  # static # readonly
    DefaultCalib_SchemaFileName: str = ...  # static # readonly
    DeviceConfig_FileName: str = ...  # static # readonly
    Devices_FileName: str = ...  # static # readonly
    Devices_SchemaFileName: str = ...  # static # readonly
    InstallHome_Location: str = ...  # static # readonly
    InstallHome_RegKeyName: str = ...  # static # readonly
    Letter_Paper_Size: str = ...  # static # readonly
    MSActualsDefinition_FileName: str = ...  # static # readonly
    MSActualsDefinition_SchemaFileName: str = ...  # static # readonly
    MSCalibration_FileName: str = ...  # static # readonly
    MSPeak_DataFileName: str = ...  # static # readonly
    MSPeriodicActuals_FileName: str = ...  # static # readonly
    MSProfile_DataFileName: str = ...  # static # readonly
    MSScanActuals_FileName: str = ...  # static # readonly
    MSScan_BinaryFileName: str = ...  # static # readonly
    MSScan_SchemaFileName: str = ...  # static # readonly
    MSScan_XSpecific_FileName: str = ...  # static # readonly
    MSScan_XSpecific_SchemaFileName: str = ...  # static # readonly
    MSTS_XSpecific_FileName: str = ...  # static # readonly
    MSTS_XSpecific_SchemaFileName: str = ...  # static # readonly
    MSTimeSegments_FileName: str = ...  # static # readonly
    MSTimeSegments_SchemaFileName: str = ...  # static # readonly
    MetID_Dir: str = ...  # static # readonly
    MethodAcq_Dir: str = ...  # static # readonly
    MethodDA_Dir: str = ...  # static # readonly
    MethodParamChange_FileName: str = ...  # static # readonly
    MethodParamDefinition_FileName: str = ...  # static # readonly
    MethodParamDefinition_SchemaFileName: str = ...  # static # readonly
    Method_LogName: str = ...  # static # readonly
    Methods_Dir: str = ...  # static # readonly
    MetlinDB_FileExtn: str = ...  # static # readonly
    Pcdl_FileExtn: str = ...  # static # readonly
    QTOF_Default_Calibration_Masslist_FileName: str = ...  # static # readonly
    QTOF_MassLists_InstallLocation: str = ...  # static # readonly
    Qual_Dir: str = ...  # static # readonly
    Quant_Dir: str = ...  # static # readonly
    ReportOutput_DirName: str = ...  # static # readonly
    ReportTemplates_DirName: str = ...  # static # readonly
    Reprocessing_Dir: str = ...  # static # readonly
    Result_Dir: str = ...  # static # readonly
    SpecDirectory_FileExtn: str = ...  # static # readonly
    Spectrum_FileExtn: str = ...  # static # readonly
    Worklist_FileName: str = ...  # static # readonly

class SpectrumInfoWrapper(System.IDisposable):  # Class
    @overload
    def __init__(self, src: System.IntPtr) -> None: ...
    @overload
    def __init__(self) -> None: ...

    Baseline: float
    MaxY: float
    MinY: float
    Noise: float
    XAtMaxY: float

    def Dispose(self) -> None: ...

class SpectrumParamWrapper(System.IDisposable):  # Class
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.SpectrumParamWrapper) -> None: ...
    @overload
    def __init__(self, src: System.IntPtr) -> None: ...
    @overload
    def __init__(self) -> None: ...

    CalA: float
    CalTo: float
    MaxCountsPerTrans: int
    SaturationThreshold: float
    XIsTime: bool

    def Dispose(self) -> None: ...

class TofCalAutomation(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    FullAuto: Agilent.MassSpectrometry.TofCalAutomation = ...  # static # readonly
    PolyAutoMassWeightedTrad: Agilent.MassSpectrometry.TofCalAutomation = (
        ...
    )  # static # readonly
    PolyAutoTradAsSpecified: Agilent.MassSpectrometry.TofCalAutomation = (
        ...
    )  # static # readonly
    PolyAutoUnweightedTrad: Agilent.MassSpectrometry.TofCalAutomation = (
        ...
    )  # static # readonly

class TofCalWtEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Mass: Agilent.MassSpectrometry.TofCalWtEnum = ...  # static # readonly
    MassInv: Agilent.MassSpectrometry.TofCalWtEnum = ...  # static # readonly
    MassSqInv: Agilent.MassSpectrometry.TofCalWtEnum = ...  # static # readonly
    NoWeighting: Agilent.MassSpectrometry.TofCalWtEnum = ...  # static # readonly
    Time: Agilent.MassSpectrometry.TofCalWtEnum = ...  # static # readonly
    TimeInv: Agilent.MassSpectrometry.TofCalWtEnum = ...  # static # readonly
    TimeSqInv: Agilent.MassSpectrometry.TofCalWtEnum = ...  # static # readonly

class TofPfWrap(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def EnablePsFilters(self, enableFilter: bool) -> None: ...
    def LastSpectrumInformation(
        self,
    ) -> Agilent.MassSpectrometry.SpectrumInfoWrapper: ...
    def SetParameters(
        self,
        spectrum: Agilent.MassSpectrometry.SpectrumParamWrapper,
        baseline: Agilent.MassSpectrometry.BaselineParamWrapper,
        locate: Agilent.MassSpectrometry.PeakLocateParamWrapper,
        filter: Agilent.MassSpectrometry.PeakFilterParamWrapper,
    ) -> None: ...
    @overload
    def FindPeaksLw(
        self,
        xArray: List[float],
        yArray: List[float],
        yFullScale: float,
        minXPeak: float,
        maxXPeak: float,
        doCentroid: bool,
        doWidth: bool,
        doArea: bool,
        zeroBounded: bool,
    ) -> List[LwMsPeak]: ...
    @overload
    def FindPeaksLw(
        self,
        xArray: List[float],
        yArray: List[float],
        yFullScale: float,
        deltaX: float,
        minXPeak: float,
        maxXPeak: float,
        doCentroid: bool,
        doWidth: bool,
        doArea: bool,
    ) -> List[LwMsPeak]: ...
    @overload
    def FindPeaksLw(
        self,
        firstX: float,
        deltaX: float,
        yArray: List[float],
        numPoints: int,
        yFullScale: float,
        minXPeak: float,
        maxXPeak: float,
        doCentroid: bool,
        doWidth: bool,
        doArea: bool,
    ) -> List[LwMsPeak]: ...
    @overload
    def FindPeaks(
        self,
        xArray: List[float],
        yArray: List[float],
        yFullScale: float,
        minXPeak: float,
        maxXPeak: float,
        doCentroid: bool,
        doWidth: bool,
        doArea: bool,
        zeroBounded: bool,
    ) -> List[Agilent.MassSpectrometry.PeakInfoWrapper]: ...
    @overload
    def FindPeaks(
        self,
        xArray: List[float],
        yArray: List[float],
        yFullScale: float,
        deltaX: float,
        minXPeak: float,
        maxXPeak: float,
        doCentroid: bool,
        doWidth: bool,
        doArea: bool,
    ) -> List[Agilent.MassSpectrometry.PeakInfoWrapper]: ...
    @overload
    def FindPeaks(
        self,
        firstX: float,
        deltaX: float,
        yArray: List[float],
        numPoints: int,
        yFullScale: float,
        minXPeak: float,
        maxXPeak: float,
        doCentroid: bool,
        doWidth: bool,
        doArea: bool,
    ) -> List[Agilent.MassSpectrometry.PeakInfoWrapper]: ...
    def EnableHtCorrection(self, enableCorrection: bool) -> None: ...
    def SetAdvancedParameters(
        self, parms: Agilent.MassSpectrometry.AdvancedParamWrapper
    ) -> None: ...
    def Dispose(self) -> None: ...
    def EnableLbFilters(self, enableFilter: bool) -> None: ...

class WtcCalStepPolynomial(
    Agilent.MassSpectrometry.ITofCalStep,
    System.IDisposable,
    Agilent.MassSpectrometry.ITofCalStepPoly,
):  # Class
    @overload
    def __init__(
        self, source: Agilent.MassSpectrometry.WtcCalStepPolynomial
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    Coefficients: List[float]
    MaxTerms: int
    PowerFlags: int
    TMax: float
    TMin: float
    Weighting: Agilent.MassSpectrometry.TofCalWtEnum

    def Dispose(self) -> None: ...
    def Clone(self) -> Agilent.MassSpectrometry.ITofCalStepPoly: ...

class WtcCalStepTraditional(
    Agilent.MassSpectrometry.ITofCalStepTrad,
    System.IDisposable,
    Agilent.MassSpectrometry.ITofCalStep,
):  # Class
    @overload
    def __init__(
        self, source: Agilent.MassSpectrometry.WtcCalStepTraditional
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    A: float
    To: float
    Weighting: Agilent.MassSpectrometry.TofCalWtEnum

    def Dispose(self) -> None: ...
    def Clone(self) -> Agilent.MassSpectrometry.ITofCalStepTrad: ...

class WtcCalibration(
    System.IDisposable, System.ContextBoundObject, Agilent.MassSpectrometry.ITofCal
):  # Class
    @overload
    def __init__(self, source: Agilent.MassSpectrometry.WtcCalibration) -> None: ...
    @overload
    def __init__(self, enableLogging: bool) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetStep(self, index: int) -> Agilent.MassSpectrometry.ITofCalStep: ...
    def ClearSteps(self) -> None: ...
    def TimesToMasses(self, times: List[float], masses: List[float]) -> None: ...
    def EndLogging(self) -> None: ...
    def FullRecalMinMassRange(self) -> float: ...
    def MassToTime(self, mass: float) -> float: ...
    def RecalibrateStep2(self, times: List[float], masses: List[float]) -> None: ...
    def Dispose(self) -> None: ...
    def StepCount(self) -> int: ...
    def TimeToMass(self, time: float) -> float: ...
    def NewTradStep(self) -> Agilent.MassSpectrometry.ITofCalStepTrad: ...
    def NewPolyStep(self) -> Agilent.MassSpectrometry.ITofCalStepPoly: ...
    def SetFullRecalibrationLimits(
        self, minMass: float, minMassRange: float
    ) -> None: ...
    def UpdateStep(
        self, index: int, step: Agilent.MassSpectrometry.ITofCalStep
    ) -> None: ...
    @overload
    def Recalibrate(self, times: List[float], masses: List[float]) -> None: ...
    @overload
    def Recalibrate(
        self, times: List[float], masses: List[float], preferA: bool, preferSvd: bool
    ) -> None: ...
    def Equals(self, other: Agilent.MassSpectrometry.ITofCal) -> bool: ...
    @overload
    def Calibrate(
        self,
        times: List[float],
        masses: List[float],
        calOption: Agilent.MassSpectrometry.TofCalAutomation,
    ) -> None: ...
    @overload
    def Calibrate(self, times: List[float], masses: List[float]) -> None: ...
    @overload
    def Calibrate(
        self,
        times: List[float],
        masses: List[float],
        calOption: Agilent.MassSpectrometry.TofCalAutomation,
        preferSvd: bool,
    ) -> None: ...
    def Clone(self) -> Agilent.MassSpectrometry.ITofCal: ...
    def MassesToTimes(self, masses: List[float], times: List[float]) -> None: ...
    def AppendStep(self, step: Agilent.MassSpectrometry.ITofCalStep) -> None: ...
    def FullRecalMinMass(self) -> float: ...
