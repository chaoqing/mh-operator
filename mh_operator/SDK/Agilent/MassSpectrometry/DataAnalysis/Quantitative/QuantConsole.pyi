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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantConsole

class CommandLine:  # Class
    def __init__(self) -> None: ...

    AccountName: str
    ConnectionTicket: str
    ConsoleTrace: bool
    Culture: str
    DefineConstants: List[str]
    Domain: str
    EncryptedPassword: str
    ErrorHasUserWhileNotRequired: bool
    Help: bool
    Instrument: str
    NoLogo: bool
    ParametersXml: str
    Password: str
    ScriptFiles: List[str]
    Server: str
    Silent: bool
    User: str

    def Run(self) -> int: ...
