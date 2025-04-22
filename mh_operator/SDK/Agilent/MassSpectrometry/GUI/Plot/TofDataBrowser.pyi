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

from . import (
    DefaultEventManipulatorBase,
    IMarkerData,
    IPeakData,
    IPlotData,
    IPlotDataAxisAssoc,
    PlotModes,
)

# Stubs for namespace: Agilent.MassSpectrometry.GUI.Plot.TofDataBrowser

class ChromPlotData(
    Agilent.MassSpectrometry.GUI.Plot.TofDataBrowser.PlotData,
    IPeakData,
    System.IDisposable,
    IPlotDataAxisAssoc,
    IPlotData,
):  # Class
    def __init__(self) -> None: ...

    PeakList: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.IChromPeak
    ]

    def Dispose(self) -> None: ...

class DefaultEventManipulator(
    DefaultEventManipulatorBase,
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
):  # Class
    def __init__(
        self, context: Agilent.MassSpectrometry.EventManipulating.EventContext
    ) -> None: ...
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseMove(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...

class FDDialog(
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

class FDProgressDlg(
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
        parent: Agilent.MassSpectrometry.GUI.Plot.TofDataBrowser.MainForm,
        totalNumScanRecords: int,
    ) -> None: ...

class GoToDialog(
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

    Rt: float  # readonly
    ScanIndex: int  # readonly
    UseRT: bool  # readonly

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

    MassCalOptions: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.MassCalibrationOptions
    )  # readonly
    StatusText: str

    @staticmethod
    def ShowError(msg: str) -> None: ...
    @staticmethod
    def ShowMessage(msg: str) -> None: ...

class OptionsDialog(
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
        self, mainForm: Agilent.MassSpectrometry.GUI.Plot.TofDataBrowser.MainForm
    ) -> None: ...

    ApplyMassStepFiltering: bool
    CentroidType: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidType
    DoMassCal: bool
    InterpolationType: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.InterpolationType
    )
    MaxRefMzDelta: float
    MinFoundRefMZsForTradFit: int
    MinFoundRefMZsPerRange: int
    ReferenceMassFilePath: str
    ResolveShoulderPeaks: bool
    WriteApexList: bool
    WriteHistogram: bool
    WriteMassCalResults: bool
    WritePeakShapes: bool
    WriteRefMzResiduals: bool

class PlotData(System.IDisposable, IPlotData, IPlotDataAxisAssoc):  # Class
    def __init__(self) -> None: ...
    def GetPointCount(self, series: int) -> int: ...
    def GetSeriesCount(self) -> int: ...
    def DisplaySeries(self, series: int) -> bool: ...
    def RemoveSeries(self, index: int) -> None: ...
    def GetPoint(self, series: int, pointIndex: int, x: float, y: float) -> None: ...
    def GetYRange(self, minY: float, maxY: float) -> None: ...
    def AddSeries(
        self,
        color: System.Drawing.Color,
        mode: PlotModes,
        points: List[System.Drawing.PointF],
    ) -> None: ...
    def GetXRange(self, minX: float, maxX: float) -> None: ...
    def Dispose(self) -> None: ...
    def GetSeriesLineStyle(
        self,
        series: int,
        mode: PlotModes,
        color: System.Drawing.Color,
        style: System.Drawing.Drawing2D.DashStyle,
        width: int,
    ) -> None: ...

class ProgressDlg(
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
        parent: Agilent.MassSpectrometry.GUI.Plot.TofDataBrowser.MainForm,
        totalNumScanRecords: int,
    ) -> None: ...

class RidgeDialog(
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
        ridgeInfo: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.RidgeFeatureInfo,
    ) -> None: ...

class RidgePlotData(
    Agilent.MassSpectrometry.GUI.Plot.TofDataBrowser.PlotData,
    IPeakData,
    System.IDisposable,
    IPlotDataAxisAssoc,
    IPlotData,
):  # Class
    def __init__(
        self,
        ridge: Agilent.MassSpectrometry.DataAnalysis.FD.Ridge,
        features: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.FD.Feature
        ],
    ) -> None: ...

    ShowFeatureFlightTimes: bool

    def Dispose(self) -> None: ...

class SpectrumPlotData(
    Agilent.MassSpectrometry.GUI.Plot.TofDataBrowser.PlotData,
    IPeakData,
    System.IDisposable,
    IPlotDataAxisAssoc,
    IPlotData,
):  # Class
    def __init__(self) -> None: ...

    PeakList: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.ProfileSpectrumPeak
    ]

    def Dispose(self) -> None: ...

class TICPlotData(
    Agilent.MassSpectrometry.GUI.Plot.TofDataBrowser.PlotData,
    System.IDisposable,
    IPlotDataAxisAssoc,
    IPlotData,
    IMarkerData,
):  # Class
    def __init__(
        self,
        dataNavigator: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.SampleDataNavigator,
    ) -> None: ...
