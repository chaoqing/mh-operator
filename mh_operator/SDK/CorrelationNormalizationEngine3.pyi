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

from .Mathematics import RangeDouble, Regression

# Stubs for namespace: CorrelationNormalizationEngine3

class TimeShiftModeler:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def SafeConstructModel(
        initialModel: Regression,
        observations: Sequence[Regression.Observation],
        damping: float,
        modelApplicableRange: RangeDouble,
        degreeOfFreedom: int,
    ) -> Regression: ...
    @staticmethod
    def Model(
        modelApplicationRange: RangeDouble,
        observations: Sequence[Regression.Observation],
    ) -> Regression: ...
