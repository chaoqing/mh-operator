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
    BracketingTypeEnum,
    CalibPeakRoleEnum,
    CorrectionFactorType,
    DoubleUnitType,
    IContainer,
    IDaParam,
    IIdentifiedPeakAggregation,
    IIdentParamBaseType,
    IInjectionCompoundType,
    IInjectionContainer,
    IInjectionMeasDataType,
    IInjectionResultType,
    IInjectionSignalResultType,
    IMSSamplePurityResultType,
    IMSSamplePuritySetupType,
    InjectorPositionEnum,
    INonIdentParamBaseType,
    IPeakType,
    ISampleContainer,
    ISampleContextContainer,
    ISampleMeasDataContextType,
    ISampleMeasDataType,
    ISamplePurityContainer,
    ISampleSetupContextType,
    ISampleSetupType,
    ISignalContainer,
    ISignalType,
    LimsIDType,
    MethodRefType,
    ResponseFactorUpdateEnum,
    RetentionTimeUpdateEnum,
    RunTypeAndReplicationType,
    SampleTypeEnum,
    StandardCompoundAmountType,
)

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects

class AcamlExternalReferenceId:  # Class
    def __init__(self, docId: System.Guid, path: str, traceId: str) -> None: ...

    DocId: System.Guid  # readonly
    Path: str  # readonly
    TraceId: str  # readonly

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class AcamlInjectionId:  # Class
    def __init__(self, acamlDocId: System.Guid, injectionId: System.Guid) -> None: ...

    AcamlDocId: System.Guid  # readonly
    InjectionId: System.Guid  # readonly

    def GetHashCode(self) -> int: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(
        self,
        other: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.AcamlInjectionId,
    ) -> bool: ...

class AcamlInjectionSpectrumId:  # Class
    def __init__(
        self, acamlDocId: System.Guid, injectionId: System.Guid, spectrumName: str
    ) -> None: ...

    AcamlDocId: System.Guid  # readonly
    InjectionId: System.Guid  # readonly
    SpectrumName: str  # readonly

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class AcamlSignalId:  # Class
    def __init__(self, docId: System.Guid, signal: ISignalType) -> None: ...

    DocId: System.Guid  # readonly
    SignalId: System.Guid  # readonly
    SignalName: str  # readonly

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class DaParam(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.NonIdentParamBaseType,
    INonIdentParamBaseType,
    IDaParam,
):  # Class
    def __init__(self) -> None: ...

    CalibrationLevel: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    CalibrationStandards: System.Collections.Generic.List[StandardCompoundAmountType]
    DilutionFactors: System.Collections.Generic.List[CorrectionFactorType]
    InternalStandards: System.Collections.Generic.List[StandardCompoundAmountType]
    Multipliers: System.Collections.Generic.List[CorrectionFactorType]
    OrderNo: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    ResponseFactorUpdate: ResponseFactorUpdateEnum
    ResponseFactorUpdateSpecified: bool
    ResponseFactorUpdateWeight: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    )
    RetentionTimeUpdate: RetentionTimeUpdateEnum
    RetentionTimeUpdateSpecified: bool
    RetentionTimeUpdateWeight: Agilent.OpenLab.Framework.DataAccess.CoreTypes.DoubleType
    RunTypes: System.Collections.Generic.List[RunTypeAndReplicationType]
    SampleAmount: DoubleUnitType

class IInjectionMetaData(object):  # Interface
    AcqMethodName: str
    Barcode: str
    BracketingType: BracketingTypeEnum
    CalibrationLevel: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    CalibrationStandards: System.Collections.Generic.List[str]
    DaMethodName: str
    DilutionFactors: str
    ExpectedBarcode: str
    InjectionAcqDateTime: System.DateTime
    InjectionId: System.Guid
    InjectorPosition: InjectorPositionEnum
    InternalStandardAmounts: System.Collections.Generic.List[str]
    LastModifiedDateTime: System.DateTime
    LegacyCalibrationStandards: System.Collections.Generic.List[
        StandardCompoundAmountType
    ]
    LegacyDilutionFactors: System.Collections.Generic.List[CorrectionFactorType]
    LegacyInternalStandardAmounts: System.Collections.Generic.List[
        StandardCompoundAmountType
    ]
    LegacyMultipliers: System.Collections.Generic.List[CorrectionFactorType]
    LimsIds: System.Collections.Generic.List[LimsIDType]
    Multipliers: str
    RawDataFileName: str
    ReplicateNumber: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    RunTypes: System.Collections.Generic.List[RunTypeAndReplicationType]
    SampleAmount: DoubleUnitType
    SampleDescription: str
    SampleInjectionsCount: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    SampleName: str
    SampleOrderNumber: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    SampleSetupId: System.Guid
    SampleType: SampleTypeEnum
    SequenceName: str
    VialNumber: str

class IdVer:  # Struct
    def __init__(self, id: System.Guid, version: int) -> None: ...

    Id: System.Guid  # readonly
    Version: int  # readonly

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class IdentParamBaseType(IIdentParamBaseType):  # Class
    Description: str
    Name: str
    ProjectID: str

class IdentifiedPeakAggregation(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
    IContainer,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
    IIdentifiedPeakAggregation,
):  # Class
    def __init__(
        self,
        peak: IPeakType,
        calibRole: CalibPeakRoleEnum,
        calibrationCurve: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
        injectionCompound: IInjectionCompoundType,
        docId: System.Guid,
    ) -> None: ...

    CalibRole: CalibPeakRoleEnum  # readonly
    CalibrationCurve: (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType
    )  # readonly
    DocId: System.Guid  # readonly
    Peak: IPeakType  # readonly
    RelatedInjectionCompound: IInjectionCompoundType  # readonly

class InjectionContainer(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectBaseType,
    IInjectionContainer,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
    IContainer,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, injectionMeasData: IInjectionMeasDataType, docId: System.Guid
    ) -> None: ...
    @overload
    def __init__(self, injectionMeasData: IInjectionMeasDataType) -> None: ...

    DocId: System.Guid  # readonly
    InjectionMeasData: IInjectionMeasDataType  # readonly
    InjectionResult: IInjectionResultType

class InjectionMetaData(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData
):  # Class
    @overload
    def __init__(
        self, injectionSetupId: System.Guid, sampleSetupId: System.Guid
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    AcqMethodName: str
    Barcode: str
    BracketingType: BracketingTypeEnum
    CalibrationLevel: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    CalibrationStandards: System.Collections.Generic.List[str]
    DaMethodName: str
    DilutionFactors: str
    ExpectedBarcode: str
    InjectionAcqDateTime: System.DateTime
    InjectionId: System.Guid
    InjectorPosition: InjectorPositionEnum
    InternalStandardAmounts: System.Collections.Generic.List[str]
    LastModifiedDateTime: System.DateTime
    LegacyBracketingType: str
    LegacyCalibrationStandards: System.Collections.Generic.List[
        StandardCompoundAmountType
    ]
    LegacyDilutionFactors: System.Collections.Generic.List[CorrectionFactorType]
    LegacyInternalStandardAmounts: System.Collections.Generic.List[
        StandardCompoundAmountType
    ]
    LegacyMultipliers: System.Collections.Generic.List[CorrectionFactorType]
    LimsIds: System.Collections.Generic.List[LimsIDType]
    Multipliers: str
    RawDataFileName: str
    ReplicateNumber: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    RunTypes: System.Collections.Generic.List[RunTypeAndReplicationType]
    SampleAmount: DoubleUnitType
    SampleDescription: str
    SampleInjectionsCount: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    SampleName: str
    SampleOrderNumber: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IntegerType
    SampleSetupId: System.Guid
    SampleType: SampleTypeEnum
    SequenceName: str
    VialNumber: str

    @staticmethod
    def CreateValueString(valueList: System.Collections.Generic.List[float]) -> str: ...
    @staticmethod
    def CreateAmountString(
        standardCompoundAmountType: StandardCompoundAmountType,
    ) -> str: ...
    @staticmethod
    def CreateStandardCompoundAmountType(
        amountString: str,
    ) -> StandardCompoundAmountType: ...
    @staticmethod
    def CreateValueList(valueString: str) -> Iterable[float]: ...

class NonIdentParamBaseType(INonIdentParamBaseType):  # Class
    def __init__(self) -> None: ...

    Method_ID: MethodRefType

class SampleContainer(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectBaseType,
    ISampleContainer,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
    IContainer,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Class
    @overload
    def __init__(self, sampleSetup: ISampleSetupType, docId: System.Guid) -> None: ...
    @overload
    def __init__(self, sampleSetup: ISampleSetupType) -> None: ...

    DocId: System.Guid  # readonly
    SampleMeasData: ISampleMeasDataType
    SampleSetup: ISampleSetupType  # readonly

class SampleContextContainer(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectBaseType,
    ISampleContextContainer,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
    IContainer,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Class
    @overload
    def __init__(
        self, sampleSetupContext: ISampleSetupContextType, docId: System.Guid
    ) -> None: ...
    @overload
    def __init__(self, sampleSetupContext: ISampleSetupContextType) -> None: ...

    DocId: System.Guid  # readonly
    SampleMeasDataContext: ISampleMeasDataContextType
    SampleSetupContext: ISampleSetupContextType  # readonly

class SamplePurityContainer(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectBaseType,
    ISamplePurityContainer,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
    IContainer,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, samplePuritySetup: IMSSamplePuritySetupType, docId: System.Guid
    ) -> None: ...
    @overload
    def __init__(self, samplePuritySetup: IMSSamplePuritySetupType) -> None: ...

    DocId: System.Guid  # readonly
    SamplePurityResult: IMSSamplePurityResultType  # readonly
    SamplePuritySetup: IMSSamplePuritySetupType  # readonly

    def AddSamplePurityResult(
        self, samplePurityResult: IMSSamplePurityResultType
    ) -> None: ...

class SignalContainer(
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType,
    IContainer,
    Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectRoot,
    ISignalContainer,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, signalMeasData: ISignalType, docId: System.Guid) -> None: ...
    @overload
    def __init__(self, signalMeasData: ISignalType) -> None: ...

    DocId: System.Guid
    SignalMeasData: ISignalType  # readonly
    SignalRawData: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
    SignalResult: IInjectionSignalResultType
    SpectrumRawData: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData
