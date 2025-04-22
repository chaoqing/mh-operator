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

from . import SampleDataNavigator, TuneEvaluationMethod, TuneEvaluationResult

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.UI

class CommandLine:  # Class
    def __init__(self) -> None: ...

    MethodPath: str
    ReportPath: str
    SamplePath: str
    Silent: bool
    StatusPath: str

class DefaultEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.DefaultEventManipulatorBase,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.EventManipulating.EventContext,
        mainForm: Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.UI.MainForm,
    ) -> None: ...
    def OnMouseDoubleClick(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseDown(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...

class MainForm(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

    EXT_DATA: str = ...  # static # readonly
    EXT_METHOD: str = ...  # static # readonly
    MZEXTRACTIONWINDOW_LEFT: float = ...  # static # readonly
    MZEXTRACTIONWINDOW_RIGHT: float = ...  # static # readonly
    TUNE_HELP_TOPICID: int = ...  # static # readonly
    UnifiedMethod_File: str = ...  # static # readonly
    UnifiedMethod_SubFolders: str = ...  # static # readonly

    DataNavigator: SampleDataNavigator
    MassHunterDir: str  # readonly
    Method: TuneEvaluationMethod
    Result: TuneEvaluationResult
    SamplePath: str
    SpectrumPane: Agilent.MassSpectrometry.GUI.Plot.Pane  # readonly
    SpectrumPlotControl: (
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.UI.SpectrumPlotControl
    )  # readonly
    TICPane: Agilent.MassSpectrometry.GUI.Plot.Pane  # readonly
    TICPlotControl: (
        Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.UI.TICPlotControl
    )  # readonly
    UnifiedMethodFolder: str

    def ShowExceptionMessage(self, ex: System.Exception) -> None: ...
    @staticmethod
    def ShowError(msg: str) -> None: ...
    def ClearResults(self) -> None: ...
    def RunTuneEvaluation(self) -> None: ...

class MarkerData(Agilent.MassSpectrometry.GUI.Plot.IMarkerData):  # Class
    def __init__(
        self, x: float, pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> None: ...

class MethodForm(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(
        self,
        method: TuneEvaluationMethod,
        mainForm: Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.UI.MainForm,
    ) -> None: ...

    Method: TuneEvaluationMethod

class PlotData(
    System.IDisposable, Agilent.MassSpectrometry.GUI.Plot.IPlotData
):  # Class
    def __init__(self) -> None: ...

    NextColor: System.Drawing.Color  # readonly

    def GetPointCount(self, series: int) -> int: ...
    def GetSeriesCount(self) -> int: ...
    def DisplaySeries(self, series: int) -> bool: ...
    def RemoveSeries(self, index: int) -> None: ...
    def GetPoint(self, series: int, pointIndex: int, x: float, y: float) -> None: ...
    def GetYRange(self, minY: float, maxY: float) -> None: ...
    def AddSeries(
        self,
        color: System.Drawing.Color,
        mode: Agilent.MassSpectrometry.GUI.Plot.PlotModes,
        points: List[System.Drawing.PointF],
        title: str,
    ) -> None: ...
    def GetXRange(self, minX: float, maxX: float) -> None: ...
    def Dispose(self) -> None: ...
    def GetSeriesLineStyle(
        self,
        series: int,
        mode: Agilent.MassSpectrometry.GUI.Plot.PlotModes,
        color: System.Drawing.Color,
        style: System.Drawing.Drawing2D.DashStyle,
        width: int,
    ) -> None: ...

class SpectrumPlotControl(
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

class SpectrumPlotData(
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.IPeakData,
    Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.UI.PlotData,
    Agilent.MassSpectrometry.GUI.Plot.IPlotData,
):  # Class
    def __init__(self, xArray: List[float], yArray: List[float]) -> None: ...
    def Dispose(self) -> None: ...

class TICPlotControl(
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

class TICPlotData(
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.IPeakData,
    Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.UI.PlotData,
    Agilent.MassSpectrometry.GUI.Plot.IPlotData,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, dataNavigator: SampleDataNavigator) -> None: ...

    PeakList: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.IChromPeak
    ]

class TuneEvalMethodFileDialog(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogBase,
):  # Class
    def __init__(
        self,
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogType,
        extFolderName: str,
    ) -> None: ...

class TuneEvaluationReport:  # Class
    @overload
    def __init__(
        self,
        mainForm: Agilent.MassSpectrometry.DataAnalysis.TuneEvaluation.UI.MainForm,
        result: TuneEvaluationResult,
    ) -> None: ...
    @overload
    def __init__(
        self, samplePath: str, unifiedTuneMathodPath: str, result: TuneEvaluationResult
    ) -> None: ...

    PreferredPageSize: str

    def Process(self, file: str) -> None: ...
    def Dispose(self) -> None: ...

class Utils:  # Class
    @staticmethod
    def RegisterFont(name: str) -> None: ...
    @staticmethod
    def GetFont(name: str) -> iTextSharp.text.Font: ...
    @staticmethod
    def GetDefaultPageSize() -> iTextSharp.text.Rectangle: ...
    @staticmethod
    def GetDefaultFontNameByCulture(ci: System.Globalization.CultureInfo) -> str: ...
    @staticmethod
    def GetPageSize(name: str) -> iTextSharp.text.Rectangle: ...
