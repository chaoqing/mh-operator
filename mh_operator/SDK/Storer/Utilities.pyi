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

# Stubs for namespace: Storer.Utilities

class xDirectory:  # Class
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def Copy(SourcePath: str, DestinationPath: str, Overwrite: bool) -> None: ...
    @overload
    @staticmethod
    def Copy(
        SourcePath: str, DestinationPath: str, SourceFileFilter: str, Overwrite: bool
    ) -> None: ...
    @overload
    @staticmethod
    def Copy(
        SourcePath: str,
        DestinationPath: str,
        SourceDirectoryFilter: str,
        SourceFileFilter: str,
        Overwrite: bool,
    ) -> None: ...
    @overload
    @staticmethod
    def Copy(
        SourceDirectory: System.IO.DirectoryInfo,
        DestinationDirectory: System.IO.DirectoryInfo,
        Overwrite: bool,
    ) -> None: ...
    @overload
    @staticmethod
    def Copy(
        SourceDirectory: System.IO.DirectoryInfo,
        DestinationDirectory: System.IO.DirectoryInfo,
        SourceFileFilter: str,
        Overwrite: bool,
    ) -> None: ...
    @overload
    @staticmethod
    def Copy(
        SourceDirectory: System.IO.DirectoryInfo,
        DestinationDirectory: System.IO.DirectoryInfo,
        SourceDirectoryFilter: str,
        SourceFileFilter: str,
        Overwrite: bool,
    ) -> None: ...
