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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Schema

class Batch:  # Class
    AcqDateTime: str = ...  # static # readonly
    AcqMethod: str = ...  # static # readonly
    BatchID: str = ...  # static # readonly
    CalibrationReferenceSampleID: str = ...  # static # readonly
    DataFileName: str = ...  # static # readonly
    DataPathName: str = ...  # static # readonly
    Dilution: str = ...  # static # readonly
    EquilibrationTime: str = ...  # static # readonly
    InjectorVolume: str = ...  # static # readonly
    LevelName: str = ...  # static # readonly
    MatrixType: str = ...  # static # readonly
    QuantitationMessage: str = ...  # static # readonly
    SampleAmount: str = ...  # static # readonly
    SampleGroup: str = ...  # static # readonly
    SampleID: str = ...  # static # readonly
    SampleName: str = ...  # static # readonly
    SamplePosition: str = ...  # static # readonly
    SampleType: str = ...  # static # readonly
    TableName: str = ...  # static # readonly
    TotalSampleAmount: str = ...  # static # readonly

class BatchAttributes:  # Class
    ApplyMultiplierISTD: str = ...  # static # readonly
    ApplyMultiplierSurrogate: str = ...  # static # readonly
    ApplyMultiplierTarget: str = ...  # static # readonly
    BandName: str = ...  # static # readonly
    BatchState: str = ...  # static # readonly
    BracketingType: str = ...  # static # readonly
    CorrelationWindow: str = ...  # static # readonly
    DataVersion: str = ...  # static # readonly
    FeatureDetection: str = ...  # static # readonly
    HashCode: str = ...  # static # readonly
    IgnorePeaksNotFound: str = ...  # static # readonly
    LibraryMethodPathFileName: str = ...  # static # readonly
    LibraryPathFileName: str = ...  # static # readonly
    NonReferenceWindow: str = ...  # static # readonly
    NonReferenceWindowPercentOrMinutes: str = ...  # static # readonly
    RefLibraryPathFileName: str = ...  # static # readonly
    RefLibraryPatternPathFileName: str = ...  # static # readonly
    ReferenceWindow: str = ...  # static # readonly
    ReferenceWindowPercentOrMinutes: str = ...  # static # readonly
    SchemaVersion: str = ...  # static # readonly
    TimeStamp: str = ...  # static # readonly

class Calibration:  # Class
    CalibrationName: str = ...  # static # readonly
    CalibrationSTDPathName: str = ...  # static # readonly
    CalibrationType: str = ...  # static # readonly
    LevelAverageCounter: str = ...  # static # readonly
    LevelConcentration: str = ...  # static # readonly
    LevelEnable: str = ...  # static # readonly
    LevelID: str = ...  # static # readonly
    LevelName: str = ...  # static # readonly
    LevelRSD: str = ...  # static # readonly
    LevelResponse: str = ...  # static # readonly
    LevelResponseFactor: str = ...  # static # readonly
    TableName: str = ...  # static # readonly

class Peak:  # Class
    Accuracy: str = ...  # static # readonly
    Area: str = ...  # static # readonly
    AreaCorrectionResponse: str = ...  # static # readonly
    BaselineEnd: str = ...  # static # readonly
    BaselineStandardDeviation: str = ...  # static # readonly
    BaselineStart: str = ...  # static # readonly
    CalculatedConcentration: str = ...  # static # readonly
    DeltaRetentionTime_: str = ...  # static # readonly
    FinalConcentration: str = ...  # static # readonly
    Height: str = ...  # static # readonly
    ISTDConcentrationRatio: str = ...  # static # readonly
    ISTDRelativeResponseFactor: str = ...  # static # readonly
    ISTDResponseRatio: str = ...  # static # readonly
    IntegrationEndTime: str = ...  # static # readonly
    IntegrationMetricDetail: str = ...  # static # readonly
    IntegrationMetricQualityFlags: str = ...  # static # readonly
    IntegrationQualityMetric: str = ...  # static # readonly
    IntegrationStartTime: str = ...  # static # readonly
    ManuallyIntegrated: str = ...  # static # readonly
    MassMatchScore: str = ...  # static # readonly
    MatrixSpikePercentDeviation: str = ...  # static # readonly
    MatrixSpikePercentRecovery: str = ...  # static # readonly
    QValueComputed: str = ...  # static # readonly
    ReferenceLibraryMatchScore: str = ...  # static # readonly
    RelationISTDCompoundPeak: str = ...  # static # readonly
    RelativeRetentionTime: str = ...  # static # readonly
    ResponseRatio: str = ...  # static # readonly
    RetentionTime: str = ...  # static # readonly
    RetentionTimeDifference: str = ...  # static # readonly
    SelectedGroupRetentionTime: str = ...  # static # readonly
    SelectedTargetRetentionTime: str = ...  # static # readonly
    SignalToNoiseRatio: str = ...  # static # readonly
    SurrogatePercentRecovery: str = ...  # static # readonly
    TargetResponse: str = ...  # static # readonly
    Width: str = ...  # static # readonly

class PeakQualifier:  # Class
    CoelutionScore: str = ...  # static # readonly
    ManuallyIntegrated: str = ...  # static # readonly
    QualifierResponseRatio: str = ...  # static # readonly
    SignalToNoiseRatio: str = ...  # static # readonly

class Relations:  # Class
    FKBatchTargetCompound: str = ...  # static # readonly
    FKPeakPeakQualifier: str = ...  # static # readonly
    FKTargetCompoundCalibration: str = ...  # static # readonly
    FKTargetCompoundPeak: str = ...  # static # readonly
    FKTargetCompoundTargetQualifier: str = ...  # static # readonly
    FKTargetQualifierPeakQualifier: str = ...  # static # readonly
    TargetCompoundISTDCompoundID: str = ...  # static # readonly

class TargetCompound:  # Class
    AccuracyLimitMultiplierLOQ: str = ...  # static # readonly
    AccuracyMaximumPercentDeviation: str = ...  # static # readonly
    AlternativePeakCriteria: str = ...  # static # readonly
    AreaCorrectionFactor: str = ...  # static # readonly
    AreaCorrectionMZ: str = ...  # static # readonly
    AverageRelativeRetentionTime: str = ...  # static # readonly
    AverageResponseFactor: str = ...  # static # readonly
    BatchID: str = ...  # static # readonly
    CASNumber: str = ...  # static # readonly
    CalibraionRangeFilter: str = ...  # static # readonly
    CalibrationReferenceCompoundID: str = ...  # static # readonly
    CollisionEnergy: str = ...  # static # readonly
    CompoundApproved: str = ...  # static # readonly
    CompoundGroup: str = ...  # static # readonly
    CompoundID: str = ...  # static # readonly
    CompoundMath: str = ...  # static # readonly
    CompoundName: str = ...  # static # readonly
    CompoundType: str = ...  # static # readonly
    ConcentrationUnits: str = ...  # static # readonly
    CurveFit: str = ...  # static # readonly
    CurveFitLimitHigh: str = ...  # static # readonly
    CurveFitLimitLow: str = ...  # static # readonly
    CurveFitMinimumR2: str = ...  # static # readonly
    CurveFitOrigin: str = ...  # static # readonly
    CurveFitR2: str = ...  # static # readonly
    CurveFitStatus: str = ...  # static # readonly
    CurveFitWeight: str = ...  # static # readonly
    DilutionHighestConcentration: str = ...  # static # readonly
    DilutionPattern: str = ...  # static # readonly
    ExpectedConcentration: str = ...  # static # readonly
    FragmentorVoltage: str = ...  # static # readonly
    ID: str = ...  # static # readonly
    ISTDCompoundID: str = ...  # static # readonly
    ISTDConcentration: str = ...  # static # readonly
    ISTDFlag: str = ...  # static # readonly
    ISTDResponseLimitHigh: str = ...  # static # readonly
    ISTDResponseLimitLow: str = ...  # static # readonly
    IntegrationParameters: str = ...  # static # readonly
    IntegrationParametersModified: str = ...  # static # readonly
    Integrator: str = ...  # static # readonly
    IonPolarity: str = ...  # static # readonly
    IonSource: str = ...  # static # readonly
    LeftRetentionTimeDelta: str = ...  # static # readonly
    LimitOfDetection: str = ...  # static # readonly
    LimitOfQuantitation: str = ...  # static # readonly
    MZ: str = ...  # static # readonly
    MZExtractionWindowFilterLeft: str = ...  # static # readonly
    MZExtractionWindowFilterRight: str = ...  # static # readonly
    MZExtractionWindowUnits: str = ...  # static # readonly
    MZScanRangeHigh: str = ...  # static # readonly
    MZScanRangeLow: str = ...  # static # readonly
    MatrixAConcentrationLimitHigh: str = ...  # static # readonly
    MatrixAConcentrationLimitLow: str = ...  # static # readonly
    MatrixBConcentrationLimitHigh: str = ...  # static # readonly
    MatrixBConcentrationLimitLow: str = ...  # static # readonly
    MatrixSpikeConcentration: str = ...  # static # readonly
    MatrixSpikeMaximumPercentDeviation: str = ...  # static # readonly
    MatrixSpikePercentRecoveryMaximum: str = ...  # static # readonly
    MatrixSpikePercentRecoveryMinimum: str = ...  # static # readonly
    MatrixTypeOverride: str = ...  # static # readonly
    MaximumBlankConcentration: str = ...  # static # readonly
    MaximumPercentResidual: str = ...  # static # readonly
    MinimumAverageResponseFactor: str = ...  # static # readonly
    MinimumSignalToNoiseRatio: str = ...  # static # readonly
    MolecularFormula: str = ...  # static # readonly
    Multiplier: str = ...  # static # readonly
    NeutralLossGain: str = ...  # static # readonly
    NoiseAlgorithmType: str = ...  # static # readonly
    NoiseReference: str = ...  # static # readonly
    NoiseStandardDeviationMultiplier: str = ...  # static # readonly
    PeakFilterThreshold: str = ...  # static # readonly
    PeakFilterThresholdValue: str = ...  # static # readonly
    PeakSelectionCriterion: str = ...  # static # readonly
    PlatesCalculationType: str = ...  # static # readonly
    QCMaximumDeviation: str = ...  # static # readonly
    QCMaximumPercentRSD: str = ...  # static # readonly
    QualifierRatioMethod: str = ...  # static # readonly
    QuantitateByHeight: str = ...  # static # readonly
    ReferenceMSPathName: str = ...  # static # readonly
    RelativeResponseFactorMaximumPercentDeviation: str = ...  # static # readonly
    RelativeRetentionTimeMaximumPercentDeviation: str = ...  # static # readonly
    ResolutionCalculationType: str = ...  # static # readonly
    ResponseCheckMinimum: str = ...  # static # readonly
    ResponseFactorMaximumPercentDeviation: str = ...  # static # readonly
    RetentionTime: str = ...  # static # readonly
    RetentionTimeDeltaUnits: str = ...  # static # readonly
    RetentionTimeWindow: str = ...  # static # readonly
    RetentionTimeWindowUnits: str = ...  # static # readonly
    RightRetentionTimeDelta: str = ...  # static # readonly
    RxUnlabeledIsotopicDilution: str = ...  # static # readonly
    RyLabeledIsotopicDilution: str = ...  # static # readonly
    SampleAmountLimitHigh: str = ...  # static # readonly
    SampleAmountLimitLow: str = ...  # static # readonly
    ScanType: str = ...  # static # readonly
    SelectedMZ: str = ...  # static # readonly
    Signal: str = ...  # static # readonly
    SignalInstance: str = ...  # static # readonly
    SignalName: str = ...  # static # readonly
    SignalType: str = ...  # static # readonly
    Smoothing: str = ...  # static # readonly
    SmoothingFunctionWidth: str = ...  # static # readonly
    SmoothingGaussianWidth: str = ...  # static # readonly
    SurrogateConcentration: str = ...  # static # readonly
    SurrogateConcentrationLimitHigh: str = ...  # static # readonly
    SurrogateConcentrationLimitLow: str = ...  # static # readonly
    SurrogatePercentRecoveryMaximum: str = ...  # static # readonly
    SurrogatePercentRecoveryMinimum: str = ...  # static # readonly
    SymmetryCalculationType: str = ...  # static # readonly
    TableName: str = ...  # static # readonly
    ThresholdNumberOfPeaks: str = ...  # static # readonly
    TimeReferenceFlag: str = ...  # static # readonly
    TimeSegment: str = ...  # static # readonly
    Transition: str = ...  # static # readonly
    UncertaintyRelativeOrAbsolute: str = ...  # static # readonly
    UserAnnotation: str = ...  # static # readonly
    UserDefined: str = ...  # static # readonly

class TargetQualifier:  # Class
    AreaSum: str = ...  # static # readonly
    IntegrationParameters: str = ...  # static # readonly
    IonPolarity: str = ...  # static # readonly
    MZ: str = ...  # static # readonly
    MZExtractionWindowFilterLeft: str = ...  # static # readonly
    MZExtractionWindowFilterRight: str = ...  # static # readonly
    MZExtractionWindowUnits: str = ...  # static # readonly
    PeakFilterThreshold: str = ...  # static # readonly
    PeakFilterThresholdValue: str = ...  # static # readonly
    QualifierRangeMaximum: str = ...  # static # readonly
    QualifierRangeMinimum: str = ...  # static # readonly
    RelativeResponse: str = ...  # static # readonly
    SelectedMZ: str = ...  # static # readonly
    TableName: str = ...  # static # readonly
    ThresholdNumberOfPeaks: str = ...  # static # readonly
    Transition: str = ...  # static # readonly
    Uncertainty: str = ...  # static # readonly
    UserDefined: str = ...  # static # readonly

class VirtualColumns:  # Class
    CalibrationReferenceCompoundName: str = ...  # static # readonly
    OutlierSummary: str = ...  # static # readonly
    QuantitationMessageSummary: str = ...  # static # readonly
