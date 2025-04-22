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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Tools

class ToolHandlerEdit(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
        objUiState: Any,
    ) -> None: ...
    def SetState(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
        objUiState: Any,
    ) -> None: ...

class ToolHandlerFile(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerTools(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
        objUiState: Any,
    ) -> None: ...
    def SetState(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
        objUiState: Any,
    ) -> None: ...

class ToolHandlerView(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...
