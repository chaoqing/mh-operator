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

# Stubs for namespace: Agilent.MassHunter.Quantitative.QuantWPF.Tools

class CagToolManager(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.ToolManagerBase,
):  # Class
    def __init__(
        self,
        ribbon: Infragistics.Windows.Ribbon.XamRibbon,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...
    def RegisterScriptToolHandler(
        self, id: str, module: str, setState: str, execute: str
    ) -> None: ...
    def SetToolState(
        self, state: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState
    ) -> None: ...
    def GetImage(self, image: str) -> System.Windows.Media.Imaging.BitmapSource: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    @overload
    def GetToolCaption(self, id: str) -> str: ...
    @overload
    def GetToolCaption(
        self, id: str, culture: System.Globalization.CultureInfo
    ) -> str: ...

class CiwToolManager(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.ToolManagerBase,
):  # Class
    def __init__(
        self,
        ribbon: Infragistics.Windows.Ribbon.XamRibbon,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...
    @overload
    def GetToolCaption(self, id: str) -> str: ...
    @overload
    def GetToolCaption(
        self, id: str, culture: System.Globalization.CultureInfo
    ) -> str: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def RegisterScriptToolHandler(
        self, tool: str, module: str, setState: str, execute: str
    ) -> None: ...
    def GetImage(self, image: str) -> System.Windows.Media.Imaging.BitmapSource: ...

class ToolsUtil:  # Class
    @staticmethod
    def CheckWpfTools() -> None: ...
