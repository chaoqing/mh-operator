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

from . import IApplicationMenu2010Content
from .OpenBatch import BrowseDataStorageViewModel, OpenBatchViewModel, OpenBatchViewType

# Stubs for namespace: Agilent.MassHunter.Quantitative.Controls.NewBatch

class BrowseDataStorageView(
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

class BrowseDataStorageViewModel:  # Class
    def __init__(
        self, model: Agilent.MassHunter.Quantitative.Controls.NewBatch.NewBatchViewModel
    ) -> None: ...

    BatchFileProperty: System.Windows.DependencyProperty  # static # readonly

    AuditTrailOptionVisibility: System.Windows.Visibility  # readonly
    BatchFile: str
    NewBatchCommand: System.Windows.Input.ICommand  # readonly
    NewBatchViewModel: (
        Agilent.MassHunter.Quantitative.Controls.NewBatch.NewBatchViewModel
    )  # readonly

class NewBatchCommand(System.Windows.Input.ICommand):  # Class
    def __init__(
        self,
        browseDataStorageViewModel: Agilent.MassHunter.Quantitative.Controls.NewBatch.BrowseDataStorageViewModel,
    ) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Execute(self, parameter: Any) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class NewBatchView(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    IApplicationMenu2010Content,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(
        self, model: Agilent.MassHunter.Quantitative.Controls.NewBatch.NewBatchViewModel
    ) -> None: ...
    def InitializeComponent(self) -> None: ...
    def SetSize(self, width: float, height: float) -> None: ...

class NewBatchViewModel(OpenBatchViewModel):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

    AuditTrailButtonEnabledProperty: (
        System.Windows.DependencyProperty
    )  # static # readonly
    AuditTrailOptionVisibleProperty: (
        System.Windows.DependencyProperty
    )  # static # readonly
    AuditTrailProperty: System.Windows.DependencyProperty  # static # readonly
    NewBatchButtonLabelProperty: System.Windows.DependencyProperty  # static # readonly

    AuditTrail: bool
    AuditTrailButtonEnabled: bool
    AuditTrailOptionVisible: bool
    CurrentViewType: OpenBatchViewType
    NewBatchButtonLabel: str

    def ClearNewFileName(self) -> None: ...
    def DoBrowse(self, folder: str) -> None: ...
