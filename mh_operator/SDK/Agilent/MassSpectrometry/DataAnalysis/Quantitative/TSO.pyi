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

from . import AcquisitionMethod, AppCommandContext, MethodSetupSession

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO

class AcqMethodGenerator:  # Class
    def __init__(
        self,
        context: AppCommandContext,
        acqMethod: AcquisitionMethod,
        peaksNotFound: List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow
        ],
    ) -> None: ...

    OptimizedAcqMethodXml: System.Xml.XmlDocument  # readonly
    UnoptimizedAcqMethod: AcquisitionMethod  # readonly

    @overload
    def SaveAcqMethodXml(self, dirPath: str) -> None: ...
    @overload
    def SaveAcqMethodXml(self, dirPath: str, fileName: str) -> None: ...
    def CreateOptimizedAcqMethod(
        self,
        ods: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet,
    ) -> System.Xml.XmlDocument: ...

class AcquiredTransitionTable:  # Class
    PeaksNotFound: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow
    ]  # readonly

class AutoSIMParams(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.CompoundListTSOptimizerParams
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        claParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.CompoundListTSOptimizerParams,
    ) -> None: ...

    DEFAULT_CYCLES_PER_SECOND: float = ...  # static # readonly
    DEFAULT_MAX_DWELL_TIME: float = ...  # static # readonly
    DEFAULT_MEDIAN_DWELL_TIME: float = ...  # static # readonly
    DEFAULT_MIN_DWELL_TIME: float = ...  # static # readonly
    DEFAULT_USE_CONSTANT_CYCLE_TIME: bool = ...  # static # readonly
    DEFAULT_USE_EQUAL_DWELL_TIMES: bool = ...  # static # readonly
    XML_PARAM_FILE: str = ...  # static # readonly

    MaxDwellTime: float
    MinDwellTime: float

    def UseDefaults(self) -> None: ...
    @overload
    def Write(self) -> None: ...
    @overload
    def Write(self, fileName: str) -> None: ...

class BoundaryCostScale(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Log10_0: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.BoundaryCostScale
    ) = ...  # static # readonly
    Log10_1: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.BoundaryCostScale
    ) = ...  # static # readonly
    Log10_2: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.BoundaryCostScale
    ) = ...  # static # readonly
    Log10_3: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.BoundaryCostScale
    ) = ...  # static # readonly
    Log10_4: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.BoundaryCostScale
    ) = ...  # static # readonly
    Log10_5: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.BoundaryCostScale
    ) = ...  # static # readonly
    Log10_6: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.BoundaryCostScale
    ) = ...  # static # readonly

class CompoundListTSOptimizer:  # Class
    @overload
    def __init__(
        self,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet,
    ) -> None: ...
    @overload
    def __init__(
        self,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet,
        userParams: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.CompoundListTSOptimizerParams,
    ) -> None: ...

    MaxTimeSegments: int
    MinPointsPerTimeSegment: int  # readonly
    TransitionTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.AcquiredTransitionTable
    )  # readonly

    def RunOptimization(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet
    ): ...
    def RunOptimizationImpl(self) -> None: ...

class CompoundListTSOptimizerParams:  # Class
    def __init__(self) -> None: ...

    DEFAULT_CYCLE_TIME: float = ...  # static # readonly
    DEFAULT_DWELL_TIME: float = ...  # static # readonly

    CyclesPerSecond: float
    DwellTime: float
    EqualDwellTimes: bool
    RemoveDuplicateTransitions: bool
    UseConstantCycleTime: bool

class ExcelInputColumns(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CE: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns = (
        ...
    )  # static # readonly
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns
    ) = ...  # static # readonly
    Dwell: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns = (
        ...
    )  # static # readonly
    FV: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns = (
        ...
    )  # static # readonly
    ISTD: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns = (
        ...
    )  # static # readonly
    MS1_Res: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns
    ) = ...  # static # readonly
    MS2_Res: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns
    ) = ...  # static # readonly
    Polarity: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns
    ) = ...  # static # readonly
    Precursor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns
    ) = ...  # static # readonly
    Product: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns
    ) = ...  # static # readonly
    RT: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns = (
        ...
    )  # static # readonly
    RTWindow: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns
    ) = ...  # static # readonly
    Reference: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.ExcelInputColumns
    ) = ...  # static # readonly

class ExcelInputDataReader:  # Class
    def __init__(self) -> None: ...

    COLUMN_NAMES: List[str]  # static # readonly

    DataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet
    )  # readonly

    def Read(self, inputFilePath: str, worksheetName: str) -> None: ...

class Function1D(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> float: ...
    def BeginInvoke(
        self, x: float, callback: System.AsyncCallback, object: Any
    ) -> System.IAsyncResult: ...
    def Invoke(self, x: float) -> float: ...

class FunctionGradientND(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        x: List[float],
        df: List[float],
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, x: List[float], df: List[float]) -> None: ...

class FunctionND(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> float: ...
    def BeginInvoke(
        self, x: List[float], callback: System.AsyncCallback, object: Any
    ) -> System.IAsyncResult: ...
    def Invoke(self, x: List[float]) -> float: ...

class NDimOptimization:  # Class
    def __init__(
        self,
        func: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.FunctionND,
        dfunc: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.FunctionGradientND,
        nDim: int,
    ) -> None: ...
    def GoldenSectionSearch(
        self,
        func: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.Function1D,
        a: float,
        b: float,
        c: float,
        tolerance: float,
        xmin: float,
    ) -> float: ...
    def MinimizeFunctionAlongLine(
        self,
        f1dim: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.Function1D,
        p: List[float],
        xdir: List[float],
    ) -> float: ...
    def BracketFunctionMinimum(
        self,
        func: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.Function1D,
        a: float,
        b: float,
        c: float,
    ) -> None: ...
    def ConjugateGradientMinimization(
        self, p: List[float], tolerance: float, nIter: int
    ) -> float: ...

class SIMAcqMethodGenerator:  # Class
    def __init__(self) -> None: ...

    AutoSIMDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet
    )  # readonly
    AutoSIMParams: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.AutoSIMParams
    )  # readonly

    def CreateSIMAcquisitionMethod(
        self,
        acqMethodDirectory: str,
        setupSession: MethodSetupSession,
        options: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.CompoundListTSOptimizerParams,
    ) -> None: ...

class SafetyMarginUnits(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Minutes: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.SafetyMarginUnits
    ) = ...  # static # readonly
    PeakWidths: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.SafetyMarginUnits
    ) = ...  # static # readonly
    Percent: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.SafetyMarginUnits
    ) = ...  # static # readonly

class TimeSegmentBoundary:  # Class
    DEFAULT_COST_SCALE: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.BoundaryCostScale
    ) = ...  # static # readonly
    DEFAULT_SAFETY_MARGIN: float = ...  # static # readonly

    CostScale: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.BoundaryCostScale
    )  # static
    SafetyMargin: float  # static
    SafetyMarginUnits: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.SafetyMarginUnits
    )  # static

class TimeSegmentOptimizer:  # Class
    def __init__(
        self,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet,
    ) -> None: ...

    DEFAULT_MIN_DWELL_TIME: float = ...  # static # readonly
    DEFAULT_MIN_POINTS_PER_PEAK: int = ...  # static # readonly
    DIAG_DIR: str = ...  # static # readonly
    MAX_TIME_SEGMENTS: int = ...  # static # readonly
    MAX_TRANSITIONS_PER_TS: int = ...  # static # readonly
    MIN_ALLOWED_DWELL_TIME: float = ...  # static # readonly
    MIN_POINTS_PER_TIME_SEGMENT: int = ...  # static # readonly

    MinDwellTime: float
    MinPointsPerPeak: int
    MinPointsPerTimeSegment: int  # readonly
    TransitionTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.AcquiredTransitionTable
    )  # readonly

    def IsolateOutliers(self) -> None: ...
    def RunOptimization(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet
    ): ...

class TimeSegmentOptimizerDataSet(
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

    IsSIM: bool  # readonly
    Relations: System.Data.DataRelationCollection  # readonly
    SchemaSerializationMode: System.Data.SchemaSerializationMode
    Tables: System.Data.DataTableCollection  # readonly
    TimeSegment: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentDataTable
    )  # readonly
    TransitionPeak: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakDataTable
    )  # readonly

    @staticmethod
    def GetTypedDataSetSchema(
        xs: System.Xml.Schema.XmlSchemaSet,
    ) -> System.Xml.Schema.XmlSchemaComplexType: ...
    def GetUnusedTimeSegmentID(self) -> int: ...
    def Clone(self) -> System.Data.DataSet: ...

    # Nested Types

    class TimeSegmentDataTable(
        System.IServiceProvider,
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow
        ],
        System.ComponentModel.IListSource,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow
        ],
        System.IDisposable,
    ):  # Class
        def __init__(self) -> None: ...

        Count: int  # readonly
        IndexColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow
        ): ...
        OptimizationFactorColumn: System.Data.DataColumn  # readonly
        OptimizedCycleTimeColumn: System.Data.DataColumn  # readonly
        TimeSegmentIDColumn: System.Data.DataColumn  # readonly
        TransitionCountColumn: System.Data.DataColumn  # readonly
        XEndColumn: System.Data.DataColumn  # readonly
        XStartColumn: System.Data.DataColumn  # readonly

        def RemoveTimeSegmentRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow,
        ) -> None: ...
        @overload
        def AddTimeSegmentRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow,
        ) -> None: ...
        @overload
        def AddTimeSegmentRow(
            self,
            TimeSegmentID: int,
            Index: int,
            OptimizationFactor: float,
            OptimizedCycleTime: float,
            TransitionCount: int,
            XEnd: float,
            XStart: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewTimeSegmentRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow
        ): ...
        def FindByTimeSegmentID(
            self, TimeSegmentID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...

        TimeSegmentRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRowChangeEventHandler
        )  # Event
        TimeSegmentRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRowChangeEventHandler
        )  # Event
        TimeSegmentRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRowChangeEventHandler
        )  # Event
        TimeSegmentRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRowChangeEventHandler
        )  # Event

    class TimeSegmentRow(System.Data.DataRow):  # Class
        Index: int
        OptimizationFactor: float
        OptimizedCycleTime: float
        TimeSegmentID: int
        TransitionCount: int
        XEnd: float
        XStart: float

        def SetOptimizedCycleTimeNull(self) -> None: ...
        def IsOptimizationFactorNull(self) -> bool: ...
        def IsXStartNull(self) -> bool: ...
        def SetIndexNull(self) -> None: ...
        def IsIndexNull(self) -> bool: ...
        def SetXEndNull(self) -> None: ...
        def GetTransitionPeakRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow
        ]: ...
        def IsOptimizedCycleTimeNull(self) -> bool: ...
        def IsTransitionCountNull(self) -> bool: ...
        def SetTransitionCountNull(self) -> None: ...
        def IsXEndNull(self) -> bool: ...
        def SetOptimizationFactorNull(self) -> None: ...
        def SetXStartNull(self) -> None: ...

    class TimeSegmentRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow
        )  # readonly

    class TimeSegmentRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRowChangeEvent,
        ) -> None: ...

    class TransitionPeakDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AbundanceValuesColumn: System.Data.DataColumn  # readonly
        AcquiredDwellTimeColumn: System.Data.DataColumn  # readonly
        AreaColumn: System.Data.DataColumn  # readonly
        CollisionEnergyColumn: System.Data.DataColumn  # readonly
        CompoundNameColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DeltaEMVColumn: System.Data.DataColumn  # readonly
        FragmentorVoltageColumn: System.Data.DataColumn  # readonly
        GainColumn: System.Data.DataColumn  # readonly
        HeightColumn: System.Data.DataColumn  # readonly
        ISTDFlagColumn: System.Data.DataColumn  # readonly
        IonPolarityColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow
        ): ...
        MZColumn: System.Data.DataColumn  # readonly
        Ms1ResColumn: System.Data.DataColumn  # readonly
        Ms2ResColumn: System.Data.DataColumn  # readonly
        NoiseFactorColumn: System.Data.DataColumn  # readonly
        NumberOfPointsColumn: System.Data.DataColumn  # readonly
        OptimizedDwellTimeColumn: System.Data.DataColumn  # readonly
        OptimizedNumberOfPointsColumn: System.Data.DataColumn  # readonly
        OptimizedRSDColumn: System.Data.DataColumn  # readonly
        OutlierColumn: System.Data.DataColumn  # readonly
        RTValuesColumn: System.Data.DataColumn  # readonly
        RetentionTimeColumn: System.Data.DataColumn  # readonly
        SampleDataPathColumn: System.Data.DataColumn  # readonly
        ScanModeColumn: System.Data.DataColumn  # readonly
        SelectedMZColumn: System.Data.DataColumn  # readonly
        TimeSegmentIDColumn: System.Data.DataColumn  # readonly
        TransitionColumn: System.Data.DataColumn  # readonly
        TransitionPeakIDColumn: System.Data.DataColumn  # readonly
        XEndColumn: System.Data.DataColumn  # readonly
        XStartColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByTimeSegmentIDTransitionPeakID(
            self, TimeSegmentID: int, TransitionPeakID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow
        ): ...
        @overload
        def AddTransitionPeakRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow,
        ) -> None: ...
        @overload
        def AddTransitionPeakRow(
            self,
            parentTimeSegmentRowByFK_TimeSegment_TransitionPeak: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow,
            TransitionPeakID: int,
            AbundanceValues: str,
            AcquiredDwellTime: float,
            Area: float,
            CollisionEnergy: float,
            CompoundName: str,
            DeltaEMV: float,
            FragmentorVoltage: float,
            Gain: float,
            Height: float,
            IonPolarity: str,
            ISTDFlag: bool,
            Ms1Res: str,
            Ms2Res: str,
            MZ: float,
            NoiseFactor: float,
            NumberOfPoints: int,
            OptimizedDwellTime: float,
            OptimizedNumberOfPoints: int,
            OptimizedRSD: float,
            Outlier: bool,
            RetentionTime: float,
            RTValues: str,
            SampleDataPath: str,
            ScanMode: str,
            SelectedMZ: float,
            Transition: str,
            XEnd: float,
            XStart: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveTransitionPeakRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow,
        ) -> None: ...
        def NewTransitionPeakRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow
        ): ...

        TransitionPeakRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRowChangeEventHandler
        )  # Event
        TransitionPeakRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRowChangeEventHandler
        )  # Event
        TransitionPeakRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRowChangeEventHandler
        )  # Event
        TransitionPeakRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRowChangeEventHandler
        )  # Event

    class TransitionPeakRow(System.Data.DataRow):  # Class
        AbundanceValues: str
        AcquiredDwellTime: float
        Area: float
        CollisionEnergy: float
        CompoundName: str
        DeltaEMV: float
        FragmentorVoltage: float
        Gain: float
        Height: float
        ISTDFlag: bool
        IonPolarity: str
        IsPeakNotFound: bool  # readonly
        MZ: float
        Ms1Res: str
        Ms2Res: str
        NoiseFactor: float
        NumberOfPoints: int
        OptimizedDwellTime: float
        OptimizedNumberOfPoints: int
        OptimizedRSD: float
        Outlier: bool
        RTValues: str
        RetentionTime: float
        SampleDataPath: str
        ScanMode: str
        SelectedMZ: float
        TimeSegmentID: int
        TimeSegmentRow: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TimeSegmentRow
        )
        Transition: str
        TransitionPeakID: int
        XEnd: float
        XStart: float

        def IsMZNull(self) -> bool: ...
        def IsNoiseFactorNull(self) -> bool: ...
        def IsOptimizedRSDNull(self) -> bool: ...
        def SetMs1ResNull(self) -> None: ...
        def IsAbundanceValuesNull(self) -> bool: ...
        def IsRTValuesNull(self) -> bool: ...
        def IsAcquiredDwellTimeNull(self) -> bool: ...
        def SetNumberOfPointsNull(self) -> None: ...
        def IsHeightNull(self) -> bool: ...
        def SetAcquiredDwellTimeNull(self) -> None: ...
        def SetNoiseFactorNull(self) -> None: ...
        def SetScanModeNull(self) -> None: ...
        def SetISTDFlagNull(self) -> None: ...
        def IsAreaNull(self) -> bool: ...
        def SetIonPolarityNull(self) -> None: ...
        def SetAbundanceValuesNull(self) -> None: ...
        def IsMs2ResNull(self) -> bool: ...
        def IsRetentionTimeNull(self) -> bool: ...
        def SetOutlierNull(self) -> None: ...
        def SetRTValuesNull(self) -> None: ...
        def IsFragmentorVoltageNull(self) -> bool: ...
        def SetDeltaEMVNull(self) -> None: ...
        def SetTransitionNull(self) -> None: ...
        def SetFragmentorVoltageNull(self) -> None: ...
        def IsIonPolarityNull(self) -> bool: ...
        def IsGainNull(self) -> bool: ...
        def IsNumberOfPointsNull(self) -> bool: ...
        def SetSampleDataPathNull(self) -> None: ...
        def SetHeightNull(self) -> None: ...
        def SetXEndNull(self) -> None: ...
        def IsSelectedMZNull(self) -> bool: ...
        def IsCollisionEnergyNull(self) -> bool: ...
        def IsOptimizedNumberOfPointsNull(self) -> bool: ...
        def IsOutlierNull(self) -> bool: ...
        def IsScanModeNull(self) -> bool: ...
        def SetOptimizedNumberOfPointsNull(self) -> None: ...
        def SetMs2ResNull(self) -> None: ...
        def IsXStartNull(self) -> bool: ...
        def SetRetentionTimeNull(self) -> None: ...
        def IsDeltaEMVNull(self) -> bool: ...
        def IsCompoundNameNull(self) -> bool: ...
        def SetXStartNull(self) -> None: ...
        def SetGainNull(self) -> None: ...
        def IsSampleDataPathNull(self) -> bool: ...
        def SetMZNull(self) -> None: ...
        def IsMs1ResNull(self) -> bool: ...
        def SetAreaNull(self) -> None: ...
        def SetOptimizedDwellTimeNull(self) -> None: ...
        def SetCollisionEnergyNull(self) -> None: ...
        def SetCompoundNameNull(self) -> None: ...
        def SetOptimizedRSDNull(self) -> None: ...
        def IsISTDFlagNull(self) -> bool: ...
        def IsXEndNull(self) -> bool: ...
        def IsOptimizedDwellTimeNull(self) -> bool: ...
        def IsTransitionNull(self) -> bool: ...
        def SetSelectedMZNull(self) -> None: ...

    class TransitionPeakRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRow
        )  # readonly

    class TransitionPeakRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet.TransitionPeakRowChangeEvent,
        ) -> None: ...

class TransitionTableGenerator:  # Class
    def __init__(self, context: AppCommandContext) -> None: ...

    AcqMehod: AcquisitionMethod  # readonly
    DataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TSO.TimeSegmentOptimizerDataSet
    )  # readonly

    def AddTransitionTableFromSample(self, samplePath: str) -> None: ...
