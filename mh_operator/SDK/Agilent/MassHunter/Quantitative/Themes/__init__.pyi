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

from . import Behavior, Microsoft, Wizard

# Stubs for namespace: Agilent.MassHunter.Quantitative.Themes

class IntGreaterThanConverter(System.Windows.Data.IValueConverter):  # Class
    def __init__(self) -> None: ...

    Instance: System.Windows.Data.IValueConverter  # static # readonly

    def ConvertBack(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...
    def Convert(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...

class LocalToFontFamilyConverter(System.Windows.Data.IValueConverter):  # Class
    def __init__(self) -> None: ...
    def ConvertBack(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...
    def Convert(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...

class TooltipTextToWidthConverter(System.Windows.Data.IMultiValueConverter):  # Class
    def __init__(self) -> None: ...
    def ConvertBack(
        self,
        value_: Any,
        targetTypes: List[System.Type],
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> List[Any]: ...
    def Convert(
        self,
        values: List[Any],
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...

class Utils:  # Class
    @staticmethod
    def SetupCulture(ci: System.Globalization.CultureInfo) -> None: ...
    @staticmethod
    def SetupDataGridView(dataGridView: System.Windows.Forms.DataGridView) -> None: ...
