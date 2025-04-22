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

from . import (
    CDBDataSetTableAdapters,
    DeviceType,
    IonizationMode,
    IonPolarity,
    MSScanType,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Compounds

class CDBCompoundsQuery:  # Class
    def __init__(self) -> None: ...

    Agilent_ID: int
    CASNumber: str
    ChemSpider_ID: str
    CompoundID: int
    CompoundName: str
    CreationDateTime: str
    Description: str
    Formula: str
    HMP_ID: str
    IUPACName: str
    KEGG_ID: str
    LMP_ID: str
    LastEditDateTime: str
    METLIN_ID: str
    Mass: float
    RetentionTime: float
    calculateMassDeltas: bool
    calculateRTDeltas: bool
    dynamicColumns: Dict[str, str]
    includeNullRTs: bool
    massTolerance: float
    massUnits: Agilent.MassSpectrometry.DataAnalysis.Compounds.MassUnits
    radicalSearchMode: Agilent.MassSpectrometry.DataAnalysis.Compounds.RadicalSearchMode
    retentionTimeTolerance: float

class CDBCompoundsRecord:  # Class
    def __init__(self) -> None: ...

    Agilent_ID: str
    Anion: bool
    CASNumber: str
    Cation: bool
    ChemSpider_ID: str
    CompoundId: int
    CompoundName: str
    CreationDateTime: System.DateTime
    Description: str
    Formula: str
    HMP_ID: str
    IUPACName: str
    KEGG_ID: str
    LMP_ID: str
    LastEditDateTime: System.DateTime
    METLIN_ID: str
    MOLFile: str
    Mass: float
    RetentionTime: float
    RetentionTimeUpdatedDateTime: System.DateTime

class CDBData(
    System.IDisposable, Agilent.MassSpectrometry.DataAnalysis.Compounds.DisposableBase
):  # Class
    def __init__(self) -> None: ...

    Database: str  # readonly

    @staticmethod
    def ValidLicense() -> bool: ...
    def GetInstrumentTypeEnumFromString(self, instrumentType: str) -> DeviceType: ...
    @staticmethod
    def IsDynamicSchemaSame(databaseFile1: str, databaseFile2: str) -> bool: ...
    def GetYValues(self, compoundID: int, spectrumID: int) -> str: ...
    def GetPolarityEnumFromString(self, polarity: str) -> IonPolarity: ...
    def UpdateDataSet(
        self, dataSet: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet
    ) -> bool: ...
    @overload
    def QueryRecords(
        self, sqlQueryString: str
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBCompoundsRecord]: ...
    @overload
    def QueryRecords(
        self,
        spectraQuery: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBSpectraQuery,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBSpectraRecord]: ...
    def GetCompoundsCount(self) -> int: ...
    def UpdateLibraryInfo(
        self, libInfo: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBLibraryInfo
    ) -> bool: ...
    def SetDatabase(self, dbFilePath: str) -> None: ...
    def QueryLibrary(
        self, cdbQuery: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery
    ) -> System.Data.DataSet: ...
    def GetSpectralPoints(
        self,
        compoundID: int,
        spectrumID: int,
        xValues: List[float],
        yValues: List[float],
    ) -> None: ...
    @overload
    def Initialize(self, databaseFolder: str, id: str) -> bool: ...
    @overload
    def Initialize(self, databaseFolder: str) -> bool: ...
    def GetIonModeEnumFromString(self, ionMode: str) -> IonizationMode: ...
    @overload
    def GetDatabaseInfo(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBLibraryInfo: ...
    @overload
    def GetDatabaseInfo(
        self, dbFile: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBLibraryInfo: ...
    @staticmethod
    def QueryNonResults(dbFileName: str, sqlQuery: str) -> None: ...
    def GetScanTypeEnumFromString(self, scanType: str) -> MSScanType: ...
    @overload
    def IsMaster(self, databaseName: str) -> bool: ...
    @overload
    def IsMaster(self) -> bool: ...
    def AddCompound(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow,
    ) -> bool: ...
    def QueryCompoundRecords(
        self,
        compoundsQuery: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBCompoundsQuery,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBCompoundsRecord]: ...
    @overload
    def IsReadOnly(self, databaseName: str) -> bool: ...
    @overload
    def IsReadOnly(self) -> bool: ...
    def QuerySpectraRecords(
        self, sqlQueryString: str
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBSpectraRecord]: ...
    @overload
    def Query(self, sqlQueryString: str) -> System.Data.DataSet: ...
    @overload
    def Query(
        self,
        compoundsQuery: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBCompoundsQuery,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet: ...
    @overload
    def Query(
        self,
        spectraQuery: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBSpectraQuery,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet: ...
    def AddSpectrum(
        self, row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow
    ) -> bool: ...
    def GetXValues(self, compoundID: int, spectrumID: int) -> str: ...
    def UpdateSpectralDataSet(
        self, dataSet: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet
    ) -> bool: ...

class CDBDataAccess(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.ComponentModel.Component,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, container: System.ComponentModel.IContainer) -> None: ...

class CDBDataSet(
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
    @overload
    def __init__(self, databaseFileName: str) -> None: ...
    @overload
    def __init__(self) -> None: ...

    Compounds: (
        Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsDataTable
    )  # readonly
    Library: (
        Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryDataTable
    )  # readonly
    Relations: System.Data.DataRelationCollection  # readonly
    SchemaSerializationMode: System.Data.SchemaSerializationMode
    Spectra: (
        Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraDataTable
    )  # readonly
    Tables: System.Data.DataTableCollection  # readonly

    @staticmethod
    def GetTypedDataSetSchema(
        xs: System.Xml.Schema.XmlSchemaSet,
    ) -> System.Xml.Schema.XmlSchemaComplexType: ...
    def GetDynamicAddedColumns(
        self, table: System.Data.DataTable
    ) -> System.Collections.Generic.List[System.Data.DataColumn]: ...
    def Clone(self) -> System.Data.DataSet: ...
    def GetDynamicRemovedColumns(
        self, table: System.Data.DataTable
    ) -> System.Collections.Generic.List[System.Data.DataColumn]: ...
    @staticmethod
    def GetSqlDBTypeFromType(type: System.Type) -> System.Data.SqlDbType: ...

    # Nested Types

    class CompoundsDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow
        ],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        Agilent_IDColumn: System.Data.DataColumn  # readonly
        AnionColumn: System.Data.DataColumn  # readonly
        BestFitColumn: System.Data.DataColumn  # readonly
        CASNumberColumn: System.Data.DataColumn  # readonly
        CationColumn: System.Data.DataColumn  # readonly
        ChemSpider_IDColumn: System.Data.DataColumn  # readonly
        CompoundIDColumn: System.Data.DataColumn  # readonly
        CompoundNameColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        CreationDateTimeColumn: System.Data.DataColumn  # readonly
        DeltaMassColumn: System.Data.DataColumn  # readonly
        DeltaRetentionTimeColumn: System.Data.DataColumn  # readonly
        DescriptionColumn: System.Data.DataColumn  # readonly
        FormulaColumn: System.Data.DataColumn  # readonly
        HMP_IDColumn: System.Data.DataColumn  # readonly
        IUPACNameColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow
        ): ...
        KEGG_IDColumn: System.Data.DataColumn  # readonly
        LMP_IDColumn: System.Data.DataColumn  # readonly
        LastEditDateTimeColumn: System.Data.DataColumn  # readonly
        METLIN_IDColumn: System.Data.DataColumn  # readonly
        MassColumn: System.Data.DataColumn  # readonly
        MassSubmittedColumn: System.Data.DataColumn  # readonly
        MolFileColumn: System.Data.DataColumn  # readonly
        NumSpectraColumn: System.Data.DataColumn  # readonly
        RTUpdatedTimeColumn: System.Data.DataColumn  # readonly
        RetentionIndexColumn: System.Data.DataColumn  # readonly
        RetentionTimeColumn: System.Data.DataColumn  # readonly
        RetentionTimeSubmittedColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemoveCompoundsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow,
        ) -> None: ...
        def Clone(self) -> System.Data.DataTable: ...
        def NewCompoundsRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow
        ): ...
        def FindByCompoundID(
            self, CompoundID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow
        ): ...
        @overload
        def AddCompoundsRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow,
        ) -> None: ...
        @overload
        def AddCompoundsRow(
            self,
            CompoundName: str,
            Description: str,
            Formula: str,
            Mass: float,
            RetentionTime: float,
            Cation: bool,
            Anion: bool,
            CASNumber: str,
            HMP_ID: str,
            KEGG_ID: str,
            LMP_ID: str,
            METLIN_ID: str,
            ChemSpider_ID: str,
            Agilent_ID: int,
            MolFile: str,
            IUPACName: str,
            CreationDateTime: System.DateTime,
            LastEditDateTime: System.DateTime,
            RTUpdatedTime: System.DateTime,
            MassSubmitted: float,
            DeltaMass: float,
            RetentionTimeSubmitted: float,
            DeltaRetentionTime: float,
            BestFit: bool,
            NumSpectra: int,
            RetentionIndex: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow
        ): ...

        CompoundsRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRowChangeEventHandler
        )  # Event
        CompoundsRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRowChangeEventHandler
        )  # Event
        CompoundsRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRowChangeEventHandler
        )  # Event
        CompoundsRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRowChangeEventHandler
        )  # Event

    class CompoundsRow(System.Data.DataRow):  # Class
        Agilent_ID: int
        Anion: bool
        BestFit: bool
        CASNumber: str
        Cation: bool
        ChemSpider_ID: str
        CompoundID: int
        CompoundName: str
        CreationDateTime: System.DateTime
        DeltaMass: float
        DeltaRetentionTime: float
        Description: str
        Formula: str
        HMP_ID: str
        IUPACName: str
        KEGG_ID: str
        LMP_ID: str
        LastEditDateTime: System.DateTime
        METLIN_ID: str
        Mass: float
        MassSubmitted: float
        MolFile: str
        NumSpectra: int
        RTUpdatedTime: System.DateTime
        RetentionIndex: float
        RetentionTime: float
        RetentionTimeSubmitted: float

        def IsIUPACNameNull(self) -> bool: ...
        def IsMassSubmittedNull(self) -> bool: ...
        def SetLMP_IDNull(self) -> None: ...
        def IsRetentionIndexNull(self) -> bool: ...
        def SetNumSpectraNull(self) -> None: ...
        def IsCationNull(self) -> bool: ...
        def IsAgilent_IDNull(self) -> bool: ...
        def IsAnionNull(self) -> bool: ...
        def IsLastEditDateTimeNull(self) -> bool: ...
        def SetAgilent_IDNull(self) -> None: ...
        def SetCationNull(self) -> None: ...
        def SetDeltaRetentionTimeNull(self) -> None: ...
        def IsRTUpdatedTimeNull(self) -> bool: ...
        def SetHMP_IDNull(self) -> None: ...
        def SetLastEditDateTimeNull(self) -> None: ...
        def SetMETLIN_IDNull(self) -> None: ...
        def SetMassSubmittedNull(self) -> None: ...
        def SetDeltaMassNull(self) -> None: ...
        def IsCreationDateTimeNull(self) -> bool: ...
        def SetFormulaNull(self) -> None: ...
        def SetBestFitNull(self) -> None: ...
        def IsRetentionTimeNull(self) -> bool: ...
        def IsFormulaNull(self) -> bool: ...
        def IsLMP_IDNull(self) -> bool: ...
        def SetMolFileNull(self) -> None: ...
        def IsDescriptionNull(self) -> bool: ...
        def SetIUPACNameNull(self) -> None: ...
        def SetRetentionTimeSubmittedNull(self) -> None: ...
        def SetRTUpdatedTimeNull(self) -> None: ...
        def SetRetentionIndexNull(self) -> None: ...
        def IsNumSpectraNull(self) -> bool: ...
        def IsHMP_IDNull(self) -> bool: ...
        def IsMETLIN_IDNull(self) -> bool: ...
        def IsMolFileNull(self) -> bool: ...
        def IsDeltaRetentionTimeNull(self) -> bool: ...
        def SetRetentionTimeNull(self) -> None: ...
        def SetDescriptionNull(self) -> None: ...
        def IsCompoundNameNull(self) -> bool: ...
        def IsDeltaMassNull(self) -> bool: ...
        def IsCASNumberNull(self) -> bool: ...
        def SetKEGG_IDNull(self) -> None: ...
        def SetAnionNull(self) -> None: ...
        def SetCompoundNameNull(self) -> None: ...
        def SetChemSpider_IDNull(self) -> None: ...
        def IsKEGG_IDNull(self) -> bool: ...
        def SetCASNumberNull(self) -> None: ...
        def SetCreationDateTimeNull(self) -> None: ...
        def IsChemSpider_IDNull(self) -> bool: ...
        def IsRetentionTimeSubmittedNull(self) -> bool: ...
        def IsBestFitNull(self) -> bool: ...

    class CompoundsRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRow
        )  # readonly

    class CompoundsRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.CompoundsRowChangeEvent,
        ) -> None: ...

    class LibraryDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRow],
        System.ComponentModel.IComponent,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRow
        ],
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        Count: int  # readonly
        CreationDateTimeColumn: System.Data.DataColumn  # readonly
        DescriptionColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRow: ...
        LastEditDateTimeColumn: System.Data.DataColumn  # readonly
        LibraryIDColumn: System.Data.DataColumn  # readonly
        LibraryNameColumn: System.Data.DataColumn  # readonly
        LibrarySourceColumn: System.Data.DataColumn  # readonly
        LibrarySourceVersionColumn: System.Data.DataColumn  # readonly
        LibraryTypeColumn: System.Data.DataColumn  # readonly
        LibraryVersionMajorColumn: System.Data.DataColumn  # readonly
        LibraryVersionMinorColumn: System.Data.DataColumn  # readonly
        MasterColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewLibraryRow(
            self,
        ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRow: ...
        def FindByLibraryID(
            self, LibraryID: int
        ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRow: ...
        @overload
        def AddLibraryRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRow,
        ) -> None: ...
        @overload
        def AddLibraryRow(
            self,
            LibraryName: str,
            LibraryType: str,
            Description: str,
            LibrarySource: str,
            LibrarySourceVersion: str,
            LibraryVersionMajor: int,
            LibraryVersionMinor: int,
            Master: bool,
            CreationDateTime: System.DateTime,
            LastEditDateTime: System.DateTime,
        ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRow: ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveLibraryRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRow,
        ) -> None: ...

        LibraryRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRowChangeEventHandler
        )  # Event
        LibraryRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRowChangeEventHandler
        )  # Event
        LibraryRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRowChangeEventHandler
        )  # Event
        LibraryRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRowChangeEventHandler
        )  # Event

    class LibraryRow(System.Data.DataRow):  # Class
        CreationDateTime: System.DateTime
        Description: str
        LastEditDateTime: System.DateTime
        LibraryID: int
        LibraryName: str
        LibrarySource: str
        LibrarySourceVersion: str
        LibraryType: str
        LibraryVersionMajor: int
        LibraryVersionMinor: int
        Master: bool

        def SetCreationDateTimeNull(self) -> None: ...
        def SetDescriptionNull(self) -> None: ...
        def SetLibraryVersionMinorNull(self) -> None: ...
        def IsLibraryNameNull(self) -> bool: ...
        def SetLibraryVersionMajorNull(self) -> None: ...
        def IsLibraryTypeNull(self) -> bool: ...
        def SetMasterNull(self) -> None: ...
        def IsLibraryVersionMajorNull(self) -> bool: ...
        def SetLibrarySourceNull(self) -> None: ...
        def SetLibrarySourceVersionNull(self) -> None: ...
        def SetLastEditDateTimeNull(self) -> None: ...
        def IsLibrarySourceVersionNull(self) -> bool: ...
        def IsLibraryVersionMinorNull(self) -> bool: ...
        def IsCreationDateTimeNull(self) -> bool: ...
        def SetLibraryTypeNull(self) -> None: ...
        def IsDescriptionNull(self) -> bool: ...
        def IsLastEditDateTimeNull(self) -> bool: ...
        def IsLibrarySourceNull(self) -> bool: ...
        def SetLibraryNameNull(self) -> None: ...
        def IsMasterNull(self) -> bool: ...

    class LibraryRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRow
        )  # readonly

    class LibraryRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.LibraryRowChangeEvent,
        ) -> None: ...

    class SpectraDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow
        ],
        Iterable[Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AbundanceValuesColumn: System.Data.DataColumn  # readonly
        CollisionEnergyColumn: System.Data.DataColumn  # readonly
        CompoundIDColumn: System.Data.DataColumn  # readonly
        CompoundNameColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        CreationDateTimeColumn: System.Data.DataColumn  # readonly
        FragmentorColumn: System.Data.DataColumn  # readonly
        HighestMzColumn: System.Data.DataColumn  # readonly
        InstrumentTypeColumn: System.Data.DataColumn  # readonly
        IonModeColumn: System.Data.DataColumn  # readonly
        IonPolarityColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow: ...
        LastEditDateTimeColumn: System.Data.DataColumn  # readonly
        LowestMzColumn: System.Data.DataColumn  # readonly
        MSLevelColumn: System.Data.DataColumn  # readonly
        MzValuesColumn: System.Data.DataColumn  # readonly
        ScanTypeColumn: System.Data.DataColumn  # readonly
        SelectedMzColumn: System.Data.DataColumn  # readonly
        SpeciesColumn: System.Data.DataColumn  # readonly
        SpectrumIDColumn: System.Data.DataColumn  # readonly

        def NewSpectraRow(
            self,
        ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddSpectraRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow,
        ) -> None: ...
        @overload
        def AddSpectraRow(
            self,
            CompoundID: int,
            CompoundName: str,
            MzValues: str,
            AbundanceValues: str,
            SelectedMz: float,
            LowestMz: float,
            HighestMz: float,
            CollisionEnergy: float,
            Fragmentor: float,
            InstrumentType: str,
            IonPolarity: str,
            IonMode: str,
            MSLevel: int,
            ScanType: str,
            CreationDateTime: System.DateTime,
            LastEditDateTime: System.DateTime,
            Species: str,
        ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow: ...
        def Clone(self) -> System.Data.DataTable: ...
        def FindByCompoundIDSpectrumID(
            self, CompoundID: int, SpectrumID: int
        ) -> Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow: ...
        def RemoveSpectraRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow,
        ) -> None: ...

        SpectraRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRowChangeEventHandler
        )  # Event
        SpectraRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRowChangeEventHandler
        )  # Event
        SpectraRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRowChangeEventHandler
        )  # Event
        SpectraRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRowChangeEventHandler
        )  # Event

    class SpectraRow(System.Data.DataRow):  # Class
        AbundanceValues: str
        CollisionEnergy: float
        CompoundID: int
        CompoundName: str
        CreationDateTime: System.DateTime
        Fragmentor: float
        HighestMz: float
        InstrumentType: str
        IonMode: str
        IonPolarity: str
        LastEditDateTime: System.DateTime
        LowestMz: float
        MSLevel: int
        MzValues: str
        ScanType: str
        SelectedMz: float
        Species: str
        SpectrumID: int

        def SetLowestMzNull(self) -> None: ...
        def IsAbundanceValuesNull(self) -> bool: ...
        def SetSpeciesNull(self) -> None: ...
        def IsLastEditDateTimeNull(self) -> bool: ...
        def IsScanTypeNull(self) -> bool: ...
        def IsIonModeNull(self) -> bool: ...
        def SetLastEditDateTimeNull(self) -> None: ...
        def IsCreationDateTimeNull(self) -> bool: ...
        def SetAbundanceValuesNull(self) -> None: ...
        def SetIonPolarityNull(self) -> None: ...
        def IsMzValuesNull(self) -> bool: ...
        def IsLowestMzNull(self) -> bool: ...
        def IsIonPolarityNull(self) -> bool: ...
        def IsCollisionEnergyNull(self) -> bool: ...
        def IsFragmentorNull(self) -> bool: ...
        def SetHighestMzNull(self) -> None: ...
        def IsMSLevelNull(self) -> bool: ...
        def IsInstrumentTypeNull(self) -> bool: ...
        def IsSelectedMzNull(self) -> bool: ...
        def IsCompoundNameNull(self) -> bool: ...
        def SetSelectedMzNull(self) -> None: ...
        def SetInstrumentTypeNull(self) -> None: ...
        def SetScanTypeNull(self) -> None: ...
        def SetMzValuesNull(self) -> None: ...
        def IsHighestMzNull(self) -> bool: ...
        def SetCollisionEnergyNull(self) -> None: ...
        def SetMSLevelNull(self) -> None: ...
        def SetIonModeNull(self) -> None: ...
        def SetCompoundNameNull(self) -> None: ...
        def SetFragmentorNull(self) -> None: ...
        def SetCreationDateTimeNull(self) -> None: ...
        def IsSpeciesNull(self) -> bool: ...

    class SpectraRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRow
        )  # readonly

    class SpectraRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSet.SpectraRowChangeEvent,
        ) -> None: ...

class CDBLibraryInfo:  # Class
    def __init__(self) -> None: ...

    CreationDateTime: System.DateTime
    Description: str
    LastEditDateTime: System.DateTime
    LibraryID: int
    LibraryName: str
    LibrarySource: str
    LibrarySourceVersion: str
    LibraryType: str
    LibraryVersionMajor: int
    LibraryVersionMinor: int
    Master: bool

class CDBQuery:  # Class
    def __init__(self) -> None: ...

    m_queryParts: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBQueryPart
    ]

    def AddCondition(
        self,
        field: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField,
        options: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBCompare,
        value_: Any,
    ) -> None: ...

    # Nested Types

    class CDBCompare(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        Contains: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBCompare
        ) = ...  # static # readonly
        Equals: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBCompare = (
            ...
        )  # static # readonly
        GreaterThan: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBCompare
        ) = ...  # static # readonly
        LessThan: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBCompare
        ) = ...  # static # readonly
        Not: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBCompare = (
            ...
        )  # static # readonly

    class CDBField(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        AbundanceValues: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        Agilent_ID: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        CASNumber: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        ChemSpider_ID: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        CollisionEnergy: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        CompoundID: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        CompoundName: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        CompoundSpecID: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        CreationDateTime: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        Description: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        Formula: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        Fragmentor: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        HMP_ID: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        HighestMz: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        IUPACName: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        IncludeCompounds: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        IncludeSpectra: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        InstrumentType: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        IonMode: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        IonPolarity: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        KEGG_ID: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        LMP_ID: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        LastEditDateTime: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        LowestMz: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        METLIN_ID: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        Mass: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        MolFile: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        MsLevel: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        MzValues: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        RadicalSearchMode: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        RetentionTime: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        ScanType: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        SelectedMz: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        SpecCreationDateTime: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        SpecLastEditDateTime: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly
        Species: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField = (
            ...
        )  # static # readonly
        SpectrumID: (
            Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        ) = ...  # static # readonly

    class CDBQueryPart:  # Class
        def __init__(self) -> None: ...

        condition: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBCompare
        field: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBQuery.CDBField
        value: Any

class CDBSpectraQuery:  # Class
    def __init__(self) -> None: ...

    CollisionEnergy: float
    CompoundID: int
    CreationDateTime: str
    Fragmentor: float
    InstrumentType: DeviceType
    IonMode: IonizationMode
    IonPolarity: IonPolarity
    LastEditDateTime: str
    MSLevel: int
    ScanType: MSScanType
    SelectedMz: float
    SpectrumID: int
    ceTolerance: float
    dynamicColumns: Dict[str, str]
    massTolerance: float
    massUnits: Agilent.MassSpectrometry.DataAnalysis.Compounds.MassUnits

class CDBSpectraRecord:  # Class
    def __init__(self) -> None: ...

    AbundanceValues: str
    CollisionEnergy: float
    CompoundId: int
    CreationDateTime: System.DateTime
    Fragmentor: float
    HighestMz: float
    InstrumentType: str
    IonMode: str
    IonPolarity: str
    LastEditDateTime: System.DateTime
    LowestMz: float
    MSLevel: int
    MzValues: str
    ScanType: str
    SelectedMz: float
    Species: str
    SpectrumId: int

class DisposableBase(System.IDisposable):  # Class
    def Dispose(self) -> None: ...

class MassUnits(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    mDa: Agilent.MassSpectrometry.DataAnalysis.Compounds.MassUnits = (
        ...
    )  # static # readonly
    ppm: Agilent.MassSpectrometry.DataAnalysis.Compounds.MassUnits = (
        ...
    )  # static # readonly

class RadicalSearchMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    IncludeAnions: Agilent.MassSpectrometry.DataAnalysis.Compounds.RadicalSearchMode = (
        ...
    )  # static # readonly
    IncludeCations: (
        Agilent.MassSpectrometry.DataAnalysis.Compounds.RadicalSearchMode
    ) = ...  # static # readonly
    IncludeEverything: (
        Agilent.MassSpectrometry.DataAnalysis.Compounds.RadicalSearchMode
    ) = ...  # static # readonly
    IncludeNeutrals: (
        Agilent.MassSpectrometry.DataAnalysis.Compounds.RadicalSearchMode
    ) = ...  # static # readonly
    NotSpecified: Agilent.MassSpectrometry.DataAnalysis.Compounds.RadicalSearchMode = (
        ...
    )  # static # readonly
