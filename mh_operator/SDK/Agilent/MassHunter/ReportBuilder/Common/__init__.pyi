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

from . import Engine
from .Template import IColor, IFont, ILength, ILine

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.Common

class ColorComparer(System.Collections.Generic.IEqualityComparer[IColor]):  # Class
    def __init__(self) -> None: ...
    def GetHashCode(self, obj: IColor) -> int: ...
    def Equals(self, x: IColor, y: IColor) -> bool: ...

class FontComparer(System.Collections.Generic.IEqualityComparer[IFont]):  # Class
    def __init__(self) -> None: ...
    def GetHashCode(self, obj: IFont) -> int: ...
    def Equals(self, x: IFont, y: IFont) -> bool: ...

class LengthComparer(System.Collections.Generic.IEqualityComparer[ILength]):  # Class
    def __init__(self) -> None: ...
    def GetHashCode(self, obj: ILength) -> int: ...
    def Equals(self, x: ILength, y: ILength) -> bool: ...

class LineComparer(System.Collections.Generic.IEqualityComparer[ILine]):  # Class
    def __init__(self) -> None: ...
    def GetHashCode(self, obj: ILine) -> int: ...
    def Equals(self, x: ILine, y: ILine) -> bool: ...

class ReportBuilderAbortException(
    System.Runtime.InteropServices._Exception,
    Agilent.MassHunter.ReportBuilder.Common.ReportBuilderException,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class ReportBuilderException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...
    @overload
    def __init__(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class ReportBuilderPreviewAbortException(
    System.Runtime.InteropServices._Exception,
    Agilent.MassHunter.ReportBuilder.Common.ReportBuilderException,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...
    @overload
    def __init__(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...
