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

from .QueuedTask import QueuedTasks

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging

class DirectoryWatcher(System.IDisposable):  # Class
    def __init__(
        self,
        queue: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.WatchFileProcessQueue,
        wpe: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.WatchPathEntry,
    ) -> None: ...
    def Dispose(self) -> None: ...

class FileMessagingLog(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def CloseEventLog(self) -> None: ...
    @staticmethod
    def Log(
        filelog: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.FileMessagingLog,
        type: System.Diagnostics.EventLogEntryType,
        trace: bool,
        cat: str,
        format: str,
        args: List[Any],
    ) -> None: ...
    @staticmethod
    def LogWarning(
        log: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.FileMessagingLog,
        trace: bool,
        cat: str,
        format: str,
        args: List[Any],
    ) -> None: ...
    @staticmethod
    def LogInfo(
        log: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.FileMessagingLog,
        trace: bool,
        cat: str,
        format: str,
        args: List[Any],
    ) -> None: ...
    def StartEventLog(self, source: str) -> None: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def LogError(
        log: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.FileMessagingLog,
        trace: bool,
        cat: str,
        format: str,
        args: List[Any],
    ) -> None: ...

class IQueuedTaskEventSink(object):  # Interface
    def OnTaskFinish(
        self,
        info: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskInformation,
        e: System.Exception,
    ) -> None: ...
    def OnTaskStart(
        self,
        info: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskInformation,
    ) -> None: ...

class PriorityEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AboveNormal: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.PriorityEnum
    ) = ...  # static # readonly
    High: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.PriorityEnum
    ) = ...  # static # readonly
    Highest: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.PriorityEnum
    ) = ...  # static # readonly
    Low: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.PriorityEnum
    ) = ...  # static # readonly
    Lowest: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.PriorityEnum
    ) = ...  # static # readonly
    Normal: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.PriorityEnum
    ) = ...  # static # readonly
    VeryHigh: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.PriorityEnum
    ) = ...  # static # readonly
    VeryLow: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.PriorityEnum
    ) = ...  # static # readonly

class QueuedTaskInformation:  # Class
    Completion: System.DateTime  # readonly
    Creation: System.DateTime  # readonly
    Host: str  # readonly
    Name: str  # readonly
    Owner: str  # readonly
    Path: str  # readonly
    Status: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskStatus
    )  # readonly

    def Equals(
        self,
        info: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskInformation,
    ) -> bool: ...

class QueuedTaskStatus(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Canceled: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskStatus
    ) = ...  # static # readonly
    Done: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskStatus
    ) = ...  # static # readonly
    Error: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskStatus
    ) = ...  # static # readonly
    Processing: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskStatus
    ) = ...  # static # readonly
    Unknown: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskStatus
    ) = ...  # static # readonly
    Waiting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskStatus
    ) = ...  # static # readonly

class QueuedTaskWatchEntry(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.WatchPathEntry,
    System.IDisposable,
    System.ICloneable,
):  # Class
    def __init__(self) -> None: ...

    Controller: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskWatchPathController
    )
    Tasks: QueuedTasks  # readonly

    def BeginProcess(
        self, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def Abort(self) -> None: ...
    def Clone(self) -> Any: ...

class QueuedTaskWatchPathController(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.WatchPathController,
    System.IDisposable,
):  # Class
    def __init__(self) -> None: ...

    QueueDirectory: str  # static # readonly
    WatchDirectory: str  # static # readonly

    def Start(self) -> None: ...
    def Stop(self) -> None: ...
    def EventSink(
        self,
        sink: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.IQueuedTaskEventSink,
        register: bool,
    ) -> None: ...
    @staticmethod
    def GetQueueTasks(
        watchpath: str, queuedirectory: str
    ) -> Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskInformation
    ]: ...
    def GetProcessingTasks(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskInformation
    ]: ...

class ServiceObject(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.IQueuedTaskEventSink,
    System.ServiceProcess.ServiceBase,
    System.ComponentModel.IComponent,
):  # Class
    def __init__(self) -> None: ...

    IsLocked: bool  # static # readonly
    IsRunning: bool  # readonly

    def DeleteTasks(
        self,
        tasks: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskInformation
        ],
    ) -> None: ...
    def Lock(self) -> None: ...
    def UserStop(self) -> None: ...
    def EventSink(
        self,
        sink: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.IQueuedTaskEventSink,
        register: bool,
    ) -> None: ...
    def RetryTasks(
        self,
        tasks: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskInformation
        ],
    ) -> None: ...
    @staticmethod
    def ConnectToServer() -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.ServiceObject
    ): ...
    @staticmethod
    def CreateServer() -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.ServiceObject
    ): ...
    def UserStart(self) -> None: ...
    @staticmethod
    def SetupLogTraceListener(configSetting: str) -> None: ...
    def GetTaskInformation(
        self,
    ) -> Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.QueuedTaskInformation
    ]: ...

class WatchFileProcessQueue(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def AddPath(
        self,
        entry: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.WatchPathEntry,
    ) -> None: ...
    def Abort(self) -> None: ...
    def Dispose(self) -> None: ...
    def GetProcessingEntries(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.WatchPathEntry
    ]: ...

class WatchPathController(System.IDisposable):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, configfilename: str) -> None: ...

    Log: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.FileMessagingLog
    )

    def Start(self) -> None: ...
    def Dispose(self) -> None: ...
    def Stop(self) -> None: ...

class WatchPathEntry(System.IDisposable, System.ICloneable):  # Class
    def __init__(self) -> None: ...

    filter: str
    includesubdirectories: bool
    queuefilename: str
    type: str
    watchfilename: str
    watchname: str

    Log: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.FileMessagingLog
    )
    queuedirectory: str
    watchpath: str

    def EndProcess(self, result: System.IAsyncResult) -> None: ...
    def Abort(self) -> None: ...
    def Clone(self) -> Any: ...
    def BeginProcess(
        self, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def Dispose(self) -> None: ...

class WatchPaths(System.MarshalByRefObject):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, WatchConfigName: str) -> None: ...

    Log: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessaging.FileMessagingLog
    )
    WatchConfigName: str  # readonly
    WatchPathsTable: System.Data.DataTable  # readonly

    def Load(self) -> None: ...

    Changed: System.EventHandler  # Event
    Deleted: System.EventHandler  # Event
