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

# Discovered Generic TypeVars:
T = TypeVar("T")
from . import ChromatogramPeakLabelType, DataNavigator, NormalizeType, Signal
from .Controls2 import IPropertyPage
from .Toolbar import IToolbarsManager

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleData

class DataUtils:  # Class
    @staticmethod
    def GetTic(
        dataNavigator: DataNavigator,
        scanType: Optional[Agilent.MassSpectrometry.DataAnalysis.MSScanType],
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...
    @staticmethod
    def GetSignalChromatogram(
        dataNavigator: DataNavigator, signal: Signal
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...

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

    AutoScale: bool
    CanAutoScale: bool  # readonly
    CanCopy: bool  # readonly
    CanCreateTargetCompound: bool  # readonly
    CanCreateTargetQualifier: bool  # readonly
    CanFindComponents: bool  # readonly
    CanNormalizeEachX: bool  # readonly
    CanSearchLibrary: bool  # readonly
    DataNavigator: DataNavigator
    DisplayAllSignals: bool
    HasSpectrumPanes: bool  # readonly
    HasTic: bool  # readonly
    MaxNumVisibleRows: int
    NormalizeType: NormalizeType
    OverlayAllSignals: bool
    OverlayIstdCompounds: bool
    OverlayTargetCompounds: bool
    Properties: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleData.SampleInfoProperties
    )  # readonly
    SampleDataPath: str  # readonly
    ShowCurrentCompound: bool
    ShowTic: bool
    TicColor: System.Drawing.Color
    TimeRange: Agilent.MassSpectrometry.DataAnalysis.IRange  # readonly
    ToolbarsManager: IToolbarsManager

    def GetActiveObject(self) -> T: ...
    def GetPreferredYRangeLimit(
        self, row: int, column: int
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def AutoScaleX(self) -> None: ...
    def EnsureTimeRangeContainsScanLine(
        self, range: Agilent.MassSpectrometry.DataAnalysis.IRange
    ) -> Agilent.MassSpectrometry.DataAnalysis.IRange: ...
    def ShowSpectrum(self, x1: float, x2: float) -> None: ...
    def GetAutoScaleRangeX(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetMSScanColor(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Drawing.Color: ...
    @overload
    def DrawTicTo(
        self,
        graphics: System.Drawing.Graphics,
        bounds: System.Drawing.Rectangle,
        xrange: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
        yrange: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
    ) -> None: ...
    @overload
    def DrawTicTo(
        self,
        graphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        bounds: System.Drawing.Rectangle,
        xrange: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
        yrange: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
    ) -> None: ...
    @overload
    def DrawTicTo(
        self,
        graphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        scanType: Optional[Agilent.MassSpectrometry.DataAnalysis.MSScanType],
        bounds: System.Drawing.Rectangle,
        xrange: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
        yrange: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
        paintBackground: bool,
    ) -> None: ...
    def GetDisplayedMSScanTypes(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    def ShowComponents(
        self, components: Iterable[Agilent.MassSpectrometry.DataAnalysis.Component]
    ) -> None: ...
    def Copy(self) -> None: ...
    def GetAvailableSignals(self) -> List[Signal]: ...
    @staticmethod
    def CompareSignal(signal1: Signal, signal2: Signal) -> int: ...
    def CreateTargetCompound(self) -> None: ...
    def ClearSpectrumPanes(self) -> None: ...
    def CreatePropertyPages(self) -> List[IPropertyPage]: ...
    def InitConfiguration(self) -> None: ...
    def CreateTargetQualifier(self) -> None: ...
    def AutoScaleY(self) -> None: ...
    def FindComponents(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Component
    ]: ...
    def ShowMSScan(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType, show: bool
    ) -> None: ...
    def DisplaySignal(self, signal: Signal) -> None: ...
    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetAvailableMSScanTypes(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    def HideSignal(self, signal: Signal) -> None: ...
    def GetSignalColor(self, signal: Signal) -> System.Drawing.Color: ...
    def InitializePanes(self) -> None: ...
    def GetDisplayedSignals(self) -> List[Signal]: ...
    def SearchLibrary(
        self, app: Agilent.MassHunter.Quantitative.UIModel.ILibraryApp
    ) -> None: ...

class SampleDataControl(
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
    Agilent.MassHunter.Quantitative.UIModel.ISampleDataPane,
    System.Windows.Forms.IWin32Window,
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

    AutoScale: bool
    CanAutoScale: bool  # readonly
    CanCopy: bool  # readonly
    CanCreateTargetCompound: bool  # readonly
    CanCreateTargetQualifier: bool  # readonly
    CanExtractSpectrum: bool  # readonly
    CanFindComponents: bool  # readonly
    CanNormalizeEachX: bool  # readonly
    CanSearchLibrary: bool  # readonly
    HasSpectrumPanes: bool  # readonly
    MaxNumVisibleRows: int
    NormalizeType: NormalizeType
    OverlayAllSignals: bool
    OverlayIstdCompounds: bool
    OverlayTargetCompounds: bool
    PlotControl: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleData.PlotControl
    )  # readonly
    SampleDataPath: str  # readonly
    ShowCurrentCompound: bool
    ShowTic: bool
    TimeRange: Agilent.MassSpectrometry.DataAnalysis.IRange  # readonly

    def StoreSettings(self) -> None: ...
    def GetActiveObject(self) -> T: ...
    def AutoScaleX(self) -> None: ...
    def ShowSpectrum(self, start: float, end: float) -> None: ...
    def GetMSScanColor(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Drawing.Color: ...
    def GetDisplayedMSScanTypes(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    def ShowComponents(
        self, components: Iterable[Agilent.MassSpectrometry.DataAnalysis.Component]
    ) -> None: ...
    def Copy(self) -> None: ...
    def GetAvailableSignals(self) -> List[Signal]: ...
    def CreateTargetCompound(self) -> None: ...
    def ClearSpectrumPanes(self) -> None: ...
    def CreatePropertyPages(self) -> List[IPropertyPage]: ...
    def CreateTargetQualifier(self) -> None: ...
    def AutoScaleY(self) -> None: ...
    def FindComponents(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Component
    ]: ...
    def ShowMSScan(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType, show: bool
    ) -> None: ...
    def DisplaySignal(self, signal: Signal) -> None: ...
    def GetAvailableMSScanTypes(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    def HideSignal(self, signal: Signal) -> None: ...
    def GetSignalColor(self, signal: Signal) -> System.Drawing.Color: ...
    def GetDisplayedSignals(self) -> List[Signal]: ...
    def SearchLibrary(
        self, app: Agilent.MassHunter.Quantitative.UIModel.ILibraryApp
    ) -> None: ...

class SampleInfoPropPage(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    IPropertyPage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.IWin32Window,
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
    def __init__(
        self,
        control: Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleData.PlotControl,
    ) -> None: ...

class SampleInfoProperties:  # Class
    AutoScaleAfter: float
    BackColor: System.Drawing.Color
    ChromatogramPeakLabelCaption: bool
    ChromatogramPeakLabelTypes: List[ChromatogramPeakLabelType]
    ChromatogramPeakLabelUnits: bool
    ComponentColors: List[System.Drawing.Color]
    CompoundColors: List[System.Drawing.Color]
    CurrentCompoundColor: System.Drawing.Color
    FontSize: float
    ForeColor: System.Drawing.Color
    GridlinesColor: System.Drawing.Color
    GridlinesVisible: bool
    Normalize: bool
    OverlayAllMSScans: bool
    OverlayAllSignals: bool
    OverlayIstdCompounds: bool
    OverlayTargetCompounds: bool
    PeakLabelsAllowOverlap: bool
    PeakLabelsVertical: bool
    PrecursorColor: System.Drawing.Color
    PrecursorFill: bool
    PrecursorSize: int
    ShowCurrentCompound: bool
    ShowSignalLabels: bool
    ShowTic: bool
    SignalColors: List[System.Drawing.Color]
    SpectrumColor: System.Drawing.Color  # readonly
    TargetPeakLabelsOnTIC: bool
    TicColor: System.Drawing.Color
    TimeSegmentBorderColor: System.Drawing.Color
    TimeSegmentBorderVisible: bool

    def InitFromConfiguration(self) -> None: ...

class SelectMassEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.EventManipulator,
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
):  # Class
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseDown(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
