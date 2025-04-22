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

# Stubs for namespace: Agilent.MassSpectrometry.Utilities

class CsvFileTraceListener(
    System.IDisposable, System.Diagnostics.TextWriterTraceListener
):  # Class
    @overload
    def __init__(self, stream: System.IO.Stream, name: str) -> None: ...
    @overload
    def __init__(self, stream: System.IO.Stream) -> None: ...
    @overload
    def __init__(self, fileName: str, name: str) -> None: ...
    @overload
    def __init__(self, fileName: str) -> None: ...
    @overload
    def __init__(self, writer: System.IO.TextWriter, name: str) -> None: ...
    @overload
    def __init__(self, writer: System.IO.TextWriter) -> None: ...
    @overload
    def Write(self, anObject: Any) -> None: ...
    @overload
    def Write(self, message: str) -> None: ...
    @overload
    def Write(self, anObject: Any, category: str) -> None: ...
    @overload
    def Write(self, message: str, category: str) -> None: ...
    @overload
    def WriteLine(self, anObject: Any) -> None: ...
    @overload
    def WriteLine(self, message: str) -> None: ...
    @overload
    def WriteLine(self, anObject: Any, category: str) -> None: ...
    @overload
    def WriteLine(self, message: str, category: str) -> None: ...

class MemoryTraceListener(
    System.IDisposable, System.Diagnostics.TraceListener
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, initData: str) -> None: ...
    @overload
    def __init__(self, initData: str, name: str) -> None: ...

    DEFAULT_LOG_FILE_NAME: str = ...  # static # readonly
    DEFAULT_LOG_SIZE: int = ...  # static # readonly
    MAX_LOG_SIZE: int = ...  # static # readonly
    MEGABYTE: int = ...  # static # readonly
    MIN_LOG_SIZE: int = ...  # static # readonly

    LastWrittenCompressedLogFile: str  # static # readonly
    LastWrittenLogFile: str  # static # readonly
    LogFileName: str
    LogSize: int

    @staticmethod
    def IsActive() -> bool: ...
    @overload
    def Write(self, anObject: Any) -> None: ...
    @overload
    def Write(self, message: str) -> None: ...
    @overload
    def Write(self, anObject: Any, category: str) -> None: ...
    @overload
    def Write(self, message: str, category: str) -> None: ...
    @overload
    def WriteLine(self, anObject: Any) -> None: ...
    @overload
    def WriteLine(self, message: str) -> None: ...
    @overload
    def WriteLine(self, anObject: Any, category: str) -> None: ...
    @overload
    def WriteLine(self, message: str, category: str) -> None: ...
    @staticmethod
    def DumpCompressedLog() -> None: ...
    @staticmethod
    def DumpLog() -> None: ...
    def Close(self) -> None: ...

class TraceListenerUtilities:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def GetLogPath(fileName: str) -> str: ...
