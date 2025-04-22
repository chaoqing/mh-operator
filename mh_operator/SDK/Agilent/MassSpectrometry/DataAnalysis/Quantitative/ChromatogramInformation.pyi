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

from . import Signal
from .Controls2 import IPropertyPage
from .Toolbar import IToolbarsManager, IToolHandler, IToolState, ToolbarsManagerBase
from .UIScriptIF import IChromatogramInformation, IUIState
from .UIUtils import PlotPageSettings, PlotPrintDocument

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation

class ChromForm(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationWindow,
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
    def __init__(self) -> None: ...

    ChromView: (
        Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationView
    )  # readonly
    GridView: (
        Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationGridView
    )  # readonly
    HeadToTail: bool
    LinkXAxes: bool
    LinkYAxes: bool
    MaxNumVisibleRows: int
    Overlay: bool
    ToolbarsManager: IToolbarsManager  # readonly
    UIContext: (
        Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationUIContext
    )  # readonly

    def Initialize(
        self,
        uiState: IUIState,
        dataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator,
    ) -> None: ...
    def AutoScaleY(self) -> None: ...
    def CanAutoScale(self) -> bool: ...
    def Copy(self) -> None: ...
    def AutoScaleX(self) -> None: ...
    def CanCopy(self) -> bool: ...
    def CreatePropertyPages(self) -> List[IPropertyPage]: ...
    def AutoScaleXY(self) -> None: ...
    def CanCreateCompound(self) -> bool: ...
    @overload
    @staticmethod
    def CreateCompound() -> None: ...
    @overload
    @staticmethod
    def CreateCompound(
        uiState: IUIState,
        chromView: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.ChromView,
    ) -> None: ...

    Initialized: System.EventHandler  # Event

class ChromGridView(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationGridView,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.DataGridView,
    System.ComponentModel.ISupportInitialize,
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
    def __init__(self) -> None: ...

    UIContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.UIContext
    )

    def Copy(self) -> None: ...
    def UpdateItems(self) -> None: ...
    def CanCopy(self) -> bool: ...

class ChromItem(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.ChromItem
    ],
    Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationItem,
):  # Class
    BatchID: int
    Color: System.Drawing.Color
    DataFileName: str
    InstrumentName: str
    MSScanType: Optional[Agilent.MassSpectrometry.DataAnalysis.MSScanType]
    SampleID: int
    SampleName: str
    Signal: Signal

    def Equals(self, obj: Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        item: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.ChromItem,
    ) -> int: ...
    def Clone(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.ChromItem
    ): ...

class ChromView(
    Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationView,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.IComponent,
    System.Windows.Forms.IDropTarget,
    Agilent.MassSpectrometry.GUI.Plot.PlotControl,
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    System.ComponentModel.ISupportInitialize,
    Agilent.MassSpectrometry.GUI.Plot.ICustomDrawPeakLabelsEx,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
):  # Class
    def __init__(self) -> None: ...

    LinkXAxes: bool
    LinkYAxes: bool
    MaxVisibleRowsPerPage: int
    Mirror: bool
    Overlay: bool
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    UIContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.UIContext
    )

    def DrawLabel(
        self,
        plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane,
        font: System.Drawing.Font,
        rect: System.Drawing.RectangleF,
        color: System.Drawing.Color,
        text: str,
        x: float,
        y: float,
        series: int,
        peakIndex: int,
    ) -> None: ...
    def UpdateHighlight(self) -> None: ...
    def AutoScaleY(self) -> None: ...
    def CanAutoScale(self) -> bool: ...
    def Copy(self) -> None: ...
    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def UIContext_ItemHighlightChanged(
        self, sender: Any, e: System.EventArgs
    ) -> None: ...
    def AutoScaleX(self) -> None: ...
    def CanCopy(self) -> bool: ...
    def InitConfiguration(self) -> None: ...
    def AutoScaleXY(self) -> None: ...
    def UpdatePeaks(self) -> None: ...
    def MeasureLabel(
        self,
        plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane,
        font: System.Drawing.Font,
        text: str,
        x: float,
        y: float,
        series: int,
        peakIndex: int,
    ) -> System.Drawing.RectangleF: ...
    def UpdateData(self, keepScale: bool) -> None: ...

class ColorCell(
    System.IDisposable, System.ICloneable, System.Windows.Forms.DataGridViewCell
):  # Class
    def __init__(self) -> None: ...

    ValueType: System.Type  # readonly

class ColorColumn(
    System.ICloneable,
    System.IDisposable,
    System.Windows.Forms.DataGridViewColumn,
    System.ComponentModel.IComponent,
):  # Class
    def __init__(self) -> None: ...

class DefaultEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.DefaultEventManipulatorBase,
):  # Class
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseMove(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseDown(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...

class ExportToSampleFoldersDialog(
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
    def __init__(self, uiState: IUIState) -> None: ...

    FileName: str  # readonly

class GraphicsRangeDialog(
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
    def __init__(self, ichrominfo: IChromatogramInformation) -> None: ...
    def Initialize(self, ichrominfo: IChromatogramInformation) -> None: ...
    def PerformRanges(self, ichrominfo: IChromatogramInformation) -> None: ...

class PlotData(
    Agilent.MassSpectrometry.GUI.Plot.IPlotData,
    Agilent.MassSpectrometry.GUI.Plot.IPeakData,
):  # Class
    def GetPointCount(self, series: int) -> int: ...
    def GetSeries(
        self, index: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.SeriesData
    ): ...
    def GetSeriesCount(self) -> int: ...
    def DisplaySeries(self, series: int) -> bool: ...
    def DisplayLabel(
        self, series: int, peak: int, label: str, color: System.Drawing.Color
    ) -> bool: ...
    def GetPeakCount(self, series: int) -> int: ...
    def GetPeak(self, series: int, peak: int, x: float, y: float) -> None: ...
    def GetPoint(self, series: int, pointIndex: int, x: float, y: float) -> None: ...
    def DisplayMarker(
        self, series: int, peak: int, marker: Agilent.MassSpectrometry.GUI.Plot.Marker
    ) -> bool: ...
    def GetSeriesLineStyle(
        self,
        series: int,
        mode: Agilent.MassSpectrometry.GUI.Plot.PlotModes,
        color: System.Drawing.Color,
        style: System.Drawing.Drawing2D.DashStyle,
        width: int,
    ) -> None: ...
    def Fill(
        self,
        series: int,
        peak: int,
        startPlotIndex: int,
        endPlotIndex: int,
        startBaselineX: float,
        startBaselineY: float,
        endBaselineX: float,
        endBaselineY: float,
        baselineColor: System.Drawing.Color,
        fillColor: System.Drawing.Color,
    ) -> bool: ...

class PrintDoc(
    System.IDisposable, System.ComponentModel.IComponent, PlotPrintDocument
):  # Class
    def __init__(
        self,
        form: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.ChromForm,
        printerSettings: System.Drawing.Printing.PrinterSettings,
        pageSettings: PlotPageSettings,
        preview: bool,
    ) -> None: ...
    def GetNumPages(self) -> int: ...

class PropertiesControl(
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
        chromView: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.ChromView,
    ) -> None: ...

    DisplayName: str
    IsDirty: bool  # readonly

    def SetActive(self) -> None: ...
    def DoDefault(self) -> None: ...
    def Apply(self) -> None: ...

    PageChanged: System.EventHandler  # Event

class SeriesData:  # Class
    Item: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.ChromItem
    )  # readonly

class ToolHandlerEdit(IToolHandler):  # Class
    def __init__(self) -> None: ...
    def Execute(self, toolState: IToolState, objUiState: Any) -> None: ...
    def SetState(self, toolState: IToolState, objUiState: Any) -> None: ...

class ToolHandlerFile(IToolHandler):  # Class
    def __init__(self) -> None: ...
    def Execute(self, toolState: IToolState, objUiState: Any) -> None: ...
    def SetState(self, toolState: IToolState, objUiState: Any) -> None: ...

class ToolHandlerView(IToolHandler):  # Class
    def __init__(self) -> None: ...
    def Execute(self, toolState: IToolState, objUiState: Any) -> None: ...
    def SetState(self, toolState: IToolState, objUiState: Any) -> None: ...

class ToolbarsManager(
    System.ComponentModel.ISupportInitialize,
    System.IDisposable,
    ToolbarsManagerBase,
    System.Windows.Forms.IMessageFilter,
    IToolbarsManager,
):  # Class
    def __init__(self, uiState: IUIState) -> None: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def RegisterScriptToolHandler(
        self, tool: str, module: str, setState: str, execute: str
    ) -> None: ...

class UIContext(
    System.IDisposable,
    Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationUIContext,
):  # Class
    def __init__(
        self,
        form: Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationWindow,
    ) -> None: ...

    DataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator
    ItemCount: int  # readonly
    Items: List[
        Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationItem
    ]  # readonly
    VisibleItemCount: int  # readonly

    def UpdateItems(self) -> None: ...
    def SetVisible(
        self,
        items: List[
            Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationItem
        ],
        visible: bool,
    ) -> None: ...
    def GetItem(
        self, index: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.ChromItem
    ): ...
    def GetVisibleItem(
        self, index: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromatogramInformation.ChromItem
    ): ...
    def IsVisible(
        self, item: Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationItem
    ) -> bool: ...
    def OnItemColorChanged(self, e: System.EventArgs) -> None: ...
    def Dispose(self) -> None: ...
