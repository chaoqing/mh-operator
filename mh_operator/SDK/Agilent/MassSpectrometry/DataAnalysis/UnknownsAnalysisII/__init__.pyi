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

import Agilent
import System

from . import (
    Component,
    ComponentPerceptionParams,
    DoubleRangeD,
    IChromatogram,
    IChromPeak,
    ICoreAlgorithmFactory,
    IDataAccess,
    ILibrary,
    IonPeak,
    IonPolarity,
    IPeak,
    ISpectrum,
    LibrarySearchParams,
    MSScanType,
    RTCalibrationTable,
)
from .Exactify import ExactifyParams
from .Quantitative import IntegratorType, Signal
from .Quantitative.Compliance import ICompliance

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII

class AccurateMassPatternMatch:  # Class
    def __init__(
        self,
        cancelEvent: System.Threading.WaitHandle,
        imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
        lsmrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow,
        library: ILibrary,
        rtcal: RTCalibrationTable,
    ) -> None: ...

    RTCalibrationTable: RTCalibrationTable  # readonly

    def ProcessComponent(
        self,
        crow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
        mzs: List[float],
        abs: List[float],
        rt: float,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.AccurateMassPatternMatch.HitItem
    ]: ...

    # Nested Types

    class HitItem:  # Class
        def __init__(
            self,
            lsmrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow,
            library: ILibrary,
            rtTable: RTCalibrationTable,
            score: float,
            spectrumIndex: int,
            match: Agilent.MassSpectrometry.IAmrtMatch,
        ) -> None: ...

        Score: float  # readonly

        @overload
        def AddTo(
            self,
            hdt: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitDataTable,
            crow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
            imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
            hitID: int,
        ) -> None: ...
        @overload
        def AddTo(
            self,
            crow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
            imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
            hitID: int,
            resultsStore: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IResultsStore,
        ) -> None: ...
        @staticmethod
        def Compare(
            h1: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.AccurateMassPatternMatch.HitItem,
            h2: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.AccurateMassPatternMatch.HitItem,
        ) -> int: ...

class AppConfigurationSection(System.Configuration.ConfigurationSection):  # Class
    def __init__(self) -> None: ...

class BestHitSelector:  # Class
    def __init__(
        self,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
        batchID: int,
        sampleID: int,
    ) -> None: ...
    def GetGroupedComponents(
        self,
        componentRow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
    ]: ...
    def ProcessComponents(self) -> None: ...

class BlankSubtract:  # Class
    def __init__(
        self,
        abortEvent: System.Threading.WaitHandle,
        dataset: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
        blankHits: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IBlankHits,
        resultsStore: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IResultsStore,
    ) -> None: ...
    def Process(self) -> None: ...

class BlankSubtractPeakThresholdType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ComponentArea: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.BlankSubtractPeakThresholdType
    ) = ...  # static # readonly
    EstimatedConcentration: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.BlankSubtractPeakThresholdType
    ) = ...  # static # readonly

class BlankSubtractRTWindowType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    FullWidthHalfMaximum: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.BlankSubtractRTWindowType
    ) = ...  # static # readonly
    Minutes: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.BlankSubtractRTWindowType
    ) = ...  # static # readonly

class BlankSubtractionMethodRowID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.BlankSubtractionMethodRowID
    ],
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, blankSubtractionMethodID: int
    ) -> None: ...

    BatchID: int  # readonly
    BlankSubtractionMethodID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        rid: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.BlankSubtractionMethodRowID,
    ) -> int: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(
        self,
        rid: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.BlankSubtractionMethodRowID,
    ) -> bool: ...

class ComponentRowID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ComponentRowID
    ],
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int, componentID: int
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ComponentRowID,
    ) -> int: ...
    @overload
    def Equals(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ComponentRowID,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class Deconvolution:  # Class
    def __init__(
        self,
        cancelEvent: System.Threading.WaitHandle,
        dataAccess: IDataAccess,
        compliance: ICompliance,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
        batchID: int,
        sampleID: int,
        taskScheduler: System.Threading.Tasks.TaskScheduler,
        deconvolutionScreening: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IDeconvolutionScreening,
        resultsStore: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IResultsStore,
        reportProgress: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IReportProgress,
    ) -> None: ...
    @staticmethod
    def FilterComponents(
        dmrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow,
        components: System.Collections.Generic.List[Component],
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Deconvolution.ComponentAreaHeight
    ]: ...
    def ProcessDeconvolution(self, deconvolutionMethodID: int) -> None: ...
    def ProcessTargetedDeconvolution(
        self,
        deconvolutionMethodID: int,
        openLibrary: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IOpenLibrary,
    ) -> None: ...
    @staticmethod
    def CalcDeconvolutedValues(
        component: Component, area: Optional[float], height: Optional[float]
    ) -> None: ...

    # Nested Types

    class ComponentAreaHeight:  # Class
        def __init__(self, component: Component) -> None: ...

        Area: Optional[float]  # readonly
        Component: Component  # readonly
        Height: Optional[float]  # readonly

class DeconvolutionAlgorithmFactory(ICoreAlgorithmFactory):  # Class
    def __init__(
        self, baseFactory: ICoreAlgorithmFactory, integratorType: IntegratorType
    ) -> None: ...

    IntegratorType: IntegratorType  # readonly

class DeconvolutionMethodRowID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DeconvolutionMethodRowID
    ],
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int
    ) -> None: ...

    BatchID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DeconvolutionMethodRowID,
    ) -> int: ...
    @overload
    def Equals(
        self,
        rowID: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DeconvolutionMethodRowID,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class DelayDeleteFile:  # Class
    def __init__(self, file: str) -> None: ...

class DuplicatePeakRemoval:  # Class
    def __init__(
        self,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
        batchID: int,
        sampleID: int,
    ) -> None: ...
    @overload
    @staticmethod
    def RemoveDuplicateSpectrumPeaks(
        componentID: int,
        hitID: int,
        deconvolutionMethodID: int,
        referenceMzValues: List[float],
    ) -> List[float]: ...
    @overload
    @staticmethod
    def RemoveDuplicateSpectrumPeaks(
        hitRow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow,
        referenceMzValues: List[float],
    ) -> List[float]: ...
    @overload
    @staticmethod
    def RemoveDuplicateSpectrumPeaks(
        mzValues: List[float],
        abundanceValues: List[float],
        referenceMzValues: List[float],
        extractionMzDeltaPpm: float,
        accurateMassTolerancePpm: float,
        nonDuplicateMzValues: List[float],
        nonDuplicateAbundanceValues: List[float],
    ) -> List[float]: ...

class EventHandlerSet(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    Empty: bool  # readonly
    def __getitem__(self, key: Any) -> System.Delegate: ...
    def __setitem__(self, key: Any, value_: System.Delegate) -> None: ...
    def DoFire(self, key: Any, args: List[Any]) -> None: ...
    def Add(self, key: Any, handler: System.Delegate) -> None: ...
    def GetInvocationList(self, key: Any) -> List[System.Delegate]: ...
    def Clear(self) -> None: ...
    def Remove(self, key: Any, handler: System.Delegate) -> None: ...
    def Dispose(self) -> None: ...

class ExactMassCalculation:  # Class
    def __init__(
        self,
        ds: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
        batchID: int,
        sampleID: int,
        openLibrary: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IOpenLibrary,
        resultsStore: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IResultsStore,
        reportProgress: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IReportProgress,
    ) -> None: ...
    def ProcessSample(self) -> None: ...

class ExactMassRowID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ExactMassRowID
    ],
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        exactMassID: int,
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    ExactMassID: int  # readonly
    HitID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ExactMassRowID,
    ) -> int: ...
    @overload
    def Equals(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ExactMassRowID,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class HitConcentrationEstimation(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AverageRFofAllISTDs: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.HitConcentrationEstimation
    ) = ...  # static # readonly
    AverageRFofAllTargets: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.HitConcentrationEstimation
    ) = ...  # static # readonly
    AverageRFofClosestTarget: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.HitConcentrationEstimation
    ) = ...  # static # readonly
    ManualRF: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.HitConcentrationEstimation
    ) = ...  # static # readonly
    RFofClosestISTD: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.HitConcentrationEstimation
    ) = ...  # static # readonly
    RFofClosestTargetISTD: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.HitConcentrationEstimation
    ) = ...  # static # readonly
    RelativeISTDEstimation: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.HitConcentrationEstimation
    ) = ...  # static # readonly

class HitRowID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.HitRowID
    ],
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    HitID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self, other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.HitRowID
    ) -> int: ...
    @overload
    def Equals(
        self, rid: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.HitRowID
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class IBlankHits(object):  # Interface
    BlankSampleCount: int  # readonly

    def HasBlankHits(
        self,
        hit: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow,
        parentComponent: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
        modelIonPeak: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow,
        method: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow,
    ) -> bool: ...

class IDeconvolutionScreening(object):  # Interface
    def GetLibraryMZValues(
        self,
        rows: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        ],
    ) -> System.Collections.Generic.List[float]: ...

class ILibraryFile(object):  # Interface
    Library: ILibrary  # readonly

class IOpenLibrary(object):  # Interface
    def CloseLibrary(
        self,
        library: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ILibraryFile,
    ) -> None: ...
    def OpenLibrary(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow,
    ) -> Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ILibraryFile: ...

class IReportProgress(object):  # Interface
    def ReportProgress(self, totalSteps: int, currentStep: int) -> None: ...

class IResultsStore(object):  # Interface
    def SetComponentHit(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        primaryHitID: Optional[int],
        retentionIndex: Optional[float],
    ) -> None: ...
    def SetNumberOfExactMasses(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        numOfExactMasses: int,
    ) -> None: ...
    def InsertHit(
        self,
        values: System.Collections.Generic.List[
            System.Collections.Generic.KeyValuePair[str, Any]
        ],
    ) -> None: ...
    def SetBlankSubtracted(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
    ) -> None: ...
    @overload
    def InsertIonPeak(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
        component: Component,
        ionPeak: IonPeak,
    ) -> None: ...
    @overload
    def InsertIonPeak(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
        eicPeak: IChromPeak,
        scanType: MSScanType,
        ionPolarity: IonPolarity,
        eic: IChromatogram,
        mzPeak: IPeak,
    ) -> None: ...
    @overload
    def InsertComponent(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        component: Component,
        deconvolutedArea: Optional[float],
        deconvolutedHeight: Optional[float],
    ) -> None: ...
    @overload
    def InsertComponent(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        chromatogram: IChromatogram,
        spectrum: ISpectrum,
        peak: IChromPeak,
        polarity: IonPolarity,
        isAccurateMass: bool,
    ) -> None: ...
    def SetComponent(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        basePeakID: Optional[int],
        modelIonPeakID: Optional[int],
    ) -> None: ...
    def InsertExactMass(
        self, values: Iterable[System.Collections.Generic.KeyValuePair[str, Any]]
    ) -> None: ...
    def SetTargetedDeconvolution(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
        libEntryID: int,
    ) -> None: ...

class Identification:  # Class
    def __init__(
        self,
        cancelEvent: System.Threading.WaitHandle,
        compliance: ICompliance,
        openLibrary: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IOpenLibrary,
        dataAccess: IDataAccess,
        resultsStore: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IResultsStore,
        reportProgress: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IReportProgress,
        imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
        lsmrows: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        ],
    ) -> None: ...

    Lock: Any  # static

    def ProcessComponent(
        self,
        dmrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow,
        crow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
        iprows: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow
        ],
        basePeak: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow,
    ) -> None: ...

class IdentificationMethodRowID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IdentificationMethodRowID
    ],
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, identificationMethodID: int
    ) -> None: ...

    BatchID: int  # readonly
    IdentificationMethodID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IdentificationMethodRowID,
    ) -> int: ...
    @overload
    def Equals(
        self,
        rid: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IdentificationMethodRowID,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class IonPeakRowID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IonPeakRowID
    ],
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    IonPeakID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IonPeakRowID,
    ) -> int: ...
    @overload
    def Equals(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IonPeakRowID,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class LibrarySearch:  # Class
    def __init__(
        self,
        compliance: ICompliance,
        imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
        lsmrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow,
        library: ILibrary,
        dataAccess: IDataAccess,
    ) -> None: ...

    LibrarySearchMethod: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
    )  # readonly
    RTCalibrationTable: RTCalibrationTable  # readonly

    # Nested Types

    class HitItem:  # Class
        Library: ILibrary  # readonly
        LibrarySeachMethodRow: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        )  # readonly
        MatchFactor: float
        RemovedDuplicateMZs: List[float]

        @overload
        def AddTo(
            self,
            hdt: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitDataTable,
            crow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
            imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
            hitID: int,
        ) -> None: ...
        @overload
        def AddTo(
            self,
            crow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
            imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
            hitID: int,
            resultsStore: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IResultsStore,
        ) -> None: ...
        @staticmethod
        def Compare(
            h1: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.LibrarySearch.HitItem,
            h2: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.LibrarySearch.HitItem,
        ) -> int: ...

class LibrarySearchMethodRowID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.LibrarySearchMethodRowID
    ],
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> None: ...

    BatchID: int  # readonly
    IdentificationMethodID: int  # readonly
    LibrarySearchMethodID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.LibrarySearchMethodRowID,
    ) -> int: ...
    @overload
    def Equals(
        self,
        rid: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.LibrarySearchMethodRowID,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class LibrarySearchType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AccurateMassPatternMatch: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.LibrarySearchType
    ) = ...  # static # readonly
    RetentionTimeMatch: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.LibrarySearchType
    ) = ...  # static # readonly
    SpectralSearch: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.LibrarySearchType
    ) = ...  # static # readonly

class MethodUtils:  # Class
    SingleFileExt: str = ...  # static # readonly

    @staticmethod
    def GetDefaultDeconvolutionMethods(list: List[Dict[str, Any]]) -> None: ...
    @staticmethod
    def GetTicAnalysisMS(ticAnalysisSignalType: str, scantype: MSScanType) -> bool: ...
    @staticmethod
    def GetTicAnalysisSignal(
        ticAnalysisSignalType: str, deviceName: str, ordinalNumber: int, signalName: str
    ) -> bool: ...
    @staticmethod
    def GetUnifiedMethodRelattivePath() -> str: ...
    @staticmethod
    def GetDefaultLibrarySearchMethods(list: List[Dict[str, Any]]) -> None: ...
    @staticmethod
    def GetDefaultMethod() -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet
    ): ...
    @staticmethod
    def FillDeconvolutionParameters(
        dmrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow,
        parameters: ComponentPerceptionParams,
    ) -> None: ...
    @staticmethod
    def FillExactifyParameters(
        imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
        parameters: ExactifyParams,
    ) -> None: ...
    @staticmethod
    def FillLibrarySearchParameters(
        imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
        lsmrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow,
        parameters: LibrarySearchParams,
    ) -> None: ...
    @staticmethod
    def GetDefaultBlankSubtractionMethod(values: Dict[str, Any]) -> None: ...
    @staticmethod
    def GetDefaultAuxiliaryMethod(values: Dict[str, Any]) -> None: ...
    @overload
    @staticmethod
    def GetTicAnalysisSignalType(type: MSScanType) -> str: ...
    @overload
    @staticmethod
    def GetTicAnalysisSignalType(
        deviceName: str, ordinalNumber: int, signalName: str
    ) -> str: ...
    @overload
    @staticmethod
    def LoadMethod(
        methodPath: str,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
    ) -> None: ...
    @overload
    @staticmethod
    def LoadMethod(
        stream: System.IO.Stream,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
    ) -> None: ...
    @staticmethod
    def SaveMethod(
        dataSet: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
        methodPath: str,
    ) -> None: ...
    @staticmethod
    def StringToDoubleRangeArray(
        value_: str, splitter: str, formatProvider: System.IFormatProvider
    ) -> List[DoubleRangeD]: ...
    @staticmethod
    def UnifiedMethodFilePath(dir: str) -> str: ...
    @staticmethod
    def DoubleRangeArrayToString(
        arr: List[DoubleRangeD], separator: str, formatProvider: System.IFormatProvider
    ) -> str: ...
    @staticmethod
    def CheckMethodFileExists(methodPath: str) -> bool: ...
    @staticmethod
    def GetDefaultIdentificationMethod(values: Dict[str, Any]) -> None: ...
    @staticmethod
    def GetDefaultTargetMatchMethod(values: Dict[str, Any]) -> None: ...

class MultiLibrarySearchType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    All: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.MultiLibrarySearchType
    ) = ...  # static # readonly
    StopWhenFirstFoundInFirstLibrary: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.MultiLibrarySearchType
    ) = ...  # static # readonly
    StopWhenFound: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.MultiLibrarySearchType
    ) = ...  # static # readonly

class PeakDetectionAlgorithm(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    FeatureDeconvolution: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.PeakDetectionAlgorithm
    ) = ...  # static # readonly
    SpectralDeconvolution: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.PeakDetectionAlgorithm
    ) = ...  # static # readonly
    TICAnalysis: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.PeakDetectionAlgorithm
    ) = ...  # static # readonly
    TargetDeconvolution: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.PeakDetectionAlgorithm
    ) = ...  # static # readonly

class PeakQualifierRowID(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        compoundID: int,
        qualifierID: int,
        peakID: int,
    ) -> None: ...

    BatchID: int  # readonly
    CompoundID: int  # readonly
    PeakID: int  # readonly
    QualifierID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.PeakQualifierRowID,
    ) -> int: ...
    @overload
    def Equals(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.PeakQualifierRowID,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class PeakRowID(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, compoundID: int, peakID: int
    ) -> None: ...

    BatchID: int  # readonly
    CompoundID: int  # readonly
    PeakID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self, other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.PeakRowID
    ) -> int: ...
    @overload
    def Equals(
        self, rowID: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.PeakRowID
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class ProgressEventArgs(System.EventArgs):  # Class
    def __init__(self, total: int, step: int, message: str) -> None: ...

    CurrentStep: int  # readonly
    Message: str  # readonly
    TotalSteps: int  # readonly

class RankPeakBy(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Area: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RankPeakBy = (
        ...
    )  # static # readonly
    Height: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RankPeakBy = (
        ...
    )  # static # readonly

class RetentionTimeMatch:  # Class
    def __init__(
        self,
        imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
        lsmrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow,
        library: ILibrary,
        rtCal: RTCalibrationTable,
    ) -> None: ...

    RTCalibrationTable: RTCalibrationTable  # readonly

    # Nested Types

    class HitItem:  # Class
        CompoundIndex: int  # readonly
        Library: ILibrary  # readonly
        LibraryRI: float  # readonly
        LibraryRT: float  # readonly
        LibrarySearchMethodRow: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        )  # readonly
        RTCalibrationTable: RTCalibrationTable  # readonly
        Score: float  # readonly
        TargetRI: float  # readonly

        def AddTo(
            self,
            hdt: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitDataTable,
            crow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
            imrow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
            hitID: int,
        ) -> None: ...

    class LibEntry:  # Class
        def __init__(
            self, index: int, rt: float, librt: float, libri: float
        ) -> None: ...

        Index: int  # readonly
        LibRI: float  # readonly
        LibRT: float  # readonly
        RT: float  # readonly

class RowID:  # Class
    def __init__(self) -> None: ...

class RowsEventArgs(System.EventArgs):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        rowIDs: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID
        ],
    ) -> None: ...

    RowIDs: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID
    ]  # readonly

class SampleRowID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
    ],
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
):  # Class
    def __init__(self, batchID: int, sampleID: int) -> None: ...

    BatchID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID,
    ) -> int: ...
    @overload
    def Equals(
        self, rid: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class TICAnalysis(System.IDisposable):  # Class
    def __init__(
        self,
        cancelEvent: System.Threading.WaitHandle,
        samplePath: str,
        compliance: ICompliance,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        resultsStore: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IResultsStore,
        reportProgress: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IReportProgress,
    ) -> None: ...
    @staticmethod
    def GetSignalChromatogram(
        da: IDataAccess,
        ordinalNumber: int,
        deviceName: str,
        signalName: str,
        min: Optional[float],
        max: Optional[float],
    ) -> IChromatogram: ...
    @staticmethod
    def GetEIC(
        ida: IDataAccess,
        mz: float,
        startX: float,
        endX: float,
        scanType: MSScanType,
        ionPolarity: IonPolarity,
        mzOfInterest: float,
        cpParams: ComponentPerceptionParams,
    ) -> IChromatogram: ...
    @staticmethod
    def GetTICAnalysisScanType(
        ida: IDataAccess, scanType: MSScanType
    ) -> MSScanType: ...
    @staticmethod
    def IsExcludedMZ(
        mz: float,
        leftMzDelta: float,
        rightMzDelta: float,
        excludedMZs: List[float],
        excludedMzRanges: List[DoubleRangeD],
    ) -> bool: ...
    @staticmethod
    def CreateDataAccess() -> IDataAccess: ...
    @staticmethod
    def GetSignals(ida: IDataAccess) -> List[Signal]: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def GetTIC(
        ida: IDataAccess,
        ionPolarity: IonPolarity,
        scanType: MSScanType,
        min: Optional[float],
        max: Optional[float],
    ) -> IChromatogram: ...
    def ProcessSample(self) -> None: ...

class TargetCompoundRowID(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID
):  # Class
    def __init__(self, batchID: int, sampleID: int, compoundID: int) -> None: ...

    BatchID: int  # readonly
    CompoundID: int  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.TargetCompoundRowID,
    ) -> int: ...
    @overload
    def Equals(
        self,
        tcrid: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.TargetCompoundRowID,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class TargetMatch:  # Class
    def __init__(
        self,
        cancelEvent: System.Threading.WaitHandle,
        dataset: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
        batchID: int,
        sampleID: int,
        targetMatchMethodID: int,
        reportProgress: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.IReportProgress,
    ) -> None: ...
    def ProcessSample(self) -> None: ...

    # Nested Types

    class IonPeakComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.TargetMatch.IonPeakItem
        ]
    ):  # Class
        def __init__(self, mz: float) -> None: ...

    class TargetCompoundComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.TargetMatch.TargetCompoundItem
        ]
    ):  # Class
        def __init__(
            self,
            method: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow,
            hit: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow,
        ) -> None: ...

class TargetMatchMethodRowID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.TargetMatchMethodRowID
    ],
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, targetMatchMethodID: int
    ) -> None: ...

    BatchID: int  # readonly
    SampleID: int  # readonly
    TargetMatchMethodID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.TargetMatchMethodRowID,
    ) -> int: ...
    @overload
    def Equals(
        self,
        rid: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.TargetMatchMethodRowID,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class TargetQualifierRowID(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, compoundId: int, qualifierID: int
    ) -> None: ...

    BatchID: int  # readonly
    CompoundID: int  # readonly
    QualifierID: int  # readonly
    SampleID: int  # readonly

    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.TargetQualifierRowID,
    ) -> int: ...

class UnknownsAnalysisCancelException(
    System.Runtime.InteropServices._Exception,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisException,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class UnknownsAnalysisDataSet(
    System.IDisposable,
    System.ComponentModel.ISupportInitializeNotification,
    System.IServiceProvider,
    System.Data.DataSet,
    System.Xml.Serialization.IXmlSerializable,
    System.Runtime.Serialization.ISerializable,
    System.ComponentModel.IListSource,
    System.ComponentModel.ISupportInitialize,
    System.ComponentModel.IComponent,
):  # Class
    def __init__(self) -> None: ...

    SchemaVersion: int  # static # readonly

    Analysis: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisDataTable
    )  # readonly
    AuxiliaryMethod: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodDataTable
    )  # readonly
    Batch: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchDataTable
    )  # readonly
    BlankSubtractionMethod: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodDataTable
    )  # readonly
    Component: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentDataTable
    )  # readonly
    DeconvolutionMethod: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodDataTable
    )  # readonly
    ExactMass: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassDataTable
    )  # readonly
    Hit: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitDataTable
    )  # readonly
    IdentificationMethod: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodDataTable
    )  # readonly
    IonPeak: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakDataTable
    )  # readonly
    LibrarySearchMethod: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodDataTable
    )  # readonly
    Peak: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakDataTable
    )  # readonly
    PeakQualifier: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierDataTable
    )  # readonly
    Relations: System.Data.DataRelationCollection  # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleDataTable
    )  # readonly
    SchemaSerializationMode: System.Data.SchemaSerializationMode
    Tables: System.Data.DataTableCollection  # readonly
    TargetCompound: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundDataTable
    )  # readonly
    TargetMatchMethod: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodDataTable
    )  # readonly
    TargetQualifier: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierDataTable
    )  # readonly

    @staticmethod
    def GetTypedDataSetSchema(
        xs: System.Xml.Schema.XmlSchemaSet,
    ) -> System.Xml.Schema.XmlSchemaComplexType: ...
    @staticmethod
    def StringToDoubleArray(
        value_: str, separator: str, formatProvider: System.IFormatProvider
    ) -> List[float]: ...
    @staticmethod
    def DoubleArrayToString(
        arr: List[float], separator: str, formatProvider: System.IFormatProvider
    ) -> str: ...
    def Clone(self) -> System.Data.DataSet: ...

    # Nested Types

    class AnalysisDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRow
        ],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRow
        ],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[Any],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AnalysisFileNameColumn: System.Data.DataColumn  # readonly
        AnalysisIDColumn: System.Data.DataColumn  # readonly
        AnalysisTimeColumn: System.Data.DataColumn  # readonly
        AnalystNameColumn: System.Data.DataColumn  # readonly
        AppVersionColumn: System.Data.DataColumn  # readonly
        BatchPathColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DataVersionColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRow
        ): ...
        ReportTimeColumn: System.Data.DataColumn  # readonly
        SchemaVersionColumn: System.Data.DataColumn  # readonly
        StoreResultsPerSampleColumn: System.Data.DataColumn  # readonly

        def FindByAnalysisID(
            self, AnalysisID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemoveAnalysisRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRow,
        ) -> None: ...
        def Clone(self) -> System.Data.DataTable: ...
        @overload
        def AddAnalysisRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRow,
        ) -> None: ...
        @overload
        def AddAnalysisRow(
            self,
            AnalysisID: int,
            SchemaVersion: int,
            AnalystName: str,
            AnalysisTime: System.DateTime,
            DataVersion: int,
            ReportTime: System.DateTime,
            StoreResultsPerSample: bool,
            AppVersion: str,
            BatchPath: str,
            AnalysisFileName: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRow
        ): ...
        def NewAnalysisRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRow
        ): ...

        AnalysisRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRowChangeEventHandler
        )  # Event
        AnalysisRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRowChangeEventHandler
        )  # Event
        AnalysisRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRowChangeEventHandler
        )  # Event
        AnalysisRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRowChangeEventHandler
        )  # Event

    class AnalysisRow(System.Data.DataRow):  # Class
        AnalysisFileName: str
        AnalysisID: int
        AnalysisTime: System.DateTime
        AnalystName: str
        AppVersion: str
        BatchPath: str
        DataVersion: int
        ReportTime: System.DateTime
        SchemaVersion: int
        StoreResultsPerSample: bool

        def IsAnalysisTimeNull(self) -> bool: ...
        def IsAnalystNameNull(self) -> bool: ...
        def IsAppVersionNull(self) -> bool: ...
        def SetAppVersionNull(self) -> None: ...
        def SetDataVersionNull(self) -> None: ...
        def SetAnalysisFileNameNull(self) -> None: ...
        def SetStoreResultsPerSampleNull(self) -> None: ...
        def IsBatchPathNull(self) -> bool: ...
        def SetAnalysisTimeNull(self) -> None: ...
        def IsReportTimeNull(self) -> bool: ...
        def SetAnalystNameNull(self) -> None: ...
        def SetReportTimeNull(self) -> None: ...
        def IsStoreResultsPerSampleNull(self) -> bool: ...
        def IsAnalysisFileNameNull(self) -> bool: ...
        def SetBatchPathNull(self) -> None: ...
        def IsDataVersionNull(self) -> bool: ...

    class AnalysisRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRow
        )  # readonly

    class AnalysisRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisRowChangeEvent,
        ) -> None: ...

    class AuxiliaryMethodDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        BatchIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow
        ): ...
        MZExtractIonsColumn: System.Data.DataColumn  # readonly
        MZExtractionWindowFilterLeftColumn: System.Data.DataColumn  # readonly
        MZExtractionWindowFilterRightColumn: System.Data.DataColumn  # readonly
        MZExtractionWindowUnitsColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly

        def NewAuxiliaryMethodRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow
        ): ...
        def RemoveAuxiliaryMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByBatchIDSampleID(
            self, BatchID: int, SampleID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        @overload
        def AddAuxiliaryMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow,
        ) -> None: ...
        @overload
        def AddAuxiliaryMethodRow(
            self,
            BatchID: int,
            SampleID: int,
            MZExtractIons: str,
            MZExtractionWindowFilterLeft: float,
            MZExtractionWindowFilterRight: float,
            MZExtractionWindowUnits: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow
        ): ...

        AuxiliaryMethodRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRowChangeEventHandler
        )  # Event
        AuxiliaryMethodRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRowChangeEventHandler
        )  # Event
        AuxiliaryMethodRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRowChangeEventHandler
        )  # Event
        AuxiliaryMethodRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRowChangeEventHandler
        )  # Event

    class AuxiliaryMethodRow(System.Data.DataRow):  # Class
        BatchID: int
        MZExtractIons: str
        MZExtractionWindowFilterLeft: float
        MZExtractionWindowFilterRight: float
        MZExtractionWindowUnits: str
        SampleID: int
        SampleRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        )

        def SetMZExtractionWindowUnitsNull(self) -> None: ...
        def IsMZExtractionWindowUnitsNull(self) -> bool: ...
        def SetMZExtractionWindowFilterRightNull(self) -> None: ...
        def SetMZExtractionWindowFilterLeftNull(self) -> None: ...
        def IsMZExtractIonsNull(self) -> bool: ...
        def SetMZExtractIonsNull(self) -> None: ...
        def IsMZExtractionWindowFilterLeftNull(self) -> bool: ...
        def IsMZExtractionWindowFilterRightNull(self) -> bool: ...

    class AuxiliaryMethodRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow
        )  # readonly

    class AuxiliaryMethodRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRowChangeEvent,
        ) -> None: ...

    class BatchDataTable(
        System.ComponentModel.IListSource,
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow
        ],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow
        ],
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AnalysisTimeStampColumn: System.Data.DataColumn  # readonly
        AnalystNameColumn: System.Data.DataColumn  # readonly
        AnalyzeQuantVersionColumn: System.Data.DataColumn  # readonly
        AppSchemaVersionColumn: System.Data.DataColumn  # readonly
        ApplyMultiplierISTDColumn: System.Data.DataColumn  # readonly
        ApplyMultiplierMatrixSpikeColumn: System.Data.DataColumn  # readonly
        ApplyMultiplierSurrogateColumn: System.Data.DataColumn  # readonly
        ApplyMultiplierTargetColumn: System.Data.DataColumn  # readonly
        AuditTrailColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        BatchStateColumn: System.Data.DataColumn  # readonly
        BracketingTypeColumn: System.Data.DataColumn  # readonly
        CCMaximumElapsedTimeInHoursColumn: System.Data.DataColumn  # readonly
        CalibrationLastUpdatedTimeStampColumn: System.Data.DataColumn  # readonly
        CorrelationWindowColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DAMethodLastAppliedTimeStampColumn: System.Data.DataColumn  # readonly
        DAMethodPathFileNameOriginColumn: System.Data.DataColumn  # readonly
        DataVersionColumn: System.Data.DataColumn  # readonly
        DynamicBackgroundSubtractionColumn: System.Data.DataColumn  # readonly
        FeatureDetectionColumn: System.Data.DataColumn  # readonly
        IgnorePeaksNotFoundColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow
        ): ...
        LibraryMethodPathFileNameColumn: System.Data.DataColumn  # readonly
        NonReferenceWindowColumn: System.Data.DataColumn  # readonly
        NonReferenceWindowPercentOrMinutesColumn: System.Data.DataColumn  # readonly
        RefLibraryPathFileNameColumn: System.Data.DataColumn  # readonly
        RefLibraryPatternPathFileNameColumn: System.Data.DataColumn  # readonly
        ReferencePatternLibraryPathFileNameColumn: System.Data.DataColumn  # readonly
        ReferenceWindowColumn: System.Data.DataColumn  # readonly
        ReferenceWindowPercentOrMinutesColumn: System.Data.DataColumn  # readonly
        RelativeISTDColumn: System.Data.DataColumn  # readonly
        SchemaVersionColumn: System.Data.DataColumn  # readonly
        StandardAdditionColumn: System.Data.DataColumn  # readonly
        TargetBatchDataPathColumn: System.Data.DataColumn  # readonly
        TargetBatchFileNameColumn: System.Data.DataColumn  # readonly

        def RemoveBatchRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddBatchRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow,
        ) -> None: ...
        @overload
        def AddBatchRow(
            self,
            BatchID: int,
            TargetBatchDataPath: str,
            TargetBatchFileName: str,
            AppSchemaVersion: int,
            SchemaVersion: int,
            DataVersion: int,
            BatchState: str,
            AnalystName: str,
            AnalysisTimeStamp: System.DateTime,
            FeatureDetection: bool,
            ReferenceWindow: float,
            ReferenceWindowPercentOrMinutes: str,
            NonReferenceWindow: float,
            NonReferenceWindowPercentOrMinutes: str,
            CorrelationWindow: float,
            ApplyMultiplierTarget: bool,
            ApplyMultiplierSurrogate: bool,
            ApplyMultiplierISTD: bool,
            ApplyMultiplierMatrixSpike: bool,
            IgnorePeaksNotFound: bool,
            RelativeISTD: bool,
            AuditTrail: bool,
            RefLibraryPathFileName: str,
            RefLibraryPatternPathFileName: str,
            LibraryMethodPathFileName: str,
            ReferencePatternLibraryPathFileName: str,
            CCMaximumElapsedTimeInHours: float,
            BracketingType: str,
            StandardAddition: bool,
            DynamicBackgroundSubtraction: bool,
            DAMethodPathFileNameOrigin: str,
            DAMethodLastAppliedTimeStamp: System.DateTime,
            CalibrationLastUpdatedTimeStamp: System.DateTime,
            AnalyzeQuantVersion: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow
        ): ...
        def NewBatchRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def FindByBatchID(
            self, BatchID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow
        ): ...

        BatchRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRowChangeEventHandler
        )  # Event
        BatchRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRowChangeEventHandler
        )  # Event
        BatchRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRowChangeEventHandler
        )  # Event
        BatchRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRowChangeEventHandler
        )  # Event

    class BatchRow(System.Data.DataRow):  # Class
        AnalysisTimeStamp: System.DateTime
        AnalystName: str
        AnalyzeQuantVersion: str
        AppSchemaVersion: int
        ApplyMultiplierISTD: bool
        ApplyMultiplierMatrixSpike: bool
        ApplyMultiplierSurrogate: bool
        ApplyMultiplierTarget: bool
        AuditTrail: bool
        BatchID: int
        BatchState: str
        BracketingType: str
        CCMaximumElapsedTimeInHours: float
        CalibrationLastUpdatedTimeStamp: System.DateTime
        CorrelationWindow: float
        DAMethodLastAppliedTimeStamp: System.DateTime
        DAMethodPathFileNameOrigin: str
        DataVersion: int
        DynamicBackgroundSubtraction: bool
        FeatureDetection: bool
        IgnorePeaksNotFound: bool
        LibraryMethodPathFileName: str
        NonReferenceWindow: float
        NonReferenceWindowPercentOrMinutes: str
        RefLibraryPathFileName: str
        RefLibraryPatternPathFileName: str
        ReferencePatternLibraryPathFileName: str
        ReferenceWindow: float
        ReferenceWindowPercentOrMinutes: str
        RelativeISTD: bool
        SchemaVersion: int
        StandardAddition: bool
        TargetBatchDataPath: str
        TargetBatchFileName: str

        def SetApplyMultiplierISTDNull(self) -> None: ...
        def SetAuditTrailNull(self) -> None: ...
        def SetDataVersionNull(self) -> None: ...
        def SetNonReferenceWindowNull(self) -> None: ...
        def SetAnalyzeQuantVersionNull(self) -> None: ...
        def SetApplyMultiplierTargetNull(self) -> None: ...
        def IsTargetBatchDataPathNull(self) -> bool: ...
        def SetReferenceWindowPercentOrMinutesNull(self) -> None: ...
        def SetReferenceWindowNull(self) -> None: ...
        def SetAppSchemaVersionNull(self) -> None: ...
        def SetTargetBatchDataPathNull(self) -> None: ...
        def SetDAMethodPathFileNameOriginNull(self) -> None: ...
        def IsAnalysisTimeStampNull(self) -> bool: ...
        def IsIgnorePeaksNotFoundNull(self) -> bool: ...
        def IsApplyMultiplierISTDNull(self) -> bool: ...
        def SetFeatureDetectionNull(self) -> None: ...
        def IsRelativeISTDNull(self) -> bool: ...
        def IsTargetBatchFileNameNull(self) -> bool: ...
        def SetReferencePatternLibraryPathFileNameNull(self) -> None: ...
        def SetAnalysisTimeStampNull(self) -> None: ...
        def IsCCMaximumElapsedTimeInHoursNull(self) -> bool: ...
        def IsAnalyzeQuantVersionNull(self) -> bool: ...
        def SetStandardAdditionNull(self) -> None: ...
        def IsAppSchemaVersionNull(self) -> bool: ...
        def SetDynamicBackgroundSubtractionNull(self) -> None: ...
        def SetIgnorePeaksNotFoundNull(self) -> None: ...
        def SetRefLibraryPatternPathFileNameNull(self) -> None: ...
        def SetApplyMultiplierSurrogateNull(self) -> None: ...
        def SetSchemaVersionNull(self) -> None: ...
        def SetNonReferenceWindowPercentOrMinutesNull(self) -> None: ...
        def IsBracketingTypeNull(self) -> bool: ...
        def IsDynamicBackgroundSubtractionNull(self) -> bool: ...
        def IsCalibrationLastUpdatedTimeStampNull(self) -> bool: ...
        def SetRefLibraryPathFileNameNull(self) -> None: ...
        def IsRefLibraryPathFileNameNull(self) -> bool: ...
        def IsApplyMultiplierSurrogateNull(self) -> bool: ...
        def IsReferenceWindowPercentOrMinutesNull(self) -> bool: ...
        def SetAnalystNameNull(self) -> None: ...
        def IsAnalystNameNull(self) -> bool: ...
        def IsAuditTrailNull(self) -> bool: ...
        def IsDAMethodLastAppliedTimeStampNull(self) -> bool: ...
        def IsLibraryMethodPathFileNameNull(self) -> bool: ...
        def SetCorrelationWindowNull(self) -> None: ...
        def GetSampleRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        ]: ...
        def IsCorrelationWindowNull(self) -> bool: ...
        def IsBatchStateNull(self) -> bool: ...
        def SetApplyMultiplierMatrixSpikeNull(self) -> None: ...
        def SetBatchStateNull(self) -> None: ...
        def IsDAMethodPathFileNameOriginNull(self) -> bool: ...
        def SetBracketingTypeNull(self) -> None: ...
        def IsApplyMultiplierTargetNull(self) -> bool: ...
        def IsReferencePatternLibraryPathFileNameNull(self) -> bool: ...
        def SetDAMethodLastAppliedTimeStampNull(self) -> None: ...
        def IsDataVersionNull(self) -> bool: ...
        def IsNonReferenceWindowPercentOrMinutesNull(self) -> bool: ...
        def SetCCMaximumElapsedTimeInHoursNull(self) -> None: ...
        def IsReferenceWindowNull(self) -> bool: ...
        def IsRefLibraryPatternPathFileNameNull(self) -> bool: ...
        def IsSchemaVersionNull(self) -> bool: ...
        def IsStandardAdditionNull(self) -> bool: ...
        def SetLibraryMethodPathFileNameNull(self) -> None: ...
        def SetRelativeISTDNull(self) -> None: ...
        def SetTargetBatchFileNameNull(self) -> None: ...
        def SetCalibrationLastUpdatedTimeStampNull(self) -> None: ...
        def IsApplyMultiplierMatrixSpikeNull(self) -> bool: ...
        def IsFeatureDetectionNull(self) -> bool: ...
        def IsNonReferenceWindowNull(self) -> bool: ...

    class BatchRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow
        )  # readonly

    class BatchRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRowChangeEvent,
        ) -> None: ...

    class BlankSubtractionMethodDataTable(
        System.ComponentModel.ISupportInitialize,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow
        ],
        Iterable[Any],
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow
        ],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        BatchIDColumn: System.Data.DataColumn  # readonly
        BlankSubtractionMethodIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow
        ): ...
        PeakThresholdColumn: System.Data.DataColumn  # readonly
        PeakThresholdTypeColumn: System.Data.DataColumn  # readonly
        PerformBlankSubtractionColumn: System.Data.DataColumn  # readonly
        RTWindowColumn: System.Data.DataColumn  # readonly
        RTWindowFWHMColumn: System.Data.DataColumn  # readonly
        RTWindowTypeColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly

        def NewBlankSubtractionMethodRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow
        ): ...
        def FindByBatchIDSampleIDBlankSubtractionMethodID(
            self, BatchID: int, SampleID: int, BlankSubtractionMethodID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemoveBlankSubtractionMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow,
        ) -> None: ...
        def Clone(self) -> System.Data.DataTable: ...
        @overload
        def AddBlankSubtractionMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow,
        ) -> None: ...
        @overload
        def AddBlankSubtractionMethodRow(
            self,
            BatchID: int,
            SampleID: int,
            BlankSubtractionMethodID: int,
            PerformBlankSubtraction: bool,
            PeakThresholdType: str,
            PeakThreshold: float,
            RTWindowType: str,
            RTWindow: float,
            RTWindowFWHM: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow
        ): ...

        BlankSubtractionMethodRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRowChangeEventHandler
        )  # Event
        BlankSubtractionMethodRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRowChangeEventHandler
        )  # Event
        BlankSubtractionMethodRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRowChangeEventHandler
        )  # Event
        BlankSubtractionMethodRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRowChangeEventHandler
        )  # Event

    class BlankSubtractionMethodRow(System.Data.DataRow):  # Class
        BatchID: int
        BlankSubtractionMethodID: int
        PeakThreshold: float
        PeakThresholdType: str
        PerformBlankSubtraction: bool
        RTWindow: float
        RTWindowFWHM: float
        RTWindowType: str
        SampleID: int
        SampleRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        )

        def IsPerformBlankSubtractionNull(self) -> bool: ...
        def SetRTWindowNull(self) -> None: ...
        def SetRTWindowTypeNull(self) -> None: ...
        def SetPerformBlankSubtractionNull(self) -> None: ...
        def SetRTWindowFWHMNull(self) -> None: ...
        def IsPeakThresholdNull(self) -> bool: ...
        def IsRTWindowFWHMNull(self) -> bool: ...
        def SetPeakThresholdTypeNull(self) -> None: ...
        def IsRTWindowTypeNull(self) -> bool: ...
        def IsRTWindowNull(self) -> bool: ...
        def SetPeakThresholdNull(self) -> None: ...
        def IsPeakThresholdTypeNull(self) -> bool: ...

    class BlankSubtractionMethodRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow
        )  # readonly

    class BlankSubtractionMethodRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRowChangeEvent,
        ) -> None: ...

    class ComponentDataTable(
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
        ],
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AreaColumn: System.Data.DataColumn  # readonly
        AreaPercentColumn: System.Data.DataColumn  # readonly
        AreaPercentMaxColumn: System.Data.DataColumn  # readonly
        BasePeakIDColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        BestHitColumn: System.Data.DataColumn  # readonly
        BestHitOverriddenColumn: System.Data.DataColumn  # readonly
        ComponentIDColumn: System.Data.DataColumn  # readonly
        ComponentNameColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DeconvolutedHeightColumn: System.Data.DataColumn  # readonly
        DeconvolutionMethodIDColumn: System.Data.DataColumn  # readonly
        EndXColumn: System.Data.DataColumn  # readonly
        GraphicsComponentSpectrumColumn: System.Data.DataColumn  # readonly
        HeightColumn: System.Data.DataColumn  # readonly
        IsAccurateMassColumn: System.Data.DataColumn  # readonly
        IsBackgroundSubtractedColumn: System.Data.DataColumn  # readonly
        IsManuallyIntegratedColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
        ): ...
        ModelIonPeakIDColumn: System.Data.DataColumn  # readonly
        PrimaryHitIDColumn: System.Data.DataColumn  # readonly
        RetentionIndexColumn: System.Data.DataColumn  # readonly
        RetentionTimeColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        ShapeQualityColumn: System.Data.DataColumn  # readonly
        SpectrumAbundancesColumn: System.Data.DataColumn  # readonly
        SpectrumMZsColumn: System.Data.DataColumn  # readonly
        StartXColumn: System.Data.DataColumn  # readonly
        TargetedDeconvolution_IdentificationMethodIDColumn: (
            System.Data.DataColumn
        )  # readonly
        TargetedDeconvolution_LibraryEntryIDColumn: System.Data.DataColumn  # readonly
        TargetedDeconvolution_LibrarySearchMethodIDColumn: (
            System.Data.DataColumn
        )  # readonly
        UserCustomCalculationColumn: System.Data.DataColumn  # readonly
        UserDefinedColumn: System.Data.DataColumn  # readonly
        VisibleColumn: System.Data.DataColumn  # readonly
        XArrayColumn: System.Data.DataColumn  # readonly
        YArrayColumn: System.Data.DataColumn  # readonly

        def FindByBatchIDSampleIDDeconvolutionMethodIDComponentID(
            self,
            BatchID: int,
            SampleID: int,
            DeconvolutionMethodID: int,
            ComponentID: int,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
        ): ...
        def RemoveComponentRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewComponentRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
        ): ...
        @overload
        def AddComponentRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
        ) -> None: ...
        @overload
        def AddComponentRow(
            self,
            BatchID: int,
            SampleID: int,
            DeconvolutionMethodID: int,
            ComponentID: int,
            PrimaryHitID: int,
            ModelIonPeakID: int,
            ComponentName: str,
            BasePeakID: int,
            IsManuallyIntegrated: bool,
            IsBackgroundSubtracted: bool,
            BestHit: bool,
            BestHitOverridden: bool,
            Area: float,
            EndX: float,
            Height: float,
            IsAccurateMass: bool,
            RetentionTime: float,
            RetentionIndex: float,
            SpectrumAbundances: str,
            SpectrumMZs: str,
            StartX: float,
            XArray: str,
            YArray: str,
            ShapeQuality: float,
            DeconvolutedHeight: float,
            AreaPercent: float,
            AreaPercentMax: float,
            Visible: bool,
            UserDefined: str,
            UserCustomCalculation: float,
            GraphicsComponentSpectrum: str,
            TargetedDeconvolution_IdentificationMethodID: int,
            TargetedDeconvolution_LibrarySearchMethodID: int,
            TargetedDeconvolution_LibraryEntryID: int,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...

        ComponentRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRowChangeEventHandler
        )  # Event
        ComponentRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRowChangeEventHandler
        )  # Event
        ComponentRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRowChangeEventHandler
        )  # Event
        ComponentRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRowChangeEventHandler
        )  # Event

    class ComponentRow(System.Data.DataRow):  # Class
        Area: float
        AreaPercent: float
        AreaPercentMax: float
        BasePeakID: int
        BatchID: int
        BestHit: bool
        BestHitOverridden: bool
        ComponentID: int
        ComponentName: str
        DeconvolutedHeight: float
        DeconvolutionMethodID: int
        DeconvolutionMethodRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow
        )
        EndX: float
        GraphicsComponentSpectrum: str
        Height: float
        IsAccurateMass: bool
        IsBackgroundSubtracted: bool
        IsManuallyIntegrated: bool
        ModelIonPeakID: int
        PrimaryHitID: int
        RetentionIndex: float
        RetentionTime: float
        SampleID: int
        ShapeQuality: float
        SpectrumAbundances: str
        SpectrumMZs: str
        StartX: float
        TargetedDeconvolution_IdentificationMethodID: int
        TargetedDeconvolution_LibraryEntryID: int
        TargetedDeconvolution_LibrarySearchMethodID: int
        UserCustomCalculation: float
        UserDefined: str
        Visible: bool
        XArray: str
        YArray: str

        def IsSpectrumAbundancesNull(self) -> bool: ...
        def IsRetentionIndexNull(self) -> bool: ...
        def IsTargetedDeconvolution_LibrarySearchMethodIDNull(self) -> bool: ...
        def IsTargetedDeconvolution_LibraryEntryIDNull(self) -> bool: ...
        def IsVisibleNull(self) -> bool: ...
        def SetBestHitOverriddenNull(self) -> None: ...
        def SetIsManuallyIntegratedNull(self) -> None: ...
        def IsIsAccurateMassNull(self) -> bool: ...
        def SetShapeQualityNull(self) -> None: ...
        def SetUserDefinedNull(self) -> None: ...
        def IsHeightNull(self) -> bool: ...
        def SetDeconvolutedHeightNull(self) -> None: ...
        def SetSpectrumAbundancesNull(self) -> None: ...
        def SetTargetedDeconvolution_LibraryEntryIDNull(self) -> None: ...
        def IsXArrayNull(self) -> bool: ...
        def SetVisibleNull(self) -> None: ...
        def IsAreaNull(self) -> bool: ...
        def IsGraphicsComponentSpectrumNull(self) -> bool: ...
        def IsIsBackgroundSubtractedNull(self) -> bool: ...
        def GetIonPeakRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow
        ]: ...
        def IsRetentionTimeNull(self) -> bool: ...
        def IsComponentNameNull(self) -> bool: ...
        def IsEndXNull(self) -> bool: ...
        def SetTargetedDeconvolution_IdentificationMethodIDNull(self) -> None: ...
        def IsUserCustomCalculationNull(self) -> bool: ...
        def IsSpectrumMZsNull(self) -> bool: ...
        def GetHitRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow
        ]: ...
        def SetModelIonPeakIDNull(self) -> None: ...
        def SetRetentionIndexNull(self) -> None: ...
        def SetGraphicsComponentSpectrumNull(self) -> None: ...
        def SetUserCustomCalculationNull(self) -> None: ...
        def SetSpectrumMZsNull(self) -> None: ...
        def SetTargetedDeconvolution_LibrarySearchMethodIDNull(self) -> None: ...
        def SetIsBackgroundSubtractedNull(self) -> None: ...
        def IsBestHitOverriddenNull(self) -> bool: ...
        def SetHeightNull(self) -> None: ...
        def SetYArrayNull(self) -> None: ...
        def IsPrimaryHitIDNull(self) -> bool: ...
        def SetIsAccurateMassNull(self) -> None: ...
        def IsAreaPercentNull(self) -> bool: ...
        def IsIsManuallyIntegratedNull(self) -> bool: ...
        def SetComponentNameNull(self) -> None: ...
        def SetRetentionTimeNull(self) -> None: ...
        def IsDeconvolutedHeightNull(self) -> bool: ...
        def SetXArrayNull(self) -> None: ...
        def SetAreaPercentNull(self) -> None: ...
        def IsAreaPercentMaxNull(self) -> bool: ...
        def IsShapeQualityNull(self) -> bool: ...
        def IsTargetedDeconvolution_IdentificationMethodIDNull(self) -> bool: ...
        def IsBasePeakIDNull(self) -> bool: ...
        def IsYArrayNull(self) -> bool: ...
        def IsModelIonPeakIDNull(self) -> bool: ...
        def IsStartXNull(self) -> bool: ...
        def SetAreaPercentMaxNull(self) -> None: ...
        def SetAreaNull(self) -> None: ...
        def SetEndXNull(self) -> None: ...
        def IsUserDefinedNull(self) -> bool: ...
        def SetPrimaryHitIDNull(self) -> None: ...
        def SetBasePeakIDNull(self) -> None: ...
        def SetStartXNull(self) -> None: ...
        def IsBestHitNull(self) -> bool: ...
        def SetBestHitNull(self) -> None: ...

    class ComponentRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
        )  # readonly

    class ComponentRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRowChangeEvent,
        ) -> None: ...

    class DeconvolutionMethodDataTable(
        System.IServiceProvider,
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow
        ],
        System.IDisposable,
    ):  # Class
        def __init__(self) -> None: ...

        AlgorithmColumn: System.Data.DataColumn  # readonly
        AreaFilterAbsoluteColumn: System.Data.DataColumn  # readonly
        AreaFilterRelativeColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        ChromPeakThresholdColumn: System.Data.DataColumn  # readonly
        ChromRangeHighColumn: System.Data.DataColumn  # readonly
        ChromRangeLowColumn: System.Data.DataColumn  # readonly
        ChromSNRThresholdColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DeconvolutionMethodIDColumn: System.Data.DataColumn  # readonly
        EICPeakThresholdColumn: System.Data.DataColumn  # readonly
        EICSNRThresholdColumn: System.Data.DataColumn  # readonly
        ExcludedMZsColumn: System.Data.DataColumn  # readonly
        HeightFilterAbsoluteColumn: System.Data.DataColumn  # readonly
        HeightFilterRelativeColumn: System.Data.DataColumn  # readonly
        IntegratorColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow
        ): ...
        LargestPeaksRankedByColumn: System.Data.DataColumn  # readonly
        LeftMZDeltaColumn: System.Data.DataColumn  # readonly
        MZDeltaUnitsColumn: System.Data.DataColumn  # readonly
        MaxNumPeaksColumn: System.Data.DataColumn  # readonly
        MaxNumStoredIonPeaksColumn: System.Data.DataColumn  # readonly
        MaxSpectrumPeaksPerChromPeakColumn: System.Data.DataColumn  # readonly
        MinNumPeaksColumn: System.Data.DataColumn  # readonly
        MinShapeQualityColumn: System.Data.DataColumn  # readonly
        ModelShapePercentileColumn: System.Data.DataColumn  # readonly
        RefineComponentsColumn: System.Data.DataColumn  # readonly
        RetentionTimeBinSizeColumn: System.Data.DataColumn  # readonly
        RightMZDeltaColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        ScreeningColumn: System.Data.DataColumn  # readonly
        SpectrumPeakThresholdColumn: System.Data.DataColumn  # readonly
        TICAnalysisColumn: System.Data.DataColumn  # readonly
        TICAnalysisSignalTypeColumn: System.Data.DataColumn  # readonly
        TargetedDeconvolutionColumn: System.Data.DataColumn  # readonly
        UseAreaFilterAbsoluteColumn: System.Data.DataColumn  # readonly
        UseAreaFilterRelativeColumn: System.Data.DataColumn  # readonly
        UseHeightFilterAbsoluteColumn: System.Data.DataColumn  # readonly
        UseHeightFilterRelativeColumn: System.Data.DataColumn  # readonly
        UseIntegerMZValuesColumn: System.Data.DataColumn  # readonly
        UseLargestPeakShapeColumn: System.Data.DataColumn  # readonly
        WindowSizeFactorColumn: System.Data.DataColumn  # readonly

        def NewDeconvolutionMethodRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddDeconvolutionMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow,
        ) -> None: ...
        @overload
        def AddDeconvolutionMethodRow(
            self,
            BatchID: int,
            SampleID: int,
            DeconvolutionMethodID: int,
            Algorithm: str,
            ChromRangeHigh: float,
            ChromRangeLow: float,
            EICPeakThreshold: float,
            EICSNRThreshold: float,
            ExcludedMZs: str,
            LeftMZDelta: float,
            ModelShapePercentile: float,
            MZDeltaUnits: str,
            RetentionTimeBinSize: float,
            RightMZDelta: float,
            UseIntegerMZValues: bool,
            MaxSpectrumPeaksPerChromPeak: int,
            SpectrumPeakThreshold: float,
            UseLargestPeakShape: bool,
            WindowSizeFactor: float,
            TICAnalysis: bool,
            ChromPeakThreshold: float,
            ChromSNRThreshold: float,
            UseAreaFilterAbsolute: bool,
            AreaFilterAbsolute: float,
            UseAreaFilterRelative: bool,
            AreaFilterRelative: float,
            UseHeightFilterAbsolute: bool,
            HeightFilterAbsolute: float,
            UseHeightFilterRelative: bool,
            HeightFilterRelative: float,
            MaxNumPeaks: int,
            LargestPeaksRankedBy: str,
            RefineComponents: bool,
            MaxNumStoredIonPeaks: int,
            Integrator: str,
            Screening: bool,
            TargetedDeconvolution: bool,
            MinShapeQuality: float,
            MinNumPeaks: int,
            TICAnalysisSignalType: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow
        ): ...
        def FindByBatchIDSampleIDDeconvolutionMethodID(
            self, BatchID: int, SampleID: int, DeconvolutionMethodID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveDeconvolutionMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow,
        ) -> None: ...

        DeconvolutionMethodRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRowChangeEventHandler
        )  # Event
        DeconvolutionMethodRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRowChangeEventHandler
        )  # Event
        DeconvolutionMethodRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRowChangeEventHandler
        )  # Event
        DeconvolutionMethodRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRowChangeEventHandler
        )  # Event

    class DeconvolutionMethodRow(System.Data.DataRow):  # Class
        Algorithm: str
        AreaFilterAbsolute: float
        AreaFilterRelative: float
        BatchID: int
        ChromPeakThreshold: float
        ChromRangeHigh: float
        ChromRangeLow: float
        ChromSNRThreshold: float
        DeconvolutionMethodID: int
        EICPeakThreshold: float
        EICSNRThreshold: float
        ExcludedMZs: str
        HeightFilterAbsolute: float
        HeightFilterRelative: float
        Integrator: str
        LargestPeaksRankedBy: str
        LeftMZDelta: float
        MZDeltaUnits: str
        MaxNumPeaks: int
        MaxNumStoredIonPeaks: int
        MaxSpectrumPeaksPerChromPeak: int
        MinNumPeaks: int
        MinShapeQuality: float
        ModelShapePercentile: float
        RefineComponents: bool
        RetentionTimeBinSize: float
        RightMZDelta: float
        SampleID: int
        SampleRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        )
        Screening: bool
        SpectrumPeakThreshold: float
        TICAnalysis: bool
        TICAnalysisSignalType: str
        TargetedDeconvolution: bool
        UseAreaFilterAbsolute: bool
        UseAreaFilterRelative: bool
        UseHeightFilterAbsolute: bool
        UseHeightFilterRelative: bool
        UseIntegerMZValues: bool
        UseLargestPeakShape: bool
        WindowSizeFactor: float

        def SetMaxNumStoredIonPeaksNull(self) -> None: ...
        def IsMaxNumStoredIonPeaksNull(self) -> bool: ...
        def SetHeightFilterRelativeNull(self) -> None: ...
        def SetTargetedDeconvolutionNull(self) -> None: ...
        def IsHeightFilterAbsoluteNull(self) -> bool: ...
        def SetTICAnalysisNull(self) -> None: ...
        def SetUseAreaFilterRelativeNull(self) -> None: ...
        def IsHeightFilterRelativeNull(self) -> bool: ...
        def IsAreaFilterAbsoluteNull(self) -> bool: ...
        def SetChromRangeLowNull(self) -> None: ...
        def SetUseHeightFilterRelativeNull(self) -> None: ...
        def SetLargestPeaksRankedByNull(self) -> None: ...
        def SetAlgorithmNull(self) -> None: ...
        def SetTICAnalysisSignalTypeNull(self) -> None: ...
        def SetIntegratorNull(self) -> None: ...
        def IsRefineComponentsNull(self) -> bool: ...
        def IsScreeningNull(self) -> bool: ...
        def SetUseIntegerMZValuesNull(self) -> None: ...
        def IsMaxNumPeaksNull(self) -> bool: ...
        def IsUseAreaFilterRelativeNull(self) -> bool: ...
        def IsTICAnalysisNull(self) -> bool: ...
        def IsUseIntegerMZValuesNull(self) -> bool: ...
        def SetMinShapeQualityNull(self) -> None: ...
        def SetChromRangeHighNull(self) -> None: ...
        def SetRefineComponentsNull(self) -> None: ...
        def IsMinNumPeaksNull(self) -> bool: ...
        def IsAlgorithmNull(self) -> bool: ...
        def IsLargestPeaksRankedByNull(self) -> bool: ...
        def SetAreaFilterRelativeNull(self) -> None: ...
        def IsUseAreaFilterAbsoluteNull(self) -> bool: ...
        def SetMinNumPeaksNull(self) -> None: ...
        def IsTargetedDeconvolutionNull(self) -> bool: ...
        def SetUseAreaFilterAbsoluteNull(self) -> None: ...
        def SetUseHeightFilterAbsoluteNull(self) -> None: ...
        def IsAreaFilterRelativeNull(self) -> bool: ...
        def IsMinShapeQualityNull(self) -> bool: ...
        def GetAlgorithm(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.PeakDetectionAlgorithm
        ): ...
        def IsIntegratorNull(self) -> bool: ...
        def SetScreeningNull(self) -> None: ...
        def IsTICAnalysisSignalTypeNull(self) -> bool: ...
        def IsUseHeightFilterAbsoluteNull(self) -> bool: ...
        def SetMaxNumPeaksNull(self) -> None: ...
        def IsChromRangeHighNull(self) -> bool: ...
        def SetAreaFilterAbsoluteNull(self) -> None: ...
        def SetHeightFilterAbsoluteNull(self) -> None: ...
        def IsChromRangeLowNull(self) -> bool: ...
        def IsUseHeightFilterRelativeNull(self) -> bool: ...
        def GetComponentRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
        ]: ...
        def SetExcludedMZsNull(self) -> None: ...
        def IsExcludedMZsNull(self) -> bool: ...

    class DeconvolutionMethodRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow
        )  # readonly

    class DeconvolutionMethodRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRowChangeEvent,
        ) -> None: ...

    class ExactMassDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AbundanceColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        ChargeColumn: System.Data.DataColumn  # readonly
        ComponentIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DeconvolutionMethodIDColumn: System.Data.DataColumn  # readonly
        ExactMassIDColumn: System.Data.DataColumn  # readonly
        FragmentFormulaColumn: System.Data.DataColumn  # readonly
        HitIDColumn: System.Data.DataColumn  # readonly
        IsUniqueColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRow
        ): ...
        MassDeltaMdaColumn: System.Data.DataColumn  # readonly
        MassDeltaPpmColumn: System.Data.DataColumn  # readonly
        MassExactColumn: System.Data.DataColumn  # readonly
        MassSourceColumn: System.Data.DataColumn  # readonly
        RelativeAbundanceColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByBatchIDSampleIDDeconvolutionMethodIDComponentIDHitIDExactMassID(
            self,
            BatchID: int,
            SampleID: int,
            DeconvolutionMethodID: int,
            ComponentID: int,
            HitID: int,
            ExactMassID: int,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRow
        ): ...
        def RemoveExactMassRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRow,
        ) -> None: ...
        def Clone(self) -> System.Data.DataTable: ...
        @overload
        def AddExactMassRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRow,
        ) -> None: ...
        @overload
        def AddExactMassRow(
            self,
            BatchID: int,
            SampleID: int,
            DeconvolutionMethodID: int,
            ComponentID: int,
            HitID: int,
            ExactMassID: int,
            MassSource: float,
            MassExact: float,
            MassDeltaPpm: float,
            MassDeltaMda: float,
            FragmentFormula: str,
            Abundance: float,
            RelativeAbundance: float,
            Charge: int,
            IsUnique: bool,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRow
        ): ...
        def NewExactMassRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRow
        ): ...

        ExactMassRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRowChangeEventHandler
        )  # Event
        ExactMassRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRowChangeEventHandler
        )  # Event
        ExactMassRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRowChangeEventHandler
        )  # Event
        ExactMassRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRowChangeEventHandler
        )  # Event

    class ExactMassRow(System.Data.DataRow):  # Class
        Abundance: float
        BatchID: int
        Charge: int
        ComponentID: int
        DeconvolutionMethodID: int
        ExactMassID: int
        FragmentFormula: str
        HitID: int
        IsUnique: bool
        MassDeltaMda: float
        MassDeltaPpm: float
        MassExact: float
        MassSource: float
        RelativeAbundance: float
        SampleID: int

        def SetMassExactNull(self) -> None: ...
        def SetAbundanceNull(self) -> None: ...
        def SetIsUniqueNull(self) -> None: ...
        def IsAbundanceNull(self) -> bool: ...
        def SetMassSourceNull(self) -> None: ...
        def IsIsUniqueNull(self) -> bool: ...
        def SetMassDeltaMdaNull(self) -> None: ...
        def IsMassDeltaPpmNull(self) -> bool: ...
        def SetRelativeAbundanceNull(self) -> None: ...
        def SetFragmentFormulaNull(self) -> None: ...
        def SetMassDeltaPpmNull(self) -> None: ...
        def IsChargeNull(self) -> bool: ...
        def IsMassSourceNull(self) -> bool: ...
        def IsRelativeAbundanceNull(self) -> bool: ...
        def SetChargeNull(self) -> None: ...
        def IsMassExactNull(self) -> bool: ...
        def IsFragmentFormulaNull(self) -> bool: ...
        def IsMassDeltaMdaNull(self) -> bool: ...

    class ExactMassRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRow
        )  # readonly

    class ExactMassRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ExactMassRowChangeEvent,
        ) -> None: ...

    class HitDataTable(
        System.ComponentModel.ISupportInitialize,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AgilentIDColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        BlankSubtractedColumn: System.Data.DataColumn  # readonly
        CASNumberColumn: System.Data.DataColumn  # readonly
        ComponentIDColumn: System.Data.DataColumn  # readonly
        CompoundNameColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DeconvolutionMethodIDColumn: System.Data.DataColumn  # readonly
        EstimatedConcentrationColumn: System.Data.DataColumn  # readonly
        FormulaColumn: System.Data.DataColumn  # readonly
        GraphicsHitLibrarySpectrumColumn: System.Data.DataColumn  # readonly
        HitIDColumn: System.Data.DataColumn  # readonly
        IdentificationMethodIDColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow
        ): ...
        KEGGIDColumn: System.Data.DataColumn  # readonly
        LibraryCompoundDescriptionColumn: System.Data.DataColumn  # readonly
        LibraryEntryIDColumn: System.Data.DataColumn  # readonly
        LibraryMatchScoreColumn: System.Data.DataColumn  # readonly
        LibraryRetentionIndexColumn: System.Data.DataColumn  # readonly
        LibraryRetentionTimeColumn: System.Data.DataColumn  # readonly
        LibrarySearchMethodIDColumn: System.Data.DataColumn  # readonly
        MassAbundanceScoreColumn: System.Data.DataColumn  # readonly
        MassAccuracyScoreColumn: System.Data.DataColumn  # readonly
        MassMatchScoreColumn: System.Data.DataColumn  # readonly
        MassSpacingScoreColumn: System.Data.DataColumn  # readonly
        MolecularWeightColumn: System.Data.DataColumn  # readonly
        MonoIsotopicMassColumn: System.Data.DataColumn  # readonly
        NumberOfExactMassesColumn: System.Data.DataColumn  # readonly
        RTMismatchPenaltyColumn: System.Data.DataColumn  # readonly
        RemovedDuplicateMZsColumn: System.Data.DataColumn  # readonly
        ResponseFactorForEstimationColumn: System.Data.DataColumn  # readonly
        RetentionIndexColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        TargetCompoundIDColumn: System.Data.DataColumn  # readonly
        UserCustomCalculationColumn: System.Data.DataColumn  # readonly
        UserDefinedColumn: System.Data.DataColumn  # readonly
        VisibleColumn: System.Data.DataColumn  # readonly

        @overload
        def AddHitRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow,
        ) -> None: ...
        @overload
        def AddHitRow(
            self,
            BatchID: int,
            SampleID: int,
            DeconvolutionMethodID: int,
            ComponentID: int,
            HitID: int,
            AgilentID: str,
            IdentificationMethodID: int,
            LibrarySearchMethodID: int,
            LibraryEntryID: int,
            TargetCompoundID: int,
            CASNumber: str,
            CompoundName: str,
            EstimatedConcentration: float,
            Formula: str,
            KEGGID: str,
            LibraryMatchScore: float,
            LibraryRetentionIndex: float,
            LibraryRetentionTime: float,
            LibraryCompoundDescription: str,
            MolecularWeight: float,
            RTMismatchPenalty: float,
            RetentionIndex: float,
            MassMatchScore: float,
            MassAbundanceScore: float,
            MassAccuracyScore: float,
            MassSpacingScore: float,
            Visible: bool,
            BlankSubtracted: bool,
            RemovedDuplicateMZs: str,
            ResponseFactorForEstimation: float,
            MonoIsotopicMass: float,
            NumberOfExactMasses: int,
            UserDefined: str,
            UserCustomCalculation: float,
            GraphicsHitLibrarySpectrum: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow
        ): ...
        def RemoveHitRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewHitRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def FindByBatchIDSampleIDDeconvolutionMethodIDComponentIDHitID(
            self,
            BatchID: int,
            SampleID: int,
            DeconvolutionMethodID: int,
            ComponentID: int,
            HitID: int,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow
        ): ...

        HitRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRowChangeEventHandler
        )  # Event
        HitRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRowChangeEventHandler
        )  # Event
        HitRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRowChangeEventHandler
        )  # Event
        HitRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRowChangeEventHandler
        )  # Event

    class HitRow(System.Data.DataRow):  # Class
        AgilentID: str
        BatchID: int
        BlankSubtracted: bool
        CASNumber: str
        ComponentID: int
        ComponentRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
        )
        CompoundName: str
        DeconvolutionMethodID: int
        EstimatedConcentration: float
        Formula: str
        GraphicsHitLibrarySpectrum: str
        HitID: int
        IdentificationMethodID: int
        KEGGID: str
        LibraryCompoundDescription: str
        LibraryEntryID: int
        LibraryMatchScore: float
        LibraryRetentionIndex: float
        LibraryRetentionTime: float
        LibrarySearchMethodID: int
        LibrarySearchMethodRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        )
        MassAbundanceScore: float
        MassAccuracyScore: float
        MassMatchScore: float
        MassSpacingScore: float
        MolecularWeight: float
        MonoIsotopicMass: float
        NumberOfExactMasses: int
        RTMismatchPenalty: float
        RemovedDuplicateMZs: str
        ResponseFactorForEstimation: float
        RetentionIndex: float
        SampleID: int
        TargetCompoundID: int
        UserCustomCalculation: float
        UserDefined: str
        Visible: bool

        def IsRemovedDuplicateMZsNull(self) -> bool: ...
        def IsRetentionIndexNull(self) -> bool: ...
        def SetTargetCompoundIDNull(self) -> None: ...
        def SetMonoIsotopicMassNull(self) -> None: ...
        def IsEstimatedConcentrationNull(self) -> bool: ...
        def SetUserDefinedNull(self) -> None: ...
        def SetEstimatedConcentrationNull(self) -> None: ...
        def SetRemovedDuplicateMZsNull(self) -> None: ...
        def SetAgilentIDNull(self) -> None: ...
        def IsGraphicsHitLibrarySpectrumNull(self) -> bool: ...
        def IsResponseFactorForEstimationNull(self) -> bool: ...
        def SetFormulaNull(self) -> None: ...
        def IsFormulaNull(self) -> bool: ...
        def SetGraphicsHitLibrarySpectrumNull(self) -> None: ...
        def SetMolecularWeightNull(self) -> None: ...
        def IsAgilentIDNull(self) -> bool: ...
        def SetResponseFactorForEstimationNull(self) -> None: ...
        def IsUserCustomCalculationNull(self) -> bool: ...
        def IsLibraryMatchScoreNull(self) -> bool: ...
        def IsMonoIsotopicMassNull(self) -> bool: ...
        def SetBlankSubtractedNull(self) -> None: ...
        def SetRetentionIndexNull(self) -> None: ...
        def SetUserCustomCalculationNull(self) -> None: ...
        def SetLibraryCompoundDescriptionNull(self) -> None: ...
        def SetLibraryRetentionTimeNull(self) -> None: ...
        def IsLibraryRetentionTimeNull(self) -> bool: ...
        def IsRTMismatchPenaltyNull(self) -> bool: ...
        def IsMassAbundanceScoreNull(self) -> bool: ...
        def SetNumberOfExactMassesNull(self) -> None: ...
        def IsKEGGIDNull(self) -> bool: ...
        def SetMassAccuracyScoreNull(self) -> None: ...
        def SetRTMismatchPenaltyNull(self) -> None: ...
        def IsBlankSubtractedNull(self) -> bool: ...
        def SetMassSpacingScoreNull(self) -> None: ...
        def SetLibraryMatchScoreNull(self) -> None: ...
        def IsCompoundNameNull(self) -> bool: ...
        def IsTargetCompoundIDNull(self) -> bool: ...
        def SetMassAbundanceScoreNull(self) -> None: ...
        def SetLibraryRetentionIndexNull(self) -> None: ...
        def IsCASNumberNull(self) -> bool: ...
        def IsNumberOfExactMassesNull(self) -> bool: ...
        def IsMassAccuracyScoreNull(self) -> bool: ...
        def IsMassSpacingScoreNull(self) -> bool: ...
        def IsMassMatchScoreNull(self) -> bool: ...
        def IsUserDefinedNull(self) -> bool: ...
        def SetMassMatchScoreNull(self) -> None: ...
        def IsLibraryRetentionIndexNull(self) -> bool: ...
        def IsLibraryCompoundDescriptionNull(self) -> bool: ...
        def SetCompoundNameNull(self) -> None: ...
        def SetCASNumberNull(self) -> None: ...
        def SetKEGGIDNull(self) -> None: ...
        def IsMolecularWeightNull(self) -> bool: ...

    class HitRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow
        )  # readonly

    class HitRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRowChangeEvent,
        ) -> None: ...

    class IdentificationMethodDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        BatchIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        ExactMassAllowMultiplyChargedIonsColumn: System.Data.DataColumn  # readonly
        ExactMassMZDeltaColumn: System.Data.DataColumn  # readonly
        ExactMassMaxIonsPerSpectrumColumn: System.Data.DataColumn  # readonly
        ExactMassMinMZDeltaColumn: System.Data.DataColumn  # readonly
        ExactMassMinRelativeAbundanceColumn: System.Data.DataColumn  # readonly
        ExactMassPeakSelectionWeightingColumn: System.Data.DataColumn  # readonly
        IdentificationMethodIDColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow
        ): ...
        LibrarySearchTypeColumn: System.Data.DataColumn  # readonly
        MaxHitCountColumn: System.Data.DataColumn  # readonly
        MaxMZColumn: System.Data.DataColumn  # readonly
        MinMZColumn: System.Data.DataColumn  # readonly
        MinMatchScoreColumn: System.Data.DataColumn  # readonly
        MultiLibrarySearchTypeColumn: System.Data.DataColumn  # readonly
        PerformExactMassColumn: System.Data.DataColumn  # readonly
        RatioPercentUncertaintyColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByBatchIDSampleIDIdentificationMethodID(
            self, BatchID: int, SampleID: int, IdentificationMethodID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def NewIdentificationMethodRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow
        ): ...
        @overload
        def AddIdentificationMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
        ) -> None: ...
        @overload
        def AddIdentificationMethodRow(
            self,
            BatchID: int,
            SampleID: int,
            IdentificationMethodID: int,
            MaxHitCount: int,
            MaxMZ: float,
            MinMatchScore: float,
            MinMZ: float,
            RatioPercentUncertainty: float,
            MultiLibrarySearchType: str,
            LibrarySearchType: str,
            PerformExactMass: bool,
            ExactMassAllowMultiplyChargedIons: bool,
            ExactMassMaxIonsPerSpectrum: int,
            ExactMassMinRelativeAbundance: float,
            ExactMassMZDelta: float,
            ExactMassMinMZDelta: float,
            ExactMassPeakSelectionWeighting: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow
        ): ...
        def RemoveIdentificationMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
        ) -> None: ...

        IdentificationMethodRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRowChangeEventHandler
        )  # Event
        IdentificationMethodRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRowChangeEventHandler
        )  # Event
        IdentificationMethodRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRowChangeEventHandler
        )  # Event
        IdentificationMethodRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRowChangeEventHandler
        )  # Event

    class IdentificationMethodRow(System.Data.DataRow):  # Class
        BatchID: int
        ExactMassAllowMultiplyChargedIons: bool
        ExactMassMZDelta: float
        ExactMassMaxIonsPerSpectrum: int
        ExactMassMinMZDelta: float
        ExactMassMinRelativeAbundance: float
        ExactMassPeakSelectionWeighting: str
        IdentificationMethodID: int
        LibrarySearchType: str
        MaxHitCount: int
        MaxMZ: float
        MinMZ: float
        MinMatchScore: float
        MultiLibrarySearchType: str
        PerformExactMass: bool
        RatioPercentUncertainty: float
        SampleID: int
        SampleRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        )

        def GetLibrarySearchMethodRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        ]: ...
        def IsExactMassMaxIonsPerSpectrumNull(self) -> bool: ...
        def SetExactMassPeakSelectionWeightingNull(self) -> None: ...
        def SetExactMassMaxIonsPerSpectrumNull(self) -> None: ...
        def IsMinMZNull(self) -> bool: ...
        def IsExactMassMZDeltaNull(self) -> bool: ...
        def IsPerformExactMassNull(self) -> bool: ...
        def SetMinMZNull(self) -> None: ...
        def IsExactMassMinRelativeAbundanceNull(self) -> bool: ...
        def IsExactMassAllowMultiplyChargedIonsNull(self) -> bool: ...
        def SetExactMassMinMZDeltaNull(self) -> None: ...
        def IsLibrarySearchTypeNull(self) -> bool: ...
        def SetMaxMZNull(self) -> None: ...
        def IsExactMassMinMZDeltaNull(self) -> bool: ...
        def SetExactMassAllowMultiplyChargedIonsNull(self) -> None: ...
        def IsMaxMZNull(self) -> bool: ...
        def SetLibrarySearchTypeNull(self) -> None: ...
        def SetPerformExactMassNull(self) -> None: ...
        def IsExactMassPeakSelectionWeightingNull(self) -> bool: ...
        def SetExactMassMZDeltaNull(self) -> None: ...
        def SetExactMassMinRelativeAbundanceNull(self) -> None: ...

    class IdentificationMethodRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow
        )  # readonly

    class IdentificationMethodRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRowChangeEvent,
        ) -> None: ...

    class IonPeakDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow
        ],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AreaColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        ComponentIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DeconvolutedAreaColumn: System.Data.DataColumn  # readonly
        DeconvolutedHeightColumn: System.Data.DataColumn  # readonly
        DeconvolutionMethodIDColumn: System.Data.DataColumn  # readonly
        EndXColumn: System.Data.DataColumn  # readonly
        FullWidthHalfMaximumColumn: System.Data.DataColumn  # readonly
        HeightColumn: System.Data.DataColumn  # readonly
        IonPeakIDColumn: System.Data.DataColumn  # readonly
        IonPolarityColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow
        ): ...
        MZColumn: System.Data.DataColumn  # readonly
        PeakStatusColumn: System.Data.DataColumn  # readonly
        RetentionTimeColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        SaturatedColumn: System.Data.DataColumn  # readonly
        ScanTypeColumn: System.Data.DataColumn  # readonly
        SelectedMZColumn: System.Data.DataColumn  # readonly
        SharpnessColumn: System.Data.DataColumn  # readonly
        SignalToNoiseRatioColumn: System.Data.DataColumn  # readonly
        StartXColumn: System.Data.DataColumn  # readonly
        SymmetryColumn: System.Data.DataColumn  # readonly
        TargetCompoundIDColumn: System.Data.DataColumn  # readonly
        TargetQualifierIDColumn: System.Data.DataColumn  # readonly
        UserCustomCalculationColumn: System.Data.DataColumn  # readonly
        XArrayColumn: System.Data.DataColumn  # readonly
        YArrayColumn: System.Data.DataColumn  # readonly

        def RemoveIonPeakRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByBatchIDSampleIDDeconvolutionMethodIDComponentIDIonPeakID(
            self,
            BatchID: int,
            SampleID: int,
            DeconvolutionMethodID: int,
            ComponentID: int,
            IonPeakID: int,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow
        ): ...
        def NewIonPeakRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow
        ): ...
        @overload
        def AddIonPeakRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow,
        ) -> None: ...
        @overload
        def AddIonPeakRow(
            self,
            BatchID: int,
            SampleID: int,
            DeconvolutionMethodID: int,
            ComponentID: int,
            IonPeakID: int,
            TargetCompoundID: int,
            TargetQualifierID: int,
            Area: float,
            DeconvolutedArea: float,
            DeconvolutedHeight: float,
            EndX: float,
            FullWidthHalfMaximum: float,
            Height: float,
            IonPolarity: str,
            MZ: float,
            PeakStatus: str,
            RetentionTime: float,
            Saturated: bool,
            ScanType: str,
            SelectedMZ: float,
            Sharpness: float,
            SignalToNoiseRatio: float,
            StartX: float,
            Symmetry: float,
            XArray: str,
            YArray: str,
            UserCustomCalculation: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...

        IonPeakRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRowChangeEventHandler
        )  # Event
        IonPeakRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRowChangeEventHandler
        )  # Event
        IonPeakRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRowChangeEventHandler
        )  # Event
        IonPeakRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRowChangeEventHandler
        )  # Event

    class IonPeakRow(System.Data.DataRow):  # Class
        Area: float
        BatchID: int
        ComponentID: int
        ComponentRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentRow
        )
        DeconvolutedArea: float
        DeconvolutedHeight: float
        DeconvolutionMethodID: int
        EndX: float
        FullWidthHalfMaximum: float
        Height: float
        IonPeakID: int
        IonPolarity: str
        MZ: float
        PeakStatus: str
        RetentionTime: float
        SampleID: int
        Saturated: bool
        ScanType: str
        SelectedMZ: float
        Sharpness: float
        SignalToNoiseRatio: float
        StartX: float
        Symmetry: float
        TargetCompoundID: int
        TargetQualifierID: int
        UserCustomCalculation: float
        XArray: str
        YArray: str

        def IsMZNull(self) -> bool: ...
        def SetDeconvolutedAreaNull(self) -> None: ...
        def SetTargetCompoundIDNull(self) -> None: ...
        def IsScanTypeNull(self) -> bool: ...
        def IsHeightNull(self) -> bool: ...
        def SetDeconvolutedHeightNull(self) -> None: ...
        def IsXArrayNull(self) -> bool: ...
        def IsAreaNull(self) -> bool: ...
        def IsSaturatedNull(self) -> bool: ...
        def SetIonPolarityNull(self) -> None: ...
        def IsFullWidthHalfMaximumNull(self) -> bool: ...
        def IsRetentionTimeNull(self) -> bool: ...
        def IsEndXNull(self) -> bool: ...
        def IsSharpnessNull(self) -> bool: ...
        def IsPeakStatusNull(self) -> bool: ...
        def IsUserCustomCalculationNull(self) -> bool: ...
        def IsSignalToNoiseRatioNull(self) -> bool: ...
        def IsDeconvolutedAreaNull(self) -> bool: ...
        def IsIonPolarityNull(self) -> bool: ...
        def SetSharpnessNull(self) -> None: ...
        def SetUserCustomCalculationNull(self) -> None: ...
        def SetSignalToNoiseRatioNull(self) -> None: ...
        def SetHeightNull(self) -> None: ...
        def IsSelectedMZNull(self) -> bool: ...
        def SetYArrayNull(self) -> None: ...
        def SetSaturatedNull(self) -> None: ...
        def SetPeakStatusNull(self) -> None: ...
        def SetSymmetryNull(self) -> None: ...
        def IsTargetQualifierIDNull(self) -> bool: ...
        def SetRetentionTimeNull(self) -> None: ...
        def IsDeconvolutedHeightNull(self) -> bool: ...
        def SetXArrayNull(self) -> None: ...
        def IsTargetCompoundIDNull(self) -> bool: ...
        def SetScanTypeNull(self) -> None: ...
        def SetTargetQualifierIDNull(self) -> None: ...
        def IsYArrayNull(self) -> bool: ...
        def SetFullWidthHalfMaximumNull(self) -> None: ...
        def IsStartXNull(self) -> bool: ...
        def SetMZNull(self) -> None: ...
        def SetAreaNull(self) -> None: ...
        def SetEndXNull(self) -> None: ...
        def IsSymmetryNull(self) -> bool: ...
        def SetStartXNull(self) -> None: ...
        def SetSelectedMZNull(self) -> None: ...

    class IonPeakRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRow
        )  # readonly

    class IonPeakRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakRowChangeEvent,
        ) -> None: ...

    class LibrarySearchMethodDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        ],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AccurateMassToleranceColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        IdentificationMethodIDColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        ): ...
        LibraryFileColumn: System.Data.DataColumn  # readonly
        LibraryPathColumn: System.Data.DataColumn  # readonly
        LibrarySearchMethodIDColumn: System.Data.DataColumn  # readonly
        LibraryTypeColumn: System.Data.DataColumn  # readonly
        NISTCompatibilityColumn: System.Data.DataColumn  # readonly
        PureWeightFactorColumn: System.Data.DataColumn  # readonly
        RTCalibrationColumn: System.Data.DataColumn  # readonly
        RTMatchFactorTypeColumn: System.Data.DataColumn  # readonly
        RTMaxPenaltyColumn: System.Data.DataColumn  # readonly
        RTPenaltyTypeColumn: System.Data.DataColumn  # readonly
        RTRangeColumn: System.Data.DataColumn  # readonly
        RTRangeNoPenaltyColumn: System.Data.DataColumn  # readonly
        RemoveDuplicateHitsColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        ScreeningEnabledColumn: System.Data.DataColumn  # readonly
        ScreeningTypeColumn: System.Data.DataColumn  # readonly
        SearchOrderColumn: System.Data.DataColumn  # readonly
        SpectrumThresholdColumn: System.Data.DataColumn  # readonly

        def RemoveLibrarySearchMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow,
        ) -> None: ...
        @overload
        def AddLibrarySearchMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow,
        ) -> None: ...
        @overload
        def AddLibrarySearchMethodRow(
            self,
            BatchID: int,
            SampleID: int,
            IdentificationMethodID: int,
            LibrarySearchMethodID: int,
            LibraryFile: str,
            LibraryPath: str,
            LibraryType: str,
            ScreeningEnabled: bool,
            ScreeningType: str,
            NISTCompatibility: bool,
            PureWeightFactor: float,
            SearchOrder: int,
            RTCalibration: str,
            RTMatchFactorType: str,
            RTMaxPenalty: float,
            RTPenaltyType: str,
            RTRange: float,
            RTRangeNoPenalty: float,
            SpectrumThreshold: float,
            RemoveDuplicateHits: bool,
            AccurateMassTolerance: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def NewLibrarySearchMethodRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def FindByBatchIDSampleIDIdentificationMethodIDLibrarySearchMethodID(
            self,
            BatchID: int,
            SampleID: int,
            IdentificationMethodID: int,
            LibrarySearchMethodID: int,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        ): ...

        LibrarySearchMethodRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRowChangeEventHandler
        )  # Event
        LibrarySearchMethodRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRowChangeEventHandler
        )  # Event
        LibrarySearchMethodRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRowChangeEventHandler
        )  # Event
        LibrarySearchMethodRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRowChangeEventHandler
        )  # Event

    class LibrarySearchMethodRow(System.Data.DataRow):  # Class
        AccurateMassTolerance: float
        BatchID: int
        IdentificationMethodID: int
        IdentificationMethodRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow
        )
        LibraryFile: str
        LibraryPath: str
        LibrarySearchMethodID: int
        LibraryType: str
        NISTCompatibility: bool
        PureWeightFactor: float
        RTCalibration: str
        RTMatchFactorType: str
        RTMaxPenalty: float
        RTPenaltyType: str
        RTRange: float
        RTRangeNoPenalty: float
        RemoveDuplicateHits: bool
        SampleID: int
        ScreeningEnabled: bool
        ScreeningType: str
        SearchOrder: int
        SpectrumThreshold: float

        def IsAccurateMassToleranceNull(self) -> bool: ...
        def SetRTCalibrationNull(self) -> None: ...
        def IsSpectrumThresholdNull(self) -> bool: ...
        def SetSpectrumThresholdNull(self) -> None: ...
        def GetHitRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow
        ]: ...
        def IsRemoveDuplicateHitsNull(self) -> bool: ...
        def SetAccurateMassToleranceNull(self) -> None: ...
        def IsRTCalibrationNull(self) -> bool: ...
        def SetRemoveDuplicateHitsNull(self) -> None: ...
        def SetScreeningTypeNull(self) -> None: ...
        def IsScreeningTypeNull(self) -> bool: ...

    class LibrarySearchMethodRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRow
        )  # readonly

    class LibrarySearchMethodRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodRowChangeEvent,
        ) -> None: ...

    class PeakDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow
        ],
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AreaColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        CalculatedConcentrationColumn: System.Data.DataColumn  # readonly
        CoelutionScoreColumn: System.Data.DataColumn  # readonly
        CompoundIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FinalConcentrationColumn: System.Data.DataColumn  # readonly
        FullWidthHalfMaximumColumn: System.Data.DataColumn  # readonly
        HeightColumn: System.Data.DataColumn  # readonly
        IntegrationEndTimeColumn: System.Data.DataColumn  # readonly
        IntegrationMetricQualityFlagsColumn: System.Data.DataColumn  # readonly
        IntegrationStartTimeColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow
        ): ...
        MZColumn: System.Data.DataColumn  # readonly
        ManuallyIntegratedColumn: System.Data.DataColumn  # readonly
        MassAccuracyColumn: System.Data.DataColumn  # readonly
        MassMatchScoreColumn: System.Data.DataColumn  # readonly
        MatrixSpikePercentRecoveryColumn: System.Data.DataColumn  # readonly
        NoiseColumn: System.Data.DataColumn  # readonly
        PeakIDColumn: System.Data.DataColumn  # readonly
        PlatesColumn: System.Data.DataColumn  # readonly
        PurityColumn: System.Data.DataColumn  # readonly
        QValueComputedColumn: System.Data.DataColumn  # readonly
        ReferenceLibraryMatchScoreColumn: System.Data.DataColumn  # readonly
        ResolutionFrontColumn: System.Data.DataColumn  # readonly
        ResolutionRearColumn: System.Data.DataColumn  # readonly
        RetentionIndexColumn: System.Data.DataColumn  # readonly
        RetentionTimeColumn: System.Data.DataColumn  # readonly
        RetentionTimeDifferenceColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        SaturationRecoveryRatioColumn: System.Data.DataColumn  # readonly
        SignalToNoiseRatioColumn: System.Data.DataColumn  # readonly
        SurrogatePercentRecoveryColumn: System.Data.DataColumn  # readonly
        SymmetryColumn: System.Data.DataColumn  # readonly
        TargetResponseColumn: System.Data.DataColumn  # readonly
        UserCustomCalculation1Column: System.Data.DataColumn  # readonly
        UserCustomCalculation2Column: System.Data.DataColumn  # readonly
        UserCustomCalculation3Column: System.Data.DataColumn  # readonly
        UserCustomCalculation4Column: System.Data.DataColumn  # readonly
        UserCustomCalculationColumn: System.Data.DataColumn  # readonly
        WidthColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemovePeakRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow,
        ) -> None: ...
        def NewPeakRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow
        ): ...
        def FindByBatchIDSampleIDCompoundIDPeakID(
            self, BatchID: int, SampleID: int, CompoundID: int, PeakID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        @overload
        def AddPeakRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow,
        ) -> None: ...
        @overload
        def AddPeakRow(
            self,
            BatchID: int,
            SampleID: int,
            CompoundID: int,
            PeakID: int,
            Area: float,
            CalculatedConcentration: float,
            CoelutionScore: float,
            FinalConcentration: float,
            FullWidthHalfMaximum: float,
            Height: float,
            IntegrationMetricQualityFlags: str,
            IntegrationStartTime: float,
            IntegrationEndTime: float,
            Noise: float,
            ManuallyIntegrated: bool,
            MassAccuracy: float,
            MassMatchScore: float,
            MatrixSpikePercentRecovery: float,
            MZ: float,
            Plates: int,
            QValueComputed: int,
            RetentionIndex: float,
            RetentionTime: float,
            RetentionTimeDifference: float,
            ResolutionFront: float,
            ResolutionRear: float,
            SaturationRecoveryRatio: float,
            SignalToNoiseRatio: float,
            SurrogatePercentRecovery: float,
            Symmetry: float,
            TargetResponse: float,
            UserCustomCalculation: float,
            UserCustomCalculation1: float,
            UserCustomCalculation2: float,
            UserCustomCalculation3: float,
            UserCustomCalculation4: float,
            Width: float,
            ReferenceLibraryMatchScore: float,
            Purity: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow
        ): ...

        PeakRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRowChangeEventHandler
        )  # Event
        PeakRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRowChangeEventHandler
        )  # Event
        PeakRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRowChangeEventHandler
        )  # Event
        PeakRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRowChangeEventHandler
        )  # Event

    class PeakQualifierDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow
        ],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AreaColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        CompoundIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FullWidthHalfMaximumColumn: System.Data.DataColumn  # readonly
        HeightColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow
        ): ...
        ManuallyIntegratedColumn: System.Data.DataColumn  # readonly
        NoiseColumn: System.Data.DataColumn  # readonly
        PeakIDColumn: System.Data.DataColumn  # readonly
        QualifierIDColumn: System.Data.DataColumn  # readonly
        QualifierResponseRatioColumn: System.Data.DataColumn  # readonly
        RetentionTimeColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        SignalToNoiseRatioColumn: System.Data.DataColumn  # readonly
        SymmetryColumn: System.Data.DataColumn  # readonly

        def NewPeakQualifierRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow
        ): ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def RemovePeakQualifierRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow,
        ) -> None: ...
        @overload
        def AddPeakQualifierRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow,
        ) -> None: ...
        @overload
        def AddPeakQualifierRow(
            self,
            BatchID: int,
            SampleID: int,
            CompoundID: int,
            QualifierID: int,
            PeakID: int,
            Area: float,
            FullWidthHalfMaximum: float,
            Height: float,
            Noise: str,
            ManuallyIntegrated: bool,
            QualifierResponseRatio: float,
            RetentionTime: float,
            SignalToNoiseRatio: float,
            Symmetry: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def FindByBatchIDSampleIDCompoundIDQualifierIDPeakID(
            self,
            BatchID: int,
            SampleID: int,
            CompoundID: int,
            QualifierID: int,
            PeakID: int,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow
        ): ...

        PeakQualifierRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRowChangeEventHandler
        )  # Event
        PeakQualifierRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRowChangeEventHandler
        )  # Event
        PeakQualifierRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRowChangeEventHandler
        )  # Event
        PeakQualifierRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRowChangeEventHandler
        )  # Event

    class PeakQualifierRow(System.Data.DataRow):  # Class
        Area: float
        BatchID: int
        CompoundID: int
        FullWidthHalfMaximum: float
        Height: float
        ManuallyIntegrated: bool
        Noise: str
        PeakID: int
        QualifierID: int
        QualifierResponseRatio: float
        RetentionTime: float
        SampleID: int
        SignalToNoiseRatio: float
        Symmetry: float
        TargetQualifierRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow
        )

        def IsFullWidthHalfMaximumNull(self) -> bool: ...
        def IsSignalToNoiseRatioNull(self) -> bool: ...
        def IsRetentionTimeNull(self) -> bool: ...
        def SetNoiseNull(self) -> None: ...
        def SetSignalToNoiseRatioNull(self) -> None: ...
        def IsSymmetryNull(self) -> bool: ...
        def SetFullWidthHalfMaximumNull(self) -> None: ...
        def SetQualifierResponseRatioNull(self) -> None: ...
        def IsManuallyIntegratedNull(self) -> bool: ...
        def IsAreaNull(self) -> bool: ...
        def IsNoiseNull(self) -> bool: ...
        def IsHeightNull(self) -> bool: ...
        def IsQualifierResponseRatioNull(self) -> bool: ...
        def SetManuallyIntegratedNull(self) -> None: ...
        def SetAreaNull(self) -> None: ...
        def SetHeightNull(self) -> None: ...
        def SetSymmetryNull(self) -> None: ...
        def SetRetentionTimeNull(self) -> None: ...

    class PeakQualifierRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow
        )  # readonly

    class PeakQualifierRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRowChangeEvent,
        ) -> None: ...

    class PeakRow(System.Data.DataRow):  # Class
        Area: float
        BatchID: int
        CalculatedConcentration: float
        CoelutionScore: float
        CompoundID: int
        FinalConcentration: float
        FullWidthHalfMaximum: float
        Height: float
        IntegrationEndTime: float
        IntegrationMetricQualityFlags: str
        IntegrationStartTime: float
        MZ: float
        ManuallyIntegrated: bool
        MassAccuracy: float
        MassMatchScore: float
        MatrixSpikePercentRecovery: float
        Noise: float
        PeakID: int
        Plates: int
        Purity: float
        QValueComputed: int
        ReferenceLibraryMatchScore: float
        ResolutionFront: float
        ResolutionRear: float
        RetentionIndex: float
        RetentionTime: float
        RetentionTimeDifference: float
        SampleID: int
        SaturationRecoveryRatio: float
        SignalToNoiseRatio: float
        SurrogatePercentRecovery: float
        Symmetry: float
        TargetCompoundRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
        )
        TargetResponse: float
        UserCustomCalculation: float
        UserCustomCalculation1: float
        UserCustomCalculation2: float
        UserCustomCalculation3: float
        UserCustomCalculation4: float
        Width: float

        def IsCalculatedConcentrationNull(self) -> bool: ...
        def IsMZNull(self) -> bool: ...
        def IsRetentionIndexNull(self) -> bool: ...
        def IsMassAccuracyNull(self) -> bool: ...
        def IsWidthNull(self) -> bool: ...
        def IsResolutionRearNull(self) -> bool: ...
        def IsHeightNull(self) -> bool: ...
        def SetFinalConcentrationNull(self) -> None: ...
        def SetIntegrationStartTimeNull(self) -> None: ...
        def IsManuallyIntegratedNull(self) -> bool: ...
        def SetWidthNull(self) -> None: ...
        def IsAreaNull(self) -> bool: ...
        def IsNoiseNull(self) -> bool: ...
        def SetResolutionFrontNull(self) -> None: ...
        def SetSaturationRecoveryRatioNull(self) -> None: ...
        def IsFullWidthHalfMaximumNull(self) -> bool: ...
        def SetManuallyIntegratedNull(self) -> None: ...
        def SetIntegrationEndTimeNull(self) -> None: ...
        def IsRetentionTimeNull(self) -> bool: ...
        def SetQValueComputedNull(self) -> None: ...
        def SetResolutionRearNull(self) -> None: ...
        def IsUserCustomCalculationNull(self) -> bool: ...
        def SetCalculatedConcentrationNull(self) -> None: ...
        def IsSignalToNoiseRatioNull(self) -> bool: ...
        def IsFinalConcentrationNull(self) -> bool: ...
        def IsUserCustomCalculation4Null(self) -> bool: ...
        def IsSaturationRecoveryRatioNull(self) -> bool: ...
        def IsPurityNull(self) -> bool: ...
        def SetRetentionIndexNull(self) -> None: ...
        def SetUserCustomCalculation2Null(self) -> None: ...
        def SetSurrogatePercentRecoveryNull(self) -> None: ...
        def IsReferenceLibraryMatchScoreNull(self) -> bool: ...
        def SetSignalToNoiseRatioNull(self) -> None: ...
        def SetUserCustomCalculationNull(self) -> None: ...
        def SetHeightNull(self) -> None: ...
        def IsCoelutionScoreNull(self) -> bool: ...
        def SetCoelutionScoreNull(self) -> None: ...
        def SetMassAccuracyNull(self) -> None: ...
        def IsMatrixSpikePercentRecoveryNull(self) -> bool: ...
        def SetSymmetryNull(self) -> None: ...
        def IsSurrogatePercentRecoveryNull(self) -> bool: ...
        def SetIntegrationMetricQualityFlagsNull(self) -> None: ...
        def IsUserCustomCalculation1Null(self) -> bool: ...
        def SetMatrixSpikePercentRecoveryNull(self) -> None: ...
        def SetUserCustomCalculation1Null(self) -> None: ...
        def SetRetentionTimeNull(self) -> None: ...
        def SetTargetResponseNull(self) -> None: ...
        def IsIntegrationEndTimeNull(self) -> bool: ...
        def SetPlatesNull(self) -> None: ...
        def IsRetentionTimeDifferenceNull(self) -> bool: ...
        def SetNoiseNull(self) -> None: ...
        def IsQValueComputedNull(self) -> bool: ...
        def SetReferenceLibraryMatchScoreNull(self) -> None: ...
        def IsUserCustomCalculation2Null(self) -> bool: ...
        def SetPurityNull(self) -> None: ...
        def IsTargetResponseNull(self) -> bool: ...
        def IsUserCustomCalculation3Null(self) -> bool: ...
        def IsIntegrationStartTimeNull(self) -> bool: ...
        def SetFullWidthHalfMaximumNull(self) -> None: ...
        def IsPlatesNull(self) -> bool: ...
        def SetUserCustomCalculation4Null(self) -> None: ...
        def SetMZNull(self) -> None: ...
        def IsMassMatchScoreNull(self) -> bool: ...
        def SetAreaNull(self) -> None: ...
        def SetUserCustomCalculation3Null(self) -> None: ...
        def SetMassMatchScoreNull(self) -> None: ...
        def IsSymmetryNull(self) -> bool: ...
        def SetRetentionTimeDifferenceNull(self) -> None: ...
        def IsIntegrationMetricQualityFlagsNull(self) -> bool: ...
        def IsResolutionFrontNull(self) -> bool: ...

    class PeakRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow
        )  # readonly

    class PeakRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRowChangeEvent,
        ) -> None: ...

    class SampleDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        ],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AcqDateTimeColumn: System.Data.DataColumn  # readonly
        AcqDateTimeLocalColumn: System.Data.DataColumn  # readonly
        AcqMethodFileNameColumn: System.Data.DataColumn  # readonly
        AcqMethodPathNameColumn: System.Data.DataColumn  # readonly
        AcqOperatorColumn: System.Data.DataColumn  # readonly
        AnalysisStateColumn: System.Data.DataColumn  # readonly
        BarcodeColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        CommentColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DataFileNameColumn: System.Data.DataColumn  # readonly
        DataPathNameColumn: System.Data.DataColumn  # readonly
        DilutionColumn: System.Data.DataColumn  # readonly
        ExpectedBarCodeColumn: System.Data.DataColumn  # readonly
        GraphicsSampleChromatogramColumn: System.Data.DataColumn  # readonly
        ISTDDilutionColumn: System.Data.DataColumn  # readonly
        InjectorVolumeColumn: System.Data.DataColumn  # readonly
        InstrumentNameColumn: System.Data.DataColumn  # readonly
        InstrumentTypeColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        ): ...
        MatrixSpikeDilutionColumn: System.Data.DataColumn  # readonly
        MatrixSpikeGroupColumn: System.Data.DataColumn  # readonly
        MatrixTypeColumn: System.Data.DataColumn  # readonly
        PlateCodeColumn: System.Data.DataColumn  # readonly
        PlatePositionColumn: System.Data.DataColumn  # readonly
        RackCodeColumn: System.Data.DataColumn  # readonly
        RackPositionColumn: System.Data.DataColumn  # readonly
        SampleAmountColumn: System.Data.DataColumn  # readonly
        SampleGroupColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        SampleInformationColumn: System.Data.DataColumn  # readonly
        SampleNameColumn: System.Data.DataColumn  # readonly
        SamplePositionColumn: System.Data.DataColumn  # readonly
        SamplePrepFileNameColumn: System.Data.DataColumn  # readonly
        SamplePrepPathNameColumn: System.Data.DataColumn  # readonly
        SampleTypeColumn: System.Data.DataColumn  # readonly
        SamplingDateTimeColumn: System.Data.DataColumn  # readonly
        SamplingTimeColumn: System.Data.DataColumn  # readonly
        SurrogateDilutionColumn: System.Data.DataColumn  # readonly
        TotalSampleAmountColumn: System.Data.DataColumn  # readonly
        TrayNameColumn: System.Data.DataColumn  # readonly
        TuneFileLastTimeStampColumn: System.Data.DataColumn  # readonly
        TuneFileNameColumn: System.Data.DataColumn  # readonly
        TunePathNameColumn: System.Data.DataColumn  # readonly
        UserDefined1Column: System.Data.DataColumn  # readonly
        UserDefined2Column: System.Data.DataColumn  # readonly
        UserDefined3Column: System.Data.DataColumn  # readonly
        UserDefined4Column: System.Data.DataColumn  # readonly
        UserDefined5Column: System.Data.DataColumn  # readonly
        UserDefined6Column: System.Data.DataColumn  # readonly
        UserDefined7Column: System.Data.DataColumn  # readonly
        UserDefined8Column: System.Data.DataColumn  # readonly
        UserDefined9Column: System.Data.DataColumn  # readonly
        UserDefinedColumn: System.Data.DataColumn  # readonly
        VialColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddSampleRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow,
        ) -> None: ...
        @overload
        def AddSampleRow(
            self,
            parentBatchRowByFK_Batch_Sample: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow,
            SampleID: int,
            AcqDateTime: System.DateTime,
            AcqDateTimeLocal: System.DateTimeOffset,
            AcqMethodFileName: str,
            AcqMethodPathName: str,
            AcqOperator: str,
            Barcode: str,
            Comment: str,
            DataFileName: str,
            DataPathName: str,
            Dilution: float,
            ExpectedBarCode: str,
            InjectorVolume: float,
            InstrumentName: str,
            InstrumentType: str,
            ISTDDilution: float,
            MatrixSpikeDilution: float,
            MatrixSpikeGroup: str,
            MatrixType: str,
            PlateCode: str,
            PlatePosition: str,
            RackCode: str,
            RackPosition: str,
            SampleAmount: float,
            SampleInformation: str,
            SampleGroup: str,
            SampleName: str,
            SamplePosition: str,
            SamplePrepFileName: str,
            SamplePrepPathName: str,
            SampleType: str,
            SamplingDateTime: System.DateTime,
            SamplingTime: float,
            SurrogateDilution: float,
            TotalSampleAmount: float,
            TrayName: str,
            TuneFileLastTimeStamp: System.DateTime,
            TuneFileName: str,
            TunePathName: str,
            UserDefined: str,
            UserDefined1: str,
            UserDefined2: str,
            UserDefined3: str,
            UserDefined4: str,
            UserDefined5: str,
            UserDefined6: str,
            UserDefined7: str,
            UserDefined8: str,
            UserDefined9: str,
            Vial: int,
            AnalysisState: str,
            GraphicsSampleChromatogram: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        ): ...
        def FindByBatchIDSampleID(
            self, BatchID: int, SampleID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def NewSampleRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        ): ...
        def RemoveSampleRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow,
        ) -> None: ...

        SampleRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRowChangeEventHandler
        )  # Event
        SampleRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRowChangeEventHandler
        )  # Event
        SampleRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRowChangeEventHandler
        )  # Event
        SampleRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRowChangeEventHandler
        )  # Event

    class SampleRow(System.Data.DataRow):  # Class
        AcqDateTime: System.DateTime
        AcqDateTimeLocal: System.DateTimeOffset
        AcqMethodFileName: str
        AcqMethodPathName: str
        AcqOperator: str
        AnalysisState: str
        Barcode: str
        BatchID: int
        BatchRow: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchRow
        )
        Comment: str
        DataFileName: str
        DataPathName: str
        Dilution: float
        ExpectedBarCode: str
        GraphicsSampleChromatogram: str
        ISTDDilution: float
        InjectorVolume: float
        InstrumentName: str
        InstrumentType: str
        MatrixSpikeDilution: float
        MatrixSpikeGroup: str
        MatrixType: str
        PlateCode: str
        PlatePosition: str
        RackCode: str
        RackPosition: str
        SampleAmount: float
        SampleGroup: str
        SampleID: int
        SampleInformation: str
        SampleName: str
        SamplePosition: str
        SamplePrepFileName: str
        SamplePrepPathName: str
        SampleType: str
        SamplingDateTime: System.DateTime
        SamplingTime: float
        SurrogateDilution: float
        TotalSampleAmount: float
        TrayName: str
        TuneFileLastTimeStamp: System.DateTime
        TuneFileName: str
        TunePathName: str
        UserDefined: str
        UserDefined1: str
        UserDefined2: str
        UserDefined3: str
        UserDefined4: str
        UserDefined5: str
        UserDefined6: str
        UserDefined7: str
        UserDefined8: str
        UserDefined9: str
        Vial: int

        def IsRackPositionNull(self) -> bool: ...
        def SetDataPathNameNull(self) -> None: ...
        def IsSampleTypeNull(self) -> bool: ...
        def GetTargetCompoundRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
        ]: ...
        def IsISTDDilutionNull(self) -> bool: ...
        def IsTrayNameNull(self) -> bool: ...
        def SetTotalSampleAmountNull(self) -> None: ...
        def IsAcqOperatorNull(self) -> bool: ...
        def IsBarcodeNull(self) -> bool: ...
        def IsUserDefined8Null(self) -> bool: ...
        def GetBlankSubtractionMethodRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodRow
        ]: ...
        def SetSamplingDateTimeNull(self) -> None: ...
        def IsInstrumentTypeNull(self) -> bool: ...
        def SetAnalysisStateNull(self) -> None: ...
        def SetUserDefined5Null(self) -> None: ...
        def IsUserDefined1Null(self) -> bool: ...
        def IsMatrixSpikeGroupNull(self) -> bool: ...
        def SetDilutionNull(self) -> None: ...
        def IsDataPathNameNull(self) -> bool: ...
        def SetSampleNameNull(self) -> None: ...
        def IsAcqMethodFileNameNull(self) -> bool: ...
        def SetSamplingTimeNull(self) -> None: ...
        def IsSampleInformationNull(self) -> bool: ...
        def SetTuneFileLastTimeStampNull(self) -> None: ...
        def IsSamplingDateTimeNull(self) -> bool: ...
        def SetSampleInformationNull(self) -> None: ...
        def SetCommentNull(self) -> None: ...
        def IsUserDefined6Null(self) -> bool: ...
        def IsUserDefined3Null(self) -> bool: ...
        def GetTargetMatchMethodRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow
        ]: ...
        def SetSampleGroupNull(self) -> None: ...
        def IsSampleAmountNull(self) -> bool: ...
        def SetTunePathNameNull(self) -> None: ...
        def SetAcqDateTimeLocalNull(self) -> None: ...
        def SetVialNull(self) -> None: ...
        def SetUserDefinedNull(self) -> None: ...
        def SetGraphicsSampleChromatogramNull(self) -> None: ...
        def SetUserDefined3Null(self) -> None: ...
        def SetMatrixSpikeDilutionNull(self) -> None: ...
        def IsPlateCodeNull(self) -> bool: ...
        def GetAuxiliaryMethodRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodRow
        ]: ...
        def SetBarcodeNull(self) -> None: ...
        def SetRackCodeNull(self) -> None: ...
        def IsSamplePrepPathNameNull(self) -> bool: ...
        def SetUserDefined4Null(self) -> None: ...
        def SetInstrumentTypeNull(self) -> None: ...
        def SetSamplePositionNull(self) -> None: ...
        def IsUserDefined4Null(self) -> bool: ...
        def SetUserDefined9Null(self) -> None: ...
        def IsUserDefined9Null(self) -> bool: ...
        def IsTuneFileLastTimeStampNull(self) -> bool: ...
        def IsExpectedBarCodeNull(self) -> bool: ...
        def SetPlateCodeNull(self) -> None: ...
        def IsAcqMethodPathNameNull(self) -> bool: ...
        def SetPlatePositionNull(self) -> None: ...
        def SetUserDefined6Null(self) -> None: ...
        def SetUserDefined1Null(self) -> None: ...
        def IsInjectorVolumeNull(self) -> bool: ...
        def IsInstrumentNameNull(self) -> bool: ...
        def IsDataFileNameNull(self) -> bool: ...
        def IsSamplingTimeNull(self) -> bool: ...
        def IsDilutionNull(self) -> bool: ...
        def GetIdentificationMethodRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodRow
        ]: ...
        def SetTuneFileNameNull(self) -> None: ...
        def SetDataFileNameNull(self) -> None: ...
        def IsAnalysisStateNull(self) -> bool: ...
        def IsGraphicsSampleChromatogramNull(self) -> bool: ...
        def IsSamplePrepFileNameNull(self) -> bool: ...
        def IsUserDefinedNull(self) -> bool: ...
        def SetAcqMethodPathNameNull(self) -> None: ...
        def IsMatrixTypeNull(self) -> bool: ...
        def IsUserDefined2Null(self) -> bool: ...
        def IsTotalSampleAmountNull(self) -> bool: ...
        def SetUserDefined8Null(self) -> None: ...
        def SetInjectorVolumeNull(self) -> None: ...
        def GetDeconvolutionMethodRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodRow
        ]: ...
        def IsTuneFileNameNull(self) -> bool: ...
        def SetSurrogateDilutionNull(self) -> None: ...
        def SetMatrixTypeNull(self) -> None: ...
        def SetAcqOperatorNull(self) -> None: ...
        def IsUserDefined5Null(self) -> bool: ...
        def IsTunePathNameNull(self) -> bool: ...
        def SetSamplePrepFileNameNull(self) -> None: ...
        def IsSamplePositionNull(self) -> bool: ...
        def IsCommentNull(self) -> bool: ...
        def SetAcqMethodFileNameNull(self) -> None: ...
        def SetExpectedBarCodeNull(self) -> None: ...
        def SetTrayNameNull(self) -> None: ...
        def IsMatrixSpikeDilutionNull(self) -> bool: ...
        def IsAcqDateTimeLocalNull(self) -> bool: ...
        def IsUserDefined7Null(self) -> bool: ...
        def SetSampleTypeNull(self) -> None: ...
        def SetUserDefined7Null(self) -> None: ...
        def SetISTDDilutionNull(self) -> None: ...
        def SetAcqDateTimeNull(self) -> None: ...
        def SetUserDefined2Null(self) -> None: ...
        def SetMatrixSpikeGroupNull(self) -> None: ...
        def SetSamplePrepPathNameNull(self) -> None: ...
        def IsRackCodeNull(self) -> bool: ...
        def IsAcqDateTimeNull(self) -> bool: ...
        def SetSampleAmountNull(self) -> None: ...
        def IsSampleGroupNull(self) -> bool: ...
        def SetInstrumentNameNull(self) -> None: ...
        def IsPlatePositionNull(self) -> bool: ...
        def SetRackPositionNull(self) -> None: ...
        def IsSampleNameNull(self) -> bool: ...
        def IsSurrogateDilutionNull(self) -> bool: ...
        def IsVialNull(self) -> bool: ...

    class SampleRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        )  # readonly

    class SampleRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRowChangeEvent,
        ) -> None: ...

    class TargetCompoundDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
        ],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        AgilentIDColumn: System.Data.DataColumn  # readonly
        AverageResponseFactorColumn: System.Data.DataColumn  # readonly
        BatchIDColumn: System.Data.DataColumn  # readonly
        CASNumberColumn: System.Data.DataColumn  # readonly
        CellAcceleratorVoltageColumn: System.Data.DataColumn  # readonly
        CollisionEnergyColumn: System.Data.DataColumn  # readonly
        CompoundApprovedColumn: System.Data.DataColumn  # readonly
        CompoundGroupColumn: System.Data.DataColumn  # readonly
        CompoundIDColumn: System.Data.DataColumn  # readonly
        CompoundMathColumn: System.Data.DataColumn  # readonly
        CompoundNameColumn: System.Data.DataColumn  # readonly
        CompoundTypeColumn: System.Data.DataColumn  # readonly
        ConcentrationUnitsColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FragmentorVoltageColumn: System.Data.DataColumn  # readonly
        IDColumn: System.Data.DataColumn  # readonly
        ISTDCompoundIDColumn: System.Data.DataColumn  # readonly
        ISTDConcentrationColumn: System.Data.DataColumn  # readonly
        ISTDFlagColumn: System.Data.DataColumn  # readonly
        InstrumentTypeColumn: System.Data.DataColumn  # readonly
        IntegratorColumn: System.Data.DataColumn  # readonly
        IonPolarityColumn: System.Data.DataColumn  # readonly
        IonSourceColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
        ): ...
        KEGGIDColumn: System.Data.DataColumn  # readonly
        LeftRetentionTimeDeltaColumn: System.Data.DataColumn  # readonly
        LibraryMatchScoreColumn: System.Data.DataColumn  # readonly
        MZAdditionalColumn: System.Data.DataColumn  # readonly
        MZColumn: System.Data.DataColumn  # readonly
        MZExtractionWindowFilterLeftColumn: System.Data.DataColumn  # readonly
        MZExtractionWindowFilterRightColumn: System.Data.DataColumn  # readonly
        MZExtractionWindowUnitsColumn: System.Data.DataColumn  # readonly
        MZScanRangeHighColumn: System.Data.DataColumn  # readonly
        MZScanRangeLowColumn: System.Data.DataColumn  # readonly
        MatrixSpikeConcentrationColumn: System.Data.DataColumn  # readonly
        MolecularFormulaColumn: System.Data.DataColumn  # readonly
        MultiplierColumn: System.Data.DataColumn  # readonly
        NoiseOfRawSignalColumn: System.Data.DataColumn  # readonly
        PrimaryHitPeakIDColumn: System.Data.DataColumn  # readonly
        QuantitateByHeightColumn: System.Data.DataColumn  # readonly
        ReferenceMSPathNameColumn: System.Data.DataColumn  # readonly
        RelativeISTDMultiplierColumn: System.Data.DataColumn  # readonly
        RetentionIndexColumn: System.Data.DataColumn  # readonly
        RetentionTimeColumn: System.Data.DataColumn  # readonly
        RetentionTimeDeltaUnitsColumn: System.Data.DataColumn  # readonly
        RetentionTimeWindowColumn: System.Data.DataColumn  # readonly
        RetentionTimeWindowUnitsColumn: System.Data.DataColumn  # readonly
        RightRetentionTimeDeltaColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        ScanTypeColumn: System.Data.DataColumn  # readonly
        SelectedMZColumn: System.Data.DataColumn  # readonly
        UncertaintyRelativeOrAbsoluteColumn: System.Data.DataColumn  # readonly
        UserAnnotationColumn: System.Data.DataColumn  # readonly
        UserCustomCalculationColumn: System.Data.DataColumn  # readonly
        UserDefined1Column: System.Data.DataColumn  # readonly
        UserDefined2Column: System.Data.DataColumn  # readonly
        UserDefined3Column: System.Data.DataColumn  # readonly
        UserDefined4Column: System.Data.DataColumn  # readonly
        UserDefinedColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddTargetCompoundRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow,
        ) -> None: ...
        @overload
        def AddTargetCompoundRow(
            self,
            BatchID: int,
            SampleID: int,
            CompoundID: int,
            AgilentID: str,
            AverageResponseFactor: float,
            CASNumber: str,
            CellAcceleratorVoltage: float,
            CollisionEnergy: float,
            CompoundApproved: bool,
            CompoundGroup: str,
            CompoundName: str,
            CompoundType: str,
            ConcentrationUnits: str,
            FragmentorVoltage: float,
            Integrator: str,
            InstrumentType: str,
            IonPolarity: str,
            IonSource: str,
            ISTDCompoundID: int,
            ISTDConcentration: float,
            ISTDFlag: bool,
            KEGGID: str,
            LeftRetentionTimeDelta: float,
            LibraryMatchScore: float,
            MatrixSpikeConcentration: float,
            MolecularFormula: str,
            Multiplier: float,
            MZ: float,
            MZAdditional: str,
            MZExtractionWindowUnits: str,
            MZExtractionWindowFilterLeft: float,
            MZExtractionWindowFilterRight: float,
            MZScanRangeHigh: float,
            MZScanRangeLow: float,
            NoiseOfRawSignal: float,
            PrimaryHitPeakID: str,
            QuantitateByHeight: bool,
            ReferenceMSPathName: str,
            RelativeISTDMultiplier: float,
            RetentionTime: float,
            RetentionTimeDeltaUnits: str,
            RetentionTimeWindow: float,
            RetentionTimeWindowUnits: str,
            RightRetentionTimeDelta: float,
            ScanType: str,
            SelectedMZ: float,
            UncertaintyRelativeOrAbsolute: str,
            UserDefined: str,
            UserDefined1: str,
            UserDefined2: str,
            UserDefined3: str,
            UserDefined4: str,
            CompoundMath: str,
            UserAnnotation: str,
            UserCustomCalculation: float,
            RetentionIndex: float,
            ID: int,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
        ): ...
        def FindByBatchIDSampleIDCompoundID(
            self, BatchID: int, SampleID: int, CompoundID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
        ): ...
        def NewTargetCompoundRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def RemoveTargetCompoundRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow,
        ) -> None: ...

        TargetCompoundRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRowChangeEventHandler
        )  # Event
        TargetCompoundRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRowChangeEventHandler
        )  # Event
        TargetCompoundRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRowChangeEventHandler
        )  # Event
        TargetCompoundRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRowChangeEventHandler
        )  # Event

    class TargetCompoundRow(System.Data.DataRow):  # Class
        AgilentID: str
        AverageResponseFactor: float
        BatchID: int
        CASNumber: str
        CellAcceleratorVoltage: float
        CollisionEnergy: float
        CompoundApproved: bool
        CompoundGroup: str
        CompoundID: int
        CompoundMath: str
        CompoundName: str
        CompoundType: str
        ConcentrationUnits: str
        FragmentorVoltage: float
        ID: int
        ISTDCompoundID: int
        ISTDConcentration: float
        ISTDFlag: bool
        InstrumentType: str
        Integrator: str
        IonPolarity: str
        IonSource: str
        KEGGID: str
        LeftRetentionTimeDelta: float
        LibraryMatchScore: float
        MZ: float
        MZAdditional: str
        MZExtractionWindowFilterLeft: float
        MZExtractionWindowFilterRight: float
        MZExtractionWindowUnits: str
        MZScanRangeHigh: float
        MZScanRangeLow: float
        MatrixSpikeConcentration: float
        MolecularFormula: str
        Multiplier: float
        NoiseOfRawSignal: float
        PrimaryHitPeakID: str
        QuantitateByHeight: bool
        ReferenceMSPathName: str
        RelativeISTDMultiplier: float
        RetentionIndex: float
        RetentionTime: float
        RetentionTimeDeltaUnits: str
        RetentionTimeWindow: float
        RetentionTimeWindowUnits: str
        RightRetentionTimeDelta: float
        SampleID: int
        SampleRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        )
        ScanType: str
        SelectedMZ: float
        UncertaintyRelativeOrAbsolute: str
        UserAnnotation: str
        UserCustomCalculation: float
        UserDefined: str
        UserDefined1: str
        UserDefined2: str
        UserDefined3: str
        UserDefined4: str

        def IsMolecularFormulaNull(self) -> bool: ...
        def IsMZScanRangeHighNull(self) -> bool: ...
        def IsIonPolarityNull(self) -> bool: ...
        def IsIntegratorNull(self) -> bool: ...
        def SetCompoundTypeNull(self) -> None: ...
        def SetISTDCompoundIDNull(self) -> None: ...
        def SetAgilentIDNull(self) -> None: ...
        def IsKEGGIDNull(self) -> bool: ...
        def SetScanTypeNull(self) -> None: ...
        def IsAgilentIDNull(self) -> bool: ...
        def SetRetentionTimeWindowUnitsNull(self) -> None: ...
        def IsInstrumentTypeNull(self) -> bool: ...
        def SetMZExtractionWindowUnitsNull(self) -> None: ...
        def IsUserDefined1Null(self) -> bool: ...
        def IsCompoundGroupNull(self) -> bool: ...
        def IsCompoundApprovedNull(self) -> bool: ...
        def IsRightRetentionTimeDeltaNull(self) -> bool: ...
        def SetRelativeISTDMultiplierNull(self) -> None: ...
        def SetIonSourceNull(self) -> None: ...
        def SetIDNull(self) -> None: ...
        def IsMZExtractionWindowUnitsNull(self) -> bool: ...
        def IsRelativeISTDMultiplierNull(self) -> bool: ...
        def SetCompoundNameNull(self) -> None: ...
        def SetCompoundApprovedNull(self) -> None: ...
        def SetUserAnnotationNull(self) -> None: ...
        def SetMZExtractionWindowFilterLeftNull(self) -> None: ...
        def IsUserDefined3Null(self) -> bool: ...
        def IsNoiseOfRawSignalNull(self) -> bool: ...
        def IsMultiplierNull(self) -> bool: ...
        def IsIonSourceNull(self) -> bool: ...
        def IsMZExtractionWindowFilterLeftNull(self) -> bool: ...
        def GetPeakRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakRow
        ]: ...
        def SetUserDefinedNull(self) -> None: ...
        def SetSelectedMZNull(self) -> None: ...
        def SetISTDConcentrationNull(self) -> None: ...
        def SetMZExtractionWindowFilterRightNull(self) -> None: ...
        def SetUserDefined3Null(self) -> None: ...
        def GetTargetQualifierRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow
        ]: ...
        def SetNoiseOfRawSignalNull(self) -> None: ...
        def SetInstrumentTypeNull(self) -> None: ...
        def SetRetentionTimeWindowNull(self) -> None: ...
        def SetUserDefined4Null(self) -> None: ...
        def IsUserDefined4Null(self) -> bool: ...
        def SetReferenceMSPathNameNull(self) -> None: ...
        def SetLibraryMatchScoreNull(self) -> None: ...
        def SetPrimaryHitPeakIDNull(self) -> None: ...
        def IsFragmentorVoltageNull(self) -> bool: ...
        def SetMatrixSpikeConcentrationNull(self) -> None: ...
        def IsSelectedMZNull(self) -> bool: ...
        def IsMatrixSpikeConcentrationNull(self) -> bool: ...
        def IsCollisionEnergyNull(self) -> bool: ...
        def SetConcentrationUnitsNull(self) -> None: ...
        def IsISTDFlagNull(self) -> bool: ...
        def IsPrimaryHitPeakIDNull(self) -> bool: ...
        def SetCompoundGroupNull(self) -> None: ...
        def IsMZScanRangeLowNull(self) -> bool: ...
        def SetKEGGIDNull(self) -> None: ...
        def SetUserDefined1Null(self) -> None: ...
        def SetRetentionTimeNull(self) -> None: ...
        def SetMZScanRangeLowNull(self) -> None: ...
        def SetMZNull(self) -> None: ...
        def SetCollisionEnergyNull(self) -> None: ...
        def IsCASNumberNull(self) -> bool: ...
        def SetFragmentorVoltageNull(self) -> None: ...
        def SetLeftRetentionTimeDeltaNull(self) -> None: ...
        def IsISTDCompoundIDNull(self) -> bool: ...
        def IsUserDefinedNull(self) -> bool: ...
        def IsUserDefined2Null(self) -> bool: ...
        def SetCASNumberNull(self) -> None: ...
        def IsQuantitateByHeightNull(self) -> bool: ...
        def SetIntegratorNull(self) -> None: ...
        def SetISTDFlagNull(self) -> None: ...
        def IsLibraryMatchScoreNull(self) -> bool: ...
        def SetRightRetentionTimeDeltaNull(self) -> None: ...
        def IsRetentionTimeDeltaUnitsNull(self) -> bool: ...
        def IsCellAcceleratorVoltageNull(self) -> bool: ...
        def IsLeftRetentionTimeDeltaNull(self) -> bool: ...
        def IsCompoundMathNull(self) -> bool: ...
        def IsCompoundTypeNull(self) -> bool: ...
        def SetMolecularFormulaNull(self) -> None: ...
        def IsReferenceMSPathNameNull(self) -> bool: ...
        def IsUserAnnotationNull(self) -> bool: ...
        def IsMZAdditionalNull(self) -> bool: ...
        def SetMZScanRangeHighNull(self) -> None: ...
        def IsRetentionTimeWindowUnitsNull(self) -> bool: ...
        def IsRetentionIndexNull(self) -> bool: ...
        def IsMZExtractionWindowFilterRightNull(self) -> bool: ...
        def SetIonPolarityNull(self) -> None: ...
        def IsCompoundNameNull(self) -> bool: ...
        def SetMultiplierNull(self) -> None: ...
        def IsAverageResponseFactorNull(self) -> bool: ...
        def IsMZNull(self) -> bool: ...
        def IsScanTypeNull(self) -> bool: ...
        def SetUserCustomCalculationNull(self) -> None: ...
        def IsUncertaintyRelativeOrAbsoluteNull(self) -> bool: ...
        def SetRetentionIndexNull(self) -> None: ...
        def IsIDNull(self) -> bool: ...
        def SetQuantitateByHeightNull(self) -> None: ...
        def IsRetentionTimeNull(self) -> bool: ...
        def SetRetentionTimeDeltaUnitsNull(self) -> None: ...
        def SetUserDefined2Null(self) -> None: ...
        def IsRetentionTimeWindowNull(self) -> bool: ...
        def IsUserCustomCalculationNull(self) -> bool: ...
        def SetMZAdditionalNull(self) -> None: ...
        def SetAverageResponseFactorNull(self) -> None: ...
        def IsConcentrationUnitsNull(self) -> bool: ...
        def SetUncertaintyRelativeOrAbsoluteNull(self) -> None: ...
        def SetCellAcceleratorVoltageNull(self) -> None: ...
        def SetCompoundMathNull(self) -> None: ...
        def IsISTDConcentrationNull(self) -> bool: ...

    class TargetCompoundRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
        )  # readonly

    class TargetCompoundRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRowChangeEvent,
        ) -> None: ...

    class TargetMatchMethodDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow
        ],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow
        ],
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        BatchIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        HitConcentrationEstimationColumn: System.Data.DataColumn  # readonly
        HitContainsQualifierIonsColumn: System.Data.DataColumn  # readonly
        HitContainsQuantifierIonColumn: System.Data.DataColumn  # readonly
        HitQualifierRatioWithinRangeColumn: System.Data.DataColumn  # readonly
        HitWithinTargetRTWindowColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow
        ): ...
        ManualResponseFactorColumn: System.Data.DataColumn  # readonly
        MatchCASNumberColumn: System.Data.DataColumn  # readonly
        MatchCompoundNameColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        TargetFinalConcentrationRequiredColumn: System.Data.DataColumn  # readonly
        TargetMatchMethodIDColumn: System.Data.DataColumn  # readonly
        TargetQualifierIonRatiosWithinRangeRequiredColumn: (
            System.Data.DataColumn
        )  # readonly
        TargetQualifierIonRequiredColumn: System.Data.DataColumn  # readonly
        TargetResponseRequiredColumn: System.Data.DataColumn  # readonly

        def FindByBatchIDSampleIDTargetMatchMethodID(
            self, BatchID: int, SampleID: int, TargetMatchMethodID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow
        ): ...
        def RemoveTargetMatchMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def Clone(self) -> System.Data.DataTable: ...
        @overload
        def AddTargetMatchMethodRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow,
        ) -> None: ...
        @overload
        def AddTargetMatchMethodRow(
            self,
            BatchID: int,
            SampleID: int,
            TargetMatchMethodID: int,
            TargetFinalConcentrationRequired: bool,
            TargetResponseRequired: bool,
            TargetQualifierIonRatiosWithinRangeRequired: bool,
            TargetQualifierIonRequired: bool,
            HitContainsQuantifierIon: bool,
            HitContainsQualifierIons: bool,
            HitQualifierRatioWithinRange: bool,
            HitWithinTargetRTWindow: bool,
            ManualResponseFactor: float,
            MatchCompoundName: bool,
            MatchCASNumber: bool,
            HitConcentrationEstimation: str,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow
        ): ...
        def NewTargetMatchMethodRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow
        ): ...

        TargetMatchMethodRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRowChangeEventHandler
        )  # Event
        TargetMatchMethodRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRowChangeEventHandler
        )  # Event
        TargetMatchMethodRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRowChangeEventHandler
        )  # Event
        TargetMatchMethodRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRowChangeEventHandler
        )  # Event

    class TargetMatchMethodRow(System.Data.DataRow):  # Class
        BatchID: int
        HitConcentrationEstimation: str
        HitContainsQualifierIons: bool
        HitContainsQuantifierIon: bool
        HitQualifierRatioWithinRange: bool
        HitWithinTargetRTWindow: bool
        ManualResponseFactor: float
        MatchCASNumber: bool
        MatchCompoundName: bool
        SampleID: int
        SampleRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleRow
        )
        TargetFinalConcentrationRequired: bool
        TargetMatchMethodID: int
        TargetQualifierIonRatiosWithinRangeRequired: bool
        TargetQualifierIonRequired: bool
        TargetResponseRequired: bool

        def SetManualResponseFactorNull(self) -> None: ...
        def IsManualResponseFactorNull(self) -> bool: ...

    class TargetMatchMethodRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRow
        )  # readonly

    class TargetMatchMethodRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodRowChangeEvent,
        ) -> None: ...

    class TargetQualifierDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow
        ],
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        BatchIDColumn: System.Data.DataColumn  # readonly
        CollisionEnergyColumn: System.Data.DataColumn  # readonly
        CompoundIDColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        FragmentorVoltageColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow
        ): ...
        MZColumn: System.Data.DataColumn  # readonly
        MZExtractionWindowFilterLeftColumn: System.Data.DataColumn  # readonly
        MZExtractionWindowFilterRightColumn: System.Data.DataColumn  # readonly
        MZExtractionWindowUnitsColumn: System.Data.DataColumn  # readonly
        QualifierIDColumn: System.Data.DataColumn  # readonly
        RelativeResponseColumn: System.Data.DataColumn  # readonly
        SampleIDColumn: System.Data.DataColumn  # readonly
        SelectedMZColumn: System.Data.DataColumn  # readonly
        UncertaintyColumn: System.Data.DataColumn  # readonly

        def RemoveTargetQualifierRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        def FindByBatchIDSampleIDCompoundIDQualifierID(
            self, BatchID: int, SampleID: int, CompoundID: int, QualifierID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow
        ): ...
        def NewTargetQualifierRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        @overload
        def AddTargetQualifierRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow,
        ) -> None: ...
        @overload
        def AddTargetQualifierRow(
            self,
            BatchID: int,
            SampleID: int,
            CompoundID: int,
            QualifierID: int,
            CollisionEnergy: float,
            FragmentorVoltage: float,
            MZ: float,
            MZExtractionWindowUnits: str,
            MZExtractionWindowFilterLeft: float,
            MZExtractionWindowFilterRight: float,
            RelativeResponse: float,
            SelectedMZ: float,
            Uncertainty: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow
        ): ...

        TargetQualifierRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRowChangeEventHandler
        )  # Event
        TargetQualifierRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRowChangeEventHandler
        )  # Event
        TargetQualifierRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRowChangeEventHandler
        )  # Event
        TargetQualifierRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRowChangeEventHandler
        )  # Event

    class TargetQualifierRow(System.Data.DataRow):  # Class
        BatchID: int
        CollisionEnergy: float
        CompoundID: int
        FragmentorVoltage: float
        MZ: float
        MZExtractionWindowFilterLeft: float
        MZExtractionWindowFilterRight: float
        MZExtractionWindowUnits: str
        QualifierID: int
        RelativeResponse: float
        SampleID: int
        SelectedMZ: float
        TargetCompoundRowParent: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
        )
        Uncertainty: float

        def SetMZNull(self) -> None: ...
        def SetCollisionEnergyNull(self) -> None: ...
        def SetMZExtractionWindowUnitsNull(self) -> None: ...
        def IsUncertaintyNull(self) -> bool: ...
        def IsFragmentorVoltageNull(self) -> bool: ...
        def SetSelectedMZNull(self) -> None: ...
        def GetPeakQualifierRows(
            self,
        ) -> List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierRow
        ]: ...
        def IsMZExtractionWindowUnitsNull(self) -> bool: ...
        def IsMZNull(self) -> bool: ...
        def IsRelativeResponseNull(self) -> bool: ...
        def SetFragmentorVoltageNull(self) -> None: ...
        def SetMZExtractionWindowFilterRightNull(self) -> None: ...
        def IsSelectedMZNull(self) -> bool: ...
        def SetMZExtractionWindowFilterLeftNull(self) -> None: ...
        def IsCollisionEnergyNull(self) -> bool: ...
        def SetRelativeResponseNull(self) -> None: ...
        def SetUncertaintyNull(self) -> None: ...
        def IsMZExtractionWindowFilterLeftNull(self) -> bool: ...
        def IsMZExtractionWindowFilterRightNull(self) -> bool: ...

    class TargetQualifierRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRow
        )  # readonly

    class TargetQualifierRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierRowChangeEvent,
        ) -> None: ...

class UnknownsAnalysisException(
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
