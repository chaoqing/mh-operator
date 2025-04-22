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

from .Compliance import ICompliance

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceConfiguration

class CheckListControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
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
    System.Windows.Forms.UserControl,
):  # Class
    def __init__(self) -> None: ...

    ContextMenuStrip: System.Windows.Forms.ContextMenuStrip
    StateImageList: System.Windows.Forms.ImageList
    TitleText: str

    def ClearItems(self) -> None: ...
    def SelectItem(self, key: str) -> None: ...
    def SetItemState(
        self, key: str, state: System.Windows.Forms.CheckState
    ) -> None: ...
    def GetSelectedItems(self) -> List[str]: ...
    def GetItemKey(self, index: int) -> str: ...
    def EndUpdate(self) -> None: ...
    def SetItem(
        self, key: str, text: str, state: System.Windows.Forms.CheckState
    ) -> None: ...
    def BeginUpdate(self) -> None: ...

    ItemCheck: System.Windows.Forms.ItemCheckEventHandler  # Event

class CommandLine:  # Class
    def __init__(self) -> None: ...

    Culture: str

class CommandSettingsControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceConfiguration.IMapView,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.IWin32Window,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
):  # Class
    def __init__(self) -> None: ...

class CommandTreeControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
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
    System.Windows.Forms.UserControl,
):  # Class
    def __init__(self) -> None: ...

    TreeNodeAfterSelect: System.EventHandler  # Event

class DataType(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Command: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceConfiguration.DataType
    ) = ...  # static # readonly
    CommandGroup: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceConfiguration.DataType
    ) = ...  # static # readonly
    Settings: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceConfiguration.DataType
    ) = ...  # static # readonly
    Unknown: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceConfiguration.DataType
    ) = ...  # static # readonly

class EditorForm(
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
    def __init__(self, compliance: ICompliance) -> None: ...

class SettingsControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceConfiguration.IMapView,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.IWin32Window,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
):  # Class
    def __init__(self) -> None: ...

class TitleLabel(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.Label,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
):  # Class
    def __init__(self) -> None: ...

    BackColor2: System.Drawing.Color
