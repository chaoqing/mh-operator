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

from . import DataNavigator
from .Grid import IPlottableGrid
from .Toolbar import IToolbarsManager

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MetricsPlot

class MetricsPlotControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.IWin32Window,
    Agilent.MassHunter.Quantitative.UIModel.IMetricsPlotPane,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
):  # Class
    def __init__(self) -> None: ...

    PlotControl: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MetricsPlot.PlotControl
    )  # readonly
    PlottableGrid: Agilent.MassHunter.Quantitative.UIModel.IPlottableGrid  # readonly
    ShowAverageStdDevLines: bool

    def GetActivePaneData(
        self,
    ) -> Agilent.MassHunter.Quantitative.UIModel.IMetricsPlotData: ...

class PlotControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    Agilent.MassSpectrometry.GUI.Plot.PlotControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

    DataNavigator: DataNavigator
    PlottableGrid: IPlottableGrid
    ShowAverageStdDevLines: bool
    ToolbarsManager: IToolbarsManager

    def GetAutoScaleRangeX(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetActivePaneData(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.MetricsPlot.PlotData: ...

class PlotData(
    Agilent.MassSpectrometry.GUI.Plot.IPeakData,
    Agilent.MassHunter.Quantitative.UIModel.IMetricsPlotData,
    Agilent.MassSpectrometry.GUI.Plot.IPlotData,
):  # Class
    AutoScale: bool
    NextColor: System.Drawing.Color  # readonly

    def AutoScaleY(self) -> None: ...
    def Clear(self) -> None: ...
    def AddSeries(self, columnName: str, color: System.Drawing.Color) -> None: ...
    def AutoScaleX(self) -> None: ...
