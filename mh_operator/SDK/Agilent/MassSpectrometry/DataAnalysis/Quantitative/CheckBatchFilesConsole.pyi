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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFilesConsole

class CommandLine(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    CsvFile: str
    Culture: str
    Folders: List[str]
    Help: bool
    NoLogo: bool
    OutFile: str
    Recursive: bool
    TabDelimitedFile: str
    XmlFile: str

    def Dispose(self) -> None: ...
