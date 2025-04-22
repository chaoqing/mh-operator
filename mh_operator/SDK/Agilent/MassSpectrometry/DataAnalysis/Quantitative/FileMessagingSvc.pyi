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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FileMessagingSvc

class ProjectInstaller(
    System.Configuration.Install.Installer,
    System.IDisposable,
    System.ComponentModel.IComponent,
):  # Class
    def __init__(self) -> None: ...

    ServiceName: str  # static # readonly
