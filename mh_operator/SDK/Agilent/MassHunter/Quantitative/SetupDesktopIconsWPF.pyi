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

# Stubs for namespace: Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF

class App(
    System.Windows.Application,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...

    CANCELED: int = ...  # static # readonly
    ERROR: int = ...  # static # readonly
    SUCCESS: int = ...  # static # readonly

    @staticmethod
    def GetLogfilePath(logfileFolderName: str, filenamePrefix: str) -> str: ...
    def InitializeComponent(self) -> None: ...
    @staticmethod
    def SetupLogfileTraceListener() -> None: ...
    @staticmethod
    def Main() -> None: ...

class CommandLine:  # Class
    def __init__(self) -> None: ...

    Append: bool  # readonly
    Culture: str  # readonly
    Icons: List[str]  # readonly
    Install: bool  # readonly
    Silent: bool  # readonly
    Uninstall: bool  # readonly

    def Parse(self, args: List[str]) -> None: ...

class FlavorIconsViewModel:  # Class
    def __init__(self) -> None: ...
    def __getitem__(self, name: str) -> bool: ...
    def __setitem__(self, name: str, value_: bool) -> None: ...
    Vanilla: bool

    def Clear(self) -> None: ...
    def CreateShortcuts(
        self,
    ) -> List[Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.Shortcut]: ...

class IconItem:  # Class
    def __init__(self) -> None: ...

    DQ: bool
    EQ: bool
    Instrument: str
    STD: bool

    def Clear(self) -> None: ...
    def CreateShortcuts(
        self, inst: str, isGC: bool, wpf: bool
    ) -> List[Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.Shortcut]: ...

class MainViewModel:  # Class
    def __init__(self) -> None: ...

    ClassicIcons: (
        Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.QuantIconsViewModel
    )  # readonly
    FlavorIcons: (
        Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.FlavorIconsViewModel
    )  # readonly
    OpenLabIcons: (
        Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.OpenLabIconsViewModel
    )  # readonly

    def Initialize(self, icons: List[str], append: bool) -> None: ...
    def SetupShortcuts(self) -> None: ...

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

class OpenLabIconsViewModel(
    Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.QuantIconsViewModel
):  # Class
    def __init__(self) -> None: ...

    StartupRootFolderProperty: System.Windows.DependencyProperty  # static

    QuantMyWayIcon: bool
    StartupRootFolder: str

    def Clear(self) -> None: ...
    def CreateShortcuts(
        self, wpf: bool
    ) -> List[Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.Shortcut]: ...

class QuantIconsViewModel(System.Windows.DependencyObject):  # Class
    def __init__(self) -> None: ...

    GC: Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.IconItem  # readonly
    MS: Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.IconItem  # readonly
    QQQ: Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.IconItem  # readonly
    QTOF: Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.IconItem  # readonly
    TOF: Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.IconItem  # readonly
    UA: bool

    def Clear(self) -> None: ...
    def CreateShortcuts(
        self, wpf: bool
    ) -> List[Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.Shortcut]: ...

class QuantIonsControl(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IHaveResources,
    System.Windows.IInputElement,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Controls.Grid,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class Shortcut:  # Class
    def __init__(self) -> None: ...

    Application: str
    Desktop: str
    Flavor: str
    Instrument: str
    StartMenu: str
    UA: bool
    WPF: bool

class Shortcuts:  # Class
    def __init__(self) -> None: ...

    CreatedShortcuts: List[
        Agilent.MassHunter.Quantitative.SetupDesktopIconsWPF.Shortcut
    ]
