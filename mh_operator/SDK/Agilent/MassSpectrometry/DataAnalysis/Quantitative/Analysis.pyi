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

from . import (
    AppCommandContext,
    BatchAttributes,
    BatchDataSet,
    BracketingType,
    CalibrationCurveFit,
    CalibrationLevel,
    CompoundType,
    IBatchRow,
    ICalibrationRow,
    ICustomExpressions,
    IMSDataAccess,
    IQuantDataSet,
    IScriptableBatch,
    IScriptableCompound,
    IScriptableQualifierIon,
    IScriptableQuantifierIon,
    IScriptableSample,
    ITargetCompoundRow,
    OptimizedQuantDataSet,
    QuantitationDataSet,
    RowIdBase,
    SampleType,
    SpectrumExtractionOverride,
    TargetCompoundRowId,
    TargetQualifierRowId,
)
from .Compliance import ICompliance

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis

class AnalysisContext:  # Class
    BatchDataSet: QuantitationDataSet  # readonly

    def GetTargetCompoundChromatogram(
        self, batchId: int, sampleId: int, compoundId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...
    def NotifyAnalysisStart(self, totalSteps: int) -> None: ...
    def NotifyAnalysisEnd(self) -> None: ...
    def NotifyAnalysisStep(self, step: int, analysisTarget: str) -> None: ...
    def GetBatchFilePath(self, batchId: int) -> str: ...
    def MergeBatchDataSet(self, dataset: QuantitationDataSet, batchId: int) -> None: ...
    def GetTargetQualifierChromatogram(
        self, batchId: int, sampleId: int, compoundId: int, qualifierId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...

class Batch(
    System.IDisposable,
    IScriptableBatch,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.BatchAnalysisBase,
):  # Class
    BatchAnalyzer: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.BatchAnalyzer
    )  # readonly
    BatchAttributes: BatchAttributes  # readonly
    BatchID: int  # readonly
    BracketingType: BracketingType
    DataSet: BatchDataSet  # readonly
    SampleCount: int  # readonly

    def GetCalibrationReferenceSample(
        self,
        referringSample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample: ...
    def ValidateBatchMethod(self) -> None: ...
    def _OnBatchLoaded(self, dataSet: QuantitationDataSet, batchId: int) -> None: ...
    def RemoveCalibration(
        self, compoundIds: List[int], levelNames: List[str], levelTypes: List[str]
    ) -> None: ...
    def GetCompoundReferenceSet(
        self,
        targetSample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample,
        compoundId: int,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound]: ...
    def GetSample(
        self, sampleId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample: ...
    def Quantitate(self) -> None: ...
    def GetDependentSamples(
        self,
        calSample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CalibrationSample,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample]: ...
    @overload
    @staticmethod
    def IsSampleSkipped(rowId: RowIdBase) -> bool: ...
    @overload
    @staticmethod
    def IsSampleSkipped(sampleId: int) -> bool: ...
    @overload
    def GetCompounds(
        self,
        compoundRows: System.Collections.Generic.List[
            QuantitationDataSet.TargetCompoundRow
        ],
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    @overload
    def GetCompounds(
        self, sampleType: SampleType
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    @overload
    def GetCompounds(
        self, sampleTypes: List[SampleType]
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    @overload
    def GetCompounds(
        self, sampleType: SampleType, compoundType: CompoundType
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    def GetCalibrationSamples(
        self,
        targetSample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CalibrationSample
    ]: ...
    def GetISTDCompounds(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    def GetTargetCompounds(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    def PrepareToEditMethodWithSample(self, sampleId: int) -> None: ...
    def Integrate(self) -> None: ...
    def GetMatrixCompounds(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    @overload
    def GetNonISTDCompounds(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    @overload
    def GetNonISTDCompounds(
        self, sampleType: SampleType
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    @overload
    def GetNonISTDCompounds(
        self, sampleTypes: List[SampleType]
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    @overload
    def GetSamples(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample
    ]: ...
    @overload
    def GetSamples(
        self, sampleType: SampleType
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample
    ]: ...
    @overload
    def GetSamples(
        self, sampleTypes: List[SampleType]
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample
    ]: ...
    def Analyze(self) -> None: ...
    @overload
    def ClearCalibration(self) -> None: ...
    @overload
    def ClearCalibration(
        self, compoundIds: List[int], levleNames: List[str], levelTypes: List[str]
    ) -> None: ...
    def _OnBatchAnalyzed(self, dataSet: QuantitationDataSet, batchId: int) -> None: ...
    @overload
    def Calibrate(self, average: bool) -> None: ...
    @overload
    def Calibrate(
        self,
        compoundIds: List[int],
        levelConcentrations: List[Optional[float]],
        calSampleIds: List[int],
        average: bool,
    ) -> None: ...
    def CancelBatchProcessing(self) -> None: ...
    def GetCalibrationReferenceCompound(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound: ...
    @overload
    def GetCompoundsExceptFromSampleTypes(
        self, excludedSampleTypes: List[SampleType]
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    @overload
    def GetCompoundsExceptFromSampleTypes(
        self, compoundType: CompoundType, excludedSampleTypes: List[SampleType]
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    def GetAllCompounds(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    @staticmethod
    def EnsureOpenLibraries(
        compliance: ICompliance, batchAttributes: BatchAttributes
    ) -> None: ...
    def CheckSampleTypeForAnalysis(self, sampleId: int) -> None: ...
    def ClearResults(self) -> None: ...
    def _OnBatchAnalysisStarting(
        self, dataSet: QuantitationDataSet, batchId: int
    ) -> None: ...
    def GetSamplesExceptForTypes(
        self, excludedSampleTypes: List[SampleType]
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample
    ]: ...

    BatchAnalyzed: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.BatchAnalyzedEventHandler
    )  # Event
    CompoundListChanged: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundListChangedEventHandler
    )  # Event
    OptimizedBatchAnalysisCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.OptimizedBatchAnalysisCompletedEventHandler
    )  # Event
    OptimizedBatchAnalysisStarting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.OptimizedBatchAnalysisStartingEventHandler
    )  # Event
    SampleDeleted: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.SampleDeletedEventHandler
    )  # Event
    SampleRowSkipped: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.SampleRowSkippedEventHandler
    )  # Event

class BatchAnalysisBase(System.IDisposable):  # Class
    DataSet: BatchDataSet  # readonly
    TraceString: str  # readonly

    def IsDirty(self) -> bool: ...
    def Dispose(self) -> None: ...

class BatchAnalysisContext:  # Class
    CurrentBatch: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Batch
    )  # static # readonly

    @staticmethod
    def GetActiveBatch() -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Batch
    ): ...
    @staticmethod
    def CloseBatch() -> None: ...
    @staticmethod
    def GetQualifier(
        rowId: TargetQualifierRowId,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.QualifierIon: ...
    @staticmethod
    def GetCompound(
        rowId: TargetCompoundRowId,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound: ...
    @staticmethod
    def OpenBatch(
        commandContext: AppCommandContext, batchId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Batch: ...
    @staticmethod
    def ValidateActiveBatch(batchId: int) -> None: ...
    @staticmethod
    def ValidateRowId(rowId: RowIdBase) -> None: ...

class BatchAnalyzedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, args: System.EventArgs) -> None: ...

class BatchAnalyzer(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.IQuantDataSetLookup
):  # Class
    def __init__(
        self, batch: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Batch
    ) -> None: ...

    SampleAnalyzers: System.Collections.Generic.SortedList[
        int, Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.SampleAnalyzer
    ]  # readonly

    def GetCompoundReferenceSet(
        self,
        targetSampleAnalyzer: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.SampleAnalyzer,
        compoundID: int,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundAnalyzer
    ]: ...
    def GetDataSet(self, sampleID: int) -> IQuantDataSet: ...
    def Quantitate(self, parallel: bool) -> None: ...
    def GetCalibrationSamples(
        self,
        targetSample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.SampleAnalyzer
    ]: ...
    def Analyze(self, parallel: bool) -> None: ...
    @overload
    def GetOptimizedCompoundRow(
        self, sampleID: int, compoundID: int
    ) -> ITargetCompoundRow: ...
    @overload
    def GetOptimizedCompoundRow(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound,
    ) -> ITargetCompoundRow: ...
    @overload
    def GetSampleRow(self, sampleID: int) -> IBatchRow: ...
    @overload
    def GetSampleRow(
        self, sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample
    ) -> IBatchRow: ...
    def Integrate(self, parallel: bool) -> None: ...
    def Calibrate(self, parallel: bool) -> None: ...
    def GetCalibrationReferenceCompoundAnalyzer(
        self,
        compoundAnalyzer: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundAnalyzer,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundAnalyzer
    ): ...

class BatchAnalyzer:  # Class
    def __init__(self) -> None: ...

class CalibrationChangedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, args: System.EventArgs) -> None: ...

class CalibrationSample(
    IScriptableSample,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        batch: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Batch,
        sampleId: int,
    ) -> None: ...

    LevelName: str  # readonly

    CalibrationChanged: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CalibrationChangedEventHandler
    )  # Event

class ChromPeakDeconvolution:  # Class
    @overload
    def __init__(self, dataAccess: IMSDataAccess) -> None: ...
    @overload
    def __init__(
        self, dataAccess: Agilent.MassSpectrometry.DataAnalysis.IDataAccess
    ) -> None: ...

    RTRange: Agilent.MassSpectrometry.DataAnalysis.IRange  # readonly

    @staticmethod
    def RescaleComponentSpectrum(
        targetComponent: Agilent.MassSpectrometry.DataAnalysis.Component,
        peakAveragedSpectrum: Agilent.MassSpectrometry.DataAnalysis.ISpectrum,
        targetPurity: float,
    ) -> None: ...
    @overload
    def ComputePeakPurity(
        self,
        peak: Agilent.MassSpectrometry.DataAnalysis.IChromPeak,
        compoundRow: ITargetCompoundRow,
        spectralComponents: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Component
        ],
        targetComponent: Agilent.MassSpectrometry.DataAnalysis.Component,
    ) -> float: ...
    @overload
    def ComputePeakPurity(
        self,
        peak: Agilent.MassSpectrometry.DataAnalysis.IChromPeak,
        spectralComponents: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Component
        ],
        targetComponent: Agilent.MassSpectrometry.DataAnalysis.Component,
    ) -> float: ...
    @overload
    def GetSpectralComponents(
        self,
        peak: Agilent.MassSpectrometry.DataAnalysis.IChromPeak,
        compoundRow: ITargetCompoundRow,
    ) -> Dict[
        Agilent.MassSpectrometry.DataAnalysis.Component,
        System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Component
        ],
    ]: ...
    @overload
    def GetSpectralComponents(
        self,
        peak: Agilent.MassSpectrometry.DataAnalysis.IChromPeak,
        mzRange: Agilent.MassSpectrometry.DataAnalysis.IRange,
    ) -> Dict[
        Agilent.MassSpectrometry.DataAnalysis.Component,
        System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Component
        ],
    ]: ...
    @overload
    def GetSpectralComponents(
        self,
        peak: Agilent.MassSpectrometry.DataAnalysis.IChromPeak,
        compoundRow: ITargetCompoundRow,
        deconvolutionMethods: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
    ) -> Dict[
        Agilent.MassSpectrometry.DataAnalysis.Component,
        System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Component
        ],
    ]: ...
    @overload
    def GetSpectralComponents(
        self,
        peak: Agilent.MassSpectrometry.DataAnalysis.IChromPeak,
        mzRange: Agilent.MassSpectrometry.DataAnalysis.IRange,
        deconvolutionMethods: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
    ) -> Dict[
        Agilent.MassSpectrometry.DataAnalysis.Component,
        System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Component
        ],
    ]: ...

class Compound(
    IScriptableCompound,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.BatchAnalysisBase,
):  # Class
    def __init__(
        self,
        sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample,
        compoundId: int,
    ) -> None: ...

    Calibration: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundCalibration
    )  # readonly
    CompoundID: int  # readonly
    CompoundRow: QuantitationDataSet.TargetCompoundRow  # readonly
    CompoundSpectrum: Agilent.MassSpectrometry.DataAnalysis.ISpectrum  # readonly
    CompoundSpectrumForReferenceLibraryMatch: (
        Agilent.MassSpectrometry.DataAnalysis.ISpectrum
    )  # readonly
    CompoundType: CompoundType  # readonly
    DataSet: BatchDataSet  # readonly
    Dependents: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]  # readonly
    HasDependents: bool  # readonly
    HasTimeReference: bool  # readonly
    IsAreaCorrectionEnabled: bool  # readonly
    IsCompoundOrDependentsAreaCorrected: bool  # readonly
    IsISTD: bool  # readonly
    IsManuallyIntegrated: bool  # readonly
    Qualifiers: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.QualifierIon
    ]  # readonly
    Quantifier: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.QuantifierIon
    )  # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample
    )  # readonly
    SpectrumExtractionOverride: SpectrumExtractionOverride  # readonly

    def Quantitate(self) -> None: ...
    def _OnCompoundCalibrationStarting(
        self, compoundRow: QuantitationDataSet.TargetCompoundRow, average: bool
    ) -> None: ...
    def _OnCompoundQuantitated(
        self, compoundRow: QuantitationDataSet.TargetCompoundRow
    ) -> None: ...
    def GetAggregateCompound(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    def _IgnoreQuantitationErrors(
        self,
        compoundRow: QuantitationDataSet.TargetCompoundRow,
        manuallyIntegrated: bool,
    ) -> bool: ...
    def GetQualifier(
        self, qualifierId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.QualifierIon: ...
    def GetGroupCompounds(
        self, groupName: str
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    def _OnCompoundIntegrationStarting(
        self, compoundRow: QuantitationDataSet.TargetCompoundRow
    ) -> None: ...
    def _OnCompoundQuantitationFailed(
        self, compoundRow: QuantitationDataSet.TargetCompoundRow
    ) -> None: ...
    def HasISTD(self) -> bool: ...
    def Integrate(self, startFromScratch: bool) -> None: ...
    def _OnCompoundCalibrated(
        self, compoundRow: QuantitationDataSet.TargetCompoundRow, average: bool
    ) -> None: ...
    def Calibrate(
        self,
        calSampleIds: List[int],
        levelConcentration: Optional[float],
        average: bool,
    ) -> None: ...
    def _IgnorePeakNotFoundException(
        self,
        compoundRow: QuantitationDataSet.TargetCompoundRow,
        e: System.ApplicationException,
        manuallyIntegrated: bool,
    ) -> bool: ...
    def _OnCompoundIntegrated(
        self, compoundRow: QuantitationDataSet.TargetCompoundRow
    ) -> None: ...
    def GetISTD(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound: ...
    def _OnCompoundQuantitationStarting(
        self, compoundRow: QuantitationDataSet.TargetCompoundRow
    ) -> None: ...

    CompoundIntegrated: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundQuantitationEventHandler
    )  # Event
    CompoundQuantitated: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundQuantitationEventHandler
    )  # Event
    CompoundQuantitationFailed: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundQuantitationEventHandler
    )  # Event
    OptimizedCompoundQuantitated: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.OptimizedCompoundEventHandler
    )  # Event
    QuantitationChanged: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundQuantitationEventHandler
    )  # Event

class CompoundAnalyzer:  # Class
    Calibrator: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundCalibrator
    )  # readonly
    CompoundID: int  # readonly
    CompoundSpectrumForReferenceLibraryMatch: (
        Agilent.MassSpectrometry.DataAnalysis.ISpectrum
    )  # readonly
    ISTDCompoundAnalyzer: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundAnalyzer
    )  # readonly
    IsISTD: bool  # readonly

class CompoundCalibration(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.BatchAnalysisBase,
):  # Class
    CalCurveFit: CalibrationCurveFit  # readonly
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    )  # readonly
    DataSet: BatchDataSet  # readonly

    def GetCalRowsByLevel(
        self, levelNames: System.Collections.Generic.List[str]
    ) -> Dict[str, System.Collections.Generic.List[ICalibrationRow]]: ...
    def GetISTDConcentration(self) -> float: ...
    @staticmethod
    def GetResponseStatisticsByLevel(
        rowId: TargetCompoundRowId,
    ) -> List[CalibrationLevel]: ...
    @staticmethod
    def ApplyIsotopicDilutionCorrection(
        rowId: TargetCompoundRowId, relResponses: List[float]
    ) -> None: ...

class CompoundCalibrator:  # Class
    def __init__(
        self,
        compoundAnalyzer: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundAnalyzer,
    ) -> None: ...
    def GetISTDConcentration(self) -> float: ...

class CompoundListChangedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, args: System.EventArgs) -> None: ...

class CompoundQuantitationEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, args: System.EventArgs) -> None: ...

class IQuantDataSetLookup(object):  # Interface
    @overload
    def GetSampleRow(self, sampleID: int) -> IBatchRow: ...
    @overload
    def GetSampleRow(
        self, sample: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample
    ) -> IBatchRow: ...
    def GetDataSet(self, sampleID: int) -> IQuantDataSet: ...
    @overload
    def GetOptimizedCompoundRow(
        self, sampleID: int, compoundID: int
    ) -> ITargetCompoundRow: ...
    @overload
    def GetOptimizedCompoundRow(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound,
    ) -> ITargetCompoundRow: ...

class IntegratorPSetCache:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, nSamples: int, nCompounds: int, nQualifiers: int) -> None: ...
    def AddTimeSegments(self, sampleID: int, timeSegments: List[float]) -> None: ...

class ManualIntegrationEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, args: System.EventArgs) -> None: ...

class ManualIntegrationResult:  # Class
    ResponseRatioOriginal: float  # readonly

class MeasuredIon(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.BatchAnalysisBase,
):  # Class
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    )  # readonly
    DataSet: BatchDataSet  # readonly
    IntegrationErrorMessage: str  # readonly
    ManuallyIntegrated: bool
    NoiseRegions: Agilent.MassSpectrometry.DataAnalysis.RangeCollection  # readonly
    Response: float  # readonly
    SpectralComponents: List[
        Agilent.MassSpectrometry.DataAnalysis.Component
    ]  # readonly
    TargetComponent: Agilent.MassSpectrometry.DataAnalysis.Component  # readonly
    TargetComponentArea: Optional[float]  # readonly
    UserSelectedPeak: Agilent.MassSpectrometry.DataAnalysis.IChromPeak  # readonly
    UserSelectedPeakIndex: int  # readonly

    @staticmethod
    def CalcDeconvolutedValues(
        component: Agilent.MassSpectrometry.DataAnalysis.Component,
        area: Optional[float],
        height: Optional[float],
    ) -> None: ...
    @overload
    def FindSpectralComponents(self) -> None: ...
    @overload
    def FindSpectralComponents(
        self, peakRow: QuantitationDataSet.PeakRow
    ) -> Optional[float]: ...
    def GetPeaksInRange(
        self, xMin: float, xMax: float
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.IChromPeak]: ...
    def FindPeaks(self) -> Agilent.MassSpectrometry.DataAnalysis.IChromPeakList: ...
    def ClearManualIntegration(self) -> None: ...
    def SnapBaseline(self, xStart: float, xEnd: float) -> None: ...
    def ManualIntegrate(
        self, xStart: float, yStart: float, xEnd: float, yEnd: float
    ) -> None: ...

    ManualIntegrationChanged: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.ManualIntegrationEventHandler
    )  # Event
    ManualIntegrationCleared: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.ManualIntegrationEventHandler
    )  # Event

class OptimizedBatchAnalysisCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, args: System.EventArgs) -> None: ...

class OptimizedBatchAnalysisStartingEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.OptimizedBatchEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.OptimizedBatchEventArgs,
    ) -> None: ...

class OptimizedBatchEventArgs:  # Class
    def __init__(
        self, childDataSets: System.Collections.Generic.List[IQuantDataSet]
    ) -> None: ...

    ChildDataSets: System.Collections.Generic.List[IQuantDataSet]  # readonly

class OptimizedCompoundEventArgs:  # Class
    CompoundRow: ITargetCompoundRow  # readonly

class OptimizedCompoundEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.OptimizedCompoundEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.OptimizedCompoundEventArgs,
    ) -> None: ...

class ProcessingState(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Dirty: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.ProcessingState
    ) = ...  # static # readonly
    Initialized: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.ProcessingState
    ) = ...  # static # readonly
    Processed: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.ProcessingState
    ) = ...  # static # readonly

class Qualifier(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.TargetIon
):  # Class
    ...

class QualifierIon(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.MeasuredIon,
    IScriptableQualifierIon,
):  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound,
        qualifierId: int,
    ) -> None: ...

    Chromatogram: Agilent.MassSpectrometry.DataAnalysis.IChromatogram  # readonly
    PeakQualifierRow: QuantitationDataSet.PeakQualifierRow  # readonly
    QualifierID: int  # readonly
    Response: float  # readonly
    TargetQualifierRow: QuantitationDataSet.TargetQualifierRow  # readonly

    def MergePeak(self, withLeft: bool, snap: bool) -> None: ...
    @staticmethod
    def IsValidManuallyIntegratedPeak(
        peakQualifierRow: QuantitationDataSet.PeakQualifierRow,
    ) -> bool: ...
    def ZeroOutPeak(self) -> None: ...
    def _OnManualIntegrationCompleted(
        self,
        qualifierRow: QuantitationDataSet.TargetQualifierRow,
        peakList: Agilent.MassSpectrometry.DataAnalysis.IPeakList,
    ) -> None: ...
    def SplitPeak(self, isLeftPrimary: bool, snap: bool) -> None: ...
    def _OnManualIntegrationStarting(
        self,
        qualifierRow: QuantitationDataSet.TargetQualifierRow,
        peakList: Agilent.MassSpectrometry.DataAnalysis.IPeakList,
        xStart: float,
        xEnd: float,
        yStart: float,
        yEnd: float,
    ) -> None: ...
    def DropBaseline(self, y: float) -> None: ...
    def _OnFindPeaksCompleted(
        self,
        qualifierRow: QuantitationDataSet.TargetQualifierRow,
        peakList: Agilent.MassSpectrometry.DataAnalysis.IPeakList,
    ) -> None: ...
    def SelectPeak(self, peakId: int) -> None: ...
    def _OnFindPeaksStarting(
        self, qualifierRow: QuantitationDataSet.TargetQualifierRow
    ) -> None: ...

class QuantEngine(System.IDisposable):  # Class
    def StartSet(self, sortBySignal: bool) -> None: ...
    def Dispose(self) -> None: ...
    def EndSet(
        self, sortBySignal: bool, correlationWindowInMilliseconds: int
    ) -> None: ...
    def AddPeaks(
        self, peakList: Agilent.MassSpectrometry.DataAnalysis.IPeakList, signalId: int
    ) -> None: ...

class Quantifier(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.TargetIon
):  # Class
    @staticmethod
    def CalcDeconvolutedValues(
        component: Agilent.MassSpectrometry.DataAnalysis.Component,
        area: Optional[float],
        height: Optional[float],
    ) -> None: ...
    def FindSpectralComponents(self) -> None: ...

class QuantifierIon(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.MeasuredIon,
    System.IDisposable,
    IScriptableQuantifierIon,
    ICustomExpressions,
):  # Class
    def __init__(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound,
    ) -> None: ...

    CONFIG_XML_FILE: str = ...  # static # readonly

    Chromatogram: Agilent.MassSpectrometry.DataAnalysis.IChromatogram  # readonly
    PeakRow: QuantitationDataSet.PeakRow  # readonly
    Response: float  # readonly
    UncorrectedResponse: float  # readonly

    def MergePeak(self, withLeft: bool, snap: bool) -> None: ...
    @overload
    def ZeroOutPeak(self) -> None: ...
    @overload
    def ZeroOutPeak(self, peakId: int) -> None: ...
    def _OnManualIntegrationCompleted(
        self,
        compoundRow: QuantitationDataSet.TargetCompoundRow,
        peakList: Agilent.MassSpectrometry.DataAnalysis.IPeakList,
    ) -> None: ...
    def _UpdateFinalConcentration(
        self, peakRow: QuantitationDataSet.PeakRow
    ) -> None: ...
    def SplitPeak(self, isLeftPrimary: bool, snap: bool) -> None: ...
    def _OnManualIntegrationStarting(
        self,
        compoundRow: QuantitationDataSet.TargetCompoundRow,
        peakList: Agilent.MassSpectrometry.DataAnalysis.IPeakList,
        xStart: float,
        xEnd: float,
        yStart: float,
        yEnd: float,
    ) -> None: ...
    def _UpdateAccuracy(self, peakRow: QuantitationDataSet.PeakRow) -> None: ...
    def DropBaseline(self, y: float) -> None: ...
    def _OnFindPeaksCompleted(
        self,
        compoundRow: QuantitationDataSet.TargetCompoundRow,
        peakList: Agilent.MassSpectrometry.DataAnalysis.IPeakList,
    ) -> None: ...
    def SelectPeak(self, peakId: int) -> None: ...
    def _OnFindPeaksStarting(
        self, compoundRow: QuantitationDataSet.TargetCompoundRow
    ) -> None: ...

class QuantitationEngine:  # Class
    def Quantitate(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound,
        bComputeConcentration: bool,
        clearManualIntegration: bool,
    ) -> None: ...
    def IntegrateCompound(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound,
    ) -> None: ...

class Sample(
    IScriptableSample,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.BatchAnalysisBase,
):  # Class
    def __init__(
        self,
        batch: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Batch,
        sampleId: int,
    ) -> None: ...

    Batch: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Batch  # readonly
    CalibrationSamples: Dict[
        str,
        System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CalibrationSample
        ],
    ]  # readonly
    DataAccess: IMSDataAccess  # readonly
    DataSet: BatchDataSet  # readonly
    Deconvolution: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.ChromPeakDeconvolution
    )  # readonly
    QuantitationEngine: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.QuantitationEngine
    )  # readonly
    SampleID: int  # readonly
    SampleRow: QuantitationDataSet.BatchRow  # readonly
    SampleType: SampleType  # readonly
    TraceString: str  # readonly

    def Quantitate(self) -> None: ...
    def _OnSampleIntegrationStarting(
        self, sampleRow: QuantitationDataSet.BatchRow
    ) -> None: ...
    def GetISTDCompounds(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    def GetCalibrationSamples(
        self, levelName: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CalibrationSample
    ]: ...
    def GetTICResponse(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound,
        rt: float,
    ) -> float: ...
    @staticmethod
    def SortByDateTime(
        samples: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Sample
        ],
    ) -> None: ...
    def ContainsCompound(self, compoundId: int) -> bool: ...
    def _OnSampleCalibrated(
        self, sampleRow: QuantitationDataSet.BatchRow, average: bool
    ) -> None: ...
    @overload
    def GetCompounds(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    @overload
    def GetCompounds(
        self, compoundType: CompoundType
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    def GetCompound(
        self, compoundId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound: ...
    def _OnSampleCalibrationStarting(
        self, sampleRow: QuantitationDataSet.BatchRow, average: bool
    ) -> None: ...
    def GetNonISTDCompounds(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    def _OnSampleIntegrated(self, sampleRow: QuantitationDataSet.BatchRow) -> None: ...
    def Integrate(self, clearResults: bool) -> None: ...
    def _OnSampleQuantitated(self, sampleRow: QuantitationDataSet.BatchRow) -> None: ...
    def Calibrate(self, average: bool) -> None: ...
    def GetTargetCompounds(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound
    ]: ...
    def FindCompound(
        self, compoundId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.Compound: ...
    def _OnSampleQuantitationStarting(
        self, sampleRow: QuantitationDataSet.BatchRow
    ) -> None: ...

class SampleAnalyzer:  # Class
    SampleDataSet: OptimizedQuantDataSet  # readonly

    def GetTICResponse(
        self,
        cmpdAnalyzer: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Analysis.CompoundAnalyzer,
        rt: float,
    ) -> float: ...

class SampleDeletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, args: System.EventArgs) -> None: ...

class SampleRowSkippedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, args: System.EventArgs) -> None: ...

class TargetIon:  # Class
    ...
