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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Properties

class Resources:  # Class
    ActionString_GenerateReport: str  # static # readonly
    AnalysisMessageTarget_Sample: str  # static # readonly
    AppIcon: System.Drawing.Icon  # static # readonly
    AppName: str  # static # readonly
    AppName_Short: str  # static # readonly
    BlankSubtractPeakThresholdType_ComponentArea: str  # static # readonly
    BlankSubtractPeakThresholdType_EstimatedConcentration: str  # static # readonly
    BlankSubtractPeakThresholdType_None: str  # static # readonly
    BlankSubtractRTWindowType_FullWidthHalfMaximum: str  # static # readonly
    BlankSubtractRTWindowType_Minutes: str  # static # readonly
    BlankSubtractRTWindowType_None: str  # static # readonly
    BmpError: System.Drawing.Bitmap  # static # readonly
    BmpInformation: System.Drawing.Bitmap  # static # readonly
    BmpWarning: System.Drawing.Bitmap  # static # readonly
    ButtonLabel_NewAnalysis: str  # static # readonly
    Category_All: str  # static # readonly
    Category_BasePeak: str  # static # readonly
    Category_Component: str  # static # readonly
    Category_DeconvolutionMethod: str  # static # readonly
    Category_ExactMass: str  # static # readonly
    Category_Hit: str  # static # readonly
    Category_LibrarySearchMethod: str  # static # readonly
    Category_ModelPeakIon: str  # static # readonly
    Category_Peak: str  # static # readonly
    Category_Sample: str  # static # readonly
    Category_TargetCompound: str  # static # readonly
    Collapse: System.Drawing.Bitmap  # static # readonly
    Copy: System.Drawing.Bitmap  # static # readonly
    Culture: System.Globalization.CultureInfo  # static
    DeconvolutionMethod_BatchID: str  # static # readonly
    DeconvolutionMethod_SampleID: str  # static # readonly
    DialogResult_AddSamples: str  # static # readonly
    DialogTitle_AddSamples: str  # static # readonly
    DialogTitle_Analyze: str  # static # readonly
    DialogTitle_CompressResults: str  # static # readonly
    DialogTitle_Export: str  # static # readonly
    DialogTitle_ExportTableToLibrary: str  # static # readonly
    DialogTitle_ImportQuantBatch: str  # static # readonly
    DialogTitle_LoadMethod: str  # static # readonly
    DialogTitle_NewAnalysis: str  # static # readonly
    DialogTitle_OpenAnalysis: str  # static # readonly
    DialogTitle_Properties: str  # static # readonly
    DialogTitle_Query: str  # static # readonly
    DialogTitle_RTCalibration: str  # static # readonly
    DialogTitle_RunScript: str  # static # readonly
    DialogTitle_SaveAnalysis: str  # static # readonly
    DialogTitle_SaveAnalysisAs: str  # static # readonly
    DialogTitle_SaveMethod: str  # static # readonly
    Err_ApplicationIsInModalState: str  # static # readonly
    Err_CannotGenerateReportReadOnlyAuditTrail: str  # static # readonly
    Err_ConfigurationError: str  # static # readonly
    Err_Error: str  # static # readonly
    Err_ErrorWhileAnalyzing: str  # static # readonly
    Err_FileAlreadyExists: str  # static # readonly
    Err_LayoutFileVersionNotMatch: str  # static # readonly
    Err_LogonRequired: str  # static # readonly
    Err_PleaseEnter: str  # static # readonly
    Err_PleaseEnterValidNumber: str  # static # readonly
    Err_PleaseEnterValidNumbers: str  # static # readonly
    Err_ReportError: str  # static # readonly
    Err_SpecifyUserName: str  # static # readonly
    Err_TranslatorNotInstalled: str  # static # readonly
    Expand: System.Drawing.Bitmap  # static # readonly
    ExportDestinationType_Csv: str  # static # readonly
    ExportDestinationType_Library: str  # static # readonly
    ExportDestinationType_QuantMethod: str  # static # readonly
    FileType_AllFiles: str  # static # readonly
    FileType_CSVFiles: str  # static # readonly
    FileType_LayoutFiles: str  # static # readonly
    FileType_MethodFiles: str  # static # readonly
    FileType_Methods: str  # static # readonly
    FileType_QuantMethod: str  # static # readonly
    FileType_QueryFiles: str  # static # readonly
    FileType_RTCalibrationFiles: str  # static # readonly
    FileType_ReportTemplateFiles: str  # static # readonly
    FileType_ScriptFiles: str  # static # readonly
    FileType_UnknownsAnalysisFiles: str  # static # readonly
    FileType_XmlFiles: str  # static # readonly
    FillDown: System.Drawing.Bitmap  # static # readonly
    HitConcentrationEstimation_AverageRFofAllISTDs: str  # static # readonly
    HitConcentrationEstimation_AverageRFofAllTargets: str  # static # readonly
    HitConcentrationEstimation_AverageRFofClosestTarget: str  # static # readonly
    HitConcentrationEstimation_ManualRF: str  # static # readonly
    HitConcentrationEstimation_None: str  # static # readonly
    HitConcentrationEstimation_RFofClosestISTD: str  # static # readonly
    HitConcentrationEstimation_RFofClosestTargetISTD: str  # static # readonly
    HitConcentrationEstimation_RelativeISTDEstimation: str  # static # readonly
    IntegratorType_Agile: str  # static # readonly
    IntegratorType_Agile2: str  # static # readonly
    IonPeakLabel_Component: str  # static # readonly
    IonPeakLabel_TIC: str  # static # readonly
    Label_Automatic: str  # static # readonly
    Label_Component: str  # static # readonly
    Label_NoDisplay: str  # static # readonly
    Label_None: str  # static # readonly
    Label_ReadOnly: str  # static # readonly
    Label_StoppingAnalysis: str  # static # readonly
    Legend_Components: str  # static # readonly
    LibrarySearchTool_SetBestHit: str  # static # readonly
    LibrarySearchType_AccurateMassPatternMatch: str  # static # readonly
    LibrarySearchType_RetentionTimeMatch: str  # static # readonly
    LibrarySearchType_SpectralSearch: str  # static # readonly
    MSLibraryFormat_Binary: str  # static # readonly
    MSLibraryFormat_Compressed: str  # static # readonly
    MSLibraryFormat_PCDL: str  # static # readonly
    MSLibraryFormat_XML: str  # static # readonly
    MethodFromLibraryIonMode_HighestMass: str  # static # readonly
    MethodFromLibraryIonMode_Monoisotopic: str  # static # readonly
    MethodFromLibraryIonMode_MostAbundant: str  # static # readonly
    MethodFromLibraryIonMode_Weighted: str  # static # readonly
    Msg_CannotRecognizeLayoutFile: str  # static # readonly
    Msg_ChooseBatchFileInSameBatchFolder: str  # static # readonly
    Msg_ConvertingSample: str  # static # readonly
    Msg_GeneratingReportsPleaseWait: str  # static # readonly
    Msg_LoggingIn: str  # static # readonly
    Msg_ProcessWasStoppedByUser: str  # static # readonly
    Msg_SelectCellsToCopy: str  # static # readonly
    Msg_SelectOneComponent: str  # static # readonly
    Msg_SelectOneSampleToEditMethod: str  # static # readonly
    Msg_SelectOneSampleToReport: str  # static # readonly
    Msg_SelectOneSampleToSaveMethod: str  # static # readonly
    MultiLibrarySearchType_All: str  # static # readonly
    MultiLibrarySearchType_StopWhenFirstFoundInFirstLibrary: str  # static # readonly
    MultiLibrarySearchType_StopWhenFound: str  # static # readonly
    MzDeltaUnits_AMU: str  # static # readonly
    MzDeltaUnits_PPM: str  # static # readonly
    MzDeltaUnits_Percent: str  # static # readonly
    PaneTitle_ComponentChromatogram: str  # static # readonly
    PaneTitle_ComponentSpectrum: str  # static # readonly
    PaneTitle_EIC: str  # static # readonly
    Pane_AnalysisMessage: str  # static # readonly
    Pane_Chromatogram: str  # static # readonly
    Pane_ComponentTable: str  # static # readonly
    Pane_EicPeaks: str  # static # readonly
    Pane_ExactMass: str  # static # readonly
    Pane_HitTable: str  # static # readonly
    Pane_Hits: str  # static # readonly
    Pane_IonPeaks: str  # static # readonly
    Pane_SampleTable: str  # static # readonly
    Pane_Script: str  # static # readonly
    Pane_Spectrum: str  # static # readonly
    Pane_Structure: str  # static # readonly
    Pane_TargetTable: str  # static # readonly
    PeakDetectionAlgorithm_FeatureDeconvolution: str  # static # readonly
    PeakDetectionAlgorithm_SpectralDeconvolution: str  # static # readonly
    PeakDetectionAlgorithm_TICAnalysis: str  # static # readonly
    PeakDetectionAlgorithm_TargetDeconvolution: str  # static # readonly
    PeakDetectionAlgorithm_TargetDeconvolution_SureTarget: str  # static # readonly
    PeakLabel_RTUnit_Minites: str  # static # readonly
    Progress_CompressingResults: str  # static # readonly
    Progress_Deconvolutiong: str  # static # readonly
    Progress_ExportingTableToLibrary: str  # static # readonly
    Progress_FindingTICPeaks: str  # static # readonly
    Progress_Identifying: str  # static # readonly
    Progress_ImportingComponentTable: str  # static # readonly
    Progress_ImportingQuantBatch: str  # static # readonly
    Progress_MatchingTarget: str  # static # readonly
    Progress_OpeningAnalysis: str  # static # readonly
    Progress_RunningScript: str  # static # readonly
    Progress_SavingAnalysis: str  # static # readonly
    Prompt_MethodFileExistsOverwrite: str  # static # readonly
    Prompt_SaveAnalysis: str  # static # readonly
    Prompt_SaveAnalysisBeforeReport: str  # static # readonly
    Prompt_UndoCheckoutAnalysis: str  # static # readonly
    Prompt_YouMadeChangesApply: str  # static # readonly
    Prompt_YouMadeChangesApplyToAllSamples: str  # static # readonly
    PropertyPageTitle_ChromatogramProperties: str  # static # readonly
    PropertyPageTitle_EicPeaks: str  # static # readonly
    PropertyPageTitle_IonPeaks: str  # static # readonly
    PropertyPageTitle_SpectrumProperties: str  # static # readonly
    RTMatchFactorType_Gaussian: str  # static # readonly
    RTMatchFactorType_None: str  # static # readonly
    RTMatchFactorType_Trapezoidal: str  # static # readonly
    RTPenaltyType_Additive: str  # static # readonly
    RTPenaltyType_Multiplicative: str  # static # readonly
    Refresh: System.Drawing.Bitmap  # static # readonly
    Remoting_QuantBatchNotExist: str  # static # readonly
    ResourceManager: System.Resources.ResourceManager  # static # readonly
    ScreeningType_Fast: str  # static # readonly
    ScreeningType_None: str  # static # readonly
    ScreeningType_Normal: str  # static # readonly
    SpectrumPeakWeighting_EqualWeight: str  # static # readonly
    SpectrumPeakWeighting_Mass: str  # static # readonly
    SpectrumPeakWeighting_Mass2: str  # static # readonly
    SpectrumPeakWeighting_Mass3: str  # static # readonly
    Title_CopySamples: str  # static # readonly
    Title_EicPeaks: str  # static # readonly
    Title_LoggingIn: str  # static # readonly
    Tools: List[int]  # static # readonly
    Usage: str  # static # readonly
