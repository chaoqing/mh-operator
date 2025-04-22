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

from . import Commands, ReportFixedGraphicsDataSet, Tools

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics

class AppException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class CommandLine:  # Class
    def __init__(self) -> None: ...

    Culture: str
    File: str

    def Form_Shown(self, sender: Any, e: System.EventArgs) -> None: ...

class CompoundGridView(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.DataGridView,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
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
    def Initialize(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Context,
    ) -> None: ...
    def Copy(self) -> None: ...
    def CanCopy(self) -> bool: ...
    def CanPaste(self) -> bool: ...
    def Delete(self, copyToClipboard: bool) -> None: ...
    def Paste(self) -> None: ...
    def CanDelete(self) -> bool: ...

class Context(
    Agilent.MassSpectrometry.CommandModel.Model.ICommandHistory,
    Agilent.MassSpectrometry.CommandModel.CommandHistory,
    System.IDisposable,
):  # Class
    def __init__(self) -> None: ...

    DataSet: ReportFixedGraphicsDataSet  # readonly
    File: str  # readonly
    IsDirty: bool  # readonly
    NewCompound: ReportFixedGraphicsDataSet.CompoundRow  # readonly

    def Save(self) -> None: ...
    def Open(self, file: str, readOnly: bool) -> None: ...
    def StartNewCompound(self) -> None: ...
    def NewFile(self) -> None: ...
    def SetNewCompoundColumn(self, name: str, value_: Any) -> None: ...
    def SetCompoundColumn(self, compoundName: str, name: str, value_: Any) -> None: ...
    def NewSample(self, sampleName: str) -> None: ...
    def CancelNewCompound(self) -> None: ...
    def SaveAs(self, path: str) -> None: ...
    def SetSampleColumn(self, sampleName: str, name: str, value_: Any) -> None: ...
    def RemoveSample(self, sampleName: str) -> None: ...
    def CommitNewCompound(self) -> None: ...
    def RemoveCompound(self, compoundName: str) -> None: ...

    NewCompoundCancel: System.EventHandler  # Event
    NewCompoundColumnChanged: System.Data.DataColumnChangeEventHandler  # Event
    NewCompoundCommit: System.EventHandler  # Event
    NewCompoundStart: System.EventHandler  # Event

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

    Context: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Context
    )  # readonly
    FilePath: str  # readonly

    def OpenFile(self, file: str, readOnly: bool) -> bool: ...
    def Copy(self) -> None: ...
    def CanCopy(self) -> bool: ...
    def CanPaste(self) -> bool: ...
    def CommitEdit(self, commitNewRow: bool) -> bool: ...
    def Delete(self, copyToClipboard: bool) -> None: ...
    def Paste(self) -> None: ...
    def CanDelete(self) -> bool: ...
