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
    MFE,
    MFE2005,
    MS,
    AGaugeApp,
    Agilent,
    AgilentErrorReporter,
    AGTPICSYSSERVICESLib,
    AGTPICWORKLISTLib,
    BasicTypes,
    Biochemistry,
    CommonAlgorithms,
    ComponentAce,
    CompositionCalculatorEngine,
    CompositionDB,
    CompoundFilters,
    CorrelationNormalizationEngine3,
    DataFitX3,
    Definitions,
    Dennany,
    GenieIntegrator,
    Infragistics,
    Ionic,
    IronPython,
    IronRuby,
    IsotopePatternCalculator,
    IWshRuntimeLibrary,
    Mathematics,
    Mfe,
    MhdFile,
    Microsoft,
    OpenLABTranslator,
    Org,
    PdfSharp,
    PerCederberg,
    PersistanceFiles,
    Storer,
    System,
    Util,
    XamlGeneratedNamespace,
    Xceed,
    com,
    iTextSharp,
    log4net,
    vbAccelerator,
)

# Stubs for namespace: <global>

class CompressWrapper(System.IDisposable):  # Class
    @overload
    def __init__(self, deviceType: int) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def SetDeviceType(self, deviceType: int) -> None: ...
    def Dispose(self) -> None: ...
    @overload
    def DecompressData(
        self,
        pRecordInfo: ScanRecordInfo,
        CompressionType: int,
        inOutCompressedBuff: List[int],
    ) -> None: ...
    @overload
    def DecompressData(
        self,
        pRecordInfo: ScanRecordInfo,
        CompressionType: int,
        inCompressedBuff: List[int],
        outDecompressedBuff: List[int],
    ) -> None: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class DotfuscatorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, a: str, c: int) -> None: ...

    A: str  # readonly
    C: int  # readonly

    def a(self) -> str: ...
    def c(self) -> int: ...

class PeakAdapter(System.IDisposable):  # Class
    def __init__(
        self,
        startIndex: int,
        apexIndex: int,
        endIndex: int,
        startY: float,
        apexY: float,
        endY: float,
        height: float,
        centerX: float,
        width: float,
        area: float,
        suspect: int,
    ) -> None: ...

    ApexIndex: int
    ApexY: float
    Area: float
    CenterX: float
    EndIndex: int
    EndY: float
    Height: float
    StartIndex: int
    StartY: float
    Suspect: int
    Width: float

    def Dispose(self) -> None: ...

class PeakFinderAdapter(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def SetParameters(self, heightRejectAbs: float, saturationLevel: float) -> None: ...
    def Dispose(self) -> None: ...
    def FindPeaks(self, spectrum: List[float]) -> List[PeakAdapter]: ...

class ScanRecordInfo(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    m_ActualsOffset: int
    m_BpcAbundance: float
    m_BpcMZ: float
    m_CollisionEnergy: float
    m_DD_ParamMz_1: float
    m_DD_ScanID: int
    m_Fragmentor: float
    m_IonMode: int
    m_IonPolarity: int
    m_MSLevel: int
    m_MSScanType: int
    m_MZOfInterest: float
    m_MassCalOffset: int
    m_MethodID: int
    m_RetentionTime: float
    m_SamplingPeriod: float
    m_ScanID: int
    m_TIC: float
    m_TimeSegmentID: int
    m_pSpectrumParams: SpecParams

    def Dispose(self) -> None: ...
    def GetUnmanagedScanRecordInfo(self, scanrec: System.IntPtr) -> bool: ...

class SharedWorklistStrings:  # Class
    def __init__(self) -> None: ...

    AcqMethod: str = ...  # static # readonly
    AcqTime: str = ...  # static # readonly
    AutoIncr: str = ...  # static # readonly
    BalanceType: str = ...  # static # readonly
    Barcode: str = ...  # static # readonly
    CalibLevelName: str = ...  # static # readonly
    CombinedReportOutputFile: str = ...  # static # readonly
    DAMethod: str = ...  # static # readonly
    DataFileName: str = ...  # static # readonly
    Description: str = ...  # static # readonly
    DilutionFactor: str = ...  # static # readonly
    EquilibrationTime: str = ...  # static # readonly
    ExpectedBarcode: str = ...  # static # readonly
    ISTDDilution: str = ...  # static # readonly
    InjectionVolume: str = ...  # static # readonly
    InstrumentName: str = ...  # static # readonly
    MethodExecutionType: str = ...  # static # readonly
    MethodNoOverride: str = ...  # static # readonly
    OperatorName: str = ...  # static # readonly
    OverWriteDataFile: str = ...  # static # readonly
    PlateCode: str = ...  # static # readonly
    PlatePosition: str = ...  # static # readonly
    RackCode: str = ...  # static # readonly
    RackPosition: str = ...  # static # readonly
    ReadyTimeOut: str = ...  # static # readonly
    Reserved1: str = ...  # static # readonly
    Reserved2: str = ...  # static # readonly
    Reserved3: str = ...  # static # readonly
    Reserved4: str = ...  # static # readonly
    Reserved5: str = ...  # static # readonly
    Reserved6: str = ...  # static # readonly
    RunAcqAndDAMethod: str = ...  # static # readonly
    RunAcqOnlyMethod: str = ...  # static # readonly
    RunCompletedFlag: str = ...  # static # readonly
    RunDAOnlyMethod: str = ...  # static # readonly
    RunType: str = ...  # static # readonly
    RuntypeExternalRun: str = ...  # static # readonly
    RuntypeLCOnlyRun: str = ...  # static # readonly
    RuntypeManualRun: str = ...  # static # readonly
    RuntypeStandardRun: str = ...  # static # readonly
    SampleAmount: str = ...  # static # readonly
    SampleID: str = ...  # static # readonly
    SampleLockedRunMode: str = ...  # static # readonly
    SampleName: str = ...  # static # readonly
    SamplePosition: str = ...  # static # readonly
    SampleType: str = ...  # static # readonly
    SamplingDateTime: str = ...  # static # readonly
    TotalSampleAmount: str = ...  # static # readonly
    UserDefined: str = ...  # static # readonly
    UserName: str = ...  # static # readonly
    WeightPerVolume: str = ...  # static # readonly
    strBlank: str = ...  # static # readonly
    strCalibration: str = ...  # static # readonly
    strConCal: str = ...  # static # readonly
    strDoubleBlank: str = ...  # static # readonly
    strMatrix: str = ...  # static # readonly
    strMatrixBlank: str = ...  # static # readonly
    strMatrixDup: str = ...  # static # readonly
    strQC: str = ...  # static # readonly
    strResponseCheck: str = ...  # static # readonly
    strSample: str = ...  # static # readonly
    strTuneCheck: str = ...  # static # readonly

class SharedWorklistStrings:  # Class
    def __init__(self) -> None: ...

    AcqMethod: str = ...  # static # readonly
    AcqTime: str = ...  # static # readonly
    BalanceType: str = ...  # static # readonly
    Barcode: str = ...  # static # readonly
    CalibLevelName: str = ...  # static # readonly
    CombinedReportOutputFile: str = ...  # static # readonly
    DAMethod: str = ...  # static # readonly
    DataFileName: str = ...  # static # readonly
    Description: str = ...  # static # readonly
    DilutionFactor: str = ...  # static # readonly
    EquilibrationTime: str = ...  # static # readonly
    ExpectedBarcode: str = ...  # static # readonly
    ISTDDilution: str = ...  # static # readonly
    InjectionVolume: str = ...  # static # readonly
    InstrumentName: str = ...  # static # readonly
    MethodExecutionType: str = ...  # static # readonly
    OperatorName: str = ...  # static # readonly
    PlateCode: str = ...  # static # readonly
    PlatePosition: str = ...  # static # readonly
    RackCode: str = ...  # static # readonly
    RackPosition: str = ...  # static # readonly
    Reserved1: str = ...  # static # readonly
    Reserved2: str = ...  # static # readonly
    Reserved3: str = ...  # static # readonly
    Reserved4: str = ...  # static # readonly
    Reserved5: str = ...  # static # readonly
    Reserved6: str = ...  # static # readonly
    RunCompletedFlag: str = ...  # static # readonly
    SampleAmount: str = ...  # static # readonly
    SampleID: str = ...  # static # readonly
    SampleLockedRunMode: str = ...  # static # readonly
    SampleName: str = ...  # static # readonly
    SamplePosition: str = ...  # static # readonly
    SampleType: str = ...  # static # readonly
    SamplingDateTime: str = ...  # static # readonly
    TotalSampleAmount: str = ...  # static # readonly
    UserDefined: str = ...  # static # readonly
    UserName: str = ...  # static # readonly
    WeightPerVolume: str = ...  # static # readonly
    strBlank: str = ...  # static # readonly
    strCalibration: str = ...  # static # readonly
    strConCal: str = ...  # static # readonly
    strDoubleBlank: str = ...  # static # readonly
    strMatrix: str = ...  # static # readonly
    strMatrixBlank: str = ...  # static # readonly
    strMatrixDup: str = ...  # static # readonly
    strQC: str = ...  # static # readonly
    strResponseCheck: str = ...  # static # readonly
    strSample: str = ...  # static # readonly
    strTuneCheck: str = ...  # static # readonly

class SpecParams(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    m_ByteCount: int
    m_MinX: float
    m_Offset: int
    m_PointCount: int
    m_UncompressedByteCount: int

    def Dispose(self) -> None: ...
