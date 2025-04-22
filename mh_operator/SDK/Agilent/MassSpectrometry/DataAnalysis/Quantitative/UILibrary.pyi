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

from . import INumericCustomFormat
from .Compliance import ICompliance

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UILibrary

class EntryGrid(
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
    @staticmethod
    def GetDefaultColumnNames() -> List[str]: ...

class ILibraryApp(Agilent.MassHunter.Quantitative.UIModel.ILibraryApp):  # Interface
    SelectedEntry: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UILibrary.ILibraryEntry
    )  # readonly
    Site: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UILibrary.ILibraryAppSite

    def ClearEntries(self) -> None: ...
    def ShowMessage(
        self,
        message: str,
        buttons: System.Windows.Forms.MessageBoxButtons,
        icon: System.Windows.Forms.MessageBoxIcon,
    ) -> System.Windows.Forms.DialogResult: ...
    def AddTool(self, name: str, caption: str, image: System.Drawing.Image) -> None: ...
    def ExitApplication(self) -> None: ...

class ILibraryAppSite(
    Agilent.MassHunter.Quantitative.UIModel.ILibraryAppSite
):  # Interface
    def OnToolClicked(self, name: str) -> None: ...
    def OnCloseWindow(self) -> None: ...

class ILibraryEntry(object):  # Interface
    BoilPt: float  # readonly
    CASNumber: str  # readonly
    CompoundName: str  # readonly
    Formula: str  # readonly
    Library: Agilent.MassSpectrometry.DataAnalysis.ILibrary  # readonly
    LibraryPath: str  # readonly
    LibraryRetentionIndex: float  # readonly
    LibraryRetentionTime: float  # readonly
    MatchFactor: float  # readonly
    MeltPt: float  # readonly
    MolecularWeight: float  # readonly
    OverlapCount: int  # readonly
    RetentionTimeDifference: float  # readonly
    Spectrum: Agilent.MassHunter.Quantitative.UIModel.ISpectrumTransfer  # readonly
    SpectrumId: Agilent.MassSpectrometry.DataAnalysis.ISpectrumId  # readonly
    TargetRetentionIndex: float  # readonly

class LibraryApp(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UILibrary.ILibraryApp,
    Agilent.MassHunter.Quantitative.UIModel.ILibraryApp,
    System.IDisposable,
):  # Class
    HasLibrary: bool  # readonly
    TargetSpectrum: (
        Agilent.MassHunter.Quantitative.UIModel.ISpectrumTransfer
    )  # readonly

    @staticmethod
    def CreateInstance(
        compliance: ICompliance,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UILibrary.ILibraryApp: ...
    def SetLibraries(
        self,
        libraries: List[Agilent.MassHunter.Quantitative.UIModel.ILibraryItem],
        searchType: Agilent.MassSpectrometry.DataAnalysis.MultipleLibrarySearchType,
        libraryUnitMassFormat: INumericCustomFormat,
        libraryAccurateMassFormat: INumericCustomFormat,
    ) -> None: ...
    def ShowWindow(self) -> None: ...
    def Dispose(self) -> None: ...
    def Search(self) -> None: ...
    def SetTargetSpectrum(
        self,
        transfer: Agilent.MassHunter.Quantitative.UIModel.ISpectrumTransfer,
        massDisplayFormat: INumericCustomFormat,
    ) -> None: ...

class LibraryConfiguration:  # Class
    Section: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UILibrary.LibraryConfigurationSettingsSection
    )  # static # readonly

class LibraryConfigurationSettingsSection(
    System.Configuration.ConfigurationSection
):  # Class
    def __init__(self) -> None: ...

    BackColor: System.Drawing.Color
    ForeColor: System.Drawing.Color
    LibrarySpectrumColor: System.Drawing.Color
    MolecularStructureColor: System.Drawing.Color  # readonly
    SupportsCASLink: bool  # readonly
    TargetSpectrumColor: System.Drawing.Color

class LibraryException(
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

class LibraryItem(Agilent.MassHunter.Quantitative.UIModel.ILibraryItem):  # Struct
    def __init__(
        self,
        library: Agilent.MassSpectrometry.DataAnalysis.ILibrary,
        parameters: Agilent.MassSpectrometry.DataAnalysis.LibrarySearchParams,
    ) -> None: ...

    Library: Agilent.MassSpectrometry.DataAnalysis.ILibrary  # readonly
    Parameters: Agilent.MassSpectrometry.DataAnalysis.LibrarySearchParams  # readonly

class LibraryPrintDocument(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.Drawing.Printing.PrintDocument,
):  # Class
    def __init__(
        self,
        title: str,
        grid: System.Windows.Forms.DataGridView,
        plot: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
    ) -> None: ...

class LibraryWindow(
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

class SpectrumPlotControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
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
    Agilent.MassSpectrometry.GUI.Plot.PlotControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

    ShowMolecularStructure: bool

    def GetAutoScaleRangeX(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetPreferredYRangeLimit(
        self, row: int, column: int
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
