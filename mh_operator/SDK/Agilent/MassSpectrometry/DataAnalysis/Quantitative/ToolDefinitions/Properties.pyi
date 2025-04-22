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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ToolDefinitions.Properties

class Resources:  # Class
    AddSamples_Label: str  # static # readonly
    AddSamples_Title: str  # static # readonly
    AppendMethod_Label: str  # static # readonly
    AppendMethod_Title: str  # static # readonly
    AuditTrail_GenerateReport: str  # static # readonly
    Culture: System.Globalization.CultureInfo  # static
    ErrMsg_BatchFileDoesNotExist: str  # static # readonly
    ErrMsg_CannotFindTuneEval: str  # static # readonly
    ErrMsg_CannotPlotThisColumn: str  # static # readonly
    ErrMsg_EnterMethod: str  # static # readonly
    ErrMsg_LibraryMethodDoesNotExist: str  # static # readonly
    ErrMsg_MethodNotExist: str  # static # readonly
    ErrMsg_NoPermissionToGenerateReport: str  # static # readonly
    ErrMsg_PleaseEnterInteger: str  # static # readonly
    ErrMsg_PleaseEnterNumber: str  # static # readonly
    ErrMsg_PleaseEnterSamplePath: str  # static # readonly
    ErrMsg_PleaseEnterValueToColumn: str  # static # readonly
    ErrMsg_PleaseSelectOneSample: str  # static # readonly
    ErrMsg_ReportError: str  # static # readonly
    ErrMsg_SampleDoesNotExist: str  # static # readonly
    ErrMsg_TranslatorNotInstalled: str  # static # readonly
    ErrMsg_UnknownsFileType: str  # static # readonly
    Err_PleaseEnterFloatingNumberValue: str  # static # readonly
    Exp_CannotAddSample_AcquisitionNotFinished: str  # static # readonly
    Exp_CannotAddSample_FailedToReadFile: str  # static # readonly
    Exp_CannotAddSample_FileNotFound: str  # static # readonly
    FileType_TextFiles: str  # static # readonly
    FindOperatorType_Contains: str  # static # readonly
    FindOperatorType_Equal: str  # static # readonly
    FindOperatorType_Greater: str  # static # readonly
    FindOperatorType_GreaterEqual: str  # static # readonly
    FindOperatorType_IsNull: str  # static # readonly
    FindOperatorType_Less: str  # static # readonly
    FindOperatorType_LessEqual: str  # static # readonly
    FindOperatorType_NotContains: str  # static # readonly
    FindOperatorType_NotEqual: str  # static # readonly
    FindOperatorType_NotNull: str  # static # readonly
    GotoUnknowns_Message: str  # static # readonly
    GotoUnknowns_Title: str  # static # readonly
    Label_AllFiles: str  # static # readonly
    Label_CEFFiles: str  # static # readonly
    Label_CSVFiles: str  # static # readonly
    Label_CompoundID: str  # static # readonly
    Label_ExcelFiles: str  # static # readonly
    Label_LibraryFiles: str  # static # readonly
    Label_LibraryMethodDeconvolution: str  # static # readonly
    Label_MethodFiles: str  # static # readonly
    Label_NumCalibrationSamplesSelected: str  # static # readonly
    Label_NumTargetCompoundsSelected: str  # static # readonly
    Label_OpenReportFile: str  # static # readonly
    Label_PdfFiles: str  # static # readonly
    Label_RTCalibrationFiles: str  # static # readonly
    Label_RecentReportMethods: str  # static # readonly
    Label_ReferenceLibraryFiles: str  # static # readonly
    Label_ReportTemplateFiles: str  # static # readonly
    Label_SelectCompounds: str  # static # readonly
    Label_SelectSamples: str  # static # readonly
    Label_TabDelimitedFiles: str  # static # readonly
    Label_TextFiles: str  # static # readonly
    Label_XmlFiles: str  # static # readonly
    ListItem_Origin: str  # static # readonly
    MSScanType_All: str  # static # readonly
    MSScanType_MultipleReaction: str  # static # readonly
    MSScanType_Scan: str  # static # readonly
    MSScanType_SelectedIon: str  # static # readonly
    MethodFromLibraryIonMode_HighestMass: str  # static # readonly
    MethodFromLibraryIonMode_Monoisotopic: str  # static # readonly
    MethodFromLibraryIonMode_MostAbundant: str  # static # readonly
    MethodFromLibraryIonMode_Weighted: str  # static # readonly
    Msg_AnalyzeBeforeGenerateReport: str  # static # readonly
    Msg_CannotEditMethodOfSkippedSample: str  # static # readonly
    Msg_CannotFindMethodReportTemplate: str  # static # readonly
    Msg_CannotFindTheDataSearchingFor: str  # static # readonly
    Msg_EnterExpectedConcentrationToAddCalibration: str  # static # readonly
    Msg_ExportingTable: str  # static # readonly
    Msg_GeneratingReportsPleaseWait: str  # static # readonly
    Msg_InputValidNumber: str  # static # readonly
    Msg_MethodCreated: str  # static # readonly
    Msg_ProcessingSample: str  # static # readonly
    Msg_ReferencePatternLibraryGenerated: str  # static # readonly
    Msg_ReportCanceled: str  # static # readonly
    Msg_SaveBatchBeforeAnalyzeUnknowns: str  # static # readonly
    Msg_SaveBatchBeforeReport: str  # static # readonly
    Msg_SelectASample: str  # static # readonly
    Msg_SelectCompounds: str  # static # readonly
    Msg_SelectLevels: str  # static # readonly
    Msg_SelectSamples: str  # static # readonly
    NewMethod_Label: str  # static # readonly
    NewMethod_Title: str  # static # readonly
    OpenMethod_Label: str  # static # readonly
    OpenMethod_Title: str  # static # readonly
    Progress_AddingCompound: str  # static # readonly
    Progress_CreatingXtensIonTargets: str  # static # readonly
    Progress_SetupReferencePatternLibrary: str  # static # readonly
    Prompt_EmptyMolecularFormula_Continue: str  # static # readonly
    Prompt_QualNotFound_Specify: str  # static # readonly
    Prompt_QualifierRatioNotUpdatedNoPeakFound: str  # static # readonly
    Prompt_SamplesAlreadyExistsContinue: str  # static # readonly
    Prompt_SaveBatchBeforeGotoUnknowns: str  # static # readonly
    Prompt_SaveBatchBeforeReport: str  # static # readonly
    ResourceManager: System.Resources.ResourceManager  # static # readonly
    SampleGroup_All: str  # static # readonly
    SampleGroup_Tooltip: str  # static # readonly
    SampleGroup_Unassigned: str  # static # readonly
    SampleType_All: str  # static # readonly
    SampleType_Tooltip: str  # static # readonly
    SampleType_Unassigned: str  # static # readonly
    Sample_Tooltip: str  # static # readonly
    SignalType_All: str  # static # readonly
    SignalType_None: str  # static # readonly
    Title_AddCalibration: str  # static # readonly
    Title_AppendMethodFromAcquiredData: str  # static # readonly
    Title_AppendMethodFromAcquiredScanData: str  # static # readonly
    Title_AppendMethodFromAcquiredScanDataWithLibrarySearch: str  # static # readonly
    Title_AppendMethodFromFile: str  # static # readonly
    Title_AverageCalibration: str  # static # readonly
    Title_AverageCalibrationReplicates: str  # static # readonly
    Title_AverageQualifierRatios: str  # static # readonly
    Title_AverageRetentionTime: str  # static # readonly
    Title_ClearCalibration: str  # static # readonly
    Title_CopyCalibrationLevelsTo: str  # static # readonly
    Title_CreateXtensIonTargets: str  # static # readonly
    Title_DisableCalibrationPoints: str  # static # readonly
    Title_ExportTable: str  # static # readonly
    Title_ImportLevelsFromFile: str  # static # readonly
    Title_LoadLayout: str  # static # readonly
    Title_NewMethodFromAcquiredData: str  # static # readonly
    Title_NewMethodFromAcquiredScanData: str  # static # readonly
    Title_NewMethodFromAcquiredScanDataWithLibrarySearch: str  # static # readonly
    Title_NewMethodFromFile: str  # static # readonly
    Title_OpenCEFFile: str  # static # readonly
    Title_OpenMethod: str  # static # readonly
    Title_OpenMethodFromExistingBatch: str  # static # readonly
    Title_RemoveCalibration: str  # static # readonly
    Title_ReplaceCalibration: str  # static # readonly
    Title_SaveLayout: str  # static # readonly
    Title_ScanAnalysisParameters: str  # static # readonly
    Title_ShiftRetentionTime: str  # static # readonly
    Title_UpdateMassAssignments: str  # static # readonly
    Title_UpdateQualifierRatios: str  # static # readonly
    Title_UpdateRetentionTime: str  # static # readonly
    Title_UpdateRetentionTimeFromISTD: str  # static # readonly
    ToolLabel_AllColumnsAreVisible: str  # static # readonly
