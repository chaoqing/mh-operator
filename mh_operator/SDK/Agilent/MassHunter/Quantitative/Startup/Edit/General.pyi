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

from .Utils import CultureItem
from .ViewModel import (
    IControlPanelViewModel,
    IGeneralSettingsViewModel,
    ITask,
    ITaskGroup,
    TaskViewModelBase,
)

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.General

class DemoTask(ITask):  # Class
    def __init__(self, title: str) -> None: ...

    Content: System.Windows.UIElement  # readonly
    IsEnabled: bool  # readonly
    Title: str  # readonly

    def Leaving(self) -> bool: ...
    def GetTools(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools: ...
    def Activate(self) -> None: ...

class EditStartupTaskGroup(System.Windows.DependencyObject, ITaskGroup):  # Class
    def __init__(self, model: IControlPanelViewModel) -> None: ...

    IsEnabledProperty: System.Windows.DependencyProperty  # static

    IsEnabled: bool  # readonly
    Tasks: List[ITask]  # readonly
    Title: str  # readonly

class GeneralSettingsView(
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

class GeneralSettingsViewModel(
    TaskViewModelBase, IGeneralSettingsViewModel, ITask
):  # Class
    def __init__(self, rootModel: IControlPanelViewModel) -> None: ...

    AllowFlexibleDockingProperty: System.Windows.DependencyProperty  # static
    DisplayNameHintProperty: System.Windows.DependencyProperty  # static
    DisplayNameProperty: System.Windows.DependencyProperty  # static
    InstrumentTypeProperty: System.Windows.DependencyProperty  # static
    IsEnabledProperty: System.Windows.DependencyProperty  # static
    SelectedLanguageProperty: System.Windows.DependencyProperty  # static

    AllowFlexibleDocking: bool
    Content: System.Windows.UIElement  # readonly
    DisplayName: str
    DisplayNameHint: str
    InstrumentItems: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.EnumItem[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType
        ]
    ]  # readonly
    InstrumentType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType
    IsEnabled: bool  # readonly
    Languages: List[CultureItem]  # readonly
    SelectedLanguage: str
    Title: str  # readonly

    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def IsDirty(self) -> bool: ...
    def Leaving(self) -> bool: ...
    def Activate(self) -> None: ...
    def GetTools(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools: ...

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
