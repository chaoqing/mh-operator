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

# Discovered Generic TypeVars:
T = TypeVar("T")
TLimit = TypeVar("TLimit")
Tlimit = TypeVar("Tlimit")
from . import CompressionScheme, IImsFrameMethod, IImsFrameRecord, ImsFrameScanRec

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.IMS

class FAResourceKeys:  # Class
    BAD_FILE_TYPE: str  # static
    BAD_FILE_VERSION: str  # static
    CANT_LOCK_FILE: str  # static
    CANT_OPEN_FILE: str  # static
    CANT_OPEN_FRAMEBIN: str  # static
    DRIFT_BIN_OUT_OF_RANGE: str  # static
    FILE_NOT_OPEN: str  # static
    FRAME_NUM_OUT_OF_RANGE: str  # static
    FT_BIN_OUT_OF_RANGE: str  # static
    ILLEGAL_ID_VALUE: str  # static
    INVALID_SCHEMA_FILE_VERSION: str  # static
    NONEXISTENT_BINRANGE: str  # static
    NONEXISTENT_FILE: str  # static
    NONEXISTENT_TOFCAL: str  # static
    NONUNIQUE_ID: str  # static
    NOT_ENOUGH_FORMATS: str  # static
    NOT_IMPLEMENTED: str  # static
    OUTPUT_FILE_NOT_OPEN: str  # static
    RT_NONINCREASING: str  # static
    RT_NONUNIQUE: str  # static
    SCHEMA_VALIDATION_ERROR: str  # static
    UNSUPPORTED_FILE_EXTENSION: str  # static
    UNSUPPORTED_VALUE: str  # static

class FrameData:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, autoAccumulateTfs: bool) -> None: ...
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.DataAnalysis.IMS.FrameData
    ) -> None: ...

    CentroidTfsSpecArrays: System.Collections.Generic.List[System.Array]  # readonly
    FrameBinRecord: IImsFrameRecord  # readonly
    FrameId: int
    FrameMethod: IImsFrameMethod
    FrameScanCount: int  # readonly
    FrameSpecScanRecList: System.Collections.Generic.List[ImsFrameScanRec]  # readonly
    FrameSpecYArrayCompression: CompressionScheme  # readonly
    FrameSpecYArrayList: System.Collections.Generic.List[List[int]]  # readonly
    FrameSpectrumCount: int  # readonly
    IsFinalizedForStorage: bool  # readonly
    ProfileTfsSpecFirstBin: int  # readonly
    ProfileTfsSpecYArray: List[int]  # readonly
    TfsScanRecord: ImsFrameScanRec  # readonly
    TfsSpecYArrayCompression: CompressionScheme  # readonly
    XStartDeltaArray: List[float]  # readonly

    def ValidateForStorage(self, validationMsg: str) -> bool: ...
    def AddTfsProfileScanRecord(
        self,
        FirstBin: int,
        basePeakAbund: float,
        basePeakMz: float,
        imsScanRec: ImsFrameScanRec,
    ) -> None: ...
    @overload
    def FinalizeForStorage(
        self, nextScanId: int, defaultCal: Agilent.MassSpectrometry.ITofCal
    ) -> None: ...
    @overload
    def FinalizeForStorage(
        self,
        makeCentroidTfs: bool,
        nextScanId: int,
        defaultCal: Agilent.MassSpectrometry.ITofCal,
    ) -> None: ...
    def FrameSpecScanRec(self, specIdx: int) -> ImsFrameScanRec: ...
    def FrameSpecYArray(self, specIdx: int) -> List[int]: ...
    @overload
    def AddSpectrum(self, driftBin: int, abundArray: List[int]) -> None: ...
    @overload
    def AddSpectrum(
        self,
        driftBin: int,
        metrics: Agilent.MassSpectrometry.RlzArrayMetrics,
        encodedArray: List[int],
    ) -> None: ...
    @overload
    def AddTfsProfileSpectrum(self, startNs: float, abundArray: List[int]) -> None: ...
    @overload
    def AddTfsProfileSpectrum(
        self,
        basePeakAbund: float,
        basePeakMz: float,
        metrics: Agilent.MassSpectrometry.RlzArrayMetrics,
        encodedArray: List[int],
    ) -> None: ...
    @overload
    def AddTfsCentroidSpectrum(
        self, nsArray: List[float], abundArray: List[float]
    ) -> None: ...
    @overload
    def AddTfsCentroidSpectrum(
        self, nsArray: List[float], abundArray: List[int]
    ) -> None: ...
    def AddSpectrumScanRecord(
        self, driftBin: int, imsScanRec: ImsFrameScanRec
    ) -> None: ...

class IImsMethod(
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterSet,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo,
    Iterable[Any],
):  # Interface
    IsFactoryMethod: bool

    def ReadValues(self, sourcePath: str) -> bool: ...
    def SaveValues(self, destinationPath: str) -> None: ...
    def Clone(self) -> Agilent.MassSpectrometry.DataAnalysis.IMS.IImsMethod: ...

class IMethParameter(
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo
):  # Interface
    HasAllowedValues: bool  # readonly
    HasLimits: bool  # readonly
    IsValid: bool  # readonly
    Units: Agilent.MassSpectrometry.MIDAC.MidacUnits  # readonly
    UsageKey: str
    ValidationMessage: str  # readonly
    Value: Any
    ValueString: str  # readonly

    def Equals(
        self, source: Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter
    ) -> bool: ...
    def Validate(self) -> bool: ...
    def EqualsValue(
        self, source: Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter
    ) -> bool: ...
    def SetValidation(self, validationState: bool, validationMessage: str) -> None: ...
    def EqualsStructure(
        self, source: Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter
    ) -> bool: ...
    def Clone(self) -> Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter: ...

    ValidationSetEvent: (
        Agilent.MassSpectrometry.DataAnalysis.IMS.ImsValidationSetEventHandler
    )  # Event
    ValueChangedEvent: (
        Agilent.MassSpectrometry.DataAnalysis.IMS.ImsValueChangeEventHandler
    )  # Event

class IMethParameterLimited(
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter[T],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo,
):  # Interface
    Limits: Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterLimits[Tlimit]

    def LimitString(self, withType: bool) -> str: ...

class IMethParameterLimits(object):  # Interface
    Maximum: T
    MaximumLimitType: Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterLimitType
    Minimum: T
    MinimumLimitType: Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterLimitType

    def Equals(self, other: Any) -> bool: ...
    def LimitString(self, units: Agilent.MassSpectrometry.MIDAC.MidacUnits) -> str: ...
    def Clone(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterLimits: ...

class IMethParameterRange(
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterLimited[
        Agilent.MassSpectrometry.MIDAC.IRange[T], T
    ],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter[
        Agilent.MassSpectrometry.MIDAC.IRange[T]
    ],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo,
):  # Interface
    ...

class IMethParameterSet(
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo,
    Iterable[Any],
):  # Interface
    Count: int  # readonly
    def __getitem__(
        self, parameterUsageKey: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter: ...
    UsageKeys: System.Collections.Generic.List[str]  # readonly

    def CopyValues(
        self, source: Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterSet
    ) -> None: ...
    def Clone(self) -> Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterSet: ...

class IMethParameterXmlIo(object):  # Interface
    def ReadParameter(self, nodeIter: System.Xml.XPath.XPathNodeIterator) -> None: ...
    def WriteParameter(self, writer: System.Xml.XmlWriter) -> None: ...

class IMethParameter(
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo,
):  # Interface
    AllowedValues: System.Collections.Generic.List[T]
    Value: T

    def Equals(
        self, source: Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter
    ) -> bool: ...
    def Clone(self) -> Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter: ...

class ImsFrameMethConstants:  # Class
    DefMassCalId: str = ...  # static # readonly
    DetectorGainDeltaTo: str = ...  # static # readonly
    DetectorGainMode: str = ...  # static # readonly
    DetectorGainRatio: str = ...  # static # readonly
    FileVersion: str = ...  # static # readonly
    FragEnergy: str = ...  # static # readonly
    FragEnergyMode: str = ...  # static # readonly
    FragEnergySegmentDriftBin: str = ...  # static # readonly
    FragEnergySegmentFragEnergy: str = ...  # static # readonly
    FragEnergySegmentPoint: str = ...  # static # readonly
    FragEnergySegments: str = ...  # static # readonly
    FragOpMode: str = ...  # static # readonly
    FrameDtPeriod: str = ...  # static # readonly
    FrameMethId: str = ...  # static # readonly
    FrameMethod: str = ...  # static # readonly
    FrameMethodGroup: str = ...  # static # readonly
    FrameMsXPeriod: str = ...  # static # readonly
    FrameSpecAbundLimit: str = ...  # static # readonly
    FrameSpecFmtId: str = ...  # static # readonly
    FrameType: str = ...  # static # readonly
    ImsField: str = ...  # static # readonly
    ImsGas: str = ...  # static # readonly
    ImsGateMode: str = ...  # static # readonly
    ImsGateOpenTime: str = ...  # static # readonly
    ImsMuxProcessing: str = ...  # static # readonly
    ImsMuxSequence: str = ...  # static # readonly
    ImsTrapMode: str = ...  # static # readonly
    ImsTrapTime: str = ...  # static # readonly
    IonPolarity: str = ...  # static # readonly
    IonizationMode: str = ...  # static # readonly
    MaxMsBin: str = ...  # static # readonly
    MaxMsPerFrame: str = ...  # static # readonly
    MinMsBin: str = ...  # static # readonly
    NumActuals: str = ...  # static # readonly
    NumTransients: str = ...  # static # readonly
    TfsPeakFmtId: str = ...  # static # readonly
    TfsPeakFmtId_Pre: str = ...  # static # readonly
    TfsProfileFmtId: str = ...  # static # readonly
    TfsProfileFmtId_Pre: str = ...  # static # readonly
    TfsStorageMode: str = ...  # static # readonly
    TfsStorageMode_Pre: str = ...  # static # readonly
    Threshold: str = ...  # static # readonly

class ImsFrameSchemaConstants:  # Class
    ActualsOffset: str = ...  # static # readonly
    CycleNumber: str = ...  # static # readonly
    FirstNonzeroDriftBin: str = ...  # static # readonly
    FragClass: str = ...  # static # readonly
    FragEnergy: str = ...  # static # readonly
    FrameBaseAbund: str = ...  # static # readonly
    FrameBaseDriftBin: str = ...  # static # readonly
    FrameBaseMsBin: str = ...  # static # readonly
    FrameId: str = ...  # static # readonly
    FrameMethodId: str = ...  # static # readonly
    FrameRecordType: str = ...  # static # readonly
    FrameScanTime: str = ...  # static # readonly
    FrameSpecAbundLimit: str = ...  # static # readonly
    FrameTic: str = ...  # static # readonly
    ImsField: str = ...  # static # readonly
    ImsPressure: str = ...  # static # readonly
    ImsTemperature: str = ...  # static # readonly
    ImsTrapTime: str = ...  # static # readonly
    IsolationEndMz: str = ...  # static # readonly
    IsolationMz: str = ...  # static # readonly
    IsolationStartMz: str = ...  # static # readonly
    LastNonzeroDriftBin: str = ...  # static # readonly
    MassCalOffset: str = ...  # static # readonly
    NumTransients: str = ...  # static # readonly
    TimeSegmentId: str = ...  # static # readonly

class ImsMethParameterChangeEventArgs(System.EventArgs):  # Class
    def __init__(self, usageKey: str) -> None: ...

    UsageKey: str  # readonly

class ImsMethodParameterSet(
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter,
    Iterable[Any],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IImsMethod,
    Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterSet,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterSet,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.DataAnalysis.IMS.ImsMethodParameterSet
    ) -> None: ...

    MethodVersion: str

class ImsValidationSetEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.IMS.ImsMethParameterChangeEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.IMS.ImsMethParameterChangeEventArgs,
    ) -> None: ...

class ImsValueChangeEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.IMS.ImsMethParameterChangeEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.IMS.ImsMethParameterChangeEventArgs,
    ) -> None: ...

class MethParameterLimitType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Exclusive: Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterLimitType = (
        ...
    )  # static # readonly
    Inclusive: Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterLimitType = (
        ...
    )  # static # readonly
    NoLimit: Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterLimitType = (
        ...
    )  # static # readonly

class MethParameterLimited(
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter,
    Generic[T, TLimit],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo,
    Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameter[T],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterLimited[T, TLimit],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter[T],
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, units: Agilent.MassSpectrometry.MIDAC.MidacUnits) -> None: ...
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterLimited
    ) -> None: ...

class MethParameterLimits(
    Generic[T], Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterLimits[T]
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterLimits
    ) -> None: ...

class MethParameterMinMaxRange(
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter[
        Agilent.MassSpectrometry.MIDAC.IRange[T]
    ],
    Generic[T],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo,
    Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterLimited[
        Agilent.MassSpectrometry.MIDAC.IRange[T], T
    ],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterLimited[
        Agilent.MassSpectrometry.MIDAC.IRange[T], T
    ],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterRange[T],
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, units: Agilent.MassSpectrometry.MIDAC.MidacUnits) -> None: ...
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterMinMaxRange
    ) -> None: ...
    def ToString(self) -> str: ...

class MethParameterSet(
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo,
    Iterable[Any],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterSet,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter,
):  # Class
    # Nested Types

    class ParameterSetIterator(Iterator[Any]):  # Class
        def __init__(
            self,
            parameterSet: Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameterSet,
        ) -> None: ...

        Current: Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter  # readonly

        def MoveNext(self) -> bool: ...
        def Reset(self) -> None: ...

class MethParameter(
    Generic[T],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameterXmlIo,
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter[T],
    Agilent.MassSpectrometry.DataAnalysis.IMS.IMethParameter,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, units: Agilent.MassSpectrometry.MIDAC.MidacUnits) -> None: ...
    @overload
    def __init__(
        self, src: Agilent.MassSpectrometry.DataAnalysis.IMS.MethParameter
    ) -> None: ...
    def ToString(self) -> str: ...
