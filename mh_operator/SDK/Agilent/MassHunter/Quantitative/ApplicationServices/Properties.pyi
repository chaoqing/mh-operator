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

# Stubs for namespace: Agilent.MassHunter.Quantitative.ApplicationServices.Properties

class Resources:  # Class
    Culture: System.Globalization.CultureInfo  # static
    Exp_CannotFindType: str  # static # readonly
    Exp_CannotStartServiceApplication: str  # static # readonly
    Exp_TypeCannotFoundInConfiguration: str  # static # readonly
    ResourceManager: System.Resources.ResourceManager  # static # readonly
