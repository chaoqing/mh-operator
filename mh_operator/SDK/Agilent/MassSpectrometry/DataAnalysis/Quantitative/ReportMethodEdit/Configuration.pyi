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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Configuration

class ApplicationSettings(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationElementSectionBase
):  # Class
    def __init__(self) -> None: ...

    DumpLogOnNormalExit: bool  # readonly
    ErrorReportingEmailAddress: str  # readonly
    ErrorReportingEnabled: bool  # readonly
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Configuration.ApplicationSettings
    )  # static # readonly
    PDFCultures: List[str]  # readonly
    PDFPageSizes: List[str]  # readonly

class ColumnWidthElement(System.Configuration.ConfigurationElement):  # Class
    def __init__(self) -> None: ...

    Name: str
    Width: int

class ColumnWidthElementCollection(
    Iterable[Any], System.Configuration.ConfigurationElementCollection, Sequence[Any]
):  # Class
    def __init__(self) -> None: ...
    def GetWidth(self, name: str, defaultValue: int) -> int: ...
    def SetWidth(self, name: str, value_: int) -> None: ...

class Config:  # Class
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Configuration.Config
    )  # static # readonly

class UISettings(System.Configuration.ConfigurationSection):  # Class
    def __init__(self) -> None: ...

    CompopundGraphicsRangeColumnWidths: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Configuration.ColumnWidthElementCollection
    )  # readonly
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Configuration.UISettings
    )  # static # readonly
    TemplatesColumnWidths: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Configuration.ColumnWidthElementCollection
    )  # readonly
