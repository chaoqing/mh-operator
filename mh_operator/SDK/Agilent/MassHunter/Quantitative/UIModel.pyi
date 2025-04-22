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

# Stubs for namespace: Agilent.MassHunter.Quantitative.UIModel

class CompoundGroupFilterInfo(
    System.IComparable[Agilent.MassHunter.Quantitative.UIModel.CompoundGroupFilterInfo]
):  # Struct
    def __init__(
        self,
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundFilterType,
        compoundGroup: str,
    ) -> None: ...

    CompoundGroup: str
    Type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundFilterType

    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(
        self, info: Agilent.MassHunter.Quantitative.UIModel.CompoundGroupFilterInfo
    ) -> bool: ...
    @overload
    def Matches(
        self, key: Agilent.MassHunter.Quantitative.UIModel.CompoundKey
    ) -> bool: ...
    @overload
    def Matches(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow,
    ) -> bool: ...
    def GetHashCode(self) -> int: ...
    def CompareTo(
        self, other: Agilent.MassHunter.Quantitative.UIModel.CompoundGroupFilterInfo
    ) -> int: ...
    def ToString(self) -> str: ...

class CompoundKey(
    System.IComparable[Agilent.MassHunter.Quantitative.UIModel.CompoundKey]
):  # Struct
    def __init__(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow,
    ) -> None: ...

    CompoundGroup: str  # readonly
    CompoundId: int  # readonly
    CompoundName: str  # readonly
    Empty: Agilent.MassHunter.Quantitative.UIModel.CompoundKey  # static # readonly
    ID: Optional[int]  # readonly
    IstdCompoundId: Optional[int]  # readonly
    IstdRetentionTime: Optional[float]  # readonly
    Mz: Optional[float]  # readonly
    RetentionTime: Optional[float]  # readonly
    SelectedMz: Optional[float]  # readonly
    TimeSegment: Optional[int]  # readonly
    UserDefined: str  # readonly

    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(
        self, ck: Agilent.MassHunter.Quantitative.UIModel.CompoundKey
    ) -> bool: ...
    def Matches(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow,
    ) -> bool: ...
    @staticmethod
    def Compare(
        k1: Agilent.MassHunter.Quantitative.UIModel.CompoundKey,
        k2: Agilent.MassHunter.Quantitative.UIModel.CompoundKey,
    ) -> int: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...

class ICagWindow(System.Windows.Forms.IWin32Window):  # Interface
    ContainsFocus: bool  # readonly
    DataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator  # readonly
    Height: int
    IsHandleCreated: bool  # readonly
    Location: System.Drawing.Point
    PresentationState: (
        Agilent.MassHunter.Quantitative.UIModel.IPresentationState
    )  # readonly
    ToolbarsManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager
    )  # readonly
    Visible: bool  # readonly
    Width: int
    WindowState: System.Windows.Forms.FormWindowState

    def Show(self) -> None: ...
    def ShowHelpContents(self) -> None: ...
    def ShowHelpSearch(self) -> None: ...
    def GetAddInManager(self) -> T: ...
    def ShowSetupGraphicsDialog(self) -> None: ...
    def ShowHelpIndex(self) -> None: ...
    def GetSelectedCompounds(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TargetCompoundRowId
    ]: ...
    def GetSelectedSamples(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleRowId]: ...
    def GetChromatogramControl(self) -> T: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def SetCurrentLayoutAsDefault(self) -> None: ...
    def Close(self) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def Activate(self) -> None: ...
    def GetSetupGraphicsContext(self) -> T: ...
    def GetToolbar(
        self, paneId: str, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbar: ...
    def Invoke(self, d: System.Delegate, parameters: List[Any]) -> Any: ...
    def LoadDefaultLayout(self, loadAllSamplesCompounds: bool) -> bool: ...

    Disposed: System.EventHandler  # Event

class ICalCurvePane(System.Windows.Forms.IWin32Window):  # Interface
    AutoScale: bool
    CanAcceptAssistantCurve: bool  # readonly
    CanAutoScale: bool  # readonly
    CanCopy: bool  # readonly
    CurveFitAssistantConfidenceBandVisible: bool
    CurveFitAssistantTable: (
        Agilent.MassHunter.Quantitative.UIModel.IGridControl
    )  # readonly
    CurveFitAssistantVisible: bool  # readonly
    IsLogScaleX: bool
    IsLogScaleY: bool
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    RelativeConcentration: bool
    ShowCC: bool
    ShowIstdResponses: bool
    ShowQC: bool
    ShowStandardDeviationBars: bool

    def AcceptAssistantCurve(self) -> None: ...
    def AutoScaleY(self) -> None: ...
    def Copy(self) -> None: ...
    def AutoScaleX(self) -> None: ...
    def StoreSettings(self) -> None: ...
    def CreatePropertyPages(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage
    ]: ...
    def HideCurveFitAssistant(self) -> None: ...
    def FitToLevels(self, levelNames: Iterable[str], includesOrigin: bool) -> None: ...
    def ShowCurveFitAssistant(self) -> None: ...

class ICalibrationAtAGlanceWindow(System.Windows.Forms.IWin32Window):  # Interface
    ContainsFocus: bool  # readonly
    Height: int
    Location: System.Drawing.Point
    NumColumnsPerPage: int  # readonly
    NumRowsPerPage: int  # readonly
    Visible: bool  # readonly
    Width: int
    WindowState: System.Windows.Forms.FormWindowState

    def GetSelectedTargetCompounds(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TargetCompoundRowId
    ]: ...
    def Close(self) -> None: ...
    def Show(self) -> None: ...
    def SetDimension(self, rows: int, columns: int) -> None: ...
    def Activate(self) -> None: ...

    Closed: System.EventHandler  # Event

class IChromSpecPane(System.Windows.Forms.IWin32Window):  # Interface
    AutoScale: bool
    CanAutoScale: bool  # readonly
    CanClearManualIntegration: bool  # readonly
    CanCopy: bool  # readonly
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
    ManualIntegrationMode: bool  # readonly
    ManualScaleY: bool  # readonly
    NormalizeQualifiers: bool
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    Properties: Agilent.MassHunter.Quantitative.UIModel.IChromSpecProperties  # readonly
    SelectedCompoundId: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TargetCompoundRowId
    )  # readonly
    SelectedQualifierId: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TargetQualifierRowId
    )  # readonly
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

    def GetActiveObject(self) -> T: ...
    def AutoScaleY(self) -> None: ...
    def RestoreIntegrationSetup(self) -> None: ...
    def SetManualScaleY(self, miny: float, maxy: float) -> None: ...
    def Copy(self) -> None: ...
    def SearchLibrary(
        self, app: Agilent.MassHunter.Quantitative.UIModel.ILibraryApp
    ) -> None: ...
    def ShowWiderRTRange(self) -> None: ...
    def EnterManualIntegration(self) -> None: ...
    def AutoScaleX(self) -> None: ...
    def ExitManualIntegration(self) -> None: ...
    def ResetRTRange(self) -> None: ...
    def ClearManualIntegration(self) -> None: ...
    def StoreSettings(self) -> None: ...
    def CreatePropertyPages(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage
    ]: ...
    def ZeroPeak(self) -> None: ...
    def GetActivePaneScale(
        self, minx: float, maxx: float, miny: float, maxy: float
    ) -> bool: ...
    def ShowIntegrationSetupDialog(self) -> None: ...
    def ShowPeakLabelsDialog(self) -> None: ...

class IChromSpecProperties(object):  # Interface
    ShowBaselines: bool
    ShowOriginalBaselines: bool

    def InitFromConfiguration(self) -> None: ...
    def GetPeakFillColor(
        self,
        isPrimary: bool,
        isManualIntegrated: bool,
        peakStatus: Agilent.MassSpectrometry.DataAnalysis.PeakStatus,
        fillPeakTransparency: int,
        fillAlternatePeaks: bool,
    ) -> System.Drawing.Color: ...

class IChromatogramInformationGridView(object):  # Interface
    def SelectAll(self) -> None: ...

class IChromatogramInformationItem(object):  # Interface
    BatchID: int  # readonly
    Color: System.Drawing.Color
    DataFileName: str  # readonly
    InstrumentName: str  # readonly
    MSScanType: Optional[Agilent.MassSpectrometry.DataAnalysis.MSScanType]  # readonly
    SampleID: int  # readonly
    SampleName: str  # readonly
    Signal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Signal  # readonly

class IChromatogramInformationUIContext(object):  # Interface
    Items: List[
        Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationItem
    ]  # readonly
    VisibleItemCount: int  # readonly

    def OnItemColorChanged(self, e: System.EventArgs) -> None: ...
    def IsVisible(
        self, item: Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationItem
    ) -> bool: ...
    def SetVisible(
        self,
        items: List[
            Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationItem
        ],
        visible: bool,
    ) -> None: ...

class IChromatogramInformationView(object):  # Interface
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly

    def UpdateHighlight(self) -> None: ...
    def UpdatePeaks(self) -> None: ...

class IChromatogramInformationWindow(System.Windows.Forms.IWin32Window):  # Interface
    ChromView: (
        Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationView
    )  # readonly
    ContainsFocus: bool  # readonly
    GridView: (
        Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationGridView
    )  # readonly
    HeadToTail: bool
    Height: int
    InvokeRequired: bool  # readonly
    IsHandleCreated: bool  # readonly
    LinkXAxes: bool
    LinkYAxes: bool
    Location: System.Drawing.Point
    MaxNumVisibleRows: int
    Overlay: bool
    ToolbarsManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager
    )  # readonly
    UIContext: (
        Agilent.MassHunter.Quantitative.UIModel.IChromatogramInformationUIContext
    )  # readonly
    Visible: bool  # readonly
    Width: int
    WindowState: System.Windows.Forms.FormWindowState

    def AutoScaleY(self) -> None: ...
    def CanAutoScale(self) -> bool: ...
    def Copy(self) -> None: ...
    def AutoScaleX(self) -> None: ...
    def CanCopy(self) -> bool: ...
    def Close(self) -> None: ...
    def CreatePropertyPages(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage
    ]: ...
    def AutoScaleXY(self) -> None: ...
    def Activate(self) -> None: ...
    def CanCreateCompound(self) -> bool: ...
    def CreateCompound(self) -> None: ...
    @overload
    def Invoke(self, d: System.Delegate) -> Any: ...
    @overload
    def Invoke(self, d: System.Delegate, parameters: List[Any]) -> Any: ...
    def Show(self) -> None: ...

    Disposed: System.EventHandler  # Event
    Initialized: System.EventHandler  # Event

class ICustomPane(object):  # Interface
    InitialLocation: System.Windows.Forms.AnchorStyles  # readonly
    Title: str  # readonly

    def GetControl(self) -> Any: ...

class IDataNavigator(object):  # Interface
    BatchId: int  # readonly
    CompoundGroupFilter: Agilent.MassHunter.Quantitative.UIModel.CompoundGroupFilterInfo
    CompoundId: int  # readonly
    CompoundKey: Agilent.MassHunter.Quantitative.UIModel.CompoundKey
    CompoundKeySortType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundKeySortType
    )
    CurrentCompoundRow: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    )  # readonly
    CurrentIstdRow: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    )  # readonly
    CurrentSampleRow: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.BatchRow
    )  # readonly
    HasIstd: bool  # readonly
    ISTDFilter: Agilent.MassHunter.Quantitative.UIModel.ISTDFilterInfo
    IsCompoundValid: bool  # readonly
    IsSampleValid: bool  # readonly
    IstdId: int  # readonly
    PresentationState: (
        Agilent.MassHunter.Quantitative.UIModel.IPresentationState
    )  # readonly
    SampleFileInformation: (
        Agilent.MassSpectrometry.DataAnalysis.IBDAFileInformation
    )  # readonly
    SampleId: int  # readonly
    TimeSegmentFilter: Agilent.MassHunter.Quantitative.UIModel.TimeSegmentFilterInfo

    def GetTimeSegmentFilters(
        self,
    ) -> List[Agilent.MassHunter.Quantitative.UIModel.TimeSegmentFilterInfo]: ...
    def GetSampleTic(self) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...
    def GetCompoundGroupFilters(
        self,
    ) -> List[Agilent.MassHunter.Quantitative.UIModel.CompoundGroupFilterInfo]: ...
    def GetChromatogram(
        self, pset: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...
    def NavigateSample(self, sampleId: int) -> None: ...
    def GetISTDFilters(
        self,
    ) -> List[Agilent.MassHunter.Quantitative.UIModel.ISTDFilterInfo]: ...
    def GetCompoundSpectrumForReferenceLibraryMatch(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.ISpectrum: ...
    def GetIstdSpectrum(self) -> Agilent.MassSpectrometry.DataAnalysis.ISpectrum: ...
    def GetFilteredCompoundKeys(
        self,
    ) -> List[Agilent.MassHunter.Quantitative.UIModel.CompoundKey]: ...
    def GetCompoundAndQualifierSpectrum(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum]: ...
    @overload
    def GetCompoundChromatogram(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...
    @overload
    def GetCompoundChromatogram(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow,
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...
    def GetIstdCompoundAndQualifierSpectrum(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.ISpectrum]: ...
    def GetQualifierChromatogram(
        self, compoundId: int, qualifierId: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...
    def GetTotalSignalChromatogram(
        self,
        min: float,
        max: float,
        signal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Signal,
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...
    @overload
    def GetCompoundSpectrum(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.ISpectrum: ...
    @overload
    def GetCompoundSpectrum(
        self,
        compoundId: int,
        mzranges: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.DoubleRange
        ],
        extractionRanges: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.DoubleRange
        ],
        startRT: float,
        endRT: float,
        pverrideSpectrum: bool,
    ) -> Agilent.MassSpectrometry.DataAnalysis.ISpectrum: ...
    def NavigateCompound(self, sampleId: int, compoundId: int) -> None: ...
    def GetIstdChromatogram(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...
    def GetTIC(
        self,
        msLevel: Agilent.MassSpectrometry.DataAnalysis.MSLevel,
        scanTypes: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        minRT: Optional[float],
        maxRT: Optional[float],
    ) -> Agilent.MassSpectrometry.DataAnalysis.IChromatogram: ...
    def GetReferenceLibrarySpectrum(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.ISpectrum: ...

    CompoundKeyChange: System.EventHandler  # Event
    NavigateChange: System.EventHandler[
        Agilent.MassHunter.Quantitative.UIModel.NavigateChangeEventArgs
    ]  # Event
    NavigateChanging: System.EventHandler[
        Agilent.MassHunter.Quantitative.UIModel.NavigateChangingEventArgs
    ]  # Event

class IDockManager(object):  # Interface
    ActivePane: Agilent.MassHunter.Quantitative.UIModel.IDockPane  # readonly

    def ControlPaneExists(self, paneId: str) -> bool: ...
    def GetPane(
        self, paneId: str
    ) -> Agilent.MassHunter.Quantitative.UIModel.IDockPane: ...

class IDockPane(object):  # Interface
    Control: System.Windows.Forms.Control  # readonly

class IEditMethodState(object):  # Interface
    CurrentCompoundId: int  # readonly
    CurrentLevelId: int  # readonly
    CurrentObjectIsCalibration: bool  # readonly
    CurrentObjectIsSample: bool  # readonly
    CurrentObjectIsTargetCompound: bool  # readonly
    CurrentObjectIsTargetQualifier: bool  # readonly
    CurrentQualifierId: int  # readonly
    IsDirty: bool  # readonly
    MethodFilePathName: str  # readonly
    OriginatedBatch: str  # readonly

    def NavigateQualifier(self, compoundId: int, qualifierId: int) -> None: ...
    def NavigateCalibration(self, compoundId: int, levelId: int) -> None: ...
    def GetTimeSegments(self) -> List[int]: ...
    def GetTargetCompoundRow(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    ): ...
    def NavigateCompound(self, compoundId: int) -> None: ...
    def GetIstdCompoundRow(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    ): ...

    NavigationChange: System.EventHandler  # Event

class IFlagFilter(object):  # Interface
    Category: str  # readonly
    ColumnName: str  # readonly
    Enabled: bool
    Name: str  # readonly
    OutlierCompoundType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.OutlierCompoundType
    )  # readonly
    OutlierValueColumnName: str  # readonly
    OutlierValueRelationName: str  # readonly
    RelationName: str  # readonly

    def Match(
        self,
        row: System.Data.DataRow,
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.OutlierFilterType,
        backColor: System.Drawing.Color,
        foreColor: System.Drawing.Color,
    ) -> bool: ...
    def Available(
        self,
        dataset: System.Data.DataSet,
        batchFiles: Agilent.MassSpectrometry.DataAnalysis.Quantitative.BatchFiles,
        batchId: int,
    ) -> bool: ...
    def GetMessage(self, row: System.Data.DataRow) -> str: ...

class IFlagFilterManager(object):  # Interface
    Count: int  # readonly
    Filter: bool
    FilterType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.OutlierFilterType
    Flag: bool
    def __getitem__(
        self, column: Agilent.MassSpectrometry.DataAnalysis.Quantitative.OutlierColumns
    ) -> Agilent.MassHunter.Quantitative.UIModel.IFlagFilter: ...
    def __getitem__(
        self, index: int
    ) -> Agilent.MassHunter.Quantitative.UIModel.IFlagFilter: ...
    def BeginEdit(self) -> None: ...
    def EndEdit(self) -> None: ...

class IGridControl(object):  # Interface
    CanCopy: bool  # readonly
    CanDelete: bool  # readonly
    CanExpandAll: bool  # readonly
    CanPaste: bool  # readonly
    CanPrint: bool  # readonly
    ContainsFocus: bool  # readonly
    Exporting: bool
    IsInEditMode: bool  # readonly
    LastRawBandName: str  # readonly
    LastRawColumnName: str  # readonly
    UltraGrid: Infragistics.Win.UltraWinGrid.UltraGrid  # readonly

    def CanUndoInEditMode(self) -> bool: ...
    def FormatColumn(self, rawBandName: str, rawColumnName: str) -> None: ...
    def Sort(self, rawBandName: str, rawColumnName: str, ascending: bool) -> None: ...
    def DisplayPrintPreview(self) -> None: ...
    def AutoFitColumns(self) -> None: ...
    def CollapseAll(self) -> None: ...
    def IsColumnFormattable(self, rawBandName: str, rawColumnName: str) -> bool: ...
    def GetColumnCaption(self, logicalBandName: str, logicalColumnName: str) -> str: ...
    def LoadColumnSettings(self, file: str) -> None: ...
    def GetLogicalColumnName(self, rawBandName: str, rawColumnName: str) -> str: ...
    def ShowColumn(
        self, logicalBandName: str, logicalColumnName: str, columnNameAfter: str
    ) -> None: ...
    def UndoInEditMode(self) -> None: ...
    def GetLogicalBandName(self, rawBandName: str, rawColumnName: str) -> str: ...
    def Copy(self) -> None: ...
    def ExpandAll(self) -> None: ...
    def SupportsSaveLoadColumnSettings(self) -> bool: ...
    def IsColumnVisible(self, logicalBandName: str, logicalColumnName: str) -> bool: ...
    def PageSetup(self) -> None: ...
    def SaveColumnSettings(self, file: str) -> None: ...
    def Print(self, displayDialog: bool) -> None: ...
    def GetColumnNames(self, logicalBandName: str) -> List[str]: ...
    def Delete(self) -> None: ...
    def ResetColumns(self) -> None: ...
    def ResetSort(self) -> None: ...
    def HideColumn(self, logicalBandName: str, logicalColumnName: str) -> None: ...
    def ShowColumnsDialog(self) -> None: ...
    def Paste(self) -> None: ...

class ILibraryApp(object):  # Interface
    HasLibrary: bool  # readonly
    TargetSpectrum: (
        Agilent.MassHunter.Quantitative.UIModel.ISpectrumTransfer
    )  # readonly

    def Search(self) -> None: ...
    def SetTargetSpectrum(
        self,
        spectrum: Agilent.MassHunter.Quantitative.UIModel.ISpectrumTransfer,
        massDisplayFormat: Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat,
    ) -> None: ...
    def ShowWindow(self) -> None: ...
    def SetLibraries(
        self,
        items: List[Agilent.MassHunter.Quantitative.UIModel.ILibraryItem],
        searchType: Agilent.MassSpectrometry.DataAnalysis.MultipleLibrarySearchType,
        unitMassFormat: Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat,
        accurateMassFormat: Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat,
    ) -> None: ...

class ILibraryAppSite(object):  # Interface
    LibraryApp: Agilent.MassHunter.Quantitative.UIModel.ILibraryApp  # readonly

class ILibraryItem(object):  # Interface
    Library: Agilent.MassSpectrometry.DataAnalysis.ILibrary  # readonly
    Parameters: Agilent.MassSpectrometry.DataAnalysis.LibrarySearchParams  # readonly

class IMainWindow(System.Windows.Forms.IWin32Window):  # Interface
    CalCurvePane: Agilent.MassHunter.Quantitative.UIModel.ICalCurvePane  # readonly
    ChromSpecPane: Agilent.MassHunter.Quantitative.UIModel.IChromSpecPane  # readonly
    CommandContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AppCommandContext
    )  # readonly
    ContainsFocus: bool  # readonly
    DataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator  # readonly
    DockManager: Agilent.MassHunter.Quantitative.UIModel.IDockManager  # readonly
    Height: int
    InvokeRequired: bool  # readonly
    IsDisposed: bool  # readonly
    IsHandleCreated: bool  # readonly
    Location: System.Drawing.Point
    MethodErrorListPane: (
        Agilent.MassHunter.Quantitative.UIModel.IMethodErrorListPane
    )  # readonly
    MethodTablePane: (
        Agilent.MassHunter.Quantitative.UIModel.IMethodTablePane
    )  # readonly
    MethodTasksPane: (
        Agilent.MassHunter.Quantitative.UIModel.IMethodTasksPane
    )  # readonly
    MetricsPlotPane: (
        Agilent.MassHunter.Quantitative.UIModel.IMetricsPlotPane
    )  # readonly
    PresentationState: (
        Agilent.MassHunter.Quantitative.UIModel.IPresentationState
    )  # readonly
    SampleDataPane: Agilent.MassHunter.Quantitative.UIModel.ISampleDataPane  # readonly
    ScriptPane: Agilent.MassHunter.Quantitative.UIModel.IScriptPane  # readonly
    StatusBar: Agilent.MassHunter.Quantitative.UIModel.IStatusBar  # readonly
    Text: str
    ToolbarsManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager
    )  # readonly
    Width: int
    WorktablePane: Agilent.MassHunter.Quantitative.UIModel.IWorktablePane  # readonly

    def RegisterCustomPane(
        self,
        register: bool,
        pane: str,
        control: Agilent.MassHunter.Quantitative.UIModel.ICustomPane,
    ) -> None: ...
    def ActivatePane(self, pane: str) -> None: ...
    def CustomPaneExists(self, key: str) -> bool: ...
    def ForceClose(self) -> None: ...
    def ResetLayout(self) -> None: ...
    def SetPaneVisible(self, pane: str, visible: bool) -> None: ...
    def ShowMethodErrorListPane(self) -> None: ...
    def IsInModalState(self) -> bool: ...
    def LayoutPanes(self, pattern: int) -> None: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def ValidateMethod(self, alwaysShowPane: bool) -> None: ...
    def Close(self) -> None: ...
    def MaximizePane(self, paneKey: str) -> None: ...
    def IsPaneVisible(self, pane: str) -> bool: ...
    def GetCustomPane(
        self, key: str
    ) -> Agilent.MassHunter.Quantitative.UIModel.ICustomPane: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def Activate(self) -> None: ...
    def ShowWindow(self) -> None: ...
    def ShowAboutBox(self) -> None: ...
    def Invoke(self, d: System.Delegate) -> Any: ...

    Closed: System.EventHandler  # Event

class IMethodErrorListPane(object):  # Interface
    def SetMessages(
        self,
        msgs: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodValidationMessage
        ],
    ) -> None: ...

class IMethodTablePane(object):  # Interface
    ArrangeCompoundsBy: str
    CalibrationsBandVisible: bool
    CanBrowseAcquisitionMethod: bool  # readonly
    CanDeleteRows: bool  # readonly
    CanFillDown: bool  # readonly
    CanGroupByTimeSegment: bool  # readonly
    CompoundsBandVisible: bool
    GridControl: Agilent.MassHunter.Quantitative.UIModel.IGridControl  # readonly
    GroupByTimeSegment: bool
    IsDisposed: bool  # readonly
    MethodEditTaskMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodEditTaskMode
    )
    OutlierSetup: Agilent.MassSpectrometry.DataAnalysis.Quantitative.OutlierColumns
    QualifiersBandVisible: bool
    TimeSegmentFilterInfo: Agilent.MassHunter.Quantitative.UIModel.TimeSegmentFilterInfo

    def GetSelectedCompoundIds(self) -> List[int]: ...
    def GetFilteredCompoundIds(self) -> List[int]: ...
    def CreatePropertyPages(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage
    ]: ...
    def DeleteRows(self) -> None: ...
    @overload
    def ActivateCell(self, columnName: str) -> None: ...
    @overload
    def ActivateCell(self, compoundId: int, columnnName: str) -> None: ...
    def GenerateStatusText(self) -> str: ...
    def FindNext(
        self,
        tableName: str,
        columnName: str,
        operatorType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType,
        value_: Any,
    ) -> bool: ...
    def BrowseAcquisitionMethod(self) -> None: ...
    def FillDown(self) -> None: ...

class IMethodTasksPane(object):  # Interface
    def GetGroup(
        self, id: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IExplorerBarGroup
    ): ...

class IMetricsPlotData(object):  # Interface
    AutoScale: bool
    NextColor: System.Drawing.Color  # readonly

    def AutoScaleY(self) -> None: ...
    def Clear(self) -> None: ...
    def AddSeries(self, column: str, color: System.Drawing.Color) -> None: ...
    def AutoScaleX(self) -> None: ...

class IMetricsPlotPane(object):  # Interface
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    PlottableGrid: Agilent.MassHunter.Quantitative.UIModel.IPlottableGrid  # readonly
    ShowAverageStdDevLines: bool

    def GetActivePaneData(
        self,
    ) -> Agilent.MassHunter.Quantitative.UIModel.IMetricsPlotData: ...

class INumberFormats(object):  # Interface
    def GetColumns(self) -> List[str]: ...
    def SetColumnNumberFormat(
        self,
        instrumentType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType,
        column: str,
        format: Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat,
    ) -> None: ...
    def GetColumnNumberFormat(
        self,
        instrumentType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType,
        name: str,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat: ...
    def Exists(
        self,
        instrumentType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType,
        name: str,
    ) -> bool: ...
    def GetColumnCategory(self, column: str) -> str: ...
    def StoreFormats(self) -> None: ...

class IPlottableColumn(object):  # Interface
    PropertyType: System.Type  # readonly
    Title: str  # readonly

    def GetValue(self, component: Any) -> Any: ...

class IPlottableGrid(object):  # Interface
    Count: int  # readonly

    def GetValue(
        self,
        index: int,
        column: Agilent.MassHunter.Quantitative.UIModel.IPlottableColumn,
    ) -> Optional[float]: ...
    def GetSampleID(
        self,
        index: int,
        column: Agilent.MassHunter.Quantitative.UIModel.IPlottableColumn,
    ) -> Optional[int]: ...
    def GetLabel(self, index: int) -> str: ...
    def IsPlottableColumn(
        self, column: Agilent.MassHunter.Quantitative.UIModel.IPlottableColumn
    ) -> bool: ...
    def GetCompoundID(
        self,
        index: int,
        column: Agilent.MassHunter.Quantitative.UIModel.IPlottableColumn,
    ) -> Optional[int]: ...
    def GetPlottableColumn(
        self, column: str
    ) -> Agilent.MassHunter.Quantitative.UIModel.IPlottableColumn: ...

    CountChanged: System.EventHandler  # Event
    ValueChanged: System.EventHandler  # Event

class IPresentationState(object):  # Interface
    ApplicationType: str  # readonly
    BatchDirectory: str  # readonly
    BatchFileName: str  # readonly
    BatchId: int  # readonly
    CanEditMethod: bool  # readonly
    Context: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AppCommandContext
    )  # readonly
    EditMethodState: (
        Agilent.MassHunter.Quantitative.UIModel.IEditMethodState
    )  # readonly
    EditingMethod: bool  # readonly
    HasBatch: bool  # readonly
    InstrumentType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType
    )  # readonly
    IsBatchDirty: bool  # readonly
    IsInCommandGroup: bool  # readonly
    IsWPF: bool  # readonly
    NumberFormats: Agilent.MassHunter.Quantitative.UIModel.INumberFormats  # readonly
    SubApplication: str
    SynchronizeInvoke: System.ComponentModel.ISynchronizeInvoke  # readonly

    def BeginRunScript(
        self,
        references: List[str],
        imports: List[str],
        language: str,
        code: System.IO.TextReader,
        customStub: System.MarshalByRefObject,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def EndRunScript(self, ret: System.IAsyncResult) -> Any: ...
    def ExceptionAbort(self, ex: System.Exception) -> None: ...
    def BeginCommandGroup(self) -> None: ...
    def EndCommandGroup(self) -> None: ...
    def GetLibrary(self, pathName: str) -> T: ...
    def GetLibraryError(self, pathName: str) -> str: ...
    @overload
    def ExecuteCommand(
        self, cmd: Agilent.MassSpectrometry.CommandModel.Model.ICommand
    ) -> Any: ...
    @overload
    def ExecuteCommand(
        self,
        parent: System.Windows.Forms.IWin32Window,
        cmd: Agilent.MassSpectrometry.CommandModel.Model.ICommand,
        ret: Any,
    ) -> bool: ...
    def PerformCompliancePreCommand(
        self, parent: System.Windows.Forms.IWin32Window, commandName: str, action: str
    ) -> bool: ...
    def NotifyNumericFormatChanged(self, e: System.EventArgs) -> None: ...

    AnalysisEnd: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisEventHandler
    )  # Event
    AnalysisStart: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisEventHandler
    )  # Event
    AnalysisStep: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisEventHandler
    )  # Event
    ApplyMethodEnded: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ApplyMethodEventHandler
    )  # Event
    ApplyMethodStarted: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ApplyMethodEventHandler
    )  # Event
    ApplyMethodToSample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ApplyMethodEventHandler
    )  # Event
    BatchFileClosed: System.EventHandler  # Event
    BatchFileClosing: System.EventHandler  # Event
    BatchFileCreated: System.EventHandler  # Event
    BatchFileOpened: System.EventHandler  # Event
    BatchFileOpening: System.EventHandler  # Event
    BatchFileSaved: System.EventHandler  # Event
    CommandGroupEnded: System.EventHandler  # Event
    CommandGroupStarted: System.EventHandler  # Event
    CompoundIdentificationEnd: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisEventArgs
    ]  # Event
    CompoundIdentificationStart: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisEventArgs
    ]  # Event
    CompoundIdentificationStep: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisEventArgs
    ]  # Event
    DeconvolutionEnd: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisEventArgs
    ]  # Event
    DeconvolutionStart: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisEventArgs
    ]  # Event
    DeconvolutionStep: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AnalysisEventArgs
    ]  # Event
    GraphicsSettingsChanged: System.EventHandler  # Event
    MethodEditingEnding: System.EventHandler  # Event
    MethodEditingStarted: System.EventHandler  # Event
    MethodEditingStarting: System.EventHandler  # Event
    NumericFormatChanged: System.EventHandler  # Event

class ISTDFilterInfo(
    System.IComparable[Agilent.MassHunter.Quantitative.UIModel.ISTDFilterInfo]
):  # Struct
    @overload
    def __init__(
        self,
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundFilterType,
        istdCompoundId: int,
        compoundName: str,
    ) -> None: ...
    @overload
    def __init__(
        self,
        istd: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow,
    ) -> None: ...

    CompoundId: int
    CompoundName: str
    Type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundFilterType

    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(
        self, info: Agilent.MassHunter.Quantitative.UIModel.ISTDFilterInfo
    ) -> bool: ...
    @overload
    def Matches(
        self, key: Agilent.MassHunter.Quantitative.UIModel.CompoundKey
    ) -> bool: ...
    @overload
    def Matches(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow,
    ) -> bool: ...
    def GetHashCode(self) -> int: ...
    def CompareTo(
        self, other: Agilent.MassHunter.Quantitative.UIModel.ISTDFilterInfo
    ) -> int: ...
    def ToString(self) -> str: ...

class ISampleDataPane(object):  # Interface
    AutoScale: bool
    CanAutoScale: bool  # readonly
    CanCopy: bool  # readonly
    CanCreateTargetCompound: bool  # readonly
    CanCreateTargetQualifier: bool  # readonly
    CanExtractSpectrum: bool  # readonly
    CanFindComponents: bool  # readonly
    CanNormalizeEachX: bool  # readonly
    CanSearchLibrary: bool  # readonly
    HasSpectrumPanes: bool  # readonly
    MaxNumVisibleRows: int
    NormalizeType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.NormalizeType
    OverlayAllSignals: bool
    OverlayIstdCompounds: bool
    OverlayTargetCompounds: bool
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    SampleDataPath: str  # readonly
    ShowCurrentCompound: bool
    ShowTic: bool
    TimeRange: Agilent.MassSpectrometry.DataAnalysis.IRange  # readonly

    def StoreSettings(self) -> None: ...
    def GetActiveObject(self) -> T: ...
    def AutoScaleX(self) -> None: ...
    def ShowSpectrum(self, start: float, end: float) -> None: ...
    def GetMSScanColor(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Drawing.Color: ...
    def GetDisplayedMSScanTypes(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    def ShowComponents(
        self, components: Iterable[Agilent.MassSpectrometry.DataAnalysis.Component]
    ) -> None: ...
    def Copy(self) -> None: ...
    def GetAvailableSignals(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Signal]: ...
    def CreateTargetCompound(self) -> None: ...
    def ClearSpectrumPanes(self) -> None: ...
    def CreatePropertyPages(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage
    ]: ...
    def CreateTargetQualifier(self) -> None: ...
    def AutoScaleY(self) -> None: ...
    def FindComponents(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Component
    ]: ...
    def ShowMSScan(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType, show: bool
    ) -> None: ...
    def DisplaySignal(
        self, signal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Signal
    ) -> None: ...
    def GetAvailableMSScanTypes(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    def HideSignal(
        self, signal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Signal
    ) -> None: ...
    def GetSignalColor(
        self, signal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Signal
    ) -> System.Drawing.Color: ...
    def GetDisplayedSignals(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Signal]: ...
    def SearchLibrary(
        self, site: Agilent.MassHunter.Quantitative.UIModel.ILibraryApp
    ) -> None: ...

class IScriptPane(object):  # Interface
    CanCopy: bool  # readonly
    CanPaste: bool  # readonly

    def Initialize(
        self,
        engine: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptEngine,
    ) -> None: ...
    def Copy(self) -> None: ...
    def Clear(self) -> None: ...
    def Paste(self) -> None: ...
    def Run(self) -> None: ...

class ISpectrumTransfer(object):  # Interface
    AcquiredMassRangeMinimum: Optional[float]  # readonly
    CollisionEnergy: Optional[float]  # readonly
    Count: int  # readonly
    IonPolarity: Optional[Agilent.MassSpectrometry.DataAnalysis.IonPolarity]  # readonly
    IsAccurateMass: bool  # readonly
    PeakCount: int  # readonly
    RetentionTime: Optional[float]  # readonly
    ScanType: Optional[Agilent.MassSpectrometry.DataAnalysis.MSScanType]  # readonly
    SelectedMz: Optional[float]  # readonly
    SignalToNoise: Optional[float]  # readonly
    Title: str  # readonly
    XValues: List[float]  # readonly
    YValues: List[float]  # readonly

    def GetPeakY(self, index: int) -> float: ...
    def GetMaxX(self) -> Optional[float]: ...
    def Normalize(self, y: float) -> None: ...
    def GetX(self, index: int) -> float: ...
    def GetY(self, index: int) -> float: ...
    def GetBasePeak(self, nx: Optional[float], ny: Optional[float]) -> None: ...
    def GetMinX(self) -> Optional[float]: ...
    def Clone(self) -> Agilent.MassHunter.Quantitative.UIModel.ISpectrumTransfer: ...
    def GetPeakX(self, index: int) -> float: ...

class IStatusBar(object):  # Interface
    Visible: bool

class IWorktablePane(object):  # Interface
    CanFillDown: bool  # readonly
    CanStartAutoReview: bool  # readonly
    CurrentLevelId: int  # readonly
    CurrentPeakId: int  # readonly
    CurrentQualifierId: int  # readonly
    DisplayAllSampleGroups: bool
    DisplayAllSampleTypes: bool
    FlagFilterManager: (
        Agilent.MassHunter.Quantitative.UIModel.IFlagFilterManager
    )  # readonly
    FontSizePercentage: float
    GridControl: Agilent.MassHunter.Quantitative.UIModel.IGridControl  # readonly
    HasNextSample: bool  # readonly
    HasPrevSample: bool  # readonly
    InvokeRequired: bool  # readonly
    LockSampleColumns: bool
    SingleCompoundMode: bool
    TableViewMode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TableViewMode

    def UpdateColors(self) -> None: ...
    def Invoke(self, d: System.Delegate) -> Any: ...
    def FillDown(self) -> None: ...
    def StartAutoReview(
        self, reviewCompounds: bool, manualIntegrating: bool
    ) -> None: ...
    def SetDisplaySampleType(self, type: str, display: bool) -> None: ...
    def ResetLayout(self) -> None: ...
    def HasNextCompound(self) -> bool: ...
    def ShowSelectOutliersDialog(self) -> System.Windows.Forms.DialogResult: ...
    def PrevSample(self) -> None: ...
    def GetDisplaySampleGroup(self, group: str) -> bool: ...
    def FindNext(
        self,
        tableName: str,
        columnName: str,
        operatorType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType,
        value_: Any,
    ) -> bool: ...
    def NextSample(self, manualIntegrating: bool) -> None: ...
    def DeleteSelectedSamples(self) -> None: ...
    def GetDisplaySampleType(self, type: str) -> bool: ...
    def GotoNextCompound(self) -> None: ...
    def GetDisplayedSampleGroups(self) -> List[str]: ...
    def CanDeleteSelectedSamples(self) -> bool: ...
    def CreatePropertyPages(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage
    ]: ...
    def GenerateStatusText(self) -> str: ...
    def GetSelectedSamples(
        self,
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleRowId]: ...
    def GetSamples(self) -> List[System.Data.DataRow]: ...
    def GetDisplayedSampleTypes(self) -> List[str]: ...
    def SetDisplaySampleGroup(self, group: str, display: bool) -> None: ...
    def GotoPrevCompound(self) -> None: ...
    def HasPrevCompound(self) -> bool: ...
    def RefreshSampleFilter(self) -> None: ...

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

class NavigateChangingEventArgs(System.ComponentModel.CancelEventArgs):  # Class
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

class TimeSegmentFilterInfo(
    System.IComparable[Agilent.MassHunter.Quantitative.UIModel.TimeSegmentFilterInfo]
):  # Struct
    @overload
    def __init__(
        self,
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundFilterType,
        timeSegment: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow,
    ) -> None: ...

    TimeSegment: int
    Type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundFilterType

    @overload
    def Equals(
        self, info: Agilent.MassHunter.Quantitative.UIModel.TimeSegmentFilterInfo
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Matches(
        self, key: Agilent.MassHunter.Quantitative.UIModel.CompoundKey
    ) -> bool: ...
    @overload
    def Matches(
        self,
        row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow,
    ) -> bool: ...
    def GetHashCode(self) -> int: ...
    def CompareTo(
        self, other: Agilent.MassHunter.Quantitative.UIModel.TimeSegmentFilterInfo
    ) -> int: ...
    def ToString(self) -> str: ...
