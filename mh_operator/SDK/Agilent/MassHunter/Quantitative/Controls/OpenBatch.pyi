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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Controls.OpenBatch

class BrowseDataStorageItem:  # Class
    def __init__(self) -> None: ...

    DateModified: Optional[System.DateTime]
    DateUploaded: Optional[System.DateTime]
    DisplayName: str
    Image: System.Windows.Media.ImageSource
    IsFolder: bool
    Name: str
    PathName: str

class BrowseDataStorageView(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IStyleConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class BrowseDataStorageViewModel(System.Windows.DependencyObject):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewModel,
    ) -> None: ...

    CurrentFolderProperty: System.Windows.DependencyProperty  # static # readonly
    ItemRowContextMenuProperty: System.Windows.DependencyProperty  # static
    ItemsProperty: System.Windows.DependencyProperty  # static # readonly

    CommandBrowse: System.Windows.Input.ICommand  # readonly
    CommandGoUp: System.Windows.Input.ICommand  # readonly
    CurrentFolder: (
        Agilent.MassHunter.Quantitative.Controls.OpenBatch.BrowseDataStorageItem
    )  # readonly
    IsDateModifiedVisibility: System.Windows.Visibility  # readonly
    IsDateUploadedVisibility: System.Windows.Visibility  # readonly
    ItemRowContextMenu: System.Windows.Controls.ContextMenu
    Items: List[
        Agilent.MassHunter.Quantitative.Controls.OpenBatch.BrowseDataStorageItem
    ]

    def SetCurrentFolder(self, folder: str) -> None: ...

class OpenBatchView(
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
        self,
        model: Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewModel,
    ) -> None: ...

    RecentBatchesLabel: str

    def InitializeComponent(self) -> None: ...
    def SetSize(self, width: float, height: float) -> None: ...

class OpenBatchViewModel(System.Windows.DependencyObject):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

    CurrentViewModelProperty: System.Windows.DependencyProperty  # static # readonly
    InitialFolderProperty: System.Windows.DependencyProperty  # static # readonly
    RecentBatchesLabelProperty: System.Windows.DependencyProperty  # static # readonly
    RecentBatchesProperty: System.Windows.DependencyProperty  # static # readonly
    TitleProperty: System.Windows.DependencyProperty  # static # readonly

    BatchFile: str
    BatchFolder: str
    BrowseDataStorageViewModel: (
        Agilent.MassHunter.Quantitative.Controls.OpenBatch.BrowseDataStorageViewModel
    )  # readonly
    CommandBrowse: System.Windows.Input.ICommand  # readonly
    Compliance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance
    )  # readonly
    CurrentViewModel: Any
    CurrentViewType: (
        Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewType
    )
    InitialFolder: str
    IsReadOnly: bool
    RecentBatches: List[str]
    RecentBatchesLabel: str
    RecentViewModel: (
        Agilent.MassHunter.Quantitative.Controls.OpenBatch.RecentViewModel
    )  # readonly
    RevisionNumber: str
    Title: str
    ViewModels: List[
        Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewModelItem
    ]  # readonly

    def GetView(self) -> System.Windows.Controls.Control: ...
    def SetCurrentFolder(self, folder: str) -> None: ...
    def DoBrowse(self, folder: str) -> None: ...
    def FireBatchFileSelected(self) -> None: ...
    def GetDataFiles(
        self, folder: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IFileInfo
    ]: ...
    def CreateRecentViewModel(
        self,
    ) -> Agilent.MassHunter.Quantitative.Controls.OpenBatch.RecentViewModel: ...

    BatchFileSelected: System.EventHandler  # Event

class OpenBatchViewModelItem(System.Windows.DependencyObject):  # Class
    def __init__(self) -> None: ...

    Image: System.Windows.Media.ImageSource
    Label: str
    ViewType: Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewType

class OpenBatchViewType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Computer: Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewType = (
        ...
    )  # static # readonly
    RecentBatches: (
        Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewType
    ) = ...  # static # readonly

class RecentBatchItem:  # Class
    def __init__(self) -> None: ...

    BatchFile: str
    BatchFolder: str
    DateModified: Optional[System.DateTime]
    Pathname: str

class RecentView(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IStyleConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class RecentViewModel(System.Windows.DependencyObject):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewModel,
    ) -> None: ...

    ItemRowContextMenuProperty: System.Windows.DependencyProperty  # static
    RecentBatchesProperty: System.Windows.DependencyProperty  # static

    ItemRowContextMenu: System.Windows.Controls.ContextMenu
    Model: (
        Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewModel
    )  # readonly
    RecentBatches: List[
        Agilent.MassHunter.Quantitative.Controls.OpenBatch.RecentBatchItem
    ]  # readonly
    RecentBatchesLabel: str  # readonly
    SelectedItem: Agilent.MassHunter.Quantitative.Controls.OpenBatch.RecentBatchItem

    def ItemClicked(
        self, item: Agilent.MassHunter.Quantitative.Controls.OpenBatch.RecentBatchItem
    ) -> None: ...
