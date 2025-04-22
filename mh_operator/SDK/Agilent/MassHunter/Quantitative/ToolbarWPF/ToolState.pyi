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

from .Definitions import (
    ApplicationCommand,
    ApplicationMenu2010Item,
    Button,
    CheckButton,
    ComboBox,
    ContextMenu,
    GalleryItem,
    Group,
    Label,
    Menu,
    Separator,
    TabItem,
    TextBox,
    ToolBase,
)
from .ToolManager import IContextMenuToolState, IToolbar, IToolManager

# Stubs for namespace: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState

class ApplicationCommandState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
):  # Class
    def __init__(
        self, toolManager: IToolManager, definition: ApplicationCommand
    ) -> None: ...

    Enabled: bool
    _Control: System.Windows.Controls.Control  # readonly

    def CanExecute(
        self, sender: Any, e: System.Windows.Input.CanExecuteRoutedEventArgs
    ) -> None: ...
    def Execute(
        self, sender: Any, e: System.Windows.Input.ExecutedRoutedEventArgs
    ) -> None: ...

class ApplicationMenu2010ToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: ApplicationMenu2010Item,
        item: Infragistics.Windows.Ribbon.ApplicationMenu2010Item,
    ) -> None: ...

    Definition: ApplicationMenu2010Item  # readonly
    DisplayStyle: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    )
    DisplayText: str
    Enabled: bool
    _Control: System.Windows.Controls.Control  # readonly

    def RemoveSelf(self) -> None: ...

class ButtonBaseToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: Button,
        button: System.Windows.Controls.Primitives.ButtonBase,
    ) -> None: ...

    DisplayStyle: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    )
    DisplayText: str
    Enabled: bool
    _Control: System.Windows.Controls.Control  # readonly

    def RemoveSelf(self) -> None: ...

class ButtonToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: Button,
        button: Infragistics.Windows.Ribbon.ButtonTool,
    ) -> None: ...

    Definition: Button  # readonly
    DisplayStyle: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    )
    DisplayText: str
    Enabled: bool
    Image: str
    _Control: System.Windows.Controls.Control  # readonly

    def RemoveSelf(self) -> None: ...

class CheckButtonToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ICheckToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: CheckButton,
        toggleButton: Infragistics.Windows.Ribbon.ToggleButtonTool,
    ) -> None: ...

    Checked: bool
    DisplayText: str
    Enabled: bool
    Image: str
    _Control: System.Windows.Controls.Control  # readonly

    def RemoveSelf(self) -> None: ...

class ComboBoxToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IComboBoxToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: ComboBox,
        comboBox: System.Windows.Controls.ComboBox,
    ) -> None: ...

    DisplayStyle: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    )
    DisplayText: str
    Enabled: bool
    IsComboBox: bool  # readonly
    IsDroppedDown: bool  # readonly
    ItemCount: int  # readonly
    SelectedIndex: int
    SelectedItem: Any
    _Control: System.Windows.Controls.Control  # readonly

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
    def RemoveSelf(self) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ComboEditorToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IComboBoxToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: ComboBox,
        combo: Infragistics.Windows.Ribbon.ComboEditorTool,
    ) -> None: ...

    Enabled: bool
    IsDroppedDown: bool  # readonly
    ItemCount: int  # readonly
    SelectedIndex: int
    SelectedItem: Any
    _Control: System.Windows.Controls.Control  # readonly

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

class ContextMenuState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IPopupMenuToolState,
    IContextMenuToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: ContextMenu,
        contextMenu: System.Windows.Controls.ContextMenu,
    ) -> None: ...

    Count: int  # readonly
    Enabled: bool
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    _Control: System.Windows.Controls.Control  # readonly

    def SetContextMenu(self, element: System.Windows.FrameworkElement) -> None: ...
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

class ExpanderBarGroupState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IExplorerBarGroup,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: Group,
        expander: System.Windows.Controls.Expander,
    ) -> None: ...

    Enabled: bool
    Expanded: bool
    _Control: System.Windows.Controls.Control  # readonly

    def Add(self, id: str) -> None: ...
    def IndexOf(self, id: str) -> int: ...
    def Remove(self, id: str) -> None: ...
    def Exists(self, id: str) -> bool: ...
    def Insert(self, index: int, id: str) -> None: ...

class GalleryItemToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
):  # Class
    def __init__(
        self,
        toolManaer: IToolManager,
        definition: GalleryItem,
        item: Infragistics.Windows.Ribbon.GalleryItem,
    ) -> None: ...

    Enabled: bool
    _Control: System.Windows.Controls.Control  # readonly

class IToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
):  # Interface
    Definition: ToolBase  # readonly
    ID: str
    IsEnabled: bool  # readonly
    QueryingCanExecute: bool

    def RemoveSelf(self) -> None: ...
    def RemoveChild(self, id: str) -> None: ...

class LabelToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: Label,
        label: System.Windows.Controls.Label,
    ) -> None: ...

    Enabled: bool
    _Control: System.Windows.Controls.Control  # readonly

    def RemoveSelf(self) -> None: ...

class MenuItemToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ICheckToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IPopupMenuToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: ToolBase,
        menuItem: System.Windows.Controls.MenuItem,
    ) -> None: ...

    Checked: bool
    Count: int  # readonly
    DisplayStyle: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    )
    Enabled: bool
    IsPopup: bool
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    _Control: System.Windows.Controls.Control  # readonly

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
    def RemoveSelf(self) -> None: ...
    def InsertSeparator(self, index: int) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class MenuToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IPopupMenuToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: Menu,
        menu: Infragistics.Windows.Ribbon.MenuTool,
    ) -> None: ...

    Count: int  # readonly
    DisplayStyle: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    )
    DisplayText: str
    Enabled: bool
    Image: str
    IsDropDownTool: bool  # readonly
    def __getitem__(
        self, id: str
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState: ...
    def __getitem__(
        self, index: int
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState: ...
    _Control: System.Windows.Controls.Control  # readonly

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
    def RemoveChild(self, id: str) -> None: ...
    def Insert(self, id: str, index: int) -> None: ...
    def RemoveSelf(self) -> None: ...
    def InsertSeparator(self, index: int) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class PaneToolbar(
    IToolbar, Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbar
):  # Class
    def __init__(self, toolManager: IToolManager) -> None: ...

    Caption: str  # readonly
    IsMenuBar: bool  # readonly
    Visible: bool
    _ToolBar: System.Windows.Controls.ToolBar  # readonly

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

class RibbonGroupState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonGroup,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: Group,
        group: Infragistics.Windows.Ribbon.RibbonGroup,
    ) -> None: ...

    Caption: str
    Enabled: bool
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    ItemCount: int  # readonly
    Visible: bool
    _Control: System.Windows.Controls.Control  # readonly

    def AddTool(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def InsertToolAfter(
        self, id: str, idAfter: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState: ...
    def RemoveTool(self, id: str) -> None: ...
    def ContainsTool(self, id: str) -> bool: ...
    def RemoveChild(self, id: str) -> None: ...

class RibbonLabelToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: Label,
        label: Infragistics.Windows.Ribbon.LabelTool,
    ) -> None: ...

    Enabled: bool
    _Control: System.Windows.Controls.Control  # readonly

class RibbonState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbon
):  # Class
    def __init__(
        self, toolManager: IToolManager, ribbon: Infragistics.Windows.Ribbon.XamRibbon
    ) -> None: ...
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

class RibbonTabState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IRibbonTab
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: TabItem,
        item: Infragistics.Windows.Ribbon.RibbonTabItem,
    ) -> None: ...

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

class SeparatorState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        sep: Separator,
        separator: System.Windows.Controls.Separator,
    ) -> None: ...

    Enabled: bool
    _Control: System.Windows.Controls.Control  # readonly

class SplitButtonToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IPopupMenuToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: Menu,
        button: Agilent.MassHunter.Quantitative.Controls.SplitToolButton,
    ) -> None: ...

    Count: int  # readonly
    Enabled: bool
    IsDropDownTool: bool  # readonly
    def __getitem__(
        self, id: str
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState: ...
    def __getitem__(
        self, index: int
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState: ...
    _Control: System.Windows.Controls.Control  # readonly

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

class TextBoxToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ITextBoxToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: TextBox,
        textBox: System.Windows.Controls.TextBox,
    ) -> None: ...

    Enabled: bool
    IsInEdit: bool  # readonly
    IsReadOnly: bool
    IsTextBox: bool  # readonly
    Text: str
    _Control: System.Windows.Controls.Control  # readonly

class TextEditorToolState(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ToolStateBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ITextBoxToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: TextBox,
        textEditor: Infragistics.Windows.Ribbon.TextEditorTool,
    ) -> None: ...

    Enabled: bool
    IsInEdit: bool  # readonly
    IsReadOnly: bool
    IsTextBox: bool  # readonly
    Text: str
    _Control: System.Windows.Controls.Control  # readonly

class ToggleButtonToolState(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ICheckToolState,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.ButtonBaseToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
):  # Class
    def __init__(
        self,
        toolManager: IToolManager,
        definition: CheckButton,
        button: System.Windows.Controls.Primitives.ToggleButton,
    ) -> None: ...

    Checked: bool

    def RemoveSelf(self) -> None: ...

class ToolStateBase(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolState.IToolState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
):  # Class
    def __init__(self, toolManager: IToolManager, tool: ToolBase) -> None: ...

    Appearance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolAppearance
    )  # readonly
    BoldText: bool
    Bounds: System.Drawing.Rectangle  # readonly
    Checked: bool
    Definition: ToolBase  # readonly
    DisplayStyle: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    )
    DisplayText: str
    Enabled: bool
    Executing: bool  # readonly
    ID: str
    Id: str  # readonly
    Image: str
    IsComboBox: bool  # readonly
    IsDropDownTool: bool  # readonly
    IsEnabled: bool  # readonly
    IsTextBox: bool  # readonly
    MaxWidth: int
    MinWidth: int
    QueryingCanExecute: bool
    Separator: bool
    ToolManager: IToolManager  # readonly
    Tooltip: str
    Width: int
    _Control: System.Windows.Controls.Control  # readonly

    @staticmethod
    def RemoveTool(
        toolManager: IToolManager, obj: System.Windows.FrameworkElement
    ) -> bool: ...
    def RemoveSelf(self) -> None: ...
    def Dispose(self) -> None: ...
    def RemoveChild(self, id: str) -> None: ...
