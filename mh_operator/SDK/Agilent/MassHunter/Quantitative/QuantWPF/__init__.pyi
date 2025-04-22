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

from . import AppMenu, Tools

# Discovered Generic TypeVars:
T = TypeVar("T")
from .QuantAppServices import Service
from .ToolbarWPF.Definitions import ExplorerBar
from .ToolbarWPF.ToolManager import IToolManager, ToolManagerBase
from .ToolbarWPF.ToolState import IToolState
from .UIModel import (
    ICagWindow,
    ICalCurvePane,
    IChromatogramInformationGridView,
    IChromatogramInformationUIContext,
    IChromatogramInformationView,
    IChromatogramInformationWindow,
    IChromSpecPane,
    IChromSpecProperties,
    ICustomPane,
    IDataNavigator,
    IDockManager,
    IDockPane,
    IMainWindow,
    IMethodErrorListPane,
    IMethodTablePane,
    IMethodTasksPane,
    IMetricsPlotPane,
    IPresentationState,
    ISampleDataPane,
    IScriptPane,
    IStatusBar,
    IWorktablePane,
)

# Stubs for namespace: Agilent.MassHunter.Quantitative.QuantWPF

class App(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.IAppContext,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IHaveResources,
    System.Windows.Application,
):  # Class
    def __init__(self) -> None: ...

    PresentationState: IPresentationState  # readonly
    ScriptTesting: bool
    UIState: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState
    )  # readonly

    @staticmethod
    def RegisterApplicationService(
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
        mainWindow: Agilent.MassHunter.Quantitative.QuantWPF.MainWindow,
        key: str,
    ) -> Service: ...
    def ShowErrorMessage(self, exception: System.Exception) -> None: ...
    def ExitThread(self) -> None: ...
    @staticmethod
    def Main() -> None: ...
    def InitializeComponent(self) -> None: ...

    Initialized: System.EventHandler  # Event

class CagAddInManager(
    System.MarshalByRefObject,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IAddInManager,
):  # Class
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IAddIn: ...
    def Initialize(self) -> None: ...
    def Clear(self) -> None: ...
    def Dispose(self) -> None: ...
    def GetIDs(self) -> List[str]: ...

class CagWindow(
    System.Windows.Markup.IAddChild,
    Infragistics.Windows.Ribbon.XamRibbonWindow,
    System.Windows.Markup.IHaveResources,
    System.Windows.IInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.IFrameworkInputElement,
    Infragistics.Windows.Ribbon.IRibbonWindow,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.IWindowService,
    ICagWindow,
    System.Windows.Forms.IWin32Window,
):  # Class
    def __init__(self) -> None: ...

    ContainsFocus: bool  # readonly
    DataNavigator: IDataNavigator  # readonly
    Handle: System.IntPtr  # readonly
    Height: int
    InvokeRequired: bool  # readonly
    IsHandleCreated: bool  # readonly
    Location: System.Drawing.Point
    PresentationState: IPresentationState  # readonly
    ToolbarsManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager
    )  # readonly
    Visible: bool  # readonly
    Width: int
    WindowState: System.Windows.Forms.FormWindowState

    def ShowHelpContents(self) -> None: ...
    def GetAddInManager(self) -> T: ...
    def Initialize(
        self,
        navigator: IDataNavigator,
        uiState: Agilent.MassHunter.Quantitative.QuantWPF.UIState,
        props: IChromSpecProperties,
    ) -> None: ...
    def ShowSetupGraphicsDialog(self) -> None: ...
    def ShowHelpIndex(self) -> None: ...
    def GetSelectedCompounds(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TargetCompoundRowId
    ]: ...
    def GetSelectedSamples(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleRowId]: ...
    def GetChromatogramControl(self) -> T: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def Update(self) -> None: ...
    def SetCurrentLayoutAsDefault(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def GetSetupGraphicsContext(self) -> T: ...
    def GetToolbar(
        self, pane: str, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbar: ...
    def ShowHelpSearch(self) -> None: ...
    def Invoke(self, del_: System.Delegate, parameters: List[Any]) -> Any: ...
    def LoadDefaultLayout(self, loadAllSamplesCompounds: bool) -> bool: ...

    Disposed: System.EventHandler  # Event

class ChromatogramInformationWindow(
    System.Windows.Markup.IAddChild,
    Infragistics.Windows.Ribbon.XamRibbonWindow,
    System.Windows.Markup.IHaveResources,
    System.Windows.IInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.IFrameworkInputElement,
    Infragistics.Windows.Ribbon.IRibbonWindow,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.IWindowService,
    System.Windows.Forms.IWin32Window,
    IChromatogramInformationWindow,
):  # Class
    def __init__(self) -> None: ...

    ChromView: IChromatogramInformationView  # readonly
    ContainsFocus: bool  # readonly
    GridView: IChromatogramInformationGridView  # readonly
    Handle: System.IntPtr  # readonly
    HeadToTail: bool
    Height: int
    InvokeRequired: bool  # readonly
    IsHandleCreated: bool  # readonly
    LinkXAxes: bool
    LinkYAxes: bool
    Location: System.Drawing.Point
    MaxNumVisibleRows: int
    Overlay: bool
    ToolbarsManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager
    )  # readonly
    UIContext: IChromatogramInformationUIContext  # readonly
    Visible: bool  # readonly
    Width: int
    WindowState: System.Windows.Forms.FormWindowState

    def Initialize(
        self,
        dataNavigator: IDataNavigator,
        uiState: Agilent.MassHunter.Quantitative.QuantWPF.UIState,
    ) -> None: ...
    def AutoScaleY(self) -> None: ...
    def CanAutoScale(self) -> bool: ...
    def Copy(self) -> None: ...
    def AutoScaleX(self) -> None: ...
    def CanCopy(self) -> bool: ...
    def InitializeComponent(self) -> None: ...
    def CreatePropertyPages(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage
    ]: ...
    def AutoScaleXY(self) -> None: ...
    def CanCreateCompound(self) -> bool: ...
    def CreateCompound(self) -> None: ...
    @overload
    def Invoke(self, d: System.Delegate, parameters: List[Any]) -> Any: ...
    @overload
    def Invoke(self, d: System.Delegate) -> Any: ...

    Disposed: System.EventHandler  # Event

class CommandLine(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLine
):  # Class
    def __init__(self) -> None: ...

    StartupPath: str

class DockManager(System.IDisposable, IDockManager):  # Class
    def __init__(
        self, mainWindow: Agilent.MassHunter.Quantitative.QuantWPF.MainWindow
    ) -> None: ...

    ActivePane: IDockPane  # readonly

    def ControlPaneExists(self, paneId: str) -> bool: ...
    def Dispose(self) -> None: ...
    def GetPane(self, paneId: str) -> IDockPane: ...

class DockPane(IDockPane):  # Class
    def __init__(
        self, host: System.Windows.Forms.Integration.WindowsFormsHost
    ) -> None: ...

    Control: System.Windows.Forms.Control  # readonly

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
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IQueryAmbient,
    IMainWindow,
    System.Windows.IWindowService,
    System.Windows.Forms.IWin32Window,
):  # Class
    def __init__(
        self,
        presentationState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.PresentationState,
        appService: bool,
    ) -> None: ...

    CalCurvePane: ICalCurvePane  # readonly
    ChromSpecPane: IChromSpecPane  # readonly
    CommandContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AppCommandContext
    )  # readonly
    ContainsFocus: bool  # readonly
    DataNavigator: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DataNavigator
    )  # readonly
    DockManager: IDockManager  # readonly
    Handle: System.IntPtr  # readonly
    Height: int
    InvokeRequired: bool  # readonly
    IsDisposed: bool  # readonly
    IsHandleCreated: bool  # readonly
    Location: System.Drawing.Point
    MethodErrorListPane: IMethodErrorListPane  # readonly
    MethodTablePane: IMethodTablePane  # readonly
    MethodTasksPane: IMethodTasksPane  # readonly
    MetricsPlotPane: IMetricsPlotPane  # readonly
    PresentationState: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.PresentationState
    )  # readonly
    SampleDataPane: ISampleDataPane  # readonly
    ScriptPane: IScriptPane  # readonly
    StatusBar: IStatusBar  # readonly
    Text: str
    ToolbarsManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager
    )  # readonly
    UIState: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState
    )  # readonly
    Width: int
    WorktablePane: IWorktablePane  # readonly
    _CalCurvePane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CalCurve
    )  # readonly
    _ChromSpec: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromSpec  # readonly
    _DockManager: Infragistics.Windows.DockManager.XamDockManager  # readonly
    _Ribbon: Infragistics.Windows.Ribbon.XamRibbon  # readonly
    _SampleDataPane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleData.SampleDataControl
    )  # readonly
    _Worktable: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Worktable  # readonly

    def CustomPaneExists(self, key: str) -> bool: ...
    def ShowAboutBox(self) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def Invoke(self, d: System.Delegate) -> Any: ...
    def RegisterCustomPane(
        self, register: bool, key: str, pane: ICustomPane
    ) -> None: ...
    def IsPaneVisible(self, name: str) -> bool: ...
    def InitializeComponent(self) -> None: ...
    def ResetLayout(self) -> None: ...
    def ShowMethodErrorListPane(self) -> None: ...
    def ForceClose(self) -> None: ...
    def ValidateMethod(self, alwaysShowPane: bool) -> None: ...
    def GetCustomPane(self, key: str) -> ICustomPane: ...
    def Activate(self) -> None: ...
    def SetPaneVisible(self, name: str, visible: bool) -> None: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def MaximizePane(self, paneKey: str) -> None: ...
    def ActivatePane(self, name: str) -> None: ...
    @staticmethod
    def IsModal(window: System.Windows.Window) -> bool: ...
    def LayoutPanes(self, pattern: int) -> None: ...
    def IsInModalState(self) -> bool: ...
    def ShowWindow(self) -> None: ...

class MethodTasksControl(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    IMethodTasksPane,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...

    Panel: System.Windows.Controls.StackPanel  # readonly

    def InitializeComponent(self) -> None: ...
    def InitTools(
        self,
        definitions: ExplorerBar,
        toolManager: Agilent.MassHunter.Quantitative.QuantWPF.ToolManager,
        rmgr: System.Resources.ResourceManager,
    ) -> None: ...
    def GetGroup(
        self, id: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IExplorerBarGroup
    ): ...

class StatusBar(IStatusBar):  # Class
    def __init__(
        self, mainWindow: Agilent.MassHunter.Quantitative.QuantWPF.MainWindow
    ) -> None: ...

    Visible: bool

class StatusBarController(System.IDisposable):  # Class
    def __init__(
        self, window: Agilent.MassHunter.Quantitative.QuantWPF.MainWindow
    ) -> None: ...
    def Dispose(self) -> None: ...

class ToolHandlerApplicationMenu(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        uiStateObj: Any,
    ) -> None: ...
    def SetState(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        uiStateObj: Any,
    ) -> None: ...

class ToolIds:  # Class
    def __init__(self) -> None: ...

    App_File_About: str = ...  # static # readonly
    App_File_NewBatch: str = ...  # static # readonly
    App_File_OpenBatch: str = ...  # static # readonly
    App_File_SaveAs: str = ...  # static # readonly
    ContextualTabGroup_ManualIntegrate: str = ...  # static # readonly
    View_BatchTableLayout: str = ...  # static # readonly
    View_ExpandCollapse: str = ...  # static # readonly
    View_Layout_LoadSaveLayout: str = ...  # static # readonly
    View_Layout_MaximizePane: str = ...  # static # readonly
    View_Layout_PresetLayouts: str = ...  # static # readonly
    View_Panes: str = ...  # static # readonly

class ToolManager(
    ToolManagerBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    IToolManager,
):  # Class
    def __init__(
        self,
        ribbon: Infragistics.Windows.Ribbon.XamRibbon,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...

    IUIState: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState
    )  # readonly

    @staticmethod
    def GetImageNames() -> List[str]: ...
    def RegisterScriptToolHandler(
        self, id: str, module: str, setState: str, execute: str
    ) -> None: ...
    def ApplicationMenu2010SelectedTabItemChanged(self) -> None: ...
    def SetToolState(self, state: IToolState) -> None: ...
    def GetImage(self, image: str) -> System.Windows.Media.Imaging.BitmapSource: ...
    def GetToolbarTitle(self, id: str) -> str: ...
    def GetApplicationMenu2010Content(self, category: str, id: str) -> Any: ...
    def GetToolTooltip(self, id: str) -> str: ...
    def IsContextualTabGroupVisible(self, id: str) -> bool: ...
    @staticmethod
    def _GetImage(image: str) -> System.Windows.Media.Imaging.BitmapSource: ...
    def ApplicationMenu2010Closed(self) -> None: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    @overload
    def GetToolCaption(
        self, id: str, culture: System.Globalization.CultureInfo
    ) -> str: ...
    @overload
    def GetToolCaption(self, id: str) -> str: ...

class UIState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls.UIState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
):  # Class
    def __init__(
        self, win: Agilent.MassHunter.Quantitative.QuantWPF.MainWindow
    ) -> None: ...

    ActivePane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane
    )  # readonly

    def CreateCagWindow(self) -> ICagWindow: ...
    def CreateChromatogramInformationWindow(self) -> IChromatogramInformationWindow: ...
