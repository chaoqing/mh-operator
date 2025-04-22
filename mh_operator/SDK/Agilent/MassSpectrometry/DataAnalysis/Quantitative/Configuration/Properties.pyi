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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.Properties

class Resources:  # Class
    AppName: str  # static # readonly
    Caption_OutlierCategory_Blank: str  # static # readonly
    Caption_OutlierCategory_CC: str  # static # readonly
    Caption_OutlierCategory_Calibration: str  # static # readonly
    Caption_OutlierCategory_Custom: str  # static # readonly
    Caption_OutlierCategory_ISTD: str  # static # readonly
    Caption_OutlierCategory_LibraryMatchScore: str  # static # readonly
    Caption_OutlierCategory_Mass: str  # static # readonly
    Caption_OutlierCategory_MassMatchScore: str  # static # readonly
    Caption_OutlierCategory_Matrix: str  # static # readonly
    Caption_OutlierCategory_PeakResult: str  # static # readonly
    Caption_OutlierCategory_QC: str  # static # readonly
    Caption_OutlierCategory_Qualifier: str  # static # readonly
    Caption_OutlierCategory_ResponseCheck: str  # static # readonly
    Caption_OutlierCategory_Sample: str  # static # readonly
    Caption_OutlierCategory_Surrogate: str  # static # readonly
    Caption_Outlier_Accuracy: str  # static # readonly
    Caption_Outlier_AlternativePeak: str  # static # readonly
    Caption_Outlier_AverageResponseFactor: str  # static # readonly
    Caption_Outlier_AverageResponseFactorRSD: str  # static # readonly
    Caption_Outlier_BlankConcentration: str  # static # readonly
    Caption_Outlier_BlankResponse: str  # static # readonly
    Caption_Outlier_CCAverageResponseFactor: str  # static # readonly
    Caption_Outlier_CCISTDResponseRatio: str  # static # readonly
    Caption_Outlier_CCRelativeResponseFactor: str  # static # readonly
    Caption_Outlier_CCResponseRatio: str  # static # readonly
    Caption_Outlier_CCRetentionTime: str  # static # readonly
    Caption_Outlier_CCTime: str  # static # readonly
    Caption_Outlier_CalibrationRange: str  # static # readonly
    Caption_Outlier_CapacityFactor: str  # static # readonly
    Caption_Outlier_CurveFitR2: str  # static # readonly
    Caption_Outlier_CustomCalculation: str  # static # readonly
    Caption_Outlier_DQ_Accuracy: str  # static # readonly
    Caption_Outlier_DQ_BlankConcentration: str  # static # readonly
    Caption_Outlier_DQ_SampleAmount: str  # static # readonly
    Caption_Outlier_ISTDResponse: str  # static # readonly
    Caption_Outlier_ISTDResponsePercentDeviation: str  # static # readonly
    Caption_Outlier_IntegrationMetric: str  # static # readonly
    Caption_Outlier_LibraryMatchScore: str  # static # readonly
    Caption_Outlier_LimitOfDetection: str  # static # readonly
    Caption_Outlier_LimitOfQuantitation: str  # static # readonly
    Caption_Outlier_MassAccuracy: str  # static # readonly
    Caption_Outlier_MassMatchScore: str  # static # readonly
    Caption_Outlier_MatrixSpike: str  # static # readonly
    Caption_Outlier_MatrixSpikeDeviation: str  # static # readonly
    Caption_Outlier_MatrixSpikeGroupRecovery: str  # static # readonly
    Caption_Outlier_MatrixSpikePercentRecovery: str  # static # readonly
    Caption_Outlier_MethodDetectionLimit: str  # static # readonly
    Caption_Outlier_PeakFullWidthHalfMaximum: str  # static # readonly
    Caption_Outlier_PeakNotFound: str  # static # readonly
    Caption_Outlier_PeakPurity: str  # static # readonly
    Caption_Outlier_PeakResolutionFront: str  # static # readonly
    Caption_Outlier_PeakResolutionRear: str  # static # readonly
    Caption_Outlier_PeakSymmetry: str  # static # readonly
    Caption_Outlier_Plates: str  # static # readonly
    Caption_Outlier_QC: str  # static # readonly
    Caption_Outlier_QCLCSRecovery: str  # static # readonly
    Caption_Outlier_QC_RSD: str  # static # readonly
    Caption_Outlier_QValue: str  # static # readonly
    Caption_Outlier_QualifierCoelutionScore: str  # static # readonly
    Caption_Outlier_QualifierIntegrationMetric: str  # static # readonly
    Caption_Outlier_QualifierMassAccuracy: str  # static # readonly
    Caption_Outlier_QualifierPeakFullWidthHalfMaximum: str  # static # readonly
    Caption_Outlier_QualifierPeakNotFound: str  # static # readonly
    Caption_Outlier_QualifierPeakResolutionFront: str  # static # readonly
    Caption_Outlier_QualifierPeakResolutionRear: str  # static # readonly
    Caption_Outlier_QualifierPeakSymmetry: str  # static # readonly
    Caption_Outlier_QualifierRatio: str  # static # readonly
    Caption_Outlier_QualifierSaturationRecovery: str  # static # readonly
    Caption_Outlier_QualifierSignalToNoiseRatio: str  # static # readonly
    Caption_Outlier_RelativeResponseFactor: str  # static # readonly
    Caption_Outlier_RelativeRetentionTime: str  # static # readonly
    Caption_Outlier_RelativeStandardError: str  # static # readonly
    Caption_Outlier_ResponseCheck: str  # static # readonly
    Caption_Outlier_ResponseFactor: str  # static # readonly
    Caption_Outlier_RetentionTime: str  # static # readonly
    Caption_Outlier_SampleAmount: str  # static # readonly
    Caption_Outlier_SampleRSD: str  # static # readonly
    Caption_Outlier_SaturationRecovery: str  # static # readonly
    Caption_Outlier_SignalToNoiseRatio: str  # static # readonly
    Caption_Outlier_Surrogate: str  # static # readonly
    Caption_Outlier_SurrogatePercentRecovery: str  # static # readonly
    ColorScheme_Black: str  # static # readonly
    ColorScheme_Classic: str  # static # readonly
    ColorScheme_DarkGray: str  # static # readonly
    ColorScheme_LightGray: str  # static # readonly
    ColorScheme_Pear: str  # static # readonly
    ColorScheme_Standard: str  # static # readonly
    ConcentrationUnits: str  # static # readonly
    Culture: System.Globalization.CultureInfo  # static
    HiddenColumns: List[int]  # static # readonly
    MethodTaskColumns: List[int]  # static # readonly
    NumberFormats: List[int]  # static # readonly
    QuantAnalysis_CustomTools: List[int]  # static # readonly
    ResourceManager: System.Resources.ResourceManager  # static # readonly
    SampleType_Blank_EQ_Caption: str  # static # readonly
    SampleType_MatrixBlank_EQ_Caption: str  # static # readonly
    SampleType_MatrixDup_EQ_Caption: str  # static # readonly
    SampleType_Matrix_EQ_Caption: str  # static # readonly
    ShortAppName: str  # static # readonly
