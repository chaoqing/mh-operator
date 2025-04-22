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

from . import (
    UI,
    AppCommand,
    Configuration,
    DataCommand,
    ScriptIF,
    ScriptIFImpls,
    Tools,
    UAControls,
    Utils,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit

class CommandLine:  # Class
    def __init__(self) -> None: ...

    AccountName: str
    ConnectionTicket: str
    Culture: str
    Domain: str
    EncryptedPassword: str
    Method: str
    Password: str
    Server: str
    UnknownsAnalysis: bool
    User: str

class ReportMethodEditException(
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
    @overload
    def __init__(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...
