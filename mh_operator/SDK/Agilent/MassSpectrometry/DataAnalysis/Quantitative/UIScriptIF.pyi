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

# Discovered Generic TypeVars:
T = TypeVar("T")
from . import (
    AppCommandContext,
    CompoundFilterType,
    CompoundKeySortType,
    GridExportMode,
    InstrumentType,
    INumericCustomFormat,
    INumericFormat,
    MethodEditTaskMode,
    NormalizeType,
    OutlierCategories,
    OutlierColumns,
    OutlierFilterType,
    OutlierLimitType,
    OutlierTables,
    PrintPlotFitType,
    SampleRowId,
    TargetCompoundRowId,
    TargetQualifierRowId,
)
from .CompoundsAtAGlance import OrganizeType, Overlay, PeakAnnotationType, ReviewMode
from .ScriptEngine import IScriptEngine
from .Toolbar import IExplorerBarGroup, IToolbar, IToolbarsManager
from .UIUtils2.Utils import FindOperatorType

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF

class Application:  # Class
    def __init__(self) -> None: ...

    UIState: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState
    )  # static # readonly

class CommandEventArgs(System.EventArgs):  # Class
    def __init__(self, commandName: str) -> None: ...

    Command: str

class IAddIn(object):  # Interface
    DisplayName: str  # readonly
    Enabled: bool
    Name: str  # readonly
    PathName: str  # readonly

    def Execute(self, parameters: List[Any]) -> Any: ...

class IAddInManager(object):  # Interface
    def __getitem__(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IAddIn: ...
    def GetIDs(self) -> List[str]: ...

class IAverageQualifierRatiosDialog(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISelectRowsDialog
):  # Interface
    IncludesCalibrations: bool
    IncludesQCs: bool

class IAverageRetentionTimeDialog(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISelectRowsDialog
):  # Interface
    IncludesCalibrations: bool
    IncludesQCs: bool
    UseWeighting: bool
    Weighting: float

class IBatchDataSet(object):  # Interface
    BatchState: str  # readonly
    BatchTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataTable
    )  # readonly
    CalibrationTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataTable
    )  # readonly
    PeakQualifierTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataTable
    )  # readonly
    PeakTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataTable
    )  # readonly
    TargetCompoundTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataTable
    )  # readonly
    TargetQualifierTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataTable
    )  # readonly

    def GetBatchAttribute(self, name: str) -> Any: ...

class ICalCurvePane(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPlotControlPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane,
):  # Interface
    AssistantConfidenceBandVisible: bool
    CanAcceptAssistantCurve: bool  # readonly
    CurveFitAssistantTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ICurveFitAssistantTable
    )  # readonly
    IsLogScaleX: bool
    IsLogScaleY: bool
    ShowCC: bool
    ShowIstdResponses: bool
    ShowQC: bool
    ShowRelativeConcentration: bool
    ShowStandardDeviationBars: bool

    def FitToLevels(self, levelNames: Iterable[str], includesOrigin: bool) -> None: ...
    def AcceptAssistantCurve(self) -> None: ...
    def CalibrationPointExists(self, sampleId: int) -> bool: ...
    def ShowPropertiesDialog(self) -> None: ...

class ICalibrationAtAGlance(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IWindow,
    System.Windows.Forms.IWin32Window,
):  # Interface
    NumPaneColumnsPerPage: int  # readonly
    NumPaneRowsPerPage: int  # readonly

    def Show(self) -> None: ...
    def Close(self) -> None: ...
    def GetSelectedTargetCompounds(self) -> List[TargetCompoundRowId]: ...
    def SetPaneDimension(self, rows: int, columns: int) -> None: ...

    WindowCreated: System.EventHandler  # Event

class IChromSpecPane(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPlotControlPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane,
):  # Interface
    CanClearManualIntegration: bool  # readonly
    CanFitToCalibrationLevel: bool  # readonly
    CanFitToPeak: bool  # readonly
    CanFitToPeakHeight: bool  # readonly
    CanManualIntegrate: bool  # readonly
    CanResetRTRange: bool  # readonly
    CanRestoreIntegrationSetup: bool  # readonly
    CanSearchLibrary: bool  # readonly
    CanShowDeconvolutedComponents: bool  # readonly
    CanShowIntegrationSetupDialog: bool  # readonly
    CanShowWiderRTRange: bool  # readonly
    CanZeroPeak: bool  # readonly
    ChromatogramXUnit: Agilent.MassSpectrometry.DataAnalysis.DataUnit
    FillPeaks: bool
    FitToHighestLevel: bool
    FitToLowestLevel: bool
    FitToPeak: bool
    FitToPeakHeight: bool
    IsSelectedPaneCompound: bool  # readonly
    IsSelectedPaneIstd: bool  # readonly
    IsSelectedPaneQualifier: bool  # readonly
    IsSelectedPaneSpectrum: bool  # readonly
    ManualIntegrateMode: bool  # readonly
    ManualScaleY: bool  # readonly
    NormalizeQualifiers: bool
    SelectedCompoundId: TargetCompoundRowId  # readonly
    SelectedQualifierId: TargetQualifierRowId  # readonly
    ShowBaselineCalculationPoints: bool
    ShowBaselines: bool
    ShowChromatogram: bool
    ShowDeconvolutedComponents: bool
    ShowIstd: bool
    ShowMatchScores: bool
    ShowOverrideSpectrum: bool
    ShowQualifierAnnotations: bool
    ShowQualifiers: bool
    ShowReferenceSpectrum: bool
    ShowSpectrum: bool
    ShowUncertaintyBand: bool

    def RestoreIntegrationSetup(self) -> None: ...
    def SetManualScaleY(self, miny: float, maxy: float) -> None: ...
    def SearchLibrary(self) -> None: ...
    def ShowPropertiesDialog(self) -> None: ...
    def ShowWiderRTRange(self) -> None: ...
    def ResetRTRange(self) -> None: ...
    def ClearManualIntegration(self) -> None: ...
    def ZeroPeak(self) -> None: ...
    def ExitManualIntegrationMode(self) -> None: ...
    def GetActivePaneScale(
        self, minx: float, maxx: float, miny: float, maxy: float
    ) -> bool: ...
    def EnterManualIntegrationMode(self) -> None: ...
    def ShowIntegrationSetupDialog(self) -> None: ...
    def ShowPeakLabelsDialog(self) -> None: ...

class IChromatogram(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IXYData
):  # Interface
    IChromatogram: Agilent.MassSpectrometry.DataAnalysis.IChromatogram  # readonly

class IChromatogramInformation(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IWindow,
    System.Windows.Forms.IWin32Window,
):  # Interface
    AnchorRows: int  # readonly
    HeadToTail: bool
    Items: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogramInformationItem
    ]  # readonly
    LinkXAxes: bool
    LinkYAxes: bool
    MaxNumVisibleRows: int
    Overlay: bool
    RowCount: int  # readonly

    def SelectAllGrid(self) -> None: ...
    def AutoScaleY(self) -> None: ...
    def CanAutoScale(self) -> bool: ...
    def GetPane(
        self, rowIndex: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPlotPane: ...
    def ExportGraphics(
        self,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IExportPlotParameters,
    ) -> None: ...
    def SetAllItemsVisible(self, visible: bool) -> None: ...
    def ShowPropertiesDialog(self) -> None: ...
    def AutoScaleX(self) -> None: ...
    def CreateExportGraphicsParameters(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IExportPlotParameters
    ): ...
    def AutoScale(self) -> None: ...
    def GetSelectedPane(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPlotPane: ...
    def SetItemsVisible(
        self,
        items: List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogramInformationItem
        ],
        visible: bool,
    ) -> None: ...
    def Close(self) -> None: ...
    def ShowExportGraphicsDialog(
        self,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IExportPlotParameters,
    ) -> System.Windows.Forms.DialogResult: ...
    def ShowExceptionMessage(self, ex: System.Exception) -> None: ...
    def CanCreateCompound(self) -> bool: ...
    def Show(self) -> None: ...
    def CreateCompound(self) -> None: ...
    def GetSignalsOfPane(self, rowIndex: int) -> List[
        System.Collections.Generic.KeyValuePair[
            int,
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISignalInfo,
        ]
    ]: ...
    def ShowMessage(
        self,
        message: str,
        caption: str,
        buttons: System.Windows.Forms.MessageBoxButtons,
        icon: System.Windows.Forms.MessageBoxIcon,
    ) -> System.Windows.Forms.DialogResult: ...

    WindowCreated: System.EventHandler  # Event

class IChromatogramInformationItem(object):  # Interface
    BatchID: int  # readonly
    Color: System.Drawing.Color
    DataFileName: str  # readonly
    InstrumentName: str  # readonly
    SampleID: int  # readonly
    SampleName: str  # readonly
    ScanType: Optional[Agilent.MassSpectrometry.DataAnalysis.MSScanType]  # readonly
    Signal: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISignalInfo
    )  # readonly
    Visible: bool
    _Item: (
        Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationItem
    )  # readonly

class ICompliance(object):  # Interface
    AlwaysAuditTrail: bool  # readonly
    ConnectionTicket: str  # readonly
    IsActive: bool  # readonly
    IsInstalled: bool  # readonly
    IsLocal: bool  # readonly
    Name: str  # readonly
    User: str  # readonly

    def IsUserValidationRequired(self, command: str) -> bool: ...
    def SetCommandReason(self, reason: str) -> None: ...
    def Impersonate(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IImpersonationContext
    ): ...
    def IsCommandReasonRequired(self, command: str) -> bool: ...
    def CheckoutBatch(self, batchFolder: str, batchFile: str) -> None: ...
    def HasPermission(self, command: str) -> bool: ...
    @overload
    def TranslateToLocalPath(self, path: str) -> str: ...
    @overload
    def TranslateToLocalPath(self, path: str, revisionNumber: str) -> str: ...
    @overload
    def ValidateUser(self, user: str, password: str) -> None: ...
    @overload
    def ValidateUser(
        self, user: System.Security.SecureString, password: System.Security.SecureString
    ) -> None: ...
    def IsBatchCheckedoutByCurrentUser(
        self, batchFolder: str, batchFile: str
    ) -> bool: ...
    def ValidateUserEncrypted(self, user: str, encryptedPassword: str) -> None: ...
    def UndoCheckoutBatch(self, batchFolder: str, batchFile: str) -> None: ...

class ICompoundGroupFilter(object):  # Interface
    CompoundGroup: str  # readonly
    FilterType: CompoundFilterType  # readonly

class ICompoundKey(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ICompoundKey
    ]
):  # Interface
    CompoundGroup: str  # readonly
    CompoundName: str  # readonly
    HasCompoundGroup: bool  # readonly
    HasTimeSegment: bool  # readonly
    TimeSegment: int  # readonly

class ICompoundsAtAGlance(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IWindow,
    System.Windows.Forms.IWin32Window,
):  # Interface
    AddInManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IAddInManager
    )  # readonly
    CanAutoScale: bool  # readonly
    CanCopyPage: bool  # readonly
    CanFitToCalibrationLevel: bool  # readonly
    CanFreezeColumns: bool  # readonly
    CanFreezePanes: bool  # readonly
    CanFreezeRows: bool  # readonly
    CanManualIntegrate: bool  # readonly
    CanNavigateBag: bool  # readonly
    CanShowManualIntegrateWindow: bool  # readonly
    CanUnfreezePanes: bool  # readonly
    CanUpdateRetentionTimes: bool  # readonly
    CanZeroPeakSelectedPanes: bool  # readonly
    CurrentReviewItemIndex: Optional[int]  # readonly
    FillPeaks: bool
    HasData: bool  # readonly
    HasNextReviewItem: bool  # readonly
    HasPreviousReviewItem: bool  # readonly
    IsManualIntegrating: bool  # readonly
    LinkAllXAxes: bool
    LinkAllYAxes: bool
    LinkXAxes: bool
    LinkYAxes: bool
    LinkYAxesVertically: bool
    Normalize: bool
    NumPaneColumnsPerPage: int  # readonly
    NumPaneRowsPerPage: int  # readonly
    OrganizeRows: OrganizeType  # readonly
    Overlay: Overlay  # readonly
    PeakAnnotations: List[PeakAnnotationType]
    ReviewItemCount: int  # readonly
    ReviewMode: ReviewMode  # readonly
    ShowBaselines: bool
    ShowPeakAnnotationNames: bool
    ShowPeakAnnotationUnits: bool
    ToolbarsManager: IToolbarsManager  # readonly
    Uncertainty: bool  # readonly
    WrapRows: bool  # readonly

    def FreezePanes(self) -> None: ...
    def MISplitRight(self) -> None: ...
    def FreezeRows(self) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def ShowExportGraphicsDialog(
        self,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IExportPlotParameters,
    ) -> System.Windows.Forms.DialogResult: ...
    def ShowExceptionMessage(self, ex: System.Exception) -> None: ...
    def SelectAllPanes(self) -> None: ...
    def SetupGraphics(
        self,
        samplesFilter: str,
        samplesOrder: str,
        compoundsFilter: str,
        compoundsOrder: str,
        organizeRows: OrganizeType,
        overlay: Overlay,
        reviewMode: ReviewMode,
        wrapRows: bool,
        baselines: Optional[bool],
        fillPeaks: Optional[bool],
        normalize: Optional[bool],
        uncertainty: Optional[bool],
    ) -> None: ...
    def ShowPropertiesDialog(self) -> None: ...
    def GetActivePaneScale(
        self, minx: float, maxx: float, miny: float, maxy: float
    ) -> bool: ...
    def MIMergeLeft(self) -> None: ...
    def ShowManualIntegrateWindow(self) -> None: ...
    def GotoPrevOutlierPane(self) -> bool: ...
    def MIDropBaseline(self) -> None: ...
    def CreateExportGraphicsParameters(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IExportPlotParameters
    ): ...
    def NavigateBag(self) -> None: ...
    def MovePreviousReviewItem(self) -> None: ...
    def SetCurrentLayoutAsDefault(self) -> None: ...
    def SetOutliers(self, columns: List[OutlierColumns]) -> None: ...
    def MIApplyISTDRTsToTargets(self) -> None: ...
    def AutoScaleAllPanes(self) -> None: ...
    def MIApplyTargetRTsToQualifiers(self) -> None: ...
    def MISplitLeft(self) -> None: ...
    def ZeroPeakSelectedPanes(self) -> None: ...
    def ShowHelpContents(self) -> None: ...
    def MoveNextReviewItem(self) -> None: ...
    def ShowHelpSearch(self) -> None: ...
    def UpdateRetentionTimes(self) -> None: ...
    def UnfreezePanes(self) -> None: ...
    def ExportGraphics(
        self,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IExportPlotParameters,
    ) -> None: ...
    def PrintToPdf(self, file: str) -> None: ...
    def GetReviewItems(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IReviewItem
    ]: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def Close(self) -> None: ...
    def GetAvailableOutliers(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IOutlier
    ]: ...
    def ClearManualIntegration(self) -> None: ...
    def MISnapBaseline(self) -> None: ...
    def GotoNextOutlierPane(self) -> bool: ...
    def EndManualIntegration(self) -> None: ...
    def GetSelectedSamples(self) -> List[SampleRowId]: ...
    def ShowSetupGraphicsDialog(self) -> None: ...
    def ZeroPeak(self) -> None: ...
    def MIMergeRight(self) -> None: ...
    def Print(self) -> None: ...
    def MoveReviewItem(self, index: int) -> None: ...
    def GetOutliers(self) -> List[OutlierColumns]: ...
    def FreezeColumns(self) -> None: ...
    def GetToolbar(self, paneId: str, id: str) -> IToolbar: ...
    def SetPaneDimension(self, rows: int, columns: int) -> None: ...
    def ShowHelpIndex(self) -> None: ...
    def FitToPeak(self) -> None: ...
    def SetManualScaleY(self, miny: float, maxy: float) -> None: ...
    def ManualIntegrate(self) -> None: ...
    def Show(self) -> None: ...
    def FitToCalibrationLevel(self, lowest: bool) -> None: ...
    def CopyPage(self) -> None: ...
    def FitToPeakHeight(self) -> None: ...
    def GetSelectedCompounds(self) -> List[TargetCompoundRowId]: ...
    def AutoScale(self) -> None: ...
    def ShowMessage(
        self,
        message: str,
        caption: str,
        buttons: System.Windows.Forms.MessageBoxButtons,
        icon: System.Windows.Forms.MessageBoxIcon,
    ) -> System.Windows.Forms.DialogResult: ...

    WindowCreated: System.EventHandler  # Event

class ICurveFitAssistantTable(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IGrid
):  # Interface
    Visible: bool

class IDataRow(object):  # Interface
    def __getitem__(self, column: str) -> Any: ...
    def IsNull(self, column: str) -> bool: ...

class IDataTable(object):  # Interface
    Count: int  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataRow: ...
    Name: str  # readonly

    @overload
    def Select(
        self, filterExpression: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataRow
    ]: ...
    @overload
    def Select(
        self, filterExpression: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataRow
    ]: ...
    def GetColumnNames(self) -> List[str]: ...

class IEditMethodState(object):  # Interface
    AcquisitionSamplePath: str  # readonly
    CurrentIstdCompoundName: str  # readonly
    CurrentLevelId: int  # readonly
    CurrentObjectIsCalibration: bool  # readonly
    CurrentObjectIsSample: bool  # readonly
    CurrentObjectIsTargetCompound: bool  # readonly
    CurrentObjectIsTargetQualifier: bool  # readonly
    CurrentTargetCompoundId: int  # readonly
    CurrentTargetQualifierId: int  # readonly
    IsDirty: bool  # readonly
    MethodFilePathName: str  # readonly
    TargetCompoundRow: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataRow
    )  # readonly

    def NavigateQualifier(self, compoundId: int, qualifierId: int) -> None: ...
    def ValidateMethod(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IMethodValidationMessage
    ]: ...
    def NavigateCalibration(self, compoundId: int, levelId: int) -> None: ...
    def GetTimeSegments(self) -> List[int]: ...
    def GetCompoundChromatogram(
        self, compoundId: int, minRT: float, maxRT: float
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogram
    ): ...
    def GetQualifierChromatogram(
        self, compoundId: int, qualifierId: int, minRT: float, maxRT: float
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogram
    ): ...
    def NavigateCompound(self, compoundId: int) -> None: ...
    @overload
    def GetCompoundSpectrum(
        self, compoundId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISpectrum: ...
    @overload
    def GetCompoundSpectrum(
        self, compoundId: int, minRT: float, maxRT: float
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISpectrum: ...

class IExportPlotParameters(object):  # Interface
    AllPanes: bool
    FilePath: str
    FitType: PrintPlotFitType
    ImageFormat: System.Drawing.Imaging.ImageFormat
    PageSize: System.Drawing.SizeF
    Zoom: float

    def ReadFromConfiguration(self) -> None: ...
    def SaveToConfiguration(self) -> None: ...

class IGrid(object):  # Interface
    ActiveBandName: str  # readonly
    ActiveColumnName: str  # readonly
    CanExpandAll: bool  # readonly
    ContainsFocus: bool  # readonly
    IsInEditMode: bool  # readonly
    LastLogicalBandName: str  # readonly
    LastLogicalColumnName: str  # readonly
    LastRawBandName: str  # readonly
    LastRawColumnName: str  # readonly

    def CanUndoInEditMode(self) -> bool: ...
    def FormatColumn(self, rawBandName: str, rawColumnName: str) -> None: ...
    def ColumnExists(self, rawBandName: str, rawColumnName: str) -> bool: ...
    @overload
    def ExportToXml(self, file: str) -> None: ...
    @overload
    def ExportToXml(self, file: str, mode: GridExportMode) -> None: ...
    def Sort(self, rawBandName: str, rawColumnName: str, ascending: bool) -> None: ...
    def AutoFitColumns(self) -> None: ...
    def CollapseAll(self) -> None: ...
    def IsColumnFormattable(self, rawBandName: str, rawColumnName: str) -> bool: ...
    def GetColumnCaption(self, logicalBandName: str, logicalColumnName: str) -> str: ...
    def LoadColumnSettings(self, file: str) -> None: ...
    def FindNext(
        self,
        tableName: str,
        columnName: str,
        operatorType: FindOperatorType,
        value_: Any,
    ) -> bool: ...
    def GetLogicalColumnName(self, rawBandName: str, rawColumnName: str) -> str: ...
    def ShowColumn(
        self, logicalBandName: str, logicalColumnName: str, columnNameAfter: str
    ) -> None: ...
    def UndoInEditMode(self) -> None: ...
    def GetLogicalBandName(self, rawBandName: str, rawColumnName: str) -> str: ...
    def GetSelectedRows(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IGridRow
    ]: ...
    def ExpandAll(self) -> None: ...
    def SupportsSaveLoadColumnSettings(self) -> bool: ...
    @overload
    def ExportToText(self, file: str, delimiter: str) -> None: ...
    @overload
    def ExportToText(self, file: str, delimiter: str, mode: GridExportMode) -> None: ...
    def IsColumnVisible(self, logicalBandName: str, logicalColumnName: str) -> bool: ...
    def SaveColumnSettings(self, file: str) -> None: ...
    def GetColumnNames(self, logicalBandName: str) -> List[str]: ...
    def ResetColumns(self) -> None: ...
    @overload
    def ExportToExcel(self, file: str) -> None: ...
    @overload
    def ExportToExcel(self, file: str, mode: GridExportMode) -> None: ...
    def ResetSort(self) -> None: ...
    def HideColumn(self, logicalBandName: str, logicalColumnName: str) -> None: ...
    def ShowColumnsDialog(self) -> None: ...

class IGridRow(object):  # Interface
    BandName: str  # readonly
    def __getitem__(self, columnName: str) -> Any: ...

class IISTDFilter(object):  # Interface
    FilterType: CompoundFilterType  # readonly
    ISTD: str  # readonly
    ISTDCompoundId: int  # readonly

class IImpersonationContext(System.IDisposable):  # Interface
    ...

class ILibrarySearchWindow(object):  # Interface
    def Search(self) -> None: ...
    @overload
    def SetTargetSpectrum(
        self, spectrum: Agilent.MassSpectrometry.DataAnalysis.ISpectrum
    ) -> None: ...
    @overload
    def SetTargetSpectrum(
        self,
        spectrum: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISpectrum,
    ) -> None: ...
    def ShowWindow(self) -> None: ...
    def SetLibraryMethod(self, methodPath: str) -> None: ...

class IMainFrame(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IWindow,
    System.Windows.Forms.IWin32Window,
):  # Interface
    def Layout(self, pattern: int) -> None: ...
    def ResetLayout(self) -> None: ...
    def ShowBatchPropertiesDialog(self) -> None: ...
    def ShowHelpIndex(self) -> None: ...
    def ShowHelpQuantitationDataSet(self) -> None: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def GetToolbarIds(self) -> List[str]: ...
    def ShowOutlierNavigator(self) -> None: ...
    def ShowOptionsDialog(self) -> None: ...
    def MaximizePane(self, paneKey: str) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def GetToolbar(self, id: str) -> IToolbar: ...
    def ShowHelpSearch(self) -> None: ...
    def ShowHelpContents(self) -> None: ...

class IMethodDataSet(object):  # Interface
    CalibrationTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataTable
    )  # readonly
    TargetCompoundTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataTable
    )  # readonly
    TargetQualifierTable: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataTable
    )  # readonly

    def GetGlobal(self, name: str) -> Any: ...

class IMethodErrorListPane(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane
):  # Interface
    def ShowMessages(self, messages: Any) -> None: ...
    def ValidateMethod(self, alwaysShowPane: bool) -> None: ...

class IMethodTablePane(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IGrid,
):  # Interface
    ArrangeCompoundsBy: str
    CalibrationsBandVisible: bool
    CanBrowseAcquisitionMethod: bool  # readonly
    CanDeleteRows: bool  # readonly
    CanFillDown: bool  # readonly
    CanGroupByTimeSegment: bool  # readonly
    CompoundsBandVisible: bool
    GroupByTimeSegment: bool
    HasNextCompound: bool  # readonly
    HasPreviousCompound: bool  # readonly
    OutlierSetup: OutlierColumns
    QualifiersBandVisible: bool
    TaskMode: MethodEditTaskMode
    TimeSegmentFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ITimeSegmentFilter
    )  # readonly

    def SetTimeSegmentFilter(
        self, filterType: CompoundFilterType, timeSegment: int
    ) -> None: ...
    def GetSelectedCompoundIds(self) -> List[int]: ...
    def PreviousCompound(self) -> None: ...
    def ShowPropertiesDialog(self) -> None: ...
    def GetFilteredCompoundIds(self) -> List[int]: ...
    def DeleteRows(self) -> None: ...
    @overload
    def ActivateCell(self, columnName: str) -> None: ...
    @overload
    def ActivateCell(self, compoundId: int, columnName: str) -> None: ...
    def NextCompound(self) -> None: ...
    def BrowseAcquisitionMethod(self) -> None: ...
    def FillDown(self) -> None: ...

class IMethodTasksPane(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane
):  # Interface
    def GetGroup(self, id: str) -> IExplorerBarGroup: ...

class IMethodValidationMessage(object):  # Interface
    ColumnName: str  # readonly
    IsError: bool  # readonly
    IsInfo: bool  # readonly
    IsWarning: bool  # readonly
    Message: str  # readonly
    TableName: str  # readonly

    def GetRowId(self) -> List[int]: ...

class IMetricsPlot(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPlotControlPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane,
):  # Interface
    DrawAverageStdDevLines: bool

    @overload
    def AddSeriesToActivePane(self, column: str) -> None: ...
    @overload
    def AddSeriesToActivePane(
        self, column: str, color: System.Drawing.Color
    ) -> None: ...
    def Clear(self) -> None: ...
    def IsPlottableColumn(self, column: str) -> bool: ...

class INumberFormat(INumericFormat):  # Interface
    def GetColumns(self) -> List[str]: ...
    @overload
    def SetFormat(self, column: str, formatString: str) -> None: ...
    @overload
    def SetFormat(self, column: str, format: INumericCustomFormat) -> None: ...
    def GetFormatString(self, column: str) -> str: ...
    def GetColumnCategory(self, column: str) -> str: ...
    def StoreFormats(self) -> None: ...
    def NotifyFormatChange(self) -> None: ...

class IOutlier(object):  # Interface
    Category: OutlierCategories  # readonly
    Column: OutlierColumns  # readonly
    FlagColumn: str  # readonly
    IsAvailable: bool  # readonly
    Table: OutlierTables  # readonly
    ValueColumn: str  # readonly

    def GetPrerequisiteColumns(self) -> List[str]: ...
    def GetOutlierInfo(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataRow,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IOutlierInfo: ...

class IOutlierDetector(object):  # Interface
    def GetOutlier(
        self, outlierColumn: OutlierColumns
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IOutlier: ...

class IOutlierInfo(object):  # Interface
    Deteil: str  # readonly
    LimitType: OutlierLimitType  # readonly
    Limits: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IOutlierLimits
    )  # readonly
    Message: str  # readonly
    Name: str  # readonly
    Value: Any  # readonly

class IOutlierLimits(object):  # Interface
    Max: float  # readonly
    Min: float  # readonly

class IPane(object):  # Interface
    CanCopy: bool  # readonly
    CanDelete: bool  # readonly
    CanPaste: bool  # readonly
    CanPrint: bool  # readonly
    Visible: bool

    def Copy(self) -> None: ...
    def GetToolbarIds(self) -> List[str]: ...
    def Print(self, displayDialog: bool) -> None: ...
    def PageSetup(self) -> None: ...
    def Delete(self) -> None: ...
    def Paste(self) -> None: ...
    def GetToolbar(self, id: str) -> IToolbar: ...
    def Activate(self) -> None: ...
    def PrintPreview(self) -> None: ...

class IPlotControlPane(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane
):  # Interface
    AnchorColumns: int  # readonly
    AnchorRows: int  # readonly
    AutoScale: bool
    CanAutoScale: bool  # readonly
    CanExport: bool  # readonly
    CanNextZoom: bool  # readonly
    CanPrevZoom: bool  # readonly
    ColumnCount: int  # readonly
    RowCount: int  # readonly

    def GetActiveObject(self) -> T: ...
    def AutoScaleY(self) -> None: ...
    def PrevZoom(self) -> None: ...
    def GetPane(
        self, rowIndex: int, columnIndex: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPlotPane: ...
    def ShowExportDialog(
        self,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IExportPlotParameters,
    ) -> System.Windows.Forms.DialogResult: ...
    def CreateExportParameters(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IExportPlotParameters
    ): ...
    def Export(
        self,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IExportPlotParameters,
    ) -> None: ...
    def AutoScaleX(self) -> None: ...
    def PrintToPdf(self, file: str) -> None: ...
    def NextZoom(self) -> None: ...
    def DrawPage(
        self,
        graphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        x: float,
        y: float,
        width: float,
        height: float,
        paintBackground: bool,
        anchoring: bool,
    ) -> None: ...

class IPlotPane(object):  # Interface
    MaxX: float
    MaxY: float
    MinX: float
    MinY: float
    Size: System.Drawing.Size  # readonly

    def AutoScaleY(self) -> None: ...
    @overload
    def Draw(
        self,
        graphics: System.Drawing.Graphics,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        graphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        x: float,
        y: float,
        width: float,
        height: float,
        ignoreLinkedAxis: bool,
        paintBackground: bool,
    ) -> None: ...
    def AutoScaleX(self) -> None: ...

class IReport(object):  # Interface
    def QuickReport(self, templateFile: str, outputFile: str) -> None: ...

class IReportTaskQueue(object):  # Interface
    IsRunning: bool  # readonly

    def ShowQueueViewer(self) -> None: ...
    def Run(self) -> None: ...

class IReviewItem(object):  # Interface
    DisplayText: str  # readonly

class ISampleDataPane(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPlotControlPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane,
):  # Interface
    AnchorChromatogram: bool
    CanCreateNewTargetCompound: bool  # readonly
    CanCreateNewTargetQualifier: bool  # readonly
    CanExtractSpectrum: bool  # readonly
    CanFindCompounds: bool  # readonly
    CanNormalizeEachX: bool  # readonly
    CanSearchLibrary: bool  # readonly
    HasSpectrumPanes: bool  # readonly
    MaxNumVisibleRows: int
    NormalizeType: NormalizeType
    OverlayAllSignals: bool
    OverlayIstdCompounds: bool
    OverlayTargetCompounds: bool
    SampleDataPath: str  # readonly
    ShowCurrentCompound: bool
    ShowTic: bool

    def GetDisplayedSignals(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISignalInfo
    ]: ...
    def FindCompounds(self) -> None: ...
    def ShowPropertiesDialog(self) -> None: ...
    def SearchLibrary(self) -> None: ...
    def GetMSScanColor(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Drawing.Color: ...
    def CreateNewTargetQualifier(self) -> None: ...
    def GetSignalColor(
        self,
        signal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISignalInfo,
    ) -> System.Drawing.Color: ...
    def CreateNewTargetCompound(self) -> None: ...
    def HideSignal(
        self,
        signal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISignalInfo,
    ) -> None: ...
    def ClearSpectrumPanes(self) -> None: ...
    def DisplayMSScan(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType, show: bool
    ) -> None: ...
    def GetAvailableMSScanTypes(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    def GetAvailableSignals(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISignalInfo
    ]: ...
    def GetDisplayedMSScanTypes(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    def DisplaySignal(
        self,
        signal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISignalInfo,
    ) -> None: ...
    def ExtractSpectrum(self) -> None: ...

class IScriptEngine(object):  # Interface
    CurrentScope: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IScriptScope
    )  # readonly
    DebugMode: bool  # readonly
    Engine: IScriptEngine  # readonly
    Globals: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IScriptScope
    )  # readonly

    def CreateScope(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IScriptScope: ...
    def ExecuteFile(
        self,
        file: str,
        scope: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(
        self,
        reader: System.IO.TextReader,
        encoding: System.Text.Encoding,
        scope: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(
        self,
        stream: System.IO.Stream,
        encoding: System.Text.Encoding,
        scope: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IScriptScope,
    ) -> Any: ...

class IScriptInterface(object):  # Interface
    BatchDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IBatchDataSet
    )  # readonly
    Compliance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ICompliance
    )  # readonly
    MethodDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IMethodDataSet
    )  # readonly
    OutlierDetector: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IOutlierDetector
    )  # readonly
    ReportTaskQueue: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IReportTaskQueue
    )  # readonly
    ScriptEngine: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IScriptEngine
    )  # readonly
    UIState: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState
    )  # readonly
    _ScriptInterface: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IScriptInterface
    )  # readonly

    def _WritePrivateProfileString(
        self, section: str, key: str, value_: str, fileName: str
    ) -> int: ...
    def PreCommandSetReason(self, reason: str) -> None: ...
    def _GetPrivateProfileString(
        self, section: str, key: str, defaultValue: str, fileName: str
    ) -> str: ...
    def PreCommandValidateUserEncrypted(
        self, user: str, encryptedPassword: str
    ) -> None: ...
    @overload
    def PreCommandValidateUser(self, user: str, password: str) -> None: ...
    @overload
    def PreCommandValidateUser(
        self, user: System.Security.SecureString, password: System.Security.SecureString
    ) -> None: ...

class IScriptPane(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane
):  # Interface
    def Run(self) -> None: ...
    def Clear(self) -> None: ...

class IScriptScope(object):  # Interface
    def GetVariableNames(self) -> Iterable[str]: ...
    def RemoveVariable(self, name: str) -> None: ...
    def GetVariable(self, name: str) -> Any: ...
    def ContainsVariable(self, name: str) -> bool: ...
    def SetVariable(self, name: str, value_: Any) -> None: ...

class ISelectRowsDialog(object):  # Interface
    HelpId: int
    InitialSelectionCondition: str
    LabelText: str
    MethodTable: bool
    MultipleSelection: bool
    RowFilter: str
    SelectionCount: int  # readonly
    Table: str
    Title: str

    @overload
    def AddColumn(self, columnName: str, caption: str) -> None: ...
    @overload
    def AddColumn(
        self, columnName: str, caption: str, format: INumericCustomFormat
    ) -> None: ...
    def ShowDialog(self) -> System.Windows.Forms.DialogResult: ...
    def GetSelectedRow(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataRow: ...
    def ClearColumns(self) -> None: ...

class IShiftRetentionTimeDialog(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISelectRowsDialog
):  # Interface
    AbsoluteShift: float
    RelativeShift: float

class ISignalInfo(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISignalInfo
    ]
):  # Interface
    DeviceName: str  # readonly
    IsMS: bool  # readonly
    OrdinalNumber: int  # readonly
    SignalName: str  # readonly

class ISpectrum(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IXYData
):  # Interface
    ISpectrum: Agilent.MassSpectrometry.DataAnalysis.ISpectrum  # readonly

class IStatusBar(object):  # Interface
    Visible: bool

class ITimeSegmentFilter(object):  # Interface
    FilterType: CompoundFilterType  # readonly
    TimeSegment: int  # readonly

class IUIState(object):  # Interface
    ActivePane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane
    )  # readonly
    ActiveWindow: System.Windows.Forms.IWin32Window  # readonly
    AddIns: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IAddInManager
    )  # readonly
    ApplicationPath: str  # readonly
    ApplicationType: str  # readonly
    BatchDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IBatchDataSet
    )  # readonly
    BatchDirectory: str  # readonly
    BatchFileName: str  # readonly
    BuildNumber: str  # readonly
    CalCurvePane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ICalCurvePane
    )  # readonly
    CalibrationAtAGlanceView: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ICalibrationAtAGlance
    )  # readonly
    CanEditMethod: bool  # readonly
    CanRedo: bool  # readonly
    CanUndo: bool  # readonly
    ChromSpecPane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromSpecPane
    )  # readonly
    ChromatogramInformationView: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogramInformation
    )  # readonly
    CompoundsAtAGlanceView: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ICompoundsAtAGlance
    )  # readonly
    Constants: Dict[str, str]  # readonly
    CurrentBatchId: int  # readonly
    CurrentCompoundId: int  # readonly
    CurrentIstdCompoundId: int  # readonly
    CurrentIstdCompoundName: str  # readonly
    CurrentLevelId: int  # readonly
    CurrentPeakId: int  # readonly
    CurrentQualifierId: int  # readonly
    CurrentSampleId: int  # readonly
    CurrentVersion: str  # readonly
    CustomerHome: str  # readonly
    EditMethodState: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IEditMethodState
    )  # readonly
    EditingMethod: bool  # readonly
    HasBatch: bool  # readonly
    HasIstd: bool  # readonly
    InstrumentType: InstrumentType  # readonly
    IsAuditTrailing: bool  # readonly
    IsBatchDirty: bool  # readonly
    IsCommandRunning: bool  # readonly
    IsCurrentSampleValid: bool  # readonly
    IsCurrentTargetCompoundValid: bool  # readonly
    IsInCommandGroup: bool  # readonly
    LibrarySearchWindow: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ILibrarySearchWindow
    )  # readonly
    MainFrame: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IMainFrame
    )  # readonly
    MethodDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IMethodDataSet
    )  # readonly
    MethodErrorListPane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IMethodErrorListPane
    )  # readonly
    MethodTablePane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IMethodTablePane
    )  # readonly
    MethodTasksPane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IMethodTasksPane
    )  # readonly
    MetricsPlot: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IMetricsPlot
    )  # readonly
    NumericFormat: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.INumberFormat
    )  # readonly
    Report: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IReport
    )  # readonly
    SampleDataPane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISampleDataPane
    )  # readonly
    ScriptInterface: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IScriptInterface
    )  # readonly
    ScriptPane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IScriptPane
    )  # readonly
    StatusBar: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IStatusBar
    )  # readonly
    SynchronizeInvoke: System.ComponentModel.ISynchronizeInvoke  # readonly
    ToolbarsManager: IToolbarsManager  # readonly
    Workflows: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IAddInManager
    )  # readonly
    WorktablePane: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IWorktablePane
    )  # readonly
    _AppCommandContext: AppCommandContext  # readonly
    _DataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator  # readonly
    _MainForm: Agilent.MassHunter.Quantitative.UIModel.IMainWindow  # readonly

    def CreateSelectRowsDialog(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISelectRowsDialog
    ): ...
    def GetTargetCompoundChromatogram(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogram
    ): ...
    def Undo(self) -> None: ...
    def AddRecentBatch(self, batchPath: str, batchFile: str) -> None: ...
    def ShowAboutBox(self) -> None: ...
    def Redo(self) -> None: ...
    def GetCurrentTargetCompoundRow(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataRow: ...
    def GetTargetCompoundSpectrum(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISpectrum: ...
    def CreateShiftRetentionTimeDialog(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IShiftRetentionTimeDialog
    ): ...
    def CreateAverageQualifierRatiosDialog(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IAverageQualifierRatiosDialog
    ): ...
    def NavigateCompound(self, compoundId: int) -> None: ...
    def ShowExceptionMessage(self, ex: System.Exception) -> None: ...
    @overload
    def GetTIC(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogram
    ): ...
    @overload
    def GetTIC(
        self,
        level: Agilent.MassSpectrometry.DataAnalysis.MSLevel,
        scanTypes: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        minRT: float,
        maxRT: float,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogram
    ): ...
    def EndRunScript(self, result: System.IAsyncResult) -> Any: ...
    def GetIstdCompoundChromatogram(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogram
    ): ...
    def BeginCommandGroup(self) -> None: ...
    @overload
    def ExecuteCommandWithProgressDialog(
        self, commandType: System.Type, parameters: List[Any]
    ) -> Any: ...
    @overload
    def ExecuteCommandWithProgressDialog(
        self,
        parent: System.Windows.Forms.IWin32Window,
        commandType: System.Type,
        parameters: List[Any],
    ) -> Any: ...
    def GetCompoundSpectrum(
        self, sampleId: int, compoundId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISpectrum: ...
    def ShowAuditTrailView(self) -> None: ...
    def GetIstdCompoundSpectrum(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISpectrum: ...
    def ClearRecentBatches(self) -> None: ...
    def SaveGraphicsSettingsTo(self, file: str) -> None: ...
    def GetRecentBatches(self) -> List[str]: ...
    def GetCompoundChromatogram(
        self, sampleId: int, compoundId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogram
    ): ...
    def CreateAverageRetentionTimeDialogs(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IAverageRetentionTimeDialog
    ): ...
    def NavigateSample(self, sampleId: int) -> None: ...
    def ExceptionAbort(self, ex: System.Exception) -> None: ...
    def GetCurrentSampleRow(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataRow: ...
    def GetReferenceLibrarySpectrum(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISpectrum: ...
    def BeginRunScript(
        self, stream: System.IO.Stream, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def GetPane(
        self, paneId: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane: ...
    def GetQualifierChromatogram(
        self, sampleId: int, compoundId: int, qualifierId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IChromatogram
    ): ...
    def SaveConfiguration(self) -> None: ...
    def GetTargetCompoundSpectrumForReferenceLibraryMatch(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ISpectrum: ...
    def CloseMainForm(self) -> None: ...
    def ExecuteCommand(
        self,
        parent: System.Windows.Forms.IWin32Window,
        commandType: System.Type,
        parameters: List[Any],
    ) -> Any: ...
    def PerformCompliancePreCommand(
        self, parent: System.Windows.Forms.IWin32Window, commandName: str, action: str
    ) -> bool: ...
    def RunScript(self, file: str) -> Any: ...
    def ShowMessage(
        self,
        message: str,
        caption: str,
        buttons: System.Windows.Forms.MessageBoxButtons,
        icon: System.Windows.Forms.MessageBoxIcon,
    ) -> System.Windows.Forms.DialogResult: ...
    def EndCommandGroup(self) -> None: ...

    CommandEnd: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.CommandEventArgs
    ]  # Event
    CommandGroupEnded: System.EventHandler  # Event
    CommandGroupStarted: System.EventHandler  # Event
    CommandStart: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.CommandEventArgs
    ]  # Event
    NavigateChanged: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.NavigateChangeEventArgs
    ]  # Event

class IWindow(object):  # Interface
    Height: int
    Location: System.Drawing.Point
    Width: int

    Closed: System.EventHandler  # Event

class IWorktablePane(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IGrid,
):  # Interface
    ArrangeCompoundsBy: CompoundKeySortType
    CanFillDown: bool  # readonly
    CanStartAutoReview: bool  # readonly
    CompoundGroupFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ICompoundGroupFilter
    )
    CompoundKey: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ICompoundKey
    )
    CompoundListTableMode: bool
    DisplayAllSampleGroups: bool
    DisplayAllSampleTypes: bool
    FilterOutliers: bool
    FlagOutliers: bool
    FlatTableMode: bool
    HasNextCompound: bool  # readonly
    HasNextSample: bool  # readonly
    HasPreviousCompound: bool  # readonly
    HasPreviousSample: bool  # readonly
    HorizontalNestedTableMode: bool
    ISTDFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IISTDFilter
    )
    LockSampleColumns: bool
    OutlierFilterType: OutlierFilterType
    SingleCompoundMode: bool
    TimeSegmentFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ITimeSegmentFilter
    )
    UIState: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState
    )  # readonly
    VerticalNestedTableMode: bool

    def GetFilteredSamples(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IDataRow
    ]: ...
    def FillDown(self) -> None: ...
    def NextCompound(self) -> None: ...
    def GetISTDFilters(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IISTDFilter
    ]: ...
    def ShowPropertiesDialog(self) -> None: ...
    def StartAutoReview(self, reviewCompounds: bool) -> None: ...
    def SetDisplaySampleType(self, type: str, display: bool) -> None: ...
    def ShowSelectOutliersDialog(self) -> None: ...
    def GetDisplaySampleGroup(self, group: str) -> bool: ...
    def GetTimeSegmentFilters(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ITimeSegmentFilter
    ]: ...
    def NextSample(self) -> None: ...
    def DeleteSelectedSamples(self) -> None: ...
    def GetDisplaySampleType(self, type: str) -> bool: ...
    def EnableOutlier(self, outlier: OutlierColumns, enable: bool) -> None: ...
    def GetCompoundGroupFilters(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ICompoundGroupFilter
    ]: ...
    def PreviousSample(self) -> None: ...
    def GetDisplayedSampleGroups(self) -> List[str]: ...
    def CanDeleteSelectedSamples(self) -> bool: ...
    def GetSelectedSamples(self) -> List[SampleRowId]: ...
    def GetDisplayedSampleTypes(self) -> List[str]: ...
    def SetDisplaySampleGroup(self, group: str, display: bool) -> None: ...
    def GetFilteredCompoundKeys(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.ICompoundKey
    ]: ...
    def RefreshSampleFilter(self) -> None: ...
    def PreviousCompound(self) -> None: ...

class IXYData(object):  # Interface
    Count: int  # readonly
    MaxX: float  # readonly
    MaxY: float  # readonly
    MinX: float  # readonly
    MinY: float  # readonly
    Title: str  # readonly

    def GetX(self, index: int) -> float: ...
    def GetY(self, index: int) -> float: ...

class NavigateChangeEventArgs(System.EventArgs):  # Class
    def __init__(
        self,
        prevSampleId: int,
        prevCompoundId: int,
        newSampleId: int,
        newCompoundId: int,
    ) -> None: ...

    NewCompoundId: int  # readonly
    NewSampleId: int  # readonly
    PreviousCompoundId: int  # readonly
    PreviousSampleId: int  # readonly

class Utils:  # Class
    @staticmethod
    def TryCast(obj: Any) -> T: ...
