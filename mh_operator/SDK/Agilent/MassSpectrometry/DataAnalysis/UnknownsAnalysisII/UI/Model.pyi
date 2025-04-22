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
from .Common import LibrarySearchSite
from .ScriptIF import ChromatogramViewMode, IUIState

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model

class IAnalysisMessageGridView(object):  # Interface
    ContextMenuStrip: System.Windows.Forms.ContextMenuStrip
    DataGridView: System.Windows.Forms.DataGridView  # readonly

    def Initialize(
        self,
        window: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IMainWindow,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext,
    ) -> None: ...

class IAnalysisMessageTableControl(object):  # Interface
    AnalysisMessageGridView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IAnalysisMessageGridView
    )  # readonly

class IChromatogramControl(object):  # Interface
    ChromatogramView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IChromatogramView
    )  # readonly

class IChromatogramView(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IPlotControlBase
):  # Interface
    ChromatogramViewMode: ChromatogramViewMode
    ShowComponents: bool
    ShowEics: bool
    ShowTic: bool

    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext,
    ) -> None: ...
    def AutoScaleY(self) -> None: ...
    def UpdateSettings(self) -> None: ...
    def UpdatePeakLabels(self) -> None: ...
    def UpdateSeriesVisibility(self) -> None: ...
    def UpdatePeakLabelSettings(self) -> None: ...

class IComponentGridView(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IGridControlBase
):  # Interface
    CanDeleteComponentsHits: bool  # readonly
    CanSetBestHits: bool  # readonly
    SelectedComponentBackColor: System.Drawing.Color
    SelectedComponentForeColor: System.Drawing.Color

    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext,
    ) -> None: ...
    def ExportTableToLibrary(
        self,
        allComponents: bool,
        autoCompoundNames: bool,
        nonHitPrefix: str,
        nonHitAddIndex: bool,
    ) -> None: ...
    def SetBestHits(self) -> None: ...
    def GetVisibleColumns(self) -> List[str]: ...
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
    def SelectNearestComponent(self, rt: float) -> None: ...

class IComponentTableControl(object):  # Interface
    ComponentGridView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IComponentGridView
    )  # readonly

class IComponentTableView(object):  # Interface
    BestHitsOnly: bool
    BestPrimaryHitsOnly: bool
    BlankSubtractedHits: bool
    Count: int  # readonly
    Filter: ComponentFilter
    def __getitem__(self, index: int) -> ComponentHitID: ...
    PrimaryHitsOnly: bool

    def GetWhereClause(self) -> str: ...
    def GetCount(
        self,
        batchId: int,
        sampleId: int,
        filter: ComponentFilter,
        hideBlankSubtracted: bool,
        bestHitsOnly: bool,
        primaryHitsOnly: bool,
    ) -> int: ...

    TableChanged: System.EventHandler  # Event

class IEicPeaksControl(object):  # Interface
    EicPeaksView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IEicPeaksView
    )  # readonly

class IEicPeaksView(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IPlotControlBase
):  # Interface
    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext,
        mainWindow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IMainWindow,
    ) -> None: ...
    def UpdateSettings(self) -> None: ...

class IExactMassGridView(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IGridControlBase
):  # Interface
    def CanShowAlternativeExactMassDialog(self) -> bool: ...
    def Initialize(
        self,
        mainWindow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IMainWindow,
    ) -> None: ...
    def ShowAlternativeExactMassDialog(self) -> None: ...

class IExactMassTableControl(object):  # Interface
    ExactMassGridView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IExactMassGridView
    )  # readonly

class IGridControlBase(object):  # Interface
    CanCopy: bool  # readonly
    CanSetColumnFormat: bool  # readonly
    ContextMenuStrip: System.Windows.Forms.ContextMenuStrip
    DataGridView: System.Windows.Forms.DataGridView  # readonly
    Handle: System.IntPtr  # readonly
    IsCurrentCellInEditMode: bool  # readonly
    RowCount: int  # readonly

    def Copy(self) -> None: ...
    def ExportToCsv(
        self,
        allComponents: bool,
        writer: System.IO.TextWriter,
        delimiter: str,
        autoCompoundNames: bool,
        nonHitPrefix: str,
        nonHitAddIndex: bool,
    ) -> None: ...
    def ShowColumnsDialog(self) -> None: ...
    def SetColumnFormat(self) -> None: ...

class IIonPeakTableView(object):  # Interface
    Count: int  # readonly
    def __getitem__(
        self, index: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IIonPeakViewItem
    ): ...
    def FindItem(self, x: float) -> int: ...
    def ShowDefaultIons(self) -> None: ...
    def ToggleVisible(self, index: int) -> bool: ...
    def AddIon(self, x: float) -> None: ...
    def Clear(self) -> None: ...
    def UpdateColors(self) -> None: ...

    VisibleIonPeaksChanged: System.EventHandler  # Event

class IIonPeakViewItem(object):  # Interface
    Abundance: float  # readonly
    BatchID: int  # readonly
    Color: System.Drawing.Color
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    IonPeakID: int  # readonly
    MZ: float  # readonly
    SampleID: int  # readonly
    Visible: bool  # readonly

class IIonPeaksControl(object):  # Interface
    IonPeaksView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IIonPeaksView
    )  # readonly

class IIonPeaksView(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IPlotControlBase
):  # Interface
    ShowComponent: bool
    ShowTIC: bool
    UIContext: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext
    )  # readonly

    def Initialize(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext,
    ) -> None: ...
    def UpdateSettings(self) -> None: ...

class IMainWindow(System.Windows.Forms.IWin32Window):  # Interface
    ActivePane: str  # readonly
    AddInManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.AddInManager
    )  # readonly
    AnalysisMessageTableControl: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IAnalysisMessageTableControl
    )  # readonly
    ChromatogramControl: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IChromatogramControl
    )  # readonly
    ComponentTableControl: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IComponentTableControl
    )  # readonly
    EicPeaksControl: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IEicPeaksControl
    )  # readonly
    ExactMassTableControl: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IExactMassTableControl
    )  # readonly
    InvokeRequired: bool  # readonly
    IonPeaksControl: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IIonPeaksControl
    )  # readonly
    IsDisposed: bool  # readonly
    IsHandleCreated: bool  # readonly
    SampleTableControl: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.ISampleTableControl
    )  # readonly
    ScriptControl: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.ScriptControl
    )  # readonly
    SpectrumControl: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.ISpectrumControl
    )  # readonly
    StructureControl: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IStructureControl
    )  # readonly
    Title: str
    ToolManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager
    )  # readonly
    UIContext: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext
    )  # readonly
    UIState: IUIState  # readonly

    def ActivateWindow(self) -> None: ...
    def SetLayout(self, layout: int) -> None: ...
    def SetPaneVisible(self, key: str, visible: bool) -> None: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    @overload
    def Close(self) -> None: ...
    @overload
    def Close(self, forceClose: bool) -> None: ...
    def IsPaneVisible(self, key: str) -> bool: ...
    def BeginInvoke(self, d: System.Delegate, parameters: List[Any]) -> None: ...
    def SaveLayout(self, straem: System.IO.Stream) -> None: ...
    def ShowQuery(self, queryFile: str) -> None: ...
    def Invoke(self, d: System.Delegate, parameters: List[Any]) -> Any: ...

    Closed: System.EventHandler  # Event
    PaneVisibleChanged: System.EventHandler  # Event

class IPlotControlBase(object):  # Interface
    CanAutoScaleXY: bool  # readonly
    _PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly

    def PrintDialog(
        self,
        pageSettings: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PlotPageSettings,
    ) -> None: ...
    def SetContextMenuInternal(
        self, contextMenu: System.Windows.Forms.ContextMenuStrip
    ) -> None: ...
    def AutoScaleXY(self) -> None: ...
    def PrintPreview(
        self,
        pageSettings: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PlotPageSettings,
    ) -> None: ...
    def Invalidate(self) -> None: ...

class ISampleGridView(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IGridControlBase
):  # Interface
    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext,
    ) -> None: ...
    def StoreVisibleColumns(self) -> None: ...

class ISampleTableControl(object):  # Interface
    SampleGridView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.ISampleGridView
    )  # readonly

class ISelectedRanges(object):  # Interface
    Count: int  # readonly
    HasTempSelection: bool  # readonly

    def GetTempSelection(
        self,
        sample: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID,
        range: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
    ) -> None: ...
    def SetTempSelection(
        self,
        sample: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID,
        range: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
    ) -> None: ...
    def HitTest(
        self, batchID: int, sampleID: int, rt: float
    ) -> Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange]: ...
    def RemoveRange(
        self,
        batchID: int,
        sampleID: int,
        range: Agilent.MassSpectrometry.GUI.Plot.PlotRange,
        suppressEvent: bool,
    ) -> None: ...
    def Clear(self) -> None: ...
    def GetRanges(
        self, batchID: int, sampleID: int
    ) -> Iterable[Agilent.MassSpectrometry.GUI.Plot.PlotRange]: ...
    def AddRange(
        self,
        batchID: int,
        sampleID: int,
        range: Agilent.MassSpectrometry.GUI.Plot.PlotRange,
    ) -> None: ...
    def GetSamples(
        self,
    ) -> Iterable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
    ]: ...

    SelectionChanged: System.EventHandler  # Event
    TempSelectionChanged: System.EventHandler  # Event

class ISpectrumControl(object):  # Interface
    SpectrumView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.ISpectrumView
    )  # readonly

class ISpectrumView(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IPlotControlBase
):  # Interface
    CanAutoScaleXY: bool  # readonly
    CanCopy: bool  # readonly
    HeadToTailView: bool
    ShowExtractedSpectrum: bool

    def GetActiveObject(self) -> T: ...
    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext,
    ) -> None: ...
    def Copy(self) -> None: ...
    def UpdateSettings(self) -> None: ...
    def SetContextMenuInternal(
        self, contextMenu: System.Windows.Forms.ContextMenuStrip
    ) -> None: ...
    def AutoScaleXY(self) -> None: ...
    def Invalidate(self) -> None: ...

class IStructureControl(object):  # Interface
    CanCopy: bool  # readonly
    ClientRectangle: System.Drawing.Rectangle  # readonly
    Control: System.Windows.Forms.Control  # readonly
    Handle: System.IntPtr  # readonly

    def Copy(self) -> None: ...
    def DrawTo(
        self,
        g: System.Drawing.Graphics,
        color: System.Drawing.Color,
        rect: System.Drawing.Rectangle,
    ) -> None: ...

class IUIContext(object):  # Interface
    AccurateMassExtension: bool
    BlankComponent: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ComponentRowID
    )
    CommandContext: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext
    )  # readonly
    ComponentTableView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IComponentTableView
    )  # readonly
    DataFile: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataFileBase
    )  # readonly
    IonPeakTableView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IIonPeakTableView
    )  # readonly
    IsWPF: bool  # readonly
    LibrarySearchSite: LibrarySearchSite  # readonly
    SelectedComponentHitCount: int  # readonly
    SelectedExactMassCount: int  # readonly
    SelectedRanges: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.ISelectedRanges
    )  # readonly
    SelectedSampleCount: int  # readonly
    SelectedSamples: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
    ]  # readonly
    SelectingSamples: bool  # readonly
    SingleSelectedSampleRowID: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
    )  # readonly
    SynchronizeInvoke: System.ComponentModel.ISynchronizeInvoke  # readonly
    WalkingChromatogramRanges: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.ISelectedRanges
    )  # readonly

    def IsComponentSelected(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int, componentID: int
    ) -> bool: ...
    def IdleInvoke(self, d: System.Delegate, parameters: List[Any]) -> None: ...
    def GetSelectedExactMass(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ExactMassRowID: ...
    def SelectSamples(
        self,
        srids: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
        ],
    ) -> None: ...
    def SelectComponentHits(
        self, chids: Iterable[ComponentHitID], clearSelection: bool
    ) -> None: ...
    def IsSelected(self, batchId: int, sampleId: int) -> bool: ...
    def GetSelectedComponentHitID(self, index: int) -> ComponentHitID: ...
    def SelectExactMasses(
        self,
        emrids: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ExactMassRowID
        ],
        clearSelection: bool,
    ) -> None: ...

    AnalysisClosed: System.EventHandler  # Event
    AnalysisClosing: System.EventHandler  # Event
    AnalysisNew: System.EventHandler  # Event
    AnalysisOpened: System.EventHandler  # Event
    AnalysisOpening: System.EventHandler  # Event
    AnalysisSaved: System.EventHandler  # Event
    AnalysisSaving: System.EventHandler  # Event
    BlankComponentChanged: System.EventHandler  # Event
    ComponentHitSelectionChanged: System.EventHandler  # Event
    CurrentSampleChanged: System.EventHandler  # Event
    ExactMassSelectionChanged: System.EventHandler  # Event
    SampleSelectionChanged: System.EventHandler  # Event

class PaneIds:  # Class
    AnalysisMessage: str = ...  # static # readonly
    Chromatogram: str = ...  # static # readonly
    ComponentTable: str = ...  # static # readonly
    EicPeaks: str = ...  # static # readonly
    ExactMass: str = ...  # static # readonly
    HitTable: str = ...  # static # readonly
    IonPeaks: str = ...  # static # readonly
    SampleTable: str = ...  # static # readonly
    Script: str = ...  # static # readonly
    Spectrum: str = ...  # static # readonly
    Structure: str = ...  # static # readonly
