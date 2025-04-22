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

# Stubs for namespace: Agilent.OpenLab.RawData

class AcmdDoc:  # Class
    @overload
    @staticmethod
    def Save(
        metadata: Agilent.OpenLab.RawData.RawMetadata, stream: System.IO.Stream
    ) -> None: ...
    @overload
    @staticmethod
    def Save(metadata: Agilent.OpenLab.RawData.RawMetadata, filename: str) -> None: ...

class BinReader(System.IDisposable, System.IO.BinaryReader):  # Class
    def __init__(self, stream: System.IO.Stream) -> None: ...
    def ReadBigEndianInt32(self) -> int: ...
    def ReadRawBytes(self, length: int) -> List[int]: ...
    def ReadBigEndianInt16(self) -> int: ...
    def ReadBigEndianDouble(self) -> float: ...
    @overload
    def ReadLittleEndianDoubles(
        self, values: List[float], numberOfDataPoints: int
    ) -> None: ...
    @overload
    def ReadLittleEndianDoubles(
        self, values: List[float], numberOfDataPoints: int, scalingFactor: float
    ) -> None: ...
    @overload
    def ReadLittleEndianDoubles(
        self, xvalues: List[float], yvalues: List[float], numberOfDataPoints: int
    ) -> None: ...
    def ReadLittleEndianInt16(self) -> int: ...
    def ReadLittleEndianDouble(self) -> float: ...
    def ReadBigEndianFloat(self) -> float: ...
    def ReadString(self, length: int) -> str: ...
    def ReadLittleEndianInt32(self) -> int: ...

class BinWriter(System.IDisposable, System.IO.BinaryWriter):  # Class
    def __init__(self, stream: System.IO.Stream) -> None: ...
    def WriteBigEndianFloat(self, value_: float) -> None: ...
    def WriteLittleEndianInt16(self, value_: int) -> None: ...
    def WriteString(self, value_: str, lenOfField: int) -> None: ...
    def WriteBigEndianInt32(self, value_: int) -> None: ...
    def WriteFiller(self, len: int) -> None: ...
    def WriteBigEndianInt16(self, value_: int) -> None: ...
    def WriteBigEndianDouble(self, value_: float) -> None: ...
    def WriteLittleEndianInt32(self, value_: int) -> None: ...
    def WriteLittleEndianDouble(self, value_: float) -> None: ...

class ContentTypeDx:  # Class
    ContentAcquisitionMethod: str = ...  # static # readonly
    ContentInstrumentConfiguration: str = ...  # static # readonly
    DefaultMassCalXml: str = ...  # static # readonly
    GenericPart: str = ...  # static # readonly
    GenericResults: str = ...  # static # readonly
    InstrumentTrace179: str = ...  # static # readonly
    Metadata: str = ...  # static # readonly
    MsContentsXml: str = ...  # static # readonly
    MsData: str = ...  # static # readonly
    MsDevicesXml: str = ...  # static # readonly
    MsScanXsd: str = ...  # static # readonly
    MsTimeSegmentXml: str = ...  # static # readonly
    RelationshipAcquisitionMethod: str = ...  # static # readonly
    RelationshipDefaultMassCalXml: str = ...  # static # readonly
    RelationshipGenericParts: str = ...  # static # readonly
    RelationshipMetadata: str = ...  # static # readonly
    RelationshipMsContentsXml: str = ...  # static # readonly
    RelationshipMsDevicesXml: str = ...  # static # readonly
    RelationshipMsScanXsd: str = ...  # static # readonly
    RelationshipMsTimeSegmentXml: str = ...  # static # readonly
    RelationshipSpectraDirectory: str = ...  # static # readonly
    Signal179: str = ...  # static # readonly
    SignalNonEquidistant179: str = ...  # static # readonly
    Spectra131: str = ...  # static # readonly
    SpectraDirectory131: str = ...  # static # readonly

class HeaderData:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, location: str, sequenceLine: int, replicate: int) -> None: ...

    StandardFileHeader2D: Agilent.OpenLab.RawData.StandardFileHeader2D

class IRawData(object):  # Interface
    Description: str  # readonly
    TraceId: str  # readonly

class IRawData2DNonEquidistantSignal(Agilent.OpenLab.RawData.IRawData):  # Interface
    IsIntegrable: bool  # readonly
    Slope: float  # readonly
    XUnits: Agilent.OpenLab.RawData.XUnitType  # readonly
    XValues: List[float]  # readonly
    YUnits: str  # readonly
    YValues: List[float]  # readonly

class IRawData2DSignal(Agilent.OpenLab.RawData.IRawData):  # Interface
    EndTime: float
    ExpectedEndTime: float
    IsIntegrable: bool  # readonly
    Slope: float  # readonly
    StartTime: float  # readonly
    Step: float
    XUnits: Agilent.OpenLab.RawData.XUnitType  # readonly
    YUnits: str  # readonly
    YValues: List[float]  # readonly

class IRawDataGenericResults(Agilent.OpenLab.RawData.IRawData):  # Interface
    Content: List[int]  # readonly

class IRawDataInstrumentTrace(Agilent.OpenLab.RawData.IRawData):  # Interface
    Slope: float  # readonly
    XUnits: Agilent.OpenLab.RawData.XUnitType  # readonly
    XValues: List[float]  # readonly
    YUnits: str  # readonly
    YValues: List[float]  # readonly

class IRawDataSpectra(Agilent.OpenLab.RawData.IRawData):  # Interface
    DetectorType: Agilent.OpenLab.RawData.SpectraDetectorType  # readonly
    ScaleFactor: float  # readonly
    Spectra: System.Collections.Generic.List[
        Agilent.OpenLab.RawData.LCSpectrum
    ]  # readonly
    TimeUnit: Agilent.OpenLab.RawData.TimeUnitType  # readonly
    XUnits: Agilent.OpenLab.RawData.XUnitType  # readonly
    YUnits: str  # readonly

class IWriter2DCreateInfo(Agilent.OpenLab.RawData.IWriterCreateInfo):  # Interface
    ChannelName: str
    DeviceName: str
    DeviceNumber: str
    IsIntegrable: bool
    SampleFrequency: float
    SignalDescription: str
    SignalUnits: str
    Slope: float

class IWriter3DCreateInfo(Agilent.OpenLab.RawData.IWriterCreateInfo):  # Interface
    DeviceName: str
    DeviceNumber: str
    ScaleFactor: float
    SpectraDescription: str
    Units: str

class IWriterAdd2DDataInfo(Agilent.OpenLab.RawData.IWriterAddDataInfo):  # Interface
    EndTime: float
    StartTime: Optional[float]
    YValues: List[float]

class IWriterAdd3DDataInfo(Agilent.OpenLab.RawData.IWriterAddDataInfo):  # Interface
    DetectorType: Agilent.OpenLab.RawData.SpectraDetectorType
    SpectrumRecords: System.Collections.Generic.List[Agilent.OpenLab.RawData.LCSpectrum]

class IWriterAddDataInfo(object):  # Interface
    Description: str
    TraceId: str

class IWriterAddMsDataInfo(Agilent.OpenLab.RawData.IWriterAddDataInfo):  # Interface
    IsEndOfData: bool
    ScansData: List[Agilent.OpenLab.RawData.MassSpecScan]

class IWriterCreateInfo(object):  # Interface
    Description: str
    TraceId: str

class IWriterMsCreateInfo(Agilent.OpenLab.RawData.IWriterCreateInfo):  # Interface
    Contents: Agilent.MassSpectrometry.DataAnalysis.Contents
    Device: Agilent.MassSpectrometry.DataAnalysis.Device
    MsInitializationInfo: str
    MsMassCalBinStream: System.IO.Stream
    MsPeakBinStream: System.IO.Stream
    MsProfileBinStream: System.IO.Stream
    MsScanBinStream: System.IO.Stream

class InjectionAcquisitionMetadata:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        location: str,
        sequenceLine: int,
        replicate: int,
        sampleName: str,
        runOperator: str,
        barcode: str,
        runDateTime: System.DateTime,
        injectionSource: str,
        injectionVolume: float,
        injectionVolumeUnits: str,
        acquisitionMethod: str,
    ) -> None: ...

    AcquisitionMethod: str
    Barcode: str
    InjectionSource: str
    InjectionVolume: float
    InjectionVolumeUnits: str
    Location: str
    Replicate: int
    RunDateTime: System.DateTime
    RunOperator: str
    SampleName: str
    SequenceLine: int

class LCDadSpectrum(Agilent.OpenLab.RawData.LCSpectrum):  # Class
    def __init__(self) -> None: ...

    ExposureTime: float

class LCFldSpectrum(Agilent.OpenLab.RawData.LCSpectrum):  # Class
    def __init__(self) -> None: ...

    ComplementWavelength: float
    ScanSpeed: float

class LCSpectrum:  # Class
    DataPoints: List[float]
    RetentionTime: float
    SpecAttribute: Agilent.OpenLab.RawData.SpectrumAttribute
    WavelengthFrom: float
    WavelengthStep: float
    WavelengthTo: float

class MassSpecScan:  # Class
    def __init__(
        self, msScanDataStreams: List[Agilent.OpenLab.RawData.MassSpecScanData]
    ) -> None: ...

    MassSpecScanDataStreams: List[Agilent.OpenLab.RawData.MassSpecScanData]

class MassSpecScanData:  # Class
    def __init__(self, id: str, dataInfo: str, data: List[int]) -> None: ...

    Data: List[int]
    DataInfo: str
    Id: str

class PackageBase:  # Class
    def Close(self) -> None: ...
    def LoadMetadata(self) -> Agilent.OpenLab.RawData.RawMetadata: ...

class PackageReader(Agilent.OpenLab.RawData.PackageBase):  # Class
    def __init__(self, fileStream: System.IO.Stream) -> None: ...

class PackageWriter(Agilent.OpenLab.RawData.PackageBase):  # Class
    def __init__(self, fileStream: System.IO.Stream) -> None: ...

class RawData2DSignal(
    Agilent.OpenLab.RawData.IRawData2DSignal, Agilent.OpenLab.RawData.IRawData
):  # Class
    def __init__(self) -> None: ...

    Description: str
    EndTime: float
    ExpectedEndTime: float
    IsIntegrable: bool
    Slope: float
    StartTime: float
    Step: float
    TraceId: str
    XUnits: Agilent.OpenLab.RawData.XUnitType
    YUnits: str
    YValues: List[float]

class RawDataGenericResults(
    Agilent.OpenLab.RawData.IRawData, Agilent.OpenLab.RawData.IRawDataGenericResults
):  # Class
    def __init__(self) -> None: ...

    Content: List[int]
    Description: str
    TraceId: str

class RawDataInstrumentTrace(
    Agilent.OpenLab.RawData.IRawDataInstrumentTrace, Agilent.OpenLab.RawData.IRawData
):  # Class
    def __init__(self) -> None: ...

    Description: str
    Slope: float
    TraceId: str
    XUnits: Agilent.OpenLab.RawData.XUnitType
    XValues: List[float]
    YUnits: str
    YValues: List[float]

class RawDataLegacyMetadata:  # Class
    def __init__(self) -> None: ...

    AcquisitionDateTime: str
    AcquisitionMethodName: str
    Barcode: str
    Operator: str
    Replicate: int
    SampleName: str
    SeqIndex: int
    SignalDescription: str
    Vial: str

class RawDataNonEquidistantSignal(
    Agilent.OpenLab.RawData.IRawData2DNonEquidistantSignal,
    Agilent.OpenLab.RawData.IRawData,
):  # Class
    def __init__(self) -> None: ...

    Description: str
    IsIntegrable: bool
    Slope: float
    TraceId: str
    XUnits: Agilent.OpenLab.RawData.XUnitType
    XValues: List[float]
    YUnits: str
    YValues: List[float]

class RawDataReader(System.IDisposable):  # Class
    def __init__(self, fileStream: System.IO.Stream) -> None: ...

    InjectionAcquisitionMetadata: (
        Agilent.OpenLab.RawData.InjectionAcquisitionMetadata
    )  # readonly
    Signals: System.Collections.Generic.List[
        Agilent.OpenLab.RawData.SignalMetadata
    ]  # readonly

    @staticmethod
    def ReadLegacyMetadata(
        fileStream: System.IO.Stream,
    ) -> Agilent.OpenLab.RawData.RawDataLegacyMetadata: ...
    def ReadInstrumentConfiguration(self) -> System.IO.Stream: ...
    def ReadSignalMetadata(
        self, traceId: str
    ) -> Agilent.OpenLab.RawData.SignalMetadata: ...
    def Dispose(self) -> None: ...
    def ReadSignal(self, traceId: str) -> Agilent.OpenLab.RawData.IRawData: ...
    def ReadAcquisitionMethod(self) -> System.IO.Stream: ...

class RawDataSpectra(
    Agilent.OpenLab.RawData.IRawDataSpectra, Agilent.OpenLab.RawData.IRawData
):  # Class
    def __init__(self) -> None: ...

    Description: str
    DetectorType: Agilent.OpenLab.RawData.SpectraDetectorType
    ScaleFactor: float
    Spectra: System.Collections.Generic.List[Agilent.OpenLab.RawData.LCSpectrum]
    TimeUnit: Agilent.OpenLab.RawData.TimeUnitType
    TraceId: str
    XUnits: Agilent.OpenLab.RawData.XUnitType
    YUnits: str

class RawDataWriter(System.IDisposable):  # Class
    @overload
    def __init__(
        self,
        fileStream: System.IO.Stream,
        injectionAcquisitionMetadata: Agilent.OpenLab.RawData.InjectionAcquisitionMetadata,
    ) -> None: ...
    @overload
    def __init__(self, fileStream: System.IO.Stream) -> None: ...
    def AddData(
        self, addDataInfo: Agilent.OpenLab.RawData.IWriterAddDataInfo
    ) -> bool: ...
    def AddSpectraFile(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        signalDescription: str,
        scaleFactor: float,
        units: str,
        detectorType: Agilent.OpenLab.RawData.SpectraDetectorType,
        spectrumRecords: System.Collections.Generic.List[
            Agilent.OpenLab.RawData.LCSpectrum
        ],
    ) -> bool: ...
    def CreateSignal(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        channelName: str,
        sampleFrequency: float,
        signalUnits: str,
        signalDescription: str,
        slope: float,
        isIntegrable: bool,
    ) -> bool: ...
    def Add2DSignal(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        channelName: str,
        startTime: float,
        endTime: float,
        sampleFrequency: float,
        signalUnits: str,
        signalDescription: str,
        slope: float,
        isIntegrable: bool,
        valuesY: List[float],
    ) -> bool: ...
    def Dispose(self) -> None: ...
    def AddTo2DSignal(
        self,
        traceId: str,
        startTime: Optional[float],
        endTime: float,
        valuesY: List[float],
    ) -> bool: ...
    def AddToInstrumentTrace(
        self, traceId: str, valuesX: List[float], valuesY: List[float]
    ) -> bool: ...
    def CreateFile(
        self,
        injectionAcquisitionMetadata: Agilent.OpenLab.RawData.InjectionAcquisitionMetadata,
    ) -> None: ...
    def AddAcquisitionMethod(self, methodStream: System.IO.Stream) -> bool: ...
    def AppendToMsExternalElementPaths(
        self, elementPaths: str, traceId: str
    ) -> None: ...
    def CreateNonEquidistantSignal(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        channelName: str,
        signalUnits: str,
        signalDescription: str,
        slope: float,
        isIntegrable: bool,
    ) -> bool: ...
    def CreateInstrumentTrace(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        channelName: str,
        axisTitleY: str,
        description: str,
        axisMultiplierY: float,
    ) -> bool: ...
    def CreateData(
        self, createDataInfo: Agilent.OpenLab.RawData.IWriterCreateInfo
    ) -> bool: ...
    def AddGenericResults(
        self,
        traceId: str,
        moduleId: str,
        serialNumber: str,
        dataChannelId: str,
        dataChannelName: str,
        dataChannelDescription: str,
        dataContentId: str,
        dataContentSequenceNumber: str,
        dataContentType: str,
        content: List[int],
    ) -> bool: ...
    def Add2DNonEquidistantSignal(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        channelName: str,
        signalUnits: str,
        signalDescription: str,
        slope: float,
        isIntegrable: bool,
        valuesX: List[float],
        valuesY: List[float],
    ) -> bool: ...
    def AddSpectraRecords(
        self,
        traceId: str,
        detectorType: Agilent.OpenLab.RawData.SpectraDetectorType,
        spectrumRecords: System.Collections.Generic.List[
            Agilent.OpenLab.RawData.LCSpectrum
        ],
    ) -> bool: ...
    def AddInstrumentConfiguration(
        self, configurationStream: System.IO.Stream
    ) -> bool: ...
    def CloseFile(self) -> None: ...
    def AddInstrumentTrace(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        channelName: str,
        axisTitleY: str,
        description: str,
        axisMultiplierY: float,
        valuesX: List[float],
        valuesY: List[float],
    ) -> bool: ...
    def CreateSpectra(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        spectraDescription: str,
        scaleFactor: float,
        units: str,
    ) -> bool: ...
    def AddToNonEquidistantSignal(
        self, traceId: str, valuesX: List[float], valuesY: List[float]
    ) -> bool: ...

class RawMetadata:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        injectionAcquisitionMetadata: Agilent.OpenLab.RawData.InjectionAcquisitionMetadata,
    ) -> None: ...

    InjectionAcquisitionMetadata: Agilent.OpenLab.RawData.InjectionAcquisitionMetadata
    Signals: Dict[str, Agilent.OpenLab.RawData.SignalMetadata]  # readonly

    def ExtendSpectra(
        self,
        traceId: str,
        records: int,
        detectorType: Agilent.OpenLab.RawData.SpectraDetectorType,
    ) -> None: ...
    @staticmethod
    def Load(stream: System.IO.Stream) -> Agilent.OpenLab.RawData.RawMetadata: ...
    def AddSignal(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        channelName: str,
        signalDescription: str,
        startTime: float,
        endTime: float,
        minSignal: float,
        maxSignal: float,
        slope: float,
        units: str,
        isIntegrable: bool,
        numberOfValues: int,
    ) -> None: ...
    def ExtendInstrumentTrace(
        self,
        traceId: str,
        startTime: Optional[float],
        endTime: float,
        numberOfValues: int,
    ) -> None: ...
    def AddNonEquidistantSignal(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        channelName: str,
        signalDescription: str,
        slope: float,
        units: str,
        isIntegrable: bool,
        numberOfValues: int = ...,
    ) -> None: ...
    def AddSpectra(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        spectraDescription: str,
        detectorType: Agilent.OpenLab.RawData.SpectraDetectorType,
        scaleFactor: float,
        units: str,
        records: int,
    ) -> None: ...
    def ExtendNonEquidistantSignal(
        self,
        traceId: str,
        startTime: Optional[float],
        endTime: float,
        numberOfValues: int,
    ) -> None: ...
    def AddGenericResults(
        self,
        traceId: str,
        moduleId: str,
        serialNumber: str,
        dataChannelId: str,
        dataChannelName: str,
        dataChannelDescription: str,
        dataContentId: str,
        dataContentSequenceNumber: str,
        dataContentType: str,
    ) -> None: ...
    def AddInstrumentTrace(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        channelName: str,
        signalDescription: str,
        slope: float,
        units: str,
        numberOfValues: int = ...,
    ) -> None: ...
    def ExtendSignal(
        self,
        traceId: str,
        startTime: Optional[float],
        endTime: float,
        minSignal: float,
        maxSignal: float,
        numberOfValues: int,
    ) -> None: ...
    def AddMsData(
        self,
        name: str,
        description: str,
        startTime: float,
        endTime: float,
        externalElementPaths: str,
    ) -> None: ...
    @overload
    def GetSignalMetadata(
        self, traceId: str
    ) -> Agilent.OpenLab.RawData.SignalMetadata: ...
    @overload
    def GetSignalMetadata(
        self, typeOfSignal: Agilent.OpenLab.RawData.SignalType
    ) -> Agilent.OpenLab.RawData.SignalMetadata: ...
    def Save(self, stream: System.IO.Stream) -> None: ...

class SignalData(Agilent.OpenLab.RawData.HeaderData):  # Class
    def __init__(self) -> None: ...

    SignalInfo: Agilent.OpenLab.RawData.SignalInformation2D
    UnicodeFileHeader2D: Agilent.OpenLab.RawData.UnicodeFileHeader2D
    XValues: List[float]
    YValues: List[float]

    def Write2DSignal(self, binWriter: Agilent.OpenLab.RawData.BinWriter) -> bool: ...
    def Extend2DSignal(self, binWriter: Agilent.OpenLab.RawData.BinWriter) -> bool: ...
    @staticmethod
    def ReadLegacyMetadata(
        binReader: Agilent.OpenLab.RawData.BinReader,
    ) -> Agilent.OpenLab.RawData.RawDataLegacyMetadata: ...
    @staticmethod
    def Read2DSignal(
        binReader: Agilent.OpenLab.RawData.BinReader, numberOfValues: int
    ) -> Agilent.OpenLab.RawData.SignalData: ...

class SignalInformation2D:  # Class
    def __init__(self) -> None: ...

    BunchPower1: int
    BunchPower2: int
    Detector1: int
    Detector2: int
    HeaderSize: int
    HeaderVersion: int
    Intercept: float
    Max1: float
    Max2: int
    Method1: int
    Method2: int
    Min1: float
    Min2: int
    PeakWidth1: float
    PeakWidth2: float
    Present1: int
    Present2: int
    SignalDataType: int
    SignalDescription: str
    Slope: float
    Units: str
    Version1: int
    Version2: int
    WordAlign1: int
    WordAlign2: int
    Zero1: float
    Zero2: int

class SignalMetadata:  # Class
    def __init__(self) -> None: ...

    ChannelName: str
    DataChannelDescription: str
    DataChannelId: str
    DataChannelName: str
    DataContentId: str
    DataContentSequenceNumber: str
    DataContentType: str
    Description: str
    DetectorType: Agilent.OpenLab.RawData.SpectraDetectorType
    DeviceName: str
    DeviceNumber: str
    EndTime: float
    ExternalElementPaths: str
    IsIntegrable: bool
    Max: float
    Min: float
    NumberOfRecords: int
    NumberOfValues: int
    ScaleFactor: float
    Slope: float
    StartTime: float
    TraceId: str
    TypeOfSignal: Agilent.OpenLab.RawData.SignalType  # readonly
    Units: str

class SignalType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    GenericAnalyticalResults: Agilent.OpenLab.RawData.SignalType = (
        ...
    )  # static # readonly
    InstrumentTrace: Agilent.OpenLab.RawData.SignalType = ...  # static # readonly
    MS: Agilent.OpenLab.RawData.SignalType = ...  # static # readonly
    Signal2D: Agilent.OpenLab.RawData.SignalType = ...  # static # readonly
    SignalNonEquidistant2D: Agilent.OpenLab.RawData.SignalType = (
        ...
    )  # static # readonly
    Spectra3D: Agilent.OpenLab.RawData.SignalType = ...  # static # readonly
    Undefined: Agilent.OpenLab.RawData.SignalType = ...  # static # readonly

class SpectraData(Agilent.OpenLab.RawData.HeaderData):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        location: str,
        sequenceLine: int,
        replicate: int,
        sampleName: str,
        runOperator: str,
        barcode: str,
        runDateTime: System.DateTime,
        acquisitionMethod: str,
        scaleFactor: float,
        units: str,
        detectorType: Agilent.OpenLab.RawData.SpectraDetectorType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        totalRecords: int,
        scaleFactor: float,
        detectorType: Agilent.OpenLab.RawData.SpectraDetectorType,
        newRecords: int,
    ) -> None: ...

    UnicodeFileHeader3D: Agilent.OpenLab.RawData.UnicodeFileHeader3D

class SpectraDetectorType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Dad: Agilent.OpenLab.RawData.SpectraDetectorType = ...  # static # readonly
    Fld: Agilent.OpenLab.RawData.SpectraDetectorType = ...  # static # readonly
    MS: Agilent.OpenLab.RawData.SpectraDetectorType = ...  # static # readonly
    Undefined: Agilent.OpenLab.RawData.SpectraDetectorType = ...  # static # readonly

class SpectrumAttribute(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DadCancellationPeak: Agilent.OpenLab.RawData.SpectrumAttribute = (
        ...
    )  # static # readonly
    DadEndPeak: Agilent.OpenLab.RawData.SpectrumAttribute = ...  # static # readonly
    DadInflectionPointDownslopeFalling: Agilent.OpenLab.RawData.SpectrumAttribute = (
        ...
    )  # static # readonly
    DadInflectionPointDownslopeRising: Agilent.OpenLab.RawData.SpectrumAttribute = (
        ...
    )  # static # readonly
    DadInflectionPointUpslopeFalling: Agilent.OpenLab.RawData.SpectrumAttribute = (
        ...
    )  # static # readonly
    DadInflectionPointUpslopeRising: Agilent.OpenLab.RawData.SpectrumAttribute = (
        ...
    )  # static # readonly
    DadManuallyOrTime: Agilent.OpenLab.RawData.SpectrumAttribute = (
        ...
    )  # static # readonly
    DadPeakAll: Agilent.OpenLab.RawData.SpectrumAttribute = ...  # static # readonly
    DadPeakBegin: Agilent.OpenLab.RawData.SpectrumAttribute = ...  # static # readonly
    DadPeriodically: Agilent.OpenLab.RawData.SpectrumAttribute = (
        ...
    )  # static # readonly
    DadSmallPeakTop: Agilent.OpenLab.RawData.SpectrumAttribute = (
        ...
    )  # static # readonly
    DadTopPeak: Agilent.OpenLab.RawData.SpectrumAttribute = ...  # static # readonly
    DadValley: Agilent.OpenLab.RawData.SpectrumAttribute = ...  # static # readonly
    FldEmissionScan: Agilent.OpenLab.RawData.SpectrumAttribute = (
        ...
    )  # static # readonly
    FldExcitationScan: Agilent.OpenLab.RawData.SpectrumAttribute = (
        ...
    )  # static # readonly
    ForceBaseline: Agilent.OpenLab.RawData.SpectrumAttribute = ...  # static # readonly
    Undefined: Agilent.OpenLab.RawData.SpectrumAttribute = ...  # static # readonly
    Unknown: Agilent.OpenLab.RawData.SpectrumAttribute = ...  # static # readonly

class StandardFileHeader2D:  # Class
    def __init__(self) -> None: ...

    AlsBottle: int
    AlsBottleX: int
    DataOffset: int
    DirEntType: int
    DirOffset: int
    EndTime: float
    ExtraRecords: int
    FileType: int
    FileTypeDefinition: str  # readonly
    MaxSignal: float
    MaxY: float
    MaxZ: int
    MinSignal: float
    MinY: float
    MinZ: int
    Mode: int
    NormOffset: int
    NumRecords: int
    Replicate: int
    RunTableOffset: int
    SeqIndex: int
    StartTime: Optional[float]

class TimeUnitType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Milliseconds: Agilent.OpenLab.RawData.TimeUnitType = ...  # static # readonly
    Seconds: Agilent.OpenLab.RawData.TimeUnitType = ...  # static # readonly
    Undefined: Agilent.OpenLab.RawData.TimeUnitType = ...  # static # readonly

class UnicodeFileHeader2D:  # Class
    def __init__(self) -> None: ...

    Barcode: str
    DateTime: str
    File: str
    FileNum: str
    HeaderSize: int
    HeaderVersion: int
    Inlet: str
    InstModel: str
    MethodFile: str
    Operator: str
    SampleLocation: str
    SampleName: str

class UnicodeFileHeader3D(Agilent.OpenLab.RawData.UnicodeFileHeader2D):  # Class
    def __init__(self) -> None: ...

    Detector: Agilent.OpenLab.RawData.SpectraDetectorType
    MiscInfo: str
    ScaleFactor: float
    Units: str

class Writer2DCreateInfo(
    Agilent.OpenLab.RawData.IWriterCreateInfo,
    Agilent.OpenLab.RawData.IWriter2DCreateInfo,
):  # Class
    @overload
    def __init__(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        channelName: str,
        sampleFrequency: float,
        signalUnits: str,
        signalDescription: str,
        slope: float,
        isIntegrable: bool,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    ChannelName: str
    Description: str
    DeviceName: str
    DeviceNumber: str
    IsIntegrable: bool
    SampleFrequency: float
    SignalDescription: str
    SignalUnits: str
    Slope: float
    TraceId: str

class Writer3DCreateInfo(
    Agilent.OpenLab.RawData.IWriter3DCreateInfo,
    Agilent.OpenLab.RawData.IWriterCreateInfo,
):  # Class
    @overload
    def __init__(
        self,
        traceId: str,
        deviceName: str,
        deviceNumber: str,
        spectraDescription: str,
        scaleFactor: float,
        units: str,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    Description: str
    DeviceName: str
    DeviceNumber: str
    ScaleFactor: float
    SpectraDescription: str
    TraceId: str
    Units: str

class WriterAdd2DDataInfo(
    Agilent.OpenLab.RawData.IWriterAdd2DDataInfo,
    Agilent.OpenLab.RawData.IWriterAddDataInfo,
):  # Class
    @overload
    def __init__(
        self,
        traceId: str,
        startTime: Optional[float],
        endTime: float,
        yValues: List[float],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    Description: str
    EndTime: float
    StartTime: Optional[float]
    TraceId: str
    YValues: List[float]

class WriterAdd3DDataInfo(
    Agilent.OpenLab.RawData.IWriterAddDataInfo,
    Agilent.OpenLab.RawData.IWriterAdd3DDataInfo,
):  # Class
    @overload
    def __init__(
        self,
        traceId: str,
        detectorType: Agilent.OpenLab.RawData.SpectraDetectorType,
        spectrumRecords: System.Collections.Generic.List[
            Agilent.OpenLab.RawData.LCSpectrum
        ],
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    Description: str
    DetectorType: Agilent.OpenLab.RawData.SpectraDetectorType
    SpectrumRecords: System.Collections.Generic.List[Agilent.OpenLab.RawData.LCSpectrum]
    TraceId: str

class WriterAddMsDataInfo(
    Agilent.OpenLab.RawData.IWriterAddMsDataInfo,
    Agilent.OpenLab.RawData.IWriterAddDataInfo,
):  # Class
    def __init__(self) -> None: ...

    Description: str
    IsEndOfData: bool
    ScansData: List[Agilent.OpenLab.RawData.MassSpecScan]
    TraceId: str

class WriterMsCreateInfo(
    Agilent.OpenLab.RawData.IWriterCreateInfo,
    Agilent.OpenLab.RawData.IWriterMsCreateInfo,
):  # Class
    @overload
    def __init__(
        self,
        traceId: str,
        msScanBinStream: System.IO.Stream,
        msPeakBinStream: System.IO.Stream,
        msProfileBinStream: System.IO.Stream,
        msMassCalBinStream: System.IO.Stream,
        msInitializationInfo: str,
        contents: Agilent.MassSpectrometry.DataAnalysis.Contents,
        device: Agilent.MassSpectrometry.DataAnalysis.Device,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    Contents: Agilent.MassSpectrometry.DataAnalysis.Contents
    Description: str
    Device: Agilent.MassSpectrometry.DataAnalysis.Device
    MsInitializationInfo: str
    MsMassCalBinStream: System.IO.Stream
    MsPeakBinStream: System.IO.Stream
    MsProfileBinStream: System.IO.Stream
    MsScanBinStream: System.IO.Stream
    TraceId: str

class XUnitType(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Milliseconds: Agilent.OpenLab.RawData.XUnitType = ...  # static # readonly
    Nanometer: Agilent.OpenLab.RawData.XUnitType = ...  # static # readonly
    Seconds: Agilent.OpenLab.RawData.XUnitType = ...  # static # readonly
    Undefined: Agilent.OpenLab.RawData.XUnitType = ...  # static # readonly
