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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Configurations

class ApplicationSettings(System.Configuration.ConfigurationSection):  # Class
    def __init__(self) -> None: ...

    AutoSortRows: int  # readonly
    CommandLog: str  # readonly
    CommandLogLanguage: str  # readonly
    DumpLogOnNormalExit: bool  # readonly
    ErrorReportingEmailAddress: str  # readonly
    ErrorReportingEnabled: bool  # readonly
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Configurations.ApplicationSettings
    )  # static # readonly
    MaxCompoundsToCopy: int  # readonly
    MaxVisibleSpectra: int  # readonly
    Multithreading: bool  # readonly
    PrecursorBinWidth: float  # readonly
    PrecursorFillColor: System.Drawing.Color  # readonly
    PrecursorLineColor: System.Drawing.Color  # readonly
    PrecursorSize: int  # readonly

class Config:  # Class
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Configurations.Config
    )  # static # readonly

    def Save(self) -> None: ...

class ConfigElement(System.Configuration.ConfigurationElement, Generic[T]):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, value_: T) -> None: ...

    Value: T

class Formats:  # Class
    Abundance: str
    AccurateMz: str
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Configurations.Formats
    )  # static # readonly
    def __getitem__(self, key: str) -> str: ...
    def __setitem__(self, key: str, value_: str) -> None: ...
    UnitMz: str

class UISettings(System.Configuration.ConfigurationSection):  # Class
    def __init__(self) -> None: ...

    DefaultVisibleColumns: str  # readonly
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Configurations.UISettings
    )  # static # readonly

class UserSettings(System.Configuration.ConfigurationSection):  # Class
    def __init__(self) -> None: ...

    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Configurations.UserSettings
    )  # static # readonly
