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

from .ApplicationServices import IApplicationServiceBase
from .ApplicationServices.Quant import IQuantitativeAnalysis
from .UIModel import IMainWindow

# Stubs for namespace: Agilent.MassHunter.Quantitative.QuantAppServices

class Client(
    IQuantitativeAnalysis, IApplicationServiceBase, System.IDisposable
):  # Class
    def __init__(self) -> None: ...

    CommunicationState: System.ServiceModel.CommunicationState  # readonly

    def CloseApplication(self) -> None: ...
    def Reconnect(self) -> None: ...
    def Connect(self) -> None: ...
    def ShowWindow(self) -> None: ...
    def Dispose(self) -> None: ...
    def RunScript(self, scriptFile: str) -> None: ...
    def ConnectWithCallback(self, callback: Any) -> None: ...

class IService(
    IQuantitativeAnalysis, IApplicationServiceBase, System.IDisposable
):  # Interface
    ...

class Service(
    System.IDisposable,
    IQuantitativeAnalysis,
    IApplicationServiceBase,
    Agilent.MassHunter.Quantitative.QuantAppServices.IService,
):  # Class
    def __init__(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
        mainWindow: IMainWindow,
    ) -> None: ...

    CommunicationState: System.ServiceModel.CommunicationState  # readonly

    def CloseApplication(self) -> None: ...
    def Reconnect(self) -> None: ...
    def Open(self, key: str) -> None: ...
    def Connect(self) -> None: ...
    def ShowWindow(self) -> None: ...
    def Dispose(self) -> None: ...
    def RunScript(self, scriptFile: str) -> None: ...
    def ConnectWithCallback(self, callback: Any) -> None: ...
