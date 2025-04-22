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
from .Model import IMainWindow, IUIContext

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF

class ChromatogramViewMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    SelectComponents: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.ChromatogramViewMode
    ) = ...  # static # readonly
    SelectRanges: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.ChromatogramViewMode
    ) = ...  # static # readonly
    Unknown: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.ChromatogramViewMode
    ) = ...  # static # readonly
    WalkChromatogram: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.ChromatogramViewMode
    ) = ...  # static # readonly

class IAddIn(object):  # Interface
    DisplayName: str  # readonly
    Enabled: bool
    Name: str  # readonly
    PathName: str  # readonly

class IAddInManager(object):  # Interface
    Count: int  # readonly
    def __getitem__(
        self, id: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IAddIn
    ): ...
    def GetIDs(self) -> List[str]: ...

class IAnalysisMessageTable(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane,
    System.Windows.Forms.IWin32Window,
):  # Interface
    ...

class IChromatogramPane(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPlotPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane,
    System.Windows.Forms.IWin32Window,
):  # Interface
    ChromatogramViewMode: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.ChromatogramViewMode
    )
    ShowComponents: bool
    ShowEics: bool
    ShowTic: bool

    def ShowPropertiesDialog(self) -> None: ...

class ICompliance(object):  # Interface
    ConnectionTicket: str  # readonly
    IsActive: bool  # readonly
    IsLocal: bool  # readonly
    Name: str  # readonly
    User: str  # readonly

class IComponentTable(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IGridPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane,
    System.Windows.Forms.IWin32Window,
):  # Interface
    CanDeleteComponentsHits: bool  # readonly
    CanExport: bool  # readonly
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
    def SetBestHits(self) -> None: ...
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

class IEICPane(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPlotPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane,
    System.Windows.Forms.IWin32Window,
):  # Interface
    def ShowPropertiesDialog(self) -> None: ...

class IExactMassTable(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IGridPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane,
):  # Interface
    def CanShowAlternativeExactMassDialog(self) -> bool: ...
    def ShowAlternativeExactMassDialog(self) -> None: ...
    def ShowColumnsDialog(self) -> None: ...

class IGridPane(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane
):  # Interface
    CanFormatColumn: bool  # readonly

    def FormatColumn(self) -> None: ...

class IIonPeaksPane(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPlotPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane,
    System.Windows.Forms.IWin32Window,
):  # Interface
    ShowComponent: bool
    ShowTIC: bool

    def ShowPropertiesDialog(self) -> None: ...

class IMainForm(System.Windows.Forms.IWin32Window):  # Interface
    ActivePane: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane
    )  # readonly
    AnalysisMessageTable: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IAnalysisMessageTable
    )  # readonly
    ChromatogramPane: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IChromatogramPane
    )  # readonly
    ComponentTable: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IComponentTable
    )  # readonly
    EICPane: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IEICPane
    )  # readonly
    ExactMassTable: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IExactMassTable
    )  # readonly
    IonPeaksPane: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IIonPeaksPane
    )  # readonly
    SampleTable: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.ISampleTable
    )  # readonly
    ScriptPane: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IScriptPane
    )  # readonly
    SpectrumPane: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.ISpectrumPane
    )  # readonly
    StructurePane: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IStructurePane
    )  # readonly
    ToolManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager
    )  # readonly
    _Form: IMainWindow  # readonly

    def Layout(self, layoutNumber: int) -> None: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def Close(self, forceClose: bool) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def ShowQuery(self, queryFile: str) -> None: ...

class IPane(object):  # Interface
    CanCopy: bool  # readonly
    CanPrint: bool  # readonly
    Visible: bool

    def PageSetup(self) -> None: ...
    def Copy(self) -> None: ...
    def PrintDialog(self) -> None: ...
    def PrintPreview(self) -> None: ...

class IPlotPane(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane
):  # Interface
    CanAutoScaleXY: bool  # readonly
    CanNextZoom: bool  # readonly
    CanPrevZoom: bool  # readonly

    def GetActiveObject(self) -> T: ...
    def AutoScaleXY(self) -> None: ...
    def NextZoom(self) -> None: ...
    def PrevZoom(self) -> None: ...

class IQueryAnalysis(object):  # Interface
    def QuerySamples(
        self, batchID: Optional[int]
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.SampleDataTable
    ): ...
    def QueryBatches(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BatchDataTable
    ): ...

class ISampleTable(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IGridPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane,
    System.Windows.Forms.IWin32Window,
):  # Interface
    def ShowColumnsDialog(self) -> None: ...

class IScriptEngine(object):  # Interface
    CurrentScope: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IScriptScope
    )  # readonly
    DebugMode: bool  # readonly
    Engine: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptEngine
    )  # readonly
    Globals: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IScriptScope
    )  # readonly

    def CreateScope(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IScriptScope
    ): ...
    def ExecuteFile(
        self,
        file: str,
        scope: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(
        self,
        stream: System.IO.Stream,
        encoding: System.Text.Encoding,
        scope: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(
        self,
        reader: System.IO.TextReader,
        encoding: System.Text.Encoding,
        scope: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IScriptScope,
    ) -> Any: ...

class IScriptInterface(object):  # Interface
    Compliance: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.ICompliance
    )  # readonly
    ScriptEngine: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IScriptEngine
    )  # readonly
    UADataAccess: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUADataAccess
    )  # readonly
    UIState: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState
    )  # readonly
    _ScriptInterface: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IScriptInterface
    )  # readonly

    def _GetPrivateProfileString(
        self, section: str, key: str, defaultValue: str, fileName: str
    ) -> str: ...
    def _WritePrivateProfileString(
        self, section: str, key: str, value_: str, fileName: str
    ) -> int: ...

class IScriptPane(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane
):  # Interface
    def Run(self) -> None: ...
    def Clear(self) -> None: ...

class IScriptScope(object):  # Interface
    def GetVariableNames(self) -> Iterable[str]: ...
    def RemoveVariable(self, name: str) -> None: ...
    def GetVariable(self, name: str) -> Any: ...
    def ContainsVariable(self, name: str) -> bool: ...
    def SetVariable(self, name: str, value_: Any) -> None: ...

class ISpectrumPane(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPlotPane,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane,
    System.Windows.Forms.IWin32Window,
):  # Interface
    HeadToTail: bool
    ShowExtractedSpectrum: bool

    def ShowPropertiesDialog(self) -> None: ...

class IStructurePane(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane,
    System.Windows.Forms.IWin32Window,
):  # Interface
    ...

class IUADataAccess(object):  # Interface
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

class IUIState(object):  # Interface
    ActiveForm: System.Windows.Forms.IWin32Window  # readonly
    ActivePane: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IPane
    )  # readonly
    AddInManager: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IAddInManager
    )  # readonly
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
    MainForm: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IMainForm
    )  # readonly
    PrimaryHitsOnly: bool
    QueryAnalysis: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IQueryAnalysis
    )  # readonly
    SampleCount: int  # readonly
    ScriptEngine: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IScriptEngine
    )  # readonly
    SelectedComponentHitCount: int  # readonly
    SelectedSampleCount: int  # readonly
    SelectedSamples: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
    ]  # readonly
    SynchronizeInvoke: System.ComponentModel.ISynchronizeInvoke  # readonly
    ToolManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager
    )  # readonly
    UADataAccess: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUADataAccess
    )  # readonly
    _CommandContext: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext
    )  # readonly
    _UIContext: IUIContext  # readonly

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
