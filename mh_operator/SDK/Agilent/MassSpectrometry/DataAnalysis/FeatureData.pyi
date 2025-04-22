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

from .FeatureDetection import Feature
from .Quantitative.IndexedData import ScanConditions, ScanSpace

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.FeatureData

class FeatureDataAccess:  # Class
    def __init__(self) -> None: ...

    IsOpen: bool  # readonly
    ScanConditionList: System.Collections.Generic.List[ScanConditions]  # readonly

    def GetFeatureSet(
        self, scanConditions: ScanConditions
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureData.IFeatureSetQuery: ...
    def GetSaturatedFeatureCount(self) -> int: ...
    def Open(self, sampleDataPath: str) -> bool: ...
    def WriteFeaturesToFile(
        self, features: System.Collections.Generic.List[Feature], sampleDataPath: str
    ) -> None: ...
    def GetTotalFeatureCount(self) -> int: ...
    def Close(self) -> None: ...

class FeatureFile(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    IsOpen: bool  # readonly
    IsReadOnly: bool  # readonly

    def Read(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureData.SampleFeatures: ...
    def Write(
        self, sf: Agilent.MassSpectrometry.DataAnalysis.FeatureData.SampleFeatures
    ) -> None: ...
    def Open(self, sampleDataPath: str, readOnly: bool) -> None: ...
    def Close(self) -> None: ...
    @staticmethod
    def Exists(sampleDataPath: str) -> bool: ...
    def Dispose(self) -> None: ...

class FeatureSet(
    Agilent.MassSpectrometry.DataAnalysis.FeatureData.IFeatureSetQuery
):  # Class
    @overload
    def __init__(self, scanSpace: ScanSpace) -> None: ...
    @overload
    def __init__(
        self, scanSpace: ScanSpace, features: System.Collections.Generic.List[Feature]
    ) -> None: ...

    Count: int  # readonly
    SaturatedCount: int  # readonly
    ScanSpace: ScanSpace  # readonly

    @overload
    def GetFeatures(self) -> System.Collections.Generic.List[Feature]: ...
    @overload
    def GetFeatures(
        self, rtStart: float, rtEnd: float, mzLow: float, mzHigh: float
    ) -> System.Collections.Generic.List[Feature]: ...
    def GetCoelutingFeatures(
        self, f: Feature
    ) -> System.Collections.Generic.List[Feature]: ...
    def ReadFeatures(self, br: System.IO.BinaryReader) -> bool: ...
    def GetFeaturesInRTRange(
        self, rtStart: float, rtEnd: float
    ) -> System.Collections.Generic.List[Feature]: ...
    def WriteFeatures(self, bw: System.IO.BinaryWriter) -> None: ...
    def GetFeaturesInMzRange(
        self, mzLow: float, mzHigh: float
    ) -> System.Collections.Generic.List[Feature]: ...

class IFeatureSetQuery(object):  # Interface
    Count: int  # readonly
    SaturatedCount: int  # readonly
    ScanSpace: ScanSpace  # readonly

    def GetCoelutingFeatures(
        self, f: Feature
    ) -> System.Collections.Generic.List[Feature]: ...
    @overload
    def GetFeatures(self) -> System.Collections.Generic.List[Feature]: ...
    @overload
    def GetFeatures(
        self, rtStart: float, rtEnd: float, mzLow: float, mzHigh: float
    ) -> System.Collections.Generic.List[Feature]: ...
    def GetFeaturesInRTRange(
        self, rtStart: float, rtEnd: float
    ) -> System.Collections.Generic.List[Feature]: ...
    def GetFeaturesInMzRange(
        self, mzLow: float, mzHigh: float
    ) -> System.Collections.Generic.List[Feature]: ...

class SampleFeatures:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, features: System.Collections.Generic.List[Feature]) -> None: ...

    ScanConditionCount: int  # readonly
    ScanConditionList: System.Collections.Generic.List[ScanConditions]  # readonly

    def GetFeatureSet(
        self, scanConditions: ScanConditions
    ) -> Agilent.MassSpectrometry.DataAnalysis.FeatureData.FeatureSet: ...
    def GetScanSpace(self, scanConditions: ScanConditions) -> ScanSpace: ...
    def AddFeatureSet(
        self,
        scanSpace: ScanSpace,
        featureSet: Agilent.MassSpectrometry.DataAnalysis.FeatureData.FeatureSet,
    ) -> None: ...
