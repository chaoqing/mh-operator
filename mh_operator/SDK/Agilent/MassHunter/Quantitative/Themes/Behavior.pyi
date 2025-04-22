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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Themes.Behavior

class DataGridBehavior:  # Class
    FullRowSelectProperty: System.Windows.DependencyProperty  # static # readonly

    @staticmethod
    def SetFullRowSelect(
        grid: System.Windows.Controls.DataGrid, value_: bool
    ) -> None: ...
    @staticmethod
    def GetFullRowSelect(grid: System.Windows.Controls.DataGrid) -> bool: ...
