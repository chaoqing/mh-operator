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

# Stubs for namespace: Agilent.MSAcquisition.CustomizeFolder

class AgtCustomizeFolder(
    Agilent.MSAcquisition.CustomizeFolder.IAgtCustomizeFolder
):  # Class
    def __init__(self) -> None: ...

class IAgtCustomizeFolder(object):  # Interface
    def SetMassHunterDataFolderIcon(self, sFolderPath: str) -> None: ...
    def SetFolderIcon(
        self, sFolderPath: str, sResourcePath: str, iIconIndex: int
    ) -> None: ...
