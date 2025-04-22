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

from . import Definitions, ToolManager, ToolState

# Stubs for namespace: Agilent.MassHunter.Quantitative.ToolbarWPF

class ImageConverter(
    System.Windows.DependencyObject, System.Windows.Data.IValueConverter
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, color: System.Windows.Media.Color) -> None: ...

    ColorProperty: System.Windows.DependencyProperty  # static # readonly

    Color: System.Windows.Media.Color

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
