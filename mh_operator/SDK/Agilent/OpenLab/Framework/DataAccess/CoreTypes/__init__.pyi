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

from . import Exceptions, Math, Utilities

# Discovered Generic TypeVars:
T = TypeVar("T")

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.CoreTypes

class ApprovalLevelType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IApprovalLevelType
):  # Class
    def __init__(self) -> None: ...

    Comment: str
    EntryBy: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UserLinkType
    EntryDate: System.DateTime
    LevelName: str
    LevelNo: int
    Reason: str

class ApprovalsType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IApprovalsType
):  # Class
    def __init__(self) -> None: ...

    Levels: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ApprovalLevelType
    ]

class AuditTrailEntryType:  # Class
    def __init__(self) -> None: ...

    Date: System.DateTime
    Description: str
    EntryBy: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UserLinkType
    Reason: str
    UserText: Any

class Axis(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    X: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Axis = ...  # static # readonly
    Y: Agilent.OpenLab.Framework.DataAccess.CoreTypes.Axis = ...  # static # readonly

class BackgroundSourceType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DesignatedBackgroundSpectrum: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.BackgroundSourceType
    ) = ...  # static # readonly
    DesignatedTimeRange: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.BackgroundSourceType
    ) = ...  # static # readonly
    MissingSpectra: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.BackgroundSourceType
    ) = ...  # static # readonly
    PeakEnd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.BackgroundSourceType = (
        ...
    )  # static # readonly
    PeakStart: Agilent.OpenLab.Framework.DataAccess.CoreTypes.BackgroundSourceType = (
        ...
    )  # static # readonly
    PeakStartAndEnd: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.BackgroundSourceType
    ) = ...  # static # readonly

class BaseExtractionParameters(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IExtractionParameters
):  # Class
    LongDisplayString: str  # readonly
    ShortDisplayString: str  # readonly

    @overload
    def ShiftTimeValues(self, delta: float) -> None: ...
    @overload
    def ShiftTimeValues(
        self,
        delta: float,
        timeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> None: ...
    def Serialize(self) -> str: ...

class CalibrationCurveCoeffType:  # Class
    def __init__(self) -> None: ...

    A: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    B: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    C: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    D: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    E: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    F: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType

class CalibrationCurveOriginEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Connect: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveOriginEnum
    ) = ...  # static # readonly
    Force: Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveOriginEnum = (
        ...
    )  # static # readonly
    Include: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveOriginEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveOriginEnum
    ) = ...  # static # readonly

class CalibrationCurveType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    AreRelativeValues: bool
    AreRelativeValuesSpecified: bool
    CalibrationLevels: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationLevelType
    ]
    Coefficients: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveCoeffType
    )
    CorrCoefficient: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    DetermCoefficient: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Formula: str
    Info: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectInfoType
    Origin: Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveOriginEnum
    Residual: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseFactorCalcMode: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ResponseFactorCalcModeEnum
    )
    ResponseFactorCalcModeSpecified: bool
    ResponseFactorRSDPercent: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseFactorStdDev: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Scale: str
    Type: Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum
    TypeDescription: str
    WeightType: str

class CalibrationCurveTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AverageRF: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum
    ) = ...  # static # readonly
    Cubic: Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum = (
        ...
    )  # static # readonly
    Custom: Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum = (
        ...
    )  # static # readonly
    Exponential: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum
    ) = ...  # static # readonly
    Linear: Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum = (
        ...
    )  # static # readonly
    LogLog: Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum = (
        ...
    )  # static # readonly
    Logarithmic: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum
    ) = ...  # static # readonly
    Piecewise: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum
    ) = ...  # static # readonly
    Power: Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum = (
        ...
    )  # static # readonly
    Quadratic: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum
    ) = ...  # static # readonly

class CalibrationHistoryType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationHistoryType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    Amount: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    AmountAbs: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    DataFileName: str
    ProcessedBy: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UserLinkType
    ProcessedDate: System.DateTime
    ProcessedDateSpecified: bool
    RelativeResidual: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    RelativeResidualPercent: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Residual: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Response: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseAbs: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    SampleName: str
    Valid: bool
    ValidSpecified: bool

class CalibrationLevelType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationLevelType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    Amount: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    AverageAmountAbs: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    AverageResponse: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    AverageResponseAbs: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    CalibrationHistories: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationHistoryType
    ]
    Level: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    RelativeResidual: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    RelativeResidualPercent: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Residual: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseFactor: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseFactorRelStdDev: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseFactorStdDev: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Valid: bool
    ValidSpecified: bool

class ChromAcquisitionDetails(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromAcquisitionDetails
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, isIntRawData: bool) -> None: ...

    IsIntRawData: bool  # readonly

class ChromData(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
    ],
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISubtractableData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IShiftableData,
):  # Class
    def __init__(
        self,
        data: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData,
        xunit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit,
        yunit: str,
    ) -> None: ...

    ChromAcquisitionDetails: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromAcquisitionDetails
    )
    Data: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData  # readonly
    MsAcquisitionDetails: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsAcquisitionDetails
    )
    SignalDescription: str
    SignalName: str
    XUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit  # readonly
    YUnit: str  # readonly

    def ConvertDataToCompatibleUnit(
        self, data: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData: ...
    @overload
    def Shift(
        self,
        delta: float,
        timeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> None: ...
    @overload
    def Shift(self, delta: float) -> None: ...
    def Subtract(
        self, dataToSubtract: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
    ) -> None: ...
    def Clone(self) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData: ...

class ChromDataEx(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISubtractableData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromDataEx,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IShiftableData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromDataEx
    ],
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
    ],
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData,
):  # Class
    @overload
    def __init__(
        self,
        data: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData,
        xUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit,
        yUnit: str,
    ) -> None: ...
    @overload
    def __init__(
        self,
        data: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData,
        xUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit,
        yUnit: str,
        originalName: str,
        dataSlope: Optional[float],
        dataIntercept: Optional[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        data: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData,
        xUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit,
        yUnit: str,
        originalName: str,
        dataSlope: Optional[float],
        dataIntercept: Optional[float],
        yAxisScalingFactor: Optional[float],
    ) -> None: ...

    DataIntercept: Optional[float]  # readonly
    DataSlope: Optional[float]  # readonly
    OrginalName: str  # readonly
    YScalingFactor: Optional[float]  # readonly

class ChromatogramExtractionParameters(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IExtractionParameters,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.BaseExtractionParameters,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        extractionType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        extractionType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionType,
        extractionTimeRange: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeRange,
        extractionTimeRangeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> None: ...
    @overload
    def __init__(
        self, neutralMass: float, intervalLow: float, intervalHigh: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        neutralMass: float,
        intervalLow: float,
        intervalHigh: float,
        extractionTimeRange: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeRange,
        extractionTimeRangeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> None: ...

    ExtractionTimeRange: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeRange
    ExtractionTimeRangeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit
    ExtractionType: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionType
    )
    IntervalHigh: float
    IntervalLow: float
    LongDisplayString: str  # readonly
    MsExtractionParameters: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsExtractionParameters
    )
    NeutralMass: float
    ShortDisplayString: str  # readonly

    def Serialize(self) -> str: ...

class ChromatogramExtractionType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    BPC: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionType = (
        ...
    )  # static # readonly
    EIC: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionType = (
        ...
    )  # static # readonly
    SIM: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionType = (
        ...
    )  # static # readonly
    TIC: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionType = (
        ...
    )  # static # readonly

class Data(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData
    ],
):  # Class
    def __init__(self, xValues: List[float], yValues: List[float]) -> None: ...

    XValues: List[float]  # readonly
    YValues: List[float]  # readonly

    def Shift(self, delta: float) -> None: ...
    def Subtract(
        self, dataToSubtract: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData
    ) -> None: ...
    def Clone(self) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData: ...

class DetectorType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Adc: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Afc: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Ce: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Dad: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Dfpd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Ecd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Elsd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Fid: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Fld: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Fpd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Mecd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Ms: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Msms: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Mwd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Npd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Rid: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Tcd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Tst: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Unknown: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Uv: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly
    Vwd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType = (
        ...
    )  # static # readonly

class DoubleType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ValueBaseType,
):  # Class
    def __init__(self) -> None: ...

    Val: float

class DoubleTypeExtensions:  # Class
    @overload
    @staticmethod
    def Equals(
        double1: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
        double2: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
    ) -> bool: ...
    @overload
    @staticmethod
    def Equals(
        double1: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
        double2: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
        comparisonMode: Agilent.OpenLab.Framework.DataAccess.CoreTypes.NumericComparison,
        precision: float,
    ) -> bool: ...
    @overload
    @staticmethod
    def GetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
    ) -> float: ...
    @overload
    @staticmethod
    def GetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
        defaultValue: float,
    ) -> float: ...
    @overload
    @staticmethod
    def TryGetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
    ) -> Optional[float]: ...
    @overload
    @staticmethod
    def TryGetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
        defaultValue: float,
    ) -> float: ...
    @overload
    @staticmethod
    def DoubleTypeEquals(
        double1: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
        double2: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
    ) -> bool: ...
    @overload
    @staticmethod
    def DoubleTypeEquals(
        double1: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
        double2: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
        comparisonMode: Agilent.OpenLab.Framework.DataAccess.CoreTypes.NumericComparison,
        precision: float,
    ) -> bool: ...
    @staticmethod
    def DoubleTypeToString(
        doubleType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IDoubleType,
    ) -> str: ...

class EqualizeMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Combined: Agilent.OpenLab.Framework.DataAccess.CoreTypes.EqualizeMode = (
        ...
    )  # static # readonly
    First: Agilent.OpenLab.Framework.DataAccess.CoreTypes.EqualizeMode = (
        ...
    )  # static # readonly
    Overlap: Agilent.OpenLab.Framework.DataAccess.CoreTypes.EqualizeMode = (
        ...
    )  # static # readonly
    Second: Agilent.OpenLab.Framework.DataAccess.CoreTypes.EqualizeMode = (
        ...
    )  # static # readonly

class EquidistantData(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IEquidistantData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData
    ],
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IEquidistantData
    ],
):  # Class
    def __init__(self, yValues: List[float], xMin: float, xStep: float) -> None: ...

    XMin: float  # readonly
    XStep: float  # readonly
    YValues: List[float]  # readonly

    def Shift(self, delta: float) -> None: ...
    def Subtract(
        self, dataToSubtract: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData
    ) -> None: ...

class GenericAnalyticalResultDataInfo(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IGenericAnalyticalResultDataInfo
):  # Class
    def __init__(self) -> None: ...

    DataChannelDescription: str
    DataChannelId: str
    DataChannelName: str
    DataContentId: str
    DataContentSequenceNumber: str
    DataContentType: str
    RawDataFilePath: str
    TraceId: str

class IApprovalLevelType(object):  # Interface
    Comment: str
    EntryBy: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UserLinkType
    EntryDate: System.DateTime
    LevelName: str
    LevelNo: int
    Reason: str

class IApprovalsType(object):  # Interface
    Levels: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ApprovalLevelType
    ]

class ICalibrationCurveType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Interface
    AreRelativeValues: bool
    AreRelativeValuesSpecified: bool
    CalibrationLevels: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationLevelType
    ]
    Coefficients: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveCoeffType
    )
    CorrCoefficient: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    DetermCoefficient: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Formula: str
    Info: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectInfoType
    Origin: Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveOriginEnum
    Residual: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseFactorCalcMode: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ResponseFactorCalcModeEnum
    )
    ResponseFactorCalcModeSpecified: bool
    ResponseFactorRSDPercent: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseFactorStdDev: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Scale: str
    Type: Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationCurveTypeEnum
    TypeDescription: str
    WeightType: str

class ICalibrationHistoryType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot
):  # Interface
    Amount: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    AmountAbs: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    DataFileName: str
    ProcessedBy: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UserLinkType
    ProcessedDate: System.DateTime
    ProcessedDateSpecified: bool
    RelativeResidual: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    RelativeResidualPercent: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Residual: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Response: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseAbs: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    SampleName: str
    Valid: bool
    ValidSpecified: bool

class ICalibrationLevelType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot
):  # Interface
    Amount: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    AverageAmountAbs: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    AverageResponse: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    AverageResponseAbs: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    CalibrationHistories: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationHistoryType
    ]
    Level: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    RelativeResidual: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    RelativeResidualPercent: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Residual: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseFactor: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseFactorRelStdDev: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    ResponseFactorStdDev: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    Valid: bool
    ValidSpecified: bool

class IChromAcquisitionDetails(object):  # Interface
    IsIntRawData: bool  # readonly

class IChromData(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
    ],
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IShiftableData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISubtractableData,
):  # Interface
    ChromAcquisitionDetails: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromAcquisitionDetails
    )  # readonly
    Data: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData  # readonly
    MsAcquisitionDetails: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsAcquisitionDetails
    )  # readonly
    SignalDescription: str
    SignalName: str
    XUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit  # readonly
    YUnit: str  # readonly

class IChromDataEx(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
    ],
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IShiftableData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISubtractableData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromDataEx
    ],
):  # Interface
    DataIntercept: Optional[float]  # readonly
    DataSlope: Optional[float]  # readonly
    OrginalName: str  # readonly
    YScalingFactor: Optional[float]  # readonly

class ICloneableData(object):  # Interface
    def Clone(self) -> T: ...

class IData(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData
    ]
):  # Interface
    XValues: List[float]  # readonly
    YValues: List[float]  # readonly

    def Shift(self, delta: float) -> None: ...
    def Subtract(
        self, dataToSubtract: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData
    ) -> None: ...

class IDoubleType(object):  # Interface
    Val: float

class IEquidistantData(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData
    ],
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IEquidistantData
    ],
):  # Interface
    XMin: float  # readonly
    XStep: float  # readonly

class IExtractionParameters(object):  # Interface
    LongDisplayString: str  # readonly
    ShortDisplayString: str  # readonly

    @overload
    def ShiftTimeValues(self, delta: float) -> None: ...
    @overload
    def ShiftTimeValues(
        self,
        delta: float,
        timeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> None: ...
    def Serialize(self) -> str: ...

class IGenericAnalyticalResultDataInfo(object):  # Interface
    DataChannelDescription: str  # readonly
    DataChannelId: str  # readonly
    DataChannelName: str  # readonly
    DataContentId: str  # readonly
    DataContentSequenceNumber: str  # readonly
    DataContentType: str  # readonly
    RawDataFilePath: str  # readonly
    TraceId: str  # readonly

class IIntegerType(object):  # Interface
    Val: int

class IMethodConfigurationType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Interface
    MethodDescription: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodSectionType
    Ver: int

class IMethodItemBaseType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot
):  # Interface
    ID: str
    Name: str

class IMethodParameterType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodItemBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Interface
    Unit: str
    Value: str

class IMethodRowType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot
):  # Interface
    Parameters: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodParameterType
    ]

class IMethodSectionType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodItemBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Interface
    Parameters: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodParameterType
    ]
    Sections: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodSectionType
    ]
    Tables: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodTableType
    ]

class IMethodTableType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodItemBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Interface
    Rows: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodRowType
    ]

class IMsAcquisitionDetails(object):  # Interface
    CollisionEnergy: float  # readonly
    FragmentorIsDynamic: bool  # readonly
    FragmentorVoltage: float  # readonly
    IonPolarity: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonPolarity  # readonly
    IonizationMode: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode
    )  # readonly
    MsLevels: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsLevel  # readonly
    MsScanType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType  # readonly

class IMsRawDataInformation(object):  # Interface
    AcquisitionDetails: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsAcquisitionDetails
    )  # readonly
    BasicSignalExtractionParams: Iterable[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionParameters
    ]  # readonly
    FragmentVoltages: List[float]  # readonly
    SIMIons: List[float]  # readonly

class IObjectBaseType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot
):  # Interface
    Id: str

    def SetNewId(self, id: System.Guid) -> None: ...
    def GetGuid(self) -> System.Guid: ...

class IObjectInfoType(object):  # Interface
    Approvals: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ApprovalsType
    AuditTrail: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.AuditTrailEntryType
    ]
    CreatedBy: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UserLinkType
    CreatedDate: System.DateTime
    CreatedDateSpecified: bool
    LastModifiedBy: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UserLinkType
    LastModifiedDate: System.DateTime
    LastModifiedDateSpecified: bool
    Status: str

class IObjectRoot(object):  # Interface
    ...

class IShiftableData(object):  # Interface
    @overload
    def Shift(
        self,
        delta: float,
        timeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> None: ...
    @overload
    def Shift(self, delta: float) -> None: ...

class ISignalInformation(object):  # Interface
    MSRawDataInformation: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsRawDataInformation
    )  # readonly

class ISmooth(object):  # Interface
    Name: str  # readonly

    def Smooth(self, x: List[float], y: List[float]) -> List[float]: ...

class ISpectraData(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectraData
    ]
):  # Interface
    Data: Iterable[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData
    ]  # readonly
    SpectraDescription: str  # readonly
    SpectraName: str  # readonly

    def CountDataPoints(self) -> int: ...
    @overload
    def GetSpectrum(
        self, time: float
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData: ...
    @overload
    def GetSpectrum(
        self,
        time: float,
        timeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData: ...
    @overload
    def GetSpectrum(
        self,
        spectrumExtractionParameters: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExtractionParameters,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData: ...
    @overload
    def Shift(self, delta: float) -> None: ...
    @overload
    def Shift(
        self,
        delta: float,
        timeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> None: ...

class ISpectrumData(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData
    ],
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IShiftableData,
):  # Interface
    Data: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData  # readonly
    Description: str
    ExprType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr
    MsAcquisitionDetails: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsAcquisitionDetails
    )  # readonly
    Name: str
    Time: Optional[float]  # readonly
    TimeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit
    XUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit  # readonly
    YUnit: str  # readonly

class ISubtractableData(object):  # Interface
    def Subtract(
        self, dataToSubtract: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
    ) -> None: ...

class IntegerType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IIntegerType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ValueBaseType,
):  # Class
    def __init__(self) -> None: ...

    Val: int

class IonPolarity(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Mixed: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonPolarity = (
        ...
    )  # static # readonly
    Negative: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonPolarity = (
        ...
    )  # static # readonly
    Positive: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonPolarity = (
        ...
    )  # static # readonly
    Unassigned: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonPolarity = (
        ...
    )  # static # readonly

class IonizationMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Apci: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    Appi: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    CI: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    EI: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    Esi: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    ICP: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    JetStream: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    Maldi: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    Mixed: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    MsChip: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    NanoEsi: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly
    Unspecified: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode = (
        ...
    )  # static # readonly

class MethodConfigurationType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodConfigurationType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    MethodDescription: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodSectionType
    Ver: int

class MethodParameterType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodItemBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodParameterType,
):  # Class
    def __init__(self) -> None: ...

    ID: str
    Name: str
    Unit: str
    Value: str

class MethodRowType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodRowType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    Parameters: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodParameterType
    ]

class MethodSectionType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodItemBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodSectionType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    ID: str
    Name: str
    Parameters: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodParameterType
    ]
    Sections: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodSectionType
    ]
    Tables: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodTableType
    ]

class MethodTableType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodTableType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodItemBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    ID: str
    Name: str
    Rows: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MethodRowType
    ]

class MsAcquisitionDetails(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsAcquisitionDetails
):  # Class
    @overload
    def __init__(
        self,
        ionizationMode: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode,
        ionPolarity: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonPolarity,
        msScanType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    CollisionEnergy: float
    FragmentorIsDynamic: bool
    FragmentorVoltage: float
    IonPolarity: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonPolarity
    IonizationMode: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode
    MsLevels: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsLevel
    MsScanType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType

class MsExtractionParameters:  # Class
    def __init__(self) -> None: ...

    CollisionEnergy: float
    FragmentorVoltage: float
    IonPolarity: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonPolarity
    IonizationMode: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IonizationMode
    MSScanType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType

class MsLevel(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    All: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsLevel = (
        ...
    )  # static # readonly
    MS: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsLevel = (
        ...
    )  # static # readonly
    MSMS: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsLevel = (
        ...
    )  # static # readonly

class MsRawDataInformation(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsRawDataInformation
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        acquisitionDetails: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsAcquisitionDetails,
        simIons: List[float],
        basicSignalExtractionParams: Iterable[
            Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionParameters
        ],
        fragmentVoltages: List[float],
    ) -> None: ...

    AcquisitionDetails: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsAcquisitionDetails
    )  # readonly
    BasicSignalExtractionParams: Iterable[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionParameters
    ]  # readonly
    FragmentVoltages: List[float]  # readonly
    SIMIons: List[float]

class MsScanType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    All: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    AllMS: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    AllMSN: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    HighResolutionScan: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    MultipleReaction: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    NeutralGain: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    NeutralLoss: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    PrecursorIon: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    ProductIon: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    Scan: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    SelectedIon: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    TotalIon: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly
    Unspecified: Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsScanType = (
        ...
    )  # static # readonly

class NumericComparison(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AbsolutePrecision: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.NumericComparison
    ) = ...  # static # readonly
    Exact: Agilent.OpenLab.Framework.DataAccess.CoreTypes.NumericComparison = (
        ...
    )  # static # readonly
    RelativePrecision: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.NumericComparison
    ) = ...  # static # readonly

class ObjectBaseType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Class
    Id: str

    def SetNewId(self, id: System.Guid) -> None: ...
    def GetGuid(self) -> System.Guid: ...

class ObjectInfoType(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectInfoType
):  # Class
    def __init__(self) -> None: ...

    Approvals: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ApprovalsType
    AuditTrail: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.AuditTrailEntryType
    ]
    CreatedBy: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UserLinkType
    CreatedDate: System.DateTime
    CreatedDateSpecified: bool
    LastModifiedBy: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UserLinkType
    LastModifiedDate: System.DateTime
    LastModifiedDateSpecified: bool
    Status: str

class ObjectRootExtensions:  # Class
    @staticmethod
    def CloneBySerialization(source: T, useTempFile: bool = ...) -> T: ...
    @overload
    @staticmethod
    def Compare(
        source: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
        target: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
        ignoreIdProperties: bool,
    ) -> bool: ...
    @overload
    @staticmethod
    def Compare(
        source: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
        target: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
        ignoreIdProperties: bool,
        comparisonResults: str,
    ) -> bool: ...
    @overload
    @staticmethod
    def Compare(
        source: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
        target: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
        ignoreIdProperties: bool,
        maxDiffCount: int,
        comparisonResults: str,
    ) -> bool: ...
    @staticmethod
    def Clone(
        sourceObj: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
        useParallelCloning: bool = ...,
        cancellationToken: System.Threading.CancellationToken = ...,
    ) -> Any: ...

class ResponseFactorCalcModeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AmountPerResponse: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ResponseFactorCalcModeEnum
    ) = ...  # static # readonly
    ResponsePerAmount: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ResponseFactorCalcModeEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ResponseFactorCalcModeEnum
    ) = ...  # static # readonly

class SeparationTechnology(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CapillaryElectrophoresis: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.SeparationTechnology
    ) = ...  # static # readonly
    GasChromatography: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.SeparationTechnology
    ) = ...  # static # readonly
    LiquidChromatography: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.SeparationTechnology
    ) = ...  # static # readonly
    MassSpectrometry: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.SeparationTechnology
    ) = ...  # static # readonly
    Unknown: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SeparationTechnology = (
        ...
    )  # static # readonly

class SignalInfo:  # Class
    def __init__(self, shortName: str) -> None: ...

    Channel: str  # readonly
    Detector: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType  # readonly
    DetectorInstance: int  # readonly
    DetectorName: str  # readonly
    Injector: str  # readonly
    Name: str  # readonly
    SeparationTechnology: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.SeparationTechnology
    )  # readonly

    def GetHashCode(self) -> int: ...
    @staticmethod
    def GetSeparationTechnology(
        detector: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DetectorType,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.SeparationTechnology: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(
        self, signalInfo: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SignalInfo
    ) -> bool: ...

class SignalInformation(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISignalInformation
):  # Class
    def __init__(
        self,
        msRawDataInformation: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsRawDataInformation,
    ) -> None: ...

    MSRawDataInformation: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsRawDataInformation
    )  # readonly

class SpectraData(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectraData
    ],
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectraData,
):  # Class
    def __init__(self) -> None: ...

    Data: Iterable[Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData]
    SpectraDescription: str
    SpectraName: str

    @overload
    def Shift(self, delta: float) -> None: ...
    @overload
    def Shift(
        self,
        delta: float,
        timeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> None: ...
    def CountDataPoints(self) -> int: ...
    @overload
    def GetSpectrum(
        self, time: float
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData: ...
    @overload
    def GetSpectrum(
        self,
        time: float,
        timeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData: ...
    @overload
    def GetSpectrum(
        self,
        spectrumExtractionParameters: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExtractionParameters,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData: ...
    def Clone(self) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectraData: ...

class SpectrumData(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IShiftableData,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICloneableData[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData
    ],
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData,
):  # Class
    def __init__(
        self,
        data: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData,
        xunit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit,
        yunit: str,
        time: Optional[float] = ...,
    ) -> None: ...

    Data: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IData  # readonly
    Description: str
    ExprType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr
    MsAcquisitionDetails: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMsAcquisitionDetails
    )
    Name: str
    Time: Optional[float]  # readonly
    TimeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit
    XUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit  # readonly
    YUnit: str  # readonly

    @overload
    def Shift(
        self,
        delta: float,
        timeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> None: ...
    @overload
    def Shift(self, delta: float) -> None: ...
    def Clone(self) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData: ...

class SpectrumExpr(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Apex: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    CancelPeak: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    Downslope1: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    Downslope2: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    Emission: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    Excitation: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    ForceBaseline: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    PeakAll: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    PeakBegin: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    PeakEnd: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    Periodic: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    SmallPeakTop: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    Undefined: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    Unknown: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    Upslope1: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    Upslope2: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly
    Valley: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExpr = (
        ...
    )  # static # readonly

class SpectrumExtractionParameters(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IExtractionParameters,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.BaseExtractionParameters,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        unit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
        extractionTime: float,
    ) -> None: ...

    BackgroundSourceType: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.BackgroundSourceType
    )
    BackgroundTimeRanges: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeRange
    ]
    ForegroundTimeRanges: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeRange
    ]
    LongDisplayString: str  # readonly
    MassWindow: float
    MaxExtractionTime: float
    MinExtractionTime: float
    MsExtractionParameters: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.MsExtractionParameters
    )
    ShortDisplayString: str  # readonly
    SimIonMass: float
    TimeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit

    @staticmethod
    def BuildLongDisplayString(
        minExtractionTime: float,
        maxExtractionTime: float,
        timeUnit: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit,
    ) -> str: ...
    @staticmethod
    def BuildShortDisplayString(maxExtractionTime: float) -> str: ...
    def Serialize(self) -> str: ...

class TimeRange:  # Struct
    def __init__(self, beginTime: float, endTime: float) -> None: ...

    BeginTime: float
    EndTime: float

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class TimeUnit(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Milliseconds: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit = (
        ...
    )  # static # readonly
    Minutes: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit = (
        ...
    )  # static # readonly
    Seconds: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit = (
        ...
    )  # static # readonly
    Unknown: Agilent.OpenLab.Framework.DataAccess.CoreTypes.TimeUnit = (
        ...
    )  # static # readonly

class UserLinkType:  # Class
    def __init__(self) -> None: ...

    Item: Any

class UvChromatogramExtractionParameters(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IExtractionParameters,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.BaseExtractionParameters,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        extractionType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UvChromatogramExtractionType,
        minWavelength: float,
        maxWavelength: float,
        spectraDetectorName: str,
        spectraDetectorInstance: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        extractionType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.UvChromatogramExtractionType,
        spectraDetectorName: str,
        spectraDetectorInstance: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        wavelength: float,
        bandwidth: float,
        spectraDetectorName: str,
        spectraDetectorInstance: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        wavelength: float,
        bandwidth: float,
        referenceWavelength: float,
        referenceBandwidth: float,
        spectraDetectorName: str,
        spectraDetectorInstance: int,
    ) -> None: ...

    Bandwidth: float
    ExtractionType: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.UvChromatogramExtractionType
    )
    LongDisplayString: str  # readonly
    MaxWavelength: float
    MinWavelength: float
    RefBandwidth: float
    RefWavelength: float
    ShortDisplayString: str  # readonly
    SpectraDetectorInstance: int
    SpectraDetectorName: str
    UseReference: bool
    Wavelength: float

    def Serialize(self) -> str: ...

class UvChromatogramExtractionType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ExtractedWavelengthChromatogram: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.UvChromatogramExtractionType
    ) = ...  # static # readonly
    MaxWavelengthChromatogram: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.UvChromatogramExtractionType
    ) = ...  # static # readonly
    TotalWavelengthChromatogram: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.UvChromatogramExtractionType
    ) = ...  # static # readonly

class ValueBaseType:  # Class
    def __init__(self) -> None: ...

    DeclaringType: System.Type  # readonly
    HasResourceContext: bool  # readonly
    PropertyName: str  # readonly

    def SetResourceContext(
        self, runTimeDeclaringType: System.Type, runTimePropertyName: str
    ) -> None: ...

class XUnit(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    MassToCharge: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit = (
        ...
    )  # static # readonly
    Milliseconds: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit = (
        ...
    )  # static # readonly
    Minutes: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit = (
        ...
    )  # static # readonly
    Nanometer: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit = (
        ...
    )  # static # readonly
    Seconds: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit = (
        ...
    )  # static # readonly
    Unknown: Agilent.OpenLab.Framework.DataAccess.CoreTypes.XUnit = (
        ...
    )  # static # readonly
