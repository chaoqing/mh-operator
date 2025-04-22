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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.Configuration

class UserConfiguration:  # Class
    def __init__(self) -> None: ...

    s_instance: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Configuration.UserConfiguration
    )  # static

    Instance: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Configuration.UserConfiguration
    )  # static # readonly
    LastInstrumentType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType
    )
