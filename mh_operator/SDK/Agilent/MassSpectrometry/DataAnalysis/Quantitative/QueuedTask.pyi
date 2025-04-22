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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask

class CancelSignalDetectedException(
    System.ApplicationException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class IQueuedTask(
    System.Xml.Serialization.IXmlSerializable, System.IDisposable
):  # Interface
    Actions: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskAction
    ]  # readonly
    CancelEventName: str
    Context: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskContext
    )
    ProcessingPriority: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.TaskPriority
    )
    TaskDescription: str  # readonly
    TaskLockName: str  # readonly
    TaskName: str  # readonly

    def Process(self) -> None: ...

class IQueuedTaskAction(object):  # Interface
    DisplayName: str  # readonly

    def Execute(self, parent: System.Windows.Forms.IWin32Window) -> None: ...

class IQueuedTaskContext(object):  # Interface
    Compliance: ICompliance  # readonly

class IQueuedTaskNotification(
    System.Xml.Serialization.IXmlSerializable, System.IDisposable
):  # Interface
    def OnSubTaskStart(
        self,
        task: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    ) -> None: ...
    def OnTaskFinish(self) -> None: ...
    def OnTaskError(self, message: str, e: System.Exception) -> None: ...
    def OnTaskStart(self, queuedFile: str) -> None: ...
    def OnSubTaskFinish(self) -> None: ...

class LockTasks(System.IDisposable):  # Class
    def __init__(self, lockNames: List[str]) -> None: ...
    def CanStart(self) -> bool: ...
    def Dispose(self) -> None: ...
    def Unlock(self) -> None: ...
    def Lock(self) -> None: ...

class OpenDirectoryTaskAction(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskAction,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.OpenFileTaskAction,
):  # Class
    def __init__(self, directory: str) -> None: ...

    DisplayName: str  # readonly

class OpenFileTaskAction(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskAction
):  # Class
    def __init__(self, file: str) -> None: ...

    DisplayName: str  # readonly

    def Execute(self, parent: System.Windows.Forms.IWin32Window) -> None: ...

class QueuedTaskConfiguration:  # Class
    LogDirectory: str  # static # readonly
    QueueDirectory: str  # static
    ServiceType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.ServiceType
    )  # static # readonly
    TaskNotificationSettings: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.QueuedTaskNotificationSetting
    ]  # static # readonly
    WatchDirectory: str  # static
    WriteTaskLog: bool  # static # readonly

    @staticmethod
    def GenerateQueueFileName(nameBase: str) -> str: ...
    @overload
    @staticmethod
    def GetFullPathName(path: str) -> str: ...
    @overload
    @staticmethod
    def GetFullPathName(assembly: System.Reflection.Assembly, path: str) -> str: ...

class QueuedTaskContext(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskContext
):  # Class
    def __init__(self) -> None: ...

    Compliance: ICompliance

class QueuedTaskException(
    System.ApplicationException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class QueuedTaskNotificationSetting(System.Configuration.ConfigurationElement):  # Class
    def __init__(self) -> None: ...

    Name: str
    Type: str

class QueuedTaskNotificationSettingCollection(
    Iterable[Any], System.Configuration.ConfigurationElementCollection, Sequence[Any]
):  # Class
    def __init__(self) -> None: ...

class QueuedTaskSettingsSection(System.Configuration.ConfigurationSection):  # Class
    def __init__(self) -> None: ...

    LogDirectory: str
    QueueDirectory: str
    ServiceNotifications: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.QueuedTaskNotificationSettingCollection
    )  # readonly
    ServiceType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.ServiceType
    )
    WatchDirectory: str
    WriteTaskLog: bool

class QueuedTasks(System.Xml.Serialization.IXmlSerializable):  # Class
    def __init__(self) -> None: ...

    Completion: System.DateTime
    Notifications: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskNotification
    ]
    Tasks: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask
    ]

    def Cleanup(self) -> None: ...

class ServiceType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    LocalProcess: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.ServiceType
    ) = ...  # static # readonly
    LocalService: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.ServiceType
    ) = ...  # static # readonly
    RemoteUserProcess: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.ServiceType
    ) = ...  # static # readonly
    RemoteWindowsService: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.ServiceType
    ) = ...  # static # readonly

class TaskPriority(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    High: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.TaskPriority = (
        ...
    )  # static # readonly
    Low: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.TaskPriority = (
        ...
    )  # static # readonly
    Normal: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.TaskPriority
    ) = ...  # static # readonly

class TaskQueue:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def WriteTaskCompletionTime(taskFile: str, completion: System.DateTime) -> None: ...
    @staticmethod
    def LoadTaskLockNames(stream: System.IO.Stream) -> List[str]: ...
    @staticmethod
    def CreateTask(
        type: System.Type,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask: ...
    @staticmethod
    def ReadTaskCompletionTime(taskFile: str) -> System.DateTime: ...
    @staticmethod
    def ProcessTasksInSeparateDomain(
        queuedFile: str, cancelEventName: str, logFilePath: str
    ) -> None: ...
    @staticmethod
    def PushTasks(
        name: str,
        notifications: List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskNotification
        ],
        tasks: List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask
        ],
    ) -> None: ...
    @staticmethod
    def LoadTasks(
        stream: System.IO.Stream,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.QueuedTasks: ...

    # Nested Types

    class TaskStarter(System.MarshalByRefObject):  # Class
        def __init__(self) -> None: ...
        def Start(
            self, queuedFile: str, cancelEventName: str, logFilePath: str
        ) -> None: ...

class TaskQueueType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    FileWatcher: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.TaskQueueType
    ) = ...  # static # readonly
    MSMQ: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.TaskQueueType
    ) = ...  # static # readonly
