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

from . import CustomObjects, Utilities

# Discovered Generic TypeVars:
TElement = TypeVar("TElement")
from .CoreTypes import (
    CalibrationCurveCoeffType,
    CalibrationCurveOriginEnum,
    CalibrationCurveTypeEnum,
    CalibrationLevelType,
    DoubleType,
    ICalibrationCurveType,
    IChromData,
    IDoubleType,
    IIntegerType,
    IntegerType,
    IObjectBaseType,
    IObjectRoot,
    ISpectrumData,
    MethodConfigurationType,
    MethodParameterType,
    NumericComparison,
    ObjectBaseType,
    ObjectInfoType,
    ResponseFactorCalcModeEnum,
    UserLinkType,
    ValueBaseType,
)

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel

class ACAML(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML, IObjectRoot
):  # Class
    def __init__(self) -> None: ...

    Checksum: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocChecksumType
    Doc: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocType
    DocumentStoragePath: str
    MigrationHistory: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MigrationHistoryType
    )

class AcamlVersions:  # Class
    CurrentNamespace: str = ...  # static # readonly

    CurrentNamespaceString: str  # static # readonly
    CurrentVersion: str  # static # readonly
    ObsoleteNamespaceStrings: List[str]  # static # readonly

    @staticmethod
    def GetFullNamespace(namespaceString: str) -> str: ...

class AcquisitionStatusEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Aborted: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AcquisitionStatusEnum
    ) = ...  # static # readonly
    Completed: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AcquisitionStatusEnum
    ) = ...  # static # readonly

class AcquisitionStatusType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IAcquisitionStatusType
):  # Class
    def __init__(self) -> None: ...

    Message: str
    Status: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AcquisitionStatusEnum

class AgilentAppType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IAgilentAppType, IObjectRoot
):  # Class
    def __init__(self) -> None: ...

    Name: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    Version: str

class AgilentApplicationEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CerityP: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ) = ...  # static # readonly
    ChemStation: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ) = ...  # static # readonly
    ChemStore: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ) = ...  # static # readonly
    Chromeleon: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ) = ...  # static # readonly
    EZChromElite: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ) = ...  # static # readonly
    Empower: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ) = ...  # static # readonly
    IntelligentDataAnalysis: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ) = ...  # static # readonly
    OpenLABICM: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ) = ...  # static # readonly
    OpenLabCDS: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ) = ...  # static # readonly

class AgtChemStoreInjectionMeasDataType:  # Class
    def __init__(self) -> None: ...

    ArchiveStatus: str
    ChemStationRev: str
    HashValue: List[int]
    Hostname: str
    MethodName: str
    MethodPath: str
    OperatorName: str
    SequenceName: str
    SequencePath: str

class AgtChemStoreInjectionResultType:  # Class
    def __init__(self) -> None: ...

    ArchiveStatus: str
    ChemStationInternalType: str
    ChemStationRev: str
    HashValue: List[int]
    Hostname: str
    InternalID: str
    LimsApprovalStatus: str

class AgtChemStoreInstrumentType:  # Class
    def __init__(self) -> None: ...

    HashValue: List[int]
    Hostname: str

class AgtChemStoreMethodType:  # Class
    def __init__(self) -> None: ...

    ArchiveStatus: str
    ChemStationRev: str
    HashValue: List[int]
    Hostname: str

class AgtChemStoreSampleMeasDataContextType:  # Class
    def __init__(self) -> None: ...

    ArchiveStatus: str
    ChemStationRev: str
    HashValue: List[int]
    Hostname: str

class AgtChemStoreSampleMeasDataType:  # Class
    def __init__(self) -> None: ...

    ChemStationRev: str

class AgtChemStoreSampleSetupContextType:  # Class
    def __init__(self) -> None: ...

    ChemStationRev: str

class AgtChemStoreSampleSetupType:  # Class
    def __init__(self) -> None: ...

    ChemStationRev: str

class AgtChemStoreSeparationMediumType:  # Class
    def __init__(self) -> None: ...

    HashValue: List[int]

class AssociatedSpectraType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IAssociatedSpectraType
):  # Class
    def __init__(self) -> None: ...

    Signal_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalRefType
    ]

class AuditTrailEntryType:  # Class
    def __init__(self) -> None: ...

    Date: System.DateTime
    Description: str
    EntryBy: UserLinkType
    Reason: str
    UserText: Any

class BackgroundSubtractionExternalSignalType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IBackgroundSubtractionExternalSignalType
):  # Class
    def __init__(self) -> None: ...

    Filename: str
    TraceID: str

class BackgroundSubtractionModeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ExplicitWithinSequence: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionModeEnum
    ) = ...  # static # readonly
    LastBlank: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionModeEnum
    ) = ...  # static # readonly
    TakeFromMethod: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionModeEnum
    ) = ...  # static # readonly

class BackgroundSubtractionReferenceSignalType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IBackgroundSubtractionReferenceSignalType
):  # Class
    def __init__(self) -> None: ...

    Item: Any

class BackgroundSubtractionSignalType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IBackgroundSubtractionSignalType
):  # Class
    def __init__(self) -> None: ...

    Item: Any

class BackgroundSubtractionType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IBackgroundSubtractionType
):  # Class
    def __init__(self) -> None: ...

    ReferenceSignal: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionReferenceSignalType
    )
    SubtractionMode: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionModeEnum
    )

class BaselineModelEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Exponential: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BaselineModelEnum
    ) = ...  # static # readonly
    ExtendedExponential: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BaselineModelEnum
    ) = ...  # static # readonly
    Linear: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BaselineModelEnum = (
        ...
    )  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BaselineModelEnum
    ) = ...  # static # readonly

class BaselineParametersType:  # Class
    def __init__(self) -> None: ...

    BaselineParameters: System.Collections.Generic.List[DoubleType]

class BinaryDataDirectoryType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IBinaryDataDirectoryType,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    DataItems: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemType
    ]
    Description: str
    DirItems: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataDirectoryType
    ]
    Name: str
    OriginalFilePath: str

class BinaryDataItemType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IBinaryDataItemType,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    BinaryContent: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemTypeBinaryContent
    )
    Data: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataStorageType
    Description: str
    Length: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LongType
    Name: str
    OriginalFilePath: str
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum
    TypeSpecified: bool

class BinaryDataItemTypeBinaryContent:  # Class
    def __init__(self) -> None: ...

    Item: Any

class BinaryDataItemTypeBinaryContentVector(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataVectorType
):  # Class
    def __init__(self) -> None: ...

class BinaryDataItemTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ByExtension: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemTypeEnum
    ) = ...  # static # readonly
    ChemStation: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemTypeEnum
    ) = ...  # static # readonly
    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemTypeEnum
    ) = ...  # static # readonly
    WMF: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemTypeEnum
    ) = ...  # static # readonly

class BinaryDataStorageType:  # Class
    def __init__(self) -> None: ...

    Item: Any

class BinaryDataType(
    IObjectRoot, Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IBinaryDataType
):  # Class
    def __init__(self) -> None: ...

    DataItems: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemType
    ]
    DirItems: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataDirectoryType
    ]

class BracketingModeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    OverallSequence: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingModeEnum
    ) = ...  # static # readonly
    SequenceBackCalculation: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingModeEnum
    ) = ...  # static # readonly
    Standard: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingModeEnum
    ) = ...  # static # readonly
    StandardClearCalibration: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingModeEnum
    ) = ...  # static # readonly
    StandardOverlap: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingModeEnum
    ) = ...  # static # readonly

class BracketingTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Close: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingTypeEnum = (
        ...
    )  # static # readonly
    Custom: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingTypeEnum = (
        ...
    )  # static # readonly
    Intermediate: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingTypeEnum
    ) = ...  # static # readonly
    Open: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingTypeEnum = (
        ...
    )  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingTypeEnum
    ) = ...  # static # readonly

class CEInjectionResultType:  # Class
    def __init__(self) -> None: ...

    IsAreaCorrected: bool
    IsAreaCorrectedSpecified: bool

class CEMethodType:  # Class
    def __init__(self) -> None: ...

    Mobility: str

class CEPeakType:  # Class
    def __init__(self) -> None: ...

    ApparentMobility: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    ExpMobility: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    MeasMobility: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType

class CESampleSetupType:  # Class
    def __init__(self) -> None: ...

    UserVariables: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    Voltage: DoubleType

class CalibPeakRoleEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DetectorMain: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum
    ) = ...  # static # readonly
    Ignore: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum = (
        ...
    )  # static # readonly
    Main: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum = (
        ...
    )  # static # readonly
    NewIgnore: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum
    ) = ...  # static # readonly
    NewMain: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum = (
        ...
    )  # static # readonly
    Qualifier: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum
    ) = ...  # static # readonly

class CalibrationCurveRefType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class CalibrationCurveType(
    ObjectBaseType, IObjectRoot, ICalibrationCurveType, IObjectBaseType
):  # Class
    def __init__(self) -> None: ...

    AreRelativeValues: bool
    AreRelativeValuesSpecified: bool
    CalibrationLevels: System.Collections.Generic.List[CalibrationLevelType]
    Coefficients: CalibrationCurveCoeffType
    CorrCoefficient: DoubleType
    DetermCoefficient: DoubleType
    Formula: str
    Info: ObjectInfoType
    Origin: CalibrationCurveOriginEnum
    Residual: DoubleType
    ResponseFactorCalcMode: ResponseFactorCalcModeEnum
    ResponseFactorCalcModeSpecified: bool
    ResponseFactorRSDPercent: DoubleType
    ResponseFactorStdDev: DoubleType
    Scale: str
    Type: CalibrationCurveTypeEnum
    TypeDescription: str
    WeightType: str

class CommonAppType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICommonAppType, IObjectRoot
):  # Class
    def __init__(self) -> None: ...

    Name: str
    Version: str

class CompoundSpectrumType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICompoundSpectrumType,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    ExtrType: str
    RT: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Type: str

class CompoundTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Expected: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CompoundTypeEnum = (
        ...
    )  # static # readonly
    Group: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CompoundTypeEnum = (
        ...
    )  # static # readonly
    ManuallyIdentifiedExpected: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CompoundTypeEnum
    ) = ...  # static # readonly
    ManuallyUnidentifiedExpected: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CompoundTypeEnum
    ) = ...  # static # readonly
    NotIdentifiedExpected: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CompoundTypeEnum
    ) = ...  # static # readonly
    PeakSum: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CompoundTypeEnum = (
        ...
    )  # static # readonly
    UncalibratedExpected: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CompoundTypeEnum
    ) = ...  # static # readonly
    Unknown: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CompoundTypeEnum = (
        ...
    )  # static # readonly

class CorrectionFactorType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICorrectionFactorType,
):  # Class
    def __init__(self) -> None: ...

    CorrectionFactor: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    Name: str

class CreatedByApplicationType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICreatedByApplicationType,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    Item: Any

class CustomCalcBooleanResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcBooleanResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcResultType,
):  # Class
    def __init__(self) -> None: ...

    Value: bool

class CustomCalcDateResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcDateResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcResultType,
):  # Class
    def __init__(self) -> None: ...

    Value: System.DateTime

class CustomCalcDoubleResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcDoubleResultType,
):  # Class
    def __init__(self) -> None: ...

    Value: float

class CustomCalcEmbeddedResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcEmbeddedResultType
):  # Class
    def __init__(self) -> None: ...

    Parent_id: str
    Parent_ver: int
    Results: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcResultType
    ]

class CustomCalcExternalResultsType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcExternalResultsType
):  # Class
    def __init__(self) -> None: ...

    Path: str

class CustomCalcFloatResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcFloatResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcResultType,
):  # Class
    def __init__(self) -> None: ...

    Value: float

class CustomCalcInformationType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcInformationType
):  # Class
    def __init__(self) -> None: ...

    Code: int
    Texts: System.Collections.Generic.List[str]

class CustomCalcIntegerResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcIntegerResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcResultType,
):  # Class
    def __init__(self) -> None: ...

    Value: int

class CustomCalcResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType
):  # Class
    Description: str
    Id: str
    Information: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcInformationType
    )
    Name: str
    Unit: str

class CustomCalcResultsType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultsType
):  # Class
    def __init__(self) -> None: ...

    Items: System.Collections.Generic.List

class CustomCalcTextResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcTextResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcResultType,
):  # Class
    def __init__(self) -> None: ...

    Value: str

class CustomFieldContentType:  # Class
    def __init__(self) -> None: ...

class CustomFieldType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomFieldType
):  # Class
    def __init__(self) -> None: ...

    Description: str
    Items: System.Collections.Generic.List
    Mandatory: bool
    MandatorySpecified: bool
    Name: str

class CustomFieldValueType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomFieldValueType
):  # Class
    def __init__(self) -> None: ...

    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum
    TypeSpecified: bool
    Unit: str
    Value: str

class DataBlobType:  # Class
    def __init__(self) -> None: ...

    Blob: List[int]

class DataFactoryException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class DataFileRefType(
    IObjectRoot, Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDataFileRefType
):  # Class
    def __init__(self) -> None: ...

    Checksum: List[int]
    CreatedDate: System.DateTime
    CreatedDateSpecified: bool
    ModifiedDate: System.DateTime
    ModifiedDateSpecified: bool
    Path: str
    Size: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LongType

class DataFormatType:  # Class
    def __init__(self) -> None: ...

    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemTypeEnum

class DataTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Boolean: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum = (
        ...
    )  # static # readonly
    Date: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum = (
        ...
    )  # static # readonly
    DateTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum = (
        ...
    )  # static # readonly
    Float32: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum = (
        ...
    )  # static # readonly
    Float64: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum = (
        ...
    )  # static # readonly
    Int: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum = (
        ...
    )  # static # readonly
    Long: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum = (
        ...
    )  # static # readonly
    String: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum = (
        ...
    )  # static # readonly
    Time: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum = (
        ...
    )  # static # readonly

class DataVectorType:  # Class
    def __init__(self) -> None: ...

    Count: int
    CountSpecified: bool
    ItemType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VectoreItemTypeEnum

class DocChecksumAlgorithmEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    MD5: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocChecksumAlgorithmEnum
    ) = ...  # static # readonly
    SHA1: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocChecksumAlgorithmEnum
    ) = ...  # static # readonly

class DocChecksumType:  # Class
    def __init__(self) -> None: ...

    Algorithm: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocChecksumAlgorithmEnum
    )
    Value: List[int]

class DocContentType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDocContentType, IObjectRoot
):  # Class
    def __init__(self) -> None: ...

    CustomCalcResults: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcResultsType
    )
    Injections: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionsType
    MethodConfigurations: System.Collections.Generic.List[MethodConfigurationType]
    Methods: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodType
    ]
    Resources: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResourcesType
    SampleContexts: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextsType
    )
    Samples: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SamplesType
    Users: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.UserType
    ]

class DocInfoType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDocInfoType, IObjectRoot
):  # Class
    def __init__(self) -> None: ...

    ClientName: str
    CreatedByApplication: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CreatedByApplicationType
    )
    CreatedByUser: str
    CreationDate: System.DateTime
    CustomFields: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    DatabaseName: str
    Description: str

class DocType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDocType, IObjectRoot
):  # Class
    def __init__(self) -> None: ...

    Content: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocContentType
    ContentVersioned: bool
    DocID: str
    DocInfo: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocInfoType

class DoubleUnitType(
    IDoubleType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
    ValueBaseType,
):  # Class
    def __init__(self) -> None: ...

    Unit: str
    Val: float

class EntityKeyType:  # Class
    def __init__(self) -> None: ...

    Iid: str
    Ver: int

class ExtensionsIACAML:  # Class
    @staticmethod
    def IsSingleInjectionAcaml(
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...

class ExtensionsIBinaryDataType:  # Class
    @staticmethod
    def GetBinaryDirItems(
        binaryData: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IBinaryDataType,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataDirectoryType
    ]: ...
    @staticmethod
    def GetRelativeDataFileReferences(
        binaryData: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IBinaryDataType,
    ) -> Iterable[str]: ...
    @staticmethod
    def GetBinaryDataItems(
        binaryData: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IBinaryDataType,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemType
    ]: ...

class ExtensionsIDocInfoType:  # Class
    @staticmethod
    def BackupOriginalApplicationName(
        docInfoType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDocInfoType,
    ) -> None: ...
    @staticmethod
    def GetOriginalApplicationName(
        docInfoType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDocInfoType,
    ) -> (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ): ...

class ExtensionsIDocType:  # Class
    @staticmethod
    def GetGuid(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDocType,
    ) -> System.Guid: ...

class ExtensionsIDoubleUnitType:  # Class
    @overload
    @staticmethod
    def Equals(
        double1: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
        double2: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
    ) -> bool: ...
    @overload
    @staticmethod
    def Equals(
        double1: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
        double2: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
        comparisonMode: NumericComparison,
        precision: float,
    ) -> bool: ...
    @staticmethod
    def StringEquals(first: str, second: str) -> bool: ...
    @staticmethod
    def DoubleUnitTypeToString(
        doubleUnitType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
    ) -> str: ...
    @overload
    @staticmethod
    def DoubleUnitTypeEquals(
        double1: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
        double2: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
    ) -> bool: ...
    @overload
    @staticmethod
    def DoubleUnitTypeEquals(
        double1: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
        double2: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
        comparisonMode: NumericComparison,
        precision: float,
    ) -> bool: ...
    @overload
    @staticmethod
    def TryGetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
    ) -> Optional[float]: ...
    @overload
    @staticmethod
    def TryGetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
        defaultValue: float,
    ) -> float: ...
    @staticmethod
    def TryGetUnit(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDoubleUnitType,
    ) -> str: ...

class ExtensionsIEnumerable:  # Class
    @staticmethod
    def FindById(list: Iterable[TElement], id: System.Guid) -> TElement: ...
    @staticmethod
    def Resolve(
        list: Iterable[TElement], objectsToMatch: Iterable[IObjectBaseType]
    ) -> Iterable[TElement]: ...

class ExtensionsIGenericVersionedObjectType:  # Class
    @staticmethod
    def GetCustomFields(
        genericVersionedObject: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
        name: str,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomFieldType
    ]: ...
    @staticmethod
    def RemoveCustomField(
        genericVersionedObject: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
        name: str,
        userName: str,
    ) -> None: ...
    @staticmethod
    def AddOrUpdateCustomField(
        genericVersionedObject: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
        customField: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomFieldType,
        userName: str,
    ) -> None: ...
    @staticmethod
    def UpdateObjectInfo(
        genericVersionedObject: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
        userName: str,
    ) -> None: ...
    @staticmethod
    def GetValueOfSimpleCustomField(
        genericVersionedObject: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
        name: str,
    ) -> str: ...
    @staticmethod
    def ClearCustomFields(
        genericVersionedObject: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
        userName: str,
    ) -> None: ...

class ExtensionsIInjectionCompoundType:  # Class
    @staticmethod
    def GetIdentifiedPeakReferences(
        injectionCompound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
        filterPredicate: System.Predicate[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakRefType
        ] = ...,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakRefType
    ]: ...
    @staticmethod
    def GetIdentifiedInjectionCompoundsReferences(
        injectionCompound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
        filterPredicate: System.Predicate[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundRefType
        ] = ...,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundRefType
    ]: ...

class ExtensionsIIntegerType:  # Class
    @overload
    @staticmethod
    def TryGetValue(baseType: IIntegerType) -> Optional[int]: ...
    @overload
    @staticmethod
    def TryGetValue(baseType: IIntegerType, defaultValue: int) -> int: ...
    @overload
    @staticmethod
    def GetValue(baseType: IIntegerType) -> int: ...
    @overload
    @staticmethod
    def GetValue(baseType: IIntegerType, defaultValue: int) -> int: ...

class ExtensionsILongType:  # Class
    @overload
    @staticmethod
    def TryGetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILongType,
    ) -> Optional[int]: ...
    @overload
    @staticmethod
    def TryGetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILongType,
        defaultValue: int,
    ) -> int: ...
    @overload
    @staticmethod
    def GetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILongType,
    ) -> int: ...
    @overload
    @staticmethod
    def GetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILongType,
        defaultValue: int,
    ) -> int: ...

class ExtensionsIObjectBaseType:  # Class
    @staticmethod
    def TryGetGuid(baseType: IObjectBaseType) -> System.Guid: ...
    @staticmethod
    def SetNewGuid(baseType: IObjectBaseType) -> None: ...

class ExtensionsISamplesType:  # Class
    @staticmethod
    def CountInjectionMeasDataRefItems(
        samples: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplesType,
    ) -> int: ...

class ExtensionsISignalType:  # Class
    @staticmethod
    def IsSpectraMatrix(
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    ) -> bool: ...
    @staticmethod
    def IsInstrumentCurve(
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    ) -> bool: ...
    @staticmethod
    def IsExtractedChromatogram(
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    ) -> bool: ...
    @staticmethod
    def IsChromatogram(
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    ) -> bool: ...
    @staticmethod
    def IsExtractedSpectrum(
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    ) -> bool: ...

class ExtensionsITimePeriodType:  # Class
    @overload
    @staticmethod
    def GetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType,
    ) -> float: ...
    @overload
    @staticmethod
    def GetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType,
        defaultValue: float,
    ) -> float: ...
    @staticmethod
    def TimePeriodToString(
        timePeriod: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType,
    ) -> str: ...
    @overload
    @staticmethod
    def TryGetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType,
    ) -> Optional[float]: ...
    @overload
    @staticmethod
    def TryGetValue(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType,
        defaultValue: float,
    ) -> float: ...
    @overload
    @staticmethod
    def TimePeriodEquals(
        timePeriod1: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType,
        timePeriod2: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType,
    ) -> bool: ...
    @overload
    @staticmethod
    def TimePeriodEquals(
        timePeriod1: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType,
        timePeriod2: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType,
        comparisonMode: NumericComparison,
        precision: float,
    ) -> bool: ...
    @staticmethod
    def GetTimeUnitEnumString(
        timeUnitEnum: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimeUnitEnum,
    ) -> str: ...
    @staticmethod
    def TryGetUnit(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType,
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimeUnitEnum: ...

class ExtensionsIVersionedObjectBaseType:  # Class
    @staticmethod
    def IncreaseVersion(
        baseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    ) -> int: ...

class GEFragmentSizeType:  # Class
    def __init__(self) -> None: ...

    Unit: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeUnitEnum
    UnitSpecified: bool
    Val: float

class GEFragmentSizeUnitEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Bp: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeUnitEnum = (
        ...
    )  # static # readonly
    KDa: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeUnitEnum
    ) = ...  # static # readonly
    Nt: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeUnitEnum = (
        ...
    )  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeUnitEnum
    ) = ...  # static # readonly

class GEInjectionCompoundType:  # Class
    def __init__(self) -> None: ...

    AverageSize: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeType
    )
    BeginSize: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeType
    EndSize: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeType
    Size: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeType

class GEInjectionResultType:  # Class
    def __init__(self) -> None: ...

    Regions: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GERegionType
    ]

class GEPeakType:  # Class
    def __init__(self) -> None: ...

    BeginRunDistance: DoubleType
    EndRunDistance: DoubleType
    RunDistancePercentage: DoubleType

class GERegionType:  # Class
    def __init__(self) -> None: ...

    AverageSize: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeType
    )
    Comment: str
    Concentration: DoubleType
    From: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeType
    Molarity: DoubleType
    Observation: str
    PercentTotalArea: DoubleType
    To: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEFragmentSizeType

class GenericNonVersionedObjectType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericNonVersionedObjectType,
):  # Class
    def __init__(self) -> None: ...

    BinaryData: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataType
    ComplexCustomFields: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    Info: ObjectInfoType
    SimpleCustomFields: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldsType
    )

class GenericVersionedObjectType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
):  # Class
    def __init__(self) -> None: ...

    BinaryData: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataType
    ComplexCustomFields: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    Info: ObjectInfoType
    SimpleCustomFields: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldsType
    )

class IACAML(IObjectRoot):  # Interface
    Checksum: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocChecksumType
    Doc: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocType
    DocumentStoragePath: str
    MigrationHistory: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MigrationHistoryType
    )

class IAcquisitionStatusType(object):  # Interface
    Message: str
    Status: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AcquisitionStatusEnum

class IAgilentAppType(IObjectRoot):  # Interface
    Name: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    Version: str

class IAssociatedSpectraType(object):  # Interface
    Signal_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalRefType
    ]

class IBackgroundSubtractionExternalSignalType(object):  # Interface
    Filename: str
    TraceID: str

class IBackgroundSubtractionReferenceSignalType(object):  # Interface
    Item: Any

class IBackgroundSubtractionSignalType(object):  # Interface
    Item: Any

class IBackgroundSubtractionType(object):  # Interface
    ReferenceSignal: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionReferenceSignalType
    )
    SubtractionMode: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionModeEnum
    )

class IBinaryDataDirectoryType(IObjectRoot):  # Interface
    DataItems: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemType
    ]
    Description: str
    DirItems: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataDirectoryType
    ]
    Name: str
    OriginalFilePath: str

class IBinaryDataItemType(IObjectRoot):  # Interface
    BinaryContent: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemTypeBinaryContent
    )
    Data: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataStorageType
    Description: str
    Length: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LongType
    Name: str
    OriginalFilePath: str
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum
    TypeSpecified: bool

class IBinaryDataType(IObjectRoot):  # Interface
    DataItems: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataItemType
    ]
    DirItems: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataDirectoryType
    ]

class ICommonAppType(IObjectRoot):  # Interface
    Name: str
    Version: str

class ICompoundSpectrumType(IObjectRoot):  # Interface
    ExtrType: str
    RT: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Type: str

class IContainer(IObjectBaseType, IObjectRoot):  # Interface
    DocId: System.Guid  # readonly

class IContent(IObjectRoot):  # Interface
    ...

class ICorrectionFactorType(IObjectRoot):  # Interface
    CorrectionFactor: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    Name: str

class ICreatedByApplicationType(IObjectRoot):  # Interface
    Item: Any

class ICustomCalcBooleanResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType
):  # Interface
    Value: bool

class ICustomCalcDateResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType
):  # Interface
    Value: System.DateTime

class ICustomCalcDoubleResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType
):  # Interface
    Value: float

class ICustomCalcEmbeddedResultType(object):  # Interface
    Parent_id: str
    Parent_ver: int
    Results: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcResultType
    ]

class ICustomCalcExternalResultsType(object):  # Interface
    Path: str

class ICustomCalcFloatResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType
):  # Interface
    Value: float

class ICustomCalcInformationType(object):  # Interface
    Code: int
    Texts: System.Collections.Generic.List[str]

class ICustomCalcIntegerResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType
):  # Interface
    Value: int

class ICustomCalcResultType(object):  # Interface
    Description: str
    Id: str
    Information: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomCalcInformationType
    )
    Name: str
    Unit: str

class ICustomCalcResultsType(object):  # Interface
    Items: System.Collections.Generic.List

class ICustomCalcTextResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcResultType
):  # Interface
    Value: str

class ICustomFieldType(object):  # Interface
    Description: str
    Items: System.Collections.Generic.List
    Mandatory: bool
    MandatorySpecified: bool
    Name: str

class ICustomFieldValueType(object):  # Interface
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DataTypeEnum
    TypeSpecified: bool
    Unit: str
    Value: str

class IDaParam(object):  # Interface
    CalibrationLevel: IntegerType
    CalibrationStandards: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.StandardCompoundAmountType
    ]
    DilutionFactors: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CorrectionFactorType
    ]
    InternalStandards: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.StandardCompoundAmountType
    ]
    Multipliers: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CorrectionFactorType
    ]
    OrderNo: IntegerType
    ResponseFactorUpdate: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResponseFactorUpdateEnum
    )
    ResponseFactorUpdateSpecified: bool
    ResponseFactorUpdateWeight: DoubleType
    RetentionTimeUpdate: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RetentionTimeUpdateEnum
    )
    RetentionTimeUpdateSpecified: bool
    RetentionTimeUpdateWeight: DoubleType
    RunTypes: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeAndReplicationType
    ]
    SampleAmount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType

class IDataFileRefType(IObjectRoot):  # Interface
    Checksum: List[int]
    CreatedDate: System.DateTime
    CreatedDateSpecified: bool
    ModifiedDate: System.DateTime
    ModifiedDateSpecified: bool
    Path: str
    Size: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LongType

class IDocContentType(IObjectRoot):  # Interface
    Injections: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionsType
    MethodConfigurations: System.Collections.Generic.List[MethodConfigurationType]
    Methods: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodType
    ]
    Resources: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResourcesType
    SampleContexts: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextsType
    )
    Samples: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SamplesType
    Users: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.UserType
    ]

class IDocInfoType(IObjectRoot):  # Interface
    ClientName: str
    CreatedByApplication: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CreatedByApplicationType
    )
    CreatedByUser: str
    CreationDate: System.DateTime
    CustomFields: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    DatabaseName: str
    Description: str

class IDocType(IObjectRoot):  # Interface
    Content: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocContentType
    ContentVersioned: bool
    DocID: str
    DocInfo: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DocInfoType

class IDoubleUnitType(IDoubleType):  # Interface
    Unit: str

class IGEInjectionResultType(object):  # Interface
    Regions: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GERegionType
    ]

class IGenericInjectionCompoundIndentificationType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundIdentificationItem,
    IObjectRoot,
):  # Interface
    CustomFields: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    InjectionSignalResult_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSignalResultRefType
    ]

class IGenericNonVersionedObjectType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    BinaryData: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataType
    ComplexCustomFields: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    Info: ObjectInfoType
    SimpleCustomFields: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldsType
    )

class IGenericVersionedObjectType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    BinaryData: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BinaryDataType
    ComplexCustomFields: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    Info: ObjectInfoType
    SimpleCustomFields: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldsType
    )

class IIdentParamBaseType(object):  # Interface
    Description: str
    Name: str
    ProjectID: str

class IIdentifiedPeakAggregation(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContainer,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    CalibRole: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum
    )  # readonly
    CalibrationCurve: ICalibrationCurveType  # readonly
    Peak: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType  # readonly
    RelatedInjectionCompound: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType
    )  # readonly

class IInjectionAcquisitionParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType
):  # Interface
    OrderNo: IntegerType
    OverridenMethodParameters: System.Collections.Generic.List[MethodParameterType]

class IInjectionCompoundIdentificationItem(IObjectRoot):  # Interface
    ...

class IInjectionCompoundIdentificationType(IObjectRoot):  # Interface
    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QualifiedInjectionCompoundIdentificationType
    )

class IInjectionCompoundRefType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    ...

class IInjectionCompoundType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericNonVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    Amount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Area: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    AverageResponseFactor: DoubleType
    CalibMarginPercent: DoubleType
    CalibWeight: DoubleType
    CalibrationAmount: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    CalibrationCurve_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibrationCurveRefType
    )
    Comment: str
    CompoundName: str
    Concentration: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    CorrExpectedRetTime: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    CorrectedArea: DoubleType
    ExpectedRetTime: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    ExpectedSignal: str
    Height: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    HighConcentration: DoubleType
    Identification: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundIdentificationType
    )
    IsInternalStandard: bool
    IsInternalStandardSpecified: bool
    IsTimeRef: bool
    IsTimeRefSpecified: bool
    LOD: DoubleType
    LOQ: DoubleType
    LowConcentration: DoubleType
    LowerAmountLimit: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    Multiplier: DoubleType
    NormAmount: DoubleType
    QuantitationType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    )
    QuantitationTypeSpecified: bool
    ResponseCorrectionFactor: DoubleType
    ResponseFactor: DoubleType
    ResponseFactorCalcMode: ResponseFactorCalcModeEnum
    ResponseFactorCalcModeSpecified: bool
    SpectraConfirmMatchFactor: DoubleType
    SpectraConfirmResult: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectraConfirmResultEnum
    )
    SpectraConfirmResultFieldSpecified: bool
    TechSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundTechSpecType
    )
    TimeRanges: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimeRangeType
    ]
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CompoundTypeEnum
    UpperAmountLimit: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    UsedInternalStandards: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.StandardCompoundIdentifierType
    ]

class IInjectionContainer(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContainer,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    InjectionMeasData: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionMeasDataType
    )  # readonly
    InjectionResult: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionResultType
    )

class IInjectionDataAnalysisParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDaParam,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType,
):  # Interface
    BackgroundSubtraction: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionType
    )
    InjectionAmount: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    SampleBracketingType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingTypeEnum
    )
    SampleBracketingTypeSpecified: bool
    SampleOrderNo: IntegerType
    SampleType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    SampleTypeSpecified: bool

class IInjectionMeasDataRefType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    ...

class IInjectionMeasDataTechSpecType(object):  # Interface
    LC: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LCInjectionMeasDataType

class IInjectionMeasDataType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    AcqParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionAcquisitionParamType
    )
    AcquisitionApplication: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CreatedByApplicationType
    )
    AcquisitionIdentifier: str
    AcquisitionMethodVersion: str
    AcquisitionSoftware: str
    AcquitionStatus: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AcquisitionStatusType
    )
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionMeasDataAppSpecType
    )
    DiagnosticData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    ExternalResultPath: str
    InjectionSeparationMedia: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSeparationMediumType
    ]
    InjectionVolume: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    RunTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Signals: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalType
    ]
    TechSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionMeasDataTechSpecType
    )

class IInjectionResultRefType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    ...

class IInjectionResultTechSpecType(object):  # Interface
    CE: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CEInjectionResultType
    GE: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEInjectionResultType
    MS: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSInjectionResultType

class IInjectionResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionResultAppSpecType
    )
    DAParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionDataAnalysisParamType
    )
    DataAnalysisApplication: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CreatedByApplicationType
    )
    DataAnalysisMethodVersion: str
    DataAnalysisSoftware: str
    InjectionCompounds: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundType
    ]
    InjectionMeasData_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionMeasDataRefType
    )
    Label: str
    ManualModification: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionModificationEnum
    )
    ManualModificationSpecified: bool
    NoiseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NoiseTypeEnum
    NoiseTypeSpecified: bool
    ProcessingStatus: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingStatusType
    )
    ReferencedInjectionInfo: str
    ReprocessingRequired: bool
    ReprocessingRequiredSpecified: bool
    SignalResults: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSignalResultType
    ]
    TechSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionResultTechSpecType
    )
    VirtualPeaks: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VirtualPeakType
    ]

class IInjectionSeparationMediumType(object):  # Interface
    AutoDetect: bool
    InjectionCount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LongType
    Position: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumPositionEnum
    )
    SeparationMedium_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumRefType
    )
    UsedForInjection: bool
    UsedForInjectionSpecified: bool

class IInjectionSignalResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericNonVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    NoisePeriods: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NoisePeriodType
    ]
    Peaks: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakType
    ]
    Signal_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalRefType
    Spectra: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumType
    ]

class IInjectionsType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContent, IObjectRoot
):  # Interface
    MeasData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionMeasDataType
    ]
    Results: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionResultType
    ]

class IInstrumentModuleType(object):  # Interface
    AdditionalInformation: str
    ConnectionInfo: str
    DisplayName: str
    DriverVersion: str
    FirmwareRevision: str
    Manufacturer: str
    Name: str
    PartNo: str
    SerialNo: str
    Type: str

class IInstrumentType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    AppSpec: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentAppSpecType
    Modules: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentModuleType
    ]
    SeparationMedium_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumRefType
    ]
    Technique: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentTechniqueEnum
    )

class IIntegerUnitType(IIntegerType):  # Interface
    Unit: str

class ILCFractionType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    EndTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Location: str
    Mass: str
    Number: IntegerType
    Purity: DoubleType
    Reason: str
    StartTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Volume: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Well: str

class ILCInjectionMeasDataType(object):  # Interface
    Fractions: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LCFractionType
    ]

class ILabSampleRefType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    ...

class ILabSampleType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    Barcode: str
    LimsIDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LimsIDType
    ]

class ILimsIDType(object):  # Interface
    Key: str
    Name: str

class ILongType(object):  # Interface
    Val: int

class ILongUnitType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILongType
):  # Interface
    Unit: str

class IMSInjectionCompoundType(object):  # Interface
    Found: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundEnum
    FoundDescription: str
    FoundPolarity: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundPolarityEnum
    )
    FoundPolaritySpecified: bool
    FoundSpecified: bool
    MolFormula: str
    MonoIsotopicMass: DoubleType
    Purity: DoubleType
    PurityBaseSignalDescription: str
    SpectraConfirmMatchFactor: DoubleType
    SpectraConfirmResult: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectraConfirmResultEnum
    )
    SpectraConfirmResultSpecified: bool

class IMSInjectionResultType(object):  # Interface
    SamplePurityResults: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSamplePurityResultType
    ]

class IMSSamplePurityResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    MSSamplePuritySetup_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSamplePuritySetupRefType
    )
    Peak_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakRefType
    SamplePurity: DoubleType
    Signal_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalRefType
    TargetFound: bool
    TargetPure: bool

class IMSSamplePuritySetupType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    TargetFormula: str
    TargetMass: DoubleType
    TargetName: str

class IMSSampleSetupType(object):  # Interface
    SamplePuritySetups: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSamplePuritySetupType
    ]

class IMSSignalType(object):  # Interface
    FragmentorVoltage: int
    FragmentorVoltageSpecified: bool
    IonPolarity: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSIonPolarityEnum
    IonizationMode: str
    MaximumIonIntensity: DoubleType
    ScanType: str
    StorageMode: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSStorageModeEnum

class IMSSpectrumLibraryHitType(object):  # Interface
    CASNumber: str
    LibaryNumber: IntegerType
    LibraryCompoundName: str
    LibraryID: IntegerType
    LibrarySpectrumRefLib: IntegerType
    LibrarySpectrumRefLoc: IntegerType
    LibrarySpectrumRefType: IntegerType
    MatchNumber: IntegerType
    ProbabilityPercent: DoubleType
    ReverseMatchNumber: IntegerType
    UserCompoundName: str

class IMSSpectrumLibraryType(object):  # Interface
    LibraryName: str
    LibraryPath: str
    MSSpectrumHits: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSpectrumLibraryHitType
    ]

class IMSSpectrumSearchResultsType(object):  # Interface
    MSSpectrumLibraries: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSpectrumLibraryType
    ]

class IMethodConfigurationLinkType(object):  # Interface
    Item: Any

class IMethodInstructionType(IObjectRoot):  # Interface
    Function: str
    Index: int
    ParameterString: str
    Parameters: System.Collections.Generic.List[MethodParameterType]
    Time: float
    TimeSpecified: bool

class IMethodType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    AppSpec: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodAppSpecType
    Application: str
    Instrument_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentRefType
    ]
    Integrator: str
    MethodConfigurationLink: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodConfigurationLinkType
    )
    OriginalVersion: str
    QuantitationMethod: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QuantificationMethodEnum
    )
    QuantitationMethodSpecified: bool
    SeparationMedium_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumRefType
    ]
    TechSpec: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodTechSpecType

class IMigrationHistoryType(object):  # Interface
    MigrationSteps: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MigrationStepType
    ]

class IMigrationStepType(object):  # Interface
    Application: str
    Date: System.DateTime
    FromNamespace: str
    ToNamespace: str

class IMissingQualifierType(object):  # Interface
    Mass: DoubleType
    SignalName: str

class INamedGenericVersionedObjectType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    Description: str
    Name: str
    ProjectID: str

class INoisePeriodType(IObjectRoot):  # Interface
    Drift: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Noise6SD: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    NoiseASTM: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    NoisePToP: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    TimeFrom: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    TimeTo: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Wander: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType

class INonIdentParamBaseType(object):  # Interface
    Method_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodRefType

class INonVersionedObjectBaseType(IObjectBaseType, IObjectRoot):  # Interface
    ...

class IPeakRefType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    CalibPeakRole: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum
    )
    CalibPeakRoleSpecified: bool
    CalibrationCurve_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibrationCurveRefType
    )
    QualifierPassed: bool
    QualifierPassedSpecified: bool
    QualifierRatioRangeFitMode: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QualifierRatioFitModeEnum
    )
    QualifierRatioRangeFitModeSpecified: bool
    QualifierRatioRangeMax: float
    QualifierRatioRangeMaxSpecified: bool
    QualifierRatioRangeMin: float
    QualifierRatioRangeMinSpecified: bool

class IPeakType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    Area: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    AreaPercent: DoubleType
    AreaSum: DoubleType
    AssociatedSpectra: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AssociatedSpectraType
    )
    Asymmetry_10Perc: DoubleType
    Asymmetry_5SigmaPerc: DoubleType
    BaselineCode: str
    BaselineEnd: DoubleType
    BaselineModel: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BaselineModelEnum
    )
    BaselineModelSpecified: bool
    BaselineParameters: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BaselineParametersType
    )
    BaselineRetentionHeight: DoubleType
    BaselineStart: DoubleType
    BeginTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    CapacityFactor: DoubleType
    CentroidTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    ComplexCustomFields: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    CorrExpRetTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    DownInflectionBaselineTime: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    DownInflectionBaselineY: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    DownSlopeSimilarity: DoubleType
    EndTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Excess: DoubleType
    FrontTangentOffset: DoubleType
    FrontTangentSlope: DoubleType
    Height: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    HeightPercent: DoubleType
    HeightSum: DoubleType
    HeightToValleyRatioAfter: DoubleType
    HeightToValleyRatioBefore: DoubleType
    InflectionTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    InflectionY: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    KovatsIndex: DoubleType
    LambdaMax: DoubleType
    LambdaMin: DoubleType
    LevelEnd: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    LevelStart: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    MSSpectrumSearchResults: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSpectrumSearchResultsType
    )
    Noise: DoubleType
    Noise6Sigma: DoubleType
    Number: IntegerType
    PeakValleyRatio: DoubleType
    Plate2Sigma: DoubleType
    Plate3Sigma: DoubleType
    Plate4Sigma: DoubleType
    Plate5Sigma: DoubleType
    PlatesPerColumn_FoleyDorsey: DoubleType
    PlatesPerMeter_AOH: DoubleType
    PlatesPerMeter_EMG: DoubleType
    PlatesPerMeter_EP: DoubleType
    PlatesPerMeter_FoleyDorsey: DoubleType
    PlatesPerMeter_JP: DoubleType
    PlatesPerMeter_USP: DoubleType
    PlatesStatistical: DoubleType
    Purity: DoubleType
    PurityPassed: bool
    QualifierMass: DoubleType
    RSDPercent: DoubleType
    ReferencePeakIdentifier: str
    RelativeRetentionTime: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    RelativeRetentionTime_EP: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    Resolution5Sigma: DoubleType
    ResolutionStatistical: DoubleType
    Resolution_AOH: DoubleType
    Resolution_DAB: DoubleType
    Resolution_EMG: DoubleType
    Resolution_EP: DoubleType
    Resolution_JP: DoubleType
    Resolution_USP: DoubleType
    Resolution_USP_HH: DoubleType
    ResponseRatio: DoubleType
    RetentionTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Selectivity: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    SignalToNoise: DoubleType
    SignalToNoise6Sigma: DoubleType
    SignalToNoiseEP: DoubleType
    SignalToNoiseUSP: DoubleType
    SimilarityIndex: DoubleType
    SimpleCustomFields: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldsType
    )
    Skew: DoubleType
    StatisticalMoment0: DoubleType
    StatisticalMoment1: DoubleType
    StatisticalMoment2: DoubleType
    StatisticalMoment3: DoubleType
    StatisticalMoment4: DoubleType
    Symmetry: DoubleType
    TailTangentOffset: DoubleType
    TailTangentSlope: DoubleType
    TailingFactor: DoubleType
    TechSpec: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTechSpecType
    TheoreticalPlates_AOH: DoubleType
    TheoreticalPlates_EMG: DoubleType
    TheoreticalPlates_EP: DoubleType
    TheoreticalPlates_JP: DoubleType
    TheoreticalPlates_USP: DoubleType
    ThreePointPurity: DoubleType
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    UVSpectrumSearchResults: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.UVSpectrumSearchResultsType
    )
    UpInflectionBaselineTime: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    UpInflectionBaselineY: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    UpSlopeSimilarity: DoubleType
    Width2Sigma: DoubleType
    Width3Sigma: DoubleType
    Width4Sigma: DoubleType
    Width5Sigma: DoubleType
    WidthBase: DoubleType
    WidthTangent: DoubleType
    Width_10Perc: DoubleType
    Width_50Perc: DoubleType
    Width_5Perc: DoubleType

class IProcessingStatusItemType(object):  # Interface
    Category: str
    Message: str
    TransformationState: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationStateEnum
    )

class IProcessingStatusType(object):  # Interface
    ProcessingStatusItems: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingStatusItemType
    ]
    TransformationChainState: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationChainStateEnum
    )
    TransformationChainStateSpecified: bool

class IQualifiedInjectionCompoundIdentificationType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundIdentificationItem,
    IObjectRoot,
):  # Interface
    InjectionCompounds: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundRefType
    ]
    MissingQualifiers: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MissingQualifierType
    ]
    Peaks: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakRefType
    ]
    Spectra: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumRefType
    ]
    VirtualPeaks: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VirtualPeakRefType
    ]

class IResourcesType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContent, IObjectRoot
):  # Interface
    CalibrationCurves: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibrationCurveType
    ]
    Instruments: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentType
    ]
    LabSamples: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LabSampleType
    ]
    SeparationMedia: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumType
    ]

class IRunTypeAndReplicationType(object):  # Interface
    ReplicationNo: int
    ReplicationNoSpecified: bool
    Val: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum

class ISampleAcquisitionParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType
):  # Interface
    FractionStartLocation: str
    InjectionSource: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSourceEnum
    )
    InjectionSourceInfo: str
    InjectionSourceSpecified: bool
    InjectionVolume: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    InjectorPosition: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectorPositionEnum
    )
    InjectorPositionSpecified: bool
    Instrument_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentRefType
    )
    NumberOfInjections: IntegerType
    OrderNo: IntegerType
    VialNumber: str

class ISampleContainer(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContainer,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    SampleMeasData: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleMeasDataType
    )
    SampleSetup: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleSetupType
    )  # readonly

class ISampleContextAcquisitionParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType
):  # Interface
    Instrument_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentRefType
    ]

class ISampleContextContainer(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContainer,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    SampleMeasDataContext: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleMeasDataContextType
    )
    SampleSetupContext: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleSetupContextType
    )  # readonly

class ISampleContextDataAnalysisParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType
):  # Interface
    BracketingMode: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingModeEnum
    )
    BracketingModeSpecified: bool

class ISampleContextIdentParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IIdentParamBaseType
):  # Interface
    ContextInfo: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextInfoType
    )

class ISampleContextInfoType(object):  # Interface
    ContentIntegrity: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextIntegrityEnum
    )
    ContentType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextTypeEnum
    )
    SourceType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextSourceEnum
    )

class ISampleContextsType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContent, IObjectRoot
):  # Interface
    MeasData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleMeasDataContextType
    ]
    Setups: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupContextType
    ]

class ISampleDataAnalysisParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDaParam,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType,
):  # Interface
    BracketingType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingTypeEnum
    )
    BracketingTypeSpecified: bool
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    TypeSpecified: bool
    UpdateInterval: IntegerType

class ISampleIdentParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IIdentParamBaseType
):  # Interface
    Barcode: str
    ExpectedBarcode: str
    LabSample_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LabSampleRefType
    LimsIDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LimsIDType
    ]
    PlateID: str

class ISampleMeasDataContextType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    AcqParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextAcquisitionParamType
    )
    AcquisitionApplication: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CreatedByApplicationType
    )
    AcquisitionSoftware: str
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleMeasDataContextAppSpecType
    )
    DiagnosticData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    IdentParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextIdentParamType
    )
    SampleMeasData_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleMeasDataRefType
    ]
    SampleSetupContext_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupContextRefType
    )
    Signals: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalType
    ]

class ISampleMeasDataType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    AcqParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleAcquisitionParamType
    )
    AcquisitionSoftware: str
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleMeasDataAppSpecType
    )
    DiagnosticData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    IdentParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleIdentParamType
    )
    InjectionMeasData_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionMeasDataRefType
    ]
    SampleSetup_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupRefType
    )
    Signals: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalType
    ]

class ISamplePurityContainer(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContainer,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    SamplePurityResult: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSSamplePurityResultType
    )  # readonly
    SamplePuritySetup: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSSamplePuritySetupType
    )  # readonly

    def AddSamplePurityResult(
        self,
        samplePurityResult: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSSamplePurityResultType,
    ) -> None: ...

class ISampleResultRefType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    ...

class ISampleSetupContextRefType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    ...

class ISampleSetupContextType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    AcqParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextAcquisitionParamType
    )
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupContextAppSpecType
    )
    DAParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextDataAnalysisParamType
    )
    IdentParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextIdentParamType
    )
    Locked: bool
    LockedSpecified: bool
    PackagingMode: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PackagingModeEnum
    )
    PackagingModeSpecified: bool
    SampleSetup_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupRefType
    ]
    SourceSystemRev: str
    TechSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupContextTechSpecType
    )

class ISampleSetupRefType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    ...

class ISampleSetupTechSpecType(object):  # Interface
    CE: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CESampleSetupType
    MS: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSampleSetupType

class ISampleSetupType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    AcqParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleAcquisitionParamType
    )
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupAppSpecType
    )
    DAParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleDataAnalysisParamType
    )
    IdentParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleIdentParamType
    )
    SourceSystemRev: str
    TechSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupTechSpecType
    )

class ISamplesType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContent, IObjectRoot
):  # Interface
    MeasData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleMeasDataType
    ]
    Setups: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupType
    ]

class ISeparationMediumColumnType(object):  # Interface
    BatchNo: str
    BubbleCap: bool
    BubbleCapSpecified: bool
    DeadVolume: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Diameter: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    EffLength: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    FilmThickness: DoubleType
    Length: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    MaxPH: DoubleType
    MaxPressure: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    MaxTemp: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    ParticleSize: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    ProdNo: str
    SerialNo: str
    UserText: str
    VoidTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType

class ISeparationMediumType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumAppSpecType
    )
    Type: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpecificSeparationMediumType
    )

class ISignalContainer(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContainer,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    SignalMeasData: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType
    )  # readonly
    SignalRawData: IChromData
    SignalResult: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionSignalResultType
    )
    SpectrumRawData: ISpectrumData

class ISignalType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    AutomationGenerated: bool
    BackgroundSubtraction: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionSignalType
    )
    BeginTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    BeginTimeAnalysis: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    ChannelName: str
    DetectorInstance: str
    DetectorName: str
    EndIndex: IntegerType
    EndTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    EndTimeAnalysis: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    ExtractionParameters: str
    Frequency: DoubleType
    MSSpectrumSearchResults: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSpectrumSearchResultsType
    )
    PeakDeletions: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakDeletionType
    ]
    StartIndex: IntegerType
    TechSpec: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalTechSpecType
    TimeShift: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    TraceID: str
    Type: str
    UserGenerated: bool
    XAxisScalingFactor: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    YAxisScalingFactor: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )

class ISpectrumType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericNonVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    ExprType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    RetentionTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Signal_ID: Any
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumTypeEnum
    WaveLengths: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    ]

class IStandardCompoundAmountType(IObjectRoot):  # Interface
    Amount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Identifier: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.StandardCompoundIdentifierType
    )

class IStandardCompoundIdentifierType(object):  # Interface
    Item: Any

class ITimePeriodType(object):  # Interface
    Unit: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimeUnitEnum
    UnitSpecified: bool
    Val: float

class IUVSpectrumLibraryHitType(object):  # Interface
    AboveThreshold: bool
    LibraryCompoundName: str
    LibraryID: IntegerType
    MatchNumber: IntegerType
    ReferenceSubtractionMode: str
    RetentionTime: DoubleType
    Similarity: DoubleType

class IUVSpectrumLibraryType(object):  # Interface
    LibraryName: str
    LibraryPath: str
    UVSpectrumHits: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.UVSpectrumLibraryHitType
    ]

class IUVSpectrumSearchResultsType(object):  # Interface
    UVSpectrumLibraries: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.UVSpectrumLibraryType
    ]

class IVersionedExternalObjectBaseType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    Path: str

class IVersionedObjectBaseType(IObjectBaseType, IObjectRoot):  # Interface
    Ver: int

class IVirtualPeakType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectBaseType,
    IObjectRoot,
):  # Interface
    Area: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    AreaPercent: DoubleType
    Baseline: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    BaselineEnd: DoubleType
    BaselineStart: DoubleType
    BeginTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    EndTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Height: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    HeightPercent: DoubleType
    LevelEnd: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    LevelStart: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Peak_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakRefType
    ]
    RetentionTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Symmetry: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Type: str
    WidthBase: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType

class InjectionAcquisitionParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionAcquisitionParamType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType,
):  # Class
    def __init__(self) -> None: ...

    Method_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodRefType
    OrderNo: IntegerType
    OverridenMethodParameters: System.Collections.Generic.List[MethodParameterType]

class InjectionCompoundIdentificationType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundIdentificationType,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QualifiedInjectionCompoundIdentificationType
    )

class InjectionCompoundQuantitationTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Area: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    ) = ...  # static # readonly
    AreaPerc: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    ) = ...  # static # readonly
    Count: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    ) = ...  # static # readonly
    CustomExpression: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    ) = ...  # static # readonly
    Height: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    ) = ...  # static # readonly
    HeightPerc: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    ) = ...  # static # readonly
    LogArea: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    ) = ...  # static # readonly
    LogHeight: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    ) = ...  # static # readonly

class InjectionCompoundRefType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundRefType,
):  # Class
    def __init__(self) -> None: ...

class InjectionCompoundTechSpecType:  # Class
    def __init__(self) -> None: ...

    GE: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEInjectionCompoundType
    MS: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSInjectionCompoundType

class InjectionCompoundType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericNonVersionedObjectType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GenericNonVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    Amount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Area: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    AverageResponseFactor: DoubleType
    CalibMarginPercent: DoubleType
    CalibWeight: DoubleType
    CalibrationAmount: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    CalibrationCurve_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibrationCurveRefType
    )
    Comment: str
    CompoundName: str
    Concentration: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    CorrExpectedRetTime: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    CorrectedArea: DoubleType
    ExpectedRetTime: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    ExpectedSignal: str
    Height: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    HighConcentration: DoubleType
    Identification: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundIdentificationType
    )
    IsInternalStandard: bool
    IsInternalStandardSpecified: bool
    IsTimeRef: bool
    IsTimeRefSpecified: bool
    LOD: DoubleType
    LOQ: DoubleType
    LowConcentration: DoubleType
    LowerAmountLimit: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    Multiplier: DoubleType
    NormAmount: DoubleType
    QuantitationType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundQuantitationTypeEnum
    )
    QuantitationTypeSpecified: bool
    ResponseCorrectionFactor: DoubleType
    ResponseFactor: DoubleType
    ResponseFactorCalcMode: ResponseFactorCalcModeEnum
    ResponseFactorCalcModeSpecified: bool
    SpectraConfirmMatchFactor: DoubleType
    SpectraConfirmResult: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectraConfirmResultEnum
    )
    SpectraConfirmResultFieldSpecified: bool
    TechSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundTechSpecType
    )
    TimeRanges: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimeRangeType
    ]
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CompoundTypeEnum
    UpperAmountLimit: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    UsedInternalStandards: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.StandardCompoundIdentifierType
    ]

class InjectionDataAnalysisParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionDataAnalysisParamType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDaParam,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType,
):  # Class
    def __init__(self) -> None: ...

    BackgroundSubtraction: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionType
    )
    CalibrationLevel: IntegerType
    CalibrationStandards: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.StandardCompoundAmountType
    ]
    DilutionFactors: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CorrectionFactorType
    ]
    InjectionAmount: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    InternalStandards: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.StandardCompoundAmountType
    ]
    Method_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodRefType
    Multipliers: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CorrectionFactorType
    ]
    OrderNo: IntegerType
    ResponseFactorUpdate: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResponseFactorUpdateEnum
    )
    ResponseFactorUpdateSpecified: bool
    ResponseFactorUpdateWeight: DoubleType
    RetentionTimeUpdate: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RetentionTimeUpdateEnum
    )
    RetentionTimeUpdateSpecified: bool
    RetentionTimeUpdateWeight: DoubleType
    RunTypes: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeAndReplicationType
    ]
    SampleAmount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    SampleBracketingType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingTypeEnum
    )
    SampleBracketingTypeSpecified: bool
    SampleOrderNo: IntegerType
    SampleType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    SampleTypeSpecified: bool

class InjectionMeasDataAppSpecType:  # Class
    def __init__(self) -> None: ...

    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgtChemStoreInjectionMeasDataType
    )

class InjectionMeasDataRefType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionMeasDataRefType,
):  # Class
    def __init__(self) -> None: ...

class InjectionMeasDataTechSpecType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionMeasDataTechSpecType
):  # Class
    def __init__(self) -> None: ...

    LC: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LCInjectionMeasDataType

class InjectionMeasDataType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionMeasDataType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
):  # Class
    def __init__(self) -> None: ...

    AcqParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionAcquisitionParamType
    )
    AcquisitionApplication: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CreatedByApplicationType
    )
    AcquisitionIdentifier: str
    AcquisitionMethodVersion: str
    AcquisitionSoftware: str
    AcquitionStatus: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AcquisitionStatusType
    )
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionMeasDataAppSpecType
    )
    DiagnosticData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    ExternalResultPath: str
    InjectionSeparationMedia: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSeparationMediumType
    ]
    InjectionVolume: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    RunTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Signals: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalType
    ]
    TechSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionMeasDataTechSpecType
    )

class InjectionModificationEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ManualCompoundId: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionModificationEnum
    ) = ...  # static # readonly
    ManualIntegration: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionModificationEnum
    ) = ...  # static # readonly
    ManualIntegrationAndCompoundId: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionModificationEnum
    ) = ...  # static # readonly

class InjectionResultAppSpecType:  # Class
    def __init__(self) -> None: ...

    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgtChemStoreInjectionResultType
    )

class InjectionResultRefType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionResultRefType,
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class InjectionResultTechSpecType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionResultTechSpecType
):  # Class
    def __init__(self) -> None: ...

    CE: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CEInjectionResultType
    GE: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEInjectionResultType
    MS: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSInjectionResultType

class InjectionResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionResultType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
):  # Class
    def __init__(self) -> None: ...

    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionResultAppSpecType
    )
    DAParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionDataAnalysisParamType
    )
    DataAnalysisApplication: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CreatedByApplicationType
    )
    DataAnalysisMethodVersion: str
    DataAnalysisSoftware: str
    InjectionCompounds: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundType
    ]
    InjectionMeasData_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionMeasDataRefType
    )
    Label: str
    ManualModification: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionModificationEnum
    )
    ManualModificationSpecified: bool
    NoiseType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NoiseTypeEnum
    NoiseTypeSpecified: bool
    ProcessingStatus: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingStatusType
    )
    ReferencedInjectionInfo: str
    ReprocessingRequired: bool
    ReprocessingRequiredSpecified: bool
    SignalResults: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSignalResultType
    ]
    TechSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionResultTechSpecType
    )
    VirtualPeaks: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VirtualPeakType
    ]

class InjectionSeparationMediumType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionSeparationMediumType
):  # Class
    def __init__(self) -> None: ...

    AutoDetect: bool
    InjectionCount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LongType
    Position: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumPositionEnum
    )
    SeparationMedium_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumRefType
    )
    UsedForInjection: bool
    UsedForInjectionSpecified: bool

class InjectionSignalResultRefType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class InjectionSignalResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericNonVersionedObjectType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GenericNonVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionSignalResultType,
):  # Class
    def __init__(self) -> None: ...

    NoisePeriods: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NoisePeriodType
    ]
    Peaks: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakType
    ]
    Signal_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalRefType
    Spectra: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumType
    ]

class InjectionSourceEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    InjectorProgram: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSourceEnum
    ) = ...  # static # readonly
    ManualInjection: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSourceEnum
    ) = ...  # static # readonly
    NoInjection: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSourceEnum
    ) = ...  # static # readonly
    StandardInjection: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSourceEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSourceEnum
    ) = ...  # static # readonly

class InjectionsType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionsType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContent,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    MeasData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionMeasDataType
    ]
    Results: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionResultType
    ]

class InjectorPositionEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Back: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectorPositionEnum = (
        ...
    )  # static # readonly
    Front: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectorPositionEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectorPositionEnum
    ) = ...  # static # readonly

class InstrumentAppSpecType:  # Class
    def __init__(self) -> None: ...

    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgtChemStoreInstrumentType
    )

class InstrumentModuleType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInstrumentModuleType
):  # Class
    def __init__(self) -> None: ...

    AdditionalInformation: str
    ConnectionInfo: str
    DisplayName: str
    DriverVersion: str
    FirmwareRevision: str
    Manufacturer: str
    Name: str
    PartNo: str
    SerialNo: str
    Type: str

class InstrumentRefType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class InstrumentTechniqueEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CapillaryElectrophoresis: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentTechniqueEnum
    ) = ...  # static # readonly
    GasChromatography: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentTechniqueEnum
    ) = ...  # static # readonly
    LiquidChromatography: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentTechniqueEnum
    ) = ...  # static # readonly
    MassSpectrometry: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentTechniqueEnum
    ) = ...  # static # readonly
    MicroFluidics: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentTechniqueEnum
    ) = ...  # static # readonly
    UVVis: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentTechniqueEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentTechniqueEnum
    ) = ...  # static # readonly

class InstrumentType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInstrumentType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NamedGenericVersionedObjectType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    AppSpec: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentAppSpecType
    Modules: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentModuleType
    ]
    SeparationMedium_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumRefType
    ]
    Technique: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentTechniqueEnum
    )

class IntegerUnitType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IIntegerUnitType,
    ValueBaseType,
    IIntegerType,
):  # Class
    def __init__(self) -> None: ...

    Unit: str
    Val: int

class LCFractionType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILCFractionType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    EndTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Location: str
    Mass: str
    Number: IntegerType
    Purity: DoubleType
    Reason: str
    StartTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Volume: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Well: str

class LCInjectionMeasDataType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILCInjectionMeasDataType
):  # Class
    def __init__(self) -> None: ...

    Fractions: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LCFractionType
    ]

class LCSampleContextSetupType:  # Class
    def __init__(self) -> None: ...

    FractionStartLocation: str

class LabSampleRefType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILabSampleRefType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class LabSampleType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILabSampleType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    Barcode: str
    LimsIDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LimsIDType
    ]

class LimsIDType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILimsIDType
):  # Class
    def __init__(self) -> None: ...

    Key: str
    Name: str

class LinkMode(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    CreateNewAndLink: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LinkMode = (
        ...
    )  # static # readonly
    FindFirstOrCreateNewAndLink: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LinkMode
    ) = ...  # static # readonly
    LinkToSpecifiedTargets: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LinkMode
    ) = ...  # static # readonly
    TryFindFirstAndLink: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LinkMode
    ) = ...  # static # readonly

class LongType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILongType, ValueBaseType
):  # Class
    def __init__(self) -> None: ...

    Val: int

class LongUnitType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILongUnitType,
    ValueBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ILongType,
):  # Class
    def __init__(self) -> None: ...

    Unit: str
    Val: int

class MSFoundEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Found: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundEnum = (
        ...
    )  # static # readonly
    FoundConfirmed: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundEnum
    ) = ...  # static # readonly
    NotFound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundEnum = (
        ...
    )  # static # readonly
    Undefined: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundEnum = (
        ...
    )  # static # readonly

class MSFoundPolarityEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Negative: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundPolarityEnum
    ) = ...  # static # readonly
    Positive: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundPolarityEnum
    ) = ...  # static # readonly
    PositiveAndNegative: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundPolarityEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundPolarityEnum
    ) = ...  # static # readonly

class MSInjectionCompoundType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSInjectionCompoundType
):  # Class
    def __init__(self) -> None: ...

    Found: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundEnum
    FoundDescription: str
    FoundPolarity: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSFoundPolarityEnum
    )
    FoundPolaritySpecified: bool
    FoundSpecified: bool
    MolFormula: str
    MonoIsotopicMass: DoubleType
    Purity: DoubleType
    PurityBaseSignalDescription: str
    SpectraConfirmMatchFactor: DoubleType
    SpectraConfirmResult: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectraConfirmResultEnum
    )
    SpectraConfirmResultSpecified: bool

class MSInjectionResultType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSInjectionResultType
):  # Class
    def __init__(self) -> None: ...

    SamplePurityResults: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSamplePurityResultType
    ]

class MSIonPolarityEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Negative: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSIonPolarityEnum
    ) = ...  # static # readonly
    Positive: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSIonPolarityEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSIonPolarityEnum
    ) = ...  # static # readonly

class MSPeakType:  # Class
    def __init__(self) -> None: ...

    AutomassHigh: DoubleType
    AutomassLow: DoubleType
    CrossSignalAreaPercent: DoubleType
    PurityReportValueLC: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSPurityReportValueEnum
    )
    PurityReportValueLCSpecified: bool
    PurityReportValueMS: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSPurityReportValueEnum
    )
    PurityReportValueMSSpecified: bool
    TotalIonCurrent: DoubleType

class MSPurityReportValueEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Good: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSPurityReportValueEnum
    ) = ...  # static # readonly
    Mix: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSPurityReportValueEnum
    ) = ...  # static # readonly
    Noisy: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSPurityReportValueEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSPurityReportValueEnum
    ) = ...  # static # readonly

class MSSamplePurityResultType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSSamplePurityResultType,
):  # Class
    def __init__(self) -> None: ...

    MSSamplePuritySetup_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSamplePuritySetupRefType
    )
    Peak_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakRefType
    SamplePurity: DoubleType
    Signal_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalRefType
    TargetFound: bool
    TargetPure: bool

class MSSamplePuritySetupRefType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class MSSamplePuritySetupType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSSamplePuritySetupType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    TargetFormula: str
    TargetMass: DoubleType
    TargetName: str

class MSSampleSetupType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSSampleSetupType
):  # Class
    def __init__(self) -> None: ...

    SamplePuritySetups: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSamplePuritySetupType
    ]

class MSSignalType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSSignalType
):  # Class
    def __init__(self) -> None: ...

    FragmentorVoltage: int
    FragmentorVoltageSpecified: bool
    IonPolarity: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSIonPolarityEnum
    IonizationMode: str
    MaximumIonIntensity: DoubleType
    ScanType: str
    StorageMode: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSStorageModeEnum

class MSSpectrumLibraryHitType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSSpectrumLibraryHitType
):  # Class
    def __init__(self) -> None: ...

    CASNumber: str
    LibaryNumber: IntegerType
    LibraryCompoundName: str
    LibraryID: IntegerType
    LibrarySpectrumRefLib: IntegerType
    LibrarySpectrumRefLoc: IntegerType
    LibrarySpectrumRefType: IntegerType
    MatchNumber: IntegerType
    ProbabilityPercent: DoubleType
    ReverseMatchNumber: IntegerType
    UserCompoundName: str

class MSSpectrumLibraryType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSSpectrumLibraryType
):  # Class
    def __init__(self) -> None: ...

    LibraryName: str
    LibraryPath: str
    MSSpectrumHits: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSpectrumLibraryHitType
    ]

class MSSpectrumSearchResultsType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMSSpectrumSearchResultsType
):  # Class
    def __init__(self) -> None: ...

    MSSpectrumLibraries: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSpectrumLibraryType
    ]

class MSStorageModeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Centroid: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSStorageModeEnum
    ) = ...  # static # readonly
    Continuous: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSStorageModeEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSStorageModeEnum
    ) = ...  # static # readonly

class MethodAppSpecType:  # Class
    def __init__(self) -> None: ...

    Item: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgtChemStoreMethodType

class MethodConfigurationExternalRefType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedExternalObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedExternalObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class MethodConfigurationLinkType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodConfigurationLinkType
):  # Class
    def __init__(self) -> None: ...

    Item: Any

class MethodConfigurationRefType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class MethodInstructionType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodInstructionType,
):  # Class
    def __init__(self) -> None: ...

    Function: str
    Index: int
    ParameterString: str
    Parameters: System.Collections.Generic.List[MethodParameterType]
    Time: float
    TimeSpecified: bool

class MethodRefType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class MethodTechSpecType:  # Class
    def __init__(self) -> None: ...

    CE: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CEMethodType

class MethodType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NamedGenericVersionedObjectType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    AppSpec: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodAppSpecType
    Application: str
    Instrument_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentRefType
    ]
    Integrator: str
    MethodConfigurationLink: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodConfigurationLinkType
    )
    OriginalVersion: str
    QuantitationMethod: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QuantificationMethodEnum
    )
    QuantitationMethodSpecified: bool
    SeparationMedium_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumRefType
    ]
    TechSpec: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodTechSpecType

class MigrationHistoryType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMigrationHistoryType
):  # Class
    def __init__(self) -> None: ...

    MigrationSteps: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MigrationStepType
    ]

class MigrationStepType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMigrationStepType
):  # Class
    def __init__(self) -> None: ...

    Application: str
    Date: System.DateTime
    FromNamespace: str
    ToNamespace: str

class MissingQualifierType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMissingQualifierType
):  # Class
    def __init__(self) -> None: ...

    Mass: DoubleType
    SignalName: str

class NamedGenericVersionedObjectType(
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
):  # Class
    def __init__(self) -> None: ...

    Description: str
    Name: str
    ProjectID: str

class NoisePeriodType(
    IObjectRoot, Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INoisePeriodType
):  # Class
    def __init__(self) -> None: ...

    Drift: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Noise6SD: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    NoiseASTM: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    NoisePToP: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    TimeFrom: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    TimeTo: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Wander: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType

class NoiseTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Noise6sd: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NoiseTypeEnum = (
        ...
    )  # static # readonly
    NoiseAstm: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NoiseTypeEnum = (
        ...
    )  # static # readonly
    NoiseP2p: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NoiseTypeEnum = (
        ...
    )  # static # readonly
    NoiseRms: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NoiseTypeEnum = (
        ...
    )  # static # readonly
    Undefined: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NoiseTypeEnum = (
        ...
    )  # static # readonly

class NonVersionedObjectBaseType(
    ObjectBaseType,
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class PackagingModeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Classic: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PackagingModeEnum = (
        ...
    )  # static # readonly
    FullResultSet: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PackagingModeEnum
    ) = ...  # static # readonly
    ResultSetWithMethods: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PackagingModeEnum
    ) = ...  # static # readonly
    ResultSetWithTemplates: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PackagingModeEnum
    ) = ...  # static # readonly
    SimpleResultSet: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PackagingModeEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PackagingModeEnum
    ) = ...  # static # readonly

class PeakDeletionType:  # Class
    def __init__(self) -> None: ...

    DeletionType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakDeletionTypeEnum
    )
    Range: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimeRangeType

class PeakDeletionTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DeletePeak: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakDeletionTypeEnum
    ) = ...  # static # readonly
    DeleteRegion: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakDeletionTypeEnum
    ) = ...  # static # readonly

class PeakRefType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakRefType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    CalibPeakRole: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum
    )
    CalibPeakRoleSpecified: bool
    CalibrationCurve_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibrationCurveRefType
    )
    QualifierPassed: bool
    QualifierPassedSpecified: bool
    QualifierRatioRangeFitMode: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QualifierRatioFitModeEnum
    )
    QualifierRatioRangeFitModeSpecified: bool
    QualifierRatioRangeMax: float
    QualifierRatioRangeMaxSpecified: bool
    QualifierRatioRangeMin: float
    QualifierRatioRangeMinSpecified: bool

class PeakTechSpecType:  # Class
    def __init__(self) -> None: ...

    CE: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CEPeakType
    GE: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GEPeakType
    MS: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSPeakType

class PeakType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType,
):  # Class
    def __init__(self) -> None: ...

    Area: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    AreaPercent: DoubleType
    AreaSum: DoubleType
    AssociatedSpectra: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AssociatedSpectraType
    )
    Asymmetry_10Perc: DoubleType
    Asymmetry_5SigmaPerc: DoubleType
    BaselineCode: str
    BaselineEnd: DoubleType
    BaselineModel: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BaselineModelEnum
    )
    BaselineModelSpecified: bool
    BaselineParameters: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BaselineParametersType
    )
    BaselineRetentionHeight: DoubleType
    BaselineStart: DoubleType
    BeginTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    CapacityFactor: DoubleType
    CentroidTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    ComplexCustomFields: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    CorrExpRetTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    DownInflectionBaselineTime: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    DownInflectionBaselineY: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    DownSlopeSimilarity: DoubleType
    EndTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Excess: DoubleType
    FrontTangentOffset: DoubleType
    FrontTangentSlope: DoubleType
    Height: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    HeightPercent: DoubleType
    HeightSum: DoubleType
    HeightToValleyRatioAfter: DoubleType
    HeightToValleyRatioBefore: DoubleType
    InflectionTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    InflectionY: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    KovatsIndex: DoubleType
    LambdaMax: DoubleType
    LambdaMin: DoubleType
    LevelEnd: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    LevelStart: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    MSSpectrumSearchResults: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSpectrumSearchResultsType
    )
    Noise: DoubleType
    Noise6Sigma: DoubleType
    Number: IntegerType
    PeakValleyRatio: DoubleType
    Plate2Sigma: DoubleType
    Plate3Sigma: DoubleType
    Plate4Sigma: DoubleType
    Plate5Sigma: DoubleType
    PlatesPerColumn_FoleyDorsey: DoubleType
    PlatesPerMeter_AOH: DoubleType
    PlatesPerMeter_EMG: DoubleType
    PlatesPerMeter_EP: DoubleType
    PlatesPerMeter_FoleyDorsey: DoubleType
    PlatesPerMeter_JP: DoubleType
    PlatesPerMeter_USP: DoubleType
    PlatesStatistical: DoubleType
    Purity: DoubleType
    PurityPassed: bool
    QualifierMass: DoubleType
    RSDPercent: DoubleType
    ReferencePeakIdentifier: str
    RelativeRetentionTime: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    RelativeRetentionTime_EP: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    Resolution5Sigma: DoubleType
    ResolutionStatistical: DoubleType
    Resolution_AOH: DoubleType
    Resolution_DAB: DoubleType
    Resolution_EMG: DoubleType
    Resolution_EP: DoubleType
    Resolution_JP: DoubleType
    Resolution_USP: DoubleType
    Resolution_USP_HH: DoubleType
    ResponseRatio: DoubleType
    RetentionTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Selectivity: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    SignalToNoise: DoubleType
    SignalToNoise6Sigma: DoubleType
    SignalToNoiseEP: DoubleType
    SignalToNoiseUSP: DoubleType
    SimilarityIndex: DoubleType
    SimpleCustomFields: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldsType
    )
    Skew: DoubleType
    StatisticalMoment0: DoubleType
    StatisticalMoment1: DoubleType
    StatisticalMoment2: DoubleType
    StatisticalMoment3: DoubleType
    StatisticalMoment4: DoubleType
    Symmetry: DoubleType
    TailTangentOffset: DoubleType
    TailTangentSlope: DoubleType
    TailingFactor: DoubleType
    TechSpec: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTechSpecType
    TheoreticalPlates_AOH: DoubleType
    TheoreticalPlates_EMG: DoubleType
    TheoreticalPlates_EP: DoubleType
    TheoreticalPlates_JP: DoubleType
    TheoreticalPlates_USP: DoubleType
    ThreePointPurity: DoubleType
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    UVSpectrumSearchResults: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.UVSpectrumSearchResultsType
    )
    UpInflectionBaselineTime: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    UpInflectionBaselineY: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    UpSlopeSimilarity: DoubleType
    Width2Sigma: DoubleType
    Width3Sigma: DoubleType
    Width4Sigma: DoubleType
    Width5Sigma: DoubleType
    WidthBase: DoubleType
    WidthTangent: DoubleType
    Width_10Perc: DoubleType
    Width_50Perc: DoubleType
    Width_5Perc: DoubleType

class PeakTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AreaSum: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum = (
        ...
    )  # static # readonly
    FrontShoulderDropLine: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    FrontShoulderTangent: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    Manual: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum = (
        ...
    )  # static # readonly
    ManualNegative: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    ManualNegativeShoulderDropLine: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    ManualNegativeShoulderTangent: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    ManualShoulderDropLine: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    ManualShoulderTangent: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    ManualTangentSkimExpo: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    ManualTangentSkimNewExpo: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    ManualTangentSkimNormal: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    Negative: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum = (
        ...
    )  # static # readonly
    NegativeShoulderDropLine: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    NegativeShoulderTangent: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    NormalPeak: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum = (
        ...
    )  # static # readonly
    ReCalcSolventPeak: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    RearSholderDropLine: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    RearShoulderTangent: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    ShoulderDropLine: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    ShoulderTangent: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    Solvent: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum = (
        ...
    )  # static # readonly
    Tangent: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum = (
        ...
    )  # static # readonly
    TangentSkimExpo: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    TangentSkimNewExpo: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    TangentSkimNormal: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum
    ) = ...  # static # readonly
    Unknown: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakTypeEnum = (
        ...
    )  # static # readonly

class ProcessingStatusItemType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IProcessingStatusItemType
):  # Class
    def __init__(self) -> None: ...

    Category: str
    Message: str
    TransformationState: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationStateEnum
    )

class ProcessingStatusType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IProcessingStatusType
):  # Class
    def __init__(self) -> None: ...

    ProcessingStatusItems: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingStatusItemType
    ]
    TransformationChainState: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationChainStateEnum
    )
    TransformationChainStateSpecified: bool

class ProcessingTranformationChainStateEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Aborted: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationChainStateEnum
    ) = ...  # static # readonly
    Failed: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationChainStateEnum
    ) = ...  # static # readonly
    NoMethodProvided: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationChainStateEnum
    ) = ...  # static # readonly
    NotExecuted: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationChainStateEnum
    ) = ...  # static # readonly
    Passed: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationChainStateEnum
    ) = ...  # static # readonly
    PassedWithWarning: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationChainStateEnum
    ) = ...  # static # readonly

class ProcessingTranformationStateEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Failed: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationStateEnum
    ) = ...  # static # readonly
    NotReady: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationStateEnum
    ) = ...  # static # readonly
    Passed: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationStateEnum
    ) = ...  # static # readonly
    PassedWithWarning: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationStateEnum
    ) = ...  # static # readonly
    Ready: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ProcessingTranformationStateEnum
    ) = ...  # static # readonly

class QualifiedInjectionCompoundIdentificationType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IQualifiedInjectionCompoundIdentificationType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundIdentificationItem,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    InjectionCompounds: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionCompoundRefType
    ]
    MissingQualifiers: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MissingQualifierType
    ]
    Peaks: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakRefType
    ]
    Spectra: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumRefType
    ]
    VirtualPeaks: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VirtualPeakRefType
    ]

    def ShouldSerializeInjectionCompounds(self) -> bool: ...
    def ShouldSerializePeaks(self) -> bool: ...
    def ShouldSerializeMissingQualifiersFields(self) -> bool: ...
    def ShouldSerializeSpectra(self) -> bool: ...
    def ShouldSerializeVirtualPeaks(self) -> bool: ...

class QualifierRatioFitModeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    PeakNotFound: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QualifierRatioFitModeEnum
    ) = ...  # static # readonly
    RatioRangeAbove: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QualifierRatioFitModeEnum
    ) = ...  # static # readonly
    RatioRangeBelow: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QualifierRatioFitModeEnum
    ) = ...  # static # readonly
    RatioRangeOk: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QualifierRatioFitModeEnum
    ) = ...  # static # readonly
    Unknown: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QualifierRatioFitModeEnum
    ) = ...  # static # readonly

class QuantificationMethodEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Area: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QuantificationMethodEnum
    ) = ...  # static # readonly
    ESTD: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QuantificationMethodEnum
    ) = ...  # static # readonly
    ESTD1: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QuantificationMethodEnum
    ) = ...  # static # readonly
    Height: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QuantificationMethodEnum
    ) = ...  # static # readonly
    ISTD: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QuantificationMethodEnum
    ) = ...  # static # readonly
    ISTD1: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QuantificationMethodEnum
    ) = ...  # static # readonly
    Norm: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QuantificationMethodEnum
    ) = ...  # static # readonly
    Unknown: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.QuantificationMethodEnum
    ) = ...  # static # readonly

class ResourcesType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContent,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IResourcesType,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    CalibrationCurves: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibrationCurveType
    ]
    Instruments: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentType
    ]
    LabSamples: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LabSampleType
    ]
    SeparationMedia: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumType
    ]

class ResponseFactorUpdateEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Average: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResponseFactorUpdateEnum
    ) = ...  # static # readonly
    Bracketing: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResponseFactorUpdateEnum
    ) = ...  # static # readonly
    DeltaPercent: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResponseFactorUpdateEnum
    ) = ...  # static # readonly
    NoUpdate: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResponseFactorUpdateEnum
    ) = ...  # static # readonly
    Replace: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResponseFactorUpdateEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResponseFactorUpdateEnum
    ) = ...  # static # readonly

class RetentionTimeUpdateEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Average: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RetentionTimeUpdateEnum
    ) = ...  # static # readonly
    Bracketing: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RetentionTimeUpdateEnum
    ) = ...  # static # readonly
    NoUpdate: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RetentionTimeUpdateEnum
    ) = ...  # static # readonly
    Replace: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RetentionTimeUpdateEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RetentionTimeUpdateEnum
    ) = ...  # static # readonly

class RunTypeAndReplicationType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IRunTypeAndReplicationType
):  # Class
    def __init__(self) -> None: ...

    ReplicationNo: int
    ReplicationNoSpecified: bool
    Val: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum

class RunTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AverageReplicates: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    BaselineCheck: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    BaselineFile: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    BeginCalibration: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    BeginLoop: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    BeginSummary: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    BeginSystemSuitability: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    ClearAllCalibration: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    ClearCalibrationAtLevel: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    ClearReplicates: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    Duplicate: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    EndCalibration: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    EndLoop: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    EndSummary: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    EndSystemSuitability: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    PrintAdditionalReports: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    PrintCalibrationReport: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    QCCheckStandard: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    Shutdown: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    Spike1Of2: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    Spike2Of2: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    Spiked: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    SummaryRun: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    SystemSuitablityStandard: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum
    ) = ...  # static # readonly
    Undefined: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    Unspiked: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly
    VialSummary: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeEnum = (
        ...
    )  # static # readonly

class SampleAcquisitionParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleAcquisitionParamType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType,
):  # Class
    def __init__(self) -> None: ...

    FractionStartLocation: str
    InjectionSource: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionSourceEnum
    )
    InjectionSourceInfo: str
    InjectionSourceSpecified: bool
    InjectionVolume: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    InjectorPosition: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectorPositionEnum
    )
    InjectorPositionSpecified: bool
    Instrument_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentRefType
    )
    Method_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodRefType
    NumberOfInjections: IntegerType
    OrderNo: IntegerType
    VialNumber: str

class SampleContextAcquisitionParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContextAcquisitionParamType,
):  # Class
    def __init__(self) -> None: ...

    Instrument_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InstrumentRefType
    ]
    Method_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodRefType

class SampleContextDataAnalysisParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContextDataAnalysisParamType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType,
):  # Class
    def __init__(self) -> None: ...

    BracketingMode: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingModeEnum
    )
    BracketingModeSpecified: bool
    Method_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodRefType

class SampleContextIdentParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContextIdentParamType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IIdentParamBaseType,
):  # Class
    def __init__(self) -> None: ...

    ContextInfo: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextInfoType
    )
    Description: str
    Name: str
    ProjectID: str

class SampleContextInfoType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContextInfoType
):  # Class
    def __init__(self) -> None: ...

    ContentIntegrity: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextIntegrityEnum
    )
    ContentType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextTypeEnum
    )
    SourceType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextSourceEnum
    )

class SampleContextIntegrityEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Complete: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextIntegrityEnum
    ) = ...  # static # readonly
    Partial: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextIntegrityEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextIntegrityEnum
    ) = ...  # static # readonly

class SampleContextSourceEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Acquisition: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextSourceEnum
    ) = ...  # static # readonly
    Reprocessed: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextSourceEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextSourceEnum
    ) = ...  # static # readonly
    Virtual: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextSourceEnum
    ) = ...  # static # readonly

class SampleContextTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Sequence: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextTypeEnum
    ) = ...  # static # readonly
    SingleSample: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextTypeEnum
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextTypeEnum
    ) = ...  # static # readonly

class SampleContextsType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContextsType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContent,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    MeasData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleMeasDataContextType
    ]
    Setups: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupContextType
    ]

class SampleDataAnalysisParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDaParam,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleDataAnalysisParamType,
):  # Class
    def __init__(self) -> None: ...

    BracketingType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BracketingTypeEnum
    )
    BracketingTypeSpecified: bool
    CalibrationLevel: IntegerType
    CalibrationStandards: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.StandardCompoundAmountType
    ]
    DilutionFactors: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CorrectionFactorType
    ]
    InternalStandards: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.StandardCompoundAmountType
    ]
    Method_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MethodRefType
    Multipliers: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CorrectionFactorType
    ]
    OrderNo: IntegerType
    ResponseFactorUpdate: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ResponseFactorUpdateEnum
    )
    ResponseFactorUpdateSpecified: bool
    ResponseFactorUpdateWeight: DoubleType
    RetentionTimeUpdate: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RetentionTimeUpdateEnum
    )
    RetentionTimeUpdateSpecified: bool
    RetentionTimeUpdateWeight: DoubleType
    RunTypes: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.RunTypeAndReplicationType
    ]
    SampleAmount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    TypeSpecified: bool
    UpdateInterval: IntegerType

class SampleIdentParamType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IIdentParamBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleIdentParamType,
):  # Class
    def __init__(self) -> None: ...

    Barcode: str
    Description: str
    ExpectedBarcode: str
    LabSample_ID: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LabSampleRefType
    LimsIDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LimsIDType
    ]
    Name: str
    PlateID: str
    ProjectID: str

class SampleMeasDataAppSpecType:  # Class
    def __init__(self) -> None: ...

    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgtChemStoreSampleMeasDataType
    )

class SampleMeasDataContextAppSpecType:  # Class
    def __init__(self) -> None: ...

    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgtChemStoreSampleMeasDataContextType
    )

class SampleMeasDataContextRefType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class SampleMeasDataContextType(
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleMeasDataContextType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
):  # Class
    def __init__(self) -> None: ...

    AcqParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextAcquisitionParamType
    )
    AcquisitionApplication: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CreatedByApplicationType
    )
    AcquisitionSoftware: str
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleMeasDataContextAppSpecType
    )
    DiagnosticData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    IdentParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextIdentParamType
    )
    SampleMeasData_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleMeasDataRefType
    ]
    SampleSetupContext_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupContextRefType
    )
    Signals: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalType
    ]

class SampleMeasDataRefType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class SampleMeasDataType(
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleMeasDataType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
):  # Class
    def __init__(self) -> None: ...

    AcqParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleAcquisitionParamType
    )
    AcquisitionApplication: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CreatedByApplicationType
    )
    AcquisitionSoftware: str
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleMeasDataAppSpecType
    )
    DiagnosticData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomFieldType
    ]
    IdentParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleIdentParamType
    )
    InjectionMeasData_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.InjectionMeasDataRefType
    ]
    SampleSetup_ID: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupRefType
    )
    Signals: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalType
    ]

class SampleSetupAppSpecType:  # Class
    def __init__(self) -> None: ...

    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgtChemStoreSampleSetupType
    )

class SampleSetupContextAppSpecType:  # Class
    def __init__(self) -> None: ...

    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgtChemStoreSampleSetupContextType
    )

class SampleSetupContextRefType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleSetupContextRefType,
):  # Class
    def __init__(self) -> None: ...

class SampleSetupContextTechSpecType:  # Class
    def __init__(self) -> None: ...

    LC: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.LCSampleContextSetupType

class SampleSetupContextType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleSetupContextType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
):  # Class
    def __init__(self) -> None: ...

    AcqParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextAcquisitionParamType
    )
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupContextAppSpecType
    )
    DAParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextDataAnalysisParamType
    )
    IdentParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextIdentParamType
    )
    Locked: bool
    LockedSpecified: bool
    PackagingMode: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PackagingModeEnum
    )
    PackagingModeSpecified: bool
    SampleSetup_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupRefType
    ]
    SourceSystemRev: str
    TechSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupContextTechSpecType
    )

class SampleSetupRefType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleSetupRefType,
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class SampleSetupTechSpecType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleSetupTechSpecType
):  # Class
    def __init__(self) -> None: ...

    CE: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CESampleSetupType
    MS: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSampleSetupType

class SampleSetupType(
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleSetupType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
):  # Class
    def __init__(self) -> None: ...

    AcqParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleAcquisitionParamType
    )
    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupAppSpecType
    )
    DAParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleDataAnalysisParamType
    )
    IdentParam: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleIdentParamType
    )
    SourceSystemRev: str
    TechSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupTechSpecType
    )

class SampleTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Blank: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum = (
        ...
    )  # static # readonly
    Calibration: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    ) = ...  # static # readonly
    CalibrationCheck: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    ) = ...  # static # readonly
    Checkout: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum = (
        ...
    )  # static # readonly
    Control: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum = (
        ...
    )  # static # readonly
    DoubleBlank: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    ) = ...  # static # readonly
    Ladder: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum = (
        ...
    )  # static # readonly
    Matrix: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum = (
        ...
    )  # static # readonly
    MatrixBlank: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    ) = ...  # static # readonly
    MatrixDup: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum = (
        ...
    )  # static # readonly
    ResponseCheck: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    ) = ...  # static # readonly
    Sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum = (
        ...
    )  # static # readonly
    Spike: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum = (
        ...
    )  # static # readonly
    SystemSuitability: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    ) = ...  # static # readonly
    TuneCheck: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum = (
        ...
    )  # static # readonly
    Unspecified: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleTypeEnum
    ) = ...  # static # readonly

class SamplesType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplesType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IContent,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    MeasData: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleMeasDataType
    ]
    Setups: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleSetupType
    ]

class SeparationMediumAppSpecType:  # Class
    def __init__(self) -> None: ...

    Item: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgtChemStoreSeparationMediumType
    )

class SeparationMediumChipType:  # Class
    def __init__(self) -> None: ...

class SeparationMediumColumnType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISeparationMediumColumnType
):  # Class
    def __init__(self) -> None: ...

    BatchNo: str
    BubbleCap: bool
    BubbleCapSpecified: bool
    DeadVolume: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Diameter: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    EffLength: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    FilmThickness: DoubleType
    Length: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    MaxPH: DoubleType
    MaxPressure: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    MaxTemp: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    ParticleSize: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    ProdNo: str
    SerialNo: str
    UserText: str
    VoidTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType

class SeparationMediumPositionEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Front: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumPositionEnum
    ) = ...  # static # readonly
    Left: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumPositionEnum
    ) = ...  # static # readonly
    Rear: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumPositionEnum
    ) = ...  # static # readonly
    Right: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumPositionEnum
    ) = ...  # static # readonly
    Unknown: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumPositionEnum
    ) = ...  # static # readonly

class SeparationMediumRefType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class SeparationMediumType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISeparationMediumType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NamedGenericVersionedObjectType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    AppSpec: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SeparationMediumAppSpecType
    )
    Type: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpecificSeparationMediumType
    )

class SignalRefType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class SignalTechSpecType:  # Class
    def __init__(self) -> None: ...

    MS: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSignalType

class SignalType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NamedGenericVersionedObjectType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    AutomationGenerated: bool
    BackgroundSubtraction: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.BackgroundSubtractionSignalType
    )
    BeginTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    BeginTimeAnalysis: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    ChannelName: str
    DetectorInstance: str
    DetectorName: str
    EndIndex: IntegerType
    EndTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    EndTimeAnalysis: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    )
    ExtractionParameters: str
    Frequency: DoubleType
    MSSpectrumSearchResults: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.MSSpectrumSearchResultsType
    )
    PeakDeletions: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakDeletionType
    ]
    StartIndex: IntegerType
    TechSpec: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SignalTechSpecType
    TimeShift: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    TraceID: str
    Type: str
    UserGenerated: bool
    XAxisScalingFactor: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )
    YAxisScalingFactor: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    )

class SimpleCustomFieldType:  # Class
    def __init__(self) -> None: ...

    Description: str
    Mandatory: bool
    MandatorySpecified: bool
    Name: str
    Value: str

class SimpleCustomFieldsType:  # Class
    def __init__(self) -> None: ...

    CustomField01: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldType
    )
    CustomField02: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldType
    )
    CustomField03: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldType
    )
    CustomField04: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldType
    )
    CustomField05: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldType
    )
    CustomField06: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldType
    )
    CustomField07: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldType
    )
    CustomField08: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldType
    )
    CustomField09: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldType
    )
    CustomField10: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SimpleCustomFieldType
    )

class SpecificSeparationMediumType:  # Class
    def __init__(self) -> None: ...

    Item: Any

class SpectraConfirmResultEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Confirmed: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectraConfirmResultEnum
    ) = ...  # static # readonly
    NotConfirmed: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectraConfirmResultEnum
    ) = ...  # static # readonly
    Unknown: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectraConfirmResultEnum
    ) = ...  # static # readonly

class SpectrumExprTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Apex: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum = (
        ...
    )  # static # readonly
    Downslope1: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    Downslope2: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    ForceBaseline: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    PeakAll: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    PeakBegin: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    PeakEnd: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    Periodic: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    SmallPeakTop: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    Unknown: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    Upslope1: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    Upslope2: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly
    Valley: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    ) = ...  # static # readonly

class SpectrumRefType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class SpectrumType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericNonVersionedObjectType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.GenericNonVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISpectrumType,
):  # Class
    def __init__(self) -> None: ...

    ExprType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumExprTypeEnum
    RetentionTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Signal_ID: Any
    Type: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumTypeEnum
    WaveLengths: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    ]

class SpectrumTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Emission: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumTypeEnum = (
        ...
    )  # static # readonly
    Excitation: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumTypeEnum
    ) = ...  # static # readonly
    Mass: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumTypeEnum = (
        ...
    )  # static # readonly
    UVVis: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumTypeEnum = (
        ...
    )  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumTypeEnum
    ) = ...  # static # readonly
    Unspecified: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SpectrumTypeEnum
    ) = ...  # static # readonly

class StandardCompoundAmountType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IStandardCompoundAmountType,
    IObjectRoot,
):  # Class
    def __init__(self) -> None: ...

    Amount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Identifier: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.StandardCompoundIdentifierType
    )

class StandardCompoundIdentifierType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IStandardCompoundIdentifierType
):  # Class
    def __init__(self) -> None: ...

    Item: Any

class TimePeriodType(
    ValueBaseType, Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ITimePeriodType
):  # Class
    def __init__(self) -> None: ...

    Unit: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimeUnitEnum
    UnitSpecified: bool
    Val: float

class TimeRangeType:  # Class
    def __init__(self) -> None: ...

    BeginTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    EndTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType

class TimeUnitEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Min: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimeUnitEnum = (
        ...
    )  # static # readonly
    Ms: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimeUnitEnum = (
        ...
    )  # static # readonly
    S: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimeUnitEnum = (
        ...
    )  # static # readonly

class UVLibrarySpectrumType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    CompoundName: str
    LibraryName: str
    ReferenceSubtractionMode: str
    RetentionTime: DoubleType
    Source: str
    SpectrumIdentifier: str

class UVSpectrumLibraryHitType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IUVSpectrumLibraryHitType
):  # Class
    def __init__(self) -> None: ...

    AboveThreshold: bool
    LibraryCompoundName: str
    LibraryID: IntegerType
    MatchNumber: IntegerType
    ReferenceSubtractionMode: str
    RetentionTime: DoubleType
    Similarity: DoubleType

class UVSpectrumLibraryType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IUVSpectrumLibraryType
):  # Class
    def __init__(self) -> None: ...

    LibraryName: str
    LibraryPath: str
    UVSpectrumHits: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.UVSpectrumLibraryHitType
    ]

class UVSpectrumSearchResultsType(
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IUVSpectrumSearchResultsType
):  # Class
    def __init__(self) -> None: ...

    UVSpectrumLibraries: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.UVSpectrumLibraryType
    ]

class UserRefType(
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VersionedObjectBaseType,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

class UserType(
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    IObjectRoot,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INamedGenericVersionedObjectType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IGenericVersionedObjectType,
):  # Class
    def __init__(self) -> None: ...

class VectoreItemTypeEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Float32: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VectoreItemTypeEnum
    ) = ...  # static # readonly
    Float64: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VectoreItemTypeEnum
    ) = ...  # static # readonly
    Int32: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VectoreItemTypeEnum = (
        ...
    )  # static # readonly
    Int64: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VectoreItemTypeEnum = (
        ...
    )  # static # readonly
    Item: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.VectoreItemTypeEnum = (
        ...
    )  # static # readonly

class VersionedExternalObjectBaseType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
    ObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedExternalObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    Path: str
    Ver: int

class VersionedObjectBaseType(
    ObjectBaseType,
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    Id: str
    Ver: int

class VirtualPeakRefType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
):  # Class
    def __init__(self) -> None: ...

    CalibPeakRole: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum
    )
    CalibPeakRoleSpecified: bool

class VirtualPeakType(
    IObjectRoot,
    IObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.NonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonVersionedObjectBaseType,
    Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IVirtualPeakType,
):  # Class
    def __init__(self) -> None: ...

    Area: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    AreaPercent: DoubleType
    Baseline: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    BaselineEnd: DoubleType
    BaselineStart: DoubleType
    BeginTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    EndTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Height: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    HeightPercent: DoubleType
    LevelEnd: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    LevelStart: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Peak_IDs: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakRefType
    ]
    RetentionTime: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.TimePeriodType
    Symmetry: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType
    Type: str
    WidthBase: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.DoubleUnitType

class XmlAnyType:  # Class
    def __init__(self) -> None: ...

    Anys: System.Collections.Generic.List[System.Xml.XmlElement]
