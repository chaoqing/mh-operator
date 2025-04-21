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

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.Common.Engine

class IGraphicsXps(object):  # Interface
    def Add(self, stream: System.IO.Stream) -> None: ...
