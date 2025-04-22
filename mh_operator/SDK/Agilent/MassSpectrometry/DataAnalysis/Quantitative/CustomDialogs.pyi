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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs

class BATCHFILEINFO:  # Struct
    Analyst: str
    AuditTrail: bool
    BatchFile: str
    DataVersion: int
    DateAnalyzed: float
    DateLastSaved: float
    Size: int
    lStructSize: int

class EGDFLAGS(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    EGD_DISABLE_PANES: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.EGDFLAGS
    ) = ...  # static # readonly
    EGD_DISABLE_SCALE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.EGDFLAGS
    ) = ...  # static # readonly
    EGD_FIT_TO: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.EGDFLAGS
    ) = ...  # static # readonly
    EGD_SELECTED_PANE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.EGDFLAGS
    ) = ...  # static # readonly
    EGD_UNIT_CM: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.EGDFLAGS
    ) = ...  # static # readonly
    EGD_UNIT_INCHES: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.EGDFLAGS
    ) = ...  # static # readonly

class EXPORTFILEDIALOG:  # Struct
    fOpenFile: bool
    hwndOwner: System.IntPtr
    lStructSize: int
    lpstrFile: str
    lpstrFilter: str
    lpstrHelpFile: str
    lpstrInitialDir: str
    lpstrTitle: str
    nFilterIndex: int
    nHelpTopicId: int

class EXPORTGRAPHICSFILEDIALOG:  # Struct
    Flags: int
    dpix: float
    dpiy: float
    height: float
    hwndOwner: System.IntPtr
    lStructSize: int
    lpstrFile: str
    lpstrFilter: str
    lpstrHelpFile: str
    lpstrInitialDir: str
    lpstrTitle: str
    nFilterIndex: int
    nHelpTopicId: int
    scale: float
    width: float

class GRAPHICSPAGESETUPDIALOG:  # Struct
    Flags: int
    hDevMode: System.IntPtr
    hDevNames: System.IntPtr
    hPreview: System.IntPtr
    height: int
    hwndOwner: System.IntPtr
    lStructSize: int
    ptImageSize: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.POINTF
    rtMargin: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.RECT
    scale: float
    width: int

class GetBatchFileInfo(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(
        self,
        info: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.BATCHFILEINFO,
        result: System.IAsyncResult,
    ) -> bool: ...
    def BeginInvoke(
        self,
        info: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.BATCHFILEINFO,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        info: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.BATCHFILEINFO,
    ) -> bool: ...

class NativeMethods:  # Class
    @staticmethod
    def ShowExportGraphicsFileDialog(
        dlg: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.EXPORTGRAPHICSFILEDIALOG,
    ) -> bool: ...
    @staticmethod
    def ExportFileDialog(
        dlg: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.EXPORTFILEDIALOG,
    ) -> bool: ...
    @staticmethod
    def PrintGraphicsDialog(
        dlg: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PRINTGRAPHICSDIALOG,
    ) -> int: ...
    @staticmethod
    def ShowOpenBatchDialog(
        dlg: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OPENBATCHDIALOG,
    ) -> bool: ...
    @staticmethod
    def GraphicsPageSetupDialog(
        dlg: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.GRAPHICSPAGESETUPDIALOG,
    ) -> bool: ...
    @staticmethod
    def GetDllDirectory(length: int, builder: System.Text.StringBuilder) -> bool: ...
    @staticmethod
    def ShowOpenDirectoriesDialog(
        dlg: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OPENDIRECTORIESDIALOG,
        folders: str,
    ) -> bool: ...
    @staticmethod
    def SetDllDirectory(lpPathName: str) -> bool: ...

class OBDFLAGS(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    OBD_AUDITTRAIL: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OBDFLAGS
    ) = ...  # static # readonly
    OBD_AUDITTRAIL_CHECKBOX: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OBDFLAGS
    ) = ...  # static # readonly
    OBD_AUDITTRAIL_CHECKBOX_DISABLED: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OBDFLAGS
    ) = ...  # static # readonly
    OBD_FILE_MUST_EXIST: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OBDFLAGS
    ) = ...  # static # readonly
    OBD_HIDE_AUDITTRAIL_COLUMN: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OBDFLAGS
    ) = ...  # static # readonly
    OBD_NO_OVERWRITE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OBDFLAGS
    ) = ...  # static # readonly
    OBD_READONLY: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OBDFLAGS
    ) = ...  # static # readonly
    OBD_READONLY_CHECKBOX: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OBDFLAGS
    ) = ...  # static # readonly
    OBD_SAVE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OBDFLAGS
    ) = ...  # static # readonly

class OPENBATCHDIALOG:  # Struct
    Flags: int
    hwndOwner: System.IntPtr
    lStructSize: int
    lpfnGetBatchFileInfo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.GetBatchFileInfo
    )
    lpstrBatchFileExtensions: str
    lpstrBatchFolderExtension: str
    lpstrFile: str
    lpstrFilter: str
    lpstrHelpFile: str
    lpstrInitialDir: str
    lpstrOKButtonText: str
    lpstrResultsFolder: str
    lpstrTitle: str
    nFilterIndex: int
    nHelpTopicId: int

class OPENDIRECTORIESDIALOG:  # Struct
    Flags: int
    bstrDirectories: System.IntPtr
    hwndOwner: System.IntPtr
    lStructSize: int
    lpstrExtension: str
    lpstrFileFilter: str
    lpstrHelpFile: str
    lpstrInitialDir: str
    lpstrTitle: str
    nHelpTopicId: int

class OSDFLAGS(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    OSD_ALLOWMULTISELECT: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OSDFLAGS
    ) = ...  # static # readonly
    OSD_DIRECTORYMUSTEXIST: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OSDFLAGS
    ) = ...  # static # readonly
    OSD_READONLY: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OSDFLAGS
    ) = ...  # static # readonly
    OSD_READONLY_CHECKBOX: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.OSDFLAGS
    ) = ...  # static # readonly

class PGDFLAGS(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    PGD_ADJUSTTO: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PGDFLAGS
    ) = ...  # static # readonly
    PGD_COLLATE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PGDFLAGS
    ) = ...  # static # readonly
    PGD_CURRENTPAGE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PGDFLAGS
    ) = ...  # static # readonly
    PGD_FITTO: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PGDFLAGS
    ) = ...  # static # readonly
    PGD_FITTOSHEET: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PGDFLAGS
    ) = ...  # static # readonly
    PGD_FITTOSHEETWIDTH: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PGDFLAGS
    ) = ...  # static # readonly
    PGD_PRINTTOFILE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PGDFLAGS
    ) = ...  # static # readonly
    PGD_SOMEPAGES: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PGDFLAGS
    ) = ...  # static # readonly
    PGD_UNIT_INCHES: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PGDFLAGS
    ) = ...  # static # readonly

class POINTF:  # Struct
    x: float
    y: float

class PRINTGRAPHICSDIALOG:  # Struct
    Flags: int
    PRINTPAGE_SIZE: int = ...  # static # readonly
    hDevMode: System.IntPtr
    hDevNames: System.IntPtr
    height: int
    hwndOwner: System.IntPtr
    lStructSize: int
    lpPageRanges: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PRINTPAGERANGE
    ]
    nCopies: int
    nPageRanges: int
    nPages: int
    scale: float
    width: int

class PRINTPAGERANGE:  # Struct
    nPageFrom: int
    nPageTo: int

class PrintGraphicsDialogResult(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Apply: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PrintGraphicsDialogResult
    ) = ...  # static # readonly
    Cancel: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PrintGraphicsDialogResult
    ) = ...  # static # readonly
    Error: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PrintGraphicsDialogResult
    ) = ...  # static # readonly
    Print: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CustomDialogs.PrintGraphicsDialogResult
    ) = ...  # static # readonly

class RECT:  # Struct
    bottom: int
    left: int
    right: int
    top: int

class SetCurrentFolder(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def Dispose(self) -> None: ...
