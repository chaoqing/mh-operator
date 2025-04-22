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

from . import Data, Linq, Reflection, Runtime, Windows, util

# Stubs for namespace: System

class TypeExtensions:  # Class
    @staticmethod
    def AsType(type: System.Type) -> System.Type: ...
    @staticmethod
    def GetTypeInfo(type: System.Type) -> System.Type: ...
