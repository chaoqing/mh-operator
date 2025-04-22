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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Controls.FileDialog

class FileDialog(
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
    def __init__(self) -> None: ...

    FileListView: (
        Agilent.MassHunter.Quantitative.Controls.FileDialog.FileListView
    )  # readonly
    FolderTreeView: (
        Agilent.MassHunter.Quantitative.Controls.FileDialog.FolderTreeView
    )  # readonly

    def InitializeComponent(self) -> None: ...

class FileDialogMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    New: Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialogMode = (
        ...
    )  # static # readonly
    Open: Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialogMode = (
        ...
    )  # static # readonly
    Save: Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialogMode = (
        ...
    )  # static # readonly

class FileDialogModel(System.ComponentModel.INotifyPropertyChanged):  # Class
    def __init__(
        self, mode: Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialogMode
    ) -> None: ...

    AllowCheckout: bool
    AllowMultiSelection: bool
    AllowRevisions: bool
    CheckFileExists: bool
    CheckOverwrite: bool
    CheckPathExists: bool
    CommandCancel: System.Windows.Input.ICommand  # readonly
    CommandCheckout: System.Windows.Input.ICommand  # readonly
    CommandGoUp: System.Windows.Input.ICommand  # readonly
    CommandOK: System.Windows.Input.ICommand  # readonly
    CommandOpenAsCheckedOut: System.Windows.Input.ICommand  # readonly
    CommandOpenOlder: System.Windows.Input.ICommand  # readonly
    CommandUndoCheckout: System.Windows.Input.ICommand  # readonly
    CurrentFolder: str
    DefaultExtension: str
    DialogResult: Optional[bool]
    FileListViewSelectionMode: System.Windows.Controls.SelectionMode  # readonly
    FileName: str
    Filters: List[Agilent.MassHunter.Quantitative.Controls.FileDialog.Filter]
    Folders: List[
        Agilent.MassHunter.Quantitative.Controls.FileDialog.FolderTreeViewItemModel
    ]  # readonly
    ListViewItems: List[
        Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel
    ]  # readonly
    Mode: Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialogMode  # readonly
    OpenAsCheckedout: bool
    OpenCommandText: str
    OverwritePrompt: bool
    PathName: str
    PathNames: List[str]
    RevisionNumber: str  # readonly
    SelectedFilter: Agilent.MassHunter.Quantitative.Controls.FileDialog.Filter
    Title: str

    def PerformOK(self) -> bool: ...
    def ListViewItemDoubleClick(
        self,
        item: Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel,
        selectedItems: List[
            Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel
        ],
    ) -> None: ...
    def SetSelectedListViewItems(
        self,
        items: List[
            Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel
        ],
    ) -> None: ...

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class FileListView(
    System.Windows.Markup.IHaveResources,
    System.Windows.IFrameworkInputElement,
    System.Windows.Controls.Primitives.IContainItemStorage,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Controls.ListView,
    System.Windows.IInputElement,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
    MS.Internal.Controls.IGeneratorHost,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IStyleConnector,
):  # Class
    def __init__(self) -> None: ...
    def ClearSelection(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class FileRevisionsDialog(
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
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class FileRevisionsDialogModel:  # Class
    def __init__(self) -> None: ...

    CommandOK: System.Windows.Input.ICommand  # readonly
    CommandOpenAsCheckedOut: System.Windows.Input.ICommand  # readonly
    Items: List[Any]  # readonly

class Filter:  # Class
    def __init__(self) -> None: ...

    Extensions: List[
        Agilent.MassHunter.Quantitative.Controls.FileDialog.FilterExtension
    ]
    Title: str

    def Matches(
        self,
        item: Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel,
    ) -> bool: ...

class FilterExtension:  # Class
    def __init__(self) -> None: ...

    Extensions: List[str]
    IsFolder: bool

    def Matches(
        self,
        item: Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel,
    ) -> bool: ...

class FolderTreeView(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Controls.TreeView,
    System.Windows.Markup.IQueryAmbient,
    MS.Internal.Controls.IGeneratorHost,
    System.Windows.Media.Animation.IAnimatable,
    System.ComponentModel.ISupportInitialize,
    System.Windows.IInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.IFrameworkInputElement,
    System.Windows.Controls.Primitives.IContainItemStorage,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class FolderTreeViewItemModel(System.ComponentModel.INotifyPropertyChanged):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialogModel,
        parent: Agilent.MassHunter.Quantitative.Controls.FileDialog.FolderTreeViewItemModel,
    ) -> None: ...

    Children: List[
        Agilent.MassHunter.Quantitative.Controls.FileDialog.FolderTreeViewItemModel
    ]  # readonly
    DisplayName: str
    FileDialogModel: (
        Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialogModel
    )  # readonly
    Image: System.Windows.Media.ImageSource
    IsExpanded: bool
    IsSelected: bool
    Name: str
    Parent: (
        Agilent.MassHunter.Quantitative.Controls.FileDialog.FolderTreeViewItemModel
    )  # readonly
    PathName: str

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class ListViewItemModel(System.ComponentModel.INotifyPropertyChanged):  # Class
    def __init__(self) -> None: ...

    CheckoutImage: System.Windows.Media.ImageSource
    CheckoutImageMinWidth: int  # readonly
    CheckoutImageWidth: int  # readonly
    Image: System.Windows.Media.ImageSource
    IsFolder: bool
    IsSelected: bool
    Name: str
    PathName: str
    Revision: str

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class LocalFileDialogModel(
    Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialogModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        mode: Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialogMode,
        fileDialog: Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialog,
    ) -> None: ...

    CommandCheckout: System.Windows.Input.ICommand  # readonly
    CommandGoUp: System.Windows.Input.ICommand  # readonly
    CommandOpenAsCheckedOut: System.Windows.Input.ICommand  # readonly
    CommandOpenOlder: System.Windows.Input.ICommand  # readonly
    CommandUndoCheckout: System.Windows.Input.ICommand  # readonly
    CurrentFolder: str
    FileName: str
    Filters: List[Agilent.MassHunter.Quantitative.Controls.FileDialog.Filter]
    Folders: List[
        Agilent.MassHunter.Quantitative.Controls.FileDialog.FolderTreeViewItemModel
    ]  # readonly
    ListViewItems: List[
        Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel
    ]  # readonly
    RootFolder: str
    SelectedFilter: Agilent.MassHunter.Quantitative.Controls.FileDialog.Filter

    @staticmethod
    def GetImage(path: str) -> System.Windows.Media.Imaging.BitmapSource: ...
    def PerformOK(self) -> bool: ...
    def SetSelectedListViewItems(
        self,
        items: List[
            Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel
        ],
    ) -> None: ...
    def ListViewItemDoubleClick(
        self,
        item: Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel,
        selectedItems: List[
            Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel
        ],
    ) -> None: ...
    def SelectFolderItem(self, path: str) -> None: ...
    def MatchFolder(self, pathName: str) -> bool: ...

class LocalFolderTreeViewItemModel(
    Agilent.MassHunter.Quantitative.Controls.FileDialog.FolderTreeViewItemModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Controls.FileDialog.FileDialogModel,
        parent: Agilent.MassHunter.Quantitative.Controls.FileDialog.LocalFolderTreeViewItemModel,
    ) -> None: ...

    Children: List[
        Agilent.MassHunter.Quantitative.Controls.FileDialog.FolderTreeViewItemModel
    ]  # readonly
    Image: System.Windows.Media.ImageSource

class LocalListViewItemModel(
    Agilent.MassHunter.Quantitative.Controls.FileDialog.ListViewItemModel,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self) -> None: ...

    Image: System.Windows.Media.ImageSource
