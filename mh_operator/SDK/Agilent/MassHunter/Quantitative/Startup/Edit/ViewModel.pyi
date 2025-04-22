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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel

class IBatchTableViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ITask
):  # Interface
    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def Save(self) -> None: ...

class IColumnLabelsViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ITask
):  # Interface
    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def Save(self) -> None: ...

class IControlPanelViewModel(object):  # Interface
    BatchTableViewModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.IBatchTableViewModel
    )  # readonly
    ColumnLabelsViewModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.IColumnLabelsViewModel
    )  # readonly
    Configurations: List[str]  # readonly
    CustomizeRibbonViewModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ICustomizeRibbonViewModel
    )  # readonly
    DefaultConfiguration: str
    GeneralSettingsViewModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.IGeneralSettingsViewModel
    )  # readonly
    ManageViewModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.IManageViewModel
    )  # readonly
    OutliersViewModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.IOutliersViewModel
    )  # readonly
    SampleTypesViewModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ISampleTypesViewModel
    )  # readonly
    SelectedConfiguration: str
    StartupRootFolder: str
    Window: System.Windows.Window  # readonly

    def UpdateConfigurations(self) -> None: ...
    def EditSelectedConfiguration(self) -> None: ...

class ICustomizeRibbonViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ITask
):  # Interface
    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def Save(self) -> None: ...

class IGeneralSettingsViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ITask
):  # Interface
    InstrumentType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType
    )  # readonly

    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def Save(self) -> None: ...

class IManageViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ITask
):  # Interface
    RootModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.IControlPanelViewModel
    )  # readonly

    def DeleteSelectedConfiguration(self) -> None: ...
    def CreateNewConfiguration(
        self,
        parent: System.Windows.Window,
        folderName: str,
        instrument: Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType,
    ) -> bool: ...
    def Deploy(self) -> None: ...
    def CopyConfiguration(
        self, parent: System.Windows.Window, copyFrom: str, copyTo: str
    ) -> bool: ...
    def BrowseStartupRootFolder(self) -> None: ...

class IOutliersViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ITask
):  # Interface
    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def Save(self) -> None: ...

class ISampleTypesViewModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ITask
):  # Interface
    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def Save(self) -> None: ...

class ITask(object):  # Interface
    Content: System.Windows.UIElement  # readonly
    IsEnabled: bool  # readonly
    Title: str  # readonly

    def Leaving(self) -> bool: ...
    def GetTools(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools: ...
    def Activate(self) -> None: ...

class ITaskGroup(object):  # Interface
    IsEnabled: bool  # readonly
    Tasks: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.ITask
    ]  # readonly
    Title: str  # readonly

class TaskViewModelBase(System.Windows.DependencyObject):  # Class
    RootModel: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ViewModel.IControlPanelViewModel
    )  # readonly

    def Leaving(self) -> bool: ...
    def IsDirty(self) -> bool: ...
    def Save(self) -> None: ...
