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

# Stubs for namespace: Definitions

class IMass_TimeSeparatedObject(object):  # Interface
    Abundance: float  # readonly
    Height: float  # readonly
    ID: str  # readonly
    Mass: float  # readonly
    SeparationTime: float  # readonly

class UnitConversion:  # Class
    def __init__(self) -> None: ...

    RetentionTime: float = ...  # static # readonly

    UseOldVoluemScaling: bool  # static
    Volume: float  # static # readonly
