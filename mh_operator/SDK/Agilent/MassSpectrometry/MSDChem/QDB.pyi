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

# Stubs for namespace: Agilent.MassSpectrometry.MSDChem.QDB

class QDB:  # Class
    def __init__(self) -> None: ...

class QUANT_AUX_REPORTING_INFO:  # Class
    cpndType: str

class QUANT_CALIB_LEVEL_INFO:  # Class
    def __init__(self, dConcentration: float, dResponse: float) -> None: ...

    AverageCounter: int
    Concentration: float
    HasNullConcentration: bool  # readonly
    HasNullResponse: bool  # readonly
    IsValid: bool  # readonly
    Response: float

    @staticmethod
    def IsNullConcentration(dConcentration: float) -> bool: ...
    @staticmethod
    def IsNullResponse(dResponse: float) -> bool: ...

class QUANT_CPNDENTRY:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, other: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY
    ) -> None: ...

    MATRIX_A: int = ...  # static # readonly
    MATRIX_B: int = ...  # static # readonly
    QUANT_ABSOLUTE: int = ...  # static # readonly
    QUANT_AVG_FIRST_LAST: int = ...  # static # readonly
    QUANT_AVG_RESPONSE_FACTOR_FIT: int = ...  # static # readonly
    QUANT_CLOSE_RT: int = ...  # static # readonly
    QUANT_CLOSE_RT_QUAL: int = ...  # static # readonly
    QUANT_DEFAULT_QHITS_MAX: int = ...  # static # readonly
    QUANT_EXTENDED_AREA: int = ...  # static # readonly
    QUANT_GREATEST_QVALUE: int = ...  # static # readonly
    QUANT_GREATEST_RESP: int = ...  # static # readonly
    QUANT_INV_SQ_WEIGHT: int = ...  # static # readonly
    QUANT_INV_WEIGHT: int = ...  # static # readonly
    QUANT_LINEAR_REGRESSION: int = ...  # static # readonly
    QUANT_LIN_REGR_ORIGIN: int = ...  # static # readonly
    QUANT_LOW_FIRST_LAST: int = ...  # static # readonly
    QUANT_MAX_AMU: float = ...  # static # readonly
    QUANT_MINUTES: int = ...  # static # readonly
    QUANT_NOT_AN_ISTD: int = ...  # static # readonly
    QUANT_NO_SUBTRACTION: int = ...  # static # readonly
    QUANT_NO_WEIGHT: int = ...  # static # readonly
    QUANT_NULL_CONC: float  # static
    QUANT_NULL_RESPONSE: float  # static
    QUANT_NUM_CALIB_LEVELS: int = ...  # static # readonly
    QUANT_NUM_QUALIFIER_IONS: int = ...  # static # readonly
    QUANT_PERCENT: int = ...  # static # readonly
    QUANT_QUADRATIC_REGRESSION: int = ...  # static # readonly
    QUANT_QUAD_REGR_ORIGIN: int = ...  # static # readonly
    QUANT_RELATIVE: int = ...  # static # readonly
    QUANT_REPORTALL: int = ...  # static # readonly
    aux: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_AUX_REPORTING_INFO
    calib_level_info: List[Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CALIB_LEVEL_INFO]
    curvefit_type: int
    istd_peak_: int
    qual_addl_info: List[
        Agilent.MassSpectrometry.MSDChem.QDB.QUANT_QUALIFIER_ADDITIONAL_INFO
    ]
    qualifier_ion: List[Agilent.MassSpectrometry.MSDChem.QDB.QUANT_QUALIFIER_ION]
    rt_d_left: float
    rt_d_right: float
    sequentialRecordNumber: int
    target_signal: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_TARGET_SIGNAL
    tgt_addl_info: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_TARGET_ADDITIONAL_INFO

    AreaCorrectionFactor: float
    AreaCorrectionMz20ths: int
    CASid: str
    CompoundName: str
    CompoundType: str
    ConcentrationUnitsName: str
    CurveFitType: int
    CurveWeightType: int
    ExtractWindowType: int
    GCSignalNumber: int
    IsIstd: bool  # readonly
    IsQuantitatedWith: int  # readonly
    IsQuantitatedWithTIC: bool
    IsSemiQuantCompound: bool  # readonly
    IsTargetCompound: bool  # readonly
    IsTimeReference: bool
    MSDatabaseEntryNum: int
    MSDatabaseName: str
    MatrixSpikeAmount: float
    MaxHitsToReport: int
    MaxSignalLevel: float
    MinSignalLevel: float
    PeakSelectCriterion: int
    QualifierRatioMethod: int
    QualifierUncertaintyType: int
    QuantitatedByHeight: bool
    RTDeltaLeft: float
    RTDeltaRight: float
    ReferenceSpectrumName: str
    SampleIstdConc: float
    SequentialRecordNumber: int  # readonly
    SurrogateAmount: float
    TargetIntegPFName: str
    TargetMz20ths: int
    TargetRTMsec: int
    UsesAreaCorrection: bool  # readonly
    UsesLinearCurveFit: bool  # readonly

    @staticmethod
    def ClampToLegalRtRange(dVal: float) -> None: ...
    def GetNumCalibLevels(self) -> int: ...
    def SetLevelResponse(self, usLevelNo0Based: int, dResp: float) -> None: ...
    def SetQualifierPctUncertainty(
        self, usQualNo0Based: int, dPctUnc: float
    ) -> None: ...
    def SetLevelConcentration(self, usLevelNo0Based: int, dConc: float) -> None: ...
    def SetQuantRole(
        self,
        iISTD: Agilent.MassSpectrometry.MSDChem.QDB.QuantDatabaseCompoundRoles,
        fTimeReference: bool,
    ) -> None: ...
    def ClearLevelInfo(self, usLevelNo0Based: int) -> None: ...
    def GetQualifierMz20ths(self, usQualNo0Based: int) -> int: ...
    def SetQuantWithGCSig(self, usSelection: int) -> None: ...
    def GetQualifierPctUncertainty(self, usQualNo0Based: int) -> float: ...
    @staticmethod
    def QUANT_SET_CF_TYPE(a: int, val: int) -> None: ...
    def GetLevelConcentration(self, usLevelNo0Based: int) -> float: ...
    def SetQualifierAreaSummed(self, usQualNo0Based: int, flag: int) -> None: ...
    @staticmethod
    def QUANT_GET_WT_TYPE(a: int) -> int: ...
    def MakeNull(self) -> None: ...
    def SetMatrixLowConc(self, usMatrixID: int, dLowConc: float) -> None: ...
    def SetQualifierIntegPFName(
        self, usQualNo0Based: int, pIntegFileName: str
    ) -> None: ...
    def SetMatrixMinDetLimit(self, usMatrixID: int, dRPD: float) -> None: ...
    def GetMatrixMinDetLimit(self, usMatrixID: int) -> float: ...
    def GetUserDefinedString(self, usUserIndex: int) -> str: ...
    def SetMatrixRelPctDev(self, usMatrixID: int, dRPD: float) -> None: ...
    def SetQualifierMz20ths(self, usQualNo0Based: int, usMz20ths: int) -> None: ...
    def IsISTD(self) -> bool: ...
    def GetQualifierRelResp(self, usQualNo0Based: int) -> float: ...
    def GetRetentionTimeBounds(self, leftBound: int, rightBound: int) -> None: ...
    def SetUserDefinedScalar(self, usUserIndex: int, dValue: float) -> None: ...
    @staticmethod
    def NewCompound(
        phCpnd: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY,
        quantEnvironment: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_ENVIRONMENT,
    ) -> None: ...
    def MakeNullLevelResponse(self, usLevelNo0Based: int) -> None: ...
    @staticmethod
    def GetRtBounds(
        actual_rt: int,
        rt_d_left: float,
        rt_d_right: float,
        rt_win_modifier: int,
        leftBound: int,
        rightBound: int,
    ) -> None: ...
    def SetLevelAverageCount(
        self, usLevelNo0Based: int, usAverageCount: int
    ) -> None: ...
    def GetUserDefinedScalar(self, usUserIndex: int) -> float: ...
    def ClearCalibLevelInfo(self, usLevelNo0Based: int) -> None: ...
    @staticmethod
    def QUANT_GET_CF_TYPE(a: int) -> int: ...
    def GetQualifierIntegPFName(self, usQualNo0Based: int) -> str: ...
    def GetMatrixLowConc(self, usMatrixID: int) -> float: ...
    def SetMatrixHighConc(self, usMatrixID: int, dHighConc: float) -> None: ...
    def MakeNullRecord(
        self, env: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_ENVIRONMENT
    ) -> None: ...
    @staticmethod
    def DeleteCompound(
        hCpnd: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY,
    ) -> None: ...
    def QualifierExists(self, usQualNo0Based: int) -> bool: ...
    def GetQualifierAreaSummed(self, usQualNo0Based: int) -> bool: ...
    def LevelInfoExists(self, usLevelNo0Based: int) -> bool: ...
    @staticmethod
    def QUANT_SET_WT_TYPE(a: int, val: int) -> None: ...
    def GetLevelAverageCount(self, usLevelNo0Based: int) -> int: ...
    def SetQualifierRelResp(self, usQualNo0Based: int, dRelResp: float) -> None: ...
    def GetLevelResponse(self, usLevelNo0Based: int) -> float: ...
    def GetMatrixHighConc(self, usMatrixID: int) -> float: ...
    def SetUserDefinedString(self, usUserIndex: int, pValue: str) -> None: ...
    def GetMatrixRelPctDev(self, usMatrixID: int) -> float: ...
    def ValidateEntry(self, strErrorMessage: str) -> bool: ...

class QUANT_ENVIRONMENT:  # Class
    def __init__(self) -> None: ...

    calStdDirName: str
    calStdFileName: List[str]
    db_timestamp: str
    defUnitsStr: str
    level_id: List[str]
    paramFile: str
    title: str
    unusedLvlConc: List[float]

    UseRTEINT: bool
    corrWin: int
    defCurveFit: int
    defIstdConc: float
    defSampleAmt: float
    internalVersionNum: int
    multiplier: float
    nonRefWin: int
    nonRefWinType: int
    outputType: int
    quantByHeight: int
    refWin: int
    refWinType: int
    rptFileName: str
    rt_radius: int
    runMethod: int
    singleCpndNum: int
    toFile: int
    toPrinter: int
    toScreen: int

    @overload
    def ConvertQuantEnvironment(
        self,
        pOldEnv: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_ENVIRONMENT_PRE_D_00_00,
    ) -> None: ...
    @overload
    def ConvertQuantEnvironment(
        self, pOldEnv: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_ENVIRONMENT_2002
    ) -> None: ...
    def Serialize(self, archive: Any, nVersion: int) -> None: ...

class QUANT_ENVIRONMENT_2002:  # Class
    ...

class QUANT_ENVIRONMENT_PRE_D_00_00:  # Class
    ...

class QUANT_QDB_MEMHANDLE:  # Class
    def __init__(self) -> None: ...

    GetQuantDB: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_QDB_MEMMAP  # readonly

    def StoreQuantDatabase(
        self, pDatabaseContainer: str, pDatabaseComponent: str
    ) -> None: ...
    def LoadQuantDatabase(
        self, pDatabaseContainer: str, pDatabaseComponent: str
    ) -> None: ...

class QUANT_QDB_MEMMAP:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iInitialSizeInEntries: int) -> None: ...

    QUANT_ANY: int = ...  # static # readonly
    QUANT_AREAPCT_UNCALIB_REP: int = ...  # static # readonly
    QUANT_DETAILED_NOGR_REP: int = ...  # static # readonly
    QUANT_DETAILED_REP: int = ...  # static # readonly
    QUANT_DETAILED_SNGL_REP: int = ...  # static # readonly
    QUANT_ISTD: int = ...  # static # readonly
    QUANT_SELECT: int = ...  # static # readonly
    QUANT_SUMMARY_REP: int = ...  # static # readonly
    QUANT_TIMEREF: int = ...  # static # readonly
    dbRec: System.Collections.Generic.List[
        Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY
    ]
    env: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_ENVIRONMENT

    def InsertEntry(
        self,
        hCpnd: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY,
        newEntryLoc0Based: int,
    ) -> None: ...
    def DeleteCalibLvlRange(self, levelStart: int, levelEnd: int) -> None: ...
    def DeleteEntry(self, deletedEntryLoc: int) -> None: ...
    def GetRelatedIstdCpndNum(
        self, cpndSeqNumber: int, pusRelatedIstdCpndNum: int
    ) -> bool: ...
    def IsIstdAnalyte(
        self, hCpnd: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY
    ) -> bool: ...
    def GetNextCpnd(self, indexSize: int, cpndType: int, nextCpndNum: int) -> None: ...
    def ClearCpnds(
        self, fClearLevelsOnly: bool, fBatchMode: bool, msg: str
    ) -> bool: ...
    def GetSizeInEntries(self) -> int: ...
    def UpdateEntry(
        self, hCpnd: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY, entryNo: int
    ) -> None: ...
    def GetCompoundNumber(
        self,
        usCpndNum0Based: int,
        phCpnd: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY,
    ) -> None: ...
    def SetDbTimeStamp(self) -> None: ...
    def GetRelatedIstd(
        self,
        pCpnd: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY,
        pRelatedIstdCpnd: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY,
    ) -> None: ...

class QUANT_QUALIFIER_ADDITIONAL_INFO:  # Class
    @overload
    def __init__(
        self, dPercentUncertainty: float, bAreaSum: bool, strParamFile: str
    ) -> None: ...
    @overload
    def __init__(
        self,
        source: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_QUALIFIER_ADDITIONAL_INFO,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    IsSummed: bool
    ParameterFileName: str
    PercentUncertainty: int

class QUANT_QUALIFIER_ION:  # Class
    @overload
    def __init__(self, dMZ: float, dRelResponse: float) -> None: ...
    @overload
    def __init__(
        self, source: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_QUALIFIER_ION
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    MZ: int
    Rel_Response: int

class QUANT_RESULTS:  # Class
    def __init__(self) -> None: ...

    alternateHitIndex: int
    coeff: List[float]
    istdResponse: float
    modified: int
    nTotalHits: int
    primaryHit: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_SINGLE_HIT
    primaryHitNumber: int
    qual_ratio_hi: List[float]
    qual_ratio_lo: List[float]
    rf: List[float]

    AdjustedExpectedRetentionTime: int
    CompoundRetentionTimeHigh: int
    CompoundRetentionTimeLow: int
    ConstantCalibrationCurveCoefficient: float  # readonly
    IStdCompoundLocation: int
    LinearCalibrationCurveCoefficient: float  # readonly
    QuadraticCalibrationCurveCoefficient: float  # readonly
    Rho: float

    def GetQualifierRatioHigh(self, i32WhichQualifier: int) -> float: ...
    def GetQualifierRatioLow(self, i32WhichQualifier: int) -> float: ...

class QUANT_RSLTFILE_HDR:  # Class
    def __init__(self) -> None: ...

    env: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_ENVIRONMENT

    NumberOfInternalStandards: int  # readonly
    NumberOfResults: int  # readonly
    NumberOfTimeReferenceCompounds: int  # readonly

class QUANT_RSLTFILE_MEMMAP:  # Class
    def __init__(self, fileName: str) -> None: ...

    alternateHits: System.Collections.Generic.List[
        Agilent.MassSpectrometry.MSDChem.QDB.QUANT_SINGLE_HIT
    ]
    header: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_RSLTFILE_HDR
    mainResults: System.Collections.Generic.List[
        Agilent.MassSpectrometry.MSDChem.QDB.QUANT_RSLT_FILE_REC
    ]

    def Save(self) -> None: ...
    def Load(self) -> None: ...
    def InitQuantResult(
        self,
        quantDatabase: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_QDB_MEMMAP,
        numEntries: int,
        nTimeRefs: int,
        nIstds: int,
        rsltFileName: str,
        bSecondPassHack: bool,
    ) -> None: ...

class QUANT_RSLT_FILE_REC:  # Class
    def __init__(self) -> None: ...

    dbEntry: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_CPNDENTRY
    rslt: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_RESULTS

class QUANT_SINGLE_HIT(
    System.IComparable[Agilent.MassSpectrometry.MSDChem.QDB.QUANT_SINGLE_HIT]
):  # Class
    def __init__(self) -> None: ...

    amtRatio: float
    areaCorrResp: float
    determined_amt: float
    ending_baseline: float
    ending_time: int
    groupIndex: int
    group_rt: int
    identified: int
    qValueComputed: int
    qValueKey: int
    qdel: int
    qualifier_end_bl: List[float]
    qualifier_end_time: List[int]
    qualifier_resp: List[float]
    qualifier_rt: List[int]
    qualifier_st_bl: List[float]
    qualifier_st_time: List[int]
    respRatio: float
    response: float
    rtDiffKey: int
    starting_baseline: float
    starting_time: int
    tgt_rt: int

    def CompareTo(
        self, other: Agilent.MassSpectrometry.MSDChem.QDB.QUANT_SINGLE_HIT
    ) -> int: ...

class QUANT_TARGET_ADDITIONAL_INFO:  # Class
    paramFile: str

class QUANT_TARGET_SIGNAL:  # Class
    actual_rt: int
    mz: int

class QuantDatabaseCompoundRoles(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    QUANT_ROLE_ISTD: Agilent.MassSpectrometry.MSDChem.QDB.QuantDatabaseCompoundRoles = (
        ...
    )  # static # readonly
    QUANT_ROLE_SEMIQUANT: (
        Agilent.MassSpectrometry.MSDChem.QDB.QuantDatabaseCompoundRoles
    ) = ...  # static # readonly
    QUANT_ROLE_TARGET_COMPOUND: (
        Agilent.MassSpectrometry.MSDChem.QDB.QuantDatabaseCompoundRoles
    ) = ...  # static # readonly
