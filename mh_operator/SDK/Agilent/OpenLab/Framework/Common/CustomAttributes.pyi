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

# Stubs for namespace: Agilent.OpenLab.Framework.Common.CustomAttributes

class SetpointsBindingAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, setpointContainerType: System.Type) -> None: ...

    SetpointContainerType: System.Type  # readonly

class UIBindingAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    @overload
    def __init__(self, transformationUIType: System.Type) -> None: ...
    @overload
    def __init__(
        self, transformationUIType: System.Type, displayOrder: int
    ) -> None: ...

    DisplayOrder: int  # readonly
    TransformationUIType: System.Type  # readonly
