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

from . import QDB

# Stubs for namespace: Agilent.MassSpectrometry.MSDChem

class AcqMSFile:  # Class
    def __init__(self, strFileName: str) -> None: ...
    def Open(self) -> None: ...
    def GetSIMGroups(
        self,
    ) -> Iterable[Agilent.MassSpectrometry.MSDChem.AcqMSFile.SIMTimeSegment]: ...

    # Nested Types

    class SIMIon:  # Class
        Dwell: int  # readonly
        Label: str  # readonly
        MZ: float  # readonly
        PlotThisIon: bool  # readonly

    class SIMTimeSegment:  # Class
        def __init__(self) -> None: ...

        EMVParameter: float  # readonly
        Group: int  # readonly
        GroupDwell: int  # readonly
        MassGain: float  # readonly
        MassOffset: float  # readonly
        Name: str  # readonly
        NoEICPlot: int  # static # readonly
        NumberOfIons: int  # readonly
        NumberOfSingleIonChromatograms: int  # readonly
        StartTime: float  # readonly
        UseTimeSegmentEMVParameter: bool  # readonly
        Wide: bool  # readonly

        def GetIons(
            self,
        ) -> Iterable[Agilent.MassSpectrometry.MSDChem.AcqMSFile.SIMIon]: ...

class CVTINFO:  # Class
    def __init__(self) -> None: ...

    DataDelta: float
    DataTime: float
    DataValue: int
    SigHdr_SigID: int
    SigHdr_nPts: int
    SigID: int

class ElementParse:  # Class
    def __init__(self) -> None: ...
    def LoadAWtable(self, tableFile: str) -> None: ...
    def CalcMw(self, formStr: str, mw: float) -> None: ...
    def ParseOneLevel(self, inputStr: str, strPos: int, succeeded: int) -> int: ...
    def TallyFormula(self, index: int, multiplier: int) -> None: ...

class ExtensionSpecificFolderBrowserDialog(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    Description: str
    Extension: str
    SelectedPath: str
    ShowNewFolderButton: bool

    def Close(self) -> None: ...
    def Dispose(self) -> None: ...
    def ShowDialog(self) -> System.Windows.Forms.DialogResult: ...

class FileCheckStructU6890:  # Class
    def __init__(self) -> None: ...

    CheckSum: List[int]
    FILEEXTENSIONULEN: int = ...  # static # readonly
    FileExtensionUStr: str

class FileCheckStructU7890:  # Class
    def __init__(self) -> None: ...

    CheckSum: List[int]
    FILEEXTENSIONULEN: int = ...  # static # readonly
    FileExtensionUStr: str

class FullSequenceDownloadDataSet(
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

    Method: (
        Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodDataTable
    )  # readonly
    Relations: System.Data.DataRelationCollection  # readonly
    Sample: (
        Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleDataTable
    )  # readonly
    SchemaSerializationMode: System.Data.SchemaSerializationMode
    Sequence: (
        Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceDataTable
    )  # readonly
    Tables: System.Data.DataTableCollection  # readonly

    @staticmethod
    def GetTypedDataSetSchema(
        xs: System.Xml.Schema.XmlSchemaSet,
    ) -> System.Xml.Schema.XmlSchemaComplexType: ...
    def Clone(self) -> System.Data.DataSet: ...

    # Nested Types

    class MethodDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRow
        ],
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        Count: int  # readonly
        IDPathColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRow: ...
        MethodIDColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewMethodRow(
            self,
        ) -> Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRow: ...
        def Clone(self) -> System.Data.DataTable: ...
        @overload
        def AddMethodRow(
            self,
            row: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRow,
        ) -> None: ...
        @overload
        def AddMethodRow(
            self,
            IDPath: str,
            parentSampleRowByFK_Sample_Method: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow,
        ) -> Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRow: ...
        def RemoveMethodRow(
            self,
            row: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRow,
        ) -> None: ...

        MethodRowChanged: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRowChangeEventHandler
        )  # Event
        MethodRowChanging: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRowChangeEventHandler
        )  # Event
        MethodRowDeleted: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRowChangeEventHandler
        )  # Event
        MethodRowDeleting: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRowChangeEventHandler
        )  # Event

    class MethodRow(System.Data.DataRow):  # Class
        IDPath: str
        MethodID: int
        SampleRow: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow
        )

        def SetIDPathNull(self) -> None: ...
        def SetMethodIDNull(self) -> None: ...
        def IsIDPathNull(self) -> bool: ...
        def IsMethodIDNull(self) -> bool: ...

    class MethodRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRow
        )  # readonly

    class MethodRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRowChangeEvent,
        ) -> None: ...

    class SampleDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow
        ],
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        Count: int  # readonly
        ExpectedBarcodeFrontColumn: System.Data.DataColumn  # readonly
        ExpectedBarcodeRearColumn: System.Data.DataColumn  # readonly
        InjectionLocationColumn: System.Data.DataColumn  # readonly
        InjectionSourceColumn: System.Data.DataColumn  # readonly
        InjectionVialColumn: System.Data.DataColumn  # readonly
        InjectorVolumeColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow: ...
        MethodAlreadyUsedCodeColumn: System.Data.DataColumn  # readonly
        MethodIDColumn: System.Data.DataColumn  # readonly
        SampleNameColumn: System.Data.DataColumn  # readonly
        SampleOfMethColumn: System.Data.DataColumn  # readonly
        SeqLineColumn: System.Data.DataColumn  # readonly
        TrayNameColumn: System.Data.DataColumn  # readonly
        UseHeadspaceColumn: System.Data.DataColumn  # readonly

        def FindBySeqLine(
            self, SeqLine: int
        ) -> Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddSampleRow(
            self,
            row: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow,
        ) -> None: ...
        @overload
        def AddSampleRow(
            self,
            SampleOfMeth: int,
            SeqLine: int,
            InjectionVial: int,
            InjectionSource: int,
            MethodAlreadyUsedCode: int,
            UseHeadspace: str,
            MethodID: int,
            InjectionLocation: str,
            ExpectedBarcodeFront: str,
            ExpectedBarcodeRear: str,
            InjectorVolume: float,
            TrayName: str,
            SampleName: str,
        ) -> Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow: ...
        def Clone(self) -> System.Data.DataTable: ...
        def NewSampleRow(
            self,
        ) -> Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow: ...
        def RemoveSampleRow(
            self,
            row: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow,
        ) -> None: ...

        SampleRowChanged: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRowChangeEventHandler
        )  # Event
        SampleRowChanging: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRowChangeEventHandler
        )  # Event
        SampleRowDeleted: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRowChangeEventHandler
        )  # Event
        SampleRowDeleting: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRowChangeEventHandler
        )  # Event

    class SampleRow(System.Data.DataRow):  # Class
        ExpectedBarcodeFront: str
        ExpectedBarcodeRear: str
        InjectionLocation: str
        InjectionSource: int
        InjectionVial: int
        InjectorVolume: float
        MethodAlreadyUsedCode: int
        MethodID: int
        SampleName: str
        SampleOfMeth: int
        SeqLine: int
        TrayName: str
        UseHeadspace: str

        def SetInjectionLocationNull(self) -> None: ...
        def IsInjectionSourceNull(self) -> bool: ...
        def SetUseHeadspaceNull(self) -> None: ...
        def SetInjectionSourceNull(self) -> None: ...
        def IsSampleOfMethNull(self) -> bool: ...
        def IsSampleNameNull(self) -> bool: ...
        def SetMethodAlreadyUsedCodeNull(self) -> None: ...
        def IsExpectedBarcodeFrontNull(self) -> bool: ...
        def SetExpectedBarcodeFrontNull(self) -> None: ...
        def SetTrayNameNull(self) -> None: ...
        def IsInjectorVolumeNull(self) -> bool: ...
        def IsExpectedBarcodeRearNull(self) -> bool: ...
        def SetInjectorVolumeNull(self) -> None: ...
        def SetInjectionVialNull(self) -> None: ...
        def IsTrayNameNull(self) -> bool: ...
        def SetExpectedBarcodeRearNull(self) -> None: ...
        def SetSampleNameNull(self) -> None: ...
        def GetMethodRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.MethodRow
        ]: ...
        def IsUseHeadspaceNull(self) -> bool: ...
        def IsInjectionLocationNull(self) -> bool: ...
        def IsMethodAlreadyUsedCodeNull(self) -> bool: ...
        def IsInjectionVialNull(self) -> bool: ...
        def SetSampleOfMethNull(self) -> None: ...

    class SampleRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRow
        )  # readonly

    class SampleRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SampleRowChangeEvent,
        ) -> None: ...

    class SequenceDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRow
        ],
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        Count: int  # readonly
        IDPathColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRow
        ): ...
        MethodCountColumn: System.Data.DataColumn  # readonly
        SampleCountColumn: System.Data.DataColumn  # readonly

        @overload
        def AddSequenceRow(
            self,
            row: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRow,
        ) -> None: ...
        @overload
        def AddSequenceRow(
            self, IDPath: str, SampleCount: int, MethodCount: int
        ) -> (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewSequenceRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveSequenceRow(
            self,
            row: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRow,
        ) -> None: ...

        SequenceRowChanged: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRowChangeEventHandler
        )  # Event
        SequenceRowChanging: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRowChangeEventHandler
        )  # Event
        SequenceRowDeleted: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRowChangeEventHandler
        )  # Event
        SequenceRowDeleting: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRowChangeEventHandler
        )  # Event

    class SequenceRow(System.Data.DataRow):  # Class
        IDPath: str
        MethodCount: int
        SampleCount: int

        def IsIDPathNull(self) -> bool: ...
        def IsSampleCountNull(self) -> bool: ...
        def IsMethodCountNull(self) -> bool: ...
        def SetSampleCountNull(self) -> None: ...
        def SetIDPathNull(self) -> None: ...
        def SetMethodCountNull(self) -> None: ...

    class SequenceRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRow
        )  # readonly

    class SequenceRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.MSDChem.FullSequenceDownloadDataSet.SequenceRowChangeEvent,
        ) -> None: ...

class GC5890DataFile(Agilent.MassSpectrometry.MSDChem.IChemStationDataFile):  # Class
    def __init__(self, i32FileSubType: int) -> None: ...

    END_FLAG: int = ...  # static # readonly

    ActualBarcode: str  # readonly
    DateTime: str  # readonly
    InstrumentName: str  # readonly
    def __getitem__(self, iTimeOrAbundance: int, jPointNumber: int) -> float: ...
    MethodFile: str  # readonly
    Operator: str  # readonly
    SampleName: str  # readonly

    def GetYArray(self) -> List[float]: ...
    def OpenRead(self, filename: str) -> bool: ...

class GC6890DataFile(Agilent.MassSpectrometry.MSDChem.IChemStationDataFile):  # Class
    def __init__(self) -> None: ...

    ActualBarcode: str  # readonly
    DateTime: str  # readonly
    InstrumentName: str  # readonly
    def __getitem__(self, iTimeOrAbundance: int, jPointNumber: int) -> float: ...
    MethodFile: str  # readonly
    Operator: str  # readonly
    SampleName: str  # readonly

    def GetNumPoints(self) -> int: ...
    def GetYArray(self) -> List[float]: ...
    def OpenRead(self, filename: str) -> bool: ...

class GC7890DataFile(Agilent.MassSpectrometry.MSDChem.IChemStationDataFile):  # Class
    def __init__(self) -> None: ...

    ActualBarcode: str  # readonly
    DateTime: str  # readonly
    InstrumentName: str  # readonly
    def __getitem__(self, iTimeOrAbundance: int, jPointNumber: int) -> float: ...
    MethodFile: str  # readonly
    Operator: str  # readonly
    SampleName: str  # readonly

    def GetYArray(self) -> List[float]: ...
    def OpenRead(self, filename: str) -> bool: ...

class IChemStationDataFile(object):  # Interface
    InstrumentName: str  # readonly

class IILDCommand(object):  # Interface
    def DoSomething(self) -> None: ...

class InstConfigItem(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    IC_ALS_ID: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_ALS_TYPE: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_APPLICATION: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_AUXINLET_ENABLED: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_AVAILABLE_SOURCES: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_DETECTOR_IRIS: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_GC_ID: Agilent.MassSpectrometry.MSDChem.InstConfigItem = ...  # static # readonly
    IC_GC_NETWORK_ADDRESS: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_GC_STATUS_PANEL_STATE: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_GC_TOWER: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_HS_IP: Agilent.MassSpectrometry.MSDChem.InstConfigItem = ...  # static # readonly
    IC_HS_PORT: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_HS_TYPE: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_INJECTOR_STATUS_PANEL_STATE: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_INLET_GC: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_INSTR_OFFLINE: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_IR_ID: Agilent.MassSpectrometry.MSDChem.InstConfigItem = ...  # static # readonly
    IC_IR_TYPE: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_MAX_ITEM_ID: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_MAX_MS_OPTION_ID: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_MS_CI: Agilent.MassSpectrometry.MSDChem.InstConfigItem = ...  # static # readonly
    IC_MS_CI_OFFSET: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_MS_CONNECTION: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_MS_DCPOL: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_MS_EI: Agilent.MassSpectrometry.MSDChem.InstConfigItem = ...  # static # readonly
    IC_MS_EI_OFFSET: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_MS_ID: Agilent.MassSpectrometry.MSDChem.InstConfigItem = ...  # static # readonly
    IC_MS_LCINST: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_MS_NETWORK_ADDRESS: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_MS_OPTIONS_START: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_MS_TYPE: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly
    IC_PALALS_IP: Agilent.MassSpectrometry.MSDChem.InstConfigItem = (
        ...
    )  # static # readonly

class MAT_REGRESSION:  # Class
    def __init__(self) -> None: ...

    A: System.Array[float]
    FLT_MIN: float = ...  # static # readonly
    MAX_ORDER: int = ...  # static # readonly
    coeff: List[float]
    residual: float

    def HigherOrderRegression(
        self, x: List[float], y: List[float], numPoints: int, wParam: int
    ) -> bool: ...

class MSDChemDataMSFile(Agilent.MassSpectrometry.MSDChem.IChemStationDataFile):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, bUseExtendedHeader: bool) -> None: ...

    ALSBottle: str
    AcqDateTime: System.DateTime
    AcquisitionMethod: str
    ActualBarcode: str
    BasePeakOffset: int
    ComputerName: str
    DataName: str
    ExpectedBarcode: str
    FileFullPathName: str  # readonly
    FileName: str  # readonly
    FilePath: str  # readonly
    HashExtra1: str
    HashExtra2: str
    HashForAcquisition: str
    HashForTune: str
    Inlet: str
    InstName: str
    InstrumentName: str  # readonly
    LanguageID: int
    MaximumRetentionTime: float
    MaximumSignal: int
    MinimumRetentionTime: float
    MinimumSignal: int
    MiscInfo: str
    NumberOfSpectra: int
    Operator: str
    Replicate: int
    SequenceIndex: int
    SpectralRecordsOffset: int  # readonly
    TimeZone: int
    UserAccountName: str
    UserName: str
    UsesExtendedHeaderFormat: bool  # readonly

    def InitRecover(self) -> None: ...
    def OpenRead(self, filename: str) -> bool: ...
    def GetSpectrumDataTypeByIndex1Based(
        self, iSpectrumNumber1Based: int
    ) -> Agilent.MassSpectrometry.MSDChem.SpectralRecordType: ...
    @staticmethod
    def PackAbundance(unpacked: int) -> int: ...
    def SetDataFilePath(self, dataFilePath: str, dataFileName: str) -> None: ...
    def GetExtendedHeaderTime(self) -> System.DateTime: ...
    def GetDirectoryRecord1Based(
        self,
        iIndexOneBased: int,
        iDataOffsetInBytesZeroBased: int,
        dRetentionTimeMinutes: float,
        iTotalResponse: int,
    ) -> None: ...
    @overload
    def AppendSpectrum(
        self, mz: List[float], intensity: List[float], retentionTimeMinutes: float
    ) -> None: ...
    @overload
    def AppendSpectrum(
        self,
        mz: List[float],
        intensity: List[float],
        retentionTimeMinutes: float,
        specType: Agilent.MassSpectrometry.MSDChem.SpectralRecordType,
        status: int,
    ) -> None: ...
    @overload
    def AppendSpectrum(
        self, mz: List[float], intensity: List[float], retentionTimeMinutes: float
    ) -> None: ...
    @overload
    def AppendSpectrum(
        self, smartCardDataBuffer: List[int], i32NumberOfBytesToWrite: int
    ) -> None: ...
    @overload
    def AppendSpectrum(
        self,
        mz: List[float],
        intensity: List[float],
        retentionTimeMinutes: float,
        specType: Agilent.MassSpectrometry.MSDChem.SpectralRecordType,
        status: int,
    ) -> None: ...
    def RecoverSpectrumByIndex1Based(
        self, iSpectrumNumber1Based: int, dRetentionTimeMinutes: float
    ) -> List[float]: ...
    @staticmethod
    def HasStatusIndicator(
        u16Status: int,
        code: Agilent.MassSpectrometry.MSDChem.MSDChemDataMSFile.SpectralStatusCodes,
    ) -> bool: ...
    @overload
    def Close(self) -> None: ...
    @overload
    def Close(self, updateHeader: bool) -> None: ...
    def GetStandardHeaderTime(self) -> str: ...
    @overload
    def GetSpectrumByIndex1Based(
        self,
        iSpectrumNumber1Based: int,
        dRetentionTime: float,
        u16Status: int,
        u16DataType: int,
    ) -> List[float]: ...
    @overload
    def GetSpectrumByIndex1Based(
        self,
        iSpectrumNumber1Based: int,
        dRetentionTime: float,
        u16Status: int,
        dMZs: List[float],
        dIntensities: List[float],
    ) -> None: ...
    @overload
    def GetSpectrumByIndex1Based(
        self, iSpectrumNumber1Based: int, dRetentionTime: float
    ) -> List[float]: ...
    @overload
    def GetSpectrumByIndex1Based(
        self, iSpectrumNumber1Based: int, dRetentionTime: float, u16DataType: int
    ) -> List[float]: ...
    def GetTotalIonByTime(
        self,
        dTimeRangeLowMin: float,
        dTimeRangeHighMin: float,
        times: System.Collections.Generic.List[float],
        intensities: System.Collections.Generic.List[float],
    ) -> None: ...
    @staticmethod
    def GetSpectrumFromSmartcardBuffer(
        smartCardDataBuffer: List[int],
        dRetentionTimeMinutes: float,
        dMZs: List[float],
        dIntensities: List[float],
        dMinX: float,
        dMaxX: float,
        dMaxY: float,
        dBasePeakMZ: float,
        dBasePeakIntensity: float,
        dTIC: float,
        spectralRecordType: Agilent.MassSpectrometry.MSDChem.SpectralRecordType,
    ) -> None: ...
    @overload
    def OpenWrite(self, filename: str) -> bool: ...
    @overload
    def OpenWrite(
        self,
        newFileName: str,
        guideFile: Agilent.MassSpectrometry.MSDChem.MSDChemDataMSFile,
    ) -> bool: ...
    def SetMethodPath(self, methodPath: str, methodFileName: str) -> None: ...
    def Snapshot(self, snapshotFileName: str) -> None: ...
    def SetTuneFilePath(self, tuneFilePath: str, tuneFileName: str) -> None: ...

    # Nested Types

    class SpectralStatusCodes(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        STATUS_MS_FAULT: (
            Agilent.MassSpectrometry.MSDChem.MSDChemDataMSFile.SpectralStatusCodes
        ) = ...  # static # readonly
        STATUS_MS_IOERROR: (
            Agilent.MassSpectrometry.MSDChem.MSDChemDataMSFile.SpectralStatusCodes
        ) = ...  # static # readonly
        STATUS_OK: (
            Agilent.MassSpectrometry.MSDChem.MSDChemDataMSFile.SpectralStatusCodes
        ) = ...  # static # readonly
        STATUS_RECORD_OVERFLOW: (
            Agilent.MassSpectrometry.MSDChem.MSDChemDataMSFile.SpectralStatusCodes
        ) = ...  # static # readonly
        STATUS_TIC_OVERFLOW: (
            Agilent.MassSpectrometry.MSDChem.MSDChemDataMSFile.SpectralStatusCodes
        ) = ...  # static # readonly
        STATUS_VALUE_OVERFLOW: (
            Agilent.MassSpectrometry.MSDChem.MSDChemDataMSFile.SpectralStatusCodes
        ) = ...  # static # readonly

class MSDChemUtil:  # Class
    def __init__(self) -> None: ...

    GROUP_ACQ_ANALYSTS_I: str = ...  # static # readonly
    GROUP_ACQ_ANALYSTS_II: str = ...  # static # readonly
    GROUP_ACQ_ANALYSTS_III: str = ...  # static # readonly
    GROUP_ACQ_MANAGERS: str = ...  # static # readonly

    @staticmethod
    def FindRealRoots(
        coeff: List[float], root: List[float], order: int, nRootsFound: int
    ) -> None: ...
    @staticmethod
    def RoleSecurityMode() -> bool: ...
    @staticmethod
    def lsplitspec(fullspec: str, KeepSlash: bool, lastchunk: str) -> None: ...
    @staticmethod
    def AreRealsEqual(x: float, y: float) -> bool: ...
    @staticmethod
    def RemoveAnalystUsersAndGroups(
        messages: System.Collections.Generic.List[str],
    ) -> bool: ...
    @staticmethod
    def FloatToString(dValue: float, nPrecision: int, psString: str) -> None: ...
    @staticmethod
    def lfullspec(fullspec: str, DefPath: str) -> str: ...
    @staticmethod
    def ReadCStringW(br: System.IO.BinaryReader) -> str: ...
    @staticmethod
    def WritePrivateProfileString(
        lpApplicationName: str, lpKeyName: str, lpString: str, lpFileName: str
    ) -> int: ...
    @staticmethod
    def SeparateInput(
        inputLine: str, runstringParam: System.Collections.Generic.List[str]
    ) -> None: ...
    @staticmethod
    def PrintTextFile(
        strFileName: str,
        i32NumberOfPagesPrinted: int,
        font: System.Drawing.Font,
        bUseSoftMargin: bool,
    ) -> None: ...
    @staticmethod
    def RegisterDistillerSettings(
        pathName: str, exeName: str, outfileName: str
    ) -> None: ...
    @staticmethod
    def GetExecutablesPath() -> str: ...
    @staticmethod
    def IsHeadspaceDriverInstalled() -> bool: ...
    @staticmethod
    def FormDispose(form: System.Windows.Forms.Form) -> None: ...
    @staticmethod
    def GetUTCOffsetString(dateTime: System.DateTime) -> str: ...
    @overload
    @staticmethod
    def GetPrivateProfileString(
        lpAppName: str,
        lpKeyName: str,
        lpDefault: str,
        lpReturnedString: System.Text.StringBuilder,
        nSize: int,
        lpFileName: str,
    ) -> int: ...
    @overload
    @staticmethod
    def GetPrivateProfileString(
        lpAppName: str,
        lpKeyName: str,
        lpDefault: str,
        lpReturnedString: List[str],
        nSize: int,
        lpFileName: str,
    ) -> int: ...
    @staticmethod
    def LocalePreferredFontFaceName(
        fontUsageCategory: Agilent.MassSpectrometry.MSDChem.MSDChemUtil.FontUsageCategory,
    ) -> str: ...
    @staticmethod
    def roundToInt(x: float) -> int: ...
    @staticmethod
    def roundToLong(x: float) -> int: ...
    @staticmethod
    def CreateApplicationFileName(
        rstrFileName: str, bOverwrite: bool, rstrRootElementName: str
    ) -> Agilent.MassSpectrometry.MSDChem.XMLConfiguration: ...
    @staticmethod
    def IsLeanMeanDataAnalysisInstalled() -> bool: ...
    @staticmethod
    def SetApplicationFileName(
        rstrFileName: str,
    ) -> Agilent.MassSpectrometry.MSDChem.XMLConfiguration: ...
    @staticmethod
    def IsExtOk(filename: str, extension: str, ForceAppend: bool) -> bool: ...
    @overload
    @staticmethod
    def UserPossessesRole(
        principalUser: System.Security.Principal.IPrincipal, role: str
    ) -> bool: ...
    @overload
    @staticmethod
    def UserPossessesRole(role: str) -> bool: ...
    @staticmethod
    def SetBusyCursor(formParent: System.Windows.Forms.Form, bWait: bool) -> None: ...
    @staticmethod
    def ChangeMultiExtension(filePathName: str, newExtension: str) -> None: ...
    @staticmethod
    def ChromatographFileType(strFileName: str) -> int: ...
    @staticmethod
    def GetInstallPath() -> str: ...
    @staticmethod
    def iscfr() -> bool: ...
    @overload
    @staticmethod
    def GetPageSizeInCharacters(
        font: System.Drawing.Font,
        columnsSize: int,
        rowsSize: int,
        nWidth: int,
        nHeight: int,
        dPaperSizeWidthInches: float,
        dPaperSizeHeightInches: float,
    ) -> None: ...
    @overload
    @staticmethod
    def GetPageSizeInCharacters(
        columnsSize: int, rowsSize: int, nWidth: int, nHeight: int
    ) -> None: ...
    @staticmethod
    def CopyDirectory(sourceFolder: str, destinationLocation: str) -> None: ...
    @staticmethod
    def GetWindowDoc(strWindowInfoPath: str) -> System.Xml.XmlDocument: ...
    @staticmethod
    def AddAnalystUsersAndGroups(
        messages: System.Collections.Generic.List[str], addUsers: bool
    ) -> bool: ...
    @staticmethod
    def GetPrivateProfileInt(
        lpAppName: str, lpKeyName: str, lpDefault: int, lpFileName: str
    ) -> int: ...
    @staticmethod
    def KillProcesses(blarg: str, transcript: str) -> None: ...
    @staticmethod
    def EncryptPassword(strEncryptionKey: str, password: str) -> str: ...
    @staticmethod
    def FindMdiClient(
        parent: System.Windows.Forms.Form,
    ) -> System.Windows.Forms.MdiClient: ...
    @staticmethod
    def BlockInput(fBlockIt: bool) -> bool: ...
    @staticmethod
    def IsMsinsctlNet() -> bool: ...
    def IS_AddAnalystUsersAndGroups(self, addUsers: bool) -> bool: ...
    @staticmethod
    def GetGCFileDescClassName(filename: str) -> str: ...
    @staticmethod
    def cfroperator() -> str: ...
    @staticmethod
    def GetMemoryUsage(
        hProcess: System.IntPtr,
        pi32NumPageFaults: int,
        pi64WorkingSetSize: int,
        pi64PeakWorkingSetSize: int,
        pi64Private: int,
        piSystemPerfStats: List[int],
        iCountSystemPerfStats: int,
    ) -> None: ...
    @staticmethod
    def GetDateStampWithUTCOffset(dateTime: System.DateTime) -> str: ...

    # Nested Types

    class FontUsageCategory(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        Printing: Agilent.MassSpectrometry.MSDChem.MSDChemUtil.FontUsageCategory = (
            ...
        )  # static # readonly
        Screen: Agilent.MassSpectrometry.MSDChem.MSDChemUtil.FontUsageCategory = (
            ...
        )  # static # readonly
        ScreenFixedPitch: (
            Agilent.MassSpectrometry.MSDChem.MSDChemUtil.FontUsageCategory
        ) = ...  # static # readonly
        Unknown: Agilent.MassSpectrometry.MSDChem.MSDChemUtil.FontUsageCategory = (
            ...
        )  # static # readonly

    class Point:  # Struct
        x: int
        y: int

    class RECT:  # Struct
        bottom: int
        left: int
        right: int
        top: int

class Method:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def GetAcqMSItem(
        rstrMethodLocator: str, acqMSPathComponents: List[str], rstrResult: str
    ) -> bool: ...
    @overload
    @staticmethod
    def SetAcqCtlItem(
        rstrMethodLocator: str, acqCtlPathComponents: List[str], rstrValue: str
    ) -> bool: ...
    @overload
    @staticmethod
    def SetAcqCtlItem(
        rstrMethodLocator: str, acqCtlPathComponents: List[str], i32Value: int
    ) -> bool: ...
    @staticmethod
    def MSDChemGetMethodInteger(
        rstrMethodLocator: str, rstrItemLocator: str, pi32Result: int
    ) -> bool: ...
    @staticmethod
    def GetString(
        rstrMethodLocator: str, rstrItemLocator: str, rstrResult: str
    ) -> bool: ...
    @staticmethod
    def MSDChemGetMethodScalar(
        rstrMethodLocator: str, rstrItemLocator: str, pdResult: float
    ) -> bool: ...
    @staticmethod
    def GetAcqCtlItem(
        rstrMethodLocator: str, acqCtlPathComponents: List[str], rstrResult: str
    ) -> bool: ...

class PrintTextFileDocument(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.Drawing.Printing.PrintDocument,
):  # Class
    ...

class RC_OPERATION(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    RUNOP_ARM: Agilent.MassSpectrometry.MSDChem.RC_OPERATION = ...  # static # readonly
    RUNOP_FINALPRERUN: Agilent.MassSpectrometry.MSDChem.RC_OPERATION = (
        ...
    )  # static # readonly
    RUNOP_INITIALPRERUN: Agilent.MassSpectrometry.MSDChem.RC_OPERATION = (
        ...
    )  # static # readonly
    RUNOP_NULL: Agilent.MassSpectrometry.MSDChem.RC_OPERATION = ...  # static # readonly
    RUNOP_POSTRUN: Agilent.MassSpectrometry.MSDChem.RC_OPERATION = (
        ...
    )  # static # readonly
    RUNOP_PRERUN: Agilent.MassSpectrometry.MSDChem.RC_OPERATION = (
        ...
    )  # static # readonly
    RUNOP_SAMPLEPREP: Agilent.MassSpectrometry.MSDChem.RC_OPERATION = (
        ...
    )  # static # readonly

class ReportViewerCleaner(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def CollectHandlers(self) -> None: ...
    def CleanHandlers(self) -> None: ...
    def Dispose(self) -> None: ...

class STEConfigUtil:  # Class
    @staticmethod
    def WriteKeywords(configFile: str, value_: str) -> None: ...

class SignalHeader6890U:  # Class
    def __init__(self) -> None: ...

    HeaderSize: int
    HeaderVersion: int
    m_check: List[Agilent.MassSpectrometry.MSDChem.FileCheckStructU6890]
    m_signal: List[Agilent.MassSpectrometry.MSDChem.SignalInfoStruct6890]
    m_signalU: Agilent.MassSpectrometry.MSDChem.SignalScaleStructU6890

class SignalHeader7890U:  # Class
    def __init__(self) -> None: ...

    HeaderSize: int
    HeaderVersion: int
    m_check: List[Agilent.MassSpectrometry.MSDChem.FileCheckStructU7890]
    m_signal: List[Agilent.MassSpectrometry.MSDChem.SignalInfoStruct7890]
    m_signalU: Agilent.MassSpectrometry.MSDChem.SignalScaleStructU7890

class SignalInfoStruct5890:  # Class
    def __init__(self) -> None: ...

    BunchPower: int
    Detector: int
    Max: int
    Method: int
    Min: int
    PeakWidth: float
    Present: int
    Version: int
    WordAlign: int
    Zero: int

class SignalInfoStruct6890:  # Class
    def __init__(self) -> None: ...

    BunchPower: int
    Detector: int
    Max: int
    Method: int
    Min: int
    PeakWidth: float
    Present: int
    Version: int
    WordAlign: int
    Zero: float

class SignalInfoStruct7890:  # Class
    def __init__(self) -> None: ...

    BunchPower: int
    Detector: int
    Max: int
    Method: int
    Min: int
    PeakWidth: float
    Present: int
    Version: int
    WordAlign: int
    Zero: int

class SignalScaleStructU6890:  # Class
    def __init__(self) -> None: ...

    Intercept: float
    SIGDESCULEN: int = ...  # static # readonly
    SigDescrUStr: str
    Slope: float
    UNITSULEN: int = ...  # static # readonly
    UnitsUStr: str

class SignalScaleStructU7890:  # Class
    def __init__(self) -> None: ...

    Intercept: float
    SIGDESCULEN: int = ...  # static # readonly
    SigDescrUStr: str
    Slope: float
    UNITSULEN: int = ...  # static # readonly
    UnitsUStr: str

class SpectralRecordType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Capture: Agilent.MassSpectrometry.MSDChem.SpectralRecordType = (
        ...
    )  # static # readonly
    NormalScanSpectrum: Agilent.MassSpectrometry.MSDChem.SpectralRecordType = (
        ...
    )  # static # readonly
    ProfileScanSpectrum: Agilent.MassSpectrometry.MSDChem.SpectralRecordType = (
        ...
    )  # static # readonly
    Rawscan: Agilent.MassSpectrometry.MSDChem.SpectralRecordType = (
        ...
    )  # static # readonly
    SIMPlusScan_SIM: Agilent.MassSpectrometry.MSDChem.SpectralRecordType = (
        ...
    )  # static # readonly
    SIMPlusScan_Scan: Agilent.MassSpectrometry.MSDChem.SpectralRecordType = (
        ...
    )  # static # readonly
    SIMspectrum: Agilent.MassSpectrometry.MSDChem.SpectralRecordType = (
        ...
    )  # static # readonly
    SimRamp: Agilent.MassSpectrometry.MSDChem.SpectralRecordType = (
        ...
    )  # static # readonly
    TotalIon: Agilent.MassSpectrometry.MSDChem.SpectralRecordType = (
        ...
    )  # static # readonly

class UnsignedFloatEdit(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
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
    System.Windows.Forms.TextBox,
):  # Class
    def __init__(self) -> None: ...
    def SetLegalRange(self, dLow: float, dHigh: float) -> None: ...
    def SetNumberOfDecimalPlaces(self, nDecimal: int) -> None: ...

class VersionInfo:  # Class
    def __init__(self, App: str, Product: str) -> None: ...

    App: str
    BuildDate: str
    BuildNumber: str
    Copyright: str
    Product: str
    Release: str
    Version: str

    def BuildVersionString(self, exePath: str) -> None: ...

class WindowInfo:  # Class
    @overload
    def __init__(
        self, name: str, x: int, y: int, w: int, h: int, show: bool
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        location: System.Drawing.Point,
        size: System.Drawing.Size,
        show: bool,
    ) -> None: ...

    Height: int
    Location: System.Drawing.Point
    Name: str
    Size: System.Drawing.Size
    Visible: bool
    Width: int
    X: int
    Y: int

    def SetWindowInfo(self, strWindowInfoPath: str) -> None: ...
    def GetWindowInfo(self, strWindowInfoPath: str) -> None: ...

class XMLConfiguration:  # Class
    def SetConfiguredColor(
        self, instId: int, rstrValueName: str, dwRGB: int
    ) -> bool: ...
    def SetApplicationDWORD(
        self, rstrParentElementPath: str, rstrDWORDValueName: str, dwValue: int
    ) -> bool: ...
    def SetApplicationString(
        self, rstrParentElementPath: str, rstrStringValueName: str, rstrValue: str
    ) -> bool: ...
    def GetConfiguredColor(
        self, instId: int, rstrValueName: str, pdwRGB: int
    ) -> bool: ...
    def GetApplicationString(
        self,
        rstrParentElementPath: str,
        iParentPathOccurrenceIndex: int,
        rstrStringValueName: str,
        rstrValue: str,
    ) -> bool: ...
    def GetApplicationDWORD(
        self,
        rstrParentElementPath: str,
        iParentElementOccurrenceIndex: int,
        rstrDWORDValueName: str,
        pdwValue: int,
    ) -> bool: ...
    def InsertApplicationString(
        self,
        rstrParentElementPath: str,
        iParentElementOccurrenceIndex: int,
        rstrChildValueName: str,
        rstrValue: str,
    ) -> bool: ...

class dbg:  # Class
    @overload
    def __init__(self, source: str, minLevel: int) -> None: ...
    @overload
    def __init__(
        self, source: str, minLevel: int, enableConsoleOutput: bool
    ) -> None: ...

    EnableConsoleOutput: bool
    MinLevel: int
    Source: str

    def Flush(self) -> None: ...
    def BL(self, Level: int) -> None: ...
    @overload
    def PRT(self, Level: int, s: str) -> None: ...
    @overload
    def PRT(self, Level: int) -> None: ...

class fUNPACK_6890_STATE:  # Class
    def __init__(self) -> None: ...

    D2X: int
    InitTest: int
    dDX: float
    dDXold: float
    dScale: float
    dX: float
    dXold: float
    fGap: bool
    lHoleEndTime: int
    lHoleStartTime: int

class ic:  # Class
    def __init__(self) -> None: ...

    DEV_EDIT_ACTIVE: int = ...  # static # readonly
    DEV_EDIT_INACTIVE: int = ...  # static # readonly
    DEV_LOAD_ACTIVE: int = ...  # static # readonly
    DEV_LOAD_INACTIVE: int = ...  # static # readonly
    IC_ALS_7673: int = ...  # static # readonly
    IC_ALS_HS: int = ...  # static # readonly
    IC_ALS_NONE: int = ...  # static # readonly
    IC_ALS_PREP_AND_LOAD: int = ...  # static # readonly
    IC_GC_5890: int = ...  # static # readonly
    IC_GC_6850: int = ...  # static # readonly
    IC_GC_6890: int = ...  # static # readonly
    IC_GC_7810: int = ...  # static # readonly
    IC_GC_7820: int = ...  # static # readonly
    IC_GC_7890: int = ...  # static # readonly
    IC_GC_NONE: int = ...  # static # readonly
    IC_GC_OTHER: int = ...  # static # readonly
    IC_INSTALLED: int = ...  # static # readonly
    IC_MS_220: int = ...  # static # readonly
    IC_MS_240: int = ...  # static # readonly
    IC_MS_5971: int = ...  # static # readonly
    IC_MS_5972: int = ...  # static # readonly
    IC_MS_5973: int = ...  # static # readonly
    IC_MS_5974: int = ...  # static # readonly
    IC_MS_5975: int = ...  # static # readonly
    IC_MS_5976: int = ...  # static # readonly
    IC_MS_5977: int = ...  # static # readonly
    IC_MS_7000: int = ...  # static # readonly
    IC_MS_7200: int = ...  # static # readonly
    IC_MS_NONE: int = ...  # static # readonly
    IC_MS_TOF: int = ...  # static # readonly
    IC_NOT_INSTALLED: int = ...  # static # readonly
    IC_OFFLINE: int  # static
    IC_ONLINE: int  # static
    INJ_MODE_ALS: int = ...  # static # readonly
    INJ_MODE_AUTOMATIC: int = ...  # static # readonly
    INJ_MODE_AUX: int = ...  # static # readonly
    INJ_MODE_EXTERNAL: int = ...  # static # readonly
    INJ_MODE_HEADSPACE: int = ...  # static # readonly
    INJ_MODE_IMMEDIATE: int = ...  # static # readonly
    INJ_MODE_MANUAL: int = ...  # static # readonly
    INJ_MODE_MINI_THERMAL_DESORBER: int = ...  # static # readonly
    TOWER_TYPE_7683: int = ...  # static # readonly
    TOWER_TYPE_7693: int = ...  # static # readonly

    MSDCHEM_INI_FILE: str  # static # readonly

    @overload
    @staticmethod
    def GetInstrConfigString(
        InstrumentNumber: int, ItemId: Agilent.MassSpectrometry.MSDChem.InstConfigItem
    ) -> str: ...
    @overload
    @staticmethod
    def GetInstrConfigString(InstrumentNumber: int, strAdHocString: str) -> str: ...
    @staticmethod
    def GetGCIPAddress(InstPath: str, InstrumentNumber: int) -> str: ...
    @staticmethod
    def SetInstrConfig(
        InstrumentNumber: int,
        ItemId: Agilent.MassSpectrometry.MSDChem.InstConfigItem,
        strValue: str,
    ) -> int: ...
    @staticmethod
    def GetCustomerHome() -> str: ...
    @staticmethod
    def GetAvailableSources(
        i32InstrumentNumber: int, queriedSourceNames: Iterable[str]
    ) -> Dict[str, bool]: ...
    @staticmethod
    def GetInstrConfig(
        InstrumentNumber: int, ItemId: Agilent.MassSpectrometry.MSDChem.InstConfigItem
    ) -> int: ...
    @staticmethod
    def GetInstrumentPath(instrumentNumber: int) -> str: ...
    @staticmethod
    def IsConfigOnline(InstrumentNumber: int) -> bool: ...
    @staticmethod
    def GetMSIPAddress(InstrumentNumber: int) -> str: ...
    @staticmethod
    def GetApplicationConfigString(key: str) -> str: ...

    # Nested Types

    class InstrumentButtons(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        ALSDevice: Agilent.MassSpectrometry.MSDChem.ic.InstrumentButtons = (
            ...
        )  # static # readonly
        CTCDevice: Agilent.MassSpectrometry.MSDChem.ic.InstrumentButtons = (
            ...
        )  # static # readonly
        GCDevice: Agilent.MassSpectrometry.MSDChem.ic.InstrumentButtons = (
            ...
        )  # static # readonly
        HSDevice: Agilent.MassSpectrometry.MSDChem.ic.InstrumentButtons = (
            ...
        )  # static # readonly
        Inlet: Agilent.MassSpectrometry.MSDChem.ic.InstrumentButtons = (
            ...
        )  # static # readonly
        MSDevice: Agilent.MassSpectrometry.MSDChem.ic.InstrumentButtons = (
            ...
        )  # static # readonly
        MSTune: Agilent.MassSpectrometry.MSDChem.ic.InstrumentButtons = (
            ...
        )  # static # readonly
        Tools: Agilent.MassSpectrometry.MSDChem.ic.InstrumentButtons = (
            ...
        )  # static # readonly
        Vacuum: Agilent.MassSpectrometry.MSDChem.ic.InstrumentButtons = (
            ...
        )  # static # readonly

    class PressureUnits(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        Bar: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        ForelineBar: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        ForelineKiloPascal: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        ForelineMilliBar: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        ForelineMilliTorr: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        ForelinePascal: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        HighVacuumBar: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        HighVacuumKiloPascal: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        HighVacuumMilliBar: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        HighVacuumPascal: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        HighVacuumTorr: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        KiloPascal: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        MilliBar: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        MilliTorr: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        Pascal: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
        Torr: Agilent.MassSpectrometry.MSDChem.ic.PressureUnits = (
            ...
        )  # static # readonly
