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

import Agilent
import System

from .Interfaces import DataChangeLevel

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Utilities

class Constants:  # Class
    InjectionMetadataCustomField: str = ...  # static # readonly
    OriginalPackagingModeCustomField: str = ...  # static # readonly

class ProcessingTransaction:  # Class
    def __init__(self, docId: System.Guid) -> None: ...

    IsActive: bool  # readonly

    def Open(self) -> None: ...
    def TryOpen(self) -> bool: ...
    def Commit(self, dataChangeLevel: DataChangeLevel) -> None: ...
    def TryCommit(self, dataChangeLevel: DataChangeLevel) -> None: ...
