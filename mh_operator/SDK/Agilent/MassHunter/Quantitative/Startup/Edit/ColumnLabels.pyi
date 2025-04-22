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
    IColumnLabelsViewModel,
    IControlPanelViewModel,
    ITask,
    TaskViewModelBase,
)

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.ColumnLabels

class BindingProxy(System.Windows.ISealable, System.Windows.Freezable):  # Class
    def __init__(self) -> None: ...

    DataProperty: System.Windows.DependencyProperty  # static # readonly

    Data: Any

class CaptionColorConverter(System.Windows.Data.IValueConverter):  # Class
    def __init__(self) -> None: ...
    def ConvertBack(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...
    def Convert(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...

class ColumnLabelItem(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.ColumnLabels.ColumnLabelsViewModel,
        instrumentType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType,
        relation: str,
        column: str,
    ) -> None: ...

    Caption: str
    CaptionJa: str
    CaptionRu: str
    CaptionZhHans: str
    Column: str  # readonly
    IsCaptionDefault: bool  # readonly
    IsCaptionJaDefault: bool  # readonly
    IsCaptionRuDefault: bool  # readonly
    IsCaptionZhHansDefault: bool  # readonly
    IsHidden: bool

    def GetCaption(
        self, culture: System.Globalization.CultureInfo, caption: str
    ) -> str: ...

class ColumnLabelsView(
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

class ColumnLabelsViewModel(
    TaskViewModelBase,
    IColumnLabelsViewModel,
    ITask,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self, rootModel: IControlPanelViewModel) -> None: ...

    DefaultColumnVisibilityProperty: System.Windows.DependencyProperty  # static
    JAColumnVisibilityProperty: System.Windows.DependencyProperty  # static
    RUColumnVisibilityProperty: System.Windows.DependencyProperty  # static
    SelectedLanguageProperty: System.Windows.DependencyProperty  # static
    SelectedRelationProperty: System.Windows.DependencyProperty  # static
    ZHColumnVisibilityProperty: System.Windows.DependencyProperty  # static

    ColumnLabelItems: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.ColumnLabels.ColumnLabelItem
    ]
    CommandCheckAll: System.Windows.Input.ICommand  # readonly
    CommandUncheckAll: System.Windows.Input.ICommand  # readonly
    Content: System.Windows.UIElement  # readonly
    DefaultColumnVisibility: System.Windows.Visibility
    Initializing: bool  # readonly
    IsEnabled: bool  # readonly
    JAColumnVisibility: System.Windows.Visibility
    Languages: List[CultureItem]  # readonly
    RUColumnVisibility: System.Windows.Visibility
    Relations: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.ColumnLabels.RelationItem
    ]  # readonly
    SelectedLanguage: str
    SelectedRelation: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ColumnLabels.RelationItem
    )
    Title: str  # readonly
    View: (
        Agilent.MassHunter.Quantitative.Startup.Edit.ColumnLabels.ColumnLabelsView
    )  # readonly
    ZHColumnVisibility: System.Windows.Visibility

    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def IsDirty(self) -> bool: ...
    def Activate(self) -> None: ...
    def GetTools(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools: ...

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class RelationItem:  # Class
    def __init__(self, relation: str, table: str) -> None: ...

    DisplayName: str  # readonly
    Relation: str  # readonly
    Table: str  # readonly

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
