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

# Stubs for namespace: OpenLABTranslator

class MassHunterToExcalibur:  # Class
    def __init__(self) -> None: ...
    def CreateMsData(self, dxFileName: str, massHunterFileName: str) -> None: ...

class OpenLABMSTranslator:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def TranslateData(args: List[str]) -> None: ...

class Program:  # Class
    def __init__(self) -> None: ...
