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
    AcquisitionMethod,
    DevicesXmlReader,
    DoubleRange,
    DoubleRangeCollection,
    IntRange,
    INumericFormat,
    MSScanData,
    QuantDataAccess,
    ScanRecord,
    Transition,
)
from .CoreDataTypes import ChromSpecData, IChromSpecData, IQuantMSScanInfo

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData

class AccessType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Read: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.AccessType = (
        ...
    )  # static # readonly
    Write: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.AccessType = (
        ...
    )  # static # readonly

class ChromFilter:  # Class
    RTRange: DoubleRange

class ConversionEventArgs:  # Class
    def __init__(self, dataPath: str) -> None: ...

    DataPath: str  # readonly

class ConversionFinishedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, e: System.EventArgs) -> None: ...

class ConversionStartingEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ConversionEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ConversionEventArgs,
    ) -> None: ...

class ConverterConfig:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, xmlFileName: str) -> None: ...

    DEFAULT_CONFIG_FILE_NAME: str = ...  # static # readonly

    Alpha: float  # readonly
    ConvertProfileData: bool  # readonly
    M_0: float  # readonly
    MaxBlockColumns: int
    MaxSpectrumColumns: int
    NumBlockRows: int
    NumRecordsPerBlock: int
    NumRecordsPerSpectrumColumn: int
    Rmax: float  # readonly
    SmallNumOfScanRecords: int

class ConverterLog(System.IDisposable):  # Class
    def __init__(self, logDir: str) -> None: ...

    LOG_FILE_NAME: str = ...  # static # readonly

    LogFilePath: str  # readonly

    def Dispose(self) -> None: ...

class DataHeader:  # Class
    def __init__(self) -> None: ...

    InstrumentName: str
    InstrumentType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.InstrumentType
    )
    IsProfileData: bool
    MSDataPresent: bool
    MaxMz: float
    MaxRT: float
    MinMz: float
    MinRT: float
    NonMSDataPresent: bool
    SeparationType: Agilent.MassSpectrometry.DataAnalysis.SeparationTechnique
    Version: int  # readonly

    def GetChromatographicRange(self) -> DoubleRange: ...

class IAxisGrid(object):  # Interface
    PointCount: int  # readonly

    def GetIndexOfNearestPointAbove(self, value_: float) -> int: ...
    def GetPointByIndex(self, index: int) -> float: ...
    def GetIndexOfNearestPointBelow(self, value_: float) -> int: ...
    def GetIndexOfNearestPoint(self, value_: float) -> int: ...

class IMSDataTree(IQuantMSScanInfo, System.IDisposable):  # Interface
    Header: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.DataHeader

    def Read(self, br: System.IO.BinaryReader) -> None: ...
    def Write(self, bw: System.IO.BinaryWriter) -> None: ...
    def AddTICPoint(
        self,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def GetChromData(
        self,
        chromFilter: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSChromFilter,
    ) -> IChromSpecData: ...
    def SubtractDataPoint(
        self,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def AddDataPoint(
        self,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def GetSpecData(
        self,
        specFilter: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSSpecFilter,
    ) -> IChromSpecData: ...
    def AddScanRecord(
        self,
        scanRecord: ScanRecord,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def GetScanDeskewParameters(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        selectedMZ: float,
        mzHigh: float,
        skewRate: float,
    ) -> None: ...

class IndexedDataAccess(
    Agilent.MassSpectrometry.DataAnalysis.IReadSpectra,
    Agilent.MassSpectrometry.DataAnalysis.IDataAccess,
    Agilent.MassSpectrometry.DataAnalysis.ISample,
    Agilent.MassSpectrometry.DataAnalysis.IActuals,
    Agilent.MassSpectrometry.DataAnalysis.IReadChromatogram,
    Agilent.MassSpectrometry.DataAnalysis.IUserCalibration,
    System.IDisposable,
):  # Class
    @overload
    def __init__(self, numberFormat: INumericFormat) -> None: ...
    @overload
    def __init__(self, sampleDataPath: str, numberFormat: INumericFormat) -> None: ...
    @overload
    def __init__(
        self, sampleDataPath: str, tof: bool, numberFormat: INumericFormat
    ) -> None: ...

    INDEXED_FILE: str = ...  # static # readonly
    OLD_INDEXED_FILE: str = ...  # static # readonly
    TOF_DATA_FILE: str = ...  # static # readonly
    TOF_INDEXED_FILE: str = ...  # static # readonly
    TOF_SPEC_DATA_FILE: str = ...  # static # readonly

    AcquisitionMetaData: Agilent.MassSpectrometry.DataAnalysis.IAcqMetaData  # readonly
    BaseDataAccess: Agilent.MassSpectrometry.DataAnalysis.IBDADataAccess  # readonly
    DataFileName: str  # readonly
    DataUnit: Agilent.MassSpectrometry.DataAnalysis.IPSetUnits  # readonly
    DesiredMSStorageTypeToUse: (
        Agilent.MassSpectrometry.DataAnalysis.DesiredMSStorageType
    )
    FileInformation: (
        Agilent.MassSpectrometry.DataAnalysis.IBDAFileInformation
    )  # readonly
    InstrumentType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.InstrumentType
    )  # readonly
    MassRangesOverallLimit: (
        Agilent.MassSpectrometry.DataAnalysis.DoubleParameterLimit
    )  # readonly
    Polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity  # readonly
    PrecisionType: Agilent.MassSpectrometry.DataAnalysis.IPSetPrecision  # readonly
    ScanRejectionFlagValueTable: System.Data.DataTable
    ScanTypes: Agilent.MassSpectrometry.DataAnalysis.MSScanType  # readonly
    SchemaDefaultDirectory: str
    TimeSegments: Agilent.MassSpectrometry.DataAnalysis.RangeCollection  # readonly

    def UpdateDelayInformation(
        self,
        psetDeviceDelay: Agilent.MassSpectrometry.DataAnalysis.IPSetDeviceDelayInfo,
    ) -> None: ...
    def GetScanSpace(
        self,
        scanConditions: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ScanConditions,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ScanSpace: ...
    @overload
    def ReadSpectrum(
        self,
        spectrumRequest: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self,
        spectrumRequest: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum,
        backgroundSpecArrayToSubtract: List[
            Agilent.MassSpectrometry.DataAnalysis.ISpectrum
        ],
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self,
        specType: Agilent.MassSpectrometry.DataAnalysis.SpecType,
        scanIDArray: List[int],
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self, scanNumber: int, bMassUnits: bool
    ) -> Agilent.MassSpectrometry.DataAnalysis.ISpectrum: ...
    @overload
    def ReadSpectrum(
        self,
        apseParameters: Agilent.MassSpectrometry.DataAnalysis.IPSetPeakSpectrumExtraction,
        specRequest: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum,
        sourceChromatogram: Agilent.MassSpectrometry.DataAnalysis.IChromatogram,
        backgroundSpectrum: List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum],
        peakNumber: int,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self,
        specType: Agilent.MassSpectrometry.DataAnalysis.SpecType,
        scanIDArray: List[int],
        desiredStorageMode: Agilent.MassSpectrometry.DataAnalysis.DesiredMSStorageType,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self,
        specRequest: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum,
        apseParameters: Agilent.MassSpectrometry.DataAnalysis.IPSetPeakSpectrumExtraction,
        peakIDParam: Agilent.MassSpectrometry.DataAnalysis.IPSetPeakID,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self,
        specRequest: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum,
        apseParameters: Agilent.MassSpectrometry.DataAnalysis.IPSetPeakSpectrumExtraction,
        peakIDParam: Agilent.MassSpectrometry.DataAnalysis.IPSetPeakID,
        startEndTimeRanges: Agilent.MassSpectrometry.DataAnalysis.IPSetRangeCollection,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum]: ...
    @overload
    def ReadSpectrum(
        self,
        rowIndex: int,
        bMassUnits: bool,
        desiredStorageMode: Agilent.MassSpectrometry.DataAnalysis.DesiredMSStorageType,
    ) -> Agilent.MassSpectrometry.DataAnalysis.ISpectrum: ...
    @overload
    def GetMRMTransitions(
        self, polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...
    @overload
    def GetMRMTransitions(
        self,
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...
    def Dispose(self) -> None: ...
    def RefreshDataFile(self, isNewDataPresent: bool) -> bool: ...
    def GetPolarities(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    ]: ...
    def GetSampleValue(self, internalName: str) -> str: ...
    def CloseDataFile(self) -> None: ...
    def GetActuals(self, timeInMins: float) -> System.Data.DataSet: ...
    def SubtractBackground(
        self,
        specPeakFinder: Agilent.MassSpectrometry.DataAnalysis.IFindPeaks,
        ticPeakFinder: Agilent.MassSpectrometry.DataAnalysis.IFindPeaks,
    ) -> None: ...
    def GetActualValue(
        self, actualDisplayName: str, xArray: List[float], yArray: List[float]
    ) -> None: ...
    def GetScanDeskewParameters(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        selectedMZ: float,
        mzHigh: float,
        skewRate: float,
    ) -> None: ...
    def GetTimeSegmentsIDArray(self) -> List[int]: ...
    def GetDeviceSignalInfo(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.NonMSDataPoint
    ]: ...
    @overload
    def GetSampleData(
        self, category: Agilent.MassSpectrometry.DataAnalysis.SampleCategory
    ) -> System.Data.DataSet: ...
    @overload
    def GetSampleData(self, internalNamePrefix: str) -> System.Data.DataSet: ...
    @overload
    @staticmethod
    def GetIndexedFileName(dataDir: str, tof: bool) -> str: ...
    @overload
    @staticmethod
    def GetIndexedFileName(dataDir: str) -> str: ...
    def GetSelectedMZs(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Collections.Generic.List[float]: ...
    def GetDataDependentScanInfo(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.IBdaMsScanRecordCollection: ...
    @overload
    def SaveUserCalibration(
        self, psetTofCalib: Agilent.MassSpectrometry.DataAnalysis.IPSetTofCalibration
    ) -> None: ...
    @overload
    def SaveUserCalibration(
        self,
        specArray: List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum],
        psetTofCalib: Agilent.MassSpectrometry.DataAnalysis.IPSetTofCalibration,
    ) -> None: ...
    def ClearScanRejectionFlagValueTable(self) -> None: ...
    def GetSignals(self, deviceKey: str) -> System.Collections.Generic.List[str]: ...
    def IsActualsPresent(self) -> bool: ...
    @overload
    def ReadChromatogram(
        self, extractParamSet: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.IChromatogram]: ...
    @overload
    def ReadChromatogram(
        self,
        extractParamSet: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom,
        excludeParamSet: Agilent.MassSpectrometry.DataAnalysis.IPSetExcludeMass,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.IChromatogram]: ...
    def SetUnitPrecisionValue(
        self,
        psetUnits: Agilent.MassSpectrometry.DataAnalysis.IPSetUnits,
        psetPrecision: Agilent.MassSpectrometry.DataAnalysis.IPSetPrecision,
    ) -> None: ...
    def GetTimeSegmentDetails(
        self, timesegmentID: int, numOfScans: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.IRange: ...
    def GetTimeSegmentRanges(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.RangeCollection: ...
    def GetActualNames(self) -> List[str]: ...
    @overload
    @staticmethod
    def GotIndexedData(dataDir: str) -> bool: ...
    @overload
    @staticmethod
    def GotIndexedData(dataDir: str, tof: bool) -> bool: ...
    def IsFileOpen(self) -> bool: ...
    def IsUserCalibrationPresent(self) -> bool: ...
    def IsAcquisitionStatusComplete(self) -> bool: ...
    @overload
    def OpenDataFile(self, dataDir: str) -> bool: ...
    @overload
    def OpenDataFile(self, dataDir: str, bOptimizeFileHandling: bool) -> bool: ...
    def GetScanRecordsInfo(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> Agilent.MassSpectrometry.DataAnalysis.IBdaMsScanRecordCollection: ...
    def ClearUserCalibration(self) -> None: ...
    def GetTransitions(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...
    def GetMZs(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        selectedMZ: float,
    ) -> System.Collections.Generic.List[float]: ...
    def SetUnitValue(
        self, psetUnits: Agilent.MassSpectrometry.DataAnalysis.IPSetUnits
    ) -> None: ...
    @overload
    @staticmethod
    def InitOverallMzScanRange(
        header: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.DataHeader,
        sampleDataPath: str,
        scanData: MSScanData,
    ) -> None: ...
    @overload
    @staticmethod
    def InitOverallMzScanRange(
        header: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.DataHeader,
        sampleDataPath: str,
        scanData: MSScanData,
        acqMethod: AcquisitionMethod,
    ) -> None: ...
    def PersistScanRejectionFlagValueTable(self) -> None: ...
    def IsDataDependentScanInfoPresent(self) -> bool: ...
    @staticmethod
    def ConvertPSetToNonMSSpecFilter(
        pset: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.NonMSSpecFilter
    ): ...
    @staticmethod
    def ConvertPSetToMSChromFilter(
        pset: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSChromFilter
    ): ...
    @staticmethod
    def ConvertPSetToNonMSChromFilter(
        pset: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.NonMSChromFilter
    ): ...
    def GetMsDeviceDelayTime(self, dDelay: float) -> bool: ...
    def GetElementNameCollection(self, timesegmentID: int) -> Dict[float, str]: ...

class IndexedDataConverter:  # Class
    def __init__(self, batchDataDir: str, overwrite: bool) -> None: ...

    Cancelled: bool  # readonly
    Error: bool  # readonly
    Log: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ConverterLog
    )  # readonly

    @staticmethod
    def IsConvertedSample(path: str) -> bool: ...
    @staticmethod
    def IgnoredDirectory(path: str) -> bool: ...
    @staticmethod
    def IsConvertibleSampleDirectory(path: str) -> bool: ...
    def CountSamples(self, path: str) -> int: ...
    @staticmethod
    def IsSampleDataDirectory(path: str) -> bool: ...
    @staticmethod
    def GetUnconvertedSampleCount(dataDir: str) -> int: ...
    def CancelConversion(self) -> None: ...
    @staticmethod
    def IsSampleDataAcquisitionCompleted(sampleDir: str) -> bool: ...
    def Convert(self) -> None: ...

    ConversionFinished: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ConversionFinishedEventHandler
    )  # Event
    ConversionStarting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ConversionStartingEventHandler
    )  # Event
    SampleConversionStarting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.SampleConversionStartingEventHandler
    )  # Event

class InstrumentType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    QQQ: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.InstrumentType
    ) = ...  # static # readonly
    QTOF: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.InstrumentType
    ) = ...  # static # readonly
    SingleQuad: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.InstrumentType
    ) = ...  # static # readonly
    TOF: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.InstrumentType
    ) = ...  # static # readonly

class MRMChromFilter:  # Class
    def __init__(
        self, pset: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom
    ) -> None: ...

    CollisionEnergy: float  # readonly
    CompoundName: str  # readonly
    ExtractionRangeFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSChromFilter
    )  # readonly
    FragmentorVoltage: float  # readonly
    IntegratorName: str  # readonly
    NoiseMultiplier: float  # readonly
    NoiseType: str  # readonly
    PrecursorMz: float  # readonly
    ProductMz: float  # readonly

class MRMDataAccess:  # Class
    INDEX_FILE: str = ...  # static # readonly
    LATEST_VERSION: int = ...  # static # readonly

    @overload
    def GetPolarities(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    ]: ...
    @overload
    def GetPolarities(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    ]: ...
    def GetMZs(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        selectedMZ: float,
    ) -> System.Collections.Generic.List[float]: ...
    def GetScanTypes(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ]: ...
    @staticmethod
    def GetMRMFilePath(sampleDataPath: str) -> str: ...
    def GetMRMTransitions(
        self,
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...
    @staticmethod
    def MRMFileExists(sampleDataPath: str) -> bool: ...
    def GetSelectedMZs(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Collections.Generic.List[float]: ...
    def GetTransitions(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...

class MRMSpecFilter:  # Class
    def __init__(
        self, pset: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum
    ) -> None: ...

    CompoundName: str  # readonly
    ExtractionRangeFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSSpecFilter
    )  # readonly

class MSChromFilter(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ChromFilter
):  # Class
    def __init__(self) -> None: ...

    CollisionEnergyRange: DoubleRange
    FragmentorVoltageRange: DoubleRange
    HasCEFV: bool  # readonly
    MzRange: DoubleRangeCollection
    Polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    ScanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    SelectedMzRange: DoubleRangeCollection
    TIC: bool

    def Validate(self) -> str: ...

class MSDataPoint:  # Class
    def __init__(
        self,
        instrumentType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.InstrumentType,
    ) -> None: ...

    Abundance: float
    CollisionEnergy: float
    CycleNumber: int
    FlightTime: float
    FragmentorVoltage: float
    InstrumentType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.InstrumentType
    )  # readonly
    MixedPolaritiesPresent: bool
    Mz: float
    Polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    RetentionTime: float
    ScanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    SelectedMz: float
    TimeSegmentNumber: int

    def GetScaledMZValue(self, mz: float) -> int: ...

class MSDataTree(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.IMSDataTree,
    System.IDisposable,
    IQuantMSScanInfo,
):  # Class
    def __init__(
        self,
        accessType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.AccessType,
    ) -> None: ...

    AverageScanStep: float  # readonly
    Header: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.DataHeader
    Polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity  # readonly
    ScanTypes: Agilent.MassSpectrometry.DataAnalysis.MSScanType  # readonly

    def Read(self, br: System.IO.BinaryReader) -> None: ...
    def Write(self, bw: System.IO.BinaryWriter) -> None: ...
    def GetPolarities(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    ]: ...
    def AddTICPoint(
        self,
        ticPoint: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def WriteMrmSimData(self, bw: System.IO.BinaryWriter) -> None: ...
    def GetChromData(
        self,
        chromFilter: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSChromFilter,
    ) -> IChromSpecData: ...
    def ReadMrmSimData(self, sampleDataPath: str) -> None: ...
    def GetMRMTransitions(
        self,
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...
    def AddDataPoint(
        self,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def GetMZs(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        selectedMZ: float,
    ) -> System.Collections.Generic.List[float]: ...
    def GetPolarity(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> Agilent.MassSpectrometry.DataAnalysis.IonPolarity: ...
    def GetScanTypes(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ]: ...
    def GetSelectedMZs(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Collections.Generic.List[float]: ...
    def GetSpecData(
        self,
        specFilter: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSSpecFilter,
    ) -> IChromSpecData: ...
    def AddScanRecord(
        self,
        scanRecord: ScanRecord,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def GetScanDeskewParameters(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        selectedMZ: float,
        mzHigh: float,
        skewRate: float,
    ) -> None: ...
    def GetTransitions(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...
    def SubtractDataPoint(
        self,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def Dispose(self) -> None: ...
    def ConvertMrmSimData(
        self,
        sampleDataPath: str,
        dataAccess: QuantDataAccess,
        acqMethod: AcquisitionMethod,
    ) -> None: ...

class MSSpecFilter:  # Class
    def __init__(self) -> None: ...

    AverageSpectrum: bool
    CollisionEnergyRange: DoubleRange
    FragmentorVoltageRange: DoubleRange
    HasCEFV: bool  # readonly
    HasNoiseThreshold: bool  # readonly
    MzRange: DoubleRange
    MzRanges: System.Collections.Generic.List[DoubleRange]
    NeedRtRangeInfo: bool
    NoiseSubtractionThreshold: float
    Polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    RTRange: DoubleRange
    SaturationThreshold: float
    SaturationTrackingMzRanges: System.Collections.Generic.List[DoubleRange]
    ScanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    SelectedMzRange: DoubleRangeCollection

    def Validate(self) -> str: ...

class MainForm(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...
    def CancelConversion(self) -> None: ...

class MzAxis(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.IAxisGrid
):  # Class
    def __init__(self, mzTimes10Range: IntRange) -> None: ...

    MZStep: float  # readonly
    MaxMz: float  # readonly
    MaxMzTimes10: int  # readonly
    MinMz: float  # readonly
    MinMzTimes10: int  # readonly
    PointCount: int  # readonly

    def GetIndexOfNearestPointAbove(self, value_: float) -> int: ...
    def GetPointByIndex(self, index: int) -> float: ...
    def GetIndexOfNearestPointBelow(self, value_: float) -> int: ...
    def GetIndexOfNearestPoint(self, value_: float) -> int: ...

class NonMSChromFilter(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ChromFilter
):  # Class
    def __init__(self) -> None: ...

    DeviceKey: str  # readonly
    DeviceName: str
    OrdinalNumber: int
    ReferenceRange: DoubleRange
    SignalName: str
    SignalRange: DoubleRange
    TotalSignalChrom: bool

    def Validate(self) -> str: ...

class NonMSDataPoint:  # Class
    def __init__(self, deviceType: str, ordinalNumber: int) -> None: ...

    DeviceKey: str  # readonly
    DeviceName: str
    Intensity: float
    OrdinalNumber: int
    RetentionTime: float
    Signal: float
    SignalDescription: str
    SignalName: str

    @staticmethod
    def GetDeviceTypeAndOrdinalNumber(
        deviceKey: str, deviceType: str, ordinalNumber: int
    ) -> None: ...

class NonMSDataTree:  # Class
    def __init__(
        self,
        accessType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.AccessType,
        header: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.DataHeader,
    ) -> None: ...

    AverageScanStep: float  # readonly
    Header: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.DataHeader
    )  # readonly

    def Read(self, br: System.IO.BinaryReader) -> None: ...
    def Write(self, bw: System.IO.BinaryWriter) -> None: ...
    @overload
    def ConvertNonMsDataToIndexedFormat(self, sampleDataPath: str) -> None: ...
    @overload
    def ConvertNonMsDataToIndexedFormat(
        self, deviceReader: DevicesXmlReader
    ) -> None: ...
    def GetDeviceSignalInfo(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.NonMSDataPoint
    ]: ...
    def GetSignalNames(
        self, deviceKey: str
    ) -> System.Collections.Generic.List[str]: ...
    def GetChromData(
        self,
        chromFilter: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.NonMSChromFilter,
    ) -> ChromSpecData: ...
    def AddDataPoint(
        self,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.NonMSDataPoint,
    ) -> None: ...
    def GetSpecData(
        self,
        specFilter: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.NonMSSpecFilter,
    ) -> ChromSpecData: ...
    def AddTWCPoint(
        self,
        twcPoint: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.NonMSDataPoint,
    ) -> None: ...
    def AddChromSegment(
        self,
        devSigInfo: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.NonMSDataPoint,
        xArray: List[float],
        yArray: List[float],
    ) -> None: ...
    def GetSignalDescription(self, deviceKey: str, signalName: str) -> str: ...

class NonMSSpecFilter:  # Class
    def __init__(self) -> None: ...

    DeviceKey: str  # readonly
    DeviceName: str
    OrdinalNumber: int
    RTRange: DoubleRange
    SignalRange: DoubleRange

    def Validate(self) -> str: ...

class ProgressDlg(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MainForm,
        totalNumSamples: int,
    ) -> None: ...

class RTAxis(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.IAxisGrid
):  # Class
    def __init__(
        self,
        cycleNumbers: System.Collections.Generic.List[int],
        retentionTimes: System.Collections.Generic.List[float],
    ) -> None: ...

    CycleNumberRange: IntRange  # readonly
    CycleNumbers: List[int]  # readonly
    FirstCycleNumber: int  # readonly
    PointCount: int  # readonly
    RetentionTimes: List[float]  # readonly

    def GetIndexOfNearestPointAbove(self, rt: float) -> int: ...
    def GetIndexOfCycleNumber(self, cycleNumber: int) -> int: ...
    def GetRetentionTimes(
        self, startScanIndex: int, endScanIndex: int
    ) -> List[float]: ...
    def GetPointByIndex(self, index: int) -> float: ...
    def GetIndexOfNearestPoint(self, rt: float) -> int: ...
    def InterpolateRetentionTime(self, interpolatedX: float) -> float: ...
    def GetCycleNumberByIndex(self, index: int) -> int: ...
    def GetIndexOfNearestPointBelow(self, rt: float) -> int: ...

class SampleConversionStartingEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ConversionEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ConversionEventArgs,
    ) -> None: ...

class ScanConditions:  # Class
    def __init__(self) -> None: ...

    CollisionEnergy: float
    FragmentorVoltage: float
    Polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    ScanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    SelectedMz: float

    def Equals(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ScanConditions,
    ) -> bool: ...

class ScanSpace:  # Class
    def __init__(
        self,
        scanConditions: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ScanConditions,
        rtAxis: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.RTAxis,
        mzAxis: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MzAxis,
        abundances: List[List[int]],
    ) -> None: ...

    NPointsPerSlice: int  # readonly
    NSlices: int  # readonly
    RTAxis: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.RTAxis
    )  # readonly
    ScanAxis: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MzAxis
    )  # readonly
    ScanConditions: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.ScanConditions
    )  # readonly

    def GetMzSlice(self, sliceIndex: int) -> List[int]: ...

class TOFDataTree(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.IMSDataTree,
    System.IDisposable,
    IQuantMSScanInfo,
):  # Class
    def __init__(
        self,
        sampleDataPath: str,
        accessType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.AccessType,
    ) -> None: ...

    AccessType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.AccessType
    )  # readonly
    AverageScanStep: float  # readonly
    Header: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.DataHeader
    Polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity  # readonly
    ScanTypes: Agilent.MassSpectrometry.DataAnalysis.MSScanType  # readonly

    def Read(self, br: System.IO.BinaryReader) -> None: ...
    def Write(self, bw: System.IO.BinaryWriter) -> None: ...
    def GetPolarities(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    ]: ...
    def AddTICPoint(
        self,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def GetChromData(
        self,
        chromFilter: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSChromFilter,
    ) -> IChromSpecData: ...
    def GetMRMTransitions(
        self,
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...
    def AddDataPoint(
        self,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def GetMZs(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        selectedMZ: float,
    ) -> System.Collections.Generic.List[float]: ...
    def GetPolarity(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> Agilent.MassSpectrometry.DataAnalysis.IonPolarity: ...
    def GetScanTypes(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ]: ...
    def GetSelectedMZs(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Collections.Generic.List[float]: ...
    def GetSpecData(
        self,
        specFilter: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSSpecFilter,
    ) -> IChromSpecData: ...
    def AddScanRecord(
        self,
        scanRecord: ScanRecord,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...
    def ConvertScanData(self, scanData: MSScanData, sampleDataPath: str) -> None: ...
    def GetScanDeskewParameters(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        selectedMZ: float,
        mzHigh: float,
        skewRate: float,
    ) -> None: ...
    def GetTransitions(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...
    def Dispose(self) -> None: ...
    def SubtractDataPoint(
        self,
        dataPt: Agilent.MassSpectrometry.DataAnalysis.Quantitative.IndexedData.MSDataPoint,
    ) -> None: ...

class TOFSpectrum(IChromSpecData):  # Class
    ContributingScanLineCount: int  # readonly
    Count: int  # readonly
    HasData: bool  # readonly
    HasGaps: bool  # readonly
    NScanLinesForSpectrum: int  # readonly
    RtRanges: System.Collections.Generic.List[DoubleRange]  # readonly
    XArray: List[float]  # readonly
    YArray: List[float]  # readonly

    def Sort(self) -> None: ...
