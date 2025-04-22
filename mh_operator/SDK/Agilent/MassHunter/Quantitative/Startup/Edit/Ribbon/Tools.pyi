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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools

class ApplicationMenu2010(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolsBase,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IApplicationMenu2010,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        appMenu: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ApplicationMenu2010,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...
    def Insert(
        self,
        child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
        after: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    ) -> None: ...
    def Commit(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...

class ApplicationMenu2010Item(
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IApplicationMenu2010Item,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolBase,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        item: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ApplicationMenu2010Item,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

class ApplicationMenu2010ItemSeparator(
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IApplicationMenu2010Item,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolBase,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        separator: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ApplicationMenu2010ItemSeparator,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

    Caption: str  # readonly

class Button(
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IButton,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolBase,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        button: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Button,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

class CheckButton(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolBase,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ICheckButton,
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IButton,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        button: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.CheckButton,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

class ComboBox(
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IComboBox,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolBase,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        comboBox: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ComboBox,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

class ContextMenu(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolsBase,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IContextMenu,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        contextMenu: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ContextMenu,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

    Caption: str  # readonly

    def Commit(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...

class Group(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolsBase,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IGroup,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        group: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Group,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...
    def Insert(
        self,
        child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
        after: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    ) -> None: ...
    def Commit(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...

class IApplicationMenu2010(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
):  # Interface
    ...

class IApplicationMenu2010Item(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
):  # Interface
    ...

class IButton(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
):  # Interface
    ...

class ICheckButton(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IButton,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
):  # Interface
    ...

class IComboBox(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
):  # Interface
    ...

class IContextMenu(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
):  # Interface
    ...

class IGroup(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
):  # Interface
    ...

class ILabel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
):  # Interface
    ...

class IMenu(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
):  # Interface
    ...

class ISeparator(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
):  # Interface
    ...

class ITabItem(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
):  # Interface
    ...

class ITextBox(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
):  # Interface
    ...

class ITool(object):  # Interface
    Caption: str
    LargeImage: str
    Parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools  # readonly
    SmallImage: str
    Tool: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase  # readonly
    ToolString: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString
    )  # readonly
    Tooltip: str

    def Commit(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...

class IToolString(object):  # Interface
    @overload
    def GetToolbarCaption(
        self, toolbar: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolbarDef
    ) -> str: ...
    @overload
    def GetToolbarCaption(self, id: str) -> str: ...
    def GetCategoryDisplayName(self, category: str) -> str: ...
    @overload
    def GetToolTooltip(
        self, tool: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
    ) -> str: ...
    @overload
    def GetToolTooltip(self, id: str) -> str: ...
    def GetContextMenuDisplayName(self, id: str) -> str: ...
    @overload
    def GetToolCaption(
        self, tool: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
    ) -> str: ...
    @overload
    def GetToolCaption(self, id: str) -> str: ...

class IToolbar(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
):  # Interface
    ...

class ITools(object):  # Interface
    Children: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ]  # readonly

    def MoveDown(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> None: ...
    def MoveUp(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> None: ...
    def CanMoveDown(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> bool: ...
    def CanInsert(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> bool: ...
    def Remove(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> None: ...
    def Insert(
        self,
        child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
        after: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    ) -> None: ...
    def CanMoveUp(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> bool: ...

class IWrapPanel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
):  # Interface
    ...

class Label(
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ILabel,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolBase,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        label: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Label,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

class Menu(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolsBase,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IMenu,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        menu: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Menu,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...
    def Commit(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...

class Separator(
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ISeparator,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolBase,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        separator: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Separator,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

    Caption: str  # readonly

class TabItem(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolsBase,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITabItem,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        item: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.TabItem,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...
    def Commit(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...
    def CanInsert(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> bool: ...

class TextBox(
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITextBox,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolBase,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        textBox: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.TextBox,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

class ToolBase(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    Caption: str
    LargeImage: str
    Parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools  # readonly
    SmallImage: str
    Tool: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase  # readonly
    ToolString: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString
    )  # readonly
    Tooltip: str

    def Commit(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...

class Toolbar(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolsBase,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolbar,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        toolbar: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolbarDef,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

    Caption: str  # readonly

    def Commit(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...

class ToolsBase(
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolBase,
):  # Class
    Children: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ]  # readonly

    def MoveDown(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> None: ...
    def MoveUp(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> None: ...
    def CanMoveDown(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> bool: ...
    def CanInsert(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> bool: ...
    def Remove(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> None: ...
    def Insert(
        self,
        child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
        after: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    ) -> None: ...
    def CanMoveUp(
        self, child: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool
    ) -> bool: ...

class WrapPanel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ToolsBase,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITool,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IWrapPanel,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.ITools,
        wrapPanel: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.WrapPanel,
        toolString: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Tools.IToolString,
    ) -> None: ...

    Caption: str  # readonly

    def Commit(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...
