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

# Stubs for namespace: Agilent.MassHunter.Quantitative.ErrorWindow

class App(
    System.Windows.Application,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def Main() -> None: ...

class CommandLine:  # Class
    def __init__(self) -> None: ...

    ApplicationName: str
    DetailsFile: str
    Logfile: str

class ErrorWindowModel(System.Windows.DependencyObject):  # Class
    def __init__(self) -> None: ...

    ApplicationNameProperty: System.Windows.DependencyProperty  # static
    DetailsFileProperty: System.Windows.DependencyProperty  # static
    DetailsProperty: System.Windows.DependencyProperty  # static
    DetailsVisibilityProperty: System.Windows.DependencyProperty  # static
    LogFileProperty: System.Windows.DependencyProperty  # static
    MessageProperty: System.Windows.DependencyProperty  # static
    ShowDetailsProperty: System.Windows.DependencyProperty  # static

    ApplicationName: str
    CommandCopyDetails: System.Windows.Input.ICommand  # readonly
    CommandShowLogfile: System.Windows.Input.ICommand  # readonly
    Details: str
    DetailsFile: str
    DetailsVisibility: System.Windows.Visibility
    LogFile: str
    Message: str
    ShowDetails: bool

    @staticmethod
    def ShowErrorWindow(
        appName: str,
        assembly: System.Reflection.Assembly,
        exception: System.Exception,
        logFile: str,
    ) -> None: ...

class MainWindow(
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
