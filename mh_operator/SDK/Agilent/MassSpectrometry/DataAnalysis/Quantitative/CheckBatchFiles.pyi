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

from .UIUtils2 import ConfigurationElementSectionBase

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles

class AppConfig:  # Class
    ApplicationSettings: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.ApplicationSettings
    )  # readonly
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.AppConfig
    )  # static # readonly
    UserSettings: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.UserSettings
    )  # readonly

    def Save(self) -> None: ...

class ApplicationSettings(ConfigurationElementSectionBase):  # Class
    def __init__(self) -> None: ...

    DumpLogOnNormalExit: bool  # readonly
    ErrorReportingEmailAddress: str  # readonly
    ErrorReportingEnabled: bool  # readonly

class BroncoMethodChecker(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.PicardFolderChecker,
):  # Class
    def __init__(
        self,
        folder: str,
        fileType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType,
        abort: System.Threading.WaitHandle,
    ) -> None: ...

class CheckResults:  # Class
    def __init__(
        self,
        file: str,
        fileType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType,
    ) -> None: ...

    AnalysisTimestamp: str = ...  # static # readonly
    AuditTrailValid: str = ...  # static # readonly
    DataVersion: str = ...  # static # readonly
    HashCodeValid: str = ...  # static # readonly
    LastWrittenTime: str = ...  # static # readonly

    Aborted: bool
    Complete: bool
    Exception: System.Exception
    File: str  # readonly
    FileType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType
    )  # readonly

    def Equals(self, obj: Any) -> bool: ...
    def Contains(self, key: str) -> bool: ...
    def GetValue(self, key: str) -> Any: ...
    def GetError(self, key: str) -> str: ...
    def SetValue(self, key: str, value_: Any) -> None: ...
    def GetHashCode(self) -> int: ...
    def Clone(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResults
    ): ...
    def SetError(self, key: str, error: str) -> None: ...
    def Apply(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
    ) -> None: ...

class CheckResultsDataSet(
    System.IDisposable,
    System.ComponentModel.ISupportInitializeNotification,
    System.IServiceProvider,
    System.Data.DataSet,
    System.Xml.Serialization.IXmlSerializable,
    System.Runtime.Serialization.ISerializable,
    System.ComponentModel.IListSource,
    System.ComponentModel.ISupportInitialize,
    System.ComponentModel.IComponent,
):  # Class
    def __init__(self) -> None: ...

    BatchFiles: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesDataTable
    )  # readonly
    Relations: System.Data.DataRelationCollection  # readonly
    SchemaSerializationMode: System.Data.SchemaSerializationMode
    Tables: System.Data.DataTableCollection  # readonly

    @staticmethod
    def GetTypedDataSetSchema(
        xs: System.Xml.Schema.XmlSchemaSet,
    ) -> System.Xml.Schema.XmlSchemaComplexType: ...
    def Clone(self) -> System.Data.DataSet: ...

    # Nested Types

    class BatchFilesDataTable(
        System.IServiceProvider,
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow
        ],
    ):  # Class
        def __init__(self) -> None: ...

        AnalysisTimestampColumn: System.Data.DataColumn  # readonly
        AuditTrailValidColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DataVersionColumn: System.Data.DataColumn  # readonly
        ErrorColumn: System.Data.DataColumn  # readonly
        FilePathColumn: System.Data.DataColumn  # readonly
        FileTypeColumn: System.Data.DataColumn  # readonly
        HashCodeValidColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow
        ): ...
        LastWrittenTimeColumn: System.Data.DataColumn  # readonly
        MessagesColumn: System.Data.DataColumn  # readonly

        @overload
        def AddBatchFilesRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
        ) -> None: ...
        @overload
        def AddBatchFilesRow(
            self,
            FilePath: str,
            FileType: str,
            Error: bool,
            HashCodeValid: bool,
            AuditTrailValid: bool,
            DataVersion: int,
            AnalysisTimestamp: System.DateTime,
            LastWrittenTime: System.DateTime,
            Messages: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow
        ): ...
        def RemoveBatchFilesRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def Clone(self) -> System.Data.DataTable: ...
        def NewBatchFilesRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow
        ): ...

        BatchFilesRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRowChangeEventHandler
        )  # Event
        BatchFilesRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRowChangeEventHandler
        )  # Event
        BatchFilesRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRowChangeEventHandler
        )  # Event
        BatchFilesRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRowChangeEventHandler
        )  # Event

    class BatchFilesRow(System.Data.DataRow):  # Class
        AnalysisTimestamp: System.DateTime
        AuditTrailValid: bool
        DataVersion: int
        Error: bool
        FilePath: str
        FileType: str
        HashCodeValid: bool
        LastWrittenTime: System.DateTime
        Messages: str

        def IsFileTypeNull(self) -> bool: ...
        def SetErrorNull(self) -> None: ...
        def SetMessagesNull(self) -> None: ...
        def IsMessagesNull(self) -> bool: ...
        def SetLastWrittenTimeNull(self) -> None: ...
        def SetDataVersionNull(self) -> None: ...
        def IsHashCodeValidNull(self) -> bool: ...
        def IsAnalysisTimestampNull(self) -> bool: ...
        def IsErrorNull(self) -> bool: ...
        def SetHashCodeValidNull(self) -> None: ...
        def IsAuditTrailValidNull(self) -> bool: ...
        def SetAnalysisTimestampNull(self) -> None: ...
        def IsLastWrittenTimeNull(self) -> bool: ...
        def IsDataVersionNull(self) -> bool: ...
        def SetAuditTrailValidNull(self) -> None: ...
        def SetFileTypeNull(self) -> None: ...

    class BatchFilesRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow
        )  # readonly

    class BatchFilesRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRowChangeEvent,
        ) -> None: ...

class CheckerBase(System.IDisposable):  # Class
    PathName: str  # readonly

    def Dispose(self) -> None: ...
    def ApplyResults(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
    ) -> None: ...

    Complete: System.EventHandler  # Event
    Started: System.EventHandler  # Event

class CommandLine:  # Class
    def __init__(self) -> None: ...

    Culture: str
    Folders: List[str]
    Help: bool

class DirectoryChecker(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckerBase,
):  # Class
    def __init__(
        self,
        directory: str,
        recursive: bool,
        checkPicardSamples: bool,
        checkPicardMethods: bool,
        results: Dict[str, bool],
        abortHandle: System.Threading.WaitHandle,
    ) -> None: ...

    PathName: str  # readonly
    Recursive: bool  # readonly

    def Check(self) -> None: ...
    @staticmethod
    def IsBroncoMethodFolder(folder: str) -> bool: ...

    FileCheckComplete: System.EventHandler  # Event
    FileCheckStarted: System.EventHandler  # Event

class FileChecker(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckerBase,
):  # Class
    def __init__(
        self,
        file: str,
        fileType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType,
        abort: System.Threading.WaitHandle,
    ) -> None: ...

    PathName: str  # readonly
    Results: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResults
    )  # readonly

    def Check(self) -> None: ...
    def ApplyResults(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
    ) -> None: ...

class FileType(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    AcqMethod: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType
    ) = ...  # static # readonly
    Batch: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType
    ) = ...  # static # readonly
    MethodFile: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType
    ) = ...  # static # readonly
    ReportResult: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType
    ) = ...  # static # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType
    ) = ...  # static # readonly
    Study: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType
    ) = ...  # static # readonly
    Worklist: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType
    ) = ...  # static # readonly

class Formatter(System.IDisposable):  # Class
    def WriteFileCheck(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
    ) -> None: ...
    def Dispose(self) -> None: ...

class GenericFormatter(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.Formatter,
):  # Class
    def __init__(self, writer: System.IO.TextWriter, closeOnDispose: bool) -> None: ...
    def WriteFileCheck(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
    ) -> None: ...

class PicardFolderChecker(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckerBase,
):  # Class
    def __init__(
        self,
        folder: str,
        fileType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.FileType,
        abort: System.Threading.WaitHandle,
    ) -> None: ...

    PathName: str  # readonly

    def Check(self) -> None: ...
    def ApplyResults(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
    ) -> None: ...

class ResultsForm(
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
    def Start(self) -> None: ...
    def AddFolders(self, folders: List[str]) -> None: ...

class SelectFolders(
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
    def SetSelectedFolders(self, folders: List[str]) -> None: ...
    def GetSelectedFolders(self) -> List[str]: ...

class TextFormatter(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.Formatter,
):  # Class
    def __init__(
        self, writer: System.IO.TextWriter, closeOnDispose: bool, delimiter: str
    ) -> None: ...
    def WriteFileCheck(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
    ) -> None: ...

class UserSettings(ConfigurationElementSectionBase):  # Class
    def __init__(self) -> None: ...

    LastFolder: str

class XmlFormatter(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.Formatter,
):  # Class
    def __init__(self, writer: System.IO.TextWriter, closeOnDispose: bool) -> None: ...
    def WriteFileCheck(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CheckBatchFiles.CheckResultsDataSet.BatchFilesRow,
    ) -> None: ...
