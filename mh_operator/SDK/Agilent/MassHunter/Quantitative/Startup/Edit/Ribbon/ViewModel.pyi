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

from .Model import (
    IAvailableToolCategory,
    ICustomizeRibbonModel,
    ICustomizeRibbonTarget,
    ICustomizeWindowTarget,
)
from .Tools import ITool

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel

class CustomizeRibbonViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.ICustomizeRibbonViewModel,
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ICustomizeRibbonViewModel,
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.TaskViewModelBase,
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ITask,
):  # Class
    def __init__(
        self,
        rootModel: Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.IControlPanelViewModel,
    ) -> None: ...

    SelectedToolFromProperty: System.Windows.DependencyProperty  # static
    SelectedToolToProperty: System.Windows.DependencyProperty  # static
    SelectedWindowTargetProperty: System.Windows.DependencyProperty  # static
    WindowTargetsProperty: System.Windows.DependencyProperty  # static

    AddCommand: System.Windows.Input.ICommand  # readonly
    Content: System.Windows.UIElement  # readonly
    IsEnabled: bool  # readonly
    MoveDownCommand: System.Windows.Input.ICommand  # readonly
    MoveUpCommand: System.Windows.Input.ICommand  # readonly
    NewButtonCommand: System.Windows.Input.ICommand  # readonly
    NewGroupCommand: System.Windows.Input.ICommand  # readonly
    NewMenuCommand: System.Windows.Input.ICommand  # readonly
    NewTabCommand: System.Windows.Input.ICommand  # readonly
    NewToolbarCommand: System.Windows.Input.ICommand  # readonly
    PropertiesCommand: System.Windows.Input.ICommand  # readonly
    RemoveCommand: System.Windows.Input.ICommand  # readonly
    SelectedToolFrom: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    )
    SelectedToolTo: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    )
    SelectedWindowTarget: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IWindowTargetViewModel
    )
    Title: str  # readonly
    WindowTargets: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IWindowTargetViewModel
    ]
    _Model: ICustomizeRibbonModel  # readonly

    def CanNewTab(self, parameters: Any) -> bool: ...
    def NewGroup(self, parameters: Any) -> None: ...
    def NewToolbar(self, parameter: Any) -> None: ...
    def ResetToDefault(self) -> None: ...
    @overload
    @staticmethod
    def GetImage(
        tool: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase,
    ) -> System.Windows.Media.Imaging.BitmapSource: ...
    @overload
    @staticmethod
    def GetImage(image: str) -> System.Windows.Media.Imaging.BitmapSource: ...
    def Reload(self) -> None: ...
    def CanNewGroup(self, parameters: Any) -> bool: ...
    def IsDirty(self) -> bool: ...
    def NewMenu(self, parameter: Any) -> None: ...
    def CanNewToolbar(self, parameter: Any) -> bool: ...
    def NewTab(self, parameters: Any) -> None: ...
    def NotifyTreeChanged(self) -> None: ...
    def CanNewMenu(self, parameter: Any) -> bool: ...
    def CanNewButton(self, parameter: Any) -> bool: ...
    def Activate(self) -> None: ...
    def NewButton(self, parameters: Any) -> None: ...
    def GetTools(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools: ...

class ICustomizeRibbonViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ICustomizeRibbonViewModel,
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ITask,
):  # Interface
    AddCommand: System.Windows.Input.ICommand  # readonly
    MoveDownCommand: System.Windows.Input.ICommand  # readonly
    MoveUpCommand: System.Windows.Input.ICommand  # readonly
    NewButtonCommand: System.Windows.Input.ICommand  # readonly
    NewGroupCommand: System.Windows.Input.ICommand  # readonly
    NewMenuCommand: System.Windows.Input.ICommand  # readonly
    NewTabCommand: System.Windows.Input.ICommand  # readonly
    PropertiesCommand: System.Windows.Input.ICommand  # readonly
    RemoveCommand: System.Windows.Input.ICommand  # readonly
    SelectedToolFrom: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    )
    SelectedToolTo: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    )
    SelectedWindowTarget: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IWindowTargetViewModel
    )
    WindowTargets: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IWindowTargetViewModel
    ]  # readonly
    _Model: ICustomizeRibbonModel  # readonly

    def NotifyTreeChanged(self) -> None: ...

class IRibbonTargetViewModel(object):  # Interface
    Children: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    ]  # readonly
    DisplayName: str  # readonly
    Name: str  # readonly
    Target: ICustomizeRibbonTarget  # readonly

class IToolCategoryViewModel(object):  # Interface
    DisplayName: str  # readonly
    Name: str  # readonly
    Tools: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    ]  # readonly

class IToolViewModel(object):  # Interface
    Caption: str  # readonly
    Children: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    ]  # readonly
    Image: System.Windows.Media.ImageSource  # readonly
    IsExpanded: bool
    IsSelected: bool
    Parent: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    )  # readonly
    Tool: ITool  # readonly
    Tooltip: str  # readonly
    TooltipFooter: str  # readonly
    TypeImage: System.Windows.Media.ImageSource  # readonly

class IWindowTargetViewModel(object):  # Interface
    AvailableToolCategories: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolCategoryViewModel
    ]  # readonly
    CustomizeRibbonViewModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.ICustomizeRibbonViewModel
    )  # readonly
    DisplayName: str  # readonly
    Name: str  # readonly
    RibbonTargets: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IRibbonTargetViewModel
    ]  # readonly
    SelectedRibbonTarget: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IRibbonTargetViewModel
    )
    SelectedToolCategory: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolCategoryViewModel
    )
    Target: ICustomizeWindowTarget  # readonly

class RibbonTargetViewModel(
    System.Windows.DependencyObject,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IRibbonTargetViewModel,
):  # Class
    def __init__(
        self,
        viewModel: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IWindowTargetViewModel,
        target: ICustomizeRibbonTarget,
    ) -> None: ...

    ChildrenProperty: System.Windows.DependencyProperty  # static

    Children: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    ]
    DisplayName: str  # readonly
    Name: str  # readonly
    Target: ICustomizeRibbonTarget  # readonly

class ToolCategoryViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolCategoryViewModel
):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IWindowTargetViewModel,
        cat: IAvailableToolCategory,
    ) -> None: ...

    DisplayName: str  # readonly
    Name: str  # readonly
    Tools: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    ]  # readonly

class ToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler
):  # Class
    def __init__(self) -> None: ...
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

class ToolViewModel(
    System.Windows.DependencyObject,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel,
):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IWindowTargetViewModel,
        parent: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel,
        tool: ITool,
    ) -> None: ...

    CaptionProperty: System.Windows.DependencyProperty  # static
    ChildrenProperty: System.Windows.DependencyProperty  # static
    ImageProperty: System.Windows.DependencyProperty  # static
    IsExpandedProperty: System.Windows.DependencyProperty  # static
    IsSelectedProperty: System.Windows.DependencyProperty  # static
    TooltipProperty: System.Windows.DependencyProperty  # static

    Caption: str  # readonly
    Children: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    ]
    Image: System.Windows.Media.ImageSource
    IsExpanded: bool
    IsSelected: bool
    Parent: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolViewModel
    )  # readonly
    Tool: ITool  # readonly
    Tooltip: str
    TooltipFooter: str  # readonly
    TooltipFooterVisibility: System.Windows.Visibility  # readonly
    TypeImage: System.Windows.Media.ImageSource  # readonly

class WindowTargetViewModel(
    System.Windows.DependencyObject,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IWindowTargetViewModel,
):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.ICustomizeRibbonViewModel,
        target: ICustomizeWindowTarget,
    ) -> None: ...

    SelectedRibbonTargetProperty: System.Windows.DependencyProperty  # static # readonly
    SelectedToolCategoryProperty: System.Windows.DependencyProperty  # static # readonly

    AvailableToolCategories: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolCategoryViewModel
    ]  # readonly
    CustomizeRibbonViewModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.ICustomizeRibbonViewModel
    )  # readonly
    DisplayName: str  # readonly
    Name: str  # readonly
    RibbonTargets: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IRibbonTargetViewModel
    ]  # readonly
    SelectedRibbonTarget: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IRibbonTargetViewModel
    )
    SelectedToolCategory: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.ViewModel.IToolCategoryViewModel
    )
    Target: ICustomizeWindowTarget  # readonly
