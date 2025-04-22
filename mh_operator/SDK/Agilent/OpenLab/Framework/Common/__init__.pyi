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

from . import CustomAttributes, Notification, Storage, Utilities

# Discovered Generic TypeVars:
T = TypeVar("T")

# Stubs for namespace: Agilent.OpenLab.Framework.Common

class AsyncHelpers:  # Class
    @staticmethod
    def Yield() -> System.Threading.Tasks.Task[None]: ...
    @overload
    @staticmethod
    def RunCancelableAsync(
        cancellationToken: System.Threading.CancellationToken,
        task: System.Threading.Tasks.Task[None],
        sleepTime: int = ...,
    ) -> System.Threading.Tasks.Task[None]: ...
    @overload
    @staticmethod
    def RunCancelableAsync(
        cancellationToken: System.Threading.CancellationToken,
        task: System.Threading.Tasks.Task[T],
        sleepTime: int = ...,
    ) -> System.Threading.Tasks.Task[T]: ...
    @overload
    @staticmethod
    def RunSync(task: System.Func[System.Threading.Tasks.Task[None]]) -> None: ...
    @overload
    @staticmethod
    def RunSync(
        task: System.Func[System.Threading.Tasks.Task[None]],
        setStopAction: System.Action[System.Action, bool],
    ) -> None: ...
    @overload
    @staticmethod
    def RunSync(task: System.Func[System.Threading.Tasks.Task[T]]) -> T: ...
    @overload
    @staticmethod
    def RunSync(
        task: System.Func[System.Threading.Tasks.Task[T]],
        setStopAction: System.Action[System.Action, bool],
    ) -> T: ...

class AsyncTaskManager(System.IDisposable):  # Class
    CancellationToken: System.Threading.CancellationToken  # readonly
    Instance: Agilent.OpenLab.Framework.Common.AsyncTaskManager  # static # readonly

    def Start(self, action: System.Action) -> System.Threading.Tasks.Task[None]: ...
    def Wait(self, taskId: int, timeout: int = ...) -> bool: ...
    @staticmethod
    def Reset() -> None: ...
    def Remove(self, taskId: int) -> None: ...
    def Dispose(self) -> None: ...
    def AbortAll(self) -> None: ...

class DateTimeExtensions:  # Class
    DateFormatSpecificationStringForStandardFormat: str  # static # readonly
    DateFormatStringForStandardFormat: str  # static # readonly
    FormatStringForCurrentCultureWithGmtOffset: str  # static # readonly
    FormatStringForStandardFormat: str  # static # readonly

    @staticmethod
    def NormalizeDateTimeKind(dateTime: System.DateTime) -> System.DateTime: ...
    @staticmethod
    def ToStringForCurrentCultureWithGmtOffset(dateTime: System.DateTime) -> str: ...
    @staticmethod
    def ToStringUsingStandardFormat(dateTime: System.DateTime) -> str: ...

class NotificationException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @overload
    def __init__(self, innerException: System.Exception) -> None: ...

class SearchException(
    Agilent.OpenLab.Framework.Common.StorageException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @overload
    def __init__(self, innerException: System.Exception) -> None: ...

class StorageException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @overload
    def __init__(self, innerException: System.Exception) -> None: ...

class StorageFileNotFoundException(
    Agilent.OpenLab.Framework.Common.StorageException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @overload
    def __init__(self, innerException: System.Exception) -> None: ...

class StorageNotAvailableException(
    Agilent.OpenLab.Framework.Common.StorageException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @overload
    def __init__(self, innerException: System.Exception) -> None: ...

class StoragePermissionException(
    Agilent.OpenLab.Framework.Common.StorageException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @overload
    def __init__(self, innerException: System.Exception) -> None: ...

class WorkAreaDoesNotExistException(
    Agilent.OpenLab.Framework.Common.StorageException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, inner: System.Exception) -> None: ...
    @overload
    def __init__(self, innerException: System.Exception) -> None: ...
