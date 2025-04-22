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

from .Compliance import ICompliance
from .QueuedTask import IQueuedTask, IQueuedTaskAction, IQueuedTaskContext, TaskPriority
from .ReportMethod import ReportMethodDataSet
from .ReportScript import GraphicsRange, IFixedGraphics

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodRun

class CommandLine:  # Class
    def __init__(self) -> None: ...

    AccountName: str
    ApplicationType: str
    BatchFile: str
    BatchPath: str
    CancelEventName: str
    CompoundIds: str
    ConnectionTicket: str
    Culture: str
    Domain: str
    EncryptedPassword: str
    Help: bool
    LogFile: str
    Method: str
    OutputPath: str
    Parameters: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodRun.MethodRunParameters
    )  # readonly
    Password: str
    Queue: bool
    ReporterName: str
    SampleIds: str
    Server: str
    User: str

    def Run(self) -> None: ...

class ErrorCode(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    ERR_ABORT: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodRun.ErrorCode
    ) = ...  # static # readonly
    ERR_COMMANDLINE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodRun.ErrorCode
    ) = ...  # static # readonly
    ERR_COMPLIANCE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodRun.ErrorCode
    ) = ...  # static # readonly
    ERR_INVALID_CULTURE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodRun.ErrorCode
    ) = ...  # static # readonly
    ERR_PROCESS: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodRun.ErrorCode
    ) = ...  # static # readonly
    NOERROR: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodRun.ErrorCode
    ) = ...  # static # readonly

class FixedGraphics(IFixedGraphics):  # Class
    def __init__(self, dataset: ReportMethodDataSet, reportID: int) -> None: ...
    def GetSampleRangeX(self, sampleName: str) -> Optional[GraphicsRange]: ...
    def GetSampleRangeY(self, sampleName: str) -> Optional[GraphicsRange]: ...
    def GetCompoundRangeMz(self, compoundName: str) -> Optional[GraphicsRange]: ...
    def GetCompoundRangeX(self, compoundName: str) -> Optional[GraphicsRange]: ...
    def GetCompoundRangeY(self, compoundName: str) -> Optional[GraphicsRange]: ...

class IReportMethodTask(
    IQueuedTask, System.Xml.Serialization.IXmlSerializable, System.IDisposable
):  # Interface
    ApplicationType: str
    BatchFile: str
    BatchPath: str
    CompoundIds: List[int]
    Culture: str
    MethodPath: str
    OutputPath: str
    ReporterName: str
    SampleIds: List[int]

class MethodRunParameters:  # Class
    def __init__(self) -> None: ...

    ApplicationType: str
    BatchFile: str
    BatchPath: str
    CancelEventName: str
    CompoundIds: List[int]
    Context: IQueuedTaskContext
    Culture: str
    Method: str
    OutputPath: str
    Priority: TaskPriority
    ReporterName: str
    SampleIds: List[int]

class ProcessPrePost(System.IDisposable):  # Class
    def __init__(
        self,
        outputFolder: str,
        row: ReportMethodDataSet.PrePostProcessRow,
        compliance: ICompliance,
    ) -> None: ...
    def Process(self, formatting: ReportMethodDataSet.FormattingRow) -> None: ...
    def Dispose(self) -> None: ...

class ProcessReportBuilder(System.IDisposable):  # Class
    def Dispose(self) -> None: ...

class ReportMethodTask(
    System.Xml.Serialization.IXmlSerializable,
    System.IDisposable,
    IQueuedTask,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodRun.IReportMethodTask,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodRun.MethodRunParameters,
    ) -> None: ...

    Actions: List[IQueuedTaskAction]  # readonly
    ApplicationType: str
    BatchFile: str
    BatchPath: str
    CancelEventName: str
    CompoundIds: List[int]
    Context: IQueuedTaskContext
    Culture: str
    MethodPath: str
    OutputPath: str
    ProcessingPriority: TaskPriority
    ReporterName: str
    SampleIds: List[int]
    TaskDescription: str  # readonly
    TaskLockName: str  # readonly
    TaskName: str  # readonly

    def Process(self) -> None: ...
    def GetSchema(self) -> System.Xml.Schema.XmlSchema: ...
    def WriteXml(self, writer: System.Xml.XmlWriter) -> None: ...
    def Dispose(self) -> None: ...
    def ReadXml(self, reader: System.Xml.XmlReader) -> None: ...

class Runner(System.MarshalByRefObject):  # Class
    def __init__(self) -> None: ...

    FilesToClean: List[str]  # readonly

    def Run(self, args: List[str]) -> int: ...
    def SetDebugEngine(self, engine: System.MarshalByRefObject) -> None: ...
    def InitializeLifetimeService(self) -> Any: ...
