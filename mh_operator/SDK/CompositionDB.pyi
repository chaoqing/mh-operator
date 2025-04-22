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

# Stubs for namespace: CompositionDB

class CompositionsStorage:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def GetMasses(neutralAndNaturalOnly: bool) -> List[float]: ...
    @staticmethod
    def Open() -> None: ...
    @staticmethod
    def FormulaExists(formula: str) -> bool: ...
    @staticmethod
    def GetFormulaCount(neutralAndNaturalOnly: bool) -> int: ...
    @staticmethod
    def Close() -> None: ...
    @staticmethod
    def GetIsomerAndTautomerInfo(
        formula: str, isomerCount: int, tautomerGroupCount: int
    ) -> None: ...
    @staticmethod
    def GetFormulaMasses(neutralAndNaturalOnly: bool) -> Dict[str, float]: ...
    @staticmethod
    def InsertFormula(
        formula: str, mass: float, isomerCount: int, tautomerGroupCount: int
    ) -> None: ...
