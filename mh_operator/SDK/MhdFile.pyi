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

from .Agilent.MassSpectrometry.DataAnalysis.MassHunter import CompoundFilterParameters
from .BasicTypes import (
    ChromMetadata,
    MfeCompound,
    PeakList,
    SampleChemistryInfo,
    XYCollectionLine,
)
from .Mathematics import RangeDouble, RangeInt
from .PersistanceFiles import SpectralPeakStorage

# Stubs for namespace: MhdFile

class ExtractorUserParameters:  # Class
    def __init__(self) -> None: ...

    DefaultMaxSpectralPeakCount: int  # static # readonly
    MaxSpectralPeakCount: int
    SampleChemistryInfo: SampleChemistryInfo

    C13IsotopePattern: bool  # readonly
    MaxChargeCount: int  # readonly
    SaltDominated: bool  # readonly

    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(self, p: MhdFile.ExtractorUserParameters) -> bool: ...
    def GetHashCode(self) -> int: ...
    def Clone(self) -> MhdFile.ExtractorUserParameters: ...

class P3DFile:  # Class
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def ReadCompounds(
        filePath: str,
        filters: CompoundFilterParameters,
        infoLevel: MfeCompound.InfoLevel,
    ) -> List[MfeCompound]: ...
    @overload
    @staticmethod
    def ReadCompounds(
        filePath: str,
        compoundStorageOffse: int,
        requestedLevel: MfeCompound.InfoLevel,
        useAveragine: bool,
        filterParameters: CompoundFilterParameters,
        compoundFormatVersion: int,
        scanWidths: List[float],
    ) -> List[MfeCompound]: ...
    @overload
    @staticmethod
    def ReadCompounds(
        filePath: str,
        compoundStorageOffse: int,
        requestedLevel: MfeCompound.InfoLevel,
        useAveragine: bool,
        compoundFormatVersion: int,
        scanWidth: List[float],
    ) -> System.Collections.Generic.List[MfeCompound]: ...
    @staticmethod
    def ReadHeaders(filePath: str) -> MhdFile.P3DFile.FileInfo: ...
    @overload
    @staticmethod
    def ReadSpectralPeaks(
        filePath: str,
        fileInfo: MhdFile.P3DFile.FileInfo,
        scanRange: RangeInt,
        mzRange: RangeDouble,
    ) -> System.Collections.Generic.List[PeakList]: ...
    @overload
    @staticmethod
    def ReadSpectralPeaks(
        filePath: str, fileInfo: MhdFile.P3DFile.FileInfo, scanRange: RangeInt
    ) -> SpectralPeakStorage: ...
    @staticmethod
    def ReadXYCollection(
        filePath: str, rtRange: RangeDouble, fileInfo: MhdFile.P3DFile.FileInfo
    ) -> XYCollectionLine: ...

    # Nested Types

    class FileInfo:  # Class
        def __init__(self) -> None: ...

        AlgorithmVersion: int
        CalibCoeffCount: int
        CompoundFormatVersion: int
        FileSize: int
        HunterParameters: MhdFile.ExtractorUserParameters
        Metadata: ChromMetadata
        PeakCount: int
        PeakFindingParameters: MhdFile.P3DFile.PeakFindingParameters
        PeakFormatVersion: int
        SpectralPeakFinderVersion: int
        Version: int

        CompoundBlockOffset: int  # readonly
        CompoundsAreAvailable: bool  # readonly

    class PeakFindingParameters:  # Class
        def __init__(self) -> None: ...

        MZRange: RangeDouble
        PeakPickingThresold: float
        RTRange: RangeDouble
        ThresholdType: int

        @staticmethod
        def Validate(
            userParameters: MhdFile.P3DFile.PeakFindingParameters,
            metadata: ChromMetadata,
        ) -> str: ...
        def Clone(self) -> MhdFile.P3DFile.PeakFindingParameters: ...
