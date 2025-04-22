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

from .Compliance import ICompliance, IDataStorage, ILogonECM
from .ComplianceUI import IComplianceUI
from .DataStorageECM import ComplianceECM, DataStorage

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMProxy

class Client(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    server_url: str = ...  # static # readonly

    def Download(
        self,
        onlyIfChecksumNotMatch: bool,
        filePath: str,
        revisionNumber: str,
        folderPath: str,
        recreateDirectoryStructure: bool,
        overwriteWithoutPrompt: bool,
    ) -> bool: ...
    def Dispose(self) -> None: ...
    def Connect(self, serverUrl: str, loginID: str) -> None: ...
    @staticmethod
    def GetServerHost(loginID: str) -> str: ...

class Compliance(
    IComplianceUI, System.IDisposable, ComplianceECM, ICompliance, ILogonECM
):  # Class
    def __init__(self) -> None: ...

class DataStorage(System.IDisposable, IDataStorage):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMProxy.Compliance,
    ) -> None: ...
    def InitFolders(self) -> None: ...

class ECMProxyException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, ex: System.Exception) -> None: ...
    @overload
    def __init__(self) -> None: ...

    ECMCode: int
    ECMMessage: str

class IServer(object):  # Interface
    def Download(
        self,
        onlyIfChecksumNotMatch: bool,
        filePath: str,
        revisionNumber: str,
        folderPath: str,
        recreateDirectoryStructure: bool,
        overwriteWithoutPrompt: bool,
    ) -> bool: ...
    def Disconnect(self) -> None: ...
    def Login(self, serverUrl: str, loginID: str) -> None: ...
