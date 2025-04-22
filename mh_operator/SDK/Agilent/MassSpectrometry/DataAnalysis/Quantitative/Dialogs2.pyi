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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs2

class ControlBox:  # Class
    HasHelpButtonProperty: System.Windows.DependencyProperty  # static # readonly
    HasMaximizeButtonProperty: System.Windows.DependencyProperty  # static # readonly
    HasMinimizeButtonProperty: System.Windows.DependencyProperty  # static # readonly
    HasSysMenuProperty: System.Windows.DependencyProperty  # static # readonly

    @staticmethod
    def SetHasMaximizeButton(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def SetHasHelpButton(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def SetHasMinimizeButton(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def SetHasSysMenu(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def GetHasHelpButton(element: System.Windows.Window) -> bool: ...
    @staticmethod
    def GetHasMaximizeButton(element: System.Windows.Window) -> bool: ...
    @staticmethod
    def GetHasSysMenu(element: System.Windows.Window) -> bool: ...
    @staticmethod
    def GetHasMinimizeButton(element: System.Windows.Window) -> bool: ...

class LineStyleDialog(
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
        self,
        defaultShow: bool,
        defaultColor: System.Drawing.Color,
        defaultDashStyle: System.Drawing.Drawing2D.DashStyle,
    ) -> None: ...

    CheckBoxShowLineText: str
    Color: System.Drawing.Color
    DashStyle: System.Drawing.Drawing2D.DashStyle
    ShowLine: bool

class OpenDirectoryDialog(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    AllowMultipleSelections: bool
    Directories: str  # readonly
    DirectoryMustExist: bool
    Extension: str
    FileFilter: str
    HelpFile: str
    HelpTopicId: int
    InitialDir: str
    ReadOnly: bool
    ReadOnlyCheckBox: bool
    Title: str

    def Dispose(self) -> None: ...
    def ShowDialog(self, parent: System.Windows.Forms.IWin32Window) -> bool: ...

class PaneDimensionControl(
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

    Columns: int  # readonly
    Rows: int  # readonly

    def CalcSize(self) -> System.Drawing.Size: ...

    DimensionSelected: System.EventHandler  # Event

class PaneDimensionDialogs(
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

    Columns: int  # readonly
    Rows: int  # readonly

    DimensionSelected: System.EventHandler  # Event

class ProgressDialog(
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

    Argument: Any
    CancelButtonText: str
    CancelButtonVisible: bool
    CancellationPending: bool  # readonly
    Exception: System.Exception  # readonly
    Marquee: bool
    Message: str
    ProgressMaximum: int
    ProgressMinimum: int
    ProgressStep: int
    ProgressValue: int

    def ReportProgress(self, percent: int, state: Any) -> None: ...
    def Cancel(self) -> None: ...

    CancelButtonClick: System.EventHandler  # Event
    DoWork: System.ComponentModel.DoWorkEventHandler  # Event
    ProgressChanged: System.ComponentModel.ProgressChangedEventHandler  # Event

class ProgressWindowWPF(
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

    CanCancel: bool
    Exception: System.Exception  # readonly
    IsIndeterminate: bool
    Marquee: bool
    Maximum: float
    Message: str
    Minimum: float
    Title: str
    Value: float

    def ButtonCancel_Click(
        self, sender: Any, e: System.Windows.RoutedEventArgs
    ) -> None: ...
    def InitializeComponent(self) -> None: ...
    def ReportProgress(self, percentProgress: int, state: Any) -> None: ...

    Cancel: System.EventHandler  # Event
    DoWork: System.ComponentModel.DoWorkEventHandler  # Event
    ProgressChanged: System.ComponentModel.ProgressChangedEventHandler  # Event
    RunWorkerCompleted: System.ComponentModel.RunWorkerCompletedEventHandler  # Event

class SystemInfoDialog(
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
    @staticmethod
    def ShowSystemInfo(parent: System.Windows.Forms.IWin32Window) -> None: ...

class SystemInfoItem:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, fileVersionInfo: System.Diagnostics.FileVersionInfo) -> None: ...
    @overload
    def __init__(
        self,
        fileVersionInfo: System.Diagnostics.FileVersionInfo,
        assembly: System.Reflection.Assembly,
    ) -> None: ...

    AssemblyConfiguration: str  # readonly
    AssemblyCulture: str  # readonly
    AssemblyTitle: str  # readonly
    ComVisible: Optional[bool]  # readonly
    Comments: str  # readonly
    CompanyName: str  # readonly
    FileDescription: str  # readonly
    FileVersion: str  # readonly
    Guid: str  # readonly
    InternalName: str  # readonly
    IsDebug: Optional[bool]  # readonly
    IsPatched: Optional[bool]  # readonly
    IsPrivateBuild: Optional[bool]  # readonly
    IsSpecialBuild: Optional[bool]  # readonly
    Language: str  # readonly
    LegalCopyright: str  # readonly
    LegalTrademarks: str  # readonly
    Location: str  # readonly
    Name: str  # readonly
    PrivateBuild: str  # readonly
    ProductName: str  # readonly
    ProductVersion: str  # readonly
    SpecialBuild: str  # readonly

class SystemInfoItemCollection(
    System.ComponentModel.IRaiseItemChangedEvents,
    System.ComponentModel.BindingList[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs2.SystemInfoItem
    ],
    Sequence[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs2.SystemInfoItem
    ],
    System.ComponentModel.IBindingList,
    System.ComponentModel.ICancelAddNew,
    System.ComponentModel.IComponent,
    Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs2.SystemInfoItem
    ],
    List[Any],
    Iterable[Any],
    List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs2.SystemInfoItem],
    Sequence[Any],
    System.IDisposable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, container: System.ComponentModel.IContainer) -> None: ...

    SynchronizeInvoke: System.ComponentModel.ISynchronizeInvoke

    def Dispose(self) -> None: ...

class WinFormHostWindow(System.Windows.Forms.IWin32Window):  # Class
    def __init__(self, window: System.Windows.Window) -> None: ...

    Handle: System.IntPtr  # readonly
