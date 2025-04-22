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
from . import ProviderLookupCacheBase
from .Interfaces import (
    IProviderLookupCache,
    IResourcesProvider,
    ISampleContextProvider,
    ISamplesProvider,
)

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Caches

class GlobalExternalReferenceRawDataCache:  # Class
    ChromDataCache: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Caches.TypedReferenceRawDataCache[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
    ]  # readonly
    Instance: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Caches.GlobalExternalReferenceRawDataCache
    )  # static # readonly
    SpectraDataCache: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Caches.TypedReferenceRawDataCache[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectraData
    ]  # readonly
    SpectrumDataCache: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Caches.TypedReferenceRawDataCache[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData
    ]  # readonly
    TotalCacheSize: int  # readonly
    TotalDataPointsCached: int  # readonly

    @staticmethod
    def Reset() -> None: ...

class GlobalQueryCache:  # Class
    Instance: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Caches.GlobalQueryCache
    )  # static # readonly
    IsEnabled: bool
    MaxCacheSize: int

    def Invalidate(self) -> None: ...

class GlobalRawDataCache:  # Class
    ChromDataCache: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Caches.TypedRawDataCache[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.IChromData
    ]  # readonly
    Instance: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Caches.GlobalRawDataCache
    )  # static # readonly
    SpectraDataCache: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Caches.TypedRawDataCache[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectraData
    ]  # readonly
    SpectrumDataCache: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Caches.TypedRawDataCache[
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ISpectrumData
    ]  # readonly
    TotalCacheSize: int  # readonly
    TotalDataPointsCached: int  # readonly

    @staticmethod
    def Reset() -> None: ...

class ResourcesProviderLookupCache(
    ProviderLookupCacheBase[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IResourcesType,
        IResourcesProvider,
    ],
    IProviderLookupCache,
):  # Class
    def __init__(
        self,
        docId: System.Guid,
        dataRoot: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IResourcesType,
        provider: IResourcesProvider,
    ) -> None: ...

    CalibCurveDictionary: System.Collections.ObjectModel.ReadOnlyDictionary[
        System.Guid,
        Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
    ]  # readonly
    InstrumentDictionary: System.Collections.ObjectModel.ReadOnlyDictionary[
        System.Guid,
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IInstrumentType,
    ]  # readonly
    SeparationMediaDictionary: System.Collections.ObjectModel.ReadOnlyDictionary[
        System.Guid,
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISeparationMediumType,
    ]  # readonly

    def UpdateOnCalibrationCurveChanges(self) -> None: ...
    def UpdateOnInstrumentChanges(self) -> None: ...
    def Clear(self) -> None: ...
    def UpdateOnAddCalibrationCurve(
        self,
        calibrationCurveType: Agilent.OpenLab.Framework.DataAccess.CoreTypes.ICalibrationCurveType,
    ) -> None: ...
    def UpdateOnSeparationMediaChanges(self) -> None: ...

class SampleContextProviderLookupCache(
    IProviderLookupCache,
    ProviderLookupCacheBase[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContextsType,
        ISampleContextProvider,
    ],
):  # Class
    def __init__(
        self,
        docId: System.Guid,
        dataRoot: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleContextsType,
        provider: ISampleContextProvider,
    ) -> None: ...

    ResultSetSetupMeasDataDictionary: System.Collections.ObjectModel.ReadOnlyDictionary[
        System.Guid,
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleMeasDataContextType,
    ]  # readonly

    def Clear(self) -> None: ...

class SamplesProviderLookupCache(
    ProviderLookupCacheBase[
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplesType,
        ISamplesProvider,
    ],
    IProviderLookupCache,
):  # Class
    def __init__(
        self,
        docId: System.Guid,
        dataRoot: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISamplesType,
        provider: ISamplesProvider,
    ) -> None: ...

    SampleSetupMeasDataDictionary: System.Collections.ObjectModel.ReadOnlyDictionary[
        System.Guid,
        Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.ISampleMeasDataType,
    ]  # readonly

    def Clear(self) -> None: ...

class TypedRawDataCache(Generic[T]):  # Class
    IsCacheFull: bool  # readonly
    TotalCacheSize: int  # readonly
    TotalDataPointsCached: int  # readonly

class TypedReferenceRawDataCache(Generic[T]):  # Class
    IsCacheFull: bool  # readonly
    TotalCacheSize: int  # readonly
    TotalDataPointsCached: int  # readonly
