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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2

class ButtonDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...

class CategoryHandlerDefinition:  # Class
    def __init__(self) -> None: ...

    Category: str
    HandlerType: str

class ComboBoxDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...

    DropDownStyle: System.Windows.Forms.ComboBoxStyle

class ContextMenuDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.MenuDefinition
):  # Class
    def __init__(self) -> None: ...

    Pane: str

class IComboBox(object):  # Interface
    Count: int  # readonly
    DroppedDown: bool  # readonly
    Id: str  # readonly
    def __getitem__(self, index: int) -> Any: ...
    SelectedItem: Any

    def Clear(self) -> None: ...
    def Add(self, item: Any) -> None: ...

class IDropDownHandler(object):  # Interface
    def DropDownOpening(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IDropDownTool,
        objState: Any,
    ) -> None: ...

class IDropDownTool(object):  # Interface
    Count: int  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool: ...
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool: ...
    def Add(self, id: str) -> None: ...
    def RegisterDropDownOpening(
        self,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IDropDownHandler,
        register: bool,
    ) -> None: ...
    def Clear(self) -> None: ...
    def IndexOf(self, id: str) -> int: ...
    def Remove(self, id: str) -> None: ...
    def Insert(self, id: str, index: int) -> None: ...
    def InsertSeparator(self, index: int) -> None: ...
    def RemoveAt(self, index: int) -> None: ...

class ITextBox(object):  # Interface
    Text: str

class ITool(object):  # Interface
    Checked: bool
    Enabled: bool
    Id: str  # readonly
    IsComboBox: bool  # readonly
    IsDropDownTool: bool  # readonly
    IsTextBox: bool  # readonly

class IToolComboBoxHandler(object):  # Interface
    def SelectedIndexChanged(
        self,
        comboBox: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IComboBox,
        uiState: Any,
    ) -> None: ...
    def DropDown(
        self,
        comboBox: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IComboBox,
        uiState: Any,
    ) -> None: ...
    def DropDownClosed(
        self,
        comboBox: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IComboBox,
        uiState: Any,
    ) -> None: ...

class IToolHandler(object):  # Interface
    def Execute(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
        uiState: Any,
    ) -> None: ...
    def SetState(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
        uiState: Any,
    ) -> None: ...

class IToolManager(object):  # Interface
    def ContainsCategoryHandler(self, category: str) -> bool: ...
    def RegisterCategoryHandler(
        self,
        category: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    ) -> None: ...
    def AddToolbar(self, paneId: str, toolbarId: str, text: str) -> None: ...
    def RegisterTool(
        self, id: str, category: str, caption: str, tooltipText: str
    ) -> None: ...
    def RemoveTool(self, id: str) -> None: ...
    def ContainsTool(self, id: str) -> bool: ...
    def RevokeTool(self, id: str) -> None: ...
    def InvokeMouseAction(
        self,
        pane: str,
        button: str,
        mact: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.MouseAction,
        state: str,
    ) -> None: ...
    def RemoveToolbar(self, paneId: str, toolbarId: str) -> None: ...
    def ContainsToolbar(self, paneId: str, toolbarId: str) -> bool: ...
    def GetTools(
        self, id: str
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool]: ...

class IToolTextBoxHandler(object):  # Interface
    def TextChanged(
        self,
        textBox: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITextBox,
        uiState: Any,
    ) -> None: ...
    def Leave(
        self,
        textBox: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITextBox,
        uiState: Any,
    ) -> None: ...
    def Enter(
        self,
        textBox: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITextBox,
        uiState: Any,
    ) -> None: ...
    def KeyPress(
        self,
        textBox: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITextBox,
        e: System.Windows.Forms.KeyPressEventArgs,
        uiState: Any,
    ) -> None: ...

class LabelDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...

class MenuBarDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ToolbarDefinition
):  # Class
    def __init__(self) -> None: ...

class MenuDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...

    ShortcutKeys: System.Windows.Forms.Keys

class MouseAction(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Click: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.MouseAction = (
        ...
    )  # static # readonly
    DoubleClick: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.MouseAction
    ) = ...  # static # readonly

class MouseActionKey:  # Class
    def __init__(self) -> None: ...

    Button: str
    MouseAction: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.MouseAction
    Pane: str
    State: str

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class MouseActionMap(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.MouseActionKey
):  # Class
    def __init__(self) -> None: ...

    Action: str

class SeparatorDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...

class TextBoxDefinition(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ToolDefinitionBase
):  # Class
    def __init__(self) -> None: ...

class ToolDefinitionBase:  # Class
    Alignment: System.Windows.Forms.ToolStripItemAlignment
    Caption: str
    Category: str
    DisplayStyle: System.Windows.Forms.ToolStripItemDisplayStyle
    Id: str
    Image: str
    Tools: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ToolDefinitionBase
    ]
    Tooltip: str
    Visible: bool

class ToolDefinitions:  # Class
    def __init__(self) -> None: ...

    CategoryHandlers: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.CategoryHandlerDefinition
    ]
    ContextMenus: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ContextMenuDefinition
    ]
    Toolbars: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ToolbarDefinition
    ]

class ToolManager(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
):  # Class
    def __init__(self) -> None: ...

    UIState: Any

    def RegisterCategoryHandler(
        self,
        key: str,
        handler: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    ) -> None: ...
    @overload
    def SetToolState(
        self, tools: System.Windows.Forms.ToolStripItemCollection
    ) -> None: ...
    @overload
    def SetToolState(self, item: System.Windows.Forms.ToolStripItem) -> None: ...
    def InitializeTools(
        self,
        resMgr: System.Resources.ResourceManager,
        panes: Dict[str, System.Windows.Forms.Control],
        definitionsStream: System.IO.Stream,
    ) -> None: ...
    def RegisterTool(
        self, id: str, category: str, caption: str, tooltip: str
    ) -> None: ...
    def RevokeTool(self, id: str) -> None: ...
    def FindItemByShortcut(
        self, key: System.Windows.Forms.Keys
    ) -> System.Windows.Forms.ToolStripMenuItem: ...
    def InvokeMouseAction(
        self,
        pane: str,
        button: str,
        mact: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.MouseAction,
        state: str,
    ) -> None: ...
    def UpdateToolState(self, control: System.Windows.Forms.Control) -> None: ...
    def GetContextMenu(self, id: str) -> System.Windows.Forms.ContextMenuStrip: ...
    def Dispose(self) -> None: ...
    def GetTools(
        self, id: str
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool]: ...

class ToolbarDefinition:  # Class
    def __init__(self) -> None: ...

    DockStyle: System.Windows.Forms.DockStyle
    GripStyle: System.Windows.Forms.ToolStripGripStyle
    LayoutStyle: System.Windows.Forms.ToolStripLayoutStyle
    Name: str
    Pane: str
    RenderMode: System.Windows.Forms.ToolStripRenderMode
    Tools: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ToolDefinitionBase
    ]
    Visible: bool
