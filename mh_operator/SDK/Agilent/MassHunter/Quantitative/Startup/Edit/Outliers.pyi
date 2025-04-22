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
    IControlPanelViewModel,
    IOutliersViewModel,
    ITask,
    TaskViewModelBase,
)

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.Outliers

class GroupHeaderConverter(System.Windows.Data.IValueConverter):  # Class
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

class OutlierItem(System.Windows.DependencyObject):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Startup.Edit.Outliers.OutliersViewModel,
        outlierColumns: Agilent.MassSpectrometry.DataAnalysis.Quantitative.OutlierColumns,
        category: Agilent.MassSpectrometry.DataAnalysis.Quantitative.OutlierCategories,
    ) -> None: ...

    VisibleProperty: System.Windows.DependencyProperty  # static

    DisplayName: str  # readonly
    OutlierCategory: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.OutlierCategories
    )  # readonly
    OutlierColumn: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.OutlierColumns
    )  # readonly
    Visible: bool

class OutliersView(
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

class OutliersViewModel(TaskViewModelBase, IOutliersViewModel, ITask):  # Class
    def __init__(self, rootModel: IControlPanelViewModel) -> None: ...

    OutlierItemsProperty: System.Windows.DependencyProperty  # static

    CommandCheckAll: System.Windows.Input.ICommand  # readonly
    CommandUncheckAll: System.Windows.Input.ICommand  # readonly
    Content: System.Windows.UIElement  # readonly
    Initializing: bool  # readonly
    IsEnabled: bool  # readonly
    OutlierItems: System.Windows.Data.ListCollectionView
    Title: str  # readonly
    View: Agilent.MassHunter.Quantitative.Startup.Edit.Outliers.OutliersView  # readonly

    def ResetToDefault(self) -> None: ...
    def Reload(self) -> None: ...
    def IsDirty(self) -> bool: ...
    def SetOutliers(
        self, outliers: Agilent.MassHunter.Quantitative.Startup.Common.Outliers
    ) -> None: ...
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
