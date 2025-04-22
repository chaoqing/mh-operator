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

from .Definitions import Command, Tools
from .ToolState import IToolState

# Stubs for namespace: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager

class ActiveDockPaneManager(System.IDisposable):  # Class
    def __init__(
        self, dockMgr: Infragistics.Windows.DockManager.XamDockManager
    ) -> None: ...
    def Dispose(self) -> None: ...

class ApplicationMenu2010(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IApplicationMenu2010
):  # Class
    def __init__(
        self, menu: Infragistics.Windows.Ribbon.ApplicationMenu2010
    ) -> None: ...

    IsOpen: bool
    LastSelectedTabID: str
    SelectedTabID: str

class ContextMenuBridge(System.IDisposable):  # Class
    def __init__(
        self,
        toolManager: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
        control: System.Windows.Forms.Control,
        id: str,
    ) -> None: ...
    @staticmethod
    def Register(
        toolManager: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
        control: System.Windows.Forms.Control,
        contextMenuID: str,
    ) -> None: ...
    def Dispose(self) -> None: ...

class IApplicationMenu2010(object):  # Interface
    IsOpen: bool
    LastSelectedTabID: str
    SelectedTabID: str

class IContextMenuToolState(object):  # Interface
    def SetContextMenu(self, element: System.Windows.FrameworkElement) -> None: ...

class IToolManager(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    System.IDisposable,
):  # Interface
    ApplicationMenu2010: (
        Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IApplicationMenu2010
    )  # readonly
    Command: System.Windows.Input.ICommand  # readonly
    Dispatcher: System.Windows.Threading.Dispatcher  # readonly
    InputBindings: System.Windows.Input.InputBindingCollection  # readonly
    UIState: Any  # readonly

    def GetApplicationMenu2010Content(self, category: str, id: str) -> Any: ...
    def ApplicationMenu2010SelectedTabItemChanged(self) -> None: ...
    def RegisterBeforeToolDropdown(
        self,
        id: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolBeforeDropdownHandler,
        add: bool,
    ) -> None: ...
    def AddTool(self, cateogry: str, state: IToolState) -> None: ...
    def GetToolImage(self, id: str) -> System.Drawing.Image: ...
    def GetToolbarTitle(self, id: str) -> str: ...
    def RegisterToolHandler(
        self,
        id: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    ) -> None: ...
    def IsContextualTabGroupVisible(self, id: str) -> bool: ...
    def InsertTool(self, id: str, parent: str, after: str) -> None: ...
    def Execute(self, state: IToolState) -> None: ...
    def GetImage(self, image: str) -> System.Windows.Media.Imaging.BitmapSource: ...
    def NotifyContextualTabGroupsChanged(self) -> None: ...
    def GetToolState(self, id: str) -> IToolState: ...
    @overload
    def GetToolCaption(self, id: str) -> str: ...
    @overload
    def GetToolCaption(
        self, id: str, culture: System.Globalization.CultureInfo
    ) -> str: ...
    def SetToolState(self, state: IToolState) -> None: ...
    def GetToolTooltip(self, id: str) -> str: ...
    def ApplicationMenu2010Opened(self) -> None: ...
    def NotifyBeforeToolDropdown(
        self,
        state: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    ) -> None: ...
    def ToolInstanceRemoved(self, state: IToolState) -> None: ...
    def ApplicationMenu2010Closed(self) -> None: ...
    def GetToolTooltipTitle(self, id: str) -> str: ...
    def AddToolbar(
        self,
        paneId: str,
        toolbarId: str,
        toolbar: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolbar,
    ) -> None: ...
    def RemoveTool(self, id: str, parent: str) -> None: ...
    def SetupRibbon(self, tools: Tools) -> None: ...

    ContextualTabGroupsChanged: System.EventHandler  # Event

class IToolbar(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbar
):  # Interface
    _ToolBar: System.Windows.Controls.ToolBar  # readonly

class IToolbarHost(object):  # Interface
    def AddToolbar(
        self,
        id: str,
        toolbar: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolbar,
    ) -> None: ...
    def SetFocus(self) -> None: ...
    def GetToolbarIds(self) -> List[str]: ...
    def RemoveToolbar(self, id: str) -> None: ...
    def ContainsToolbar(self, toolbarId: str) -> bool: ...
    def GetToolbar(
        self, id: str
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolbar: ...

class ThreadRequeryCommands(
    System.IDisposable, System.Windows.Forms.IMessageFilter
):  # Class
    def __init__(self) -> None: ...
    def PreFilterMessage(self, m: System.Windows.Forms.Message) -> bool: ...
    def Dispose(self) -> None: ...

class ToolHandlerSet:  # Class
    def __init__(self) -> None: ...
    @overload
    def RegisterCategoryHandler(
        self,
        category: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    ) -> None: ...
    @overload
    def RegisterCategoryHandler(
        self,
        category: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    ) -> None: ...
    def ContainsCategoryHandler(self, category: str) -> bool: ...
    def RegisterCategory(self, id: str, category: str) -> None: ...
    @overload
    def RegisterToolHandler(
        self,
        id: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    ) -> None: ...
    @overload
    def RegisterToolHandler(
        self,
        id: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    ) -> None: ...
    def SetToolState(self, tool: IToolState, uiState: Any) -> None: ...
    def GetToolCategory(self, id: str) -> str: ...
    @overload
    def Execute(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        uiState: Any,
    ) -> None: ...
    @overload
    def Execute(self, tool: IToolState, uiState: Any) -> None: ...

class ToolManagerBase(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
):  # Class
    def __init__(
        self, ribbon: Infragistics.Windows.Ribbon.XamRibbon, uiState: Any
    ) -> None: ...

    ApplicationMenu2010: (
        Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IApplicationMenu2010
    )  # readonly
    Command: System.Windows.Input.ICommand  # readonly
    Dispatcher: System.Windows.Threading.Dispatcher  # readonly
    InputBindings: System.Windows.Input.InputBindingCollection  # readonly
    Ribbon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbon
    )  # readonly
    TouchEnabled: bool
    UIState: Any  # readonly
    XamRibbon: Infragistics.Windows.Ribbon.XamRibbon  # readonly

    def GetApplicationMenu2010Content(self, category: str, id: str) -> Any: ...
    def ApplicationMenu2010SelectedTabItemChanged(self) -> None: ...
    def RegisterCheckButton(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def RegisterBeforeToolDropdown(
        self,
        id: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolBeforeDropdownHandler,
        add: bool,
    ) -> None: ...
    def GetApplicationMenu(
        self, paneId: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IApplicationMenu
    ): ...
    def SetToolImage(self, id: str, image: System.Drawing.Image) -> None: ...
    def Dispose(self) -> None: ...
    def RegisterPopupMenu(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def GetToolbarIds(self, pane: str) -> List[str]: ...
    def AddTool(self, category: str, tool: IToolState) -> None: ...
    def InvokeMouseAction(
        self,
        pane: str,
        button: str,
        mact: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.MouseAction,
        state: str,
    ) -> None: ...
    def CreateCommand(self) -> Command: ...
    def GetTool(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def GetToolImage(self, id: str) -> System.Drawing.Image: ...
    def GetTools(
        self, id: str
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool]: ...
    def GetToolbarTitle(self, id: str) -> str: ...
    @overload
    def RegisterToolHandler(
        self,
        id: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    ) -> None: ...
    @overload
    def RegisterToolHandler(
        self,
        id: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    ) -> None: ...
    def RegisterTool(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def RemoveToolbar(self, paneId: str, toolbarId: str) -> None: ...
    def ContainsTool(self, id: str) -> bool: ...
    def InsertTool(self, id: str, parent: str, after: str) -> None: ...
    def IsContextualTabGroupVisible(self, id: str) -> bool: ...
    @overload
    def Execute(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    ) -> None: ...
    @overload
    def Execute(self, tool: IToolState) -> None: ...
    def RevokeTool(self, id: str) -> None: ...
    def GetImage(self, image: str) -> System.Windows.Media.Imaging.BitmapSource: ...
    def ContainsCategoryHandler(self, category: str) -> bool: ...
    def RegisterLabel(
        self, id: str, category: str, caption: str, tooltip: str
    ) -> None: ...
    def NotifyContextualTabGroupsChanged(self) -> None: ...
    def GetToolState(self, id: str) -> IToolState: ...
    @overload
    def GetToolCaption(self, id: str) -> str: ...
    @overload
    def GetToolCaption(
        self, id: str, culture: System.Globalization.CultureInfo
    ) -> str: ...
    def SetToolState(self, state: IToolState) -> None: ...
    def RegisterToolbarHost(
        self,
        paneId: str,
        host: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolbarHost,
    ) -> None: ...
    def GetToolTooltip(self, id: str) -> str: ...
    def RegisterComboBox(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def GetToolbar(
        self, paneId: str, toolbarId: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbar: ...
    def RegisterScriptToolHandler(
        self, id: str, module: str, setState: str, execute: str
    ) -> None: ...
    def ApplicationMenu2010Opened(self) -> None: ...
    def NotifyBeforeToolDropdown(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    ) -> None: ...
    def ToolInstanceRemoved(self, tool: IToolState) -> None: ...
    def ApplicationMenu2010Closed(self) -> None: ...
    def GetToolTooltipTitle(self, id: str) -> str: ...
    @overload
    def AddToolbar(
        self, paneId: str, toolbarId: str, text: str, row: int, column: int
    ) -> None: ...
    @overload
    def AddToolbar(
        self,
        pane: str,
        toolbarId: str,
        toolbar: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolbar,
    ) -> None: ...
    @overload
    def AddToolbar(self, paneId: str, toolbarId: str, text: str) -> None: ...
    @overload
    def RemoveTool(self, id: str) -> None: ...
    @overload
    def RemoveTool(self, id: str, parent: str) -> None: ...
    def SetupRibbon(self, tools: Tools) -> None: ...
    def GetToolCategory(self, id: str) -> str: ...
    def ContainsToolbar(self, paneId: str, toolbarId: str) -> bool: ...
    @overload
    def RegisterCategoryHandler(
        self,
        category: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    ) -> None: ...
    @overload
    def RegisterCategoryHandler(
        self,
        category: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    ) -> None: ...
    def RegisterButton(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...

    ContextualTabGroupsChanged: System.EventHandler  # Event
    ToolExecuting: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolExecuteEventArgs
    ]  # Event

class ToolbarHost(
    System.Windows.Media.Composition.DUCE.IResource,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolbarHost,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.DockPanel,
    System.ComponentModel.ISupportInitialize,
    System.Windows.IInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.IFrameworkInputElement,
    System.Windows.Input.ICommand,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...

    Host: System.Windows.Forms.Integration.WindowsFormsHost  # readonly

    def AddToolbar(
        self,
        id: str,
        toolbar: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolbar,
    ) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def SetFocus(self) -> None: ...
    def GetToolbarIds(self) -> List[str]: ...
    def RemoveToolbar(self, id: str) -> None: ...
    def Execute(self, parameter: Any) -> None: ...
    def InitializeComponent(self) -> None: ...
    def ContainsToolbar(self, toolbarId: str) -> bool: ...
    def GetToolbar(
        self, id: str
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolbar: ...

    CanExecuteChanged: System.EventHandler  # Event
