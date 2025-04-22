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

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Utilities.StreamProxies

class AcamlStreamProxy(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlStreamProxy,
    System.IDisposable,
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Utilities.StreamProxies.StreamProxyBase,
):  # Class
    def __init__(self, verifyChecksum: bool, validateSchema: bool) -> None: ...
    @overload
    def Read(
        self,
        storageFileAccess: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageFileAccess,
        path: str,
    ) -> bool: ...
    @overload
    def Read(self, stream: System.IO.Stream) -> bool: ...

class StreamProxyBase(System.IDisposable):  # Class
    FileBasedStream: System.IO.Stream  # readonly
    TempFilePath: str  # readonly

    @overload
    def Read(
        self,
        storageFileAccess: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageFileAccess,
        path: str,
    ) -> bool: ...
    @overload
    def Read(self, stream: System.IO.Stream) -> bool: ...
    def Dispose(self) -> None: ...
