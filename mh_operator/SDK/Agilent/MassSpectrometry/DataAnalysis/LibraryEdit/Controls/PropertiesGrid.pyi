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
from . import TitledPanel

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Controls.PropertiesGrid

class PropertiesGridControl(
    System.Windows.Forms.ComponentModel.Com2Interop.IComPropertyBrowser,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.PropertyGrid,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.IComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPropertyNotifySink,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
):  # Class
    def __init__(self) -> None: ...
    def Refresh(self) -> None: ...

class PropertiesGridPane(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    TitledPanel,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
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

    PropertiesGridControl: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Controls.PropertiesGrid.PropertiesGridControl
    )  # readonly

class QuickSort(Generic[T]):  # Class
    def __init__(
        self,
        values: System.ComponentModel.BindingList[T],
        comparison: System.Comparison[T],
    ) -> None: ...
    def Sort(self) -> None: ...

class SpectrumEditor(
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

class SpectrumObject:  # Class
    def __init__(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.UIContext,
        key: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Utils.SpectrumKey,
        control: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Controls.PropertiesGrid.PropertiesGridControl,
    ) -> None: ...

class SpectrumObjectConverter(System.ComponentModel.TypeConverter):  # Class
    def __init__(self) -> None: ...
    def GetProperties(
        self,
        context: System.ComponentModel.ITypeDescriptorContext,
        value_: Any,
        attributes: List[System.Attribute],
    ) -> System.ComponentModel.PropertyDescriptorCollection: ...
    def GetPropertiesSupported(
        self, context: System.ComponentModel.ITypeDescriptorContext
    ) -> bool: ...
