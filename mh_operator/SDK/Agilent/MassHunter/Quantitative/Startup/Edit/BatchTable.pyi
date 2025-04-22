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
    IControlPanelViewModel,
    ITask,
    TaskViewModelBase,
)

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.BatchTable

class BatchTableLayout:  # Class
    def __init__(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TableViewMode,
        singleCompounds: bool,
        displayName: str,
    ) -> None: ...

    DisplayName: str  # readonly
    SingleCompounds: bool  # readonly
    TableViewMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TableViewMode
    )  # readonly

class BatchTableView(
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

class BatchTableViewModel(TaskViewModelBase, IBatchTableViewModel, ITask):  # Class
    def __init__(self, rootModel: IControlPanelViewModel) -> None: ...

    AvailableColumnsProperty: System.Windows.DependencyProperty  # static
    IsEnabledProperty: System.Windows.DependencyProperty  # static
    SelectedDefaultBatchTableLayoutProperty: System.Windows.DependencyProperty  # static
    SelectedTableLayoutProperty: System.Windows.DependencyProperty  # static
    SelectedTableProperty: System.Windows.DependencyProperty  # static
    VisibleColumnsProperty: System.Windows.DependencyProperty  # static

    AddColumnCommand: System.Windows.Input.ICommand  # readonly
    AvailableColumns: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.BatchTable.ColumnItem
    ]
    BatchTableLayouts: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.BatchTable.BatchTableLayout
    ]  # readonly
    Content: System.Windows.UIElement  # readonly
    IsEnabled: bool  # readonly
    MoveDownCommand: System.Windows.Input.ICommand  # readonly
    MoveUpCommand: System.Windows.Input.ICommand  # readonly
    RemoveColumnCommand: System.Windows.Input.ICommand  # readonly
    SelectedDefaultBatchTableLayout: (
        Agilent.MassHunter.Quantitative.Startup.Edit.BatchTable.BatchTableLayout
    )
    SelectedTable: Agilent.MassHunter.Quantitative.Startup.Edit.BatchTable.TableItem
    SelectedTableLayout: (
        Agilent.MassHunter.Quantitative.Startup.Edit.BatchTable.BatchTableLayout
    )
    Tables: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.BatchTable.TableItem
    ]  # readonly
    Title: str  # readonly
    VisibleColumns: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.BatchTable.ColumnItem
    ]

    def MoveDown(self, parameters: Any) -> None: ...
    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def MoveUp(self, parameters: Any) -> None: ...
    def CanMoveDown(self, parameters: Any) -> bool: ...
    def IsDirty(self) -> bool: ...
    def Activate(self) -> None: ...
    def CanMoveUp(self, parameters: Any) -> bool: ...
    def GetTools(
        self,
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools: ...
    def UpdateColumns(self) -> None: ...

class ColumnIsAvailableConverter(System.Windows.Data.IValueConverter):  # Class
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

class ColumnItem(System.Windows.DependencyObject):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.BatchTable.BatchTableViewModel,
        relation: str,
        column: str,
    ) -> None: ...

    IsSelectedProperty: System.Windows.DependencyProperty  # static
    IsVisibleProperty: System.Windows.DependencyProperty  # static

    Column: str  # readonly
    DisplayName: str  # readonly
    IsSelected: bool
    IsVisible: bool
    Relation: str  # readonly

class TableItem:  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.BatchTable.BatchTableViewModel,
        relation: str,
    ) -> None: ...

    DisplayName: str  # readonly
    IsEnabled: bool  # readonly
    Relation: str  # readonly

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

class VisibleColumnsKey:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TableViewMode,
        single: bool,
        relation: str,
    ) -> None: ...

    Relation: str
    SingleMode: bool
    TableViewMode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TableViewMode

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...
