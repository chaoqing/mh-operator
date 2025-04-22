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

# Stubs for namespace: Agilent.MSAcquisition.SampleInfoRW

class AgtSampleInfo(
    Agilent.MSAcquisition.SampleInfoRW.IAgtSampleInfoReader,
    Agilent.MSAcquisition.SampleInfoRW.IAgtSampleInfoWriter,
    Agilent.MSAcquisition.SampleInfoRW.IAgtSampleInfoXMLStringMgr,
):  # Class
    def __init__(self) -> None: ...

class DeviceConfigInformation(
    System.IDisposable,
    System.ComponentModel.IListSource,
    System.Xml.Serialization.IXmlSerializable,
    System.ComponentModel.ISupportInitializeNotification,
    System.ComponentModel.IComponent,
    System.ComponentModel.ISupportInitialize,
    System.IServiceProvider,
    System.Runtime.Serialization.ISerializable,
    Agilent.MSAcquisition.SampleInfoRW.IDeviceConfigDataMgr,
    System.Data.DataSet,
):  # Class
    def __init__(self) -> None: ...

    Device: (
        Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceDataTable
    )  # readonly
    DeviceConfigInfo: (
        Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoDataTable
    )  # readonly
    Parameter: (
        Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterDataTable
    )  # readonly
    Relations: System.Data.DataRelationCollection  # readonly
    SchemaSerializationMode: System.Data.SchemaSerializationMode
    Tables: System.Data.DataTableCollection  # readonly

    def WriteDeviceConfig(self, dataFilePath: str) -> None: ...
    @staticmethod
    def GetTypedDataSetSchema(
        xs: System.Xml.Schema.XmlSchemaSet,
    ) -> System.Xml.Schema.XmlSchemaComplexType: ...
    def ReadDeviceConfig(self, dataFilePath: str) -> None: ...
    def Clone(self) -> System.Data.DataSet: ...

    # Nested Types

    class DeviceConfigInfoDataTable(
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

        Count: int  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRow
        ): ...
        VersionColumn: System.Data.DataColumn  # readonly

        def GetEnumerator(self) -> Iterator[Any]: ...
        @overload
        def AddDeviceConfigInfoRow(
            self,
            row: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRow,
        ) -> None: ...
        @overload
        def AddDeviceConfigInfoRow(
            self, Version: str
        ) -> (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRow
        ): ...
        def NewDeviceConfigInfoRow(
            self,
        ) -> (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRow
        ): ...
        def RemoveDeviceConfigInfoRow(
            self,
            row: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def Clone(self) -> System.Data.DataTable: ...

        DeviceConfigInfoRowChanged: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRowChangeEventHandler
        )  # Event
        DeviceConfigInfoRowChanging: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRowChangeEventHandler
        )  # Event
        DeviceConfigInfoRowDeleted: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRowChangeEventHandler
        )  # Event
        DeviceConfigInfoRowDeleting: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRowChangeEventHandler
        )  # Event

    class DeviceConfigInfoRow(System.Data.DataRow):  # Class
        Version: str

        def SetVersionNull(self) -> None: ...
        def IsVersionNull(self) -> bool: ...

    class DeviceConfigInfoRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRow
        )  # readonly

    class DeviceConfigInfoRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceConfigInfoRowChangeEvent,
        ) -> None: ...

    class DeviceDataTable(
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

        Count: int  # readonly
        DeviceIDColumn: System.Data.DataColumn  # readonly
        DisplayNameColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRow: ...
        def GetEnumerator(self) -> Iterator[Any]: ...
        def RemoveDeviceRow(
            self,
            row: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewDeviceRow(
            self,
        ) -> Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRow: ...
        def FindByDeviceID(
            self, DeviceID: str
        ) -> Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRow: ...
        @overload
        def AddDeviceRow(
            self,
            row: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRow,
        ) -> None: ...
        @overload
        def AddDeviceRow(
            self, DeviceID: str, DisplayName: str
        ) -> Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRow: ...
        def Clone(self) -> System.Data.DataTable: ...

        DeviceRowChanged: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRowChangeEventHandler
        )  # Event
        DeviceRowChanging: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRowChangeEventHandler
        )  # Event
        DeviceRowDeleted: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRowChangeEventHandler
        )  # Event
        DeviceRowDeleting: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRowChangeEventHandler
        )  # Event

    class DeviceRow(System.Data.DataRow):  # Class
        DeviceID: str
        DisplayName: str

        def SetDisplayNameNull(self) -> None: ...
        def GetParameterRows(
            self,
        ) -> List[
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRow
        ]: ...
        def IsDisplayNameNull(self) -> bool: ...

    class DeviceRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRow
        )  # readonly

    class DeviceRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRowChangeEvent,
        ) -> None: ...

    class ParameterDataTable(
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

        Count: int  # readonly
        DeviceIDColumn: System.Data.DataColumn  # readonly
        DisplayNameColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRow
        ): ...
        ResourceIDColumn: System.Data.DataColumn  # readonly
        ResourceNameColumn: System.Data.DataColumn  # readonly
        UnitsColumn: System.Data.DataColumn  # readonly
        ValueColumn: System.Data.DataColumn  # readonly

        def GetEnumerator(self) -> Iterator[Any]: ...
        @overload
        def AddParameterRow(
            self,
            row: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRow,
        ) -> None: ...
        @overload
        def AddParameterRow(
            self,
            parentDeviceRowByDevice_Parameter: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRow,
            ResourceName: str,
            ResourceID: str,
            Value: str,
            Units: str,
            DisplayName: str,
        ) -> (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewParameterRow(
            self,
        ) -> (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRow
        ): ...
        def RemoveParameterRow(
            self,
            row: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRow,
        ) -> None: ...
        def Clone(self) -> System.Data.DataTable: ...

        ParameterRowChanged: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRowChangeEventHandler
        )  # Event
        ParameterRowChanging: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRowChangeEventHandler
        )  # Event
        ParameterRowDeleted: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRowChangeEventHandler
        )  # Event
        ParameterRowDeleting: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRowChangeEventHandler
        )  # Event

    class ParameterRow(System.Data.DataRow):  # Class
        DeviceID: str
        DeviceRow: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.DeviceRow
        DisplayName: str
        ResourceID: str
        ResourceName: str
        Units: str
        Value: str

        def IsUnitsNull(self) -> bool: ...
        def SetResourceNameNull(self) -> None: ...
        def IsDisplayNameNull(self) -> bool: ...
        def SetResourceIDNull(self) -> None: ...
        def SetValueNull(self) -> None: ...
        def IsDeviceIDNull(self) -> bool: ...
        def SetDeviceIDNull(self) -> None: ...
        def SetDisplayNameNull(self) -> None: ...
        def IsResourceNameNull(self) -> bool: ...
        def IsResourceIDNull(self) -> bool: ...
        def SetUnitsNull(self) -> None: ...
        def IsValueNull(self) -> bool: ...

    class ParameterRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRow
        )  # readonly

    class ParameterRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MSAcquisition.SampleInfoRW.DeviceConfigInformation.ParameterRowChangeEvent,
        ) -> None: ...

class IAgtSampleInfoReader(object):  # Interface
    def SetSchemaPath(self, SchemaPath: str) -> None: ...
    def GetSampleInfo(
        self,
        DataFilePath: str,
        ProcessingMode: str,
        ArrSystemNames: List[str],
        ArrDisplayNames: List[str],
        ArrDataValues: List[str],
        ArrDataType: List[int],
        ArrUnits: List[str],
    ) -> None: ...

class IAgtSampleInfoWriter(object):  # Interface
    def SaveSampleInfo(
        self,
        DataFilePath: str,
        ProcessingMode: str,
        ArrSystemNames: List[str],
        ArrDisplayNames: List[str],
        ArrDataValues: List[str],
        ArrDataType: List[int],
        ArrUnits: List[str],
    ) -> None: ...

class IAgtSampleInfoXMLStringMgr(object):  # Interface
    def CreateSampleInfoXMLString(self, SampleInfoXMLString: str) -> None: ...
    def SetSchemaPath(self, SchemaPath: str) -> None: ...
    def GetSampleInfo(
        self,
        ArrSystemNames: List[str],
        ArrDisplayNames: List[str],
        ArrDataValues: List[str],
        ArrDataType: List[str],
        ArrUnits: List[str],
        ArrFieldType: List[str],
    ) -> None: ...
    def LoadSampleInfoXMLStringIntoCache(
        self, FilePath: str, SampleInfoXMLString: str
    ) -> None: ...
    def SaveSampleInfoFromCache(self, FilePath: str) -> None: ...
    def SaveSampleInfoXMLString(
        self, SampleInfoXMLString: str, FilePath: str
    ) -> None: ...
    def CacheSampleInfoFromXMLString(self, SampleInfoXMLString: str) -> None: ...
    def UpdateSampleInfoField(self, Name: str, Value: str) -> None: ...
    def AddSampleInfoField(
        self,
        Name: str,
        DisplayName: str,
        Value: str,
        DataType: str,
        Units: str,
        FieldType: str,
    ) -> None: ...
    def ClearSaveXMLString(self) -> None: ...
    def GetSampleInfoField(
        self,
        Name: str,
        DisplayName: str,
        Value: str,
        DataType: str,
        Units: str,
        FieldType: str,
    ) -> None: ...

class IDeviceConfigDataMgr(object):  # Interface
    def ReadDeviceConfig(self, dataFilePath: str) -> None: ...
    def WriteDeviceConfig(self, dataFilePath: str) -> None: ...
