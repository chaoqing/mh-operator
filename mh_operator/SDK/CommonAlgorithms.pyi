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
    IFunction,
    IModificationSpecies,
    SpectralPeak,
    SpectralPeakFinderParameters,
)
from .Agilent.MassSpectrometry.DataAnalysis.MassHunter import (
    IRawSpectrumAccessor,
    SpectraType,
    SpectrumSetMetadata,
)
from .BasicTypes import (
    ChromMetadata,
    CoelutionGroup,
    EICCollection,
    IChromatographyObject,
    ILocation2D,
    IsotopeCluster,
    MfeCompound,
    MSProfile,
    Peak3D,
    PeakList,
    Signal3D,
    XYCollectionLine,
)
from .IsotopePatternCalculator import IIsotopePattern
from .Mathematics import RangeDouble
from .Mfe import IsotopeCharacter

# Stubs for namespace: CommonAlgorithms

class BaselineFinder:  # Class
    def __init__(
        self, shootingLengthForward: IFunction, shootingLengthBackward: IFunction
    ) -> None: ...
    def DetermineBaseline(self, data: List[float]) -> List[float]: ...

class BaselineFinderMSProfile:  # Class
    def __init__(self, shootingLength: IFunction) -> None: ...

    ShootingLength: float  # static # readonly

    def GetBaseline(self, spectrum: MSProfile) -> MSProfile: ...

class ChromObjectGrouper:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def Group(objectsWithRT: List[Any], targetWidth0: IFunction) -> List[Any]: ...

    # Nested Types

    class PeakGroup(
        List[IChromatographyObject],
        System.Collections.Generic.List[IChromatographyObject],
        Iterable[Any],
        Sequence[IChromatographyObject],
        Iterable[IChromatographyObject],
        Sequence[Any],
        List[Any],
    ):  # Class
        def __init__(self, count: int) -> None: ...

        MaxRT: float  # readonly
        MinRT: float  # readonly
        RT: float  # readonly

        # Nested Types

        class Comparer(
            System.Collections.Generic.IComparer[
                CommonAlgorithms.ChromObjectGrouper.PeakGroup
            ],
            System.Collections.IComparer,
        ):  # Class
            def __init__(self) -> None: ...
            @overload
            def Compare(self, o1: Any, o2: Any) -> int: ...
            @overload
            def Compare(
                self,
                g1: CommonAlgorithms.ChromObjectGrouper.PeakGroup,
                g2: CommonAlgorithms.ChromObjectGrouper.PeakGroup,
            ) -> int: ...

class CompoundGrouper:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def CalculateAveRTDeviation(compounds: List[Any]) -> float: ...
    @overload
    @staticmethod
    def GroupCompounds(
        compounds: List[Any], maxGroupSread: float
    ) -> List[CoelutionGroup]: ...
    @overload
    @staticmethod
    def GroupCompounds(
        compounds: List[MfeCompound], maxGroupSread: float
    ) -> List[CoelutionGroup]: ...

class CompoundMatcher:  # Class
    def __init__(self, formulas: Sequence[str]) -> None: ...
    def GetFormula(self, mass: float, retentionTime: float) -> str: ...
    def ContainsFormula(self, formula: str) -> bool: ...

class ConstScanRateEICProcessor(CommonAlgorithms.BaselineFinder):  # Class
    def __init__(
        self, rtPeakWidth: float, rts: List[float], scanRate: float
    ) -> None: ...
    def DetermineBaseline(self, data: List[float]) -> List[float]: ...

    # Nested Types

    class PeakWidthModel(IFunction):  # Class
        def __init__(
            self,
            lengthInTime: float,
            scanRate: float,
            rts: List[float],
            isForward: bool,
        ) -> None: ...

        IsConstant: bool  # readonly

        def Y(self, x: float) -> float: ...

class DuplicatedPeakChecker:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def Find(sortedMzs: List[float], heights: List[float]) -> Sequence[int]: ...

class FeatureCorrelator:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def CorrelateFeatures(
        signals: List[List[Any]],
        maxRTShift: IFunction,
        maxMassShift: IFunction,
        rtRange: RangeDouble,
        mzRange: RangeDouble,
    ) -> List[Any]: ...

class IntensityMatcher:  # Class
    def __init__(
        self,
        intensitiesSynthetics: List[float],
        intensitiesObserved: List[float],
        uncertainties: List[float],
    ) -> None: ...
    def CalculateMatchingScore(
        self, method: CommonAlgorithms.IntensityMatcher.Method, heightError: float
    ) -> float: ...

    # Nested Types

    class Method(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        ModifiedCC: CommonAlgorithms.IntensityMatcher.Method = ...  # static # readonly
        Probabilty: CommonAlgorithms.IntensityMatcher.Method = ...  # static # readonly

class IsotopeGrouper1:  # Class
    @overload
    def __init__(
        self,
        mzErrorFunction: ChromMetadata.MZError,
        userParameters: IsotopeCharacter,
        globalMinHeight: float,
        maxZ: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        mzErrorFunction: ChromMetadata.MZError,
        userParameters: IsotopeCharacter,
        globalMinHeight: float,
        precursorChargeCount: int,
        precursorMz: float,
        ms2DataWithPartialIsolationWindow: bool,
    ) -> None: ...

    Delta: float  # static # readonly

    @overload
    def Run(self, peaks: PeakList, maxZ: int) -> List[IsotopeCluster]: ...
    @overload
    def Run(
        self, peaks: PeakList
    ) -> System.Collections.Generic.List[IsotopeCluster]: ...
    @staticmethod
    def LocationError(mzError: ChromMetadata.MZError, mz: float) -> float: ...

class IsotopePatternMatcher:  # Class
    @overload
    def __init__(
        self, mzAccurayFunction: IFunction, relativeIntensityAccuracy: float
    ) -> None: ...
    @overload
    def __init__(
        self,
        mzAccurayFunction: IFunction,
        relativeIntensityAccuracy: float,
        scoreSinglePeak: bool,
        useProductScoring: bool,
        avgMzAbundPower: int,
    ) -> None: ...
    def CalculateMatchingScore(
        self,
        synthetic: PeakList,
        observed: PeakList,
        chargeCount: int,
        useMzScore: bool,
        useNewSpacingScoring: bool,
        averageMzScore: float,
        intensityScore: float,
        spacingScore: float,
        averageMzError: float,
        heightError: float,
        s1Error: float,
        s2Error: float,
    ) -> float: ...

class IsotopeScoreCalculator:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def GetScore(
        formula: str,
        peaks: List[SpectralPeak],
        numberOfTheoreticalPeakToCalculate: int,
        useLowestMzOnly: bool,
        ionSpecies: IModificationSpecies,
        massAccuracyCoeffients: List[float],
        relativeIntensityAccuracy: float,
        mzScore: float,
        intensityScore: float,
        spacingScore: float,
    ) -> float: ...
    @staticmethod
    def CalculateSyntheticPeaks(
        formula: str,
        z: int,
        ionSpecies: IModificationSpecies,
        maxPeakCountToUse: int,
        isotopeDistribution: IIsotopePattern,
    ) -> PeakList: ...

class Location2DGrid:  # Class
    def __init__(
        self,
        data: List[Any],
        xRange: RangeDouble,
        yRange: RangeDouble,
        gridSize: CommonAlgorithms.Location2DGrid.GridSize,
    ) -> None: ...

    AllPeaks: List[Any]  # readonly

    def Add(self, newPeak: ILocation2D) -> None: ...
    @overload
    def Neighbors(
        self, pk: ILocation2D
    ) -> System.Collections.Generic.List[ILocation2D]: ...
    @overload
    def Neighbors(
        self, mzStart: int, mzEnd: int, rtStart: int, rtEnd: int
    ) -> System.Collections.Generic.List[ILocation2D]: ...
    @overload
    def Neighbors(
        self, mz: float, rt: float, maxMzShift: float, maxRtShift: float
    ) -> System.Collections.Generic.List[ILocation2D]: ...
    def Remove(self, pk: ILocation2D) -> None: ...

    # Nested Types

    class GridSize:  # Struct
        def __init__(self, x: float, y: float) -> None: ...

        X: float
        Y: float

class MassErrorToSpacingErroConvertor:  # Class
    def __init__(self) -> None: ...

    Factor: float  # static # readonly

class MaxChargeManager:  # Class
    @overload
    def __init__(self, maxChargeCount: int) -> None: ...
    @overload
    def __init__(self, precursorMz: float, precursorChargeCount: int) -> None: ...

class NoiseLevelFinder:  # Class
    def __init__(self, data: List[float]) -> None: ...

    NoiseFunction: IFunction  # readonly

    def ThresholdLevel(self, threshold: float) -> IFunction: ...

class Peak3DQualityScoreAssigner:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def QCScore(pk: Peak3D, averagePeakWidth: float) -> float: ...

class PeakFinderParallelizer:  # Class
    @overload
    def __init__(
        self,
        spectrumAccessor: IRawSpectrumAccessor,
        rtRange: RangeDouble,
        mzRange: RangeDouble,
        metadata: ChromMetadata,
        rtHalfTaperSpan: float,
        aproriRTPeakWidth: float,
        parameters: SpectralPeakFinderParameters,
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    PeakLists: List[PeakList]  # readonly
    StepCount: int  # readonly

    def StepIt(self, stepIndex: int) -> None: ...
    def SetData(
        self,
        spectrumAccessor: IRawSpectrumAccessor,
        rtRange: RangeDouble,
        mzRange: RangeDouble,
        metadata: ChromMetadata,
        rtHalfTaperSpan: float,
        aproriRTPeakWidth: float,
        parameters: SpectralPeakFinderParameters,
    ) -> None: ...

class PeakListAligner:  # Class
    def __init__(
        self,
        synthetic: PeakList,
        observed: PeakList,
        mzAccuray: float,
        alignByFirstPeak: bool,
    ) -> None: ...
    def GetPairedIntensities(
        self, intensityA: List[float], intensityB: List[float]
    ) -> None: ...
    def GetPairedPeaks(self, peaksA: PeakList, peaksB: PeakList) -> bool: ...
    def GetPaddedPeaks(self, peaksA: PeakList, peaksB: PeakList) -> None: ...

class Probability:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def GetPaddedProbabilityDensity(
        originalDensity: float, minDensity: float
    ) -> float: ...

class ProfileSpectraReaderEmptySpectraFree(IRawSpectrumAccessor):  # Class
    def __init__(self, rawReader: IRawSpectrumAccessor) -> None: ...

    FullSaturationLevel: float  # readonly
    Metadata: SpectrumSetMetadata  # readonly
    ScanCalibCoefficients: List[float]  # readonly
    ScanFirstBinIndex: int  # readonly
    ScanFirstXValue: float  # readonly
    ScanProfileIntensities: List[float]  # readonly
    ScanRetentionTimes: List[float]  # readonly
    SpectraType: SpectraType  # readonly
    TicIntensities: List[float]  # readonly

    def Close(self) -> None: ...
    def GetPeakList(
        self, mz: List[float], heights: List[float], errorCode: List[int]
    ) -> None: ...
    def Open(self) -> None: ...
    def UpdateScan(self, scanIndex: int, minMZ: float, maxMZ: float) -> None: ...

class RtPeakWidthEstimator:  # Class
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def MeasurePeakWidth(
        eics: EICCollection, retentionTimes: List[float], maxHeight: float
    ) -> float: ...
    @overload
    @staticmethod
    def MeasurePeakWidth(profileSpectraReader: IRawSpectrumAccessor) -> float: ...

class SmootherMSProfile:  # Class
    def __init__(self, smoothingLenth: IFunction, strengths: List[float]) -> None: ...

    SmoothingLength: float  # static # readonly

    @overload
    def Smooth(self, raw: MSProfile) -> MSProfile: ...
    @overload
    def Smooth(self, raw: List[float]) -> List[float]: ...

class XYCollectionLineBinner:  # Class
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def Run(data: XYCollectionLine, minMZ: float) -> None: ...
    @overload
    @staticmethod
    def Run(
        signals: System.Collections.Generic.List[Signal3D],
        metaData: ChromMetadata,
        minMZ: float,
    ) -> EICCollection: ...
