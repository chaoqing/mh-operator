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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod

class ReportMethodDataSet(
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

    SchemaVersion: int  # static # readonly

    CompoundGraphicsRange: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeDataTable
    )  # readonly
    Filtering: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringDataTable
    )  # readonly
    FilteringValue: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueDataTable
    )  # readonly
    Formatting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingDataTable
    )  # readonly
    Globals: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsDataTable
    )  # readonly
    GraphicsRange: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeDataTable
    )  # readonly
    PeakChromatogramGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsDataTable
    )  # readonly
    PeakQualifiersGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsDataTable
    )  # readonly
    PeakSpectrumGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsDataTable
    )  # readonly
    PrePostProcess: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessDataTable
    )  # readonly
    Relations: System.Data.DataRelationCollection  # readonly
    Report: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportDataTable
    )  # readonly
    SampleChromatogramGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsDataTable
    )  # readonly
    SchemaSerializationMode: System.Data.SchemaSerializationMode
    Tables: System.Data.DataTableCollection  # readonly
    TargetCompoundCalibration: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationDataTable
    )  # readonly
    UnknownsIonPeaksGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsDataTable
    )  # readonly
    UnknownsSampleChromatogramGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsDataTable
    )  # readonly
    UnknownsSpectrumGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsDataTable
    )  # readonly

    @staticmethod
    def GetTypedDataSetSchema(
        xs: System.Xml.Schema.XmlSchemaSet,
    ) -> System.Xml.Schema.XmlSchemaComplexType: ...
    def GetSchemaVersionNumber(self) -> int: ...
    def Clone(self) -> System.Data.DataSet: ...

    # Nested Types

    class CompoundGraphicsRangeDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow
        ],
        System.ComponentModel.IComponent,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow
        ],
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        CompoundGraphicsIDColumn: System.Data.DataColumn  # readonly
        CompoundNameColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow
        ): ...
        MaxMzColumn: System.Data.DataColumn  # readonly
        MaxXColumn: System.Data.DataColumn  # readonly
        MaxYColumn: System.Data.DataColumn  # readonly
        MinMzColumn: System.Data.DataColumn  # readonly
        MinXColumn: System.Data.DataColumn  # readonly
        MinYColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemoveCompoundGraphicsRangeRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow,
        ) -> None: ...
        def Clone(self) -> System.Data.DataTable: ...
        def FindByReportIDCompoundGraphicsID(
            self, ReportID: int, CompoundGraphicsID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow
        ): ...
        def NewCompoundGraphicsRangeRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow
        ): ...
        @overload
        def AddCompoundGraphicsRangeRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow,
        ) -> None: ...
        @overload
        def AddCompoundGraphicsRangeRow(
            self,
            parentGraphicsRangeRowByFK_FixedRangeGraphics_FixedRangeCompoundGraphics: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow,
            CompoundGraphicsID: int,
            CompoundName: str,
            MinY: float,
            MaxY: float,
            MinX: float,
            MaxX: float,
            MinMz: float,
            MaxMz: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow
        ): ...

        CompoundGraphicsRangeRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRowChangeEventHandler
        )  # Event
        CompoundGraphicsRangeRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRowChangeEventHandler
        )  # Event
        CompoundGraphicsRangeRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRowChangeEventHandler
        )  # Event
        CompoundGraphicsRangeRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRowChangeEventHandler
        )  # Event

    class CompoundGraphicsRangeRow(System.Data.DataRow):  # Class
        CompoundGraphicsID: int
        CompoundName: str
        GraphicsRangeRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow
        )
        MaxMz: float
        MaxX: float
        MaxY: float
        MinMz: float
        MinX: float
        MinY: float
        ReportID: int

        def IsMinXNull(self) -> bool: ...
        def IsMinYNull(self) -> bool: ...
        def SetMinYNull(self) -> None: ...
        def IsCompoundNameNull(self) -> bool: ...
        def IsMaxYNull(self) -> bool: ...
        def SetMaxMzNull(self) -> None: ...
        def SetMaxYNull(self) -> None: ...
        def IsMaxMzNull(self) -> bool: ...
        def IsMaxXNull(self) -> bool: ...
        def SetMinMzNull(self) -> None: ...
        def SetMinXNull(self) -> None: ...
        def SetCompoundNameNull(self) -> None: ...
        def SetMaxXNull(self) -> None: ...
        def IsMinMzNull(self) -> bool: ...

    class CompoundGraphicsRangeRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow
        )  # readonly

    class CompoundGraphicsRangeRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRowChangeEvent,
        ) -> None: ...

    class FilteringDataTable(
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow
        ],
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        Count: int  # readonly
        FilteringIDColumn: System.Data.DataColumn  # readonly
        FormattingIDColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow
        ): ...
        ReportIDColumn: System.Data.DataColumn  # readonly
        TypeColumn: System.Data.DataColumn  # readonly

        def FindByFilteringIDFormattingIDReportID(
            self, FilteringID: int, FormattingID: int, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow
        ): ...
        def NewFilteringRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddFilteringRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow,
        ) -> None: ...
        @overload
        def AddFilteringRow(
            self, ReportID: int, FormattingID: int, FilteringID: int, Type: str
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveFilteringRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow,
        ) -> None: ...

        FilteringRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRowChangeEventHandler
        )  # Event
        FilteringRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRowChangeEventHandler
        )  # Event
        FilteringRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRowChangeEventHandler
        )  # Event
        FilteringRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRowChangeEventHandler
        )  # Event

    class FilteringRow(System.Data.DataRow):  # Class
        FilteringID: int
        FormattingID: int
        FormattingRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow
        )
        ReportID: int
        Type: str

        def GetFilteringValueRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow
        ]: ...
        def IsTypeNull(self) -> bool: ...
        def SetTypeNull(self) -> None: ...

    class FilteringRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow
        )  # readonly

    class FilteringRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRowChangeEvent,
        ) -> None: ...

    class FilteringValueDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow
        ],
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        Count: int  # readonly
        FilteringIDColumn: System.Data.DataColumn  # readonly
        FilteringValueIDColumn: System.Data.DataColumn  # readonly
        FormattingIDColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow
        ): ...
        NameColumn: System.Data.DataColumn  # readonly
        OperatorColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        ValueColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemoveFilteringValueRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow,
        ) -> None: ...
        def NewFilteringValueRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow
        ): ...
        def FindByReportIDFormattingIDFilteringIDFilteringValueID(
            self,
            ReportID: int,
            FormattingID: int,
            FilteringID: int,
            FilteringValueID: int,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        @overload
        def AddFilteringValueRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow,
        ) -> None: ...
        @overload
        def AddFilteringValueRow(
            self,
            ReportID: int,
            FormattingID: int,
            FilteringID: int,
            FilteringValueID: int,
            Name: str,
            Value: str,
            Operator: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow
        ): ...

        FilteringValueRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRowChangeEventHandler
        )  # Event
        FilteringValueRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRowChangeEventHandler
        )  # Event
        FilteringValueRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRowChangeEventHandler
        )  # Event
        FilteringValueRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRowChangeEventHandler
        )  # Event

    class FilteringValueRow(System.Data.DataRow):  # Class
        FilteringID: int
        FilteringRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow
        )
        FilteringValueID: int
        FormattingID: int
        Name: str
        Operator: str
        ReportID: int
        Value: str

        def IsNameNull(self) -> bool: ...
        def SetValueNull(self) -> None: ...
        def SetOperatorNull(self) -> None: ...
        def SetNameNull(self) -> None: ...
        def IsValueNull(self) -> bool: ...
        def IsOperatorNull(self) -> bool: ...

    class FilteringValueRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRow
        )  # readonly

    class FilteringValueRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringValueRowChangeEvent,
        ) -> None: ...

    class FormattingDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AuditTrailReportColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DestinationFileNameColumn: System.Data.DataColumn  # readonly
        FormattingIDColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow
        ): ...
        OpenPublishedFileColumn: System.Data.DataColumn  # readonly
        PostProcessIDColumn: System.Data.DataColumn  # readonly
        PreferredCultureColumn: System.Data.DataColumn  # readonly
        PreferredPageSizeColumn: System.Data.DataColumn  # readonly
        PrinterNameColumn: System.Data.DataColumn  # readonly
        PublishFormatColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        TemplateColumn: System.Data.DataColumn  # readonly
        TypeColumn: System.Data.DataColumn  # readonly

        @overload
        def AddFormattingRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow,
        ) -> None: ...
        @overload
        def AddFormattingRow(
            self,
            parentReportRowByFK_Report_Formatting: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            FormattingID: int,
            Type: str,
            Template: str,
            DestinationFileName: str,
            PublishFormat: str,
            PrinterName: str,
            OpenPublishedFile: bool,
            PostProcessID: int,
            AuditTrailReport: bool,
            PreferredPageSize: str,
            PreferredCulture: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemoveFormattingRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow,
        ) -> None: ...
        def Clone(self) -> System.Data.DataTable: ...
        def FindByReportIDFormattingID(
            self, ReportID: int, FormattingID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow
        ): ...
        def NewFormattingRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow
        ): ...

        FormattingRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRowChangeEventHandler
        )  # Event
        FormattingRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRowChangeEventHandler
        )  # Event
        FormattingRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRowChangeEventHandler
        )  # Event
        FormattingRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRowChangeEventHandler
        )  # Event

    class FormattingRow(System.Data.DataRow):  # Class
        AuditTrailReport: bool
        DestinationFileName: str
        FormattingID: int
        OpenPublishedFile: bool
        PostProcessID: int
        PreferredCulture: str
        PreferredPageSize: str
        PrinterName: str
        PublishFormat: str
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        Template: str
        Type: str

        def IsDestinationFileNameNull(self) -> bool: ...
        def GetFilteringRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FilteringRow
        ]: ...
        def SetPostProcessIDNull(self) -> None: ...
        def SetTemplateNull(self) -> None: ...
        def SetPublishFormatNull(self) -> None: ...
        def SetPrinterNameNull(self) -> None: ...
        def IsPostProcessIDNull(self) -> bool: ...
        def IsAuditTrailReportNull(self) -> bool: ...
        def IsPreferredCultureNull(self) -> bool: ...
        def IsOpenPublishedFileNull(self) -> bool: ...
        def SetTypeNull(self) -> None: ...
        def IsPreferredPageSizeNull(self) -> bool: ...
        def SetPreferredPageSizeNull(self) -> None: ...
        def SetAuditTrailReportNull(self) -> None: ...
        def SetPreferredCultureNull(self) -> None: ...
        def SetDestinationFileNameNull(self) -> None: ...
        def IsTypeNull(self) -> bool: ...
        def IsTemplateNull(self) -> bool: ...
        def IsPrinterNameNull(self) -> bool: ...
        def IsPublishFormatNull(self) -> bool: ...
        def SetOpenPublishedFileNull(self) -> None: ...

    class FormattingRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow
        )  # readonly

    class FormattingRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRowChangeEvent,
        ) -> None: ...

    class GlobalsDataTable(
        System.ComponentModel.ISupportInitialize,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRow
        ],
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AppVersionColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRow
        ): ...
        LastUpdateDateTimeColumn: System.Data.DataColumn  # readonly
        SchemaVersionColumn: System.Data.DataColumn  # readonly
        UserNameColumn: System.Data.DataColumn  # readonly

        def RemoveGlobalsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddGlobalsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRow,
        ) -> None: ...
        @overload
        def AddGlobalsRow(
            self,
            SchemaVersion: int,
            AppVersion: str,
            UserName: str,
            LastUpdateDateTime: System.DateTime,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRow
        ): ...
        def NewGlobalsRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...

        GlobalsRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRowChangeEventHandler
        )  # Event
        GlobalsRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRowChangeEventHandler
        )  # Event
        GlobalsRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRowChangeEventHandler
        )  # Event
        GlobalsRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRowChangeEventHandler
        )  # Event

    class GlobalsRow(System.Data.DataRow):  # Class
        AppVersion: str
        LastUpdateDateTime: System.DateTime
        SchemaVersion: int
        UserName: str

        def IsAppVersionNull(self) -> bool: ...
        def SetAppVersionNull(self) -> None: ...
        def IsLastUpdateDateTimeNull(self) -> bool: ...
        def SetSchemaVersionNull(self) -> None: ...
        def SetUserNameNull(self) -> None: ...
        def IsSchemaVersionNull(self) -> bool: ...
        def IsUserNameNull(self) -> bool: ...
        def SetLastUpdateDateTimeNull(self) -> None: ...

    class GlobalsRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRow
        )  # readonly

    class GlobalsRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GlobalsRowChangeEvent,
        ) -> None: ...

    class GraphicsRangeDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow
        ],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        Count: int  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow
        ): ...
        ReportIDColumn: System.Data.DataColumn  # readonly
        SamplesMaxXColumn: System.Data.DataColumn  # readonly
        SamplesMaxYColumn: System.Data.DataColumn  # readonly
        SamplesMinXColumn: System.Data.DataColumn  # readonly
        SamplesMinYColumn: System.Data.DataColumn  # readonly

        @overload
        def AddGraphicsRangeRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow,
        ) -> None: ...
        @overload
        def AddGraphicsRangeRow(
            self,
            parentReportRowByFK_Report_FixedRangeGraphics: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            SamplesMinY: float,
            SamplesMaxY: float,
            SamplesMinX: float,
            SamplesMaxX: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByReportID(
            self, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow
        ): ...
        def RemoveGraphicsRangeRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow,
        ) -> None: ...
        def NewGraphicsRangeRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...

        GraphicsRangeRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRowChangeEventHandler
        )  # Event
        GraphicsRangeRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRowChangeEventHandler
        )  # Event
        GraphicsRangeRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRowChangeEventHandler
        )  # Event
        GraphicsRangeRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRowChangeEventHandler
        )  # Event

    class GraphicsRangeRow(System.Data.DataRow):  # Class
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        SamplesMaxX: float
        SamplesMaxY: float
        SamplesMinX: float
        SamplesMinY: float

        def IsSamplesMinYNull(self) -> bool: ...
        def IsSamplesMinXNull(self) -> bool: ...
        def SetSamplesMaxXNull(self) -> None: ...
        def GetCompoundGraphicsRangeRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.CompoundGraphicsRangeRow
        ]: ...
        def SetSamplesMinXNull(self) -> None: ...
        def SetSamplesMaxYNull(self) -> None: ...
        def IsSamplesMaxYNull(self) -> bool: ...
        def IsSamplesMaxXNull(self) -> bool: ...
        def SetSamplesMinYNull(self) -> None: ...

    class GraphicsRangeRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow
        )  # readonly

    class GraphicsRangeRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRowChangeEvent,
        ) -> None: ...

    class PeakChromatogramGraphicsDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AlternatePeakFillColorColumn: System.Data.DataColumn  # readonly
        AutoScaleTypeColumn: System.Data.DataColumn  # readonly
        BackColorColumn: System.Data.DataColumn  # readonly
        ChromatogramTitleElementsColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FillPeaksColumn: System.Data.DataColumn  # readonly
        FillPeaksTransparencyColumn: System.Data.DataColumn  # readonly
        FontSizeColumn: System.Data.DataColumn  # readonly
        ForeColorColumn: System.Data.DataColumn  # readonly
        GridLinesColorColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow
        ): ...
        NoiseRegionsColorColumn: System.Data.DataColumn  # readonly
        NormalizeColumn: System.Data.DataColumn  # readonly
        PeakLabelTypesColumn: System.Data.DataColumn  # readonly
        PrimaryPeakAcceptedFillColorColumn: System.Data.DataColumn  # readonly
        PrimaryPeakInspectFillColorColumn: System.Data.DataColumn  # readonly
        PrimaryPeakManualIntegratedFillColorColumn: System.Data.DataColumn  # readonly
        PrimaryPeakRejectedFillColorColumn: System.Data.DataColumn  # readonly
        PurityColorsColumn: System.Data.DataColumn  # readonly
        ReferenceRetentionTimeColorColumn: System.Data.DataColumn  # readonly
        ReferenceRetentionTimeDashStyleColumn: System.Data.DataColumn  # readonly
        ReferenceWindowColorColumn: System.Data.DataColumn  # readonly
        ReferenceWindowDashStyleColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        ShowBaseRegionsColumn: System.Data.DataColumn  # readonly
        ShowBaselinesColumn: System.Data.DataColumn  # readonly
        ShowDefaultChromatogramTitleColumn: System.Data.DataColumn  # readonly
        ShowOriginalBaselinesColumn: System.Data.DataColumn  # readonly
        ShowPeakLabelNamesColumn: System.Data.DataColumn  # readonly
        ShowPeakLabelUnitsColumn: System.Data.DataColumn  # readonly
        ShowPurityColumn: System.Data.DataColumn  # readonly
        ShowReferenceRetentionTimeColumn: System.Data.DataColumn  # readonly
        ShowReferenceWindowColumn: System.Data.DataColumn  # readonly
        TimeSegmentBorderColorColumn: System.Data.DataColumn  # readonly
        WrapTitleColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemovePeakChromatogramGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow,
        ) -> None: ...
        def FindByReportID(
            self, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow
        ): ...
        @overload
        def AddPeakChromatogramGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow,
        ) -> None: ...
        @overload
        def AddPeakChromatogramGraphicsRow(
            self,
            parentReportRowByFK_Report_PeakChromatogramGraphics: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            AutoScaleType: str,
            BackColor: str,
            ForeColor: str,
            GridLinesColor: str,
            FontSize: float,
            ShowDefaultChromatogramTitle: bool,
            ChromatogramTitleElements: str,
            ShowBaselines: bool,
            ShowBaseRegions: bool,
            Normalize: bool,
            FillPeaks: bool,
            FillPeaksTransparency: int,
            PrimaryPeakAcceptedFillColor: str,
            PrimaryPeakInspectFillColor: str,
            PrimaryPeakRejectedFillColor: str,
            PrimaryPeakManualIntegratedFillColor: str,
            AlternatePeakFillColor: str,
            PeakLabelTypes: str,
            ShowPeakLabelNames: bool,
            ShowPeakLabelUnits: bool,
            ShowReferenceRetentionTime: bool,
            ReferenceRetentionTimeColor: str,
            ReferenceRetentionTimeDashStyle: str,
            ShowReferenceWindow: bool,
            ReferenceWindowColor: str,
            ReferenceWindowDashStyle: str,
            TimeSegmentBorderColor: str,
            ShowPurity: bool,
            PurityColors: str,
            ShowOriginalBaselines: bool,
            WrapTitle: bool,
            NoiseRegionsColor: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow
        ): ...
        def NewPeakChromatogramGraphicsRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...

        PeakChromatogramGraphicsRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRowChangeEventHandler
        )  # Event
        PeakChromatogramGraphicsRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRowChangeEventHandler
        )  # Event
        PeakChromatogramGraphicsRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRowChangeEventHandler
        )  # Event
        PeakChromatogramGraphicsRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRowChangeEventHandler
        )  # Event

    class PeakChromatogramGraphicsRow(System.Data.DataRow):  # Class
        AlternatePeakFillColor: str
        AutoScaleType: str
        BackColor: str
        ChromatogramTitleElements: str
        FillPeaks: bool
        FillPeaksTransparency: int
        FontSize: float
        ForeColor: str
        GridLinesColor: str
        NoiseRegionsColor: str
        Normalize: bool
        PeakLabelTypes: str
        PrimaryPeakAcceptedFillColor: str
        PrimaryPeakInspectFillColor: str
        PrimaryPeakManualIntegratedFillColor: str
        PrimaryPeakRejectedFillColor: str
        PurityColors: str
        ReferenceRetentionTimeColor: str
        ReferenceRetentionTimeDashStyle: str
        ReferenceWindowColor: str
        ReferenceWindowDashStyle: str
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        ShowBaseRegions: bool
        ShowBaselines: bool
        ShowDefaultChromatogramTitle: bool
        ShowOriginalBaselines: bool
        ShowPeakLabelNames: bool
        ShowPeakLabelUnits: bool
        ShowPurity: bool
        ShowReferenceRetentionTime: bool
        ShowReferenceWindow: bool
        TimeSegmentBorderColor: str
        WrapTitle: bool

        def IsForeColorNull(self) -> bool: ...
        def SetShowBaseRegionsNull(self) -> None: ...
        def IsFontSizeNull(self) -> bool: ...
        def IsPrimaryPeakInspectFillColorNull(self) -> bool: ...
        def SetFontSizeNull(self) -> None: ...
        def SetPurityColorsNull(self) -> None: ...
        def IsShowReferenceRetentionTimeNull(self) -> bool: ...
        def SetAlternatePeakFillColorNull(self) -> None: ...
        def SetNormalizeNull(self) -> None: ...
        def SetWrapTitleNull(self) -> None: ...
        def IsShowPurityNull(self) -> bool: ...
        def IsReferenceRetentionTimeColorNull(self) -> bool: ...
        def SetReferenceRetentionTimeColorNull(self) -> None: ...
        def IsPrimaryPeakAcceptedFillColorNull(self) -> bool: ...
        def IsWrapTitleNull(self) -> bool: ...
        def SetShowPeakLabelNamesNull(self) -> None: ...
        def IsPrimaryPeakRejectedFillColorNull(self) -> bool: ...
        def IsShowPeakLabelUnitsNull(self) -> bool: ...
        def IsAlternatePeakFillColorNull(self) -> bool: ...
        def SetBackColorNull(self) -> None: ...
        def SetChromatogramTitleElementsNull(self) -> None: ...
        def IsShowPeakLabelNamesNull(self) -> bool: ...
        def IsNoiseRegionsColorNull(self) -> bool: ...
        def SetTimeSegmentBorderColorNull(self) -> None: ...
        def IsShowOriginalBaselinesNull(self) -> bool: ...
        def IsAutoScaleTypeNull(self) -> bool: ...
        def IsFillPeaksTransparencyNull(self) -> bool: ...
        def IsPurityColorsNull(self) -> bool: ...
        def SetReferenceWindowColorNull(self) -> None: ...
        def SetShowDefaultChromatogramTitleNull(self) -> None: ...
        def SetFillPeaksNull(self) -> None: ...
        def IsBackColorNull(self) -> bool: ...
        def IsReferenceWindowColorNull(self) -> bool: ...
        def SetReferenceRetentionTimeDashStyleNull(self) -> None: ...
        def IsFillPeaksNull(self) -> bool: ...
        def IsShowBaseRegionsNull(self) -> bool: ...
        def SetShowPeakLabelUnitsNull(self) -> None: ...
        def SetShowPurityNull(self) -> None: ...
        def IsReferenceWindowDashStyleNull(self) -> bool: ...
        def IsChromatogramTitleElementsNull(self) -> bool: ...
        def SetAutoScaleTypeNull(self) -> None: ...
        def IsPeakLabelTypesNull(self) -> bool: ...
        def SetPrimaryPeakAcceptedFillColorNull(self) -> None: ...
        def SetPrimaryPeakManualIntegratedFillColorNull(self) -> None: ...
        def IsGridLinesColorNull(self) -> bool: ...
        def SetReferenceWindowDashStyleNull(self) -> None: ...
        def SetPeakLabelTypesNull(self) -> None: ...
        def SetFillPeaksTransparencyNull(self) -> None: ...
        def IsShowBaselinesNull(self) -> bool: ...
        def IsShowReferenceWindowNull(self) -> bool: ...
        def IsTimeSegmentBorderColorNull(self) -> bool: ...
        def IsPrimaryPeakManualIntegratedFillColorNull(self) -> bool: ...
        def SetPrimaryPeakInspectFillColorNull(self) -> None: ...
        def SetPrimaryPeakRejectedFillColorNull(self) -> None: ...
        def SetShowBaselinesNull(self) -> None: ...
        def SetShowOriginalBaselinesNull(self) -> None: ...
        def SetShowReferenceRetentionTimeNull(self) -> None: ...
        def SetNoiseRegionsColorNull(self) -> None: ...
        def IsReferenceRetentionTimeDashStyleNull(self) -> bool: ...
        def IsShowDefaultChromatogramTitleNull(self) -> bool: ...
        def SetForeColorNull(self) -> None: ...
        def SetGridLinesColorNull(self) -> None: ...
        def IsNormalizeNull(self) -> bool: ...
        def SetShowReferenceWindowNull(self) -> None: ...

    class PeakChromatogramGraphicsRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow
        )  # readonly

    class PeakChromatogramGraphicsRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRowChangeEvent,
        ) -> None: ...

    class PeakQualifiersGraphicsDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow
        ],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AutoScaleTypeColumn: System.Data.DataColumn  # readonly
        BackColorColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FillAllQualifierPeaksColumn: System.Data.DataColumn  # readonly
        FillOutofLimitQualifierPeaksColumn: System.Data.DataColumn  # readonly
        FillTargetPeakInQualifiersColumn: System.Data.DataColumn  # readonly
        FontSizeColumn: System.Data.DataColumn  # readonly
        ForeColorColumn: System.Data.DataColumn  # readonly
        GridLinesColorColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow
        ): ...
        NormalizeColumn: System.Data.DataColumn  # readonly
        OutofLimitQualifiersTransparencyColumn: System.Data.DataColumn  # readonly
        QualifierColorsColumn: System.Data.DataColumn  # readonly
        QualifierInfoLabelTypeColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        ShowAnnotationsColumn: System.Data.DataColumn  # readonly
        ShowUncertaintyBandColumn: System.Data.DataColumn  # readonly
        TimeSegmentBorderColorColumn: System.Data.DataColumn  # readonly
        UncertaintyBandDashStyleColumn: System.Data.DataColumn  # readonly
        WrapTitleColumn: System.Data.DataColumn  # readonly

        def RemovePeakQualifiersGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByReportID(
            self, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def NewPeakQualifiersGraphicsRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow
        ): ...
        @overload
        def AddPeakQualifiersGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow,
        ) -> None: ...
        @overload
        def AddPeakQualifiersGraphicsRow(
            self,
            parentReportRowByFK_Report_PeakQualifiersGraphics: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            AutoScaleType: str,
            BackColor: str,
            ForeColor: str,
            GridLinesColor: str,
            FontSize: float,
            Normalize: bool,
            QualifierColors: str,
            TimeSegmentBorderColor: str,
            ShowAnnotations: bool,
            ShowUncertaintyBand: bool,
            UncertaintyBandDashStyle: str,
            FillOutofLimitQualifierPeaks: bool,
            FillAllQualifierPeaks: bool,
            FillTargetPeakInQualifiers: bool,
            OutofLimitQualifiersTransparency: int,
            QualifierInfoLabelType: str,
            WrapTitle: bool,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow
        ): ...

        PeakQualifiersGraphicsRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRowChangeEventHandler
        )  # Event
        PeakQualifiersGraphicsRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRowChangeEventHandler
        )  # Event
        PeakQualifiersGraphicsRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRowChangeEventHandler
        )  # Event
        PeakQualifiersGraphicsRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRowChangeEventHandler
        )  # Event

    class PeakQualifiersGraphicsRow(System.Data.DataRow):  # Class
        AutoScaleType: str
        BackColor: str
        FillAllQualifierPeaks: bool
        FillOutofLimitQualifierPeaks: bool
        FillTargetPeakInQualifiers: bool
        FontSize: float
        ForeColor: str
        GridLinesColor: str
        Normalize: bool
        OutofLimitQualifiersTransparency: int
        QualifierColors: str
        QualifierInfoLabelType: str
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        ShowAnnotations: bool
        ShowUncertaintyBand: bool
        TimeSegmentBorderColor: str
        UncertaintyBandDashStyle: str
        WrapTitle: bool

        def IsForeColorNull(self) -> bool: ...
        def IsUncertaintyBandDashStyleNull(self) -> bool: ...
        def IsFontSizeNull(self) -> bool: ...
        def SetFontSizeNull(self) -> None: ...
        def SetQualifierColorsNull(self) -> None: ...
        def IsFillOutofLimitQualifierPeaksNull(self) -> bool: ...
        def SetNormalizeNull(self) -> None: ...
        def SetQualifierInfoLabelTypeNull(self) -> None: ...
        def IsFillAllQualifierPeaksNull(self) -> bool: ...
        def SetWrapTitleNull(self) -> None: ...
        def IsWrapTitleNull(self) -> bool: ...
        def SetBackColorNull(self) -> None: ...
        def SetOutofLimitQualifiersTransparencyNull(self) -> None: ...
        def SetTimeSegmentBorderColorNull(self) -> None: ...
        def IsAutoScaleTypeNull(self) -> bool: ...
        def IsOutofLimitQualifiersTransparencyNull(self) -> bool: ...
        def SetUncertaintyBandDashStyleNull(self) -> None: ...
        def SetShowUncertaintyBandNull(self) -> None: ...
        def IsBackColorNull(self) -> bool: ...
        def IsQualifierInfoLabelTypeNull(self) -> bool: ...
        def SetAutoScaleTypeNull(self) -> None: ...
        def SetShowAnnotationsNull(self) -> None: ...
        def IsGridLinesColorNull(self) -> bool: ...
        def IsShowUncertaintyBandNull(self) -> bool: ...
        def IsShowAnnotationsNull(self) -> bool: ...
        def IsFillTargetPeakInQualifiersNull(self) -> bool: ...
        def IsTimeSegmentBorderColorNull(self) -> bool: ...
        def SetFillAllQualifierPeaksNull(self) -> None: ...
        def IsQualifierColorsNull(self) -> bool: ...
        def SetFillOutofLimitQualifierPeaksNull(self) -> None: ...
        def SetFillTargetPeakInQualifiersNull(self) -> None: ...
        def SetForeColorNull(self) -> None: ...
        def SetGridLinesColorNull(self) -> None: ...
        def IsNormalizeNull(self) -> bool: ...

    class PeakQualifiersGraphicsRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow
        )  # readonly

    class PeakQualifiersGraphicsRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRowChangeEvent,
        ) -> None: ...

    class PeakSpectrumGraphicsDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AutoScaleTypeColumn: System.Data.DataColumn  # readonly
        BackColorColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FontSizeColumn: System.Data.DataColumn  # readonly
        ForeColorColumn: System.Data.DataColumn  # readonly
        GridLinesColorColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow
        ): ...
        OverrideSpectrumColumn: System.Data.DataColumn  # readonly
        PrecursorIonColorColumn: System.Data.DataColumn  # readonly
        PrecursorIonFillColumn: System.Data.DataColumn  # readonly
        PrecursorIonSizeColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        ShowMassIndicatorsColumn: System.Data.DataColumn  # readonly
        ShowMatchScoresColumn: System.Data.DataColumn  # readonly
        ShowReferenceLibrarySourceColumn: System.Data.DataColumn  # readonly
        ShowReferencePatternSpectrumColumn: System.Data.DataColumn  # readonly
        ShowReferenceSpectrumColumn: System.Data.DataColumn  # readonly
        WrapTitleColumn: System.Data.DataColumn  # readonly

        def RemovePeakSpectrumGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddPeakSpectrumGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow,
        ) -> None: ...
        @overload
        def AddPeakSpectrumGraphicsRow(
            self,
            parentReportRowByFK_Report_PeakSpectrumGraphics: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            AutoScaleType: str,
            BackColor: str,
            ForeColor: str,
            GridLinesColor: str,
            FontSize: float,
            PrecursorIonColor: str,
            PrecursorIonSize: int,
            PrecursorIonFill: bool,
            ShowReferenceSpectrum: bool,
            ShowReferencePatternSpectrum: bool,
            ShowMatchScores: bool,
            ShowMassIndicators: bool,
            ShowReferenceLibrarySource: bool,
            OverrideSpectrum: bool,
            WrapTitle: bool,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow
        ): ...
        def FindByReportID(
            self, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def NewPeakSpectrumGraphicsRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow
        ): ...

        PeakSpectrumGraphicsRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRowChangeEventHandler
        )  # Event
        PeakSpectrumGraphicsRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRowChangeEventHandler
        )  # Event
        PeakSpectrumGraphicsRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRowChangeEventHandler
        )  # Event
        PeakSpectrumGraphicsRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRowChangeEventHandler
        )  # Event

    class PeakSpectrumGraphicsRow(System.Data.DataRow):  # Class
        AutoScaleType: str
        BackColor: str
        FontSize: float
        ForeColor: str
        GridLinesColor: str
        OverrideSpectrum: bool
        PrecursorIonColor: str
        PrecursorIonFill: bool
        PrecursorIonSize: int
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        ShowMassIndicators: bool
        ShowMatchScores: bool
        ShowReferenceLibrarySource: bool
        ShowReferencePatternSpectrum: bool
        ShowReferenceSpectrum: bool
        WrapTitle: bool

        def IsForeColorNull(self) -> bool: ...
        def IsFontSizeNull(self) -> bool: ...
        def SetFontSizeNull(self) -> None: ...
        def IsShowReferencePatternSpectrumNull(self) -> bool: ...
        def SetPrecursorIonSizeNull(self) -> None: ...
        def SetPrecursorIonColorNull(self) -> None: ...
        def SetWrapTitleNull(self) -> None: ...
        def IsShowMatchScoresNull(self) -> bool: ...
        def IsShowReferenceSpectrumNull(self) -> bool: ...
        def SetShowReferenceSpectrumNull(self) -> None: ...
        def IsWrapTitleNull(self) -> bool: ...
        def SetBackColorNull(self) -> None: ...
        def IsPrecursorIonSizeNull(self) -> bool: ...
        def IsPrecursorIonColorNull(self) -> bool: ...
        def IsAutoScaleTypeNull(self) -> bool: ...
        def IsOverrideSpectrumNull(self) -> bool: ...
        def IsBackColorNull(self) -> bool: ...
        def SetOverrideSpectrumNull(self) -> None: ...
        def SetAutoScaleTypeNull(self) -> None: ...
        def IsShowMassIndicatorsNull(self) -> bool: ...
        def IsGridLinesColorNull(self) -> bool: ...
        def SetShowMassIndicatorsNull(self) -> None: ...
        def IsPrecursorIonFillNull(self) -> bool: ...
        def SetShowReferenceLibrarySourceNull(self) -> None: ...
        def IsShowReferenceLibrarySourceNull(self) -> bool: ...
        def SetShowReferencePatternSpectrumNull(self) -> None: ...
        def SetShowMatchScoresNull(self) -> None: ...
        def SetForeColorNull(self) -> None: ...
        def SetPrecursorIonFillNull(self) -> None: ...
        def SetGridLinesColorNull(self) -> None: ...

    class PeakSpectrumGraphicsRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow
        )  # readonly

    class PeakSpectrumGraphicsRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRowChangeEvent,
        ) -> None: ...

    class PrePostProcessDataTable(
        System.IServiceProvider,
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow
        ],
        System.IDisposable,
    ):  # Class
        def __init__(self) -> None: ...

        CommandColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow
        ): ...
        NameColumn: System.Data.DataColumn  # readonly
        ParametersColumn: System.Data.DataColumn  # readonly
        PrePostProcessIDColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        TypeColumn: System.Data.DataColumn  # readonly
        WaitForExitColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemovePrePostProcessRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow,
        ) -> None: ...
        def FindByReportIDPrePostProcessID(
            self, ReportID: int, PrePostProcessID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow
        ): ...
        def NewPrePostProcessRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        @overload
        def AddPrePostProcessRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow,
        ) -> None: ...
        @overload
        def AddPrePostProcessRow(
            self,
            parentReportRowByFK_Report_PrePostProcess: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            PrePostProcessID: int,
            Name: str,
            Type: str,
            Command: str,
            Parameters: str,
            WaitForExit: bool,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow
        ): ...

        PrePostProcessRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRowChangeEventHandler
        )  # Event
        PrePostProcessRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRowChangeEventHandler
        )  # Event
        PrePostProcessRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRowChangeEventHandler
        )  # Event
        PrePostProcessRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRowChangeEventHandler
        )  # Event

    class PrePostProcessRow(System.Data.DataRow):  # Class
        Command: str
        Name: str
        Parameters: str
        PrePostProcessID: int
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        Type: str
        WaitForExit: bool

        def IsCommandNull(self) -> bool: ...
        def SetCommandNull(self) -> None: ...
        def SetWaitForExitNull(self) -> None: ...
        def IsWaitForExitNull(self) -> bool: ...
        def IsNameNull(self) -> bool: ...
        def IsTypeNull(self) -> bool: ...
        def SetTypeNull(self) -> None: ...
        def IsParametersNull(self) -> bool: ...
        def SetNameNull(self) -> None: ...
        def SetParametersNull(self) -> None: ...

    class PrePostProcessRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow
        )  # readonly

    class PrePostProcessRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRowChangeEvent,
        ) -> None: ...

    class ReportDataTable(
        System.ComponentModel.IListSource,
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        ],
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        ApplicationColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DeleteGraphicsFileColumn: System.Data.DataColumn  # readonly
        GenerateGraphicsFilesColumn: System.Data.DataColumn  # readonly
        GenerateResultsColumn: System.Data.DataColumn  # readonly
        InstrumentTypeColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        ): ...
        PostProcessIDColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        UploadResultsFileColumn: System.Data.DataColumn  # readonly

        def NewReportRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddReportRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
        ) -> None: ...
        @overload
        def AddReportRow(
            self,
            ReportID: int,
            Application: str,
            InstrumentType: str,
            GenerateResults: bool,
            UploadResultsFile: bool,
            GenerateGraphicsFiles: bool,
            DeleteGraphicsFile: bool,
            PostProcessID: int,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        ): ...
        def FindByReportID(
            self, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveReportRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
        ) -> None: ...

        ReportRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRowChangeEventHandler
        )  # Event
        ReportRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRowChangeEventHandler
        )  # Event
        ReportRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRowChangeEventHandler
        )  # Event
        ReportRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRowChangeEventHandler
        )  # Event

    class ReportRow(System.Data.DataRow):  # Class
        Application: str
        DeleteGraphicsFile: bool
        GenerateGraphicsFiles: bool
        GenerateResults: bool
        InstrumentType: str
        PostProcessID: int
        ReportID: int
        UploadResultsFile: bool

        def GetUnknownsIonPeaksGraphicsRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow
        ]: ...
        def SetApplicationNull(self) -> None: ...
        def GetPrePostProcessRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PrePostProcessRow
        ]: ...
        def SetGenerateGraphicsFilesNull(self) -> None: ...
        def SetPostProcessIDNull(self) -> None: ...
        def IsPostProcessIDNull(self) -> bool: ...
        def GetSampleChromatogramGraphicsRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow
        ]: ...
        def IsUploadResultsFileNull(self) -> bool: ...
        def GetPeakQualifiersGraphicsRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakQualifiersGraphicsRow
        ]: ...
        def SetGenerateResultsNull(self) -> None: ...
        def GetFormattingRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.FormattingRow
        ]: ...
        def GetUnknownsSpectrumGraphicsRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow
        ]: ...
        def IsInstrumentTypeNull(self) -> bool: ...
        def IsDeleteGraphicsFileNull(self) -> bool: ...
        def GetUnknownsSampleChromatogramGraphicsRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow
        ]: ...
        def SetInstrumentTypeNull(self) -> None: ...
        def SetDeleteGraphicsFileNull(self) -> None: ...
        def GetGraphicsRangeRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.GraphicsRangeRow
        ]: ...
        def IsGenerateGraphicsFilesNull(self) -> bool: ...
        def IsGenerateResultsNull(self) -> bool: ...
        def SetUploadResultsFileNull(self) -> None: ...
        def IsApplicationNull(self) -> bool: ...
        def GetPeakSpectrumGraphicsRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakSpectrumGraphicsRow
        ]: ...
        def GetPeakChromatogramGraphicsRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.PeakChromatogramGraphicsRow
        ]: ...
        def GetTargetCompoundCalibrationRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow
        ]: ...

    class ReportRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )  # readonly

    class ReportRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRowChangeEvent,
        ) -> None: ...

    class SampleChromatogramGraphicsDataTable(
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow
        ],
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AutoScaleAfterColumn: System.Data.DataColumn  # readonly
        BackColorColumn: System.Data.DataColumn  # readonly
        CompoundColorsColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FontSizeColumn: System.Data.DataColumn  # readonly
        ForeColorColumn: System.Data.DataColumn  # readonly
        GridLinesColorColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow
        ): ...
        NormalizeColumn: System.Data.DataColumn  # readonly
        OverlayIstdsColumn: System.Data.DataColumn  # readonly
        OverlaySignalsColumn: System.Data.DataColumn  # readonly
        OverlayTargetCompoundsColumn: System.Data.DataColumn  # readonly
        PeakLabelTypesColumn: System.Data.DataColumn  # readonly
        PeakLabelsAllowOverlapColumn: System.Data.DataColumn  # readonly
        PeakLabelsOnTICColumn: System.Data.DataColumn  # readonly
        PeakLabelsVerticalColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        ShowPeakLabelCaptionColumn: System.Data.DataColumn  # readonly
        ShowPeakLabelUnitsColumn: System.Data.DataColumn  # readonly
        ShowSignalLabelsColumn: System.Data.DataColumn  # readonly
        SignalColorsColumn: System.Data.DataColumn  # readonly
        TICColorColumn: System.Data.DataColumn  # readonly
        TimeSegmentBorderColorColumn: System.Data.DataColumn  # readonly

        @overload
        def AddSampleChromatogramGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow,
        ) -> None: ...
        @overload
        def AddSampleChromatogramGraphicsRow(
            self,
            parentReportRowByFK_Report_SampleChromatogramGraphics: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            BackColor: str,
            ForeColor: str,
            GridLinesColor: str,
            FontSize: float,
            TICColor: str,
            OverlayTargetCompounds: bool,
            OverlayIstds: bool,
            CompoundColors: str,
            OverlaySignals: bool,
            ShowSignalLabels: bool,
            SignalColors: str,
            Normalize: bool,
            AutoScaleAfter: float,
            TimeSegmentBorderColor: str,
            PeakLabelsVertical: bool,
            PeakLabelsAllowOverlap: bool,
            PeakLabelsOnTIC: bool,
            PeakLabelTypes: str,
            ShowPeakLabelCaption: bool,
            ShowPeakLabelUnits: bool,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByReportID(
            self, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveSampleChromatogramGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow,
        ) -> None: ...
        def NewSampleChromatogramGraphicsRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow
        ): ...

        SampleChromatogramGraphicsRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRowChangeEventHandler
        )  # Event
        SampleChromatogramGraphicsRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRowChangeEventHandler
        )  # Event
        SampleChromatogramGraphicsRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRowChangeEventHandler
        )  # Event
        SampleChromatogramGraphicsRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRowChangeEventHandler
        )  # Event

    class SampleChromatogramGraphicsRow(System.Data.DataRow):  # Class
        AutoScaleAfter: float
        BackColor: str
        CompoundColors: str
        FontSize: float
        ForeColor: str
        GridLinesColor: str
        Normalize: bool
        OverlayIstds: bool
        OverlaySignals: bool
        OverlayTargetCompounds: bool
        PeakLabelTypes: str
        PeakLabelsAllowOverlap: bool
        PeakLabelsOnTIC: bool
        PeakLabelsVertical: bool
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        ShowPeakLabelCaption: bool
        ShowPeakLabelUnits: bool
        ShowSignalLabels: bool
        SignalColors: str
        TICColor: str
        TimeSegmentBorderColor: str

        def IsForeColorNull(self) -> bool: ...
        def SetSignalColorsNull(self) -> None: ...
        def SetOverlayTargetCompoundsNull(self) -> None: ...
        def IsSignalColorsNull(self) -> bool: ...
        def IsFontSizeNull(self) -> bool: ...
        def IsPeakLabelsAllowOverlapNull(self) -> bool: ...
        def SetFontSizeNull(self) -> None: ...
        def SetPeakLabelsOnTICNull(self) -> None: ...
        def SetNormalizeNull(self) -> None: ...
        def IsPeakLabelsOnTICNull(self) -> bool: ...
        def SetShowPeakLabelCaptionNull(self) -> None: ...
        def IsCompoundColorsNull(self) -> bool: ...
        def IsPeakLabelsVerticalNull(self) -> bool: ...
        def SetOverlayIstdsNull(self) -> None: ...
        def IsShowPeakLabelUnitsNull(self) -> bool: ...
        def SetBackColorNull(self) -> None: ...
        def SetPeakLabelsVerticalNull(self) -> None: ...
        def SetTimeSegmentBorderColorNull(self) -> None: ...
        def SetPeakLabelsAllowOverlapNull(self) -> None: ...
        def IsOverlayIstdsNull(self) -> bool: ...
        def IsTICColorNull(self) -> bool: ...
        def IsOverlaySignalsNull(self) -> bool: ...
        def SetShowSignalLabelsNull(self) -> None: ...
        def IsBackColorNull(self) -> bool: ...
        def SetShowPeakLabelUnitsNull(self) -> None: ...
        def IsAutoScaleAfterNull(self) -> bool: ...
        def IsShowPeakLabelCaptionNull(self) -> bool: ...
        def SetOverlaySignalsNull(self) -> None: ...
        def IsPeakLabelTypesNull(self) -> bool: ...
        def IsGridLinesColorNull(self) -> bool: ...
        def SetPeakLabelTypesNull(self) -> None: ...
        def IsTimeSegmentBorderColorNull(self) -> bool: ...
        def SetAutoScaleAfterNull(self) -> None: ...
        def SetCompoundColorsNull(self) -> None: ...
        def SetTICColorNull(self) -> None: ...
        def IsOverlayTargetCompoundsNull(self) -> bool: ...
        def IsShowSignalLabelsNull(self) -> bool: ...
        def SetForeColorNull(self) -> None: ...
        def SetGridLinesColorNull(self) -> None: ...
        def IsNormalizeNull(self) -> bool: ...

    class SampleChromatogramGraphicsRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRow
        )  # readonly

    class SampleChromatogramGraphicsRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.SampleChromatogramGraphicsRowChangeEvent,
        ) -> None: ...

    class TargetCompoundCalibrationDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AutoScaleToEnabledPointsColumn: System.Data.DataColumn  # readonly
        BackColorColumn: System.Data.DataColumn  # readonly
        CCFillColorColumn: System.Data.DataColumn  # readonly
        CCLineColorColumn: System.Data.DataColumn  # readonly
        CalibrationCurveColorColumn: System.Data.DataColumn  # readonly
        CalibrationPointColorColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FontSizeColumn: System.Data.DataColumn  # readonly
        ForeColorColumn: System.Data.DataColumn  # readonly
        GridLinesColorColumn: System.Data.DataColumn  # readonly
        IstdResponsesColorColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow
        ): ...
        LogScaleXColumn: System.Data.DataColumn  # readonly
        LogScaleYColumn: System.Data.DataColumn  # readonly
        PointSizeColumn: System.Data.DataColumn  # readonly
        QCFillColorColumn: System.Data.DataColumn  # readonly
        QCLineColorColumn: System.Data.DataColumn  # readonly
        RelativeConcentrationColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        ShowCCColumn: System.Data.DataColumn  # readonly
        ShowIstdResponsesColumn: System.Data.DataColumn  # readonly
        ShowQCColumn: System.Data.DataColumn  # readonly
        ShowStandardDeviationBarsColumn: System.Data.DataColumn  # readonly
        StandardDeviationBarsColorColumn: System.Data.DataColumn  # readonly

        def NewTargetCompoundCalibrationRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByReportID(
            self, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow
        ): ...
        @overload
        def AddTargetCompoundCalibrationRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow,
        ) -> None: ...
        @overload
        def AddTargetCompoundCalibrationRow(
            self,
            parentReportRowByFK_Report_TargetCompoundCalibration: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            BackColor: str,
            ForeColor: str,
            GridLinesColor: str,
            FontSize: float,
            PointSize: int,
            CalibrationCurveColor: str,
            CalibrationPointColor: str,
            AutoScaleToEnabledPoints: bool,
            ShowStandardDeviationBars: bool,
            StandardDeviationBarsColor: str,
            ShowIstdResponses: bool,
            IstdResponsesColor: str,
            ShowQC: bool,
            QCLineColor: str,
            QCFillColor: str,
            ShowCC: bool,
            CCLineColor: str,
            CCFillColor: str,
            LogScaleX: bool,
            LogScaleY: bool,
            RelativeConcentration: bool,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveTargetCompoundCalibrationRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow,
        ) -> None: ...

        TargetCompoundCalibrationRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRowChangeEventHandler
        )  # Event
        TargetCompoundCalibrationRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRowChangeEventHandler
        )  # Event
        TargetCompoundCalibrationRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRowChangeEventHandler
        )  # Event
        TargetCompoundCalibrationRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRowChangeEventHandler
        )  # Event

    class TargetCompoundCalibrationRow(System.Data.DataRow):  # Class
        AutoScaleToEnabledPoints: bool
        BackColor: str
        CCFillColor: str
        CCLineColor: str
        CalibrationCurveColor: str
        CalibrationPointColor: str
        FontSize: float
        ForeColor: str
        GridLinesColor: str
        IstdResponsesColor: str
        LogScaleX: bool
        LogScaleY: bool
        PointSize: int
        QCFillColor: str
        QCLineColor: str
        RelativeConcentration: bool
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        ShowCC: bool
        ShowIstdResponses: bool
        ShowQC: bool
        ShowStandardDeviationBars: bool
        StandardDeviationBarsColor: str

        def IsForeColorNull(self) -> bool: ...
        def SetShowQCNull(self) -> None: ...
        def IsShowCCNull(self) -> bool: ...
        def IsFontSizeNull(self) -> bool: ...
        def IsShowStandardDeviationBarsNull(self) -> bool: ...
        def SetFontSizeNull(self) -> None: ...
        def SetShowIstdResponsesNull(self) -> None: ...
        def SetShowStandardDeviationBarsNull(self) -> None: ...
        def IsCalibrationPointColorNull(self) -> bool: ...
        def IsCCLineColorNull(self) -> bool: ...
        def SetIstdResponsesColorNull(self) -> None: ...
        def SetCCFillColorNull(self) -> None: ...
        def IsLogScaleYNull(self) -> bool: ...
        def SetBackColorNull(self) -> None: ...
        def IsQCLineColorNull(self) -> bool: ...
        def SetPointSizeNull(self) -> None: ...
        def SetRelativeConcentrationNull(self) -> None: ...
        def SetAutoScaleToEnabledPointsNull(self) -> None: ...
        def SetLogScaleXNull(self) -> None: ...
        def IsRelativeConcentrationNull(self) -> bool: ...
        def IsCalibrationCurveColorNull(self) -> bool: ...
        def IsStandardDeviationBarsColorNull(self) -> bool: ...
        def IsBackColorNull(self) -> bool: ...
        def SetShowCCNull(self) -> None: ...
        def SetLogScaleYNull(self) -> None: ...
        def IsQCFillColorNull(self) -> bool: ...
        def IsCCFillColorNull(self) -> bool: ...
        def IsAutoScaleToEnabledPointsNull(self) -> bool: ...
        def SetQCFillColorNull(self) -> None: ...
        def SetCCLineColorNull(self) -> None: ...
        def IsPointSizeNull(self) -> bool: ...
        def IsShowIstdResponsesNull(self) -> bool: ...
        def IsGridLinesColorNull(self) -> bool: ...
        def IsIstdResponsesColorNull(self) -> bool: ...
        def SetCalibrationCurveColorNull(self) -> None: ...
        def SetCalibrationPointColorNull(self) -> None: ...
        def IsLogScaleXNull(self) -> bool: ...
        def SetQCLineColorNull(self) -> None: ...
        def SetForeColorNull(self) -> None: ...
        def SetStandardDeviationBarsColorNull(self) -> None: ...
        def SetGridLinesColorNull(self) -> None: ...
        def IsShowQCNull(self) -> bool: ...

    class TargetCompoundCalibrationRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRow
        )  # readonly

    class TargetCompoundCalibrationRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.TargetCompoundCalibrationRowChangeEvent,
        ) -> None: ...

    class UnknownsIonPeaksGraphicsDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow
        ],
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        BackColorColumn: System.Data.DataColumn  # readonly
        ComponentColorColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FontFamilyColumn: System.Data.DataColumn  # readonly
        FontSizeColumn: System.Data.DataColumn  # readonly
        ForeColorColumn: System.Data.DataColumn  # readonly
        GridLinesColorColumn: System.Data.DataColumn  # readonly
        IonPeakColorsColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow
        ): ...
        ReportIDColumn: System.Data.DataColumn  # readonly
        ShowIonPeaksColumn: System.Data.DataColumn  # readonly
        ShowLabelsColumn: System.Data.DataColumn  # readonly
        TICColorColumn: System.Data.DataColumn  # readonly

        def RemoveUnknownsIonPeaksGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByReportID(
            self, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow
        ): ...
        @overload
        def AddUnknownsIonPeaksGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow,
        ) -> None: ...
        @overload
        def AddUnknownsIonPeaksGraphicsRow(
            self,
            parentReportRowByFK_Report_UnknownsIonPeaksGraphics: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            BackColor: str,
            ForeColor: str,
            GridLinesColor: str,
            FontFamily: str,
            FontSize: float,
            TICColor: str,
            ComponentColor: str,
            ShowIonPeaks: bool,
            IonPeakColors: str,
            ShowLabels: bool,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def NewUnknownsIonPeaksGraphicsRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow
        ): ...

        UnknownsIonPeaksGraphicsRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRowChangeEventHandler
        )  # Event
        UnknownsIonPeaksGraphicsRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRowChangeEventHandler
        )  # Event
        UnknownsIonPeaksGraphicsRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRowChangeEventHandler
        )  # Event
        UnknownsIonPeaksGraphicsRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRowChangeEventHandler
        )  # Event

    class UnknownsIonPeaksGraphicsRow(System.Data.DataRow):  # Class
        BackColor: str
        ComponentColor: str
        FontFamily: str
        FontSize: float
        ForeColor: str
        GridLinesColor: str
        IonPeakColors: str
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        ShowIonPeaks: bool
        ShowLabels: bool
        TICColor: str

        def SetFontSizeNull(self) -> None: ...
        def SetComponentColorNull(self) -> None: ...
        def SetShowIonPeaksNull(self) -> None: ...
        def IsShowLabelsNull(self) -> bool: ...
        def SetForeColorNull(self) -> None: ...
        def IsForeColorNull(self) -> bool: ...
        def IsComponentColorNull(self) -> bool: ...
        def IsFontFamilyNull(self) -> bool: ...
        def IsFontSizeNull(self) -> bool: ...
        def SetIonPeakColorsNull(self) -> None: ...
        def SetGridLinesColorNull(self) -> None: ...
        def SetBackColorNull(self) -> None: ...
        def IsIonPeakColorsNull(self) -> bool: ...
        def IsShowIonPeaksNull(self) -> bool: ...
        def SetShowLabelsNull(self) -> None: ...
        def SetTICColorNull(self) -> None: ...
        def SetFontFamilyNull(self) -> None: ...
        def IsBackColorNull(self) -> bool: ...
        def IsGridLinesColorNull(self) -> bool: ...
        def IsTICColorNull(self) -> bool: ...

    class UnknownsIonPeaksGraphicsRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRow
        )  # readonly

    class UnknownsIonPeaksGraphicsRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsIonPeaksGraphicsRowChangeEvent,
        ) -> None: ...

    class UnknownsSampleChromatogramGraphicsDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        BackColorColumn: System.Data.DataColumn  # readonly
        ComponentColorColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        EICColorsColumn: System.Data.DataColumn  # readonly
        FontFamilyColumn: System.Data.DataColumn  # readonly
        FontSizeColumn: System.Data.DataColumn  # readonly
        ForeColorColumn: System.Data.DataColumn  # readonly
        GridLinesColorColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow
        ): ...
        PeakLabelTypesColumn: System.Data.DataColumn  # readonly
        PeakLabelsAllowOverlapColumn: System.Data.DataColumn  # readonly
        PeakLabelsVerticalColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        ScaleToHighestPeakAfterColumn: System.Data.DataColumn  # readonly
        ShowEICsColumn: System.Data.DataColumn  # readonly
        ShowLegendColumn: System.Data.DataColumn  # readonly
        ShowPeakLabelCaptionColumn: System.Data.DataColumn  # readonly
        ShowPeakLabelUnitsColumn: System.Data.DataColumn  # readonly
        ShowPeakLabelsColumn: System.Data.DataColumn  # readonly
        TICColorColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemoveUnknownsSampleChromatogramGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow,
        ) -> None: ...
        def NewUnknownsSampleChromatogramGraphicsRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow
        ): ...
        def FindByReportID(
            self, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow
        ): ...
        @overload
        def AddUnknownsSampleChromatogramGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow,
        ) -> None: ...
        @overload
        def AddUnknownsSampleChromatogramGraphicsRow(
            self,
            parentReportRowByFK_Report_UnknownsSampleChromatogramGraphics: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            BackColor: str,
            ForeColor: str,
            GridLinesColor: str,
            FontFamily: str,
            FontSize: float,
            TICColor: str,
            ComponentColor: str,
            ShowEICs: bool,
            EICColors: str,
            ShowLegend: bool,
            ScaleToHighestPeakAfter: float,
            ShowPeakLabels: bool,
            PeakLabelsVertical: bool,
            PeakLabelsAllowOverlap: bool,
            PeakLabelTypes: str,
            ShowPeakLabelCaption: bool,
            ShowPeakLabelUnits: bool,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...

        UnknownsSampleChromatogramGraphicsRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRowChangeEventHandler
        )  # Event
        UnknownsSampleChromatogramGraphicsRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRowChangeEventHandler
        )  # Event
        UnknownsSampleChromatogramGraphicsRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRowChangeEventHandler
        )  # Event
        UnknownsSampleChromatogramGraphicsRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRowChangeEventHandler
        )  # Event

    class UnknownsSampleChromatogramGraphicsRow(System.Data.DataRow):  # Class
        BackColor: str
        ComponentColor: str
        EICColors: str
        FontFamily: str
        FontSize: float
        ForeColor: str
        GridLinesColor: str
        PeakLabelTypes: str
        PeakLabelsAllowOverlap: bool
        PeakLabelsVertical: bool
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        ScaleToHighestPeakAfter: float
        ShowEICs: bool
        ShowLegend: bool
        ShowPeakLabelCaption: bool
        ShowPeakLabelUnits: bool
        ShowPeakLabels: bool
        TICColor: str

        def IsForeColorNull(self) -> bool: ...
        def SetComponentColorNull(self) -> None: ...
        def IsShowEICsNull(self) -> bool: ...
        def IsShowLegendNull(self) -> bool: ...
        def IsFontSizeNull(self) -> bool: ...
        def IsPeakLabelsAllowOverlapNull(self) -> bool: ...
        def SetFontSizeNull(self) -> None: ...
        def IsShowPeakLabelsNull(self) -> bool: ...
        def SetShowPeakLabelCaptionNull(self) -> None: ...
        def IsPeakLabelsVerticalNull(self) -> bool: ...
        def SetFontFamilyNull(self) -> None: ...
        def SetScaleToHighestPeakAfterNull(self) -> None: ...
        def IsShowPeakLabelUnitsNull(self) -> bool: ...
        def SetBackColorNull(self) -> None: ...
        def IsComponentColorNull(self) -> bool: ...
        def SetPeakLabelsVerticalNull(self) -> None: ...
        def SetPeakLabelsAllowOverlapNull(self) -> None: ...
        def IsTICColorNull(self) -> bool: ...
        def IsEICColorsNull(self) -> bool: ...
        def IsFontFamilyNull(self) -> bool: ...
        def IsBackColorNull(self) -> bool: ...
        def SetShowPeakLabelUnitsNull(self) -> None: ...
        def SetShowPeakLabelsNull(self) -> None: ...
        def SetEICColorsNull(self) -> None: ...
        def IsShowPeakLabelCaptionNull(self) -> bool: ...
        def SetShowLegendNull(self) -> None: ...
        def IsPeakLabelTypesNull(self) -> bool: ...
        def IsGridLinesColorNull(self) -> bool: ...
        def IsScaleToHighestPeakAfterNull(self) -> bool: ...
        def SetPeakLabelTypesNull(self) -> None: ...
        def SetTICColorNull(self) -> None: ...
        def SetShowEICsNull(self) -> None: ...
        def SetForeColorNull(self) -> None: ...
        def SetGridLinesColorNull(self) -> None: ...

    class UnknownsSampleChromatogramGraphicsRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow
        )  # readonly

    class UnknownsSampleChromatogramGraphicsRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRowChangeEvent,
        ) -> None: ...

    class UnknownsSpectrumGraphicsDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        BackColorColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FontFamilyColumn: System.Data.DataColumn  # readonly
        FontSizeColumn: System.Data.DataColumn  # readonly
        ForeColorColumn: System.Data.DataColumn  # readonly
        GridLinesColorColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow
        ): ...
        PeakLabelsAllowOverlapColumn: System.Data.DataColumn  # readonly
        PeakLabelsVerticalColumn: System.Data.DataColumn  # readonly
        ReportIDColumn: System.Data.DataColumn  # readonly
        ShowPeakLabelsColumn: System.Data.DataColumn  # readonly

        @overload
        def AddUnknownsSpectrumGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow,
        ) -> None: ...
        @overload
        def AddUnknownsSpectrumGraphicsRow(
            self,
            parentReportRowByFK_Report_UnknownsSpectrumGraphics: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow,
            BackColor: str,
            ForeColor: str,
            GridLinesColor: str,
            FontFamily: str,
            FontSize: float,
            ShowPeakLabels: bool,
            PeakLabelsVertical: bool,
            PeakLabelsAllowOverlap: bool,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByReportID(
            self, ReportID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow
        ): ...
        def RemoveUnknownsSpectrumGraphicsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow,
        ) -> None: ...
        def Clone(self) -> System.Data.DataTable: ...
        def NewUnknownsSpectrumGraphicsRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow
        ): ...

        UnknownsSpectrumGraphicsRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRowChangeEventHandler
        )  # Event
        UnknownsSpectrumGraphicsRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRowChangeEventHandler
        )  # Event
        UnknownsSpectrumGraphicsRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRowChangeEventHandler
        )  # Event
        UnknownsSpectrumGraphicsRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRowChangeEventHandler
        )  # Event

    class UnknownsSpectrumGraphicsRow(System.Data.DataRow):  # Class
        BackColor: str
        FontFamily: str
        FontSize: float
        ForeColor: str
        GridLinesColor: str
        PeakLabelsAllowOverlap: bool
        PeakLabelsVertical: bool
        ReportID: int
        ReportRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.ReportRow
        )
        ShowPeakLabels: bool

        def SetShowPeakLabelsNull(self) -> None: ...
        def SetPeakLabelsVerticalNull(self) -> None: ...
        def SetForeColorNull(self) -> None: ...
        def IsForeColorNull(self) -> bool: ...
        def IsFontFamilyNull(self) -> bool: ...
        def IsFontSizeNull(self) -> bool: ...
        def IsPeakLabelsAllowOverlapNull(self) -> bool: ...
        def IsShowPeakLabelsNull(self) -> bool: ...
        def SetGridLinesColorNull(self) -> None: ...
        def SetBackColorNull(self) -> None: ...
        def IsPeakLabelsVerticalNull(self) -> bool: ...
        def SetPeakLabelsAllowOverlapNull(self) -> None: ...
        def SetFontFamilyNull(self) -> None: ...
        def IsBackColorNull(self) -> bool: ...
        def IsGridLinesColorNull(self) -> bool: ...
        def SetFontSizeNull(self) -> None: ...

    class UnknownsSpectrumGraphicsRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRow
        )  # readonly

    class UnknownsSpectrumGraphicsRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet.UnknownsSpectrumGraphicsRowChangeEvent,
        ) -> None: ...
