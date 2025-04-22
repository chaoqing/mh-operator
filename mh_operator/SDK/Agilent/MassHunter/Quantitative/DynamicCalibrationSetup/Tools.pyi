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

from .ScriptIF import IUIState

# Stubs for namespace: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Tools

class FileToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        objUiState: Any,
    ) -> None: ...
    def SetState(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        objUiState: Any,
    ) -> None: ...

class ToolHandlerIonGroupsView(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        objUiState: Any,
    ) -> None: ...
    def SetState(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        objUiState: Any,
    ) -> None: ...

class ToolHandlerMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        objUiState: Any,
    ) -> None: ...
    def SetState(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        objUiState: Any,
    ) -> None: ...

class ToolManager(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.ToolManagerBase,
):  # Class
    def __init__(
        self, ribbon: Infragistics.Windows.Ribbon.XamRibbon, uiState: IUIState
    ) -> None: ...

    _UIState: IUIState  # readonly

    def RegisterScriptToolHandler(
        self, id: str, module: str, setState: str, execute: str
    ) -> None: ...
    def ApplicationMenu2010SelectedTabItemChanged(self) -> None: ...
    def GetApplicationMenu2010Content(self, category: str, id: str) -> Any: ...
    def ApplicationMenu2010Closed(self) -> None: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def GetToolCaption(self, id: str) -> str: ...
