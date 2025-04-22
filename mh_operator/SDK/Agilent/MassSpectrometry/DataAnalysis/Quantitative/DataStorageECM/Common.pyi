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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DataStorageECM.Common

class Command:  # Class
    def __init__(self) -> None: ...

    Group: str
    Name: str
    RequireReason: bool
    RequireUserValidation: bool

class CommandGroup:  # Class
    def __init__(self) -> None: ...

    Commands: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DataStorageECM.Common.Command
    ]
    Name: str
    PrivilegeID: int

class CommandGroups:  # Class
    def __init__(self) -> None: ...

    CurrentSchemaVersion: int = ...  # static # readonly

    Groups: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DataStorageECM.Common.CommandGroup
    ]
    SchemaVersion: int

class IViewModel(object):  # Interface
    ...

class Role:  # Class
    def __init__(self) -> None: ...

    PrivilegePrefix: str = ...  # static # readonly

    Name: str  # readonly
    Privileges: Iterable[str]  # readonly

    def HasPriviledge(self, name: str) -> bool: ...
    def SetPriviledge(self, name: str, value_: bool) -> None: ...
