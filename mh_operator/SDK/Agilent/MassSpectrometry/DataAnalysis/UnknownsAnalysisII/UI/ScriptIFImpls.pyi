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
from . import ComponentFilter, ComponentHitID
from .Model import IMainWindow
from .ScriptIF import (
    ChromatogramViewMode,
    IAddIn,
    IAddInManager,
    IAnalysisMessageTable,
    IChromatogramPane,
    ICompliance,
    IComponentTable,
    IEICPane,
    IExactMassTable,
    IGridPane,
    IIonPeaksPane,
    IMainForm,
    IPane,
    IPlotPane,
    IQueryAnalysis,
    ISampleTable,
    IScriptEngine,
    IScriptInterface,
    IScriptPane,
    IScriptScope,
    ISpectrumPane,
    IStructurePane,
    IUADataAccess,
    IUIState,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls

class AddIn(System.MarshalByRefObject, IAddIn):  # Class
    DisplayName: str  # readonly
    Enabled: bool
    Name: str  # readonly
    PathName: str  # readonly

class AddInManager(
    System.MarshalByRefObject, System.IDisposable, IAddInManager
):  # Class
    Count: int  # readonly
    def __getitem__(self, id: str) -> IAddIn: ...
    def Dispose(self) -> None: ...
    def GetIDs(self) -> List[str]: ...

class AnalysisMessageTable(
    IPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.GridPaneBase,
    System.IDisposable,
    IAnalysisMessageTable,
    System.Windows.Forms.IWin32Window,
):  # Class
    ...

class ChromatogramPane(
    IPlotPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.PlotPaneBase,
    System.IDisposable,
    IPane,
    IChromatogramPane,
    System.Windows.Forms.IWin32Window,
):  # Class
    CanAutoScaleXY: bool  # readonly
    CanCopy: bool  # readonly
    ChromatogramViewMode: ChromatogramViewMode
    ShowComponents: bool
    ShowEics: bool
    ShowTic: bool

    def Copy(self) -> None: ...
    def AutoScaleXY(self) -> None: ...
    def ShowPropertiesDialog(self) -> None: ...

class Compliance(System.MarshalByRefObject, ICompliance):  # Class
    ConnectionTicket: str  # readonly
    IsActive: bool  # readonly
    IsLocal: bool  # readonly
    Name: str  # readonly
    User: str  # readonly

class ComponentTable(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.GridPaneBase,
    IGridPane,
    System.IDisposable,
    IComponentTable,
    IPane,
    System.Windows.Forms.IWin32Window,
):  # Class
    CanCopy: bool  # readonly
    CanDeleteComponentsHits: bool  # readonly
    CanExport: bool  # readonly
    CanFormatColumn: bool  # readonly
    CanSetBestHits: bool  # readonly

    def SetColumnVisible(self, columnName: str, visible: bool) -> None: ...
    def ExportToText(
        self,
        allComponents: bool,
        writer: System.IO.TextWriter,
        delimiter: str,
        autoCompoundNames: bool,
        nonHitPrefix: str,
        nonHitAddIndex: bool,
    ) -> None: ...
    def FormatColumn(self) -> None: ...
    def SetBestHits(self) -> None: ...
    def Copy(self) -> None: ...
    def IsColumnVisible(self, columnName: str) -> bool: ...
    def ExportToLibrary(
        self,
        allComponents: bool,
        autoCompoundNames: bool,
        nonHitPrefix: str,
        nonHitAddIndex: bool,
    ) -> None: ...
    def ShowColumnsDialog(self) -> None: ...
    def DeleteComponentsHits(self) -> None: ...
    def RestoreComponentsHits(self) -> None: ...
    def ExportToQuantMethod(
        self,
        destination: str,
        allComponents: bool,
        autoCompoundNames: bool,
        nonHitPrefix: str,
        nonHitAddIndex: bool,
        ionMode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodFromLibraryIonMode,
        numQualifiers: int,
    ) -> None: ...

class ExactMassTable(
    IPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.GridPaneBase,
    System.IDisposable,
    IExactMassTable,
    IGridPane,
):  # Class
    CanCopy: bool  # readonly
    CanFormatColumn: bool  # readonly

    def FormatColumn(self) -> None: ...
    def Copy(self) -> None: ...
    def ShowColumnsDialog(self) -> None: ...
    def ShowAlternativeExactMassDialog(self) -> None: ...
    def CanShowAlternativeExactMassDialog(self) -> bool: ...

class GridPaneBase(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.PaneBase,
    IPane,
    System.IDisposable,
):  # Class
    CanPrint: bool  # readonly

    def PageSetup(self) -> None: ...
    def PrintDialog(self) -> None: ...
    def PrintPreview(self) -> None: ...

class IonPeaksPane(
    IPlotPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.PlotPaneBase,
    System.IDisposable,
    IIonPeaksPane,
    IPane,
    System.Windows.Forms.IWin32Window,
):  # Class
    CanAutoScaleXY: bool  # readonly
    CanCopy: bool  # readonly
    ShowComponent: bool
    ShowTIC: bool

    def Copy(self) -> None: ...
    def AutoScaleXY(self) -> None: ...
    def ShowPropertiesDialog(self) -> None: ...

class MainForm(
    System.MarshalByRefObject, IMainForm, System.Windows.Forms.IWin32Window
):  # Class
    ActivePane: IPane  # readonly
    AnalysisMessageTable: IAnalysisMessageTable  # readonly
    ChromatogramPane: IChromatogramPane  # readonly
    ComponentTable: IComponentTable  # readonly
    EICPane: IEICPane  # readonly
    ExactMassTable: IExactMassTable  # readonly
    IonPeaksPane: IIonPeaksPane  # readonly
    SampleTable: ISampleTable  # readonly
    ScriptPane: IScriptPane  # readonly
    SpectrumPane: ISpectrumPane  # readonly
    StructurePane: IStructurePane  # readonly
    ToolManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager
    )  # readonly
    _Form: IMainWindow  # readonly

    def Layout(self, layout: int) -> None: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def Close(self, forceClose: bool) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def ShowQuery(self, queryFile: str) -> None: ...

class PaneBase(IPane, System.MarshalByRefObject, System.IDisposable):  # Class
    CanCopy: bool  # readonly
    CanPrint: bool  # readonly
    Visible: bool

    def GetActiveObject(self) -> T: ...
    def Copy(self) -> None: ...
    def PrintDialog(self) -> None: ...
    def PageSetup(self) -> None: ...
    def PrintPreview(self) -> None: ...
    def Dispose(self) -> None: ...

class PlotPaneBase(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.PaneBase,
    IPane,
    System.IDisposable,
):  # Class
    CanNextZoom: bool  # readonly
    CanPrevZoom: bool  # readonly
    CanPrint: bool  # readonly

    def PrevZoom(self) -> None: ...
    def PrintDialog(self) -> None: ...
    def PageSetup(self) -> None: ...
    def PrintPreview(self) -> None: ...
    def NextZoom(self) -> None: ...

class QueryAnalysis(
    System.MarshalByRefObject, IQueryAnalysis, System.IDisposable
):  # Class
    def QuerySamples(
        self, batchID: Optional[int]
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleDataTable
    ): ...
    def Dispose(self) -> None: ...
    def QueryBatches(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchDataTable
    ): ...

class SampleTable(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.GridPaneBase,
    ISampleTable,
    IGridPane,
    System.IDisposable,
    IPane,
    System.Windows.Forms.IWin32Window,
):  # Class
    CanCopy: bool  # readonly
    CanFormatColumn: bool  # readonly

    def Copy(self) -> None: ...
    def ShowColumnsDialog(self) -> None: ...
    def FormatColumn(self) -> None: ...

class ScriptEngine(
    IScriptEngine, System.MarshalByRefObject, System.IDisposable
):  # Class
    CurrentScope: IScriptScope  # readonly
    DebugMode: bool  # readonly
    Engine: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptEngine
    )  # readonly
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
        engine: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IronEngine,
        initEngine: System.Action[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IronEngine,
            Any,
        ],
    ) -> None: ...
    def Dispose(self) -> None: ...
    def ExecuteFile(self, file: str, scope: IScriptScope) -> Any: ...

class ScriptInterface(
    IScriptInterface, System.MarshalByRefObject, System.IDisposable
):  # Class
    Compliance: ICompliance  # readonly
    ScriptEngine: IScriptEngine  # readonly
    UADataAccess: IUADataAccess  # readonly
    UIState: IUIState  # readonly
    _ScriptInterface: IScriptInterface  # readonly

    def Dispose(self) -> None: ...
    def _GetPrivateProfileString(
        self, section: str, key: str, defaultValue: str, fileName: str
    ) -> str: ...
    def _WritePrivateProfileString(
        self, section: str, key: str, value_: str, fileName: str
    ) -> int: ...

class ScriptPane(
    System.IDisposable,
    IPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.PaneBase,
    IScriptPane,
):  # Class
    CanCopy: bool  # readonly

    def Copy(self) -> None: ...
    def Run(self) -> None: ...
    def Clear(self) -> None: ...

class SpectrumPane(
    IPlotPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.PlotPaneBase,
    System.IDisposable,
    ISpectrumPane,
    IPane,
    System.Windows.Forms.IWin32Window,
):  # Class
    CanAutoScaleXY: bool  # readonly
    CanCopy: bool  # readonly
    HeadToTail: bool
    ShowExtractedSpectrum: bool

    def Copy(self) -> None: ...
    def GetActiveObject(self) -> T: ...
    def AutoScaleXY(self) -> None: ...
    def ShowPropertiesDialog(self) -> None: ...

class StructurePane(
    IPane,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.PaneBase,
    IStructurePane,
    System.Windows.Forms.IWin32Window,
):  # Class
    CanCopy: bool  # readonly
    CanPrint: bool  # readonly

    def PageSetup(self) -> None: ...
    def Copy(self) -> None: ...
    def PrintDialog(self) -> None: ...
    def PrintPreview(self) -> None: ...

class UADataAccess(System.MarshalByRefObject, IUADataAccess):  # Class
    def GetBatches(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchDataTable
    ): ...
    def GetLibrarySearchMethods(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodDataTable
    ): ...
    def GetHits(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitDataTable
    ): ...
    def GetPeakQualifier(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakQualifierDataTable
    ): ...
    def GetIonPeak(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IonPeakDataTable
    ): ...
    def Base64ToDoubleArray(self, base64: str) -> List[float]: ...
    def GetTargetQualifier(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetQualifierDataTable
    ): ...
    def GetPeak(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.PeakDataTable
    ): ...
    def GetTargetMatchMethods(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodDataTable
    ): ...
    def GetAnalysis(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AnalysisDataTable
    ): ...
    def GetAuxiliaryMethod(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.AuxiliaryMethodDataTable
    ): ...
    def GetComponents(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.ComponentDataTable
    ): ...
    def GetDeconvolutionMethods(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodDataTable
    ): ...
    def GetIdentificationMethods(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodDataTable
    ): ...
    def GetSamples(
        self, batchID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleDataTable
    ): ...
    def GetTargetCompounds(
        self, batchID: int, sampleID: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundDataTable
    ): ...

class UIState(System.MarshalByRefObject, IUIState, System.IDisposable):  # Class
    def __init__(self, mainForm: IMainWindow) -> None: ...

    ActiveForm: System.Windows.Forms.IWin32Window  # readonly
    ActivePane: IPane  # readonly
    AddInManager: IAddInManager  # readonly
    AnalysisFileName: str  # readonly
    BatchFolder: str  # readonly
    BestHitsOnly: bool
    BestPrimaryHitsOnly: bool
    BlankComponent: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ComponentRowID
    )
    BlankSubtractedHits: bool
    CanRedo: bool  # readonly
    CanUndo: bool  # readonly
    ComponentFilter: ComponentFilter
    Constants: Dict[str, str]  # readonly
    ExitCode: int
    FilePath: str  # readonly
    HasAnalysis: bool  # readonly
    IsAuditTrailing: bool  # readonly
    IsDirty: bool  # readonly
    MainForm: IMainForm  # readonly
    PrimaryHitsOnly: bool
    QueryAnalysis: IQueryAnalysis  # readonly
    SampleCount: int  # readonly
    ScriptEngine: IScriptEngine  # readonly
    SelectedComponentHitCount: int  # readonly
    SelectedSampleCount: int  # readonly
    SelectedSamples: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
    ]  # readonly
    SynchronizeInvoke: System.ComponentModel.ISynchronizeInvoke  # readonly
    ToolManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager
    )  # readonly
    UADataAccess: IUADataAccess  # readonly
    _ExitCode: int  # static

    def IsSampleSelected(self, batchId: int, sampleId: int) -> bool: ...
    def GetSelectedComponentHits(self) -> Iterable[ComponentHitID]: ...
    def SelectSamples(
        self,
        samples: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
        ],
    ) -> None: ...
    def ShowAuditTrailWindow(self) -> None: ...
    def SelectComponentHits(
        self, chids: Iterable[ComponentHitID], clear: bool
    ) -> None: ...
    def Dispose(self) -> None: ...
    @overload
    def RunScript(self, file: str) -> Any: ...
    @overload
    def RunScript(self, stream: System.IO.Stream) -> Any: ...
    def ShowMessage(
        self,
        message: str,
        caption: str,
        buttons: System.Windows.Forms.MessageBoxButtons,
        icon: System.Windows.Forms.MessageBoxIcon,
    ) -> System.Windows.Forms.DialogResult: ...
