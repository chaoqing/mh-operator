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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.ViewModel

class FileListFilter:  # Class
    def __init__(self, text: str, extensions: str) -> None: ...

    Extensions: List[str]  # readonly
    Text: str  # readonly

    def Match(self, name: str) -> bool: ...
    def ToString(self) -> str: ...

class FileListViewModel(System.ComponentModel.INotifyPropertyChanged):  # Class
    def __init__(self) -> None: ...

    CommandCheckout: System.Windows.Input.ICommand  # readonly
    CommandUndoCheckout: System.Windows.Input.ICommand  # readonly
    Filters: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.ViewModel.FileListFilter
    )
    Items: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.ViewModel.ListItemViewModel
    ]  # readonly
    OpenCommandText: str  # readonly
    OpenCommandVisibility: System.Windows.Visibility  # readonly
    OpenRevisionVisibility: System.Windows.Visibility  # readonly
    OpenSeparatorVisibility: System.Windows.Visibility  # readonly
    Window: System.Windows.Window

    def UpdateItems(self, path: str) -> None: ...
    def Sort(self, name: str) -> None: ...

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class FolderTreeViewModel:  # Class
    def __init__(self) -> None: ...

    Folders: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.ViewModel.TreeItemViewModel
    ]  # readonly

class ListItemViewModel(System.ComponentModel.INotifyPropertyChanged):  # Class
    def __init__(self) -> None: ...

    CheckedOut: Optional[bool]
    CheckedOutByCurrentUser: bool
    CheckoutImage: System.Windows.Media.ImageSource
    CheckoutReason: str
    CheckoutTime: Optional[System.DateTime]
    CheckoutUser: str
    CreateDate: str
    Image: System.Windows.Media.ImageSource
    IsFolder: bool
    ModifiedDate: str
    Name: str
    RevisionNumber: Optional[int]
    UploadDate: Optional[System.DateTime]
    UploadReason: str
    UploadUser: str
    _CheckoutTime: str  # readonly
    _UploadDate: str  # readonly

    def Update(self) -> Any: ...

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class TreeItemViewModel(System.ComponentModel.INotifyPropertyChanged):  # Class
    def __init__(self) -> None: ...

    Children: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.ViewModel.TreeItemViewModel
    ]  # readonly
    FolderLevel: int
    Image: System.Windows.Media.ImageSource
    IsExpanded: bool
    IsLastLevelFolder: bool
    IsSelected: bool
    Name: str
    Parent: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.ViewModel.TreeItemViewModel
    )  # readonly
    PathName: str

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event
