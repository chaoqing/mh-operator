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

from . import IApplicationServiceBase

# Stubs for namespace: Agilent.MassHunter.Quantitative.ApplicationServices.Quant

class IQuantitativeAnalysis(IApplicationServiceBase, System.IDisposable):  # Interface
    def ShowWindow(self) -> None: ...
    def RunScript(self, scriptFile: str) -> None: ...
