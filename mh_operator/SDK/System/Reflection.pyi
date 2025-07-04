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

# Stubs for namespace: System.Reflection

class RuntimeReflectionExtensions:  # Class
    @staticmethod
    def GetRuntimeMethods(
        type: System.Type,
    ) -> Iterable[System.Reflection.MethodInfo]: ...
    @staticmethod
    def GetRuntimeBaseDefinition(
        method: System.Reflection.MethodInfo,
    ) -> System.Reflection.MethodInfo: ...
