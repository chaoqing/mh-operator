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

from .Commands import AppContext

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Remoting

class Client(System.MarshalByRefObject, System.IDisposable):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...
    def CloseApplication(self, force: bool) -> None: ...
    def OpenProgressDialog(
        self, title: str, message: str, dowork: System.ComponentModel.DoWorkEventHandler
    ) -> None: ...
    def PrepareNewLibrary(self, library: str) -> bool: ...
    def DoWork(
        self,
        p: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Remoting.DoWorkParameters,
    ) -> None: ...
    def SetLibraryProperty(self, properties: Dict[str, Any]) -> None: ...
    def SynthesizeSpectra(
        self, compoundId: int, spectrumProperties: Dict[str, Any], species: str
    ) -> None: ...
    def CloseProgressDialog(self) -> None: ...
    def PrepareImporting(self, isNewLibrary: bool) -> bool: ...
    def Connect(self) -> None: ...
    def Dispose(self) -> None: ...
    def ReportProgress(self, percent: int, message: str) -> None: ...
    def NewCompound(
        self, compoundProperties: Dict[str, Any], spectrumProperties: Dict[str, Any]
    ) -> int: ...
    def SaveLibrary(self) -> None: ...

class DoWorkParameters:  # Class
    def __init__(self, argument: Any) -> None: ...

    Argument: Any
    Cancel: bool
    Result: Any

class ImportDialog(
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
    def __init__(self, context: AppContext) -> None: ...

    CurrentLibrary: bool
    ExistingLibrary: bool
    NewLibrary: bool

class Server(System.MarshalByRefObject, System.IDisposable):  # Class
    def CloseApplication(self, force: bool) -> None: ...
    def Ready(self) -> None: ...
    def OpenProgressDialog(self, title: str, message: str) -> None: ...
    def PrepareNewLibrary(self, path: str) -> bool: ...
    def SetCulture(self, ci: System.Globalization.CultureInfo) -> None: ...
    def SetLibraryProperty(self, properties: Dict[str, Any]) -> None: ...
    def SynthesizeSpectra(
        self, compoundId: int, spectrumProperties: Dict[str, Any], species: str
    ) -> None: ...
    def CloseProgressDialog(self) -> None: ...
    def PrepareImporting(self, isNewLibrary: bool) -> bool: ...
    def Dispose(self) -> None: ...
    def ReportProgress(self, percent: int, message: str) -> None: ...
    def NewCompound(
        self, compoundProperties: Dict[str, Any], spectrumProperties: Dict[str, Any]
    ) -> int: ...
    def SaveLibrary(self) -> None: ...
