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

from .Compliance import ILogonParameters

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Report

class ReportGeneratorCommandLine(ILogonParameters):  # Class
    def __init__(self) -> None: ...

    AccountName: str
    BatchFileName: str
    BatchPath: str
    CompoundIds: str
    ConnectionTicket: str
    Domain: str
    EncryptedPassword: str
    FixedGraphicsFile: str
    Help: bool
    InstrumentType: str
    Local: bool
    NoGraphics: bool
    NoLogo: bool
    OutputExcelFile: str
    OutputPath: str
    Password: str
    Printer: str
    PublishFormat: str
    Queue: bool
    ReportFileName: str
    SampleIds: str
    ScriptFile: str
    Server: str
    SettingsFile: str
    SingleSampleMode: bool
    Template: str
    User: str
    _Password: System.Security.SecureString  # readonly

    def Run(self) -> int: ...
