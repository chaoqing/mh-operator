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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Extract

class App(
    System.Windows.Application,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    @staticmethod
    def Main() -> None: ...

class CommandLine:  # Class
    def __init__(self) -> None: ...

    Culture: str
    DeploymentFile: str
    Destination: str
    Help: bool
    Silent: bool
    Uninstall: bool

class MainViewModel(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self) -> None: ...

    CommandBrowseDeploymentFilePath: System.Windows.Input.ICommand  # readonly
    CommandBrowseDestinationPath: System.Windows.Input.ICommand  # readonly
    CommandExtract: System.Windows.Input.ICommand  # readonly
    DeploymentFilePath: str
    DestinationPath: str
    Window: Agilent.MassHunter.Quantitative.Startup.Extract.MainWindow  # readonly

    def DoExtract(self) -> None: ...
    def Uninstall(self) -> None: ...

class MainWindow(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IWindowService,
    Infragistics.Windows.Ribbon.IRibbonWindow,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Animation.IAnimatable,
    System.ComponentModel.ISupportInitialize,
    Infragistics.Windows.Ribbon.XamRibbonWindow,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...
