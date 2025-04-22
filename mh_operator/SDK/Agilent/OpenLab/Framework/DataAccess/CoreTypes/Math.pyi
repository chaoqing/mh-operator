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
    Axis,
    EqualizeMode,
    IData,
    IEquidistantData,
    ISmooth,
    NumericComparison,
    ResponseFactorCalcModeEnum,
)

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math

class CubicSpline:  # Class
    def __init__(self) -> None: ...
    def Fit(
        self,
        x: List[float],
        y: List[float],
        startSlope: float = ...,
        endSlope: float = ...,
        debug: bool = ...,
    ) -> None: ...
    def FitAndEval(
        self,
        x: List[float],
        y: List[float],
        xs: List[float],
        startSlope: float = ...,
        endSlope: float = ...,
        debug: bool = ...,
    ) -> List[float]: ...
    def Eval(self, x: List[float], debug: bool = ...) -> List[float]: ...

class DataOperations:  # Class
    def __init__(self) -> None: ...

    RelativePrecision: float = ...  # static # readonly

    @staticmethod
    def Spline(
        data: IData,
        samples: int,
        startX: Optional[float] = ...,
        endX: Optional[float] = ...,
    ) -> IEquidistantData: ...
    @staticmethod
    def ExtrapolateData(
        data: IData, rangeToExtrapolateData: List[float]
    ) -> List[float]: ...
    @staticmethod
    def ScaleLinear(data: IData, scale: float) -> IData: ...
    @staticmethod
    def Add(data1: IData, data2: IData) -> IData: ...
    @staticmethod
    def Equalize(
        data1: IData, data2: IData, mode: EqualizeMode = ...
    ) -> IEquidistantData: ...
    @staticmethod
    def Extract(data: IData, xstart: float, xend: float) -> IData: ...
    @staticmethod
    def GetYfromIndex(data: IData, index: int) -> Optional[float]: ...
    @staticmethod
    def Transform(
        data: IData, d0from: float, d1from: float, d0to: float, d1to: float, axis: Axis
    ) -> IData: ...
    @staticmethod
    def GetXfromIndex(data: IData, index: int) -> Optional[float]: ...
    @overload
    @staticmethod
    def GetYMinMax(data: IData, min: float, max: float) -> None: ...
    @overload
    @staticmethod
    def GetYMinMax(
        data: IData, min: float, max: float, inclusiveStart: int, exclusiveEnd: int
    ) -> None: ...
    @staticmethod
    def GetIndexFromXvalue(data: IData, xvalue: float) -> int: ...
    @staticmethod
    def AreConsistent(data1: IData, data2: IData) -> bool: ...
    @staticmethod
    def Sub(data1: IData, data2: IData) -> IData: ...
    @staticmethod
    def InterpolateLinear(
        t1: float, data1: IData, t2: float, data2: IData, t: float
    ) -> IData: ...
    @staticmethod
    def UnreelData(data: IData) -> IData: ...

class FloatingPointOperations:  # Class
    RelativePrecision: float = ...  # static # readonly
    RetentionTimeMaxInMinutes: float  # static # readonly
    RetentionTimeMinInMinutes: float  # static # readonly
    RetentionTimeUndefined: float  # static # readonly

    @overload
    @staticmethod
    def PearsonCorrelation(
        dataArray1: List[float],
        dataArray2: List[float],
        inclusiveStart: int,
        exclusiveEnd: int,
        noiseLevel: Optional[float],
        noiseVariance: Optional[float],
        yintercept: float,
        slope: float,
        threshold: Optional[float],
    ) -> float: ...
    @overload
    @staticmethod
    def PearsonCorrelation(
        dataArray1: List[float], dataArray2: List[float]
    ) -> float: ...
    @staticmethod
    def AreRelativeEqual(number1: float, number2: float) -> bool: ...
    @overload
    @staticmethod
    def AreNumbersEqual(
        number1: float,
        number2: float,
        comparisonMode: NumericComparison,
        precision: float,
    ) -> bool: ...
    @overload
    @staticmethod
    def AreNumbersEqual(
        number1: Optional[float],
        number2: Optional[float],
        comparisonMode: NumericComparison,
        precision: float,
    ) -> bool: ...
    @staticmethod
    def LinearNormalization(dataArray: List[float]) -> None: ...
    @staticmethod
    def ReadPercentFromString(valueToConvert: str) -> float: ...
    @overload
    @staticmethod
    def LinearRegression(
        dataArray1: List[float],
        dataArray2: List[float],
        inclusiveStart: int,
        exclusiveEnd: int,
        yintercept: float,
        slope: float,
    ) -> float: ...
    @overload
    @staticmethod
    def LinearRegression(
        dataArray1: List[float],
        dataArray2: List[float],
        inclusiveStart: int,
        exclusiveEnd: int,
        noiseLevel: Optional[float],
        noiseVariance: Optional[float],
        yintercept: float,
        slope: float,
        thres: Optional[float],
    ) -> float: ...

class LoessInterpolator(ISmooth):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, bandwidth: float, robustnessIters: int) -> None: ...

    DefaultBandwidth: float = ...  # static # readonly
    DefaultRobustnessIters: int = ...  # static # readonly

    Name: str  # readonly

    def Smooth(self, xval: List[float], yval: List[float]) -> List[float]: ...

class MathException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.ArgumentException,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...

class MathModel(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Exponential: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModel = (
        ...
    )  # static # readonly
    Linear: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModel = (
        ...
    )  # static # readonly
    Logarithmic: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModel = (
        ...
    )  # static # readonly
    Quadratic: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModel = (
        ...
    )  # static # readonly

class MathModelCoefficients:  # Class
    def __init__(self, a: float, b: float, c: float) -> None: ...

    A: float  # readonly
    B: float  # readonly
    C: float  # readonly

class MathModels:  # Class
    @staticmethod
    def ComputeRelativeResidual(
        residual: Optional[float],
        amount: Optional[float],
        response: Optional[float],
        responseFactorCalcMode: ResponseFactorCalcModeEnum,
    ) -> float: ...
    @staticmethod
    def QuadraticReverseCompute(
        coefficients: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModelCoefficients,
        y: float,
    ) -> float: ...
    @staticmethod
    def ReverseCompute(
        mathModel: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModel,
        coefficients: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModelCoefficients,
        y: float,
    ) -> float: ...
    @staticmethod
    def Compute(
        mathModel: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModel,
        coefficients: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModelCoefficients,
        x: float,
    ) -> float: ...
    @staticmethod
    def GetConnectPoint(
        mathModel: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModel,
        coefficients: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModelCoefficients,
        minValue: float,
        minValueIsOnX: bool,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathPoint: ...
    @staticmethod
    def ComputeRelativeResidualPerHistoryPoint(
        modelType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModel,
        coefficients: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModelCoefficients,
        historyPointAmount: Optional[float],
        historyPointResponse: Optional[float],
        responseFactorCalcMode: ResponseFactorCalcModeEnum,
    ) -> float: ...
    @staticmethod
    def ComputeResidualPerHistoryPoint(
        modelType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModel,
        coefficients: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathModelCoefficients,
        historyPointAmount: Optional[float],
        historyPointResponse: Optional[float],
        responseFactorCalcMode: ResponseFactorCalcModeEnum,
    ) -> Optional[float]: ...

class MathPoint:  # Struct
    def __init__(self, x: float, y: float) -> None: ...

    X: float  # readonly
    Y: float  # readonly

    def GetHashCode(self) -> int: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(
        self, other: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Math.MathPoint
    ) -> bool: ...

class SavitzkyGolay(ISmooth):  # Class
    @overload
    def __init__(self, coefficients: List[float]) -> None: ...
    @overload
    def __init__(self, coefficients: List[float], name: str) -> None: ...

    Name: str  # readonly

    @overload
    def Smooth(self, y: List[float]) -> List[float]: ...
    @overload
    def Smooth(self, x: List[float], y: List[float]) -> List[float]: ...
    @overload
    def Derive(self, x: List[float], y: List[float]) -> List[float]: ...
    @overload
    def Derive(self, xstep: float, y: List[float]) -> List[float]: ...

class SavitzkyGolayFilterCoefficients:  # Class
    Derive1stCubicNp11: List[float]  # static # readonly
    Derive1stCubicNp111: List[float]  # static # readonly
    Derive1stCubicNp13: List[float]  # static # readonly
    Derive1stCubicNp131: List[float]  # static # readonly
    Derive1stCubicNp15: List[float]  # static # readonly
    Derive1stCubicNp151: List[float]  # static # readonly
    Derive1stCubicNp17: List[float]  # static # readonly
    Derive1stCubicNp19: List[float]  # static # readonly
    Derive1stCubicNp21: List[float]  # static # readonly
    Derive1stCubicNp23: List[float]  # static # readonly
    Derive1stCubicNp25: List[float]  # static # readonly
    Derive1stCubicNp27: List[float]  # static # readonly
    Derive1stCubicNp29: List[float]  # static # readonly
    Derive1stCubicNp301: List[float]  # static # readonly
    Derive1stCubicNp31: List[float]  # static # readonly
    Derive1stCubicNp33: List[float]  # static # readonly
    Derive1stCubicNp35: List[float]  # static # readonly
    Derive1stCubicNp37: List[float]  # static # readonly
    Derive1stCubicNp39: List[float]  # static # readonly
    Derive1stCubicNp41: List[float]  # static # readonly
    Derive1stCubicNp43: List[float]  # static # readonly
    Derive1stCubicNp45: List[float]  # static # readonly
    Derive1stCubicNp47: List[float]  # static # readonly
    Derive1stCubicNp49: List[float]  # static # readonly
    Derive1stCubicNp5: List[float]  # static # readonly
    Derive1stCubicNp51: List[float]  # static # readonly
    Derive1stCubicNp53: List[float]  # static # readonly
    Derive1stCubicNp55: List[float]  # static # readonly
    Derive1stCubicNp57: List[float]  # static # readonly
    Derive1stCubicNp59: List[float]  # static # readonly
    Derive1stCubicNp69: List[float]  # static # readonly
    Derive1stCubicNp7: List[float]  # static # readonly
    Derive1stCubicNp79: List[float]  # static # readonly
    Derive1stCubicNp89: List[float]  # static # readonly
    Derive1stCubicNp9: List[float]  # static # readonly
    Derive1stCubicNp99: List[float]  # static # readonly
    SmoothNp11: List[float]  # static # readonly
    SmoothNp13: List[float]  # static # readonly
    SmoothNp15: List[float]  # static # readonly
    SmoothNp17: List[float]  # static # readonly
    SmoothNp19: List[float]  # static # readonly
    SmoothNp21: List[float]  # static # readonly
    SmoothNp23: List[float]  # static # readonly
    SmoothNp25: List[float]  # static # readonly
    SmoothNp27: List[float]  # static # readonly
    SmoothNp29: List[float]  # static # readonly
    SmoothNp3: List[float]  # static # readonly
    SmoothNp31: List[float]  # static # readonly
    SmoothNp33: List[float]  # static # readonly
    SmoothNp35: List[float]  # static # readonly
    SmoothNp37: List[float]  # static # readonly
    SmoothNp39: List[float]  # static # readonly
    SmoothNp41: List[float]  # static # readonly
    SmoothNp43: List[float]  # static # readonly
    SmoothNp45: List[float]  # static # readonly
    SmoothNp47: List[float]  # static # readonly
    SmoothNp49: List[float]  # static # readonly
    SmoothNp5: List[float]  # static # readonly
    SmoothNp51: List[float]  # static # readonly
    SmoothNp53: List[float]  # static # readonly
    SmoothNp55: List[float]  # static # readonly
    SmoothNp57: List[float]  # static # readonly
    SmoothNp59: List[float]  # static # readonly
    SmoothNp7: List[float]  # static # readonly
    SmoothNp9: List[float]  # static # readonly

class Statistical:  # Class
    @staticmethod
    def StdDeviation(x: List[float]) -> float: ...
    @overload
    @staticmethod
    def Variance(x: List[float], inclusiveStart: int, exclusiveEnd: int) -> float: ...
    @overload
    @staticmethod
    def Variance(x: List[float]) -> float: ...

class TriDiagonalMatrixF:  # Class
    def __init__(self, n: int) -> None: ...

    A: List[float]
    B: List[float]
    C: List[float]

    def __getitem__(self, row: int, col: int) -> float: ...
    def __setitem__(self, row: int, col: int, value_: float) -> None: ...
    N: int  # readonly

    def Solve(self, d: List[float]) -> List[float]: ...
    def ToDisplayString(self, fmt: str = ..., prefix: str = ...) -> str: ...
