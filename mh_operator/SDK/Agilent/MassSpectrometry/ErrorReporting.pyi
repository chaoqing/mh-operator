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

# Stubs for namespace: Agilent.MassSpectrometry.ErrorReporting

class ErrorReportContentsForm(
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
    def __init__(self, contents: str) -> None: ...

class ErrorReporter:  # Class
    @overload
    def __init__(
        self,
        appId: int,
        emailAddress: str,
        errorSource: str,
        exception: System.Exception,
    ) -> None: ...
    @overload
    def __init__(
        self, appId: int, emailAddress: str, errorSource: str, errorReport: str
    ) -> None: ...
    @overload
    def __init__(
        self,
        appId: int,
        emailAddress: str,
        errorSource: str,
        errorReport: str,
        contactInfo: str,
        exception: System.Exception,
    ) -> None: ...

    AppId: int  # readonly
    ContactInformation: str
    DestinationUrl: str  # readonly
    EmailAddress: str  # readonly
    EmailSubject: str
    ErrorReport: str
    ErrorSource: str
    ExceptionReport: str
    FileAttachments: System.Collections.Specialized.StringCollection  # readonly

    @overload
    def TestConnectionToDestinationUrl(self) -> bool: ...
    @overload
    def TestConnectionToDestinationUrl(self, millisecsTimeout: int) -> bool: ...
    @staticmethod
    def GetProcessModuleInformation() -> str: ...
    @staticmethod
    def GetProcessThreadInformation() -> str: ...
    def GenerateFullErrorReport(self) -> str: ...
    def AddAttachment(self, path: str) -> None: ...
    @staticmethod
    def GetPlatformInformation() -> str: ...
    @staticmethod
    def GetStackTraceReport(exception: System.Exception) -> str: ...
    @staticmethod
    def GetExceptionInformation(exception: System.Exception) -> str: ...
    @staticmethod
    def CreateExceptionReport(exception: System.Exception) -> str: ...
    def SendReport(self) -> None: ...
    def ShowErrorWindow(self) -> None: ...

class ErrorReporterForm(
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
    def __init__(
        self, errorReport: Agilent.MassSpectrometry.ErrorReporting.ErrorReporter
    ) -> None: ...

    BodyContentsLabel: System.Windows.Forms.Label  # readonly
    BodyTitleLabel: System.Windows.Forms.Label  # readonly
    ErrorReporter: Agilent.MassSpectrometry.ErrorReporting.ErrorReporter  # readonly
    HeaderLabel: System.Windows.Forms.Label  # readonly
    LogoPictureBox: System.Windows.Forms.PictureBox  # readonly
