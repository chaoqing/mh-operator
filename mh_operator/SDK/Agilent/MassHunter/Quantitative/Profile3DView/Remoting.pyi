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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Profile3DView.Remoting

class ISingletonServer(object):  # Interface
    def Open(self, args: List[str]) -> None: ...
    def Ready(self) -> None: ...

class SingletonServer(
    Agilent.MassHunter.Quantitative.Profile3DView.Remoting.ISingletonServer
):  # Class
    def __init__(self) -> None: ...
    def Open(self, args: List[str]) -> None: ...
    def Ready(self) -> None: ...
