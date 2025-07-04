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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.Utils

class CultureItem:  # Class
    def __init__(self, name: str) -> None: ...

    Culture: System.Globalization.CultureInfo  # readonly
    DisplayName: str  # readonly
    Name: str  # readonly

    @staticmethod
    def GetSystemItems() -> (
        List[Agilent.MassHunter.Quantitative.Startup.Edit.Utils.CultureItem]
    ): ...
