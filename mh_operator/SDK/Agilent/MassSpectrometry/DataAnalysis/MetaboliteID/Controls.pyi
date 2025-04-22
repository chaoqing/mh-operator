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

from .OS import FolderViewMode

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls

class AddonWindowLocation(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Bottom: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.AddonWindowLocation
    ) = ...  # static # readonly
    Right: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.AddonWindowLocation
    ) = ...  # static # readonly

class ControlsID(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ButtonCancel: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    ButtonHelp: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    ButtonOpen: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    CheckBoxReadOnly: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    ComboFileName: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    ComboFileType: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    ComboFolder: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    DefaultView: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    GroupFolder: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    LabelFileName: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    LabelFileType: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    LabelLookIn: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly
    LeftToolBar: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.ControlsID
    ) = ...  # static # readonly

class OpenFileDialogEx(
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

    DefaultViewMode: FolderViewMode
    OpenDialog: System.Windows.Forms.OpenFileDialog  # readonly
    StartLocation: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.AddonWindowLocation
    )

    def OnFileNameChanged(self, fileName: str) -> None: ...
    def OnClosingDialog(self) -> None: ...
    def OnFolderNameChanged(self, folderName: str) -> None: ...
    @overload
    def ShowDialog(self) -> System.Windows.Forms.DialogResult: ...
    @overload
    def ShowDialog(
        self, owner: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

    ClosingDialog: System.EventHandler  # Event
    FileNameChanged: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.OpenFileDialogEx.PathChangedHandler
    )  # Event
    FolderNameChanged: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.OpenFileDialogEx.PathChangedHandler
    )  # Event

    # Nested Types

    class PathChangedHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.OpenFileDialogEx,
            filePath: str,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Controls.OpenFileDialogEx,
            filePath: str,
        ) -> None: ...
