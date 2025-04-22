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
    DesiredMSStorageType,
    DoubleParameterLimit,
    IAcqMetaData,
    IActuals,
    IBDADataAccess,
    IBDAFileInformation,
    IBdaMsScanRecordCollection,
    IChromatogram,
    IDataAccess,
    IPSetDeviceDelayInfo,
    IPSetExcludeMass,
    IPSetExtractChrom,
    IPSetExtractSpectrum,
    IPSetPeakID,
    IPSetPeakSpectrumExtraction,
    IPSetPrecision,
    IPSetRangeCollection,
    IPSetTofCalibration,
    IPSetUnits,
    IRange,
    IReadChromatogram,
    IReadSpectra,
    ISample,
    ISpectrum,
    IUserCalibration,
    MSScanType,
    RangeCollection,
    SampleCategory,
    SpecType,
)
from .FD import (
    Feature,
    FeatureDetectionCompleted,
    FeatureDetectionParams,
    FeatureDetectionStarted,
    IFeatureSet,
    IFeatureSetQuery,
    IRidgeSet,
    ISampleFeatures,
    ISampleRidges,
    IScanSpace,
    Ridge,
    RidgeDetectionCancelled,
    RidgeDetectionCompleted,
    RidgeDetectionParams,
    RidgeDetectionStarted,
    RidgeDetectionStepDone,
    RidgeDetector,
    SampleFeatureDetector,
    ScanConditions,
)
from .Quantitative import INumericFormat
from .Quantitative.IndexedData import NonMSDataPoint

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess

class DefaultNumericFormat(INumericFormat):  # Class
    def __init__(self) -> None: ...

class FeatureFile(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    IsOpen: bool  # readonly
    IsReadOnly: bool  # readonly
    Version: int  # readonly

    def Read(
        self,
        fdParams: FeatureDetectionParams,
        sampleRidges: Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.SampleRidges,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.SampleFeatures: ...
    def Write(
        self,
        sf: Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.SampleFeatures,
        sampleDataPath: str,
    ) -> None: ...
    def Open(self, sampleDataPath: str, readOnly: bool) -> None: ...
    @staticmethod
    def GetFeatureFilePath(sampleDataPath: str) -> str: ...
    def DebugWriteSaturatedFeatures(
        self, sf: Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.SampleFeatures
    ) -> None: ...
    def Close(self) -> None: ...
    @staticmethod
    def Exists(sampleDataPath: str) -> bool: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def ExistsAndIsUpToDate(sampleDataPath: str) -> bool: ...

class FeatureSet(IFeatureSetQuery, IFeatureSet):  # Class
    @overload
    def __init__(
        self, scanSpace: IScanSpace, fdParams: FeatureDetectionParams, readOnly: bool
    ) -> None: ...
    @overload
    def __init__(
        self,
        scanSpace: IScanSpace,
        fdParams: FeatureDetectionParams,
        version: int,
        readOnly: bool,
    ) -> None: ...

    Count: int  # readonly
    FeatureDetectionParams: FeatureDetectionParams  # readonly
    SaturatedCount: int  # readonly
    ScanSpace: IScanSpace  # readonly

    @overload
    def GetFeatures(self) -> System.Collections.Generic.List[Feature]: ...
    @overload
    def GetFeatures(
        self, rtStart: float, rtEnd: float
    ) -> System.Collections.Generic.List[Feature]: ...
    @overload
    def GetFeatures(
        self, startScanIndex: int, endScanIndex: int
    ) -> System.Collections.Generic.List[Feature]: ...
    def GetCoelutingFeatures(
        self, apexScanIndex: int
    ) -> System.Collections.Generic.List[Feature]: ...
    def Add(self, f: Feature) -> None: ...
    def DebugWriteProtoComponents(self) -> None: ...
    @overload
    def GetFeaturesInRange(
        self, rtStart: float, rtEnd: float, mzLow: float, mzHigh: float
    ) -> System.Collections.Generic.List[Feature]: ...
    @overload
    def GetFeaturesInRange(
        self, minScanIndex: int, maxScanIndex: int, mzLow: float, mzHigh: float
    ) -> System.Collections.Generic.List[Feature]: ...
    def GetFeatureByID(self, featureID: int) -> Feature: ...
    def DebugWriteSaturatedFeatures(self, sw: System.IO.StreamWriter) -> None: ...
    def ReadFeatures(self, br: System.IO.BinaryReader) -> None: ...
    def GetFeaturesInFlightTimeRange(
        self, rtStart: float, rtEnd: float, lowFlightTime: float, highFlightTime: float
    ) -> System.Collections.Generic.List[Feature]: ...
    def WriteFeatures(self, bw: System.IO.BinaryWriter) -> None: ...
    def GetFeaturesInRidge(
        self, ridge: Ridge
    ) -> System.Collections.Generic.List[Feature]: ...
    def GetFeaturesInMzRange(
        self, mzLow: float, mzHigh: float
    ) -> System.Collections.Generic.List[Feature]: ...

class ITofDataConversion(object):  # Interface
    def ConvertToTDAFormat(self, dataPath: str) -> None: ...
    def FeatureDataExistsForSample(self, sampleDataPath: str) -> bool: ...
    def IsSampleTDAConvertible(self, sampleDataPath: str) -> bool: ...
    def CanDetectFeaturesForSample(self, sampleDataPath: str) -> bool: ...
    def IsSampleTDAConverted(self, sampleDataPath: str) -> bool: ...
    def DetectFeatures(self, dataPath: str) -> None: ...
    def RemoveFeatureData(self, dataPath: str) -> None: ...
    def RemoveTDA(self, dataPath: str) -> None: ...

    FeatureDetectionCompleted: FeatureDetectionCompleted  # Event
    FeatureDetectionStarted: FeatureDetectionStarted  # Event
    RidgeDetectionCancelled: RidgeDetectionCancelled  # Event
    RidgeDetectionCompleted: RidgeDetectionCompleted  # Event
    RidgeDetectionStarted: RidgeDetectionStarted  # Event
    RidgeDetectionStepDone: RidgeDetectionStepDone  # Event

class RidgeFile(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    FilePath: str  # readonly
    IsOpen: bool  # readonly
    IsReadOnly: bool  # readonly
    Version: int  # readonly

    def Read(
        self, rdParams: RidgeDetectionParams
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.SampleRidges: ...
    def Write(
        self,
        ridges: Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.SampleRidges,
        sampleDataPath: str,
    ) -> None: ...
    def Open(self, sampleDataPath: str, readOnly: bool) -> None: ...
    def Close(self) -> None: ...
    @staticmethod
    def GetRidgeFilePath(sampleDataPath: str) -> str: ...
    @staticmethod
    def Exists(sampleDataPath: str) -> bool: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def ExistsAndIsUpToDate(sampleDataPath: str) -> bool: ...

class RidgeSet(IRidgeSet):  # Class
    @overload
    def __init__(self, rd: RidgeDetector) -> None: ...
    @overload
    def __init__(
        self, scanSpace: IScanSpace, rdParams: RidgeDetectionParams
    ) -> None: ...

    Count: int  # readonly
    NoiseFactor2: float  # readonly
    RidgeDetectionParams: RidgeDetectionParams  # readonly
    RidgeList: System.Collections.Generic.List[Ridge]  # readonly
    SaturationLimit: float  # readonly
    ScanSpace: IScanSpace  # readonly

    def Add(self, ridge: Ridge) -> None: ...
    def ReadRidges(self, br: System.IO.BinaryReader, version: int) -> None: ...
    def GetRidge(self, scanIndex: int, flightTime: float) -> Ridge: ...
    def GetRidgeByID(self, ridgeId: int) -> Ridge: ...
    @overload
    def GetRidgesInRange(
        self, rtMin: float, rtMax: float, mzMin: float, mzMax: float
    ) -> System.Collections.Generic.List[Ridge]: ...
    @overload
    def GetRidgesInRange(
        self, minScanIndex: int, maxScanIndex: int, mzMin: float, mzMax: float
    ) -> System.Collections.Generic.List[Ridge]: ...
    def WriteRidges(self, bw: System.IO.BinaryWriter) -> None: ...

class SampleFeatures(ISampleFeatures):  # Class
    def __init__(self) -> None: ...

    ScanConditionCount: int  # readonly
    ScanConditionList: System.Collections.Generic.List[ScanConditions]  # readonly

    def GetFeatureSet(self, scanConditions: ScanConditions) -> IFeatureSet: ...
    def GetScanSpace(self, scanConditions: ScanConditions) -> IScanSpace: ...
    def CreateFeatureSet(
        self, scanSpace: IScanSpace, fdParams: FeatureDetectionParams
    ) -> IFeatureSet: ...
    def GetWritableFeatureSet(self, scanConditions: ScanConditions) -> IFeatureSet: ...
    def GetFeatureSets(self) -> System.Collections.Generic.List[IFeatureSet]: ...
    def GetFeatureSetForMassCalibration(
        self, scanConditions: ScanConditions
    ) -> IFeatureSet: ...
    def AddFeatureSet(self, scanSpace: IScanSpace, featureSet: IFeatureSet) -> None: ...

class SampleRidges(ISampleRidges):  # Class
    def __init__(self) -> None: ...

    ScanConditionCount: int  # readonly
    ScanConditionList: System.Collections.Generic.List[ScanConditions]  # readonly

    def AddRidgeSet(self, scanSpace: IScanSpace, ridgeSet: IRidgeSet) -> None: ...
    def GetScanSpace(self, scanConditions: ScanConditions) -> IScanSpace: ...
    def GetRidgeSets(self) -> System.Collections.Generic.List[IRidgeSet]: ...
    def GetRidgeSet(self, scanConditions: ScanConditions) -> IRidgeSet: ...
    def AddDetectedRidgeSet(self, rd: RidgeDetector) -> None: ...

class TofDataConversion(
    Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.ITofDataConversion
):  # Class
    def ConvertToTDAFormat(self, dataPath: str) -> None: ...
    def FeatureDataExistsForSample(self, sampleDataPath: str) -> bool: ...
    def IsSampleTDAConvertible(self, sampleDataPath: str) -> bool: ...
    def CanDetectFeaturesForSample(self, sampleDataPath: str) -> bool: ...
    def IsSampleTDAConverted(self, sampleDataPath: str) -> bool: ...
    def DetectFeatures(self, dataPath: str) -> None: ...
    def RemoveFeatureData(self, dataPath: str) -> None: ...
    def RemoveTDA(self, dataPath: str) -> None: ...

    FeatureDetectionCompleted: FeatureDetectionCompleted  # Event
    FeatureDetectionStarted: FeatureDetectionStarted  # Event
    RidgeDetectionCancelled: RidgeDetectionCancelled  # Event
    RidgeDetectionCompleted: RidgeDetectionCompleted  # Event
    RidgeDetectionStarted: RidgeDetectionStarted  # Event
    RidgeDetectionStepDone: RidgeDetectionStepDone  # Event

class TofFeatureDataAccess(
    ISample,
    IActuals,
    IDataAccess,
    IReadChromatogram,
    System.IDisposable,
    IReadSpectra,
    IUserCalibration,
):  # Class
    AcquisitionMetaData: IAcqMetaData  # readonly
    BaseDataAccess: IBDADataAccess  # readonly
    DataFileName: str  # readonly
    DataUnit: IPSetUnits  # readonly
    DesiredMSStorageTypeToUse: DesiredMSStorageType
    FallbackDA: IDataAccess  # readonly
    FeatureFile: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.FeatureFile
    )  # readonly
    FileInformation: IBDAFileInformation  # readonly
    MassRangesOverallLimit: DoubleParameterLimit  # readonly
    MostRecentlyUsed: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.TofFeatureDataAccess
    )  # static # readonly
    PrecisionType: IPSetPrecision  # readonly
    RidgeFile: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.RidgeFile
    )  # readonly
    RidgeFileExists: bool  # readonly
    SampleDataPath: str  # readonly
    SampleFeatureDetector: SampleFeatureDetector  # readonly
    SampleFeatures: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.SampleFeatures
    )  # readonly
    SampleRidges: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.SampleRidges
    )  # readonly
    ScanConditionList: System.Collections.Generic.List[ScanConditions]  # readonly
    ScanRejectionFlagValueTable: System.Data.DataTable
    SchemaDefaultDirectory: str

    def UpdateDelayInformation(self, psetDeviceDelay: IPSetDeviceDelayInfo) -> None: ...
    @overload
    def FindSampleFeatures(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.SampleFeatures: ...
    @overload
    def FindSampleFeatures(
        self, rdParams: RidgeDetectionParams, fdParams: FeatureDetectionParams
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.SampleFeatures: ...
    @overload
    def ReadSpectrum(
        self, spectrumRequest: IPSetExtractSpectrum
    ) -> List[ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self,
        spectrumRequest: IPSetExtractSpectrum,
        backgroundSpecArrayToSubtract: List[ISpectrum],
    ) -> List[ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self, specType: SpecType, scanIDArray: List[int]
    ) -> List[ISpectrum]: ...
    @overload
    def ReadSpectrum(self, scanNumber: int, bMassUnits: bool) -> ISpectrum: ...
    @overload
    def ReadSpectrum(
        self,
        apseParameters: IPSetPeakSpectrumExtraction,
        specRequest: IPSetExtractSpectrum,
        sourceChromatogram: IChromatogram,
        backgroundSpectrum: List[ISpectrum],
        peakNumber: int,
    ) -> List[ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self,
        specType: SpecType,
        scanIDArray: List[int],
        desiredStorageMode: DesiredMSStorageType,
    ) -> List[ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self,
        specRequest: IPSetExtractSpectrum,
        apseParameters: IPSetPeakSpectrumExtraction,
        peakIDParam: IPSetPeakID,
    ) -> List[ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self,
        specRequest: IPSetExtractSpectrum,
        apseParameters: IPSetPeakSpectrumExtraction,
        peakIDParam: IPSetPeakID,
        startEndTimeRanges: IPSetRangeCollection,
    ) -> List[ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self, rowIndex: int, bMassUnits: bool, desiredStorageMode: DesiredMSStorageType
    ) -> ISpectrum: ...
    @overload
    @staticmethod
    def GetInstance(
        sampleDataDir: str,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.TofFeatureDataAccess
    ): ...
    @overload
    @staticmethod
    def GetInstance(
        sampleDataDir: str, numberFormat: INumericFormat
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.TofFeatureDataAccess
    ): ...
    @staticmethod
    def GetTofDataConversion() -> (
        Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.ITofDataConversion
    ): ...
    def Dispose(self) -> None: ...
    def RefreshDataFile(self, isNewDataPresent: bool) -> bool: ...
    def GetSampleValue(self, internalName: str) -> str: ...
    def CloseDataFile(self) -> None: ...
    def GetActuals(self, timeInMins: float) -> System.Data.DataSet: ...
    def GetActualValue(
        self, actualDisplayName: str, xArray: List[float], yArray: List[float]
    ) -> None: ...
    def GetTimeSegmentsIDArray(self) -> List[int]: ...
    def GetDeviceSignalInfo(
        self,
    ) -> System.Collections.Generic.List[NonMSDataPoint]: ...
    @staticmethod
    def ClearCache() -> None: ...
    def GetFeatureSet(self, scanConditions: ScanConditions) -> IFeatureSet: ...
    @overload
    def GetSampleData(self, category: SampleCategory) -> System.Data.DataSet: ...
    @overload
    def GetSampleData(self, internalNamePrefix: str) -> System.Data.DataSet: ...
    def GetTotalRidgeCount(self) -> int: ...
    def GetDataDependentScanInfo(self) -> IBdaMsScanRecordCollection: ...
    @overload
    def SaveUserCalibration(self, psetTofCalib: IPSetTofCalibration) -> None: ...
    @overload
    def SaveUserCalibration(
        self, specArray: List[ISpectrum], psetTofCalib: IPSetTofCalibration
    ) -> None: ...
    def GetSaturatedFeatureCount(self) -> int: ...
    def ClearScanRejectionFlagValueTable(self) -> None: ...
    def GetSignals(self, deviceKey: str) -> System.Collections.Generic.List[str]: ...
    def IsActualsPresent(self) -> bool: ...
    @overload
    def ReadChromatogram(
        self, extractParamSet: IPSetExtractChrom
    ) -> List[IChromatogram]: ...
    @overload
    def ReadChromatogram(
        self, extractParamSet: IPSetExtractChrom, excludeParamSet: IPSetExcludeMass
    ) -> List[IChromatogram]: ...
    def SetUnitPrecisionValue(
        self, psetUnits: IPSetUnits, psetPrecision: IPSetPrecision
    ) -> None: ...
    def GetTimeSegmentDetails(self, timesegmentID: int, numOfScans: int) -> IRange: ...
    def GetTimeSegmentRanges(self) -> RangeCollection: ...
    def GetActualNames(self) -> List[str]: ...
    def IsFileOpen(self) -> bool: ...
    def IsUserCalibrationPresent(self) -> bool: ...
    @overload
    def OpenDataFile(self, dataDir: str, bOptimizeFileHandling: bool) -> bool: ...
    @overload
    def OpenDataFile(self, dataDir: str) -> bool: ...
    def IsAcquisitionStatusComplete(self) -> bool: ...
    @staticmethod
    def ClearCacheExcept(
        tfda: Agilent.MassSpectrometry.DataAnalysis.FeatureDataAccess.TofFeatureDataAccess,
    ) -> None: ...
    def GetScanRecordsInfo(
        self, scanType: MSScanType
    ) -> IBdaMsScanRecordCollection: ...
    def ClearUserCalibration(self) -> None: ...
    def GetTotalFeatureCount(self) -> int: ...
    def UpdateMassCalibration(
        self, referenceMZValues: Dict[Feature, float], A: float, T0: float
    ) -> str: ...
    def SetUnitValue(self, psetUnits: IPSetUnits) -> None: ...
    def GetRidgeSet(self, scanConditions: ScanConditions) -> IRidgeSet: ...
    def PersistScanRejectionFlagValueTable(self) -> None: ...
    def IsDataDependentScanInfoPresent(self) -> bool: ...
    def GetMsDeviceDelayTime(self, dDelay: float) -> bool: ...
    def GetElementNameCollection(self, timesegmentID: int) -> Dict[float, str]: ...
