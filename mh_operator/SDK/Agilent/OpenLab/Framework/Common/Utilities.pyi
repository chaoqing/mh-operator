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

# Stubs for namespace: Agilent.OpenLab.Framework.Common.Utilities

class AppInfo:  # Class
    BuildNumber: str  # static # readonly
    Company: str  # static # readonly
    Copyright: str  # static # readonly
    Description: str  # static # readonly
    FullVersion: str  # static # readonly
    InstalledModules: str  # static # readonly
    Product: str  # static # readonly
    ProductGroup: str  # static
    ProductGroupVersion: str  # static
    ProductShortName: str  # static
    Title: str  # static # readonly
    Version: str  # static # readonly

class EventSubscribers:  # Class
    @staticmethod
    def Get(target: Any, eventName: str) -> List[System.Delegate]: ...

class ParamValidator:  # Class
    @staticmethod
    def CheckLessThan(value_: T, mustBeLessThan: T, parameterName: str) -> T: ...
    @staticmethod
    def CheckEqualOrLessThan(
        value_: T, mustBeEqualOrLessThan: T, parameterName: str
    ) -> T: ...
    @staticmethod
    def CheckGreaterThan(value_: T, mustBeGreaterThan: T, parameterName: str) -> T: ...
    @staticmethod
    def CheckSame(source: T, target: T) -> T: ...
    @staticmethod
    def CheckEqualOrGreaterThan(
        value_: T, mustBeEqualOrGreaterThan: T, parameterName: str
    ) -> T: ...
    @staticmethod
    def CheckNotNull(value_: T, parameterName: str) -> T: ...
    @staticmethod
    def CheckNotNullOrEmpty(value_: str, parameterName: str) -> str: ...
    @staticmethod
    def CheckNotNullAndOfType(value_: Any, parameterName: str) -> T: ...

class StringStream(System.IO.MemoryStream, System.IDisposable):  # Class
    @overload
    def __init__(self, content: str) -> None: ...
    @overload
    def __init__(self, content: str, encoding: System.Text.Encoding) -> None: ...

    String: str  # readonly

    @overload
    @staticmethod
    def ConvertToString(stream: System.IO.Stream) -> str: ...
    @overload
    @staticmethod
    def ConvertToString(
        stream: System.IO.Stream, encoding: System.Text.Encoding
    ) -> str: ...

class TempFileStream(System.IDisposable, System.IO.Stream):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, sourceStream: System.IO.Stream) -> None: ...

    CanRead: bool  # readonly
    CanSeek: bool  # readonly
    CanWrite: bool  # readonly
    Length: int  # readonly
    Position: int

    def Read(self, buffer: List[int], offset: int, count: int) -> int: ...
    def Write(self, buffer: List[int], offset: int, count: int) -> None: ...
    def Flush(self) -> None: ...
    def SetLength(self, value_: int) -> None: ...
    def Seek(self, offset: int, origin: System.IO.SeekOrigin) -> int: ...
