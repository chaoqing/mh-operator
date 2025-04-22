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

from . import MRMOptimizer, Properties, Quant, Unknowns

# Discovered Generic TypeVars:
T = TypeVar("T")

# Stubs for namespace: Agilent.MassHunter.Quantitative.ApplicationServices

class ApplicationServiceException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class Chromatogram:  # Class
    def __init__(self) -> None: ...

    XValues: List[float]
    YValues: List[float]

class Config:  # Class
    @staticmethod
    def GetTimeout() -> Optional[System.TimeSpan]: ...
    @staticmethod
    def GetSubFolder(type: str) -> str: ...
    @staticmethod
    def GetServiceClientType(type: str) -> str: ...
    @staticmethod
    def SetupTimeout(binding: System.ServiceModel.Channels.Binding) -> None: ...
    @staticmethod
    def GetServiceInstall(type: str) -> str: ...

class DataTableTransfer(
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ApplicationServices.IDataTableTransfer,
):  # Class
    def __init__(self) -> None: ...
    def Initialize(
        self,
        host: System.ServiceModel.ServiceHost,
        table: System.Data.DataTable,
        pageSize: int,
    ) -> None: ...
    def Reset(self) -> None: ...
    def ReadNext(self) -> System.Data.DataTable: ...
    def GetTotalCount(self) -> int: ...
    def Dispose(self) -> None: ...

class DataTableTransferClient(
    System.ServiceModel.ClientBase[
        Agilent.MassHunter.Quantitative.ApplicationServices.IDataTableTransfer
    ],
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ApplicationServices.IDataTableTransfer,
    System.ServiceModel.ICommunicationObject,
):  # Class
    def __init__(
        self,
        binding: System.ServiceModel.Channels.Binding,
        address: System.ServiceModel.EndpointAddress,
    ) -> None: ...
    def ReadNext(self) -> System.Data.DataTable: ...
    def Reset(self) -> None: ...
    def Dispose(self) -> None: ...
    def GetTotalCount(self) -> int: ...

class DataTransferClient(
    System.IDisposable,
    Generic[T],
    System.ServiceModel.ClientBase[
        Agilent.MassHunter.Quantitative.ApplicationServices.IDataTransfer[T]
    ],
    Agilent.MassHunter.Quantitative.ApplicationServices.IDataTransfer[T],
    System.ServiceModel.ICommunicationObject,
):  # Class
    def __init__(
        self,
        binding: System.ServiceModel.Channels.Binding,
        address: System.ServiceModel.EndpointAddress,
    ) -> None: ...
    def ReadNext(self) -> T: ...
    def Reset(self) -> None: ...
    def Dispose(self) -> None: ...
    def GetTotalCount(self) -> int: ...

class DataTransfer(
    Generic[T],
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ApplicationServices.IDataTransfer[T],
):  # Class
    def __init__(self, list: List[T]) -> None: ...
    def ReadNext(self) -> T: ...
    def Reset(self) -> None: ...
    def Dispose(self) -> None: ...
    def GetTotalCount(self) -> int: ...

class IApplicationServiceBase(System.IDisposable):  # Interface
    CommunicationState: System.ServiceModel.CommunicationState  # readonly

    def ConnectWithCallback(self, callback: Any) -> None: ...
    def Reconnect(self) -> None: ...
    def CloseApplication(self) -> None: ...
    def Connect(self) -> None: ...

class IDataTableTransfer(System.IDisposable):  # Interface
    def ReadNext(self) -> System.Data.DataTable: ...
    def Reset(self) -> None: ...
    def GetTotalCount(self) -> int: ...

class IDataTransfer(System.IDisposable):  # Interface
    def ReadNext(self) -> T: ...
    def Reset(self) -> None: ...
    def GetTotalCount(self) -> int: ...

class ServiceFactory:  # Class
    @staticmethod
    def CreateService() -> T: ...

class ServiceFault:  # Class
    def __init__(self) -> None: ...

    InnerExceptionMessage: str
    InnerExceptionStackTrace: str
    InnerExceptionType: str
    Message: str
    Source: str
    StackTrace: str
    Type: str
