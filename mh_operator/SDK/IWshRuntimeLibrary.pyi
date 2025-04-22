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

# Stubs for namespace: IWshRuntimeLibrary

class IWshShell(object):  # Interface
    ...

class IWshShell2(IWshRuntimeLibrary.IWshShell):  # Interface
    ...

class IWshShell3(
    IWshRuntimeLibrary.IWshShell2, IWshRuntimeLibrary.IWshShell
):  # Interface
    def CreateShortcut(self, PathLink: str) -> Any: ...

class IWshShortcut(object):  # Interface
    Arguments: str
    TargetPath: str

    def Save(self) -> None: ...

class WshShell(
    IWshRuntimeLibrary.IWshShell3,
    IWshRuntimeLibrary.IWshShell2,
    IWshRuntimeLibrary.IWshShell,
):  # Interface
    ...

class WshShortcut(IWshRuntimeLibrary.IWshShortcut):  # Interface
    ...
