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

# Stubs for namespace: Agilent.MassHunter.UnknownsAnalysis.ComponentsAtAGlance

class GridPlotContent(
    System.Windows.Controls.Primitives.IScrollInfo,
    Agilent.MassHunter.Quantitative.PlotControl.GridPlotContent,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def DrawPane(
        self,
        drawingContext: System.Windows.Media.DrawingContext,
        rect: System.Windows.Rect,
        pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane,
        dataSource: Any,
    ) -> None: ...
    def Initialize(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState,
    ) -> None: ...
    def AutoScaleLinedAxesX(self) -> None: ...
    def GetAutoScaleRange(
        self,
        pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane,
        vertical: bool,
    ) -> Agilent.MassHunter.Quantitative.PlotControl.Range: ...
    def Uninitialize(self) -> None: ...

class MainWindow(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IWindowService,
    Infragistics.Windows.Ribbon.IRibbonWindow,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Animation.IAnimatable,
    System.ComponentModel.ISupportInitialize,
    Infragistics.Windows.Ribbon.XamRibbonWindow,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...

    GridPlotContent: (
        Agilent.MassHunter.UnknownsAnalysis.ComponentsAtAGlance.GridPlotContent
    )  # readonly

    def Initialize(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState,
    ) -> None: ...
    def InitializeComponent(self) -> None: ...

class PlotData(
    List[Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries],
    Iterable[Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries],
    Sequence[Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries],
    Iterable[Any],
    Sequence[Any],
    List[Any],
    System.Collections.Generic.List[
        Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries
    ],
):  # Class
    def __init__(
        self,
        chid: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentHitID,
    ) -> None: ...

    Initialized: bool  # readonly
    Title: str  # readonly

    def InitializeChromatogram(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState,
        brushes: List[System.Windows.Media.Brush],
    ) -> None: ...
    def InitializeSpectrum(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState,
        brushes: List[System.Windows.Media.Brush],
    ) -> None: ...

class PlotSeries(
    Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries,
    Agilent.MassHunter.Quantitative.PlotControl.IPeaks,
):  # Class
    def __init__(
        self, xarr: List[float], yarr: List[float], spectrum: bool
    ) -> None: ...

    Count: int  # readonly
    IsSpectrum: bool  # readonly
    PeakCount: int  # readonly
    PeakLabelFormat: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat
    )
    PeakLabelsVisible: bool  # readonly
    Pen: System.Windows.Media.Pen
    PlotMode: Agilent.MassHunter.Quantitative.PlotControl.PlotMode  # readonly
    Title: str
    Visible: bool

    def GetPeakBaselinePen(self, index: int) -> System.Windows.Media.Pen: ...
    def GetPeakLabel(self, index: int) -> str: ...
    def GetPeak(self, index: int) -> System.Windows.Point: ...
    def GetPoint(self, index: int, x: float, y: float) -> None: ...
    def GetPeakLabelBrush(self, index: int) -> System.Windows.Media.Brush: ...
    def GetPeakFillBrush(self, index: int) -> System.Windows.Media.Brush: ...
    def GetBaseline(
        self, index: int, start: System.Windows.Point, end: System.Windows.Point
    ) -> None: ...

class ToolManager(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.ToolManagerBase,
):  # Class
    def __init__(
        self,
        ribbon: Infragistics.Windows.Ribbon.XamRibbon,
        uiContext: Agilent.MassHunter.UnknownsAnalysis.ComponentsAtAGlance.UIContext,
    ) -> None: ...
    def RegisterScriptToolHandler(
        self, id: str, module: str, setState: str, execute: str
    ) -> None: ...
    def SetToolState(
        self, tool: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState
    ) -> None: ...
    def Execute(
        self, tool: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState
    ) -> None: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    @overload
    def GetToolCaption(self, id: str) -> str: ...
    @overload
    def GetToolCaption(
        self, id: str, culture: System.Globalization.CultureInfo
    ) -> str: ...

class UIContext:  # Class
    def __init__(
        self,
        mainWindow: Agilent.MassHunter.UnknownsAnalysis.ComponentsAtAGlance.MainWindow,
    ) -> None: ...

    MainWindow: (
        Agilent.MassHunter.UnknownsAnalysis.ComponentsAtAGlance.MainWindow
    )  # readonly
