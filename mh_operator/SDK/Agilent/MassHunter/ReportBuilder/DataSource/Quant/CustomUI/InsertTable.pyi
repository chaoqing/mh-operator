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

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertTable

class IInsertTableView(object):  # Interface
    CanOK: bool  # readonly

    def OnOK(self) -> None: ...

    CanOKChanged: System.EventHandler  # Event

class InsertTableWindow(
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

    Application: Agilent.MassHunter.ReportBuilder.Application.IApplication  # readonly
    DataSourceDesigner: (
        Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceDesigner
    )  # readonly
    Handled: bool  # readonly

    def InitializeComponent(self) -> None: ...

class InsertTableWindowModel(
    System.ComponentModel.INotifyPropertyChanged, NotifyPropertyChangedBase
):  # Class
    def __init__(
        self,
        window: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertTable.InsertTableWindow,
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
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertTable.IInsertTableView
    )
    Handled: bool
    InsertIndex: int  # readonly
    IsCompounds: bool

    def OnOK(self) -> None: ...
    def CloseWindow(self, handled: bool) -> None: ...

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
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertTable.IInsertTableView,
    NotifyPropertyChangedBase,
):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.InsertTable.InsertTableWindowModel,
    ) -> None: ...

    BindingName: str
    CanOK: bool  # readonly
    IncludeISTDPeaks: bool
    IncludeISTDs: bool
    IncludePeaks: bool

    def OnOK(self) -> None: ...

    CanOKChanged: System.EventHandler  # Event
