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
from .ToolManager import IToolManager
from .ToolState import IToolState, PaneToolbar

# Stubs for namespace: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions

class ApplicationCommand(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
):  # Class
    def __init__(self) -> None: ...

    Command: str

    def Build(
        self, ribbon: Infragistics.Windows.Ribbon.XamRibbon, toolManager: IToolManager
    ) -> None: ...

class ApplicationMenu2010(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
):  # Class
    def __init__(self) -> None: ...

    Items: List[
        Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ApplicationMenu2010Item
    ]

    def GetHashCode(self) -> int: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ApplicationMenu2010: ...
    def Build(
        self,
        menu2010: Infragistics.Windows.Ribbon.ApplicationMenu2010,
        toolManager: IToolManager,
    ) -> Infragistics.Windows.Ribbon.ApplicationMenu2010: ...
    def Equals(self, obj: Any) -> bool: ...

class ApplicationMenu2010Item(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Menu
):  # Class
    def __init__(self) -> None: ...

    CloseAppMenu: bool
    InitialSelected: bool
    IsTab: bool

    def ShallowCopy(
        self,
    ) -> (
        Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ApplicationMenu2010Item
    ): ...
    def Build(self, toolMgr: IToolManager) -> Any: ...

class ApplicationMenu2010ItemSeparator(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ApplicationMenu2010Item
):  # Class
    def __init__(self) -> None: ...
    def ShallowCopy(
        self,
    ) -> (
        Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ApplicationMenu2010ItemSeparator
    ): ...
    def Build(self, toolManager: IToolManager) -> Any: ...

class ApplicationMenu2010TabCommand(System.Windows.Input.ICommand):  # Class
    def __init__(self, toolManager: IToolManager, toolState: IToolState) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Execute(self, parameter: Any) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class Button(Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase):  # Class
    def __init__(self) -> None: ...
    def Equals(self, obj: Any) -> bool: ...
    def Build(
        self, toolManager: IToolManager, imageColor: System.Windows.Media.Color
    ) -> Any: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Button: ...
    def BuildContextMenuItem(self, toolManager: IToolManager) -> Any: ...
    def BuildToolbarItem(self, toolManager: IToolManager) -> Any: ...
    def GetHashCode(self) -> int: ...

class CheckButton(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Button
):  # Class
    def __init__(self) -> None: ...

    HasGlyph: bool

    def Equals(self, obj: Any) -> bool: ...
    def Build(
        self, toolManager: IToolManager, imageColor: System.Windows.Media.Color
    ) -> Any: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.CheckButton: ...
    def BuildToolbarItem(self, toolManager: IToolManager) -> Any: ...
    def GetHashCode(self) -> int: ...

class ComboBox(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
):  # Class
    def __init__(self) -> None: ...

    Width: int

    def Equals(self, obj: Any) -> bool: ...
    def Build(self, toolManager: IToolManager) -> Any: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ComboBox: ...
    def BuildToolbarItem(self, toolManager: IToolManager) -> Any: ...
    def GetHashCode(self) -> int: ...

class Command(System.Windows.Input.ICommand, System.IDisposable):  # Class
    def __init__(self, toolManager: IToolManager) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Dispose(self) -> None: ...
    def Execute(self, parameter: Any) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class ContextMenu(Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Menu):  # Class
    def __init__(self) -> None: ...

    Pane: str

    def GetHashCode(self) -> int: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ContextMenu: ...
    def BuildContextMenu(
        self, toolManager: IToolManager
    ) -> System.Windows.Controls.ContextMenu: ...
    def Equals(self, obj: Any) -> bool: ...

class ContextualTabGroup:  # Class
    def __init__(self) -> None: ...

    ID: str
    TabItems: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.TabItem]

    def GetHashCode(self) -> int: ...
    def Build(
        self, toolManager: IToolManager
    ) -> Infragistics.Windows.Ribbon.ContextualTabGroup: ...
    def Equals(self, obj: Any) -> bool: ...

class ExplorerBar(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
):  # Class
    def __init__(self) -> None: ...

    Groups: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Group]

    def GetHashCode(self) -> int: ...
    def Build(
        self,
        toolManager: IToolManager,
        parent: System.Windows.Controls.Panel,
        imageResources: System.Resources.ResourceManager,
    ) -> None: ...
    def Equals(self, obj: Any) -> bool: ...

class Gallery(Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase):  # Class
    def __init__(self) -> None: ...

    Groups: List[
        Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.GalleryItemGroup
    ]
    Items: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.GalleryItem]
    MaxPreviewColumns: int
    MinPreviewColumns: int
    ToolItemBehavior: Infragistics.Windows.Ribbon.GalleryToolItemBehavior

    def Build(self, toolManager: IToolManager) -> Any: ...

class GalleryItem(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
):  # Class
    def __init__(self) -> None: ...
    def _Build(
        self, toolManager: IToolManager
    ) -> Infragistics.Windows.Ribbon.GalleryItem: ...

class GalleryItemGroup:  # Class
    def __init__(self) -> None: ...

    ID: str
    ItemKeys: List[str]

    def Build(
        self, toolManager: IToolManager
    ) -> Infragistics.Windows.Ribbon.GalleryItemGroup: ...

class Group(Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase):  # Class
    def __init__(self) -> None: ...

    Expanded: bool
    Tools: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase]

    def Equals(self, obj: Any) -> bool: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Group: ...
    def GetHashCode(self) -> int: ...
    def BuildGroup(
        self, toolManager: IToolManager
    ) -> Infragistics.Windows.Ribbon.RibbonGroup: ...
    def BuildTasks(self, toolManager: IToolManager) -> System.Windows.UIElement: ...

class Label(Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase):  # Class
    def __init__(self) -> None: ...
    def Equals(self, obj: Any) -> bool: ...
    def Build(self, toolManager: IToolManager) -> Any: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Label: ...
    def BuildToolbarItem(self, toolManager: IToolManager) -> Any: ...
    def GetHashCode(self) -> int: ...

class Menu(Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Button):  # Class
    def __init__(self) -> None: ...

    ButtonType: str
    ShouldDisplayGalleryPreview: bool
    Tools: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase]

    def Equals(self, obj: Any) -> bool: ...
    def Build(self, toolManager: IToolManager) -> Any: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Menu: ...
    def BuildContextMenuItem(self, toolManager: IToolManager) -> Any: ...
    def BuildToolbarItem(self, toolManager: IToolManager) -> Any: ...
    def GetHashCode(self) -> int: ...

class MethodTasks:  # Class
    def __init__(self) -> None: ...

    Groups: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Group]

    def BuildTasks(
        self, panel: System.Windows.Controls.Panel, toolManager: IToolManager
    ) -> None: ...
    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class PopupMenu(Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Menu):  # Class
    def __init__(self) -> None: ...
    def GetHashCode(self) -> int: ...
    def BuildContextMenuItem(self, toolManager: IToolManager) -> Any: ...
    def Equals(self, obj: Any) -> bool: ...

class QuickAccessToolbar:  # Class
    def __init__(self) -> None: ...

    Items: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase]

    def GetHashCode(self) -> int: ...
    def Build(
        self, toolManager: IToolManager, ribbon: Infragistics.Windows.Ribbon.XamRibbon
    ) -> Infragistics.Windows.Ribbon.QuickAccessToolbar: ...
    def Equals(self, obj: Any) -> bool: ...

class RadioButton(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.CheckButton
):  # Class
    def __init__(self) -> None: ...
    def GetHashCode(self) -> int: ...
    def BuildContextMenuItem(self, toolManager: IToolManager) -> Any: ...
    def Equals(self, obj: Any) -> bool: ...

class Ribbon:  # Class
    def __init__(self) -> None: ...

    ApplicationMenu2010: (
        Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ApplicationMenu2010
    )
    ContextualTabGroups: List[
        Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ContextualTabGroup
    ]
    IsMinimized: bool
    QuickAccessToolbar: (
        Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.QuickAccessToolbar
    )
    TabItems: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.TabItem]

    def GetHashCode(self) -> int: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Ribbon: ...
    def Build(
        self, ribbon: Infragistics.Windows.Ribbon.XamRibbon, toolManager: IToolManager
    ) -> None: ...
    def Equals(self, obj: Any) -> bool: ...

class Separator(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
):  # Class
    def __init__(self) -> None: ...
    def Equals(self, obj: Any) -> bool: ...
    def Build(self, toolManager: IToolManager) -> Any: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Separator: ...
    def BuildToolbarItem(self, toolManager: IToolManager) -> Any: ...
    def GetHashCode(self) -> int: ...

class TabItem(Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase):  # Class
    def __init__(self) -> None: ...

    Groups: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Group]

    def GetHashCode(self) -> int: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.TabItem: ...
    def Build(self, toolManager: IToolManager) -> Any: ...
    def Equals(self, obj: Any) -> bool: ...

class TextBox(Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase):  # Class
    def __init__(self) -> None: ...

    IsReadOnly: bool
    Width: int

    def Equals(self, obj: Any) -> bool: ...
    def Build(self, toolManager: IToolManager) -> Any: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.TextBox: ...
    def BuildToolbarItem(self, toolManager: IToolManager) -> Any: ...
    def GetHashCode(self) -> int: ...

class ToolBase:  # Class
    def __init__(self) -> None: ...

    Caption: str
    Category: str
    HorizontalAlignment: System.Windows.HorizontalAlignment
    ID: str
    Key: System.Windows.Input.Key
    KeyTip: str
    LargeImage: str
    MaximumSize: str
    MinWidth: float
    MinimumSize: str
    ModifierKey: System.Windows.Input.ModifierKeys
    ScriptExecute: str
    ScriptModule: str
    ScriptSetState: str
    SmallImage: str
    Style: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolDisplayStyle
    Tooltip: str
    Visible: bool
    _Category: str
    _ID: str
    _Image: str

    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Build(
        self, toolManager: IToolManager, imageColor: System.Windows.Media.Color
    ) -> Any: ...
    @overload
    def Build(self, toolManager: IToolManager) -> Any: ...
    def GetCaption(self, toolManager: IToolManager, ribbon: bool) -> str: ...
    def BuildContextMenuItem(self, toolManager: IToolManager) -> Any: ...
    def BuildToolbarItem(self, toolManager: IToolManager) -> Any: ...
    @staticmethod
    def ConvertCaption(caption: str, ribbon: bool) -> str: ...
    @staticmethod
    def GetArrayHashCode(arr: List[Any]) -> int: ...
    @staticmethod
    def ObjectsAreEqual(o1: Any, o2: Any) -> bool: ...
    @staticmethod
    def StringsAreEqual(s1: str, s2: str) -> bool: ...
    def GetKeyTip(self, toolManager: IToolManager) -> str: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def ArraysAreEqual(arr1: List[T], arr2: List[T]) -> bool: ...
    def BuildTooltip(self, toolManager: IToolManager) -> Any: ...
    @staticmethod
    def GetObjectHashCode(obj: Any) -> int: ...

class ToolbarDef(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
):  # Class
    def __init__(self) -> None: ...

    Band: int
    BandIndex: int
    Pane: str
    Tools: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase]

    def GetHashCode(self) -> int: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolbarDef: ...
    def Build(self, toolManager: IToolManager) -> PaneToolbar: ...
    def Equals(self, obj: Any) -> bool: ...

class ToolbarExtension:  # Class
    @overload
    @staticmethod
    def ConvertImage(
        image: System.Windows.Media.Imaging.BitmapSource,
        color: System.Windows.Media.Color,
    ) -> System.Windows.Media.Imaging.BitmapSource: ...
    @overload
    @staticmethod
    def ConvertImage(
        image: System.Windows.Media.Imaging.BitmapSource,
    ) -> System.Windows.Media.Imaging.BitmapSource: ...
    @overload
    @staticmethod
    def Evaluate(
        ct: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CustomTools,
        toolManager: IToolManager,
        instrumentType: str,
    ) -> None: ...
    @overload
    @staticmethod
    def Evaluate(
        ct: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CustomTools,
        toolManager: IToolManager,
        instrumentType: str,
        explorerBarPanel: System.Windows.Controls.StackPanel,
    ) -> None: ...
    @overload
    @staticmethod
    def SetButtonContent(
        button: System.Windows.Controls.Primitives.ButtonBase,
        definition: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Button,
        toolManager: IToolManager,
    ) -> None: ...
    @overload
    @staticmethod
    def SetButtonContent(
        button: System.Windows.Controls.Primitives.ButtonBase,
        definition: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.MenuDefinition,
        toolManager: IToolManager,
    ) -> None: ...
    @staticmethod
    def ToBitmapSource(
        source: System.Drawing.Bitmap,
    ) -> System.Windows.Media.Imaging.BitmapSource: ...

class Tools(
    System.IEquatable[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools]
):  # Class
    def __init__(self) -> None: ...

    ApplicationCommands: List[
        Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ApplicationCommand
    ]
    CategoryToolHandlers: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.CategoryToolHandler
    ]
    ContextMenus: List[
        Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ContextMenu
    ]
    MouseActionMaps: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.MouseActionMap
    ]
    ToolHandlers: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.ToolHandler
    ]
    Toolbars: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolbarDef]
    XamRibbon: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Ribbon

    @staticmethod
    def ArrayAreEqual(arr1: List[T], arr2: List[T]) -> bool: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools: ...
    def Equals(
        self, tools: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools
    ) -> bool: ...

class WrapPanel(
    Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
):  # Class
    def __init__(self) -> None: ...

    Margin: str
    MaxRows: int
    MinRows: int
    Tools: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase]
    Vertical: bool

    def GetHashCode(self) -> int: ...
    def ShallowCopy(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.WrapPanel: ...
    def Build(self, toolManager: IToolManager) -> Any: ...
    def Equals(self, obj: Any) -> bool: ...
