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

from . import NotifyPropertyChangedBase

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList

class IInsertListView(object):  # Interface
    CanOK: bool  # readonly

    def OnOK(self) -> None: ...

    CanOKChanged: System.EventHandler  # Event

class InsertListModelView(
    System.ComponentModel.INotifyPropertyChanged, NotifyPropertyChangedBase
):  # Class
    def __init__(
        self,
        window: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList.InsertListWindow,
    ) -> None: ...

    Application: Agilent.MassHunter.ReportBuilder.Application.IApplication  # readonly
    CanInsert: bool  # readonly
    CanOK: bool  # readonly
    CommandCancel: System.Windows.Input.ICommand  # readonly
    CommandOk: System.Windows.Input.ICommand  # readonly
    Container: (
        Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer
    )  # readonly
    CurrentChildViewModel: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList.IInsertListView
    )
    DataSourceDesigner: (
        Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceDesigner
    )  # readonly
    Handled: bool
    InsertIndex: int  # readonly
    IsCompounds: bool
    IsOther: bool
    IsSamples: bool

    def OnOK(self) -> None: ...
    def CloseWindow(self, handled: bool) -> None: ...

class InsertListWindow(
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
    def __init__(
        self,
        application: Agilent.MassHunter.ReportBuilder.Application.IApplication,
        designer: Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceDesigner,
    ) -> None: ...

    Handled: bool  # readonly

    def InitializeComponent(self) -> None: ...

class PageCompounds(
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

class PageCompoundsViewModel(
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList.IInsertListView,
    NotifyPropertyChangedBase,
):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList.InsertListModelView,
    ) -> None: ...

    BindingName: str
    CanOK: bool  # readonly
    FilterItems: System.Collections.Generic.List[
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList.PageCompoundsViewModel.FilterItem
    ]  # readonly
    InsertBatchInfoTable: bool
    OrderAscending: bool
    OrderItems: System.Collections.Generic.List[str]  # readonly
    SelectedFilterItem: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList.PageCompoundsViewModel.FilterItem
    )
    SelectedOrderItem: str

    def OnOK(self) -> None: ...

    CanOKChanged: System.EventHandler  # Event

    # Nested Types

    class FilterItem:  # Class
        def __init__(
            self,
            ct: Optional[
                Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundType
            ],
        ) -> None: ...

        CompoundType: Optional[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundType
        ]  # readonly
        DisplayText: str  # readonly

        def ToString(self) -> str: ...

class PageListType(
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

class PageSamples(
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

class PageSamplesViewModel(
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList.IInsertListView,
    NotifyPropertyChangedBase,
):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList.InsertListModelView,
    ) -> None: ...

    BindingName: str
    CanOK: bool  # readonly
    FilterItems: System.Collections.Generic.List[
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList.PageSamplesViewModel.FilterItem
    ]  # readonly
    InsertBatchInfoTable: bool
    InsertSampleInfoTable: bool
    OrderAscending: bool
    OrderItems: System.Collections.Generic.List[str]  # readonly
    SelectedFilterItem: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertList.PageSamplesViewModel.FilterItem
    )
    SelectedOrderItem: str

    def OnOK(self) -> None: ...

    CanOKChanged: System.EventHandler  # Event

    # Nested Types

    class FilterItem:  # Class
        def __init__(
            self,
            sampleType: Optional[
                Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleType
            ],
        ) -> None: ...

        SampleType: Optional[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleType
        ]  # readonly

        def ToString(self) -> str: ...
