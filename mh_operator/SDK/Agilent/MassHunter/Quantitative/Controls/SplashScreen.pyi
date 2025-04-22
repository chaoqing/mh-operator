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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Controls.SplashScreen

class RUOWindow(
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

class SplashScreenClassicWindow(
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
    def InitializeComponent(self) -> None: ...

class SplashScreenModel(System.Windows.DependencyObject):  # Class
    def __init__(self) -> None: ...

    ApplicationProperty: System.Windows.DependencyProperty  # static
    BuildTextProperty: System.Windows.DependencyProperty  # static
    CloseButtonVisibleProperty: System.Windows.DependencyProperty  # static
    CopyrightProperty: System.Windows.DependencyProperty  # static
    HasPCDLWarningProperty: System.Windows.DependencyProperty  # static
    IconProperty: System.Windows.DependencyProperty  # static
    QuantAppName: str = ...  # static # readonly
    RUOLinkVisibilityProperty: System.Windows.DependencyProperty  # static
    ShowInTaskbarProperty: System.Windows.DependencyProperty  # static
    SubAppProperty: System.Windows.DependencyProperty  # static
    TrialProperty: System.Windows.DependencyProperty  # static
    VersionTextProperty: System.Windows.DependencyProperty  # static

    Application: str
    Build: str
    BuildText: str
    CloseButtonVisible: bool
    Copyright: str
    Handle: System.IntPtr  # readonly
    HasPCDLWarning: bool
    Icon: System.Windows.Media.ImageSource
    Minimum: System.TimeSpan
    RUOLinkVisibility: System.Windows.Visibility
    ServicePack: str
    ShowInTaskbar: bool
    SubApp: str
    Trial: str
    Version: str
    VersionText: str

    @overload
    def SetOwner(self, owner: System.Windows.Window) -> None: ...
    @overload
    def SetOwner(self, ptr: System.IntPtr) -> None: ...
    def InitCompliance(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...
    def ShowMessageBox(
        self,
        message: str,
        title: str,
        button: System.Windows.MessageBoxButton,
        image: System.Windows.MessageBoxImage,
    ) -> System.Windows.MessageBoxResult: ...
    @overload
    def Close(self, forceClose: bool) -> None: ...
    @overload
    def Close(self) -> None: ...
    def ShowDialog(self, parent: System.IntPtr) -> None: ...
    def Activate(self) -> None: ...
    def Show(self) -> None: ...
    def InitVersions(self) -> None: ...

class SplashScreenWindow(
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
