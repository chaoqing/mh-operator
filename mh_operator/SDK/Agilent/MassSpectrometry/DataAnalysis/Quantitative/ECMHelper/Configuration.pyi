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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.Configuration

class ColumnWidthItem:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, column: str, width: float) -> None: ...

    Column: str
    Width: float

class ColumnWidths:  # Class
    def __init__(self) -> None: ...
    def __getitem__(self, name: str) -> Optional[float]: ...
    def __setitem__(self, name: str, value_: Optional[float]) -> None: ...
    Widths: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.Configuration.ColumnWidthItem
    ]

class Configuration:  # Class
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.Configuration.Configuration
    )  # static # readonly
    UserSettings: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.Configuration.UserSettings
    )  # readonly

    @staticmethod
    def Cleanup() -> None: ...

class UserSettings(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationElementSectionBase
):  # Class
    def __init__(self) -> None: ...

    FileListColumnWidths: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.Configuration.ColumnWidths
    )
    LastFileDialogSize: Optional[System.Windows.Size]
    LastFolder: str
