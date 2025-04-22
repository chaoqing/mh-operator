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

# Stubs for namespace: Dennany.Diagnostics

class CustomTraceListener(
    System.IDisposable, System.Diagnostics.TextWriterTraceListener
):  # Class
    @overload
    def __init__(self, stream: System.IO.Stream, name: str) -> None: ...
    @overload
    def __init__(self, stream: System.IO.Stream) -> None: ...
    @overload
    def __init__(self, fileName: str, name: str) -> None: ...
    @overload
    def __init__(self, fileName: str) -> None: ...
    @overload
    def __init__(self, writer: System.IO.TextWriter, name: str) -> None: ...
    @overload
    def __init__(self, writer: System.IO.TextWriter) -> None: ...
    def Write(self, message: str) -> None: ...
    def WriteLine(self, message: str) -> None: ...
