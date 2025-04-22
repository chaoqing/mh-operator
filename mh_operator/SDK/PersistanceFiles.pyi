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

from .Agilent.MassSpectrometry.DataAnalysis import (
    CnEngine,
    IModificationUnit,
    SpectralPeak,
)
from .BasicTypes import ChromMetadata, MfeCompound, Peak3D, PeakList, Protein, TOFCalib
from .Mathematics import RangeDouble
from .Mfe import (
    CompoundFormationParameters,
    IEngineBlockUserParameters,
    IsotopeCharacter,
)

# Stubs for namespace: PersistanceFiles

class CompoundEvidenceReader:  # Class
    def __init__(self, filePath: str) -> None: ...

    FilePath: str  # readonly

    def ReadRawEic(self, mzRange: RangeDouble) -> List[float]: ...
    def ReadRawData(
        self, retentionTime: float, timeWidth: float, targetMz: List[RangeDouble]
    ) -> PersistanceFiles.CompoundEvidences: ...
    @staticmethod
    def CalculateEic(
        peakLists: List[PeakList],
        metadata: ChromMetadata,
        boundaries: List[float],
        eics: List[Sequence[PersistanceFiles.MfeFile.Signal]],
    ) -> None: ...
    def ReadCompoundAndItsRawData(
        self, mass: float, retentionTime: float
    ) -> PersistanceFiles.CompoundEvidences: ...

class CompoundEvidences:  # Class
    def __init__(self) -> None: ...

    CompoundEics: List[List[float]]
    CompoundMzs: List[RangeDouble]
    CompoundPeaks: List[SpectralPeak]
    RawEics: List[List[float]]
    RawSpectrum: List[SpectralPeak]
    RetentionTimes: List[float]
    TimeRange: RangeDouble

class EicFormationParameters(IEngineBlockUserParameters):  # Class
    def __init__(self) -> None: ...

class MfeFile:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def AppUpdateRmfeCompounds(
        filePath: str,
        engineBlockInfo: PersistanceFiles.MfeFile.BlockInfo,
        compounds: List[MfeCompound],
        modificationCode: Dict[IModificationUnit, int],
        isotopeCharacter: IsotopeCharacter,
        blockIndex: int,
    ) -> None: ...
    @staticmethod
    def AppendUpdateCompounds(
        filePath: str,
        engineBlockInfo: PersistanceFiles.MfeFile.BlockInfo,
        compounds: List[MfeCompound],
        blockIndex: int,
    ) -> None: ...
    @staticmethod
    def CreateChargeUnitCode(
        parameters: CompoundFormationParameters,
    ) -> Dict[IModificationUnit, int]: ...
    @staticmethod
    def AppendUpdatePeak3Ds(
        filePath: str,
        engineBlockInfo: PersistanceFiles.MfeFile.BlockInfo,
        peaks: List[Peak3D],
        rtPeakWidth: float,
        minSpectralPeakHeight: float,
    ) -> None: ...
    @staticmethod
    def ReadCompounds(
        filePath: str, compoundInfoLevel: PersistanceFiles.MfeFile.FeatureInfoLevel
    ) -> List[MfeCompound]: ...
    @staticmethod
    def ReadFileInfo(filePath: str) -> PersistanceFiles.MfeFile.FileInfo: ...
    @staticmethod
    def ReadPeak3Ds(
        filePath: str,
        peak3DInfoLevel: PersistanceFiles.MfeFile.Peak3DInfoLevel,
        rtPeakWidth: float,
        minSpectralPeakHeight: float,
    ) -> List[Peak3D]: ...
    @overload
    @staticmethod
    def ReadSpectralPeakLists(
        filePath: str,
        rtRange: RangeDouble,
        mzRange: RangeDouble,
        totalNumberOfPeaksRead: int,
    ) -> List[PeakList]: ...
    @overload
    @staticmethod
    def ReadSpectralPeakLists(
        filePath: str,
    ) -> PersistanceFiles.SpectralPeakStorage: ...
    @overload
    @staticmethod
    def ReadSpectralPeakLists(
        filePath: str, rtRange: RangeDouble
    ) -> PersistanceFiles.SpectralPeakStorage: ...
    @staticmethod
    def CreateFileAndSaveGloblaHeader(
        filePath: str, metadata: ChromMetadata, calibs: List[TOFCalib]
    ) -> None: ...
    @staticmethod
    def AppUpdateEics(
        filePath: str,
        engineBlockInfo: PersistanceFiles.MfeFile.BlockInfo,
        binBoundaries: List[float],
        signalBins: List[Sequence[PersistanceFiles.MfeFile.Signal]],
    ) -> None: ...
    @staticmethod
    def CreateFileAndSaveSpectralPeaks(
        filePath: str,
        peakLists: PersistanceFiles.SpectralPeakStorage,
        engineBlockInfo: PersistanceFiles.MfeFile.BlockInfo,
        metadata: ChromMetadata,
    ) -> None: ...
    @staticmethod
    def ReadMetadata(filePath: str, calibs: List[TOFCalib]) -> ChromMetadata: ...
    @staticmethod
    def ReadProteins(
        filePath: str, proteinInfoLevel: PersistanceFiles.MfeFile.FeatureInfoLevel
    ) -> List[Protein]: ...
    @staticmethod
    def AppendUpdateProteins(
        filePath: str,
        engineBlockInfo: PersistanceFiles.MfeFile.BlockInfo,
        proteins: List[Protein],
    ) -> None: ...
    @staticmethod
    def UpdateRmfeCompounds(
        filePath: str,
        blockInfoRead: PersistanceFiles.MfeFile.BlockInfo,
        compounds: List[MfeCompound],
        blockIndex: int,
    ) -> None: ...
    @staticmethod
    def ReadAdductList(filePath: str) -> List[IModificationUnit]: ...

    # Nested Types

    class BlockInfo:  # Class
        def __init__(self) -> None: ...

        AlgorithmVersion: int
        BlockType: PersistanceFiles.MfeFile.BlockType
        CreatedByMfe: bool
        DataGlobalOffset: int
        FormatVersion: int
        ParameterGlobalOffset: int
        SaveResult: bool
        UserParameters: IEngineBlockUserParameters

    class BlockType(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        Compounds: PersistanceFiles.MfeFile.BlockType = ...  # static # readonly
        Eic: PersistanceFiles.MfeFile.BlockType = ...  # static # readonly
        Peak3Ds: PersistanceFiles.MfeFile.BlockType = ...  # static # readonly
        Proteins: PersistanceFiles.MfeFile.BlockType = ...  # static # readonly
        RmfcCompounds: PersistanceFiles.MfeFile.BlockType = ...  # static # readonly
        SpectralPeaks: PersistanceFiles.MfeFile.BlockType = ...  # static # readonly
        Unknown: PersistanceFiles.MfeFile.BlockType = ...  # static # readonly

    class FeatureInfoLevel(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        FeatureAttributesOnly: PersistanceFiles.MfeFile.FeatureInfoLevel = (
            ...
        )  # static # readonly
        MostDetailed: PersistanceFiles.MfeFile.FeatureInfoLevel = (
            ...
        )  # static # readonly
        UpToPeak3DAttributes: PersistanceFiles.MfeFile.FeatureInfoLevel = (
            ...
        )  # static # readonly

    class FileInfo:  # Class
        def __init__(self) -> None: ...

        BlockInfos: System.Collections.Generic.List[PersistanceFiles.MfeFile.BlockInfo]
        FilePath: str
        Metadata: ChromMetadata
        VariableMetadataBlockOffset: int

    class Peak3DInfoLevel(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        MostDetailed: PersistanceFiles.MfeFile.Peak3DInfoLevel = (
            ...
        )  # static # readonly
        Peak3DAttributesOnly: PersistanceFiles.MfeFile.Peak3DInfoLevel = (
            ...
        )  # static # readonly

    class Signal:  # Struct
        def __init__(self, scanIndex: int, height: float) -> None: ...

        Height: float
        ScanIndex: int

class RmfeParameters(IEngineBlockUserParameters):  # Class
    def __init__(self) -> None: ...

    CorrelationParameters: CnEngine.UserParameters
    MinQualityScoreForBucket: float
    SamplePathAndScalings: Dict[str, float]

    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(self, other: PersistanceFiles.RmfeParameters) -> bool: ...
    def BinaryWrite(self, writer: System.IO.BinaryWriter) -> None: ...
    def BinaryRead(self, reader: System.IO.BinaryReader) -> None: ...
    def GetHashCode(self) -> int: ...
    def CalculateDataBlockLength(self) -> int: ...

class SpectralPeakStorage(Iterable[Any], Iterable[PeakList]):  # Class
    def __init__(self, persistanceFilePath: str) -> None: ...

    Calibrations: List[TOFCalib]  # readonly
    MZRange: RangeDouble  # readonly
    SequenciallyAccessiblePeakLists: List[PeakList]  # readonly
    SpectraCount: int  # readonly
    TotalPeakCount: int  # readonly

    def GetEnumerator(self) -> Iterator[PeakList]: ...
    def FinishAdding(self) -> None: ...
    def AddPeakList(self, peaks: PeakList) -> None: ...
    def AddPeakLists(self, peakLists: List[PeakList]) -> None: ...
    def Dispose(self) -> None: ...
