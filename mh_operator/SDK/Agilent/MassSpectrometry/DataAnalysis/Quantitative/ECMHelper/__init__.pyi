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

from . import Configuration, Properties, ViewModel
from .ViewModel import FolderTreeViewModel

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper

class ControlBox:  # Class
    HasHelpButtonProperty: System.Windows.DependencyProperty  # static # readonly
    HasMaximizeButtonProperty: System.Windows.DependencyProperty  # static # readonly
    HasMinimizeButtonProperty: System.Windows.DependencyProperty  # static # readonly

    @staticmethod
    def SetHasMaximizeButton(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def SetHasHelpButton(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def SetHasMinimizeButton(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def GetHasHelpButton(element: System.Windows.Window) -> bool: ...
    @staticmethod
    def GetHasMaximizeButton(element: System.Windows.Window) -> bool: ...
    @staticmethod
    def GetHasMinimizeButton(element: System.Windows.Window) -> bool: ...

class DomainDialog(
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

    Domain: str  # readonly

    def InitializeComponent(self) -> None: ...

class FileDialog(
    System.Windows.Window,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IWindowService,
    System.Windows.Markup.IStyleConnector,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Animation.IAnimatable,
    System.ComponentModel.ISupportInitialize,
    System.Windows.IInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.IFrameworkInputElement,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...

    AllowFileRevisions: bool
    DefaultExtension: str
    DefaultFileName: str
    FileMustExists: bool
    FileMustNotExist: bool
    Filters: str
    InitialFolder: str
    Multiselect: bool
    OkButtonText: str
    OpenMode: bool  # readonly
    OverwritePrompt: bool
    PathName: str
    PathNames: List[str]
    Readonly: bool  # readonly
    RevisionNumber: str  # readonly
    RootFolder: str

    def InitializeComponent(self) -> None: ...

class FileRevisionDialog(
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

    AllowOpenAsCheckedout: bool
    RevisionNumber: int  # readonly

    def InitializeComponent(self) -> None: ...

class FolderTree(
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

    SelectedPath: str  # readonly
    ViewModel: FolderTreeViewModel  # readonly

    def Initialize(self) -> Any: ...
    def InitializeComponent(self) -> None: ...
    def SetSelectedFolder(self, pathName: str) -> None: ...

    SelectedItemChanged: System.Windows.RoutedPropertyChangedEventHandler  # Event

class LoginDialog(
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

    CanLogin: bool  # readonly
    Domain: str
    LogonXml: str  # readonly
    Message: str
    Password: System.Security.SecureString  # readonly
    Server: str
    User: str
    ValidationMode: bool

    def InitializeComponent(self) -> None: ...
    @staticmethod
    def Login() -> Any: ...

    Cancel: System.ComponentModel.CancelEventHandler  # Event
    Logon: System.ComponentModel.CancelEventHandler  # Event

class OpenFileDialog(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IWindowService,
    System.Windows.Markup.IStyleConnector,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.FileDialog,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Animation.IAnimatable,
    System.ComponentModel.ISupportInitialize,
    System.Windows.IInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.IFrameworkInputElement,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...

    OpenMode: bool  # readonly

class RelayCommand(System.Windows.Input.ICommand):  # Class
    @overload
    def __init__(self, execute: System.Action) -> None: ...
    @overload
    def __init__(
        self, execute: System.Action, canExecute: System.Predicate
    ) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Execute(self, parameter: Any) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class SaveFileDialog(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IWindowService,
    System.Windows.Markup.IStyleConnector,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.FileDialog,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Animation.IAnimatable,
    System.ComponentModel.ISupportInitialize,
    System.Windows.IInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.IFrameworkInputElement,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...

    OpenMode: bool  # readonly

class Utils:  # Class
    IsECM5OrLater: bool  # static # readonly

    @staticmethod
    def InitComplianceEnvironment() -> None: ...
