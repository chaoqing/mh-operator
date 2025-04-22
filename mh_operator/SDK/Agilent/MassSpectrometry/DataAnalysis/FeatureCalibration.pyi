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

from . import CandidateHit, Component, LibraryCompoundInfo
from .FD import Feature, IFeatureSet, IScanSpace, ScanAxis
from .FeatureDataAccess import TofFeatureDataAccess

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration

class BestFitCriterionType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    BIC: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.BestFitCriterionType
    ) = ...  # static # readonly
    MinRmsResidual: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.BestFitCriterionType
    ) = ...  # static # readonly

class CalRefCompoundSet(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Alkanes: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefCompoundSet
    ) = ...  # static # readonly
    All: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefCompoundSet = (
        ...
    )  # static # readonly
    CycloSiloxanes: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefCompoundSet
    ) = ...  # static # readonly
    FAMEs: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefCompoundSet
    ) = ...  # static # readonly
    LinearSiloxanes: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefCompoundSet
    ) = ...  # static # readonly
    Matrix: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefCompoundSet
    ) = ...  # static # readonly

class CalRefDataSet(
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

    CalibrationCompound: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundDataTable
    )  # readonly
    CompoundReferenceIon: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonDataTable
    )  # readonly
    ReferenceIon: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonDataTable
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

    class CalibrationCompoundDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
        ],
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        CASNumberColumn: System.Data.DataColumn  # readonly
        CompoundIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FormulaColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
        ): ...
        LadderColumn: System.Data.DataColumn  # readonly
        LadderStepColumn: System.Data.DataColumn  # readonly
        NameColumn: System.Data.DataColumn  # readonly
        RetentionIndexColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddCalibrationCompoundRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow,
        ) -> None: ...
        @overload
        def AddCalibrationCompoundRow(
            self,
            CompoundID: int,
            CASNumber: str,
            Formula: str,
            Ladder: str,
            LadderStep: str,
            Name: str,
            RetentionIndex: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveCalibrationCompoundRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow,
        ) -> None: ...
        def NewCalibrationCompoundRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
        ): ...
        def FindByCompoundID(
            self, CompoundID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
        ): ...

        CalibrationCompoundRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRowChangeEventHandler
        )  # Event
        CalibrationCompoundRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRowChangeEventHandler
        )  # Event
        CalibrationCompoundRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRowChangeEventHandler
        )  # Event
        CalibrationCompoundRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRowChangeEventHandler
        )  # Event

    class CalibrationCompoundRow(System.Data.DataRow):  # Class
        CASNumber: str
        CompoundID: int
        Formula: str
        Ladder: str
        LadderStep: str
        Name: str
        RetentionIndex: float

        def SetLadderNull(self) -> None: ...
        def IsCASNumberNull(self) -> bool: ...
        def IsNameNull(self) -> bool: ...
        def IsLadderNull(self) -> bool: ...
        def SetLadderStepNull(self) -> None: ...
        def IsFormulaNull(self) -> bool: ...
        def GetCompoundReferenceIonRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow
        ]: ...
        def IsLadderStepNull(self) -> bool: ...
        def SetNameNull(self) -> None: ...
        def SetFormulaNull(self) -> None: ...
        def SetRetentionIndexNull(self) -> None: ...
        def SetCASNumberNull(self) -> None: ...
        def IsRetentionIndexNull(self) -> bool: ...

    class CalibrationCompoundRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
        )  # readonly

    class CalibrationCompoundRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRowChangeEvent,
        ) -> None: ...

    class CompoundReferenceIonDataTable(
        System.IServiceProvider,
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow
        ],
    ):  # Class
        def __init__(self) -> None: ...

        CompoundIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow
        ): ...
        ReferenceIonIDColumn: System.Data.DataColumn  # readonly
        RelativeAbundanceColumn: System.Data.DataColumn  # readonly

        @overload
        def AddCompoundReferenceIonRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow,
        ) -> None: ...
        @overload
        def AddCompoundReferenceIonRow(
            self,
            parentCalibrationCompoundRowByFK_CalibrationCompound_CompoundReferenceIon: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow,
            parentReferenceIonRowByFK_ReferenceIon_CompoundReferenceIon: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow,
            RelativeAbundance: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewCompoundReferenceIonRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow
        ): ...
        def RemoveCompoundReferenceIonRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow,
        ) -> None: ...
        def Clone(self) -> System.Data.DataTable: ...
        def FindByCompoundIDReferenceIonID(
            self, CompoundID: int, ReferenceIonID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow
        ): ...

        CompoundReferenceIonRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRowChangeEventHandler
        )  # Event
        CompoundReferenceIonRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRowChangeEventHandler
        )  # Event
        CompoundReferenceIonRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRowChangeEventHandler
        )  # Event
        CompoundReferenceIonRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRowChangeEventHandler
        )  # Event

    class CompoundReferenceIonRow(System.Data.DataRow):  # Class
        CalibrationCompoundRow: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
        )
        CompoundID: int
        ReferenceIonID: int
        ReferenceIonRow: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow
        )
        RelativeAbundance: float

        def IsRelativeAbundanceNull(self) -> bool: ...
        def SetRelativeAbundanceNull(self) -> None: ...

    class CompoundReferenceIonRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow
        )  # readonly

    class CompoundReferenceIonRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRowChangeEvent,
        ) -> None: ...

    class ReferenceIonDataTable(
        System.IServiceProvider,
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow
        ],
    ):  # Class
        def __init__(self) -> None: ...

        Count: int  # readonly
        ExactMassEIColumn: System.Data.DataColumn  # readonly
        FormulaColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow
        ): ...
        ReferenceIonIDColumn: System.Data.DataColumn  # readonly

        @overload
        def AddReferenceIonRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow,
        ) -> None: ...
        @overload
        def AddReferenceIonRow(
            self, ReferenceIonID: int, ExactMassEI: float, Formula: str
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewReferenceIonRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow
        ): ...
        def FindByReferenceIonID(
            self, ReferenceIonID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveReferenceIonRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow,
        ) -> None: ...

        ReferenceIonRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRowChangeEventHandler
        )  # Event
        ReferenceIonRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRowChangeEventHandler
        )  # Event
        ReferenceIonRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRowChangeEventHandler
        )  # Event
        ReferenceIonRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRowChangeEventHandler
        )  # Event

    class ReferenceIonRow(System.Data.DataRow):  # Class
        ExactMassEI: float
        Formula: str
        ReferenceIonID: int

        def IsExactMassEINull(self) -> bool: ...
        def IsFormulaNull(self) -> bool: ...
        def GetCompoundReferenceIonRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CompoundReferenceIonRow
        ]: ...
        def SetFormulaNull(self) -> None: ...
        def SetExactMassEINull(self) -> None: ...

    class ReferenceIonRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow
        )  # readonly

    class ReferenceIonRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRowChangeEvent,
        ) -> None: ...

class CalibrationReferenceDB:  # Class
    def __init__(self) -> None: ...
    def GetCompoundByCASNumber(
        self, casNumber: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
    ): ...
    @overload
    def Open(self, dataSourcePath: str) -> None: ...
    @overload
    def Open(
        self,
        calRefCompoundSet: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefCompoundSet,
    ) -> None: ...
    @overload
    def Open(self, dataSourcePaths: List[str]) -> None: ...

class DynamicCalibrationParams:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, xmlFilePath: str) -> None: ...
    @overload
    def __init__(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.DynamicCalibrationParams,
    ) -> None: ...

    PARAMETER_FILE: str = ...  # static # readonly

    ApplyMassCalToFeatures: bool
    BestFitCriterion: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.BestFitCriterionType
    )
    CalRefCompoundSet: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefCompoundSet
    )
    MassCalRTInterpolationType: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.MassCalRTInterpolationType
    )
    MaxInversePower: int
    MaxPolynomialOrder: int
    MaxResolvingPower: float
    MinComponentQuality: float
    MinIonMatchCount: int
    MinMatchScore: float
    MinPolynomialOrder: int
    MzTolerancePpm: float
    RModelRolloverMzScale: float
    RefLibraryPath: str
    WindowSizeFactorsForDeconvolution: List[float]

    def Equals(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.DynamicCalibrationParams,
    ) -> bool: ...
    def Clone(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.DynamicCalibrationParams
    ): ...

class FeatureCalibrator:  # Class
    def __init__(
        self, dataAccess: TofFeatureDataAccess, featureSet: IFeatureSet
    ) -> None: ...
    def Run(self) -> None: ...

class FeatureMassCalibrationRecord:  # Class
    def __init__(
        self,
        refCompoundMatch: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceCompoundMatch,
        refIonMatches: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceIonMatch
        ],
        dcParams: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.DynamicCalibrationParams,
    ) -> None: ...

    CalibrationCompound: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
    )  # readonly
    IdentifiedComponent: Component  # readonly
    IonMatchList: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceIonMatch
    ]  # readonly
    MassCalFit: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.MassCalibrationFit
    )  # readonly
    NIons: int  # readonly
    ReferenceCompoundMatch: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceCompoundMatch
    )  # readonly
    RetentionTime: float  # readonly

    def FindOptimalFit(
        self,
        ftAxis: ScanAxis,
        rModel: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ResolvingPowerModel,
    ) -> None: ...

class FeatureMassTimeCalibration:  # Class
    def __init__(
        self,
        scanSpace: IScanSpace,
        dcParams: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.DynamicCalibrationParams,
    ) -> None: ...

    NRecords: int  # readonly

    def AddMassTimeCalRecord(
        self,
        massCalRecord: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.FeatureMassCalibrationRecord,
    ) -> None: ...
    def CompleteCalibration(self, featureSet: IFeatureSet) -> None: ...
    def GetMassForFeature(self, f: Feature) -> float: ...

class GlobalAverageMassCal:  # Class
    def __init__(
        self,
        parent: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.FeatureMassTimeCalibration,
        ftAxis: ScanAxis,
        rModel: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ResolvingPowerModel,
    ) -> None: ...
    def GetMassCorrection(self, mz: float) -> float: ...
    def Run(
        self,
        calRecords: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.FeatureMassCalibrationRecord
        ],
        polynomialOrder: int,
        maxInversePower: int,
    ) -> None: ...

class MassCalRTInterpolationType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    GlobalAverage: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.MassCalRTInterpolationType
    ) = ...  # static # readonly
    Linear: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.MassCalRTInterpolationType
    ) = ...  # static # readonly
    NearestPoint: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.MassCalRTInterpolationType
    ) = ...  # static # readonly
    Quadratic: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.MassCalRTInterpolationType
    ) = ...  # static # readonly

class MassCalibrationFit:  # Class
    def __init__(
        self,
        mzRef: List[float],
        flightTimes: List[float],
        flightTimeAxis: ScanAxis,
        rModel: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ResolvingPowerModel,
    ) -> None: ...

    BestResidualFit: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.MassCalibrationFitStep
    )  # readonly
    MaxInversePower: int  # readonly
    NIons: int  # readonly
    ParabolicFit: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.MassCalibrationFitStep
    )  # readonly
    PolynomialOrder: int  # readonly
    RmsTotalResidualPpm: float  # readonly
    TotalResiduals: List[float]  # readonly
    TotalResidualsPpm: List[float]  # readonly

    def IsFlightTimeInRange(self, flightTime: float) -> bool: ...
    def ConvertTimeToMass(self, flightTime: float) -> float: ...
    def FindBestFit(
        self,
        bestFitCriterion: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.BestFitCriterionType,
        minPolynomialOrder: int,
        maxPolynomialOrder: int,
        maxInversePower: int,
    ) -> None: ...

class MassCalibrationFitStep:  # Class
    def __init__(
        self,
        mz: List[float],
        mzRef: List[float],
        flightTimes: List[float],
        flightTimeAxis: ScanAxis,
        polynomialOrder: int,
        nInversePowers: int,
        rModel: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ResolvingPowerModel,
    ) -> None: ...

    BayesianInformationCriterion: float  # readonly
    ChiSquare: float  # readonly
    Coefficients: List[float]  # readonly
    MaxInversePower: int  # readonly
    PolynomialOrder: int  # readonly
    Residuals: List[float]  # readonly
    ResidualsPpm: List[float]  # readonly
    RmsResidualPpm: float  # readonly

    def ConvertTimeToMass(self, flightTime: float) -> float: ...
    def DoFit(self) -> None: ...

class MassResidualFit:  # Class
    def __init__(
        self,
        mzMeasured: List[float],
        mzRef: List[float],
        polynomialOrder: int,
        nInversePowers: int,
        rModel: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ResolvingPowerModel,
    ) -> None: ...

    BayesianInformationCriterion: float  # readonly
    ChiSquare: float  # readonly
    Coefficients: List[float]  # readonly
    MaxInversePower: int  # readonly
    MzDelta: List[float]  # readonly
    MzDeltaFit: List[float]  # readonly
    MzDeltaFitPpm: List[float]  # readonly
    MzDeltaPpm: List[float]  # readonly
    PolynomialOrder: int  # readonly
    Residuals: List[float]  # readonly
    ResidualsPpm: List[float]  # readonly
    RmsResidualPpm: float  # readonly

    def GetMassCorrection(self, mz: float) -> float: ...
    def DoFit(self) -> None: ...

class RTCal:  # Class
    def __init__(
        self,
        _calRecords: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.FeatureMassCalibrationRecord
        ],
    ) -> None: ...

class ReferenceCompoundMatch:  # Class
    def __init__(
        self,
        refCompound: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow,
        component: Component,
        hit: CandidateHit,
        compoundInfo: LibraryCompoundInfo,
        ladderType: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefCompoundSet,
    ) -> None: ...

    CalibrationCompound: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.CalibrationCompoundRow
    )  # readonly
    IdentifiedComponent: Component  # readonly
    LadderType: (
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefCompoundSet
    )  # readonly
    LibraryHit: CandidateHit  # readonly

    def GetReferenceIonMatches(
        self, featureSet: IFeatureSet, mzTolerancePpm: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceIonMatch
    ]: ...

    # Nested Types

    class RTComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceCompoundMatch
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceCompoundMatch,
            b: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceCompoundMatch,
        ) -> int: ...

class ReferenceIonMatch:  # Class
    def __init__(
        self,
        refIon: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.CalRefDataSet.ReferenceIonRow,
        feature: Feature,
    ) -> None: ...

    Abundance: float  # readonly
    ExactMassEI: float  # readonly
    MeasuredFlightTime: float  # readonly
    MeasuredMz: float  # readonly

    # Nested Types

    class MzComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceIonMatch
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            a: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceIonMatch,
            b: Agilent.MassSpectrometry.DataAnalysis.FeatureCalibration.ReferenceIonMatch,
        ) -> int: ...

class ResolvingPowerModel:  # Class
    def __init__(self, r0: float, mz0: float) -> None: ...

    Mz0: float  # readonly
    R0: float  # readonly

    def GetMassResolutionSquared(self, mz: float) -> float: ...
    def GetResolvingPowerSquared(self, mz: float) -> float: ...
    def GetResolvingPower(self, mz: float) -> float: ...
    def GetMassResolution(self, mz: float) -> float: ...
