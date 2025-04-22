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

from . import AcamlFixes, StreamProxies
from .Interfaces import DataChangeLevel

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Utilities

class Constants:  # Class
    InjectionMetadataCustomField: str = ...  # static # readonly
    OriginalPackagingModeCustomField: str = ...  # static # readonly

class ProcessingTransaction:  # Class
    def __init__(self, docId: System.Guid) -> None: ...

    IsActive: bool  # readonly

    def Open(self) -> None: ...
    def TryOpen(self) -> bool: ...
    def Commit(self, dataChangeLevel: DataChangeLevel) -> None: ...
    def TryCommit(self, dataChangeLevel: DataChangeLevel) -> None: ...

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
