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
TData = TypeVar("TData")
from .CoreTypes import IExtractionParameters

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.CoreType

class ExtractedSignalDataContainer(
    Agilent.OpenLab.Framework.DataAccess.CoreType.IExtractedSignalDataContainer[TData],
    Generic[TData],
    Agilent.OpenLab.Framework.DataAccess.CoreType.SignalDataContainer[TData],
    Agilent.OpenLab.Framework.DataAccess.CoreType.ISignalDataContainer[TData],
):  # Class
    def __init__(
        self,
        signalData: TData,
        signalMetaData: Agilent.OpenLab.Framework.DataAccess.CoreType.ISignalMetaData,
        extractionParameters: IExtractionParameters,
    ) -> None: ...

    ExtractionParameters: IExtractionParameters  # readonly

class IExtractedSignalDataContainer(
    Agilent.OpenLab.Framework.DataAccess.CoreType.ISignalDataContainer[TData]
):  # Interface
    ExtractionParameters: IExtractionParameters  # readonly

class ISignalDataContainer(object):  # Interface
    SignalData: TData  # readonly
    SignalMetaData: (
        Agilent.OpenLab.Framework.DataAccess.CoreType.ISignalMetaData
    )  # readonly

class ISignalMetaData(object):  # Interface
    Description: str  # readonly
    Name: str  # readonly
    TraceId: str  # readonly

class SignalDataContainer(
    Generic[T], Agilent.OpenLab.Framework.DataAccess.CoreType.ISignalDataContainer[T]
):  # Class
    def __init__(
        self,
        signalData: T,
        signalMetaData: Agilent.OpenLab.Framework.DataAccess.CoreType.ISignalMetaData,
    ) -> None: ...

    SignalData: T  # readonly
    SignalMetaData: (
        Agilent.OpenLab.Framework.DataAccess.CoreType.ISignalMetaData
    )  # readonly

class SignalMetaData(
    Agilent.OpenLab.Framework.DataAccess.CoreType.ISignalMetaData
):  # Class
    def __init__(self, name: str, description: str, traceId: str) -> None: ...

    Description: str  # readonly
    Name: str  # readonly
    TraceId: str  # readonly
