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

from .ViewModel import (
    IBatchTableViewModel,
    IColumnLabelsViewModel,
    IControlPanelViewModel,
    ICustomizeRibbonViewModel,
    IGeneralSettingsViewModel,
    IManageViewModel,
    IOutliersViewModel,
    ISampleTypesViewModel,
    ITask,
    ITaskGroup,
)

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.MainView

class ControlPanelGroup(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.MainView.ControlPanelViewModel,
        group: ITaskGroup,
    ) -> None: ...

    Group: ITaskGroup  # readonly
    Model: (
        Agilent.MassHunter.Quantitative.Startup.Edit.MainView.ControlPanelViewModel
    )  # readonly
    Tasks: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.MainView.ControlPanelTask
    ]  # readonly

class ControlPanelTask(System.Windows.DependencyObject):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.MainView.ControlPanelViewModel,
        task: ITask,
    ) -> None: ...

    IsSelectedProperty: System.Windows.DependencyProperty  # static

    IsSelected: bool
    Task: ITask  # readonly

class ControlPanelViewModel(
    System.Windows.DependencyObject, IControlPanelViewModel
):  # Class
    def __init__(
        self, window: Agilent.MassHunter.Quantitative.Startup.Edit.MainView.MainWindow
    ) -> None: ...

    AlwaysLoadConfigurationProperty: System.Windows.DependencyProperty  # static
    ConfigurationsProperty: System.Windows.DependencyProperty  # static
    DefaultConfigurationProperty: System.Windows.DependencyProperty  # static
    IsStartupRootFolderValidProperty: System.Windows.DependencyProperty  # static
    SelectedConfigurationProperty: System.Windows.DependencyProperty  # static
    SelectedTaskProperty: System.Windows.DependencyProperty  # static
    StartupRootFolderProperty: System.Windows.DependencyProperty  # static
    UserCanChooseConfigurationProperty: System.Windows.DependencyProperty  # static
    WindowTitleProperty: System.Windows.DependencyProperty  # static

    AlwaysLoadConfiguration: bool
    BatchTableViewModel: IBatchTableViewModel  # readonly
    ColumnLabelsViewModel: IColumnLabelsViewModel  # readonly
    Configurations: List[str]  # readonly
    CustomizeRibbonViewModel: ICustomizeRibbonViewModel  # readonly
    DefaultConfiguration: str
    GeneralSettingsViewModel: IGeneralSettingsViewModel  # readonly
    Groups: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.MainView.ControlPanelGroup
    ]  # readonly
    IsStartupRootFolderValid: bool  # readonly
    ManageViewModel: IManageViewModel  # readonly
    OutliersViewModel: IOutliersViewModel  # readonly
    SampleTypesViewModel: ISampleTypesViewModel  # readonly
    SelectedConfiguration: str
    SelectedTask: Agilent.MassHunter.Quantitative.Startup.Edit.MainView.ControlPanelTask
    StartupRootFolder: str
    TaskSelector: (
        Agilent.MassHunter.Quantitative.Startup.Edit.MainView.TaskSelector
    )  # readonly
    UserCanChooseConfiguration: bool
    Window: System.Windows.Window  # readonly
    WindowTitle: str

    def Initialize(self) -> None: ...
    def UpdateConfigurations(self) -> None: ...
    def EditSelectedConfiguration(self) -> None: ...

class MainWindow(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IWindowService,
    Infragistics.Windows.Ribbon.IRibbonWindow,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Animation.IAnimatable,
    System.ComponentModel.ISupportInitialize,
    Infragistics.Windows.Ribbon.XamRibbonWindow,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...

    ToolManager: (
        Agilent.MassHunter.Quantitative.Startup.Edit.MainView.ToolManager
    )  # readonly

    def InitializeComponent(self) -> None: ...

class TaskSelector:  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.MainView.ControlPanelViewModel,
    ) -> None: ...

    SelectedTask: Agilent.MassHunter.Quantitative.Startup.Edit.MainView.ControlPanelTask

class ToolManager(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.ToolManagerBase,
):  # Class
    def __init__(
        self, ribbon: Infragistics.Windows.Ribbon.XamRibbon, uiState: Any
    ) -> None: ...
    def GetToolCaption(self, id: str) -> str: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def RegisterScriptToolHandler(
        self, id: str, module: str, setState: str, execute: str
    ) -> None: ...
    def GetImage(self, image: str) -> System.Windows.Media.Imaging.BitmapSource: ...
