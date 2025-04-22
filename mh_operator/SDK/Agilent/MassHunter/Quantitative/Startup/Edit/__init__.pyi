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

from . import (
    BatchTable,
    ColumnLabels,
    Configuration,
    General,
    MainView,
    Manage,
    Outliers,
    Ribbon,
    SampleType,
    Utils,
    ViewModel,
)

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit

class App(
    System.Windows.Application,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    @staticmethod
    def Main() -> None: ...

class CommandLine:  # Class
    def __init__(self) -> None: ...

    Culture: str

class EditException(
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
