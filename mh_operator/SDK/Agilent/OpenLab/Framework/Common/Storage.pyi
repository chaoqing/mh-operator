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

# Stubs for namespace: Agilent.OpenLab.Framework.Common.Storage

class FileVersionException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

    CurrentVersion: int
    FileVersion: int

    def GetObjectData(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class StorageProviderSingleton:  # Class
    @staticmethod
    def GetInstance() -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider
    ): ...
    @staticmethod
    def InitStorageProvider(
        storage: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
    ) -> None: ...
