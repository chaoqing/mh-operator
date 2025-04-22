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

from .PlotControl import GridPlotContent, GridPlotPane, IPlotSeries, PlotMode, Range
from .ToolbarWPF.ToolManager import IToolManager, ToolManagerBase
from .UIModel import ICalibrationAtAGlanceWindow

# Stubs for namespace: Agilent.MassHunter.Quantitative.CalibrationCurveAtAGlance

class GridPlotContent(
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.IInputElement,
    System.Windows.Markup.IQueryAmbient,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Controls.Primitives.IScrollInfo,
    System.Windows.Markup.IHaveResources,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IFrameworkInputElement,
):  # Class
    def __init__(self) -> None: ...
    def Initialize(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...
    def GetAutoScaleRange(self, pane: GridPlotPane, vertical: bool) -> Range: ...
    def Uninitialize(self) -> None: ...
    def GetSelectedTargetCompounds(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TargetCompoundRowId
    ]: ...
    def SetDimension(self, rows: int, columns: int) -> None: ...

class MainWindow(
    System.Windows.Markup.IAddChild,
    Infragistics.Windows.Ribbon.XamRibbonWindow,
    System.Windows.Markup.IHaveResources,
    System.Windows.IInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.IFrameworkInputElement,
    Infragistics.Windows.Ribbon.IRibbonWindow,
    System.Windows.Media.Composition.DUCE.IResource,
    ICalibrationAtAGlanceWindow,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.IWindowService,
    System.Windows.Forms.IWin32Window,
):  # Class
    def __init__(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...

    ContainsFocus: bool  # readonly
    Handle: System.IntPtr  # readonly
    Location: System.Drawing.Point
    NumColumnsPerPage: int  # readonly
    NumRowsPerPage: int  # readonly
    Visible: bool  # readonly
    WindowState: System.Windows.Forms.FormWindowState

    def SetDimension(self, rows: int, columns: int) -> None: ...
    @staticmethod
    def GetInstance(
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> Agilent.MassHunter.Quantitative.CalibrationCurveAtAGlance.MainWindow: ...
    def InitializeComponent(self) -> None: ...
    def GetSelectedTargetCompounds(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TargetCompoundRowId
    ]: ...

class PlotSeries(IPlotSeries):  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow,
        ccf: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CalibrationCurveFit,
    ) -> None: ...

    CalibrationCurveFit: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CalibrationCurveFit
    )  # readonly
    CompoundName: str  # readonly
    CompoundRow: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    )  # readonly
    Count: int  # readonly
    Pen: System.Windows.Media.Pen  # readonly
    PlotMode: PlotMode  # readonly
    Visible: bool  # readonly

    def SetPane(self, pane: GridPlotPane) -> None: ...
    def GetPoint(self, index: int, x: float, y: float) -> None: ...
    def GetCompoundID(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.TargetCompoundRowId: ...

class ToolHandlerView(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolBeforeDropdownHandler,
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
        state: Any,
    ) -> None: ...

class ToolManager(
    ToolManagerBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    IToolManager,
):  # Class
    def __init__(
        self, ribbon: Infragistics.Windows.Ribbon.XamRibbon, uiState: Any
    ) -> None: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def RegisterScriptToolHandler(
        self, id: str, module: str, setState: str, execute: str
    ) -> None: ...
    @overload
    def GetToolCaption(
        self, id: str, culture: System.Globalization.CultureInfo
    ) -> str: ...
    @overload
    def GetToolCaption(self, id: str) -> str: ...
