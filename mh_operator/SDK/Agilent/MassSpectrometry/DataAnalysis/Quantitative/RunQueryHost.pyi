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

# Discovered Generic TypeVars:
T = TypeVar("T")
from .UIScriptIF import IUIState

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.RunQueryHost

class Host(System.MarshalByRefObject):  # Class
    def __init__(self, state: IUIState) -> None: ...

    CompilerType: str

    def Run(self, queryFile: str) -> None: ...
    def SetImports(self, imports: List[str]) -> None: ...
    def SetReferences(self, references: List[str]) -> None: ...
    def SetCompilerOption(self, key: str, value_: str) -> None: ...

class QueryResultsWindow(
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
    def __init__(self, state: IUIState) -> None: ...

    RunQuery: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.RunQueryHost.RunQueryBase
    )

class RunQueryBase(System.MarshalByRefObject):  # Class
    WindowTitle: str  # readonly

    def GetColumnFormat(self, column: str) -> str: ...
    def GetColumnLabels(self, column: str) -> str: ...
    def QueryMain(self) -> Any: ...

class _BindingList(
    System.ComponentModel.IBindingList,
    Generic[T],
    System.ComponentModel.IRaiseItemChangedEvents,
    Sequence[T],
    System.ComponentModel.BindingList[T],
    List[Any],
    List[T],
    Iterable[T],
    System.ComponentModel.ICancelAddNew,
    Sequence[Any],
    Iterable[Any],
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, list: List[T]) -> None: ...
