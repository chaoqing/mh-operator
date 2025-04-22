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
    AppCommandBase,
    AppCommandContext,
    CompoundFilterType,
    InstrumentType,
    INumericCustomFormat,
    INumericFormat,
    OutlierCategories,
    OutlierColumns,
    OutlierLimitType,
    OutlierTables,
    Printing,
    PrintPlotFitType,
    QuantitationDataSet,
    TargetCompoundRowId,
)
from .Controls2 import PropertySheet
from .ScriptEngine import IronEngine, IScriptEngine
from .Toolbar import IToolbar, IToolbarsManager
from .UIScriptIF import (
    CommandEventArgs,
    IAddIn,
    IAddInManager,
    IAverageQualifierRatiosDialog,
    IAverageRetentionTimeDialog,
    IBatchDataSet,
    ICalCurvePane,
    ICalibrationAtAGlance,
    IChromatogram,
    IChromatogramInformation,
    IChromatogramInformationItem,
    IChromSpecPane,
    ICompliance,
    ICompoundGroupFilter,
    ICompoundsAtAGlance,
    IDataRow,
    IEditMethodState,
    IExportPlotParameters,
    IGridRow,
    IImpersonationContext,
    ILibrarySearchWindow,
    IMainFrame,
    IMethodDataSet,
    IMethodErrorListPane,
    IMethodTablePane,
    IMethodTasksPane,
    IMethodValidationMessage,
    IMetricsPlot,
    INumberFormat,
    IOutlier,
    IOutlierDetector,
    IOutlierInfo,
    IOutlierLimits,
    IPane,
    IReport,
    IReportTaskQueue,
    ISampleDataPane,
    IScriptEngine,
    IScriptInterface,
    IScriptPane,
    IScriptScope,
    ISelectRowsDialog,
    IShiftRetentionTimeDialog,
    ISignalInfo,
    ISpectrum,
    IStatusBar,
    IUIState,
    IWindow,
    IWorktablePane,
    NavigateChangeEventArgs,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls

class AddInManager(System.MarshalByRefObject, IAddInManager):  # Class
    def __init__(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls.UIState,
    ) -> None: ...
    def __getitem__(self, id: str) -> IAddIn: ...
    def InitializeWorkflows(self) -> None: ...
    def Initialize(self) -> None: ...
    def Clear(self) -> None: ...
    def GetIDs(self) -> List[str]: ...

class CalibrationAtAGlance(
    IWindow,
    ICalibrationAtAGlance,
    IPane,
    System.Windows.Forms.IWin32Window,
    System.MarshalByRefObject,
):  # Class
    CanCopy: bool  # readonly
    CanDelete: bool  # readonly
    CanPaste: bool  # readonly
    CanPrint: bool  # readonly
    Handle: System.IntPtr  # readonly
    Height: int
    Location: System.Drawing.Point
    NumPaneColumnsPerPage: int  # readonly
    NumPaneRowsPerPage: int  # readonly
    Visible: bool
    Width: int

    def SetPaneDimension(self, rows: int, columns: int) -> None: ...
    def Copy(self) -> None: ...
    def GetToolbarIds(self) -> List[str]: ...
    def GetSelectedTargetCompounds(self) -> List[TargetCompoundRowId]: ...
    def Print(self, displayDialog: bool) -> None: ...
    def Close(self) -> None: ...
    def PageSetup(self) -> None: ...
    def Delete(self) -> None: ...
    def Paste(self) -> None: ...
    def Activate(self) -> None: ...
    def GetToolbar(self, id: str) -> IToolbar: ...
    def PrintPreview(self) -> None: ...
    def Show(self) -> None: ...

    Closed: System.EventHandler  # Event
    WindowCreated: System.EventHandler  # Event

class ChromatogramInformationItem(
    System.MarshalByRefObject, IChromatogramInformationItem
):  # Class
    BatchID: int  # readonly
    Color: System.Drawing.Color
    DataFileName: str  # readonly
    InstrumentName: str  # readonly
    SampleID: int  # readonly
    SampleName: str  # readonly
    ScanType: Optional[Agilent.MassSpectrometry.DataAnalysis.MSScanType]  # readonly
    Signal: ISignalInfo  # readonly
    Visible: bool
    _Item: (
        Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationItem
    )  # readonly

class ComplianceCore(System.MarshalByRefObject, ICompliance):  # Class
    AlwaysAuditTrail: bool  # readonly
    ConnectionTicket: str  # readonly
    IsActive: bool  # readonly
    IsInstalled: bool  # readonly
    IsLocal: bool  # readonly
    Name: str  # readonly
    User: str  # readonly

    def IsUserValidationRequired(self, command: str) -> bool: ...
    def SetCommandReason(self, reason: str) -> None: ...
    def Impersonate(self) -> IImpersonationContext: ...
    def IsCommandReasonRequired(self, command: str) -> bool: ...
    def CheckoutBatch(self, batchFolder: str, batchFile: str) -> None: ...
    def HasPermission(self, command: str) -> bool: ...
    @overload
    def TranslateToLocalPath(self, path: str) -> str: ...
    @overload
    def TranslateToLocalPath(self, path: str, revisionNumber: str) -> str: ...
    @overload
    def ValidateUser(
        self, user: System.Security.SecureString, password: System.Security.SecureString
    ) -> None: ...
    @overload
    def ValidateUser(self, user: str, password: str) -> None: ...
    def IsBatchCheckedoutByCurrentUser(
        self, batchFolder: str, batchFile: str
    ) -> bool: ...
    def ValidateUserEncrypted(self, user: str, encryptedPassword: str) -> None: ...
    def UndoCheckoutBatch(self, batchFolder: str, batchFile: str) -> None: ...

class CompoundGroupFilter(System.MarshalByRefObject, ICompoundGroupFilter):  # Class
    def __init__(
        self, info: Agilent.MassHunter.Quantitative.UIModel.CompoundGroupFilterInfo
    ) -> None: ...

    CompoundGroup: str  # readonly
    FilterType: CompoundFilterType  # readonly

    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    def Equals(self, obj: Any) -> bool: ...

class Constants(
    Sequence[System.Collections.Generic.KeyValuePair[str, str]],
    Dict[str, str],
    Iterable[System.Collections.Generic.KeyValuePair[str, str]],
    Iterable[Any],
    System.MarshalByRefObject,
):  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly
    IsReadOnly: bool  # readonly
    def __getitem__(self, key: str) -> str: ...
    def __setitem__(self, key: str, value_: str) -> None: ...
    Keys: Sequence[str]  # readonly
    Values: Sequence[str]  # readonly

    def GetEnumerator(
        self,
    ) -> Iterator[System.Collections.Generic.KeyValuePair[str, str]]: ...
    def Contains(
        self, item: System.Collections.Generic.KeyValuePair[str, str]
    ) -> bool: ...
    def CopyTo(
        self,
        array: List[System.Collections.Generic.KeyValuePair[str, str]],
        arrayIndex: int,
    ) -> None: ...
    def Add(self, key: str, value_: str) -> None: ...
    def ContainsKey(self, key: str) -> bool: ...
    def Clear(self) -> None: ...
    @overload
    def Remove(self, key: str) -> bool: ...
    @overload
    def Remove(
        self, item: System.Collections.Generic.KeyValuePair[str, str]
    ) -> bool: ...
    def TryGetValue(self, key: str, value_: str) -> bool: ...

class CustomPane(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls.PaneBase, IPane
):  # Class
    def __init__(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls.UIState,
        key: str,
    ) -> None: ...

    CanCopy: bool  # readonly
    CanDelete: bool  # readonly
    CanPaste: bool  # readonly
    CanPrint: bool  # readonly

    def Copy(self) -> None: ...
    def Print(self, displayDialog: bool) -> None: ...
    def PageSetup(self) -> None: ...
    def Delete(self) -> None: ...
    def Paste(self) -> None: ...
    def PrintPreview(self) -> None: ...

class EventDispatcher:  # Class
    def __init__(self, invoke: System.ComponentModel.ISynchronizeInvoke) -> None: ...
    def Remove(
        self, sender: Any, target: System.Delegate
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls.EventDispatcher.EventBridge
    ): ...
    def Add(
        self, key: str, sender: Any, target: System.Delegate, convert: System.Delegate
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls.EventDispatcher.EventBridge
    ): ...
    def Dispose(self) -> None: ...
    def DispatchByKey(self, key: str, sender: Any, e: System.EventArgs) -> None: ...

    # Nested Types

    class EventBridge:  # Class
        def __init__(
            self,
            invoke: System.ComponentModel.ISynchronizeInvoke,
            key: str,
            sender: Any,
            target: System.Delegate,
            convert: System.Delegate,
        ) -> None: ...

        Key: str  # readonly

        def Dispatch(self, sender: Any, e: System.EventArgs) -> None: ...
        def Equals(self, sender: Any, target: System.Delegate) -> bool: ...

class ExportPlotParameters(System.MarshalByRefObject, IExportPlotParameters):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parameters: IExportPlotParameters) -> None: ...

    AllPanes: bool
    FilePath: str
    FitType: PrintPlotFitType
    ImageFormat: System.Drawing.Imaging.ImageFormat
    PageSize: System.Drawing.SizeF
    Zoom: float

    def Export(
        self, control: Agilent.MassSpectrometry.GUI.Plot.PlotControl
    ) -> None: ...
    def ReadFromConfiguration(self) -> None: ...
    def SaveToConfiguration(self) -> None: ...

class GridRow(System.MarshalByRefObject, IGridRow):  # Class
    BandName: str  # readonly
    def __getitem__(self, columnName: str) -> Any: ...

class ImpersonationContext(
    IImpersonationContext, System.MarshalByRefObject, System.IDisposable
):  # Class
    def Dispose(self) -> None: ...

class MethodErrorListPane(
    IMethodErrorListPane,
    IPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls.PaneBase,
):  # Class
    CanCopy: bool  # readonly
    CanDelete: bool  # readonly
    CanPaste: bool  # readonly
    CanPrint: bool  # readonly

    def ValidateMethod(self, alwaysShowPane: bool) -> None: ...
    def ShowMessages(self, messages: Any) -> None: ...
    def Copy(self) -> None: ...
    def Print(self, displayDialog: bool) -> None: ...
    def PageSetup(self) -> None: ...
    def Delete(self) -> None: ...
    def Paste(self) -> None: ...
    def PrintPreview(self) -> None: ...

class MethodValidationMessage(
    System.MarshalByRefObject, IMethodValidationMessage
):  # Class
    ColumnName: str  # readonly
    IsError: bool  # readonly
    IsInfo: bool  # readonly
    IsWarning: bool  # readonly
    Message: str  # readonly
    TableName: str  # readonly

    def GetRowId(self) -> List[int]: ...

class NumberFormat(System.MarshalByRefObject, INumberFormat, INumericFormat):  # Class
    def Contains(self, columnName: str) -> bool: ...
    def GetColumns(self) -> List[str]: ...
    @overload
    def SetFormat(self, column: str, format: INumericCustomFormat) -> None: ...
    @overload
    def SetFormat(self, column: str, format: str) -> None: ...
    def GetFormatString(self, columnName: str) -> str: ...
    def GetFormat(self, columnName: str) -> INumericCustomFormat: ...
    def GetColumnCategory(self, column: str) -> str: ...
    def StoreFormats(self) -> None: ...
    def NotifyFormatChange(self) -> None: ...

class OptionsDialog(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    PropertySheet,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

class Outlier(System.MarshalByRefObject, IOutlier):  # Class
    Category: OutlierCategories  # readonly
    Column: OutlierColumns  # readonly
    FlagColumn: str  # readonly
    IsAvailable: bool  # readonly
    Table: OutlierTables  # readonly
    ValueColumn: str  # readonly

    def GetPrerequisiteColumns(self) -> List[str]: ...
    def GetOutlierInfo(self, row: IDataRow) -> IOutlierInfo: ...

class OutlierDetector(System.MarshalByRefObject, IOutlierDetector):  # Class
    def GetOutlier(self, outlierType: OutlierColumns) -> IOutlier: ...

class OutlierInfo(System.MarshalByRefObject, IOutlierInfo):  # Class
    Deteil: str  # readonly
    LimitType: OutlierLimitType  # readonly
    Limits: IOutlierLimits  # readonly
    Message: str  # readonly
    Name: str  # readonly
    Value: Any  # readonly

class OutlierLimits(System.MarshalByRefObject, IOutlierLimits):  # Class
    def __init__(
        self, r: Agilent.MassSpectrometry.DataAnalysis.MinMaxRange
    ) -> None: ...

    Max: float  # readonly
    Min: float  # readonly

class OutlierNavigatorControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UserControl,
):  # Class
    def __init__(self) -> None: ...

class OutlierNavigatorDialog(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...
    def Initialize(
        self,
        navigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator,
        flagFilterManager: Agilent.MassHunter.Quantitative.UIModel.IFlagFilterManager,
    ) -> None: ...

class PaneBase(System.MarshalByRefObject, IPane):  # Class
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

class Report(System.IDisposable, IReport):  # Class
    def Dispose(self) -> None: ...
    def QuickReport(self, templateFile: str, outputFile: str) -> None: ...

class ScriptEngine(
    IScriptEngine, System.MarshalByRefObject, System.IDisposable
):  # Class
    CurrentScope: IScriptScope  # readonly
    DebugMode: bool  # readonly
    Engine: IScriptEngine  # readonly
    Globals: IScriptScope  # readonly

    def CreateScope(self) -> IScriptScope: ...
    @overload
    def Execute(
        self,
        reader: System.IO.TextReader,
        encoding: System.Text.Encoding,
        scope: IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(
        self,
        stream: System.IO.Stream,
        encoding: System.Text.Encoding,
        scope: IScriptScope,
    ) -> Any: ...
    @staticmethod
    def SetDebugEngine(
        engine: IronEngine, initEngine: System.Action[IronEngine, Any]
    ) -> None: ...
    def Dispose(self) -> None: ...
    def ExecuteFile(self, file: str, scope: IScriptScope) -> Any: ...

class ScriptInterface(System.MarshalByRefObject, IScriptInterface):  # Class
    BatchDataSet: IBatchDataSet  # readonly
    Compliance: ICompliance  # readonly
    MethodDataSet: IMethodDataSet  # readonly
    OutlierDetector: IOutlierDetector  # readonly
    ReportTaskQueue: IReportTaskQueue  # readonly
    ScriptEngine: IScriptEngine  # readonly
    UIState: IUIState  # readonly
    _ScriptInterface: IScriptInterface  # readonly

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

class ScriptPane(
    IPane,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls.PaneBase,
    IScriptPane,
):  # Class
    CanCopy: bool  # readonly
    CanDelete: bool  # readonly
    CanPaste: bool  # readonly
    CanPrint: bool  # readonly

    def Copy(self) -> None: ...
    def Clear(self) -> None: ...
    def Print(self, displayDialog: bool) -> None: ...
    def PageSetup(self) -> None: ...
    def Delete(self) -> None: ...
    def Paste(self) -> None: ...
    def PrintPreview(self) -> None: ...
    def Run(self) -> None: ...

class SignalInfo(
    System.MarshalByRefObject, System.IComparable[ISignalInfo], ISignalInfo
):  # Class
    DeviceName: str  # readonly
    IsMS: bool  # readonly
    OrdinalNumber: int  # readonly
    SignalName: str  # readonly

    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    def Compare(
        self,
        signal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls.SignalInfo,
    ) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class UIState(System.MarshalByRefObject, IUIState):  # Class
    def __init__(
        self, form: Agilent.MassHunter.Quantitative.UIModel.IMainWindow
    ) -> None: ...

    ActivePane: IPane  # readonly
    ActiveWindow: System.Windows.Forms.IWin32Window  # readonly
    AddIns: IAddInManager  # readonly
    ApplicationPath: str  # readonly
    ApplicationType: str  # readonly
    BatchDataSet: IBatchDataSet  # readonly
    BatchDirectory: str  # readonly
    BatchFileName: str  # readonly
    BuildNumber: str  # readonly
    CalCurvePane: ICalCurvePane  # readonly
    CalibrationAtAGlanceView: ICalibrationAtAGlance  # readonly
    CanEditMethod: bool  # readonly
    CanRedo: bool  # readonly
    CanUndo: bool  # readonly
    ChromSpecPane: IChromSpecPane  # readonly
    ChromatogramInformationView: IChromatogramInformation  # readonly
    CompoundsAtAGlanceView: ICompoundsAtAGlance  # readonly
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
    DataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator  # readonly
    EditMethodState: IEditMethodState  # readonly
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
    LibrarySearchWindow: ILibrarySearchWindow  # readonly
    MainFrame: IMainFrame  # readonly
    MethodDataSet: IMethodDataSet  # readonly
    MethodErrorListPane: IMethodErrorListPane  # readonly
    MethodTablePane: IMethodTablePane  # readonly
    MethodTasksPane: IMethodTasksPane  # readonly
    MetricsPlot: IMetricsPlot  # readonly
    NumericFormat: INumberFormat  # readonly
    Report: IReport  # readonly
    SampleDataPane: ISampleDataPane  # readonly
    ScriptInterface: IScriptInterface  # readonly
    ScriptPane: IScriptPane  # readonly
    StatusBar: IStatusBar  # readonly
    SynchronizeInvoke: System.ComponentModel.ISynchronizeInvoke  # readonly
    ToolbarsManager: IToolbarsManager  # readonly
    Workflows: IAddInManager  # readonly
    WorktablePane: IWorktablePane  # readonly
    _AppCommandContext: AppCommandContext  # readonly
    _BatchDataSet: QuantitationDataSet  # readonly
    _DataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator  # readonly
    _MainForm: Agilent.MassHunter.Quantitative.UIModel.IMainWindow  # readonly
    _MethodDataSet: QuantitationDataSet  # readonly

    def CreateSelectRowsDialog(self) -> ISelectRowsDialog: ...
    def GetTargetCompoundChromatogram(self) -> IChromatogram: ...
    def Undo(self) -> None: ...
    def AddRecentBatch(self, batchPath: str, batchFile: str) -> None: ...
    def ShowAboutBox(self) -> None: ...
    def Redo(self) -> None: ...
    def GetCurrentTargetCompoundRow(self) -> IDataRow: ...
    def CreateChromatogramInformationWindow(
        self,
    ) -> Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationWindow: ...
    def CreateShiftRetentionTimeDialog(self) -> IShiftRetentionTimeDialog: ...
    def GetTargetCompoundSpectrum(self) -> ISpectrum: ...
    def CreateAverageQualifierRatiosDialog(self) -> IAverageQualifierRatiosDialog: ...
    def NavigateCompound(self, compoundId: int) -> None: ...
    def ShowExceptionMessage(self, e: System.Exception) -> None: ...
    def CleanAddIns(self) -> None: ...
    def CreateCagWindow(self) -> Agilent.MassHunter.Quantitative.UIModel.ICagWindow: ...
    @overload
    def GetTIC(self) -> IChromatogram: ...
    @overload
    def GetTIC(
        self,
        msLevel: Agilent.MassSpectrometry.DataAnalysis.MSLevel,
        scanTypes: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        minRT: float,
        maxRT: float,
    ) -> IChromatogram: ...
    def Dispose(self) -> None: ...
    def EndRunScript(self, result: System.IAsyncResult) -> Any: ...
    def GetIstdCompoundChromatogram(self) -> IChromatogram: ...
    def BeginCommandGroup(self) -> None: ...
    @overload
    @staticmethod
    def ExecuteCommandWithProgressDialog(
        commandType: System.Type, parameters: List[Any]
    ) -> Any: ...
    @overload
    @staticmethod
    def ExecuteCommandWithProgressDialog(
        parent: System.Windows.Forms.IWin32Window,
        commandType: System.Type,
        parameters: List[Any],
    ) -> Any: ...
    @overload
    @staticmethod
    def ExecuteCommandWithProgressDialog(
        state: Agilent.MassHunter.Quantitative.UIModel.IPresentationState,
        parent: System.Windows.Forms.IWin32Window,
        command: AppCommandBase,
    ) -> Any: ...
    def SetConstant(self, key: str, value_: str) -> None: ...
    def GetCompoundSpectrum(self, sampleId: int, compoundId: int) -> ISpectrum: ...
    def ShowAuditTrailView(self) -> None: ...
    def GetIstdCompoundSpectrum(self) -> ISpectrum: ...
    def ClearRecentBatches(self) -> None: ...
    def SaveGraphicsSettingsTo(self, file: str) -> None: ...
    def GetRecentBatches(self) -> List[str]: ...
    def GetCompoundChromatogram(
        self, sampleId: int, compoundId: int
    ) -> IChromatogram: ...
    def CreateAverageRetentionTimeDialogs(self) -> IAverageRetentionTimeDialog: ...
    def NavigateSample(self, sampleId: int) -> None: ...
    def InitAddIns(self) -> None: ...
    def ExceptionAbort(self, e: System.Exception) -> None: ...
    def GetCurrentSampleRow(self) -> IDataRow: ...
    def GetReferenceLibrarySpectrum(self) -> ISpectrum: ...
    def CreateCalibrationAtAGlanceWindow(
        self,
    ) -> Agilent.MassHunter.Quantitative.UIModel.ICalibrationAtAGlanceWindow: ...
    def BeginRunScript(
        self, stream: System.IO.Stream, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def GetPane(self, paneId: str) -> IPane: ...
    def GetQualifierChromatogram(
        self, sampleId: int, compoundId: int, qualifierId: int
    ) -> IChromatogram: ...
    def SaveConfiguration(self) -> None: ...
    def GetTargetCompoundSpectrumForReferenceLibraryMatch(self) -> ISpectrum: ...
    def CloseMainForm(self) -> None: ...
    @overload
    @staticmethod
    def ExecuteCommand(
        parent: System.Windows.Forms.IWin32Window,
        commandType: System.Type,
        parameters: List[Any],
    ) -> Any: ...
    @overload
    @staticmethod
    def ExecuteCommand(
        state: Agilent.MassHunter.Quantitative.UIModel.IPresentationState,
        parent: System.Windows.Forms.IWin32Window,
        cmd: AppCommandBase,
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

    CommandEnd: System.EventHandler[CommandEventArgs]  # Event
    CommandGroupEnded: System.EventHandler  # Event
    CommandGroupStarted: System.EventHandler  # Event
    CommandStart: System.EventHandler[CommandEventArgs]  # Event
    NavigateChanged: System.EventHandler[NavigateChangeEventArgs]  # Event
