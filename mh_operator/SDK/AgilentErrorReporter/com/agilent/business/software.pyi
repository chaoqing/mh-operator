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

# Stubs for namespace: AgilentErrorReporter.com.agilent.business.software

class ErrorReport(
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

    Errors: (
        AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsDataTable
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

    class ErrorsDataTable(
        System.IDisposable,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.ISupportInitializeNotification,
        System.ComponentModel.IComponent,
        Iterable[Any],
        System.Data.DataTable,
        System.IServiceProvider,
        System.ComponentModel.ISupportInitialize,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
    ):  # Class
        def __init__(self) -> None: ...

        ApplicationIDColumn: System.Data.DataColumn  # readonly
        ApplicationNameColumn: System.Data.DataColumn  # readonly
        BinaryDumpColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        CrashDumpTextColumn: System.Data.DataColumn  # readonly
        CrashSummaryColumn: System.Data.DataColumn  # readonly
        ErrorIDColumn: System.Data.DataColumn  # readonly
        FileVersionColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRow
        ): ...
        OperatingSystemColumn: System.Data.DataColumn  # readonly
        StepsToReproduceColumn: System.Data.DataColumn  # readonly
        TimeSubmittedColumn: System.Data.DataColumn  # readonly
        UserContactColumn: System.Data.DataColumn  # readonly
        UserNameColumn: System.Data.DataColumn  # readonly
        XMLStringColumn: System.Data.DataColumn  # readonly

        def GetEnumerator(self) -> Iterator[Any]: ...
        def RemoveErrorsRow(
            self,
            row: AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddErrorsRow(
            self,
            row: AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRow,
        ) -> None: ...
        @overload
        def AddErrorsRow(
            self,
            TimeSubmitted: System.DateTime,
            ApplicationID: int,
            ApplicationName: str,
            FileVersion: str,
            OperatingSystem: str,
            UserName: str,
            UserContact: str,
            CrashSummary: str,
            StepsToReproduce: str,
            CrashDumpText: str,
            XMLString: str,
            BinaryDump: List[int],
        ) -> (
            AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def FindByErrorID(
            self, ErrorID: int
        ) -> (
            AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRow
        ): ...
        def NewErrorsRow(
            self,
        ) -> (
            AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRow
        ): ...

        ErrorsRowChanged: (
            AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRowChangeEventHandler
        )  # Event
        ErrorsRowChanging: (
            AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRowChangeEventHandler
        )  # Event
        ErrorsRowDeleted: (
            AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRowChangeEventHandler
        )  # Event
        ErrorsRowDeleting: (
            AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRowChangeEventHandler
        )  # Event

    class ErrorsRow(System.Data.DataRow):  # Class
        ApplicationID: int
        ApplicationName: str
        BinaryDump: List[int]
        CrashDumpText: str
        CrashSummary: str
        ErrorID: int
        FileVersion: str
        OperatingSystem: str
        StepsToReproduce: str
        TimeSubmitted: System.DateTime
        UserContact: str
        UserName: str
        XMLString: str

        def SetStepsToReproduceNull(self) -> None: ...
        def IsFileVersionNull(self) -> bool: ...
        def IsUserContactNull(self) -> bool: ...
        def SetXMLStringNull(self) -> None: ...
        def SetUserContactNull(self) -> None: ...
        def SetUserNameNull(self) -> None: ...
        def IsBinaryDumpNull(self) -> bool: ...
        def SetFileVersionNull(self) -> None: ...
        def IsUserNameNull(self) -> bool: ...
        def IsXMLStringNull(self) -> bool: ...
        def SetBinaryDumpNull(self) -> None: ...
        def IsOperatingSystemNull(self) -> bool: ...
        def IsStepsToReproduceNull(self) -> bool: ...
        def IsCrashDumpTextNull(self) -> bool: ...
        def SetCrashDumpTextNull(self) -> None: ...
        def SetOperatingSystemNull(self) -> None: ...

    class ErrorsRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRow
        )  # readonly

    class ErrorsRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: AgilentErrorReporter.com.agilent.business.software.ErrorReport.ErrorsRowChangeEvent,
        ) -> None: ...

class ReportErr(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.Web.Services.Protocols.SoapHttpClientProtocol,
):  # Class
    def __init__(self) -> None: ...

    Url: str
    UseDefaultCredentials: bool

    def ReportError(
        self, er: AgilentErrorReporter.com.agilent.business.software.ErrorReport
    ) -> str: ...
    @overload
    def ReportErrorAsync(
        self, er: AgilentErrorReporter.com.agilent.business.software.ErrorReport
    ) -> None: ...
    @overload
    def ReportErrorAsync(
        self,
        er: AgilentErrorReporter.com.agilent.business.software.ErrorReport,
        userState: Any,
    ) -> None: ...
    def CancelAsync(self, userState: Any) -> None: ...

    ReportErrorCompleted: (
        AgilentErrorReporter.com.agilent.business.software.ReportErrorCompletedEventHandler
    )  # Event

class ReportErrorCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class ReportErrorCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: AgilentErrorReporter.com.agilent.business.software.ReportErrorCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: AgilentErrorReporter.com.agilent.business.software.ReportErrorCompletedEventArgs,
    ) -> None: ...
