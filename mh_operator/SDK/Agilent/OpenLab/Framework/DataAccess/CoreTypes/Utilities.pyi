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
from . import TimeUnit, XUnit

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Utilities

class ObjectXmlSerializer(Generic[T]):  # Class
    def __init__(self) -> None: ...
    def Deserialize(self, serializedObject: str) -> T: ...
    def Serialize(self, objectToSerialize: T) -> str: ...

class TimeConverter:  # Class
    @staticmethod
    def ConvertValue(
        time: float, sourceUnit: TimeUnit, targetUnit: TimeUnit
    ) -> float: ...
    @overload
    @staticmethod
    def ConvertUnit(xunit: XUnit) -> TimeUnit: ...
    @overload
    @staticmethod
    def ConvertUnit(timeUnit: TimeUnit) -> XUnit: ...
