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

from . import Dialogs

# Discovered Generic TypeVars:
T = TypeVar("T")
from . import (
    BatchFile,
    ChromatogramPeakLabelType,
    ChromatographyType,
    InstrumentType,
    INumericFormat,
    PlotTitleElement,
    QualifierInfoLabelType,
    QuantitationDataSet,
)
from .Compliance import ICompliance
from .Configuration import NumberFormats
from .ScriptEngine import IScriptEngine
from .Toolbar import IScriptToolHandler, IToolHandler, IToolState
from .UIScriptIF import IScriptScope, IUIState

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils

class AskApplyAnalyzeDialog(
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

    Analyze: bool  # readonly
    Integrate: bool  # readonly
    Quantitate: bool  # readonly

class BatchPropertiesDialog(
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

    BatchFile: BatchFile

class BindingObjectCollection(
    Iterable[T],
    Generic[T],
    System.ComponentModel.IRaiseItemChangedEvents,
    System.IDisposable,
    Sequence[T],
    System.ComponentModel.IBindingList,
    System.ComponentModel.ICancelAddNew,
    System.ComponentModel.IComponent,
    List[Any],
    System.ComponentModel.BindingList[T],
    List[T],
    Iterable[Any],
    Sequence[Any],
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, container: System.ComponentModel.IContainer) -> None: ...

    BoundObject: T
    Site: System.ComponentModel.ISite

    def OnListChanged(self, e: System.ComponentModel.ListChangedEventArgs) -> None: ...
    def Dispose(self) -> None: ...

    Disposed: System.EventHandler  # Event

class ClipboardUtils:  # Class
    @staticmethod
    def GetDataObject() -> System.Windows.Forms.IDataObject: ...

class ControlBox:  # Class
    HasHelpButtonProperty: System.Windows.DependencyProperty  # static # readonly
    HasMaximizeButtonProperty: System.Windows.DependencyProperty  # static # readonly
    HasMinimizeButtonProperty: System.Windows.DependencyProperty  # static # readonly
    HasSysMenuProperty: System.Windows.DependencyProperty  # static # readonly

    @staticmethod
    def SetHasMaximizeButton(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def SetHasHelpButton(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def SetHasMinimizeButton(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def SetHasSysMenu(element: System.Windows.Window, value_: bool) -> None: ...
    @staticmethod
    def GetHasHelpButton(element: System.Windows.Window) -> bool: ...
    @staticmethod
    def GetHasMaximizeButton(element: System.Windows.Window) -> bool: ...
    @staticmethod
    def GetHasSysMenu(element: System.Windows.Window) -> bool: ...
    @staticmethod
    def GetHasMinimizeButton(element: System.Windows.Window) -> bool: ...

class DefaultEventManipulatorBase(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.DefaultEventManipulatorBase,
):  # Class
    def __init__(
        self, context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext
    ) -> None: ...

class EnumItemCollection(
    Sequence[Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.EnumItem[T]],
    Generic[T],
    System.IDisposable,
    Iterable[Any],
    Sequence[Any],
    System.ComponentModel.IComponent,
    List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.EnumItem[T]],
    Iterable[Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.EnumItem[T]],
    List[Any],
    System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.EnumItem[T]
    ],
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, container: System.ComponentModel.IContainer) -> None: ...

    Site: System.ComponentModel.ISite

    def Dispose(self) -> None: ...

    Disposed: System.EventHandler  # Event

class EnumItem(Generic[T]):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, t: T) -> None: ...
    @overload
    def __init__(self, t: T, displayText: str) -> None: ...

    DisplayText: str  # readonly
    Value: T
    ValueText: str  # readonly

    def ToString(self) -> str: ...

class FileUtilities:  # Class
    Ext_CdbFiles: str = ...  # static # readonly
    Ext_ReportMethodFile_Quant: str = ...  # static # readonly
    Ext_ReportMethodFile_Unknowns: str = ...  # static # readonly
    Ext_UnknownsAnalysisFile: str = ...  # static # readonly
    MethodFolderExt: str = ...  # static # readonly
    UnifiedMethod_MethodFile_Quant: str = ...  # static # readonly
    UnifiedMethod_MethodFile_TuneEval: str = ...  # static # readonly
    UnifiedMethod_ReportMethodFile: str = ...  # static # readonly
    UnifiedMethod_ReportMethodPath_Quant: str = ...  # static # readonly
    UnifiedMethod_ReportMethodPath_Unknowns: str = ...  # static # readonly

    BatchFolderExtension: str  # static # readonly
    BinBatchFileExtension: str  # static # readonly
    ColumnsSettingsFileExtension: str  # static # readonly
    ColumnsSettingsFileFilter: str  # static # readonly
    FixedGraphicsFileExtension: str  # static # readonly
    FixedGraphicsFileFilter: str  # static # readonly
    GraphicsSettingsFileExtension: str  # static # readonly
    GraphicsSettingsFileFilter: str  # static # readonly
    LayoutFileExtension: str  # static # readonly
    LayoutFileFilter: str  # static # readonly
    MSLibraryExtensionBin: str  # static # readonly
    MSLibraryExtensionXml: str  # static # readonly
    MethodFileExtension: str  # static # readonly
    MethodFileFilter: str  # static # readonly
    MethodFolderExtension: str  # static # readonly
    NistLibraryFolderExtension: str  # static # readonly
    PDFReportTemplateExtension: str  # static # readonly
    PDFReportUnknownsTemplateExtension: str  # static # readonly
    PatternRefLibraryExtension: str  # static # readonly
    RTCalibrationFileExtension: str  # static # readonly
    RefLibraryExtension: str  # static # readonly
    ReportAuditTrailFileName: str  # static # readonly
    ReportBuilderTemplateExtension: str  # static # readonly
    ReportResultFileName: str  # static # readonly
    ReportTemplatesFolder: str  # static # readonly
    ResultsFolderName: str  # static # readonly
    SampleFolderExtension: str  # static # readonly
    SharedCustomerHome: str  # static # readonly
    XmlBatchFileExtension: str  # static # readonly

    @staticmethod
    def FindBatchFiles(batchFolder: str) -> List[str]: ...
    @staticmethod
    def FindSampleDirectories(batchFolder: str) -> List[str]: ...
    @staticmethod
    def GetBatchFileFilter(includeXml: bool) -> str: ...
    @staticmethod
    def GetBatchFilePath(batchFolder: str, batchFile: str) -> str: ...
    @staticmethod
    def GetResultsFolder(batchFolder: str) -> str: ...
    @overload
    @staticmethod
    def GetFullPathName(path: str) -> str: ...
    @overload
    @staticmethod
    def GetFullPathName(assembly: System.Reflection.Assembly, path: str) -> str: ...
    @overload
    @staticmethod
    def GetFullPathName(basePath: str, path: str) -> str: ...

class HelpUtils:  # Class
    def __init__(self) -> None: ...

    Browse_the_acquisition_method: str  # static # readonly
    Compounds_at_a_Glance_Graphic_Settings_window: str  # static # readonly
    Compounds_at_a_Glance_Manual_Integrate_window1: str  # static # readonly
    HelpRoot: str  # static # readonly
    Method_Error_List_Window: str  # static # readonly
    Overview_Batch_Table_Window: str  # static # readonly
    Overview_Calibration_Curve_Window: str  # static # readonly
    Overview_Compound_Information_Window: str  # static # readonly
    Overview_Compounds_at_a_Glance_Window: str  # static # readonly
    Overview_Method_Tasks_Window: str  # static # readonly
    Overview_Sample_Information_Window: str  # static # readonly
    Overview_Task_Queue_Viewer: str  # static # readonly
    add_or_remove_table_columns: str  # static # readonly
    add_samples_dialog_box: str  # static # readonly
    auto_review_dialog_box: str  # static # readonly
    enter_filter_criteria_dialog_box: str  # static # readonly
    integration_setup_dialog_box: str  # static # readonly
    outliers_dialog_box: str  # static # readonly
    print_preview_dialog_box: str  # static # readonly
    sample_type_dialog_box: str  # static # readonly
    user_validation_and_reason_dialog_box: str  # static # readonly
    welcome: str  # static # readonly

    @overload
    @staticmethod
    def GetSubFolder(isWpf: bool) -> str: ...
    @overload
    @staticmethod
    def GetSubFolder() -> str: ...
    @overload
    @staticmethod
    def ShowQuantHtmlHelp(isWpf: bool, htmlfile: str, topic: str) -> bool: ...
    @overload
    @staticmethod
    def ShowQuantHtmlHelp(htmlfile: str) -> bool: ...
    @staticmethod
    def GuessIsWpf() -> bool: ...

class Localize:  # Class
    @staticmethod
    def LocalizeUltraPrintPreview() -> None: ...
    @staticmethod
    def LocalizeXamDockManager() -> None: ...
    @staticmethod
    def LocalizeUltraGrid() -> None: ...
    @staticmethod
    def LocalizeUltraDockManager() -> None: ...
    @staticmethod
    def LocalizeXamRibbon() -> None: ...
    @staticmethod
    def LocalizeUltraMisc() -> None: ...

class LogfileTraceListener(
    System.IDisposable, System.Diagnostics.TextWriterTraceListener
):  # Class
    def __init__(self, file: str, name: str) -> None: ...

    MAX_LOG_SIZE: int = ...  # static # readonly
    MEGABYTE: int = ...  # static # readonly

    ActiveInstance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.LogfileTraceListener
    )  # static # readonly
    Name: str
    PathName: str  # readonly

    @overload
    @staticmethod
    def Initialize(
        logfileFolderName: str,
        logfilePrefix: str,
        traceName: str,
        throwExceptionOnError: bool,
        args: List[str],
    ) -> bool: ...
    @overload
    @staticmethod
    def Initialize(
        logfilePath: str, traceName: str, throwExceptionOnError: bool, args: List[str]
    ) -> bool: ...
    def WriteLine(self, message: str) -> None: ...
    @staticmethod
    def Cleanup(traceName: str) -> None: ...
    @staticmethod
    def ShowLogFolder() -> None: ...
    def DumpCompressedFile(self) -> str: ...
    @staticmethod
    def GetLogfilePath(logfileFolderName: str, filenamePrefix: str) -> str: ...
    @staticmethod
    def ShowCurrentLog() -> None: ...

class MolStructureViewer(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    IsValid: bool  # readonly

    def Initialize(self) -> bool: ...
    def CreateMetafile(
        self,
        graphics: System.Drawing.Graphics,
        moldata: str,
        rect: System.Drawing.Rectangle,
        stream: System.IO.Stream,
    ) -> System.Drawing.Imaging.Metafile: ...
    def DrawStructure(
        self, graphics: System.Drawing.Graphics, moldata: str
    ) -> None: ...
    def Draw(
        self,
        graphics: System.Drawing.Graphics,
        moldata: str,
        color: System.Drawing.Color,
        rect: System.Drawing.Rectangle,
    ) -> None: ...
    def Dispose(self) -> None: ...

class NewBatchHelper(System.IDisposable):  # Class
    @overload
    @staticmethod
    def Do(uiState: IUIState) -> bool: ...
    @overload
    @staticmethod
    def Do(
        uiState: IUIState,
        batchFolder: str,
        batchFile: str,
        auditTrail: bool,
        askSave: bool,
    ) -> bool: ...
    def Dispose(self) -> None: ...

class NumericFormat(INumericFormat):  # Class
    def __init__(
        self, instrumentType: InstrumentType, formats: NumberFormats
    ) -> None: ...

class OpenBatchHelper(System.IDisposable):  # Class
    @overload
    @staticmethod
    def Do(uiState: IUIState) -> bool: ...
    @overload
    @staticmethod
    def Do(uiState: IUIState, batchFolder: str, batchFile: str) -> bool: ...
    @overload
    @staticmethod
    def Do(
        uiState: IUIState, batchFolder: str, batchFile: str, readOnly: bool
    ) -> bool: ...
    @overload
    @staticmethod
    def Do(
        uiState: IUIState,
        batchFolder: str,
        batchFile: str,
        revisionNumber: str,
        readOnly: bool,
    ) -> bool: ...
    def Dispose(self) -> None: ...

class PeakInfo:  # Class
    def __init__(
        self,
        compound: QuantitationDataSet.TargetCompoundRow,
        peak: QuantitationDataSet.PeakRow,
        tic: Agilent.MassSpectrometry.DataAnalysis.IFXData,
    ) -> None: ...

    Area: Optional[float]  # readonly
    CalculatedConcentration: Optional[float]  # readonly
    CompoundGroup: str  # readonly
    CompoundName: str  # readonly
    ConcentrationUnits: str  # readonly
    End: Optional[float]  # readonly
    ExpectedRetentionTime: Optional[float]  # readonly
    FinalConcentration: Optional[float]  # readonly
    Height: Optional[float]  # readonly
    IsSpectralSummer: bool  # readonly
    ManuallyIntegrated: bool  # readonly
    MaxY: Optional[float]  # readonly
    QValueComputed: Optional[int]  # readonly
    RetentionTime: Optional[float]  # readonly
    SignalToNoise: Optional[float]  # readonly
    Start: Optional[float]  # readonly
    TargetResponse: Optional[float]  # readonly
    Y: Optional[float]  # readonly

class PlotPageSettings:  # Class
    def __init__(self) -> None: ...

    Height: float
    MarginBottom: float
    MarginLeft: float
    MarginRight: float
    MarginTop: float
    Scale: float
    Width: float
    Zoom: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintPlotZoomType

    def GetConfigurationString(self) -> str: ...
    def LoadConfiguration(self, str: str) -> None: ...
    def ShowPageSetupDialog(
        self,
        control: System.Windows.Forms.Control,
        settings: System.Drawing.Printing.PrinterSettings,
        isMetric: bool,
    ) -> bool: ...
    @staticmethod
    def ToDialogUnit(inch: float, isMetric: bool) -> int: ...
    @staticmethod
    def FromDialogUnit(val: int, isMetric: bool) -> float: ...
    @staticmethod
    def LoadConfigurationString(
        str: str,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PlotPageSettings
    ): ...
    def DoDefault(self) -> None: ...

class PlotPrintDocument(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDocument,
    System.ComponentModel.IComponent,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        plot: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        printerSettings: System.Drawing.Printing.PrinterSettings,
        pageSettings: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PlotPageSettings,
        preview: bool,
    ) -> None: ...

    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly

class PlotUtils:  # Class
    @staticmethod
    def ConstructChromatogramTitle(
        formats: INumericFormat,
        srow: QuantitationDataSet.BatchRow,
        crow: QuantitationDataSet.TargetCompoundRow,
        backgroundSubtracted: bool,
        psext: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom,
        fxdata: Agilent.MassSpectrometry.DataAnalysis.IFXData,
        elements: List[PlotTitleElement],
    ) -> str: ...
    @staticmethod
    def PutEnhMetafileOnClipboard(
        hWnd: System.IntPtr, mf: System.Drawing.Imaging.Metafile
    ) -> bool: ...
    @staticmethod
    def PutPaneImageOnClipboard(
        panes: List[Agilent.MassSpectrometry.GUI.Plot.Pane],
        dataobj: System.Windows.Forms.DataObject,
    ) -> None: ...
    @overload
    @staticmethod
    def GeneratePeakLabel(
        builder: System.Text.StringBuilder,
        info: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PeakInfo,
        types: List[ChromatogramPeakLabelType],
        instrumentType: InstrumentType,
        formats: Agilent.MassHunter.Quantitative.UIModel.INumberFormats,
        peakLabelCaption: bool,
        peakLabelUnits: bool,
    ) -> None: ...
    @overload
    @staticmethod
    def GeneratePeakLabel(
        builder: System.Text.StringBuilder,
        types: List[ChromatogramPeakLabelType],
        format: str,
        instrumentType: InstrumentType,
        formats: Agilent.MassHunter.Quantitative.UIModel.INumberFormats,
        area: Optional[float],
        compoundName: str,
        height: Optional[float],
        retentionTime: Optional[float],
        expectedRetentionTime: Optional[float],
        calculatedConcentration: Optional[float],
        finalConcentration: Optional[float],
        signalToNoise: Optional[float],
        showLabelUnits: bool,
        concentrationUnit: str,
        retentionTimeUnit: str,
        manualIntegrated: Optional[bool],
        compoundGroup: str,
        qValueComputed: Optional[int],
    ) -> None: ...
    @staticmethod
    def SetPaneExtents(
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        graphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
    ) -> None: ...
    @staticmethod
    def GetQualifierAnnotation(
        qualifierResponseRatio: Optional[float],
        qualifierResponse: Optional[float],
        targetResponse: Optional[float],
        expectedRelativeResponse: Optional[float],
        qualifierRangeMin: Optional[float],
        qualifierRangeMax: Optional[float],
        instrumentType: InstrumentType,
        formats: Agilent.MassHunter.Quantitative.UIModel.INumberFormats,
        labelType: QualifierInfoLabelType,
    ) -> str: ...

class PrintDataGridViewDocument(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.Drawing.Printing.PrintDocument,
):  # Class
    def __init__(self, grid: System.Windows.Forms.DataGridView) -> None: ...

    CurrentPage: int  # readonly
    TotalPages: int  # readonly

    def PrintPage(
        self,
        e: System.Drawing.Printing.PrintPageEventArgs,
        marginY: int,
        printPageNumber: bool,
    ) -> None: ...
    def Clear(self) -> None: ...
    def InitPages(
        self,
        graphics: System.Drawing.Graphics,
        rect: System.Drawing.Rectangle,
        initialMargin: int,
    ) -> None: ...

class PrintDataGridViewUtil:  # Class
    @staticmethod
    def PrintPreview(
        grid: System.Windows.Forms.DataGridView,
        documentName: str,
        printerSettings: System.Drawing.Printing.PrinterSettings,
        pageSettings: System.Drawing.Printing.PageSettings,
    ) -> None: ...
    @staticmethod
    def Print(
        grid: System.Windows.Forms.DataGridView,
        displayDialogs: bool,
        documentName: str,
        printerSettings: System.Drawing.Printing.PrinterSettings,
        pageSettings: System.Drawing.Printing.PageSettings,
    ) -> None: ...

class PrintGraphicsDialogResult(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Apply: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDialogResult
    ) = ...  # static # readonly
    Cancel: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDialogResult
    ) = ...  # static # readonly
    Error: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDialogResult
    ) = ...  # static # readonly
    Print: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDialogResult
    ) = ...  # static # readonly

class PrintGraphicsDocument(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.Drawing.Printing.PrintDocument,
):  # Class
    def __init__(
        self,
        printerSettings: System.Drawing.Printing.PrinterSettings,
        pageSettings: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PlotPageSettings,
        preview: bool,
    ) -> None: ...

    PageRangeCount: int
    PageSettings: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PlotPageSettings
    )  # readonly
    Preview: bool  # readonly

    def PageTo(self, i: int) -> int: ...
    def GetNumPages(self) -> int: ...
    def PageFrom(self, i: int) -> int: ...
    def SetPageTo(self, i: int, page: int) -> None: ...
    def ShowPrintDialog(
        self, isMetric: bool
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDialogResult
    ): ...
    @staticmethod
    def GetRealMarginBounds(
        marginBounds: System.Drawing.RectangleF, g: System.Drawing.Graphics
    ) -> System.Drawing.RectangleF: ...
    def SetPageFrom(self, i: int, page: int) -> None: ...

class PrintPlotZoomType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AdjustTo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintPlotZoomType
    ) = ...  # static # readonly
    FitTo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintPlotZoomType
    ) = ...  # static # readonly
    FitToSheet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintPlotZoomType
    ) = ...  # static # readonly
    FitToSheetWidth: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintPlotZoomType
    ) = ...  # static # readonly

class PrintUtils:  # Class
    PageSettings: System.Drawing.Printing.PageSettings  # static # readonly
    PrinterSettings: System.Drawing.Printing.PrinterSettings  # static # readonly

    @staticmethod
    def PrintPreviewGrid(grid: Infragistics.Win.UltraWinGrid.UltraGrid) -> None: ...
    @overload
    @staticmethod
    def PrintPreviewPlot(
        document: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PlotPrintDocument,
        isMetric: bool,
    ) -> None: ...
    @overload
    @staticmethod
    def PrintPreviewPlot(
        document: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDocument,
        parent: System.Windows.Forms.Control,
        isMetric: bool,
    ) -> None: ...
    @staticmethod
    def PrintGrid(
        displayDialog: bool, grid: Infragistics.Win.UltraWinGrid.UltraGrid
    ) -> None: ...
    @staticmethod
    def PrintFile(path: str, printer: str) -> None: ...
    @staticmethod
    def PageSetup(
        parent: System.Windows.Forms.IWin32Window,
        pageSettings: System.Drawing.Printing.PageSettings,
        printerSettings: System.Drawing.Printing.PrinterSettings,
    ) -> System.Windows.Forms.DialogResult: ...
    @staticmethod
    def PrintPreview(
        document: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDocument,
        parent: System.Windows.Forms.Control,
        isMetric: bool,
    ) -> None: ...
    @staticmethod
    def PrintPDF(path: str, printer: str) -> bool: ...
    @staticmethod
    def PrintPlot(
        document: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDocument,
        showDialog: bool,
        isMetric: bool,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDialogResult
    ): ...

    # Nested Types

    class PrintPreviewDialog(
        Infragistics.Win.Printing.UltraPrintPreviewDialog,
        System.Windows.Forms.Layout.IArrangedElement,
        System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
        System.Windows.Forms.IContainerControl,
        System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
        System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
        System.Windows.Forms.IBindableComponent,
        System.Windows.Forms.IDropTarget,
        System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
        Infragistics.Shared.IUltraLicensedComponent,
        System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
        System.Windows.Forms.UnsafeNativeMethods.IOleControl,
        System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
        System.Windows.Forms.IWin32Window,
        System.ComponentModel.IComponent,
        System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
        System.Windows.Forms.UnsafeNativeMethods.IPersist,
        System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
        System.Windows.Forms.ISupportOleDropSource,
        System.Windows.Forms.UnsafeNativeMethods.IOleObject,
        System.Windows.Forms.UnsafeNativeMethods.IViewObject,
        System.IDisposable,
        System.ComponentModel.ISynchronizeInvoke,
    ):  # Class
        def __init__(self) -> None: ...

        PrintAfter: bool

    class RECT:  # Struct
        Bottom: int
        Left: int
        Right: int
        Top: int

class ReportUtils:  # Class
    @staticmethod
    def SetupContext(
        context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext,
        compliance: ICompliance,
    ) -> None: ...

class SaveBatchAsHelper(System.IDisposable):  # Class
    @overload
    @staticmethod
    def Do(uiState: IUIState) -> bool: ...
    @overload
    @staticmethod
    def Do(uiState: IUIState, batchFolder: str, batchFile: str) -> bool: ...
    def Dispose(self) -> None: ...

class SaveCloseBatchHelper(System.IDisposable):  # Class
    @staticmethod
    def Close(uiState: IUIState) -> bool: ...
    @staticmethod
    def AskSaveClose(uiState: IUIState) -> bool: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def AskSave(uiState: IUIState) -> bool: ...
    @staticmethod
    def Save(uiState: IUIState) -> bool: ...

class SaveExitMethodHelper(System.IDisposable):  # Class
    @staticmethod
    def AskSaveExit(uiState: IUIState) -> bool: ...
    @staticmethod
    def AskMethodFilePath(uiState: IUIState) -> str: ...
    @staticmethod
    def Validate(uiState: IUIState, canContinueWithValidateError: bool) -> bool: ...
    @staticmethod
    def AskSaveClose(uiState: IUIState) -> bool: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def AskSave(uiState: IUIState) -> bool: ...
    @staticmethod
    def Exit(uiState: IUIState) -> bool: ...

class ScriptControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    Agilent.MassHunter.Quantitative.UIModel.IScriptPane,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.IWin32Window,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
):  # Class
    def __init__(self) -> None: ...

    CanCopy: bool  # readonly
    CanPaste: bool  # readonly

    def Initialize(self, engine: IScriptEngine) -> None: ...
    def Copy(self) -> None: ...
    def Clear(self) -> None: ...
    def Paste(self) -> None: ...
    def Run(self) -> None: ...

class ScriptFile(System.IDisposable):  # Class
    def __init__(self, path: str) -> None: ...

    Description: str  # readonly
    Language: str  # readonly
    Name: str  # readonly
    PathName: str  # readonly

    def GetReferences(self) -> List[str]: ...
    def GetCompliance(self) -> List[str]: ...
    def GetImports(self) -> List[str]: ...
    def IsComplianceSupported(self, compliance: str) -> bool: ...
    @overload
    @staticmethod
    def ParseOptions() -> None: ...
    @overload
    @staticmethod
    def ParseOptions(
        path: str,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.ScriptFile: ...
    @overload
    @staticmethod
    def ParseOptions(
        reader: System.IO.TextReader,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.ScriptFile: ...
    def Dispose(self) -> None: ...

class ScriptFileCollection(
    Iterable[Any],
    System.IDisposable,
    Iterable[Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.ScriptFile],
):  # Class
    def __init__(self, scriptDir: str) -> None: ...

    Count: int  # readonly
    Extension: str  # static # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.ScriptFile: ...
    def Initialize(self) -> None: ...
    def Dispose(self) -> None: ...

class ScriptToolHandler(IScriptToolHandler, IToolHandler):  # Class
    @overload
    def __init__(
        self, scope: IScriptScope, module: str, state: str, execute: str
    ) -> None: ...
    @overload
    def __init__(self) -> None: ...

    ExecuteExpression: str
    Module: str
    Scope: IScriptScope  # readonly
    SetStateExpression: str

    def Execute(self, toolState: IToolState, objUiState: Any) -> None: ...
    def SetState(self, toolState: IToolState, objUiState: Any) -> None: ...

class ScriptUtils:  # Class
    @staticmethod
    def InitScript(
        nameSpace: str,
        className: str,
        commandAssemblies: List[System.Reflection.Assembly],
        referenceAssemblies: List[str],
    ) -> System.Reflection.Assembly: ...

class SelectedMzMarker(Agilent.MassSpectrometry.GUI.Plot.Marker):  # Class
    def __init__(
        self,
        size: int,
        lineColor: System.Drawing.Color,
        fillColor: System.Drawing.Color,
    ) -> None: ...
    def Draw(self, plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane) -> None: ...

class ShowWaitCursor(System.IDisposable):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, parent: System.Windows.Forms.IWin32Window) -> None: ...
    @overload
    def __init__(self, ctrl: System.Windows.Forms.Control) -> None: ...
    def Dispose(self) -> None: ...

class SpectrumTransfer(
    Agilent.MassHunter.Quantitative.UIModel.ISpectrumTransfer
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, spectrum: Agilent.MassSpectrometry.DataAnalysis.ISpectrum
    ) -> None: ...
    @overload
    def __init__(
        self, component: Agilent.MassSpectrometry.DataAnalysis.Component, title: str
    ) -> None: ...
    @overload
    def __init__(
        self, xvalues: List[float], yvalues: List[float], title: str
    ) -> None: ...
    @overload
    def __init__(
        self,
        library: Agilent.MassSpectrometry.DataAnalysis.INistLibrarySearch,
        specid: Agilent.MassSpectrometry.DataAnalysis.ISpectrumId,
    ) -> None: ...
    @overload
    def __init__(
        self,
        transfer: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.SpectrumTransfer,
    ) -> None: ...

    AcquiredMassRangeMinimum: Optional[float]
    ChromatographyType: Optional[ChromatographyType]
    CollisionEnergy: Optional[float]
    Count: int  # readonly
    InstrumentType: str
    IonPolarity: Optional[Agilent.MassSpectrometry.DataAnalysis.IonPolarity]
    IonizationEnergy: Optional[float]
    IonizationMode: Optional[Agilent.MassSpectrometry.DataAnalysis.IonizationMode]
    IsAccurateMass: bool
    Origin: str
    Owner: str
    PeakCount: int  # readonly
    RetentionTime: Optional[float]
    SampleId: str
    ScanType: Optional[Agilent.MassSpectrometry.DataAnalysis.MSScanType]
    SelectedMz: Optional[float]
    SignalToNoise: Optional[float]
    Title: str
    XValues: List[float]  # readonly
    YValues: List[float]  # readonly

    def GetPeakY(self, index: int) -> float: ...
    def GetMaxX(self) -> Optional[float]: ...
    def Normalize(self, max: float) -> None: ...
    def GetX(self, index: int) -> float: ...
    def GetY(self, index: int) -> float: ...
    def GetBasePeak(self, x: Optional[float], y: Optional[float]) -> None: ...
    def GetMinX(self) -> Optional[float]: ...
    def Clone(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.SpectrumTransfer
    ): ...
    def GetPeakX(self, index: int) -> float: ...

class SpectrumUtils:  # Class
    @staticmethod
    def SynthesizeSpectrum(
        informula: str, speciesFormula: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.SpectrumTransfer
    ): ...
    @staticmethod
    def ValidateSpecies(species: str) -> None: ...
    @staticmethod
    def GetDefaultAvailableSpecies() -> List[str]: ...
    @staticmethod
    def GetDefaultUsedSpecies() -> List[str]: ...

class UIException(
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

class UnhandledExceptionHandler:  # Class
    QuantAppId: int  # static # readonly

    @staticmethod
    def Cleanup() -> None: ...
    @staticmethod
    def HandleConsoleException(e: System.Exception) -> None: ...
    @overload
    @staticmethod
    def Setup(
        enableErrorReporting: bool,
        appId: int,
        appName: str,
        emailAddress: str,
        dumpLogOnNormalExit: bool,
        windowsApplication: bool,
    ) -> None: ...
    @overload
    @staticmethod
    def Setup(
        enableErrorReporting: bool,
        appId: int,
        appName: str,
        titleAppName: str,
        emailAddress: str,
        dumpLogOnNormalExit: bool,
        windowsApplication: bool,
    ) -> None: ...

class Utilities:  # Class
    HelpDataSetFilePath: str  # static # readonly

    @staticmethod
    def VerifyUserForTimeout(
        compliance: ICompliance, mainWindowHandle: System.IntPtr
    ) -> bool: ...
    @staticmethod
    def ShowExceptionMessage(
        parent: System.Windows.Forms.IWin32Window, ex: System.Exception
    ) -> None: ...
    @staticmethod
    def IsPaneVisible(control: System.Windows.Forms.Control) -> bool: ...
    @staticmethod
    def GetAssemblyAttribute(assembly: System.Reflection.Assembly) -> T: ...
    @staticmethod
    def ShowHelpQuantitationDataSet(
        parent: System.Windows.Forms.IWin32Window,
    ) -> None: ...
    @staticmethod
    def SplitMSScanTypes(
        scanTypes: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    @staticmethod
    def GetUnitStringForAxis(
        unit: Agilent.MassSpectrometry.DataAnalysis.DataUnit,
    ) -> str: ...
    @staticmethod
    def DisplayConsoleCopyright(
        asm: System.Reflection.Assembly,
        productRevision: str,
        patchNumber: str,
        writer: System.IO.TextWriter,
    ) -> None: ...
    @staticmethod
    def InitPlotPreferences(
        data: Agilent.MassSpectrometry.DataAnalysis.IFXData,
        prefs: Agilent.MassSpectrometry.DataAnalysis.IPlotPreferences,
    ) -> None: ...
    @staticmethod
    def GetHelpFilePath(filename: str) -> str: ...
    @staticmethod
    def GetParent(mainWindowHandle: System.IntPtr) -> System.IntPtr: ...
    @staticmethod
    def GetApplicationDisplayName(application: str) -> str: ...
    @staticmethod
    def CheckBeingAcquired(dir: str) -> None: ...
    @staticmethod
    def RegisterProduct(parent: System.IntPtr) -> None: ...
    @staticmethod
    def FindKnownExceptions(
        e: System.Exception, knownTypes: List[System.Type]
    ) -> List[System.Exception]: ...
    @staticmethod
    def GetInstrumentTypeDisplayName(instrument: InstrumentType) -> str: ...
    @staticmethod
    def ShowProfile3DBrowser(samplePath: str, mz: float, rt: float) -> None: ...
    @staticmethod
    def GetSubAppDisplayText(
        instrumentType: InstrumentType, application: str, compliance: ICompliance
    ) -> str: ...
    @staticmethod
    def SetLeaseTimeZero() -> None: ...
    @staticmethod
    def ShowUsage(
        parent: System.Windows.Forms.IWin32Window,
        cmdlineType: System.Type,
        rmgr: System.Resources.ResourceManager,
        predesc: str,
        title: str,
        icon: System.Drawing.Icon,
    ) -> None: ...
    @staticmethod
    def IsModal(window: System.Windows.Window) -> bool: ...
    @staticmethod
    def IntegrateSpectrum(
        spectrum: Agilent.MassSpectrometry.DataAnalysis.ISpectrum,
        heightAbsThreshold: float,
        heightPctThreshold: float,
    ) -> Agilent.MassSpectrometry.DataAnalysis.IPeakList: ...
    @staticmethod
    def IsKnownException(
        e: System.Exception, knownTypes: List[System.Type]
    ) -> bool: ...
    @overload
    @staticmethod
    def ShowMessage(
        parent: System.Windows.Forms.IWin32Window,
        message: str,
        title: str,
        buttons: System.Windows.Forms.MessageBoxButtons,
        icon: System.Windows.Forms.MessageBoxIcon,
    ) -> System.Windows.Forms.DialogResult: ...
    @overload
    @staticmethod
    def ShowMessage(
        parent: System.Windows.Forms.IWin32Window,
        message: str,
        title: str,
        buttons: System.Windows.Forms.MessageBoxButtons,
        icon: System.Windows.Forms.MessageBoxIcon,
        helpId: int,
    ) -> System.Windows.Forms.DialogResult: ...
