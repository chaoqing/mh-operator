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

from .ViewModel import IControlPanelViewModel, IManageViewModel, ITask, ITaskGroup

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.Manage

class ConfigurationItem:  # Class
    def __init__(self) -> None: ...

    IsEnabled: bool
    Name: str  # readonly

class CopyConfigurationWindow(
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
    def __init__(self, model: IManageViewModel) -> None: ...
    def InitializeComponent(self) -> None: ...

class DeployWindow(
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

class DeploymentViewModel(System.Windows.DependencyObject):  # Class
    def __init__(self, rootModel: IControlPanelViewModel) -> None: ...

    DestinationProperty: System.Windows.DependencyProperty  # static
    EmbedConfigurationsProperty: System.Windows.DependencyProperty  # static
    LinkConfigurationsProperty: System.Windows.DependencyProperty  # static

    BrowseDestinationCommand: System.Windows.Input.ICommand  # readonly
    CommandDeploy: System.Windows.Input.ICommand  # readonly
    Configurations: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Manage.ConfigurationItem
    ]  # readonly
    Destination: str
    EmbedConfigurations: bool
    LinkConfigurations: bool

    def DoDeploy(self, parameter: Any) -> None: ...
    def ShowDialog(self, parent: System.Windows.Window) -> None: ...

class ManageGroup(ITaskGroup):  # Class
    def __init__(self, rootModel: IControlPanelViewModel) -> None: ...

    IsEnabled: bool  # readonly
    Tasks: List[ITask]  # readonly
    Title: str  # readonly

class ManageView(
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

class ManageViewModel(
    System.Windows.DependencyObject, IManageViewModel, ITask
):  # Class
    def __init__(self, rootModel: IControlPanelViewModel) -> None: ...

    CommandCopyConfiguration: System.Windows.Input.ICommand  # readonly
    CommandDeleteConfiguration: System.Windows.Input.ICommand  # readonly
    CommandEditConfiguration: System.Windows.Input.ICommand  # readonly
    CommandNewConfiguration: System.Windows.Input.ICommand  # readonly
    CommandTest: System.Windows.Input.ICommand  # readonly
    Content: System.Windows.UIElement  # readonly
    IsEnabled: bool  # readonly
    RootModel: IControlPanelViewModel  # readonly
    Title: str  # readonly

    @overload
    def DeleteSelectedConfiguration(self, parameter: Any) -> None: ...
    @overload
    def DeleteSelectedConfiguration(self) -> None: ...
    def CreateNewConfiguration(
        self,
        parent: System.Windows.Window,
        folderName: str,
        instrument: Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType,
    ) -> bool: ...
    def Deploy(self) -> None: ...
    def Leaving(self) -> bool: ...
    def CopyConfiguration(
        self, parent: System.Windows.Window, copyFrom: str, copyTo: str
    ) -> bool: ...
    @overload
    def BrowseStartupRootFolder(self, parameter: Any) -> None: ...
    @overload
    def BrowseStartupRootFolder(self) -> None: ...
    def Activate(self) -> None: ...
    def GetTools(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools: ...

class NativeMethods:  # Class
    FOF_ALLOWUNDO: int = ...  # static # readonly
    FOF_NOCONFIRMATION: int = ...  # static # readonly
    FO_COPY: int = ...  # static # readonly
    FO_DELETE: int = ...  # static # readonly
    FO_MOVE: int = ...  # static # readonly
    FO_RENAME: int = ...  # static # readonly

    @staticmethod
    def SHFileOperation(
        lpFileOp: Agilent.MassHunter.Quantitative.Startup.Edit.Manage.SHFILEOPSTRUCT,
    ) -> int: ...

class NewConfigurationWindow(
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
    def __init__(self, model: IManageViewModel) -> None: ...
    def InitializeComponent(self) -> None: ...

class SHFILEOPSTRUCT:  # Struct
    fAnyOperationsAborted: int
    fFlags: int
    hNameMappings: System.IntPtr
    hwnd: System.IntPtr
    lpszProgressTitle: str
    pFrom: System.IntPtr
    pTo: System.IntPtr
    wFunc: int

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
