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

# Stubs for namespace: DataFitX3

class CubicInformation:  # Class
    Interval: int  # readonly
    LowerBound: float  # readonly
    UpperBound: float  # readonly
    a: float  # readonly
    b: float  # readonly
    c: float  # readonly
    d: float  # readonly

class CubicSpline:  # Class
    def __init__(self) -> None: ...

    IsSolved: bool  # readonly
    LastSolveError: str  # readonly
    NumIntervals: int  # readonly
    NumObservations: int  # readonly
    ResultTables: DataFitX3.DataCollection  # readonly
    Tag: str

    def ReadSolution(self, FilePath: str) -> None: ...
    def CalculateIntegral(self, XLowerBound: float, XUpperBound: float) -> float: ...
    def SaveLog(self, FilePath: str, Append: bool = ...) -> None: ...
    def CalculateDerivative(self, XValue: float) -> float: ...
    def Fit(self, XObservations: List[float], YObservations: List[float]) -> None: ...
    def ClearFit(self) -> None: ...
    def SaveSolution(self, FilePath: str) -> None: ...
    def CalculateRootsAlt(
        self,
        YValue: float,
        XLowerBound: float,
        XUpperBound: float,
        NumIntervals: int = ...,
    ) -> Any: ...
    def PredictValue(self, XValue: float) -> float: ...
    def CalculateRoots(
        self,
        YValue: float,
        XLowerBound: float,
        XUpperBound: float,
        NumIntervals: int = ...,
    ) -> List[float]: ...
    def FitAlt(self, XObservations: Any, YObservations: Any) -> None: ...
    def SaveDFT(self, FilePath: str, MajorVersion: int, MinorVersion: int) -> None: ...
    def GetCubicByInterval(self, Interval: int) -> DataFitX3.CubicInformation: ...
    def PredictArrayAlt(self, XValues: Any) -> Any: ...
    def GetCubicByValue(self, XValue: float) -> DataFitX3.CubicInformation: ...
    def PredictArray(self, XValues: List[float]) -> List[float]: ...
    def FitCollection(self, ObservedData: DataFitX3.DataCollection) -> None: ...

    SolutionComplete: DataFitX3.CubicSpline.SolutionCompleteEventHandler  # Event

    # Nested Types

    class SolutionCompleteEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(self, Success: bool) -> None: ...

class DataCollection(Iterable[Any]):  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly
    IsReadOnly: bool  # readonly
    def __getitem__(self, SeriesIndex: Any) -> DataFitX3.DataSeries: ...
    NumObservationsMax: int  # readonly
    NumObservationsMin: int  # readonly

    def GetEnumerator(self) -> Iterator[Any]: ...
    def Sort(self, SortDirection: DataFitX3.SortTypeEnum = ...) -> None: ...
    def ImportSeriesFromFile(
        self,
        FilePath: str,
        NameArray: List[str],
        Delimiter: DataFitX3.DelimiterTypeEnum = ...,
        DecimalSeparator: str = ...,
        DateSeparator: str = ...,
        MissingQualifier: str = ...,
    ) -> None: ...
    def SetNumberDisplayFormats(self, FormatString: str) -> None: ...
    def ExportSeriesToArrayAlt(self) -> Any: ...
    def SortOnSeries(
        self, SeriesIndex: Any, SortDirection: DataFitX3.SortTypeEnum = ...
    ) -> None: ...
    def ImportNamedSeriesFromFile(
        self,
        FilePath: str,
        Delimiter: DataFitX3.DelimiterTypeEnum = ...,
        DecimalSeparator: str = ...,
        DateSeparator: str = ...,
        MissingQualifier: str = ...,
    ) -> None: ...
    def RemoveSeries(self, SeriesIndex: Any = ...) -> None: ...
    def RemoveAllSeries(self) -> None: ...
    def PruneOnSeries(
        self, SeriesIndex: Any, Value: float, LogicalOperator: DataFitX3.LogicalTypeEnum
    ) -> None: ...
    def AddSeries(
        self, Name: str, PreAllocation: int = ...
    ) -> DataFitX3.DataSeries: ...
    def Prune(
        self, Value: float, LogicalOperator: DataFitX3.LogicalTypeEnum
    ) -> None: ...
    def ExportSeriesToArray(self) -> System.Array[float]: ...
    def CalculateCorrelation(self, SeriesIndex1: Any, SeriesIndex2: Any) -> float: ...
    def ExportSeriesToFile(
        self,
        FilePath: str,
        IncludeNames: bool = ...,
        SaveFormatted: bool = ...,
        AppendData: bool = ...,
    ) -> None: ...
    def ImportSeriesFromFileAlt(
        self,
        FilePath: str,
        NameArray: Any,
        Delimiter: DataFitX3.DelimiterTypeEnum = ...,
        DecimalSeparator: str = ...,
        DateSeparator: str = ...,
        MissingQualifier: str = ...,
    ) -> None: ...
    def ClearRegressionKeys(self) -> None: ...
    def ImportSeriesFromArray(
        self, DataArray: System.Array[float], NameArray: List[str]
    ) -> None: ...
    def ImportSeriesFromArrayAlt(self, DataArray: Any, NameArray: Any) -> None: ...
    def CalculateCovariance(self, SeriesIndex1: Any, SeriesIndex2: Any) -> float: ...

class DataSeries:  # Class
    IsReadOnly: bool  # readonly
    Kurtosis: float  # readonly
    Maximum: float  # readonly
    Mean: float  # readonly
    MeanAbsoluteDeviation: float  # readonly
    MeanSquareDeviation: float  # readonly
    Median: float  # readonly
    Minimum: float  # readonly
    Name: str  # readonly
    NumObservations: int  # readonly
    NumberDisplayFormat: str
    Range: float  # readonly
    RegressionKey: str
    RootMeanSquare: float  # readonly
    Skewness: float  # readonly
    StandardDeviation: float  # readonly
    Sum: float  # readonly
    SumOfSquaredDeviation: float  # readonly
    Tag: str
    Variance: float  # readonly

    def AddObservation(self, Value: float) -> None: ...
    def Sort(self, SortDirection: DataFitX3.SortTypeEnum = ...) -> None: ...
    def ExportToArray(self) -> List[float]: ...
    def Multiply(self, Factor: float) -> None: ...
    def SetObservation(self, ObservationIndex: int, Value: float) -> None: ...
    def ImportFromArrayAlt(self, DataArray: Any, AppendData: bool = ...) -> None: ...
    def GetObservation(self, ObservationIndex: int) -> float: ...
    def RemoveAllObservations(self) -> None: ...
    def ExportToFile(
        self,
        FilePath: str,
        IncludeName: bool = ...,
        SaveFormatted: bool = ...,
        AppendData: bool = ...,
    ) -> None: ...
    def Prune(
        self, Value: float, LogicalOperator: DataFitX3.LogicalTypeEnum
    ) -> None: ...
    def ImportFromFile(
        self,
        FilePath: str,
        AppendData: bool = ...,
        DecimalSeparator: str = ...,
        DateSeparator: str = ...,
    ) -> None: ...
    def GetObservationFormatted(self, ObservationIndex: int) -> str: ...
    def Transform(self, Transformation: DataFitX3.TransformTypeEnum) -> None: ...
    def GetObservationIndex(
        self, SearchType: DataFitX3.SearchTypeEnum, SearchValue: float = ...
    ) -> int: ...
    def Translate(self, Factor: float) -> None: ...
    def RemoveObservation(self, ObservationIndex: int = ...) -> None: ...
    def ExportToArrayAlt(self) -> Any: ...
    def ImportFromArray(
        self, DataArray: List[float], AppendData: bool = ...
    ) -> None: ...
    def Fill(
        self,
        StartValue: float,
        Increment: float,
        NumObservations: int,
        AppendData: bool = ...,
    ) -> None: ...

class DelimiterTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    dfxDelimiterComma: DataFitX3.DelimiterTypeEnum = ...  # static # readonly
    dfxDelimiterSemicolon: DataFitX3.DelimiterTypeEnum = ...  # static # readonly
    dfxDelimiterSpace: DataFitX3.DelimiterTypeEnum = ...  # static # readonly
    dfxDelimiterTab: DataFitX3.DelimiterTypeEnum = ...  # static # readonly

class EstimateTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    dfxEstimateAdjust: DataFitX3.EstimateTypeEnum = ...  # static # readonly
    dfxEstimateConstant: DataFitX3.EstimateTypeEnum = ...  # static # readonly

class Expression:  # Class
    def __init__(self) -> None: ...

    ExpressionDefinition: DataFitX3.ModelDefinition  # readonly
    ExpressionDefinitionLocal: DataFitX3.ModelDefinition  # readonly
    ExpressionParameters: DataFitX3.ExpressionParameters  # readonly
    IsValidExpression: bool  # readonly
    Tag: str

    def DefineExpression(
        self,
        Definition: str,
        Locale: DataFitX3.InputLocaleEnum = ...,
        Description: str = ...,
    ) -> None: ...
    def DefineExpressionSub(
        self,
        Definition: DataFitX3.ModelDefinition,
        Locale: DataFitX3.InputLocaleEnum = ...,
    ) -> None: ...
    def CalculateArrayAlt(self, ParameterIndex: Any, Values: Any) -> Any: ...
    def CalculateArray(
        self, ParameterIndex: Any, Values: List[float]
    ) -> List[float]: ...
    def CalculateValue(self) -> float: ...

class ExpressionParameter:  # Class
    Name: str  # readonly
    Value: float

class ExpressionParameters(Iterable[Any]):  # Class
    Count: int  # readonly
    def __getitem__(self, ParameterIndex: Any) -> DataFitX3.ExpressionParameter: ...
    def GetEnumerator(self) -> Iterator[Any]: ...

class General(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    dfxLast: DataFitX3.General = ...  # static # readonly

class InputLocaleEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    dfxLocaleEnglish: DataFitX3.InputLocaleEnum = ...  # static # readonly
    dfxLocaleLocal: DataFitX3.InputLocaleEnum = ...  # static # readonly

class LogicalTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    dfxLogicalEqualTo: DataFitX3.LogicalTypeEnum = ...  # static # readonly
    dfxLogicalGreaterThan: DataFitX3.LogicalTypeEnum = ...  # static # readonly
    dfxLogicalGreaterThanOrEqualTo: DataFitX3.LogicalTypeEnum = ...  # static # readonly
    dfxLogicalLessThan: DataFitX3.LogicalTypeEnum = ...  # static # readonly
    dfxLogicalLessThanOrEqualTo: DataFitX3.LogicalTypeEnum = ...  # static # readonly

class ModelDefinition:  # Class
    def __init__(self) -> None: ...

    Description: str
    F1: str
    F2: str
    F3: str
    F4: str
    F5: str
    F6: str
    F7: str
    F8: str
    F9: str
    Y: str

class ModelTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    dfxModelExternal: DataFitX3.ModelTypeEnum = ...  # static # readonly
    dfxModelInternal: DataFitX3.ModelTypeEnum = ...  # static # readonly
    dfxModelUser: DataFitX3.ModelTypeEnum = ...  # static # readonly

class MultipleNonlinearRegression:  # Class
    def __init__(self) -> None: ...

    DOFError: int  # readonly
    DOFRegression: int  # readonly
    DOFTotal: int  # readonly
    DurbinWatson: float  # readonly
    IsSolved: bool  # readonly
    IsValidModel: bool  # readonly
    IsWeighted: bool  # readonly
    LastSolveError: str  # readonly
    MaxIterations: int
    MaxUnchangedIterations: int
    ModelDefinition: DataFitX3.ModelDefinition  # readonly
    ModelDefinitionLocal: DataFitX3.ModelDefinition  # readonly
    ModelType: DataFitX3.ModelTypeEnum  # readonly
    NumIndependentVariables: int  # readonly
    NumIterations: int  # readonly
    NumObservations: int  # readonly
    NumUnchangedIterations: int  # readonly
    ProbF: float  # readonly
    R2: float  # readonly
    R2Adjust: float  # readonly
    RegressionParameters: DataFitX3.RegressionParameters  # readonly
    RegressionTolerance: float
    ResidualAverage: float  # readonly
    ResidualSum: float  # readonly
    ResultTables: DataFitX3.DataCollection  # readonly
    SSE: float  # readonly
    SSENorm: float  # readonly
    SSR: float  # readonly
    SST: float  # readonly
    StandardError: float  # readonly
    Tag: str

    def DefineExternalModel(
        self,
        NumIndependentVars: int,
        Parameters: List[str],
        ExternalDerivatives: bool = ...,
    ) -> None: ...
    def CalculateRootsAlt(
        self,
        YValue: float,
        XValues: Any,
        XIndex: int,
        XLowerBound: float,
        XUpperBound: float,
        NumIntervals: int = ...,
    ) -> Any: ...
    def DefineUserModelSub(
        self,
        Definition: DataFitX3.ModelDefinition,
        Locale: DataFitX3.InputLocaleEnum = ...,
    ) -> None: ...
    def PredictArray(self, XValues: System.Array[float]) -> List[float]: ...
    def ReadSolution(self, FilePath: str) -> None: ...
    def SaveSolution(self, FilePath: str) -> None: ...
    def FitCollection(self, ObservedData: DataFitX3.DataCollection) -> None: ...
    def SaveDFT(self, FilePath: str, MajorVersion: int, MinorVersion: int) -> None: ...
    def Fit(
        self, XObservations: System.Array[float], YObservations: List[float]
    ) -> None: ...
    def PredictArrayAlt(self, XValues: Any) -> Any: ...
    def DefineUserModel(
        self,
        Definition: str,
        Locale: DataFitX3.InputLocaleEnum = ...,
        Description: str = ...,
    ) -> None: ...
    def FitAlt(self, XObservations: Any, YObservations: Any) -> None: ...
    def CalculateDerivativeAlt(self, XValues: Any, XIndex: int) -> float: ...
    def SaveLog(self, FilePath: str, Append: bool = ...) -> None: ...
    def PredictValueAlt(self, XValues: Any) -> float: ...
    def DefineInternalModel(self, ModelID: int) -> None: ...
    def ClearFit(self) -> None: ...
    def CalculateRoots(
        self,
        YValue: float,
        XValues: List[float],
        XIndex: int,
        XLowerBound: float,
        XUpperBound: float,
        NumIntervals: int = ...,
    ) -> List[float]: ...
    def FitWeightedAlt(
        self, XObservations: Any, YObservations: Any, StandardDeviations: Any
    ) -> None: ...
    def PredictValue(self, XValues: List[float]) -> float: ...
    def FitWeighted(
        self,
        XObservations: System.Array[float],
        YObservations: List[float],
        StandardDeviations: List[float],
    ) -> None: ...
    def CalculateDerivative(self, XValues: List[float], XIndex: int) -> float: ...
    def DefineExternalModelAlt(
        self, NumIndependentVars: int, Parameters: Any, ExternalDerivatives: bool = ...
    ) -> None: ...

    DerivativeExternal: (
        DataFitX3.MultipleNonlinearRegression.DerivativeExternalEventHandler
    )  # Event
    DerivativeExternalAlt: (
        DataFitX3.MultipleNonlinearRegression.DerivativeExternalAltEventHandler
    )  # Event
    EvaluateExternal: (
        DataFitX3.MultipleNonlinearRegression.EvaluateExternalEventHandler
    )  # Event
    EvaluateExternalAlt: (
        DataFitX3.MultipleNonlinearRegression.EvaluateExternalAltEventHandler
    )  # Event
    IterationComplete: (
        DataFitX3.MultipleNonlinearRegression.IterationCompleteEventHandler
    )  # Event
    SolutionComplete: (
        DataFitX3.MultipleNonlinearRegression.SolutionCompleteEventHandler
    )  # Event

    # Nested Types

    class DerivativeExternalAltEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(
            self,
            ParameterValues: Any,
            XValues: Any,
            dParameterValues: Any,
            Success: bool,
            DelegateAsyncResult: System.IAsyncResult,
        ) -> None: ...
        def BeginInvoke(
            self,
            ParameterValues: Any,
            XValues: Any,
            dParameterValues: Any,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            ParameterValues: Any,
            XValues: Any,
            dParameterValues: Any,
            Success: bool,
        ) -> None: ...

    class DerivativeExternalEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(
            self,
            ParameterValues: System.Array,
            XValues: System.Array,
            dParameterValues: System.Array,
            Success: bool,
            DelegateAsyncResult: System.IAsyncResult,
        ) -> None: ...
        def BeginInvoke(
            self,
            ParameterValues: System.Array,
            XValues: System.Array,
            dParameterValues: System.Array,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            ParameterValues: System.Array,
            XValues: System.Array,
            dParameterValues: System.Array,
            Success: bool,
        ) -> None: ...

    class EvaluateExternalAltEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(
            self,
            ParameterValues: Any,
            XValues: Any,
            Result: float,
            Success: bool,
            DelegateAsyncResult: System.IAsyncResult,
        ) -> None: ...
        def BeginInvoke(
            self,
            ParameterValues: Any,
            XValues: Any,
            Result: float,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self, ParameterValues: Any, XValues: Any, Result: float, Success: bool
        ) -> None: ...

    class EvaluateExternalEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(
            self,
            ParameterValues: System.Array,
            XValues: System.Array,
            Result: float,
            Success: bool,
            DelegateAsyncResult: System.IAsyncResult,
        ) -> None: ...
        def BeginInvoke(
            self,
            ParameterValues: System.Array,
            XValues: System.Array,
            Result: float,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            ParameterValues: System.Array,
            XValues: System.Array,
            Result: float,
            Success: bool,
        ) -> None: ...

    class IterationCompleteEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(
            self, Abort: bool, DelegateAsyncResult: System.IAsyncResult
        ) -> None: ...
        def BeginInvoke(
            self,
            Iteration: int,
            SSE: float,
            Abort: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(self, Iteration: int, SSE: float, Abort: bool) -> None: ...

    class SolutionCompleteEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(self, Success: bool) -> None: ...

class NonlinearRegression:  # Class
    def __init__(self) -> None: ...

    DOFError: int  # readonly
    DOFRegression: int  # readonly
    DOFTotal: int  # readonly
    DurbinWatson: float  # readonly
    IsSolved: bool  # readonly
    IsValidModel: bool  # readonly
    IsWeighted: bool  # readonly
    LastSolveError: str  # readonly
    MaxIterations: int
    MaxUnchangedIterations: int
    ModelDefinition: DataFitX3.ModelDefinition  # readonly
    ModelDefinitionLocal: DataFitX3.ModelDefinition  # readonly
    ModelType: DataFitX3.ModelTypeEnum  # readonly
    NumIndependentVariables: int  # readonly
    NumIterations: int  # readonly
    NumObservations: int  # readonly
    NumUnchangedIterations: int  # readonly
    ProbF: float  # readonly
    R2: float  # readonly
    R2Adjust: float  # readonly
    RegressionParameters: DataFitX3.RegressionParameters  # readonly
    RegressionTolerance: float
    ResidualAverage: float  # readonly
    ResidualSum: float  # readonly
    ResultTables: DataFitX3.DataCollection  # readonly
    SSE: float  # readonly
    SSENorm: float  # readonly
    SSR: float  # readonly
    SST: float  # readonly
    StandardError: float  # readonly
    Tag: str

    def DefineExternalModel(
        self, Parameters: List[str], ExternalDerivatives: bool = ...
    ) -> None: ...
    def CalculateRootsAlt(
        self,
        YValue: float,
        XLowerBound: float,
        XUpperBound: float,
        NumIntervals: int = ...,
    ) -> Any: ...
    def DefineUserModelSub(
        self,
        Definition: DataFitX3.ModelDefinition,
        Locale: DataFitX3.InputLocaleEnum = ...,
    ) -> None: ...
    def PredictArray(self, XValues: List[float]) -> List[float]: ...
    def ReadSolution(self, FilePath: str) -> None: ...
    def SaveSolution(self, FilePath: str) -> None: ...
    def FitCollection(self, ObservedData: DataFitX3.DataCollection) -> None: ...
    def SaveDFT(self, FilePath: str, MajorVersion: int, MinorVersion: int) -> None: ...
    def Fit(self, XObservations: List[float], YObservations: List[float]) -> None: ...
    def PredictArrayAlt(self, XValues: Any) -> Any: ...
    def DefineUserModel(
        self,
        Definition: str,
        Locale: DataFitX3.InputLocaleEnum = ...,
        Description: str = ...,
    ) -> None: ...
    def FitAlt(self, XObservations: Any, YObservations: Any) -> None: ...
    def SaveLog(self, FilePath: str, Append: bool = ...) -> None: ...
    def DefineInternalModel(self, ModelID: int) -> None: ...
    def ClearFit(self) -> None: ...
    def CalculateRoots(
        self,
        YValue: float,
        XLowerBound: float,
        XUpperBound: float,
        NumIntervals: int = ...,
    ) -> List[float]: ...
    def CalculateIntegral(self, XLowerBound: float, XUpperBound: float) -> float: ...
    def FitWeightedAlt(
        self, XObservations: Any, YObservations: Any, StandardDeviations: Any
    ) -> None: ...
    def PredictValue(self, XValue: float) -> float: ...
    def FitWeighted(
        self,
        XObservations: List[float],
        YObservations: List[float],
        StandardDeviations: List[float],
    ) -> None: ...
    def CalculateDerivative(self, XValue: float) -> float: ...
    def DefineExternalModelAlt(
        self, Parameters: Any, ExternalDerivatives: bool = ...
    ) -> None: ...

    DerivativeExternal: (
        DataFitX3.NonlinearRegression.DerivativeExternalEventHandler
    )  # Event
    DerivativeExternalAlt: (
        DataFitX3.NonlinearRegression.DerivativeExternalAltEventHandler
    )  # Event
    EvaluateExternal: (
        DataFitX3.NonlinearRegression.EvaluateExternalEventHandler
    )  # Event
    EvaluateExternalAlt: (
        DataFitX3.NonlinearRegression.EvaluateExternalAltEventHandler
    )  # Event
    IterationComplete: (
        DataFitX3.NonlinearRegression.IterationCompleteEventHandler
    )  # Event
    SolutionComplete: (
        DataFitX3.NonlinearRegression.SolutionCompleteEventHandler
    )  # Event

    # Nested Types

    class DerivativeExternalAltEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(
            self,
            ParameterValues: Any,
            dParameterValues: Any,
            Success: bool,
            DelegateAsyncResult: System.IAsyncResult,
        ) -> None: ...
        def BeginInvoke(
            self,
            ParameterValues: Any,
            XValue: float,
            dParameterValues: Any,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            ParameterValues: Any,
            XValue: float,
            dParameterValues: Any,
            Success: bool,
        ) -> None: ...

    class DerivativeExternalEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(
            self,
            ParameterValues: System.Array,
            dParameterValues: System.Array,
            Success: bool,
            DelegateAsyncResult: System.IAsyncResult,
        ) -> None: ...
        def BeginInvoke(
            self,
            ParameterValues: System.Array,
            XValue: float,
            dParameterValues: System.Array,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            ParameterValues: System.Array,
            XValue: float,
            dParameterValues: System.Array,
            Success: bool,
        ) -> None: ...

    class EvaluateExternalAltEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(
            self,
            ParameterValues: Any,
            Result: float,
            Success: bool,
            DelegateAsyncResult: System.IAsyncResult,
        ) -> None: ...
        def BeginInvoke(
            self,
            ParameterValues: Any,
            XValue: float,
            Result: float,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self, ParameterValues: Any, XValue: float, Result: float, Success: bool
        ) -> None: ...

    class EvaluateExternalEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(
            self,
            ParameterValues: System.Array,
            Result: float,
            Success: bool,
            DelegateAsyncResult: System.IAsyncResult,
        ) -> None: ...
        def BeginInvoke(
            self,
            ParameterValues: System.Array,
            XValue: float,
            Result: float,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            ParameterValues: System.Array,
            XValue: float,
            Result: float,
            Success: bool,
        ) -> None: ...

    class IterationCompleteEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(
            self, Abort: bool, DelegateAsyncResult: System.IAsyncResult
        ) -> None: ...
        def BeginInvoke(
            self,
            Iteration: int,
            SSE: float,
            Abort: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(self, Iteration: int, SSE: float, Abort: bool) -> None: ...

    class SolutionCompleteEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, TargetObject: Any, TargetMethod: System.IntPtr) -> None: ...
        def EndInvoke(self, DelegateAsyncResult: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            Success: bool,
            DelegateCallback: System.AsyncCallback,
            DelegateAsyncState: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(self, Success: bool) -> None: ...

class RegressionParameter:  # Class
    InitialEstimate: float
    InitialEstimateType: DataFitX3.EstimateTypeEnum
    Name: str  # readonly
    PreviousValue: float  # readonly
    ProbT: float  # readonly
    StandardError: float  # readonly
    Value: float  # readonly

    def CalculateCIDelta(self, Percent: float) -> float: ...

class RegressionParameters(Iterable[Any]):  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly
    def __getitem__(self, ParameterIndex: Any) -> DataFitX3.RegressionParameter: ...
    def SetDefaultEstimates(self) -> None: ...
    def CalculateCovariance(
        self, ParameterIndex1: Any, ParameterIndex2: Any
    ) -> float: ...
    def GetEnumerator(self) -> Iterator[Any]: ...

class SearchTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    dfxMaximum: DataFitX3.SearchTypeEnum = ...  # static # readonly
    dfxMinimum: DataFitX3.SearchTypeEnum = ...  # static # readonly
    dfxValue: DataFitX3.SearchTypeEnum = ...  # static # readonly

class SortTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    dfxSortAscending: DataFitX3.SortTypeEnum = ...  # static # readonly
    dfxSortDescending: DataFitX3.SortTypeEnum = ...  # static # readonly

class TransformTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    dfxTransformInvert: DataFitX3.TransformTypeEnum = ...  # static # readonly
    dfxTransformInvertNaturalLog: DataFitX3.TransformTypeEnum = ...  # static # readonly
    dfxTransformInvertSquare: DataFitX3.TransformTypeEnum = ...  # static # readonly
    dfxTransformInvertSquareRoot: DataFitX3.TransformTypeEnum = ...  # static # readonly
    dfxTransformNaturalLog: DataFitX3.TransformTypeEnum = ...  # static # readonly
    dfxTransformSquare: DataFitX3.TransformTypeEnum = ...  # static # readonly
    dfxTransformSquareRoot: DataFitX3.TransformTypeEnum = ...  # static # readonly
