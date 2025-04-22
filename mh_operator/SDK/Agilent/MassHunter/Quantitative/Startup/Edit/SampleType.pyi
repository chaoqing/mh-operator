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
    ISampleTypesViewModel,
    ITask,
    TaskViewModelBase,
)

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.SampleType

class SampleTypeItem(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.SampleType.SampleTypesViewModel,
        sampleType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleType,
        visible: bool,
    ) -> None: ...

    Caption: str
    CaptionJa: str
    CaptionRu: str
    CaptionZhHans: str
    Initializing: bool
    IsCaptionDefault: bool  # readonly
    IsCaptionJaDefault: bool  # readonly
    IsCaptionRuDefault: bool  # readonly
    IsCaptionZhHansDefault: bool  # readonly
    IsVisible: bool
    SampleType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleType
    )  # readonly

    def GetCaption(
        self, culture: System.Globalization.CultureInfo, caption: str
    ) -> str: ...

class SampleTypesView(
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

class SampleTypesViewModel(TaskViewModelBase, ISampleTypesViewModel, ITask):  # Class
    def __init__(self, rootModel: IControlPanelViewModel) -> None: ...

    DefaultColumnVisibilityProperty: System.Windows.DependencyProperty  # static
    JAColumnVisibilityProperty: System.Windows.DependencyProperty  # static
    RUColumnVisibilityProperty: System.Windows.DependencyProperty  # static
    SampleTypeItemsProperty: System.Windows.DependencyProperty  # static
    SelectedLanguageProperty: System.Windows.DependencyProperty  # static
    ZHColumnVisibilityProperty: System.Windows.DependencyProperty  # static

    CommandCheckAll: System.Windows.Input.ICommand  # readonly
    CommandUncheckAll: System.Windows.Input.ICommand  # readonly
    Content: System.Windows.UIElement  # readonly
    Cultures: List[CultureItem]  # readonly
    DefaultColumnVisibility: System.Windows.Visibility
    IsEnabled: bool  # readonly
    JAColumnVisibility: System.Windows.Visibility
    RUColumnVisibility: System.Windows.Visibility
    SampleTypeItems: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.SampleType.SampleTypeItem
    ]  # readonly
    SelectedLanguage: str
    Title: str  # readonly
    View: (
        Agilent.MassHunter.Quantitative.Startup.Edit.SampleType.SampleTypesView
    )  # readonly
    ZHColumnVisibility: System.Windows.Visibility

    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def IsDirty(self) -> bool: ...
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
