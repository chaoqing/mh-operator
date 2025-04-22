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
TProviderInterface = TypeVar("TProviderInterface")

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces

class AcamlLoadingErrorLog(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlLoadingErrorLog
):  # Class
    def __init__(self) -> None: ...

    FailedAcamls: Dict[str, str]  # readonly

    def AddState(self, storagePath: str, message: str) -> None: ...

class AcamlLoadingState(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AlreadyLoaded: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlLoadingState
    ) = ...  # static # readonly
    Failed: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlLoadingState
    ) = ...  # static # readonly
    NoError: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlLoadingState
    ) = ...  # static # readonly

class AcamlParam(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Acquisition: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlParam
    ) = ...  # static # readonly
    DataAnalysis: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlParam
    ) = ...  # static # readonly
    Identity: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlParam
    ) = ...  # static # readonly

class AcamlSection(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    All: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlSection
    ) = ...  # static # readonly
    MeasData: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlSection
    ) = ...  # static # readonly
    Result: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlSection
    ) = ...  # static # readonly
    Setup: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlSection
    ) = ...  # static # readonly

class DataAlreadyLoadedException(
    System.Runtime.InteropServices._Exception,
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.DataLoadingException,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class DataChangeLevel(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Compound: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.DataChangeLevel
    ) = ...  # static # readonly
    Global: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.DataChangeLevel
    ) = ...  # static # readonly
    Injection: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.DataChangeLevel
    ) = ...  # static # readonly
    Method: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.DataChangeLevel
    ) = ...  # static # readonly
    Peak: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.DataChangeLevel
    ) = ...  # static # readonly
    ResultSet: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.DataChangeLevel
    ) = ...  # static # readonly
    Sample: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.DataChangeLevel
    ) = ...  # static # readonly
    Signal: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.DataChangeLevel
    ) = ...  # static # readonly

class DataChecksumException(
    System.Runtime.InteropServices._Exception,
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.DataLoadingException,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class DataLoadingException(
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

class DataUpdateException(
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

class IAcamlBusinessRule(object):  # Interface
    Messages: Iterable[str]  # readonly
    OrderNumber: int  # readonly
    ThrowIfFailed: bool  # readonly

    def Apply(
        self,
        storageFileAccess: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageFileAccess,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...

class IAcamlFix(object):  # Interface
    OrderNumber: int  # readonly

    def NeedsFix(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
    def Apply(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...

class IAcamlLoadingErrorLog(object):  # Interface
    FailedAcamls: Dict[str, str]  # readonly

class IAcamlReader(System.IDisposable):  # Interface
    DocId: System.Guid  # readonly
    IsPrefetchLockEnabled: bool  # readonly

    def MergeInjectionAcamls(
        self, injectionMeasDataIds: Iterable[System.Guid] = ...
    ) -> None: ...
    def EndInjectionAcamlPrefetching(self) -> None: ...
    def LoadSequenceAcaml(self, acamlStream: System.IO.Stream) -> None: ...
    def GetFinalizedAcaml(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        documentStoragePath: str,
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML: ...
    def PrefetchInjectionAcaml(
        self,
        reference: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IInjectionAcamlReference,
        acamlStream: System.IO.Stream,
    ) -> None: ...
    def CreatePrefetchLock(self) -> System.IDisposable: ...
    def GetInjectionReferences(
        self,
    ) -> List[
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IInjectionAcamlReference
    ]: ...
    def BeginInjectionAcamlPrefetching(self) -> None: ...

class IAcamlReaderWriter(object):  # Interface
    EnforceAcamlBusinessRules: bool
    PrepareForDataModification: bool
    ValidateChecksumOnLoad: bool
    ValidateChecksumOnSave: bool
    ValidateSchemaOnLoad: bool
    ValidateSchemaOnSave: bool

    def CreateReader(
        self,
    ) -> (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlReader
    ): ...
    @overload
    def LoadAcamlMetadataAsync(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        path: str,
        cancellationToken: System.Threading.CancellationToken,
        createIfMissing: bool = ...,
    ) -> System.Threading.Tasks.Task[
        Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData
        ]
    ]: ...
    @overload
    def LoadAcamlMetadataAsync(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        path: str,
        version: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
        cancellationToken: System.Threading.CancellationToken,
        createIfMissing: bool = ...,
    ) -> System.Threading.Tasks.Task[
        Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData
        ]
    ]: ...
    @overload
    def LoadAcamlMetadataAsync(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        paths: Iterable[str],
        cancellationToken: System.Threading.CancellationToken,
        createIfMissing: bool = ...,
    ) -> System.Threading.Tasks.Task[
        Dict[
            str,
            Iterable[
                Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData
            ],
        ]
    ]: ...
    def CreateWriter(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
        fileName: str,
        saveOnlyChangedData: bool = ...,
        updateMetadata: bool = ...,
    ) -> (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlWriter
    ): ...
    @overload
    def LoadAcamlMetadata(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        path: str,
        createIfMissing: bool = ...,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData
    ]: ...
    @overload
    def LoadAcamlMetadata(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        path: str,
        version: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
        createIfMissing: bool = ...,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData
    ]: ...
    @overload
    def LoadAcamlMetadata(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        paths: Iterable[str],
        createIfMissing: bool = ...,
    ) -> Dict[
        str,
        Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData
        ],
    ]: ...

class IAcamlSignalLoader(object):  # Interface
    def ExtractChromatograms(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        docId: System.Guid,
        spectra: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
        signalMetaDataAndParameters: Dict[
            Agilent.OpenLab.Framework.DataAccess.CoreTypes.IExtractionParameters,
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
        ],
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.CoreType.IExtractedSignalDataContainer[
            Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
        ]
    ]: ...
    def LoadInstrumentTrace(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        docId: System.Guid,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData: ...
    def LoadReferenceChromatogram(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        docId: System.Guid,
        path: str,
        traceId: str,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData: ...
    def GetSignalInformation(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        docId: System.Guid,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISignalInformation: ...
    def LoadChromatogram(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        docId: System.Guid,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData: ...
    def ReadGenericAnalyticalResultData(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        genericAnalyticalResultDataInfo: Agilent.OpenLab.Framework.DataAccess.CoreTypes.IGenericAnalyticalResultDataInfo,
    ) -> List[int]: ...
    def ReadGenericAnalyticalResultDataInfo(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        docId: System.Guid,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionMeasDataType,
    ) -> Sequence[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IGenericAnalyticalResultDataInfo
    ]: ...
    def ExtractChromatogram(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        docId: System.Guid,
        spectra: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
        metadataOfSignalToExtract: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
        chromatogramExtractionParameters: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ChromatogramExtractionParameters,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData: ...
    def TriggerSignalPrefetching(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        injectionOrder: Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.AcamlInjectionId
        ],
        currentIndex: int,
    ) -> None: ...
    def UnloadSignalFromCache(
        self,
        docId: System.Guid,
        signalType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    ) -> None: ...
    def ExtractSpectra(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        docId: System.Guid,
        spectra: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
        signalMetaDataAndParameters: Dict[
            Agilent.OpenLab.Framework.DataAccess.CoreTypes.IExtractionParameters,
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
        ],
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.CoreType.IExtractedSignalDataContainer[
            Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData
        ]
    ]: ...
    def LoadSpectra(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        docId: System.Guid,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectraData: ...
    def ExtractSpectrum(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        docId: System.Guid,
        spectra: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
        metadataOfSignalToExtract: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType,
        spectrumExtractionParameters: Agilent.OpenLab.Framework.DataAccess.CoreTypes.SpectrumExtractionParameters,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData: ...

class IAcamlStreamProxy(object):  # Interface
    FileBasedStream: System.IO.Stream  # readonly
    TempFilePath: str  # readonly

    @overload
    def Read(
        self,
        fileAccess: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageFileAccess,
        path: str,
    ) -> bool: ...
    @overload
    def Read(self, stream: System.IO.Stream) -> bool: ...
    def Dispose(self) -> None: ...

class IAcamlWriter(System.IDisposable):  # Interface
    InjectionAcamlsParts: Dict[
        System.Guid,
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IInjectionAcamlPart,
    ]  # readonly
    SequenceAcamlStream: System.IO.Stream  # readonly

    def SetSequenceAcamlSaved(self) -> None: ...
    def ClearChangesOnSaved(self) -> None: ...

class IDataProviderFactory(object):  # Interface
    @overload
    def GetProviderSet(
        self, docId: System.Guid
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IProvider
    ]: ...
    @overload
    def GetProviderSet(
        self, acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IProvider
    ]: ...
    @overload
    def GetProvider(self, docId: System.Guid) -> TProviderInterface: ...
    @overload
    def GetProvider(
        self, acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML
    ) -> TProviderInterface: ...
    def IsRegistered(
        self, acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML
    ) -> bool: ...
    def RegisterAcaml(
        self,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
        prepareForWriteAccess: bool,
    ) -> bool: ...

class IGlobalDataProvider(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IProvider
):  # Interface
    AgilentApplication: Optional[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentApplicationEnum
    ]
    DocumentInfo: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDocInfoType
    )  # readonly
    InjectionsMetadata: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData
    ]  # readonly
    Methods: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType
    ]  # readonly

    @overload
    def AddMethodDefinition(
        self,
        methodDefinition: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType,
    ) -> None: ...
    @overload
    def AddMethodDefinition(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        description: str,
        lastModifiedDate: System.DateTime,
        dataFileReferencePath: str,
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType: ...
    def RemoveCustomCalculationResult(
        self,
        customCalcEmbeddedResult: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcEmbeddedResultType,
    ) -> None: ...
    def RemoveUnusedMethodDefinitions(self) -> Iterable[System.Guid]: ...
    def RemoveUnusedCustomCalculationResults(self) -> None: ...
    def UpdateMethodDefinition(
        self,
        methodDefinition: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType,
    ) -> None: ...
    def RefreshInjectionsMetadata(
        self, injectionIds: Iterable[System.Guid]
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData
    ]: ...
    def RemoveCustomCalculationResults(self, parentId: System.Guid) -> None: ...
    @overload
    def GetMethodDefinition(
        self, methodId: System.Guid
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType: ...
    @overload
    def GetMethodDefinition(
        self,
        nonIdentParamBase: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INonIdentParamBaseType,
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType: ...
    @overload
    def GetMethodDefinition(
        self, dataFileReferencePath: str
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType: ...
    def ClearMethodDefinitions(self) -> None: ...
    def GetInjectionMetadata(
        self, injectionId: System.Guid
    ) -> (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData
    ): ...
    def PerformExactFulltextSearch(
        self, keywords: List[str]
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.AcamlInjectionId
    ]: ...
    def PerformFuzzyFulltextSearch(
        self, keywords: List[str]
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.AcamlInjectionId
    ]: ...
    def AddCustomCalculationResult(
        self,
        customCalcEmbeddedResultType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICustomCalcEmbeddedResultType,
    ) -> None: ...
    def ClearCustomCalculationResults(self) -> None: ...
    def RemoveMethodDefinition(
        self,
        methodDefinition: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType,
    ) -> None: ...
    def SetNewDocumentId(self) -> None: ...
    def ApplyMetadata(
        self,
        injectionMetadata: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.IInjectionMetaData,
    ) -> None: ...

class IInjectionAcamlPart(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IInjectionAcamlReference
):  # Interface
    InjectionAcamlStream: System.IO.Stream  # readonly

    def SetSaved(self) -> None: ...

class IInjectionAcamlReference(object):  # Interface
    InjectionFileName: str  # readonly
    InjectionMeasDataId: System.Guid  # readonly

class IInjectionsProvider(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IProvider
):  # Interface
    Injections: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer
    ]  # readonly
    def __getitem__(
        self, injectionId: System.Guid
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer: ...
    MeasData: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionMeasDataType
    ]  # readonly
    Peaks: Dict[
        System.Guid, Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType
    ]  # readonly
    Results: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionResultType
    ]  # readonly

    def AddCalibrationStandardAmount(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        istdAmount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IStandardCompoundAmountType,
    ) -> None: ...
    def LinkSamplePurityToSignal(
        self,
        samplePurity: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplePurityContainer,
        signalId: System.Guid,
    ) -> None: ...
    @overload
    def GetIdentifiedPeaks(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        injectionCompound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
        doLookupCalibCurves: bool,
        calibPeakRoles: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum = ...,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IIdentifiedPeakAggregation
    ]: ...
    @overload
    def GetIdentifiedPeaks(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        injectionCompound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
        signalFilter: System.Predicate[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType
        ],
        doLookupCalibCurves: bool,
        calibPeakRoles: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum = ...,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IIdentifiedPeakAggregation
    ]: ...
    def UnlinkInjectionCompoundFromCalibrationCurve(
        self,
        injectionCompound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
    ) -> None: ...
    def LinkSamplePurityToPeak(
        self,
        samplePurity: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplePurityContainer,
        peakId: System.Guid,
    ) -> None: ...
    def GetInjection(
        self, injectionMeasDataId: System.Guid
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer: ...
    def GetInjectionCompounds(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer = ...,
        filterPredicate: System.Predicate[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType
        ] = ...,
        ignoreUnknowns: bool = ...,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType
    ]: ...
    def RemoveInjectionCompound(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        injectionCompound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
    ) -> None: ...
    def GetCalibrationCurvesByInjectionCompound(
        self,
        injectionCompound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType: ...
    def AddRunType(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        runType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IRunTypeAndReplicationType,
    ) -> None: ...
    def UnlinkAllSeparationMediaFromInjection(
        self,
        injectionContainer: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def UnlinkSamplePurityFromSignal(
        self,
        samplePurity: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplePurityContainer,
    ) -> None: ...
    def AddMultipliers(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        multipliers: Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICorrectionFactorType
        ],
    ) -> None: ...
    def UnlinkAcqMethodDefinition(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def AddInternalStandardAmount(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        istdAmount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IStandardCompoundAmountType,
    ) -> None: ...
    def LinkAcqMethodDefinition(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        methodDefinition: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType,
    ) -> None: ...
    def AddOverriddenMethodParameters(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        methodParameter: Iterable[
            Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodParameterType
        ],
    ) -> None: ...
    def GetInjectionCompoundsByPeak(
        self,
        peakId: System.Guid,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        calibPeakRoles: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum = ...,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType
    ]: ...
    def ClearDilutionFactors(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def CreateAndLinkDaMethodDefinition(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        methodPath: str,
        description: str,
        lastModifiedDate: System.DateTime,
    ) -> None: ...
    @overload
    def GetParentInjectionOfSignal(
        self, signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer: ...
    @overload
    def GetParentInjectionOfSignal(
        self, signalId: System.Guid
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer: ...
    def AddSamplePurityResult(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        samplePurity: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplePurityContainer,
    ) -> None: ...
    def UnlinkSamplePurityFromPeak(
        self,
        samplePurity: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplePurityContainer,
    ) -> None: ...
    def GetParentSample(
        self, injectionMeasDataId: System.Guid
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer: ...
    def ClearMultipliers(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def AddDilutionFactors(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        dilutionFactors: Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICorrectionFactorType
        ],
    ) -> None: ...
    def ClearOverriddenMethodParameters(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def ClearCalibrationStandardAmounts(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def GetPrimaryDataElementName(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> str: ...
    @overload
    def GetSignalsProvider(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.ISignalsProvider
    ): ...
    @overload
    def GetSignalsProvider(
        self, signalId: System.Guid
    ) -> (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.ISignalsProvider
    ): ...
    def GetCalibrationCurvesByPeak(
        self,
        peakId: System.Guid,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        calibPeakRoles: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CalibPeakRoleEnum = ...,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType
    ]: ...
    def UpdateInjectionCompound(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        injectionCompound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
    ) -> None: ...
    def AddInjectionCompound(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        injectionCompound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
    ) -> None: ...
    def GetOverriddenMethodParameters(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IMethodParameterType
    ]: ...
    def LinkDaMethodDefinition(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        methodDefinition: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IMethodType,
    ) -> None: ...
    def ClearInjectionCompounds(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def AddInjectionCompounds(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
        injectionCompounds: Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType
        ],
        clearExistingInjectionCompounds: bool = ...,
    ) -> None: ...
    @overload
    def UnlinkIdentifiedPeakFromCalibrationCurve(
        self,
        identifiedPeak: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IIdentifiedPeakAggregation,
    ) -> None: ...
    @overload
    def UnlinkIdentifiedPeakFromCalibrationCurve(
        self,
        peakRef: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakRefType,
    ) -> None: ...
    def ClearInternalStandardAmounts(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def GetPeaksAndCompoundsAtAGlance(
        self, injectionIds: Iterable[System.Guid]
    ) -> Dict[
        str,
        Dict[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.CustomObjects.AcamlInjectionId,
            System.Tuple[
                Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
                Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType,
                Dict[str, str],
            ],
        ],
    ]: ...
    def GetDilutionFactors(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICorrectionFactorType
    ]: ...
    def ClearRunTypes(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def GetMultipliers(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICorrectionFactorType
    ]: ...
    def GetRunTypes(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IRunTypeAndReplicationType
    ]: ...
    @overload
    def LinkCalibrationCurveToIdentifiedPeak(
        self,
        calibrationCurve: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
        identifiedPeak: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IIdentifiedPeakAggregation,
    ) -> None: ...
    @overload
    def LinkCalibrationCurveToIdentifiedPeak(
        self,
        calibrationCurve: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
        peakRef: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakRefType,
    ) -> None: ...
    def LinkCalibrationCurveToInjectionCompound(
        self,
        calibrationCurve: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
        injectionCompound: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionCompoundType,
    ) -> None: ...
    @overload
    def LinkSeparationMediumToInjection(
        self,
        separationMediumId: System.Guid,
        injectionContainer: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    @overload
    def LinkSeparationMediumToInjection(
        self,
        injectionSeparationMediumType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionSeparationMediumType,
        injectionContainer: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def UnlinkDaMethodDefinition(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def UnlinkSeparationMediumFromInjection(
        self,
        separationMediumId: System.Guid,
        injectionContainer: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> None: ...
    def GetInternalStandardAmounts(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IStandardCompoundAmountType
    ]: ...
    def GetCalibrationStandardAmounts(
        self,
        injection: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IStandardCompoundAmountType
    ]: ...

class IProvider(object):  # Interface
    CurrentUserName: str
    DocId: System.Guid  # readonly

class IProviderLookupCache(object):  # Interface
    DocId: System.Guid  # readonly

    def DirtyDictionaryCount(self) -> int: ...
    def Reset(self) -> None: ...
    def Clear(self) -> None: ...
    def HasDirtyDictionaries(self) -> bool: ...

class IResourcesProvider(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IProvider
):  # Interface
    CalibrationCurves: Iterable[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType
    ]  # readonly
    Instruments: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInstrumentType
    ]  # readonly
    Resources: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IResourcesType
    )  # readonly
    SeparationMedia: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISeparationMediumType
    ]  # readonly

    def AddCalibrationCurve(
        self,
        calibrationCurve: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
    ) -> None: ...
    def RemoveUnusedInstruments(self) -> Iterable[System.Guid]: ...
    def AddSeparationMedium(
        self,
        separationMedium: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISeparationMediumType,
    ) -> None: ...
    def GetCalibrationCurve(
        self, calibrationCurveId: System.Guid
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType: ...
    def RemoveInstrument(
        self,
        instrument: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInstrumentType,
    ) -> None: ...
    def UpdateCalibrationCurve(
        self,
        calibrationCurve: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
    ) -> None: ...
    def GetSeparationMedium(
        self, separationMediumId: System.Guid
    ) -> (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISeparationMediumType
    ): ...
    def RemoveCalibrationCurve(
        self,
        calibrationCurve: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
    ) -> None: ...
    def RemoveUnusedCalibrationCurves(self) -> Iterable[System.Guid]: ...
    def AddInstrument(
        self,
        instrument: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInstrumentType,
    ) -> None: ...
    def RemoveSeparationMedium(
        self,
        separationMedium: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISeparationMediumType,
    ) -> None: ...
    def RemoveUnusedSeparationMedia(self) -> Iterable[System.Guid]: ...

class ISampleContextProvider(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IProvider
):  # Interface
    ContentType: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.SampleContextTypeEnum
    )  # readonly
    Instruments: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInstrumentType
    ]  # readonly
    MeasData: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleMeasDataContextType
    ]  # readonly
    PackagingMode: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PackagingModeEnum
    )  # readonly
    SampleContext: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContextContainer
    )  # readonly
    Setups: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleSetupContextType
    ]  # readonly

    def UnlinkAllInstrumentsFromSampleContext(self) -> None: ...
    def UnlinkInstrumentFromSampleContext(self, instrumentId: System.Guid) -> None: ...
    def LinkInstrumentToSampleContext(
        self,
        instrumentId: System.Guid,
        acamlSection: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlSection,
    ) -> None: ...

class ISamplesProvider(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IProvider
):  # Interface
    def __getitem__(
        self, sampleId: System.Guid
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer: ...
    MeasData: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleMeasDataType
    ]  # readonly
    Samples: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer
    ]  # readonly
    Setups: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleSetupType
    ]  # readonly

    def AddCalibrationStandardAmount(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
        istdAmount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IStandardCompoundAmountType,
    ) -> None: ...
    def AddSamplePuritySetup(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
        samplePurity: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplePurityContainer,
    ) -> None: ...
    def UnlinkInstrument(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> None: ...
    def RemoveSamplePurity(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
        samplePurityId: System.Guid,
    ) -> None: ...
    def GetSample(
        self, sampleSetupId: System.Guid
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer: ...
    def AddRunType(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
        runType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IRunTypeAndReplicationType,
    ) -> None: ...
    def AddMultipliers(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
        multipliers: Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICorrectionFactorType
        ],
    ) -> None: ...
    def AddInternalStandardAmount(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
        istdAmount: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IStandardCompoundAmountType,
    ) -> None: ...
    def ClearDilutionFactors(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> None: ...
    def ClearMultipliers(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> None: ...
    def AddDilutionFactors(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
        dilutionFactors: Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICorrectionFactorType
        ],
    ) -> None: ...
    def ClearCalibrationStandardAmounts(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> None: ...
    def LinkInstrumentToSample(
        self,
        instrumentId: System.Guid,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
        acamlSection: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.AcamlSection,
    ) -> None: ...
    def GetInstrument(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInstrumentType: ...
    def GetInjections(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer
    ]: ...
    def ClearInternalStandardAmounts(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> None: ...
    def GetDilutionFactors(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICorrectionFactorType
    ]: ...
    def ClearRunTypes(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> None: ...
    def GetRunTypes(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IRunTypeAndReplicationType
    ]: ...
    def GetMultipliers(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ICorrectionFactorType
    ]: ...
    def GetSamplePurities(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplePurityContainer
    ]: ...
    def ClearSamplePurities(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> None: ...
    def GetInternalStandardAmounts(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IStandardCompoundAmountType
    ]: ...
    def GetCalibrationStandardAmounts(
        self,
        sample: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContainer,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IStandardCompoundAmountType
    ]: ...

class ISignalsProvider(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IProvider
):  # Interface
    ParentInjection: (
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionContainer
    )  # readonly
    Peaks: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType
    ]  # readonly
    SignalMeasData: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType
    ]  # readonly
    SignalResults: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInjectionSignalResultType
    ]  # readonly
    Signals: Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer
    ]  # readonly

    def AddNoisePeriods(
        self,
        noisePeriods: Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INoisePeriodType
        ],
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
    ) -> None: ...
    def ClearNoisePeriods(
        self,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
    ) -> None: ...
    def AddPeak(
        self,
        peak: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
    ) -> None: ...
    def UnlinkAllSignalsFromPeak(
        self, peak: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType
    ) -> None: ...
    def LinkSignalToPeak(
        self,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
        peak: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType,
    ) -> None: ...
    def ClearPeakDeletions(
        self,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
    ) -> None: ...
    def GetSignalIdsByType(
        self,
        typeFilters: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.SignalTypeFilters,
    ) -> Iterable[System.Guid]: ...
    def GetSignalsByType(
        self,
        signalTypeFilters: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.SignalTypeFilters = ...,
    ) -> Iterable[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer
    ]: ...
    def ClearSignals(self) -> None: ...
    def ClearPeaks(
        self,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
    ) -> None: ...
    @overload
    def GetSignal(
        self, signalId: System.Guid
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer: ...
    @overload
    def GetSignal(
        self, signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalType
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer: ...
    @overload
    def GetRawChromData(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        signalId: System.Guid,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData: ...
    @overload
    def GetRawChromData(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        signalName: str,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData: ...
    def AddNoisePeriod(
        self,
        noisePeriod: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.INoisePeriodType,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
    ) -> None: ...
    def AddPeaks(
        self,
        peaks: Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType
        ],
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
        clearExistingPeaks: bool = ...,
    ) -> None: ...
    @overload
    def GetSpectraData(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        signalId: System.Guid,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectraData: ...
    @overload
    def GetSpectraData(
        self,
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        signalName: str,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectraData: ...
    def UpdatePeak(
        self,
        peak: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
    ) -> None: ...
    def UnlinkSignalFromPeak(
        self,
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
        peak: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IPeakType,
    ) -> None: ...
    def AddPeakDeletions(
        self,
        peakDeletions: Iterable[
            Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.PeakDeletionType
        ],
        signal: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISignalContainer,
    ) -> None: ...

class SignalTypeFilters(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Chromatograms: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.SignalTypeFilters
    ) = ...  # static # readonly
    ExtractedChromatograms: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.SignalTypeFilters
    ) = ...  # static # readonly
    ExtractedSpectra: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.SignalTypeFilters
    ) = ...  # static # readonly
    InstrumentCurve: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.SignalTypeFilters
    ) = ...  # static # readonly
    Spectra: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.SignalTypeFilters
    ) = ...  # static # readonly

class Versions:  # Class
    RawDataReaderPluginVersion: int = ...  # static # readonly
