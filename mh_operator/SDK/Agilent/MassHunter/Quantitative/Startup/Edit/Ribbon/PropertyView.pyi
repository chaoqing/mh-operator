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

from .Tools import (
    IApplicationMenu2010,
    IApplicationMenu2010Item,
    IContextMenu,
    IGroup,
    IMenu,
    ITabItem,
    ITool,
    IToolbar,
)
from .ViewModel import ICustomizeRibbonViewModel, IWindowTargetViewModel

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView

class ApplicationMenuItemViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView.ToolViewModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self, model: IWindowTargetViewModel, item: IApplicationMenu2010Item
    ) -> None: ...

    Title: str  # readonly

class ApplicationMenuViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView.ToolViewModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self, model: IWindowTargetViewModel, am: IApplicationMenu2010
    ) -> None: ...

    Title: str  # readonly

class ButtonView(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class ButtonViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView.ToolViewModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self, model: IWindowTargetViewModel, tool: ITool) -> None: ...

    BrowseLargeImage: System.Windows.Input.ICommand  # readonly
    BrowseSmallImage: System.Windows.Input.ICommand  # readonly
    MaximumSize: Optional[Infragistics.Windows.Ribbon.RibbonToolSizingMode]
    MaximumSizeItems: List[Any]  # readonly
    MenuTypeVisibility: System.Windows.Visibility  # readonly
    MinimumSize: Optional[Infragistics.Windows.Ribbon.RibbonToolSizingMode]
    ScriptExecute: str
    ScriptModule: str
    ScriptSetState: str
    Title: str  # readonly

    def DoDefault(self) -> None: ...
    def DoOK(self) -> None: ...

class ChooseImageWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...

    SelectedImage: str

    def InitializeComponent(self) -> None: ...

class ChooseImageWindowModel(System.Windows.DependencyObject):  # Class
    def __init__(self) -> None: ...

    SelectedItemProperty: System.Windows.DependencyProperty  # static # readonly

    ImageItems: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView.ChooseImageWindowModel.ImageItem
    ]  # readonly
    SelectedImage: str
    SelectedItem: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView.ChooseImageWindowModel.ImageItem
    )

    # Nested Types

    class ImageItem:  # Class
        def __init__(self) -> None: ...

        Image: System.Windows.Media.ImageSource
        ImageHeight: float  # readonly
        ImageWidth: float  # readonly
        Name: str

class ContextMenuView(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class ContextMenuViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView.ToolViewModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self, model: IWindowTargetViewModel, contextmenu: IContextMenu
    ) -> None: ...

    Title: str  # readonly
    Visible: bool

    def DoDefault(self) -> None: ...
    def DoOK(self) -> None: ...

class GroupView(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class GroupViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView.ToolViewModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self, model: IWindowTargetViewModel, group: IGroup) -> None: ...

    BrowseImage: System.Windows.Input.ICommand  # readonly
    Title: str  # readonly

    def DoDefault(self) -> None: ...

class MenuViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView.ButtonViewModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self, model: IWindowTargetViewModel, menu: IMenu) -> None: ...

    ButtonType: Infragistics.Windows.Ribbon.MenuToolButtonType
    ButtonTypeItems: List[Any]  # readonly
    MenuTypeVisibility: System.Windows.Visibility  # readonly
    Title: str  # readonly

    def DoDefault(self) -> None: ...
    def DoOK(self) -> None: ...

class PropertiesViewModel:  # Class
    def __init__(
        self,
        model: IWindowTargetViewModel,
        parentWindow: System.Windows.Window,
        tool: ITool,
    ) -> None: ...

    CancelCommand: System.Windows.Input.ICommand  # readonly
    ContentModel: Any
    DefaultCommand: System.Windows.Input.ICommand  # readonly
    OkCommand: System.Windows.Input.ICommand  # readonly

class PropertiesWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class TabItemView(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class TabItemViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView.ToolViewModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self, model: IWindowTargetViewModel, tabItem: ITabItem) -> None: ...

    Title: str  # readonly

class ToolViewModel(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self, model: IWindowTargetViewModel, tool: ITool) -> None: ...

    Caption: str
    CustomizeRibbonViewModel: ICustomizeRibbonViewModel  # readonly
    ID: str
    IsIDReadOnly: bool  # readonly
    LargeImage: System.Windows.Media.ImageSource  # readonly
    SmallImage: System.Windows.Media.ImageSource  # readonly
    Title: str  # readonly
    Tooltip: str
    UseDefaultCaption: bool
    UseDefaultTooltip: bool
    WindowTargetViewModel: IWindowTargetViewModel  # readonly
    _LargeImage: str
    _SmallImage: str

    def DoDefault(self) -> None: ...
    def DoOK(self) -> None: ...
    @overload
    def GetCaption(
        self, tool: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
    ) -> str: ...
    @overload
    def GetCaption(self, id: str) -> str: ...

class ToolbarView(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class ToolbarViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.PropertyView.ToolViewModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self, model: IWindowTargetViewModel, toolbar: IToolbar) -> None: ...

    Title: str  # readonly

    @overload
    def GetCaption(self, id: str) -> str: ...
    @overload
    def GetCaption(
        self, tool: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
    ) -> str: ...
