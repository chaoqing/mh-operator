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

from .Toolbar2 import MouseAction, MouseActionMap

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar

class AddRibbon(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CustomToolElementBase
):  # Class
    def __init__(self) -> None: ...

    ApplicationMenu: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonToolsDefinition
    )
    Pane: str
    QuickAccessToolar: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonToolsDefinition
    )
    TabItemToolbar: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonToolsDefinition
    )
    Tabs: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonTabDefinition
    ]

class ApplicationMenuAreaImpl(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IApplicationMenuArea
):  # Class
    ...

class ApplicationMenuImpl(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IApplicationMenu,
):  # Class
    Appearance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance
    )  # readonly
    Bounds: System.Drawing.Rectangle  # readonly
    Enabled: bool
    Executing: bool
    Id: str  # readonly
    Tooltip: str

class ButtonDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.MenuDefinition
):  # Class
    def __init__(self) -> None: ...

class CategoryScriptToolHandler(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CategoryToolHandler,
):  # Class
    def __init__(self) -> None: ...

    Execute: str
    SetState: str
    ToolHandlerType: System.Type  # static

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class CategoryToolHandler(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.TypeToolHandler,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        category: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    ) -> None: ...

    Category: str

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class CheckButtonDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ButtonDefinition
):  # Class
    def __init__(self) -> None: ...

    MenuDisplayStyle: Infragistics.Win.UltraWinToolbars.StateButtonMenuDisplayStyle
    ToolbarDisplayStyle: (
        Infragistics.Win.UltraWinToolbars.StateButtonToolbarDisplayStyle
    )

    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        group: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBarGroup,
    ) -> None: ...

class CheckToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ICheckToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
):  # Class
    def __init__(self) -> None: ...

    Checked: bool

class ComboBoxDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ButtonDefinition
):  # Class
    def __init__(self) -> None: ...

    MaxDropDownItems: int
    Spring: bool

class ComboBoxToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IComboBoxToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
):  # Class
    IsDroppedDown: bool  # readonly
    ItemCount: int  # readonly
    SelectedIndex: int
    SelectedItem: Any

    def ClearItems(self) -> None: ...
    def BeforeToolDropdown(
        self,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolBeforeDropdownHandler,
        add: bool,
    ) -> None: ...
    def GetItemValue(self, index: int) -> Any: ...
    def IndexOf(self, value_: Any) -> int: ...
    def Remove(self, item: Any) -> None: ...
    def GetItemDisplayText(self, index: int) -> str: ...
    def AddItem(self, item: Any, displayText: str) -> None: ...
    def CloseDropdown(self) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ContextMenuDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.PopupMenuDefinition
):  # Class
    def __init__(self) -> None: ...

class ContextualTabGroupDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...

    Tabs: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonTabDefinition
    ]

    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        group: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBarGroup,
    ) -> None: ...
    @overload
    def AddTo(
        self, tools: Infragistics.Win.UltraWinToolbars.ToolsCollection
    ) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        ribbon: Infragistics.Win.UltraWinToolbars.Ribbon,
    ) -> None: ...

class CustomToolElementBase:  # Class
    Id: str
    Instrument: str

class CustomTools:  # Class
    def __init__(self) -> None: ...

    Elements: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CustomToolElementBase
    ]

    @overload
    @staticmethod
    def Evaluate(
        stream: System.IO.Stream,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        instrument: str,
    ) -> None: ...
    @overload
    @staticmethod
    def Evaluate(
        stream: System.IO.Stream,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        instrument: str,
        explorerBar: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBar,
    ) -> None: ...
    @overload
    @staticmethod
    def Evaluate(
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        instrument: str,
        explorerBar: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBar,
    ) -> None: ...

class ExplorerBarDefinition:  # Class
    def __init__(self) -> None: ...

    Groups: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ExplorerBarGroup
    ]

class ExplorerBarGroup:  # Class
    def __init__(self) -> None: ...

    Expanded: bool
    Id: str
    LargeImage: str
    Tools: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionBase
    ]

class ExplorerBarItemState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ICheckToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
):  # Class
    def __init__(self) -> None: ...

    Appearance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance
    )  # readonly
    Bounds: System.Drawing.Rectangle  # readonly
    Checked: bool
    Enabled: bool
    Id: str  # readonly
    Tooltip: str

class IApplicationMenu(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState
):  # Interface
    ToolAreaRight: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IApplicationMenuArea
    )  # readonly

    def BeforeToolDropdown(
        self,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolBeforeDropdownHandler,
        register: bool,
    ) -> None: ...

class IApplicationMenuArea(object):  # Interface
    Count: int  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def Clear(self) -> None: ...
    def Add(self, id: str) -> None: ...
    def Remove(self, id: str) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ICheckToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState
):  # Interface
    Checked: bool

class IComboBoxToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState
):  # Interface
    IsDroppedDown: bool  # readonly
    ItemCount: int  # readonly
    SelectedIndex: int
    SelectedItem: Any

    def ClearItems(self) -> None: ...
    def BeforeToolDropdown(
        self,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolBeforeDropdownHandler,
        add: bool,
    ) -> None: ...
    def GetItemValue(self, index: int) -> Any: ...
    def IndexOf(self, value_: Any) -> int: ...
    def Remove(self, item: Any) -> None: ...
    def GetItemDisplayText(self, index: int) -> str: ...
    def AddItem(self, item: Any, displayText: str) -> None: ...
    def CloseDropdown(self) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class IExplorerBarGroup(object):  # Interface
    Expanded: bool
    Id: str  # readonly

    def Add(self, id: str) -> None: ...
    def IndexOf(self, id: str) -> int: ...
    def Remove(self, id: str) -> None: ...
    def Exists(self, id: str) -> bool: ...
    def Insert(self, index: int, id: str) -> None: ...

class IPopupMenuToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState
):  # Interface
    Count: int  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def Add(self, id: str) -> None: ...
    def ShowPopupMenu(self) -> None: ...
    def BeforeToolDropdown(
        self,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolBeforeDropdownHandler,
        add: bool,
    ) -> None: ...
    def Clear(self) -> None: ...
    def IndexOf(self, id: str) -> int: ...
    def Remove(self, id: str) -> None: ...
    def Exists(self, id: str) -> bool: ...
    def Insert(self, id: str, index: int) -> None: ...
    def InsertSeparator(self, index: int) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class IRibbon(object):  # Interface
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonTab: ...
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonTab: ...
    TabCount: int  # readonly

    def RemoveTab(self, id: str) -> None: ...
    def ContainsTab(self, id: str) -> bool: ...
    def AddTab(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonTab: ...
    def InsertTabAfter(
        self, id: str, idAfter: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonTab: ...

class IRibbonGroup(object):  # Interface
    Caption: str
    ID: str  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    ItemCount: int  # readonly
    Tooltip: str
    Visible: bool

    def InsertToolAfter(
        self, id: str, idAfter: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def RemoveTool(self, id: str) -> None: ...
    def AddTool(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def ContainsTool(self, id: str) -> bool: ...

class IRibbonTab(object):  # Interface
    Caption: str
    GroupCount: int  # readonly
    ID: str  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonGroup: ...
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonGroup: ...
    Visible: bool

    def RemoveGroup(self, id: str) -> None: ...
    def ContainsGroup(self, id: str) -> bool: ...
    def AddGroup(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonGroup: ...
    def InsertGroupAfter(
        self, id: str, idAfter: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonGroup: ...

class IRibbonTabState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState
):  # Interface
    Visible: bool

class IScriptToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler
):  # Interface
    ExecuteExpression: str
    SetStateExpression: str

class ITextBoxToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState
):  # Interface
    IsInEdit: bool  # readonly
    IsReadOnly: bool
    Text: str

class IToolAppearance(object):  # Interface
    BoldText: bool
    DisplayStyle: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    )
    DisplayText: str
    Image: str
    MaxWidth: int
    MinWidth: int
    Separator: bool
    Tooltip: str
    Width: int

class IToolBeforeDropdownHandler(object):  # Interface
    def Dropdown(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        uiState: Any,
    ) -> None: ...

class IToolHandler(object):  # Interface
    def Execute(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        uiState: Any,
    ) -> None: ...
    def SetState(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        uiState: Any,
    ) -> None: ...

class IToolState(object):  # Interface
    Appearance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance
    )  # readonly
    Bounds: System.Drawing.Rectangle  # readonly
    Enabled: bool
    Executing: bool  # readonly
    Id: str  # readonly
    Tooltip: str

class IToolbar(object):  # Interface
    Caption: str  # readonly
    IsMenuBar: bool  # readonly
    Visible: bool

    def Contains(self, id: str) -> bool: ...
    def AddTool(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance: ...
    def InsertToolAfter(
        self, id: str, after: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance: ...
    def RemoveTool(self, id: str) -> None: ...
    def GetTool(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance: ...
    def GetToolState(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...

class IToolbarsManager(object):  # Interface
    Ribbon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbon
    )  # readonly
    TouchEnabled: bool

    def RegisterCheckButton(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def GetApplicationMenu(
        self, paneId: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IApplicationMenu
    ): ...
    def SetToolImage(self, id: str, image: System.Drawing.Image) -> None: ...
    def RegisterPopupMenu(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def GetToolbarIds(self, pane: str) -> List[str]: ...
    def InvokeMouseAction(
        self, pane: str, button: str, mact: MouseAction, state: str
    ) -> None: ...
    def GetTool(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def RegisterToolHandler(
        self,
        id: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    ) -> None: ...
    def RemoveToolbar(self, paneId: str, toolbarId: str) -> None: ...
    def ContainsTool(self, id: str) -> bool: ...
    def Execute(
        self,
        state: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    ) -> None: ...
    def ContainsCategoryHandler(self, category: str) -> bool: ...
    def RegisterLabel(
        self, id: str, category: str, caption: str, tooltip: str
    ) -> None: ...
    def RegisterComboBox(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def GetToolbar(
        self, paneId: str, toolbarId: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbar: ...
    def RegisterScriptToolHandler(
        self, id: str, module: str, setState: str, execute: str
    ) -> None: ...
    def AddToolbar(
        self, paneId: str, toolbarId: str, text: str, row: int, column: int
    ) -> None: ...
    def RemoveTool(self, id: str) -> None: ...
    def ContainsToolbar(self, paneId: str, toolbarId: str) -> bool: ...
    def RegisterCategoryHandler(
        self,
        category: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    ) -> None: ...
    def RegisterButton(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...

    ToolExecuting: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolExecuteEventArgs
    ]  # Event

class InsertTool(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CustomToolElementBase
):  # Class
    def __init__(self) -> None: ...

    After: str
    Caption: str
    Category: str
    Checkbox: bool
    ComboBox: bool
    Label: bool
    Pane: str
    Parent: str
    RibbonGroup: str
    ScriptExecute: str
    ScriptModule: str
    ScriptSetState: str
    Toolbar: str
    Tooltip: str

class LabelDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ButtonDefinition
):  # Class
    def __init__(self) -> None: ...

class MenuBarDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarDefinition
):  # Class
    def __init__(self) -> None: ...

class MenuDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolCollectionDefinitionBase
):  # Class
    def __init__(self) -> None: ...

    BoldText: bool
    Category: str
    DropDownArrowStyle: Infragistics.Win.UltraWinToolbars.DropDownArrowStyle
    Image: str
    ImageLarge: str
    PreferredSizeOnRibbon: Infragistics.Win.UltraWinToolbars.RibbonToolSize
    ScriptExecute: str
    ScriptModule: str
    ScriptSetState: str
    Shortcut: System.Windows.Forms.Shortcut
    Style: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    Visible: bool

    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...
    @overload
    def AddTo(
        self, tools: Infragistics.Win.UltraWinToolbars.ToolsCollection
    ) -> None: ...
    @overload
    def AddTo(
        self,
        toolbarsMgr: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        group: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBarGroup,
    ) -> None: ...

class PopupMenuDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.MenuDefinition
):  # Class
    def __init__(self) -> None: ...

class PopupMenuToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IPopupMenuToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
):  # Class
    def Insert(self, id: str, index: int) -> None: ...
    def InsertSeparator(self, index: int) -> None: ...
    def Add(self, id: str) -> None: ...

class RadioButtonDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ButtonDefinition
):  # Class
    def __init__(self) -> None: ...

    Group: str

    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...

class RemoveTool(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CustomToolElementBase
):  # Class
    def __init__(self) -> None: ...

    Parent: str

class RemoveToolbar(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CustomToolElementBase
):  # Class
    def __init__(self) -> None: ...

    Pane: str

class RibbonDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarDefinition
):  # Class
    def __init__(self) -> None: ...

    ApplicationMenu: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonToolsDefinition
    )
    ApplicationMenu2010: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonToolsDefinition
    )
    ContextualTabGroups: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ContextualTabGroupDefinition
    ]
    QuickAccessToolbar: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonToolsDefinition
    )
    TabItemToolbar: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonToolsDefinition
    )
    Tabs: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonTabDefinition
    ]

    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...

class RibbonGroupDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...

    LayoutDirection: Infragistics.Win.UltraWinToolbars.RibbonGroupToolLayoutDirection
    Tools: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionBase
    ]

    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        group: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBarGroup,
    ) -> None: ...
    @overload
    def AddTo(
        self, tools: Infragistics.Win.UltraWinToolbars.ToolsCollection
    ) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        groups: Infragistics.Win.UltraWinToolbars.RibbonGroupCollection,
    ) -> None: ...

class RibbonTabDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...

    Category: str
    Groups: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.RibbonGroupDefinition
    ]

    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        group: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBarGroup,
    ) -> None: ...
    @overload
    def AddTo(
        self, tools: Infragistics.Win.UltraWinToolbars.ToolsCollection
    ) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        tabs: Infragistics.Win.UltraWinToolbars.RibbonTabCollectionBase,
    ) -> Infragistics.Win.UltraWinToolbars.RibbonTab: ...

class RibbonTabState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonTabState,
):  # Class
    def __init__(self, tab: Infragistics.Win.UltraWinToolbars.RibbonTab) -> None: ...

    Appearance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance
    )  # readonly
    Bounds: System.Drawing.Rectangle  # readonly
    Enabled: bool
    Executing: bool  # readonly
    Id: str  # readonly
    Tooltip: str
    Visible: bool

class RibbonToolsDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.MenuDefinition
):  # Class
    def __init__(self) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...
    @overload
    def AddTo(
        self, tools: Infragistics.Win.UltraWinToolbars.ToolsCollection
    ) -> None: ...

class SeparatorDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...
    @overload
    def AddTo(
        self, tools: Infragistics.Win.UltraWinToolbars.ToolsCollection
    ) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        group: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBarGroup,
    ) -> None: ...

class SetHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CustomToolElementBase
):  # Class
    def __init__(self) -> None: ...

    ScriptExecute: str
    ScriptModule: str
    ScriptSetState: str

class SystemToolDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...

    Image: str

    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...
    @overload
    def AddTo(
        self, tools: Infragistics.Win.UltraWinToolbars.ToolsCollection
    ) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        group: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBarGroup,
    ) -> None: ...

class TextBoxDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ButtonDefinition
):  # Class
    def __init__(self) -> None: ...

    Spring: bool

class TextBoxToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ITextBoxToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
):  # Class
    def __init__(self) -> None: ...

class ToolCollectionDefinitionBase(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionBase
):  # Class
    Tools: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionBase
    ]

class ToolDefinitionAssemblyAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self) -> None: ...

    MethodNavigatorResourceName: str
    ToolDefinitionResourceName: str
    ToolResourceName: str

    @overload
    @staticmethod
    def LoadDefinitions(
        stream: System.IO.Stream,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitions: ...
    @overload
    @staticmethod
    def LoadDefinitions(
        assembly: System.Reflection.Assembly,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitions: ...
    @staticmethod
    def GetAttribute(
        assembly: System.Reflection.Assembly,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionAssemblyAttribute
    ): ...
    def LoadMethodDefinitions(
        self, assembly: System.Reflection.Assembly
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ExplorerBarDefinition
    ): ...
    def GetToolResource(
        self, assembly: System.Reflection.Assembly
    ) -> System.Resources.ResourceManager: ...

class ToolDefinitionBase:  # Class
    Caption: str
    Customizable: bool
    Id: str
    MaxWidth: int
    MinWidth: int
    Tooltip: str
    Width: int

    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...
    @overload
    def AddTo(
        self, tools: Infragistics.Win.UltraWinToolbars.ToolsCollection
    ) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        group: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBarGroup,
    ) -> None: ...

class ToolDefinitions:  # Class
    def __init__(self) -> None: ...

    CategoryToolHandlers: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CategoryToolHandler
    ]
    ContextMenus: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ContextMenuDefinition
    ]
    MouseActionMaps: List[MouseActionMap]
    ToolHandlers: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolHandler
    ]
    Toolbars: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarDefinition
    ]

class ToolDisplayStyle(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Default: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    ) = ...  # static # readonly
    ImageAndText: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    ) = ...  # static # readonly
    ImageOnly: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    ) = ...  # static # readonly
    TextOnly: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    ) = ...  # static # readonly

class ToolExecuteEventArgs(System.ComponentModel.CancelEventArgs):  # Class
    def __init__(self, id: str) -> None: ...

    ID: str  # readonly

class ToolHandler(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.TypeToolHandler,
):  # Class
    def __init__(self) -> None: ...

    Id: str

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class ToolHandlerBase(System.IDisposable):  # Class
    def Dispose(self) -> None: ...

class ToolScriptToolHandler(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolHandler,
):  # Class
    def __init__(self) -> None: ...

    Execute: str
    SetState: str
    ToolHandlerType: System.Type  # static

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class ToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
):  # Class
    def __init__(self) -> None: ...

    Appearance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance
    )  # readonly
    Bounds: System.Drawing.Rectangle  # readonly
    Enabled: bool
    Id: str  # readonly
    Tooltip: str

class ToolStateBase(System.MarshalByRefObject):  # Class
    def __init__(self) -> None: ...

    Executing: bool

class ToolbarDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolCollectionDefinitionBase
):  # Class
    def __init__(self) -> None: ...

    Column: int
    Pane: str
    Row: int
    Visible: bool

    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
    ) -> None: ...
    @overload
    def AddTo(
        self, tools: Infragistics.Win.UltraWinToolbars.ToolsCollection
    ) -> None: ...
    @overload
    def AddTo(
        self,
        manager: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolbarsManagerBase,
        group: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBarGroup,
    ) -> None: ...

class ToolbarsManagerBase(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IMessageFilter,
):  # Class
    ActiveToolId: str  # readonly
    ApplicationType: str  # readonly
    Customizable: bool
    InstrumentType: str  # readonly
    Ribbon: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbon
    )  # readonly
    SynchronizeInvoke: System.ComponentModel.ISynchronizeInvoke  # readonly
    ToolbarStyle: Infragistics.Win.UltraWinToolbars.ToolbarStyle
    TouchEnabled: bool

    def SetPaneControl(
        self, paneId: str, control: System.Windows.Forms.Control
    ) -> None: ...
    def AddPane(self, paneId: str, control: System.Windows.Forms.Control) -> None: ...
    def ContainsToolHandler(self, id: str) -> bool: ...
    def RegisterCheckButton(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def EndInit(self) -> None: ...
    def GetApplicationMenu(
        self, pane: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IApplicationMenu
    ): ...
    def SetToolImage(self, id: str, image: System.Drawing.Image) -> None: ...
    def Dispose(self) -> None: ...
    def RegisterPopupMenu(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def SetupExplorerBar(
        self,
        explorerBar: Infragistics.Win.UltraWinExplorerBar.UltraExplorerBar,
        definition: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ExplorerBarDefinition,
        resourceMgr: System.Resources.ResourceManager,
    ) -> None: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def GetToolbarIds(self, paneId: str) -> List[str]: ...
    def AddTool(
        self,
        definition: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitionBase,
    ) -> None: ...
    def InvokeMouseAction(
        self, pane: str, button: str, mact: MouseAction, state: str
    ) -> None: ...
    def GetTool(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def SetupToolbars(
        self,
        definitions: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDefinitions,
        assembly: System.Reflection.Assembly,
        resourceMgr: System.Resources.ResourceManager,
    ) -> None: ...
    def RegisterToolHandler(
        self,
        id: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    ) -> None: ...
    def BeginInit(self) -> None: ...
    def RemoveToolbar(self, paneId: str, toolbarId: str) -> None: ...
    def ContainsTool(self, id: str) -> bool: ...
    def Execute(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    ) -> None: ...
    def FindToolByShortcut(self, sc: System.Windows.Forms.Shortcut) -> str: ...
    def ContainsCategoryHandler(self, id: str) -> bool: ...
    def RegisterLabel(
        self, id: str, category: str, caption: str, tooltip: str
    ) -> None: ...
    def LoadState(self, path: str) -> None: ...
    def GetPaneIds(self) -> List[str]: ...
    def RegisterComboBox(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def GetToolbar(
        self, pane: str, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbar: ...
    def RegisterScriptToolHandler(
        self, toolid: str, module: str, setState: str, execute: str
    ) -> None: ...
    def SaveState(self, path: str) -> None: ...
    def RemoveCategoryHandler(self, id: str) -> None: ...
    def UpdateToolbarsStates(self) -> None: ...
    def AddToolHandler(
        self,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolHandler,
    ) -> None: ...
    def AddToolbar(
        self, paneId: str, toolbarId: str, text: str, row: int, column: int
    ) -> None: ...
    def RemoveTool(self, id: str) -> None: ...
    def AddCategoryHandler(
        self,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CategoryToolHandler,
    ) -> None: ...
    def ContainsToolbar(self, paneId: str, toolbarId: str) -> bool: ...
    def RegisterCategoryHandler(
        self,
        category: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    ) -> None: ...
    def RegisterButton(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...

    ToolExecuting: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolExecuteEventArgs
    ]  # Event

class TypeToolHandler(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolHandlerBase,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler,
    ) -> None: ...

    Type: str

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...
