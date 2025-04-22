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

from .UIUtils2 import ConfigurationElementSectionBase

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.RTCalibration

class AppConfig:  # Class
    ApplicationSettings: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.RTCalibration.ApplicationSettings
    )  # readonly
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.RTCalibration.AppConfig
    )  # static # readonly
    UserSettings: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.RTCalibration.UserSettings
    )  # readonly

    def Save(self) -> None: ...

class ApplicationSettings(ConfigurationElementSectionBase):  # Class
    def __init__(self) -> None: ...

    DumpLogOnNormalExit: bool  # readonly
    ErrorReportingEmailAddress: str  # readonly
    ErrorReportingEnabled: bool  # readonly

class CommandLine:  # Class
    def __init__(self) -> None: ...

    Culture: str

class Context(System.IDisposable):  # Class
    def __init__(
        self, batchFolder: str, batchFile: str, library: str, destination: str
    ) -> None: ...
    def Dispose(self) -> None: ...
    def Generate(self) -> None: ...

class MainForm(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

class UserSettings(ConfigurationElementSectionBase):  # Class
    def __init__(self) -> None: ...

    LastBatchFolder: str
