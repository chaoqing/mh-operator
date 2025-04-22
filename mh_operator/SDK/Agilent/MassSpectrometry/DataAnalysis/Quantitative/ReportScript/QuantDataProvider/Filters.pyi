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
from . import IDataFilter

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.Filters

class SimpleColumnFilter(Generic[T], IDataFilter):  # Class
    def __init__(self, name: str, values: List[T]) -> None: ...

    FilterString: str  # readonly
    SupportsFilterString: bool  # readonly

    def Match(self, row: System.Data.DataRow) -> bool: ...
