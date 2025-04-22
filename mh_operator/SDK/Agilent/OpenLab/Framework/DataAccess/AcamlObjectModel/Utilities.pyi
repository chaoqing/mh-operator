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

# Discovered Generic TypeVars:
T = TypeVar("T")
from . import (
    IACAML,
    AgilentApplicationEnum,
    BackgroundSubtractionExternalSignalType,
    BackgroundSubtractionReferenceSignalType,
    BackgroundSubtractionSignalType,
    BinaryDataItemType,
    CalibrationCurveType,
    CompoundTypeEnum,
    CorrectionFactorType,
    DocInfoType,
    IBackgroundSubtractionExternalSignalType,
    InjectionAcquisitionParamType,
    InjectionCompoundType,
    InjectionDataAnalysisParamType,
    InjectionMeasDataType,
    InjectionResultType,
    InjectionSeparationMediumType,
    InjectionSignalResultType,
    InstrumentModuleType,
    InstrumentType,
    LinkMode,
    MethodType,
    PeakRefType,
    PeakType,
    SampleAcquisitionParamType,
    SampleContextAcquisitionParamType,
    SampleContextDataAnalysisParamType,
    SampleContextIdentParamType,
    SampleContextTypeEnum,
    SampleDataAnalysisParamType,
    SampleIdentParamType,
    SampleMeasDataContextType,
    SampleMeasDataType,
    SampleSetupContextType,
    SampleSetupType,
    SampleTypeEnum,
    SeparationMediumPositionEnum,
    SignalType,
    StandardCompoundAmountType,
)

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.Utilities

class AcamlFactory:  # Class
    @overload
    @staticmethod
    def AddSampleMeasData(acaml: IACAML) -> SampleMeasDataType: ...
    @overload
    @staticmethod
    def AddSampleMeasData(
        acaml: IACAML,
        sampleMeasDataId: System.Guid,
        sampleSetupLinkMode: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.Utilities.ObjectLinkMode = ...,
        injectionMeasDataIds: Iterable[System.Guid] = ...,
    ) -> SampleMeasDataType: ...
    @staticmethod
    def CreateMultiSampleAcamlStructure(
        sampleTypes: Iterable[SampleTypeEnum],
    ) -> IACAML: ...
    @overload
    @staticmethod
    def AddMethod(acaml: IACAML) -> MethodType: ...
    @overload
    @staticmethod
    def AddMethod(
        acaml: IACAML, name: str, description: str = ..., methodId: System.Guid = ...
    ) -> MethodType: ...
    @overload
    @staticmethod
    def AddInjectionResult(acaml: IACAML) -> InjectionResultType: ...
    @overload
    @staticmethod
    def AddInjectionResult(
        acaml: IACAML,
        injectionResultId: System.Guid,
        injectionMeasDataLinkMode: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.Utilities.ObjectLinkMode = ...,
    ) -> InjectionResultType: ...
    @overload
    @staticmethod
    def AddInjectionMeasData(acaml: IACAML) -> InjectionMeasDataType: ...
    @overload
    @staticmethod
    def AddInjectionMeasData(
        acaml: IACAML, injectionMeasDataId: System.Guid
    ) -> InjectionMeasDataType: ...
    @staticmethod
    def CreateInjectionTuple(
        acaml: IACAML,
    ) -> System.Tuple[InjectionMeasDataType, InjectionResultType]: ...
    @staticmethod
    def CreateMiAcamlStructure(
        numberOfInjections: int, createResources: bool = ...
    ) -> IACAML: ...
    @staticmethod
    def CreateSiAcamlWithPeaksAndInjectionCompounds(
        peakRefs: Iterable[PeakRefType],
        peakRefCalibCurveLinkMode: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.Utilities.ObjectLinkMode = ...,
    ) -> IACAML: ...
    @overload
    @staticmethod
    def AddSignal(acaml: IACAML, injectionMeasDataId: System.Guid) -> SignalType: ...
    @overload
    @staticmethod
    def AddSignal(
        acaml: IACAML,
        injectionMeasDataId: System.Guid,
        signalId: System.Guid,
        type: str = ...,
        name: str = ...,
        description: str = ...,
        pathToFile: str = ...,
        binaryDataItem: BinaryDataItemType = ...,
    ) -> SignalType: ...
    @staticmethod
    def CreateSampleTuple(
        acaml: IACAML,
        injectionTuples: Iterable[
            System.Tuple[InjectionMeasDataType, InjectionResultType]
        ],
    ) -> System.Tuple[SampleSetupType, SampleMeasDataType]: ...
    @overload
    @staticmethod
    def AddSampleContextMeasData(acaml: IACAML) -> SampleMeasDataContextType: ...
    @overload
    @staticmethod
    def AddSampleContextMeasData(
        acaml: IACAML,
        sampleContextMeasDataId: System.Guid,
        sampleContextSetupLinkMode: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.Utilities.ObjectLinkMode = ...,
        sampleMeasDataIds: Iterable[System.Guid] = ...,
    ) -> SampleMeasDataContextType: ...
    @overload
    @staticmethod
    def AddInjectionCompound(
        acaml: IACAML,
        injectionResultId: System.Guid,
        peakRef: PeakRefType,
        injectionCompoundId: System.Guid = ...,
        compoundName: str = ...,
        compoundType: CompoundTypeEnum = ...,
    ) -> InjectionCompoundType: ...
    @overload
    @staticmethod
    def AddInjectionCompound(
        acaml: IACAML,
        injectionResultId: System.Guid,
        injectionCompoundId: System.Guid = ...,
        compoundName: str = ...,
        compoundType: CompoundTypeEnum = ...,
    ) -> InjectionCompoundType: ...
    @staticmethod
    def AddInstrument(
        acaml: IACAML, name: str = ..., instrumentId: System.Guid = ...
    ) -> InstrumentType: ...
    @overload
    @staticmethod
    def AddSampleSetup(acaml: IACAML) -> SampleSetupType: ...
    @overload
    @staticmethod
    def AddSampleSetup(
        acaml: IACAML, sampleSetupId: System.Guid
    ) -> SampleSetupType: ...
    @staticmethod
    def CreateSiAcamlWithSignal(
        signalName: str = ..., binaryDataItem: BinaryDataItemType = ...
    ) -> IACAML: ...
    @overload
    @staticmethod
    def AddSampleContextSetup(acaml: IACAML) -> SampleSetupContextType: ...
    @overload
    @staticmethod
    def AddSampleContextSetup(
        acaml: IACAML,
        sampleContextSetupId: System.Guid,
        sampleSetupIds: Iterable[System.Guid] = ...,
    ) -> SampleSetupContextType: ...
    @staticmethod
    def CreateSiAcamlWithPeaks(
        numberOfPeaks: int, defaultRetentionTime: float = ..., signalName: str = ...
    ) -> IACAML: ...
    @staticmethod
    def CreateSiAcamlStructure(createResources: bool = ...) -> IACAML: ...
    @staticmethod
    def CreateBaseAcamlStructure(createResources: bool) -> IACAML: ...
    @staticmethod
    def CreateSampleContextTuple(
        acaml: IACAML,
        sampleTuples: Iterable[System.Tuple[SampleSetupType, SampleMeasDataType]],
    ) -> System.Tuple[SampleSetupContextType, SampleMeasDataContextType]: ...
    @staticmethod
    def AddInjectionSignalResult(
        acaml: IACAML,
        injectionResultId: System.Guid,
        injectionMeasDataId: System.Guid,
        injectionSignalResultId: System.Guid = ...,
        signalLinkMode: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.Utilities.ObjectLinkMode = ...,
        peakList: Iterable[PeakType] = ...,
    ) -> InjectionSignalResultType: ...
    @staticmethod
    def AddPeak(
        acaml: IACAML, injectionSignalResultId: System.Guid, peakId: System.Guid = ...
    ) -> PeakType: ...
    @overload
    @staticmethod
    def AddCalibrationCurve(acaml: IACAML) -> CalibrationCurveType: ...
    @overload
    @staticmethod
    def AddCalibrationCurve(
        acaml: IACAML, calibrationCurveId: System.Guid
    ) -> CalibrationCurveType: ...

class AcamlNamespaceMigrationReader(
    System.IDisposable,
    System.Xml.IXmlNamespaceResolver,
    System.Xml.XmlTextReader,
    System.Xml.IXmlLineInfo,
):  # Class
    def __init__(self, stream: System.IO.Stream) -> None: ...

    NamespaceURI: str  # readonly

class ObjectFactory:  # Class
    @staticmethod
    def CreateInstrumentType(
        name: str, instrumentId: System.Guid = ...
    ) -> InstrumentType: ...
    @staticmethod
    def CreateCalibrationLevelType(
        amount: float, level: int
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationLevelType: ...
    @staticmethod
    def CreateDocInfoType(
        appType: AgilentApplicationEnum,
        appVersion: str,
        userName: str,
        clientName: str,
        description: str = ...,
    ) -> DocInfoType: ...
    @staticmethod
    def CreateInjectionResultType(
        injectionResultId: System.Guid,
        injectionMeasDataId: System.Guid = ...,
        injectionDataAnalysisParam: InjectionDataAnalysisParamType = ...,
    ) -> InjectionResultType: ...
    @staticmethod
    def CreateParamType(methodId: System.Guid = ...) -> T: ...
    @staticmethod
    def CreateSampleMeasDataType(
        sampleMeasDataId: System.Guid,
        sampleSetupId: System.Guid = ...,
        injectionMeasDataIds: Iterable[System.Guid] = ...,
        sampleIdentParam: SampleIdentParamType = ...,
        sampleAcquisitionParam: SampleAcquisitionParamType = ...,
    ) -> SampleMeasDataType: ...
    @staticmethod
    def CreateInjectionMeasDataType(
        injectionMeasDataId: System.Guid,
        injectionAcquisitionParam: InjectionAcquisitionParamType = ...,
    ) -> InjectionMeasDataType: ...
    @staticmethod
    def CreateMethodType(
        name: str,
        description: str,
        dataFileReferencePath: str = ...,
        binaryDataItemName: str = ...,
        objectInfo: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectInfoType = ...,
    ) -> MethodType: ...
    @staticmethod
    def CreateInjectionSignalResult(
        injectionSignaResultId: System.Guid = ...,
        signalId: System.Guid = ...,
        peakList: Iterable[PeakType] = ...,
    ) -> InjectionSignalResultType: ...
    @staticmethod
    def CreateCalibrationHistoryType(
        sampleName: str, amount: float
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.CalibrationHistoryType: ...
    @staticmethod
    def CreateCalibrationCurveType(
        calibCurveId: System.Guid = ...,
    ) -> CalibrationCurveType: ...
    @staticmethod
    def CreateInjectionCompoundType(
        injectionCompoundId: System.Guid = ...,
        compoundName: str = ...,
        compoundType: CompoundTypeEnum = ...,
    ) -> InjectionCompoundType: ...
    @overload
    @staticmethod
    def CreateSignalType(
        name: str,
        description: str,
        type: str,
        pathToFile: str,
        signalId: System.Guid = ...,
        binaryDataItem: BinaryDataItemType = ...,
    ) -> SignalType: ...
    @overload
    @staticmethod
    def CreateSignalType(
        detectorName: str,
        detectorInstance: str,
        channelName: str,
        description: str,
        type: str,
        pathToFile: str,
        generateSignalNameFunction: System.Func[str, str, str, str],
        signalId: System.Guid = ...,
        binaryDataItem: BinaryDataItemType = ...,
    ) -> SignalType: ...
    @overload
    @staticmethod
    def CreateInstrumentModuleType(
        name: str, type: str, partNo: str, serialNo: str, firmwareRevision: str
    ) -> InstrumentModuleType: ...
    @overload
    @staticmethod
    def CreateInstrumentModuleType(
        name: str,
        type: str,
        partNo: str,
        serialNo: str,
        firmwareRevision: str,
        driverVersion: str,
        connectionInfo: str,
        additionalInformation: str,
    ) -> InstrumentModuleType: ...
    @staticmethod
    def CreateSampleSetupType(
        sampleSetupId: System.Guid,
        sampleIdentParam: SampleIdentParamType = ...,
        sampleAcquisitionParam: SampleAcquisitionParamType = ...,
        sampleDataAnalysisParam: SampleDataAnalysisParamType = ...,
    ) -> SampleSetupType: ...
    @overload
    @staticmethod
    def CreateBinaryDataItem(
        dataItemBaseName: str,
        usedataItemBaseNameAsfileReference: bool = ...,
        path: str = ...,
    ) -> BinaryDataItemType: ...
    @overload
    @staticmethod
    def CreateBinaryDataItem(
        dataItemBaseName: str,
        useDataItemBaseNameAsFileReference: bool = ...,
        path: str = ...,
        originalFilePath: str = ...,
    ) -> BinaryDataItemType: ...
    @overload
    @staticmethod
    def CreateBinaryDataItem(
        dataItemBaseName: str, path: str = ...
    ) -> BinaryDataItemType: ...
    @overload
    @staticmethod
    def CreateBinaryDataItem(
        dataItemBaseName: str, path: str = ..., originalFilePath: str = ...
    ) -> BinaryDataItemType: ...
    @overload
    @staticmethod
    def CreateStandardCompoundAmountType(
        amount: float,
    ) -> StandardCompoundAmountType: ...
    @overload
    @staticmethod
    def CreateStandardCompoundAmountType(
        amount: float, compoundName: str
    ) -> StandardCompoundAmountType: ...
    @overload
    @staticmethod
    def CreateStandardCompoundAmountType(
        amount: float, number: int
    ) -> StandardCompoundAmountType: ...
    @staticmethod
    def CreateCorrectionFactorList() -> Iterable[CorrectionFactorType]: ...
    @staticmethod
    def CreateSampleIdentParamType(
        name: str, description: str
    ) -> SampleIdentParamType: ...
    @staticmethod
    def CreatePeakType(
        peakId: System.Guid = ..., retentionTime: float = ...
    ) -> PeakType: ...
    @staticmethod
    def CreateSampleMeasDataContextType(
        sampleContextMeasDataId: System.Guid,
        sampleContextSetupId: System.Guid = ...,
        sampleMeasDataIds: Iterable[System.Guid] = ...,
        sampleContextIdentParam: SampleContextIdentParamType = ...,
        sampleContextAcquisitionParam: SampleContextAcquisitionParamType = ...,
    ) -> SampleMeasDataContextType: ...
    @staticmethod
    def CreateInjectionSeparationMediumType(
        separationMediumId: System.Guid,
        autoDetect: bool = ...,
        position: SeparationMediumPositionEnum = ...,
        injectionCount: int = ...,
    ) -> InjectionSeparationMediumType: ...
    @staticmethod
    def CreatePeakRefType(
        peakId: System.Guid = ..., calibCurveId: System.Guid = ...
    ) -> PeakRefType: ...
    @overload
    @staticmethod
    def CreateBackgroundSubtractionReferenceSignalType(
        injectionId: System.Guid,
    ) -> BackgroundSubtractionReferenceSignalType: ...
    @overload
    @staticmethod
    def CreateBackgroundSubtractionReferenceSignalType(
        externalReferenceDescription: str,
    ) -> BackgroundSubtractionReferenceSignalType: ...
    @staticmethod
    def CreateSampleSetupContextType(
        sampleContextSetupId: System.Guid,
        sampleSetupIds: Iterable[System.Guid] = ...,
        sampleContextIdentParam: SampleContextIdentParamType = ...,
        sampleContextAcquisitionParam: SampleContextAcquisitionParamType = ...,
        sampleContextDataAnalysisParam: SampleContextDataAnalysisParamType = ...,
    ) -> SampleSetupContextType: ...
    @staticmethod
    def CreateBackgroundSubtractionExternalSignalType(
        fileName: str, traceId: str
    ) -> BackgroundSubtractionExternalSignalType: ...
    @staticmethod
    def CreateObjectInfo() -> (
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ObjectInfoType
    ): ...
    @staticmethod
    def CreateSampleContextIdentParamType(
        name: str, sampleContextType: SampleContextTypeEnum
    ) -> SampleContextIdentParamType: ...
    @overload
    @staticmethod
    def CreateBackgroundSubtractionSignalType(
        signalId: System.Guid,
    ) -> BackgroundSubtractionSignalType: ...
    @overload
    @staticmethod
    def CreateBackgroundSubtractionSignalType(
        externalSignal: IBackgroundSubtractionExternalSignalType,
    ) -> BackgroundSubtractionSignalType: ...

class ObjectLinkMode:  # Struct
    def __init__(self, linkMode: LinkMode) -> None: ...

    ExistingSource: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IObjectBaseType
    ExistingTargets: Iterable[System.Guid]
    LinkMode: LinkMode  # readonly
