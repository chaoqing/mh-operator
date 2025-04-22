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

from .Interfaces import (
    IAcamlReader,
    IAcamlReaderWriter,
    IAcamlSignalLoader,
    IAcamlWriter,
)

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.DataHandlers

class AcamlObjectStore:  # Class
    @staticmethod
    def IsInitialized(docId: System.Guid) -> bool: ...
    @staticmethod
    def UpdateDocumentBaseDirectory(docId: System.Guid, fileName: str) -> None: ...
    @staticmethod
    def Clear() -> None: ...
    @staticmethod
    def GetDocumentBaseDirectory(
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        docId: System.Guid,
    ) -> str: ...
    @staticmethod
    def GetDocumentFileName(docId: System.Guid) -> str: ...
    @staticmethod
    def Exists(docId: System.Guid) -> bool: ...
    @staticmethod
    def PrepareForDataModifications(
        docId: System.Guid,
    ) -> System.Threading.Tasks.Task[None]: ...

class AcamlReaderWriter(
    IAcamlReaderWriter,
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.DistributedAcaml.IAcamlReaderWriterServices,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, validateChecksum: bool, validateSchema: bool) -> None: ...

    EnforceAcamlBusinessRules: bool
    PrepareForDataModification: bool
    ValidateChecksumOnLoad: bool
    ValidateChecksumOnSave: bool
    ValidateSchemaOnLoad: bool
    ValidateSchemaOnSave: bool

    def CreateWriter(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
        fileName: str,
        saveOnlyChangedData: bool = ...,
        updateMetadata: bool = ...,
    ) -> IAcamlWriter: ...
    @staticmethod
    def MergeInjectionAcamls(
        sequenceAcaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
        injectionMeasDataIds: Iterable[System.Guid] = ...,
    ) -> None: ...
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
    @staticmethod
    def UnloadAll() -> None: ...
    @staticmethod
    def Validate(
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
    @staticmethod
    def CreateAcaml(
        description: str,
        userName: str,
        clientName: str,
        appType: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.AgilentAppType,
    ) -> Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML: ...
    def CreateReader(self) -> IAcamlReader: ...
    @staticmethod
    def UnloadAcaml(docId: System.Guid) -> None: ...
    @staticmethod
    def UnloadAcamls(docIds: Iterable[System.Guid]) -> None: ...

class AcamlSignalLoader(IAcamlSignalLoader):  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def CancelSignalPrefetching() -> None: ...
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
    @overload
    @staticmethod
    def LoadChromatogram(
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        path: str,
    ) -> Sequence[
        Agilent.OpenLab.Framework.DataAccess.CoreType.ISignalDataContainer[
            Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
        ]
    ]: ...
    @overload
    @staticmethod
    def LoadChromatogram(
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
    @overload
    @staticmethod
    def LoadSpectra(
        storageProvider: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
        workAreaName: str,
        path: str,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectraData: ...
    @overload
    @staticmethod
    def LoadSpectra(
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

class AcamlSignalLoaderManager:  # Class
    AcamlSignalLoader: IAcamlSignalLoader  # static # readonly

    @staticmethod
    def SetSignalLoader(acamSignalLoader: IAcamlSignalLoader) -> None: ...

class CalibrationCurveReaderWriter:  # Class
    @staticmethod
    def Deserialize(
        serializedCalibrationCurve: str,
    ) -> Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType: ...
    @staticmethod
    def Serialize(
        calibrationCurve: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
    ) -> str: ...
