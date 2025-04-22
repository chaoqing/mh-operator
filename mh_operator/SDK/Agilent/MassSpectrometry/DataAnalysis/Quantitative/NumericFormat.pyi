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

from . import INumericCustomFormat

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.NumericFormat

class CustomFormatBase:  # Class
    ...

class SignificantFiguresFormat(
    System.IFormatProvider,
    INumericCustomFormat,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.NumericFormat.CustomFormatBase,
    System.ICustomFormatter,
):  # Class
    @overload
    def __init__(self, digits: int) -> None: ...
    @overload
    def __init__(self, digits: int, provider: System.IFormatProvider) -> None: ...

    Digits: int
    FormatProvider: System.IFormatProvider  # readonly
    FormatString: str  # readonly

    def GetFormat(self, formatType: System.Type) -> Any: ...
    def Format(
        self, format: str, arg: Any, formatProvider: System.IFormatProvider
    ) -> str: ...
