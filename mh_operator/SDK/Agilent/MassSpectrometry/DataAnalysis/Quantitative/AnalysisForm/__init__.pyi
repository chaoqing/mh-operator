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

from . import AppCommandContext, DataNavigator, Properties
from .Toolbar import IToolbarsManager, ToolbarsManagerBase
from .UIScriptIF import IUIState

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisForm

class DockManager(Agilent.MassHunter.Quantitative.UIModel.IDockManager):  # Class
    def __init__(
        self, manager: Infragistics.Win.UltraWinDock.UltraDockManager
    ) -> None: ...

    ActivePane: Agilent.MassHunter.Quantitative.UIModel.IDockPane  # readonly

    def ControlPaneExists(self, paneId: str) -> bool: ...
    def GetPane(
        self, paneId: str
    ) -> Agilent.MassHunter.Quantitative.UIModel.IDockPane: ...

class DockPane(Agilent.MassHunter.Quantitative.UIModel.IDockPane):  # Class
    Control: System.Windows.Forms.Control  # readonly

class MainForm(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    Agilent.MassHunter.Quantitative.UIModel.IMainWindow,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
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
    def __init__(self, navigator: DataNavigator) -> None: ...

    CalCurvePane: Agilent.MassHunter.Quantitative.UIModel.ICalCurvePane  # readonly
    ChromSpecPane: Agilent.MassHunter.Quantitative.UIModel.IChromSpecPane  # readonly
    CommandContext: AppCommandContext  # readonly
    DataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator  # readonly
    DockManager: Agilent.MassHunter.Quantitative.UIModel.IDockManager  # readonly
    MethodErrorListPane: (
        Agilent.MassHunter.Quantitative.UIModel.IMethodErrorListPane
    )  # readonly
    MethodTablePane: (
        Agilent.MassHunter.Quantitative.UIModel.IMethodTablePane
    )  # readonly
    MethodTasksPane: (
        Agilent.MassHunter.Quantitative.UIModel.IMethodTasksPane
    )  # readonly
    MetricsPlotPane: (
        Agilent.MassHunter.Quantitative.UIModel.IMetricsPlotPane
    )  # readonly
    PresentationState: (
        Agilent.MassHunter.Quantitative.UIModel.IPresentationState
    )  # readonly
    SampleDataPane: Agilent.MassHunter.Quantitative.UIModel.ISampleDataPane  # readonly
    ScriptPane: Agilent.MassHunter.Quantitative.UIModel.IScriptPane  # readonly
    StatusBar: Agilent.MassHunter.Quantitative.UIModel.IStatusBar  # readonly
    ToolbarsManager: IToolbarsManager  # readonly
    UIState: IUIState
    WorktablePane: Agilent.MassHunter.Quantitative.UIModel.IWorktablePane  # readonly

    def RegisterCustomPane(
        self,
        register: bool,
        key: str,
        pane: Agilent.MassHunter.Quantitative.UIModel.ICustomPane,
    ) -> None: ...
    def ActivatePane(self, paneKey: str) -> None: ...
    def CustomPaneExists(self, key: str) -> bool: ...
    def ForceClose(self) -> None: ...
    def ResetLayout(self) -> None: ...
    def SetPaneVisible(self, paneKey: str, visible: bool) -> None: ...
    def ShowMethodErrorListPane(self) -> None: ...
    def InitTools(self, assembly: str) -> None: ...
    def IsInModalState(self) -> bool: ...
    def LayoutPanes(self, pattern: int) -> None: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def ValidateMethod(self, alwaysShowPane: bool) -> None: ...
    def InitDockState(self) -> bool: ...
    def MaximizePane(self, paneKey: str) -> None: ...
    def IsPaneVisible(self, paneKey: str) -> bool: ...
    def GetCustomPane(
        self, key: str
    ) -> Agilent.MassHunter.Quantitative.UIModel.ICustomPane: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def ShowWindow(self) -> None: ...
    def ShowAboutBox(self) -> None: ...
    def ComplianceInitialized(self) -> None: ...

    HandleAboutBox: System.EventHandler  # Event
    MethodTablePaneCreated: System.EventHandler  # Event

class MainWindowTitleHandler(System.IDisposable):  # Class
    def __init__(
        self,
        state: Agilent.MassHunter.Quantitative.UIModel.IPresentationState,
        mainWindow: Agilent.MassHunter.Quantitative.UIModel.IMainWindow,
    ) -> None: ...
    def Dispose(self) -> None: ...
    def UpdateTitle(self) -> None: ...

class QuantCR(
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

class ToolbarsManager(
    System.ComponentModel.ISupportInitialize,
    System.IDisposable,
    ToolbarsManagerBase,
    System.Windows.Forms.IMessageFilter,
    IToolbarsManager,
):  # Class
    ApplicationType: str  # readonly
    InstrumentType: str  # readonly

    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def RegisterScriptToolHandler(
        self, tool: str, module: str, setState: str, execute: str
    ) -> None: ...
