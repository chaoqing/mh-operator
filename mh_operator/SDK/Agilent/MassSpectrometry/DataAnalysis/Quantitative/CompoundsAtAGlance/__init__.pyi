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
    BatchDataSet,
    OutlierColumns,
    PresentationState,
    ProgressEventArgs,
    QualifierInfoLabelType,
    QuantitationDataSet,
    RowIdBase,
    SampleRowId,
    TargetCompoundRowId,
)
from .Controls2 import IPropertyPage
from .Toolbar import (
    IToolbar,
    IToolbarsManager,
    IToolBeforeDropdownHandler,
    IToolHandler,
    ToolbarsManagerBase,
)
from .Toolbar2 import ITool, IToolHandler
from .UIScriptIF import (
    IAddIn,
    IAddInManager,
    ICompoundsAtAGlance,
    IReviewItem,
    IUIState,
)
from .UIUtils import DefaultEventManipulatorBase

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance

class AddInManager(
    System.MarshalByRefObject, System.IDisposable, IAddInManager
):  # Class
    def __getitem__(self, id: str) -> IAddIn: ...
    def Initialize(self) -> None: ...
    def Clear(self) -> None: ...
    def Dispose(self) -> None: ...
    def GetIDs(self) -> List[str]: ...

class CAGOutlierFilterType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    All: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CAGOutlierFilterType
    ) = ...  # static # readonly
    HideOutliers: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CAGOutlierFilterType
    ) = ...  # static # readonly
    ShowOutliers: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CAGOutlierFilterType
    ) = ...  # static # readonly

class CagLayout:  # Class
    def __init__(self) -> None: ...

    DimensionX: int
    DimensionY: int
    FillPeaks: bool
    FitMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.FitMode
    )
    LinkAllXAxes: bool
    LinkAllYAxes: bool
    LinkXAxes: bool
    LinkYAxes: bool
    LinkYAxesVertically: bool
    ManualYScale: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange]
    Normalize: bool
    OrganizeType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.OrganizeType
    )
    OutlierFilterType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CAGOutlierFilterType
    )
    Outliers: List[OutlierColumns]
    Overlay: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    )
    PeakAnnotations: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ]
    QualifierInfoLabelType: QualifierInfoLabelType
    ReviewMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewMode
    )
    ShowBaselines: bool
    ShowPeakAnnotationNames: bool
    ShowPeakAnnotationUnits: bool
    ShowRecognitionWindow: bool
    ShowReferenceRT: bool
    ShowUncertaintyBand: bool
    WrapMode: bool

    def CopyFrom(
        self,
        layout: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CagLayout,
    ) -> None: ...
    def OutlierExists(self, oc: OutlierColumns) -> bool: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def SaveConfiguration(self) -> None: ...
    def InitConfiguration(self) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...

class CagSettingsSection(System.Configuration.ConfigurationSection):  # Class
    def __init__(self) -> None: ...

    DefaultLayout: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PresetLayout
    )  # readonly
    PresetLayouts: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PresetLayoutCollection
    )  # readonly

class CagView(
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

    CagViewControl: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CagViewControl
    )  # readonly

class CagViewControl(
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ICagViewControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.ComponentModel.ISupportInitialize,
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
    Agilent.MassSpectrometry.GUI.Plot.PlotControl,
):  # Class
    def __init__(self) -> None: ...

    CanAutoScale: bool  # readonly
    CanCopyPage: bool  # readonly
    CanCopyPane: bool  # readonly
    CanFitToCalibrationLevels: bool  # readonly
    CanFreezeColumns: bool  # readonly
    CanFreezePanes: bool  # readonly
    CanFreezeRows: bool  # readonly
    CanManualIntegrate: bool  # readonly
    CanNavigateBag: bool  # readonly
    CanShowManualIntegrateWindow: bool  # readonly
    CanUnfreezePanes: bool  # readonly
    CanUpdateRetentionTimes: bool  # readonly
    CanZeroPeakSelectedPanes: bool  # readonly
    ChromSpecProperties: Agilent.MassHunter.Quantitative.UIModel.IChromSpecProperties
    HasData: bool  # readonly
    HasNextReviewItem: bool  # readonly
    HasPreviousReviewItem: bool  # readonly
    LinkAllXAxes: bool
    LinkAllYAxes: bool
    LinkXAxes: bool
    LinkYAxes: bool
    LinkYAxesVertically: bool
    ManualIntegrating: bool  # readonly
    SetupGraphicsContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SetupGraphicsContext
    )
    SynchronizeNavigation: bool
    UpdatingMethod: bool  # readonly

    def FreezePanes(self) -> None: ...
    def MISplitRight(self) -> None: ...
    def FreezeRows(self) -> None: ...
    def SelectAllPanes(self) -> None: ...
    def GetActivePaneScale(
        self, minx: float, maxx: float, miny: float, maxy: float
    ) -> bool: ...
    def MIMergeLeft(self) -> None: ...
    def ShowManualIntegrateWindow(self) -> None: ...
    def GotoPrevOutlierPane(self) -> bool: ...
    def MIDropBaseline(self) -> None: ...
    def GetAutoScaleRangeX(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def UpdateData(self) -> None: ...
    def NavigateBag(self) -> None: ...
    def MovePreviousReviewItem(self) -> None: ...
    def MIApplyISTDRTsToTargets(self) -> None: ...
    def AutoScaleAllPanes(self) -> None: ...
    def MIApplyTargetRTsToQualifiers(self) -> None: ...
    def MISplitLeft(self) -> None: ...
    def ZeroPeakSelectedPanes(self) -> None: ...
    def MoveNextReviewItem(self) -> None: ...
    def SetDimension(self, rows: int, cols: int, updatePaneData: bool) -> None: ...
    def UpdateRetentionTimes(self) -> None: ...
    def SetupGraphicsByParameters(
        self,
        sampleFilter: str,
        sampleOrder: str,
        compoundFilter: str,
        compoundOrder: str,
        organizeRows: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.OrganizeType,
        overlay: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay,
        reviewMode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewMode,
        wrapRows: bool,
        baselines: Optional[bool],
        fillPeaks: Optional[bool],
        normalize: Optional[bool],
        uncertainty: Optional[bool],
    ) -> None: ...
    def UnfreezePanes(self) -> None: ...
    def ExtractGraphics(self) -> None: ...
    def ClearManualIntegration(self) -> None: ...
    def CreatePropertyPages(self) -> List[IPropertyPage]: ...
    def CreateFillPeakBrush(
        self,
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        series: int,
        peakIndex: int,
        color: System.Drawing.Color,
    ) -> System.Drawing.Brush: ...
    def GotoNextOutlierPane(self) -> bool: ...
    def GetSelectedSamples(self) -> List[SampleRowId]: ...
    def MISnapBaseline(self) -> None: ...
    def ExtractAndManualIntegrate(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> None: ...
    def InitConfiguration(self) -> None: ...
    def MIMergeRight(self) -> None: ...
    def MoveReviewItem(self, index: int) -> None: ...
    def EndManualIntegrate(self) -> None: ...
    def FreezeColumns(self) -> None: ...
    def FitToPeak(self) -> None: ...
    def SetManualScaleY(self, miny: float, maxy: float) -> None: ...
    def ManualIntegrate(self) -> None: ...
    def FitToCalibrationLevel(self, lowest: bool) -> None: ...
    def CopyPage(self) -> None: ...
    def ClearAllPanes(self) -> None: ...
    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def FitToPeakHeight(self) -> None: ...
    def NormalizeChanged(self) -> None: ...
    def CopySelectedPane(self) -> None: ...
    def EnsureInitializePanesInPage(self, startRow: int, startCol: int) -> None: ...
    def AutoScale(self) -> None: ...
    def GetSelectedCompounds(self) -> List[TargetCompoundRowId]: ...

    DisplayDimensionChanged: System.EventHandler  # Event
    GraphicsLayoutChanged: System.EventHandler  # Event
    InitializePanesEnd: System.EventHandler  # Event
    InitializePanesProgress: System.EventHandler[ProgressEventArgs]  # Event
    InitializePanesStart: System.EventHandler  # Event

class CagWindow(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    Agilent.MassHunter.Quantitative.UIModel.ICagWindow,
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

    AddInManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.AddInManager
    )  # readonly
    ChromatogramControl: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CagViewControl
    )  # readonly
    DataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator  # readonly
    PresentationState: (
        Agilent.MassHunter.Quantitative.UIModel.IPresentationState
    )  # readonly
    SetupGraphicsContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SetupGraphicsContext
    )  # readonly
    ToolbarsManager: IToolbarsManager  # readonly

    def GetAddInManager(self) -> T: ...
    def Initialize(
        self,
        dataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator,
        uiState: IUIState,
        chromSpecProperties: Agilent.MassHunter.Quantitative.UIModel.IChromSpecProperties,
    ) -> None: ...
    def ShowSetupGraphicsDialog(self) -> None: ...
    def ShowHelpIndex(self) -> None: ...
    def GetSelectedCompounds(self) -> List[TargetCompoundRowId]: ...
    def GetSelectedSamples(self) -> List[SampleRowId]: ...
    def GetChromatogramControl(self) -> T: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def SetCurrentLayoutAsDefault(self) -> None: ...
    def DeleteDefaultLayoutFile(self) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def GetSetupGraphicsContext(self) -> T: ...
    def GetToolbar(self, paneId: str, id: str) -> IToolbar: ...
    def ShowHelpSearch(self) -> None: ...
    def ShowHelpContents(self) -> None: ...
    def LoadDefaultLayout(self, loadAllSamplesCompounds: bool) -> bool: ...

class Config:  # Class
    BackColor: System.Drawing.Color  # static
    DefaultShowManualIntegrationHandles: bool  # static # readonly
    SettingsSection: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CagSettingsSection
    )  # static # readonly

class DefaultEventManipulator(
    DefaultEventManipulatorBase,
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
):  # Class
    def __init__(
        self, context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext
    ) -> None: ...
    def OnDoubleClick(self, sender: Any, e: System.EventArgs) -> None: ...

class ExtractTICFromBatch(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ExtractorBase
):  # Class
    def __init__(
        self, index: int, state: PresentationState, batchId: int, sampleId: int
    ) -> None: ...

    RowId: RowIdBase  # readonly

    def Extract(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SetupGraphicsContext,
        extractSignals: bool,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SeriesDataBase
    ): ...

class ExtractorBase:  # Class
    AnnotationFormat: str
    Index: int  # readonly
    RowId: RowIdBase  # readonly

    def Extract(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SetupGraphicsContext,
        extractSignals: bool,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SeriesDataBase
    ): ...

class ExtractorCompoundChromatogram(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ExtractorBase
):  # Class
    def __init__(
        self, index: int, batchId: int, sampleId: int, compoundId: int
    ) -> None: ...

    CompoundMathChild: bool
    RowId: RowIdBase  # readonly

    def Extract(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SetupGraphicsContext,
        extractSignals: bool,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SeriesDataBase
    ): ...

class ExtractorCompoundMath(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ExtractorCompoundChromatogram
):  # Class
    def __init__(
        self, index: int, batchId: int, sampleId: int, compoundId: int
    ) -> None: ...
    def Extract(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SetupGraphicsContext,
        extractSignals: bool,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SeriesDataBase
    ): ...

class ExtractorQualifierChromatogram(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ExtractorBase
):  # Class
    def __init__(
        self, index: int, batchId: int, sampleId: int, compoundId: int, qualifierId: int
    ) -> None: ...

    RowId: RowIdBase  # readonly

    def Extract(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SetupGraphicsContext,
        extractSignals: bool,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SeriesDataBase
    ): ...

class FitMode(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    AutoScale: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.FitMode
    ) = ...  # static # readonly
    FitToHighestLevel: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.FitMode
    ) = ...  # static # readonly
    FitToLowestLevel: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.FitMode
    ) = ...  # static # readonly
    FitToPeak: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.FitMode
    ) = ...  # static # readonly
    FitToPeakHeight: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.FitMode
    ) = ...  # static # readonly
    ManualYScale: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.FitMode
    ) = ...  # static # readonly

class ManualIntegrateControl(
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ICagViewControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.ComponentModel.ISupportInitialize,
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
    Agilent.MassSpectrometry.GUI.Plot.PlotControl,
):  # Class
    def __init__(self) -> None: ...

    SetupGraphicsContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SetupGraphicsContext
    )  # readonly

    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def UpdateData(self) -> None: ...

class ManualIntegrateDialog(
    System.Windows.Forms.Layout.IArrangedElement,
    IToolHandler,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.Form,
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
    def Execute(self, tool: ITool, objUIState: Any) -> None: ...
    def SetState(self, tool: ITool, objUiState: Any) -> None: ...

class ManualScaleYDialog(
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
    def __init__(self, control: ICompoundsAtAGlance) -> None: ...

class OrganizeType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Compounds: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.OrganizeType
    ) = ...  # static # readonly
    Samples: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.OrganizeType
    ) = ...  # static # readonly

class Overlay(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    CompoundGroups: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    ) = ...  # static # readonly
    Compounds: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    ) = ...  # static # readonly
    ISTD: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    ) = ...  # static # readonly
    MatrixSpike: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    ) = ...  # static # readonly
    Qualifiers: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    ) = ...  # static # readonly
    SampleGroups: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    ) = ...  # static # readonly
    Samples: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    ) = ...  # static # readonly
    SeparateQualifiers: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    ) = ...  # static # readonly

class PaneDataExtractor:  # Class
    def __init__(self) -> None: ...

    ExtractorCount: int  # readonly
    RangeX: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange]
    RangeY: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange]
    Title: str

    def GetExtractor(
        self, index: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ExtractorBase
    ): ...
    def AddExtractor(
        self,
        extractor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ExtractorBase,
    ) -> None: ...

class Peak:  # Class
    @overload
    def __init__(self, peak: QuantitationDataSet.PeakRow, centerY: float) -> None: ...
    @overload
    def __init__(
        self, peak: QuantitationDataSet.PeakQualifierRow, centerY: float
    ) -> None: ...

    Area: Optional[float]  # readonly
    Base1End: Optional[float]  # readonly
    Base1Start: Optional[float]  # readonly
    Base2End: Optional[float]  # readonly
    Base2Start: Optional[float]  # readonly
    BaselineEndX: Optional[float]  # readonly
    BaselineEndY: Optional[float]  # readonly
    BaselineOffset: Optional[float]  # readonly
    BaselineStandardDeviation: Optional[float]  # readonly
    BaselineStartX: Optional[float]  # readonly
    BaselineStartY: Optional[float]  # readonly
    Center: float  # readonly
    CenterY: float  # readonly
    CompoundName: str  # readonly
    Height: Optional[float]  # readonly
    IsManualIntegrated: bool  # readonly
    IsPrimary: bool  # readonly
    PeakStatus: Agilent.MassSpectrometry.DataAnalysis.PeakStatus  # readonly
    RowId: RowIdBase  # readonly

class PeakAnnotationType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Area: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ) = ...  # static # readonly
    CalculatedConcentration: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ) = ...  # static # readonly
    DeltaRetentionTime: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ) = ...  # static # readonly
    FinalConcentration: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ) = ...  # static # readonly
    Height: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ) = ...  # static # readonly
    QValueComputed: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ) = ...  # static # readonly
    QualifierResponseRatio: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ) = ...  # static # readonly
    RetentionTime: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ) = ...  # static # readonly
    SignalToNoiseRatio: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ) = ...  # static # readonly

class PlotData(
    Agilent.MassSpectrometry.GUI.Plot.IMarkerData,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PlotDataBase,
    Agilent.MassSpectrometry.GUI.Plot.IPlotData,
    Agilent.MassSpectrometry.GUI.Plot.IPeakData,
):  # Class
    def __init__(
        self,
        control: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CagViewControl,
        extractor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PaneDataExtractor,
    ) -> None: ...

    Initialized: bool  # readonly
    PaneDataExtractor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PaneDataExtractor
    )  # readonly

    def Initialize(self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane) -> None: ...

class PlotDataBase:  # Class
    ...

class PresetLayout(System.Configuration.ConfigurationElement):  # Class
    def __init__(self) -> None: ...

    Baselines: Optional[bool]
    CompoundFilter: str
    CompoundOrder: str
    DimensionX: Optional[int]
    DimensionY: Optional[int]
    FillPeaks: Optional[bool]
    FitToHighestLevel: bool
    FitToLowestLevel: bool
    FitToPeak: bool
    FitToPeakHeight: bool
    LinkAllXAxes: bool
    LinkAllYAxes: bool
    LinkXAxes: bool
    LinkYAxes: bool
    MenuText: str
    Name: str
    Normalize: Optional[bool]
    OrganizeRows: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.OrganizeType
    )
    Outliers: str
    Overlay: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    )
    PeakAnnotations: str
    ReviewMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewMode
    )
    SampleFilter: str
    SampleOrder: str
    Separator: bool
    ShowPeakAnnotationNames: Optional[bool]
    ShowPeakAnnotationUnits: Optional[bool]
    UncertaintyBand: Optional[bool]
    WrapRows: bool

class PresetLayoutCollection(
    Iterable[Any], System.Configuration.ConfigurationElementCollection, Sequence[Any]
):  # Class
    def __init__(self) -> None: ...
    def __getitem__(
        self, index: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PresetLayout
    ): ...

class PropPage(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    IPropertyPage,
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
    def __init__(
        self,
        control: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CagViewControl,
    ) -> None: ...

class ReviewCompoundGroupItem(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewItem,
    IReviewItem,
):  # Class
    def __init__(self, dataset: BatchDataSet, groupName: str) -> None: ...
    def MatchCompound(self, rowId: TargetCompoundRowId) -> bool: ...
    def MatchSample(self, rowId: SampleRowId) -> bool: ...

class ReviewCompoundItem(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewItem,
    IReviewItem,
):  # Class
    def __init__(self, dataSet: BatchDataSet, rowId: TargetCompoundRowId) -> None: ...
    def MatchCompound(self, rowId: TargetCompoundRowId) -> bool: ...
    def MatchSample(self, rowId: SampleRowId) -> bool: ...

class ReviewItem(IReviewItem):  # Class
    def __init__(self) -> None: ...

    DisplayText: str

    def MatchCompound(self, rowId: TargetCompoundRowId) -> bool: ...
    def MatchSample(self, rowId: SampleRowId) -> bool: ...

class ReviewMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CompoundByCompound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewMode
    ) = ...  # static # readonly
    CompoundGroupByCompoundGroup: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewMode
    ) = ...  # static # readonly
    SampleBySample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewMode
    ) = ...  # static # readonly

class ReviewSampleItem(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewItem,
    IReviewItem,
):  # Class
    def __init__(self, dataSet: BatchDataSet, rowId: SampleRowId) -> None: ...
    def MatchCompound(self, rowId: TargetCompoundRowId) -> bool: ...
    def MatchSample(self, rowId: SampleRowId) -> bool: ...

class SeriesCompoundMath(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SeriesDataBase
):  # Class
    def __init__(
        self,
        extractor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ExtractorCompoundMath,
    ) -> None: ...

    MaxY: float  # readonly
    PlotMode: Agilent.MassSpectrometry.GUI.Plot.PlotModes  # readonly
    PointCount: int  # readonly

    def GetPoint(self, index: int, x: float, y: float) -> None: ...

class SeriesDataBase:  # Class
    Annotation: str
    Color: System.Drawing.Color
    Display: bool
    Extractor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ExtractorBase
    )  # readonly
    ManualIntegrated: bool
    MaxY: float  # readonly
    Outlier: bool
    OutlierMessage: str
    PeakCount: int  # readonly
    PlotMode: Agilent.MassSpectrometry.GUI.Plot.PlotModes  # readonly
    PointCount: int  # readonly
    Style: System.Drawing.Drawing2D.DashStyle
    Width: int

    def GetYFromX(self, x: float) -> Optional[float]: ...
    def AddPeak(
        self,
        peak: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Peak,
    ) -> None: ...
    def GetPeak(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Peak: ...
    def GetPoint(self, index: int, x: float, y: float) -> None: ...
    def FindIndex(self, x: float) -> int: ...
    def ClearPeaks(self) -> None: ...

class SeriesExceptionData(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SeriesDataBase
):  # Class
    def __init__(
        self,
        extractor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ExtractorBase,
        exception: System.Exception,
    ) -> None: ...

    Exception: System.Exception  # readonly
    MaxY: float  # readonly
    PlotMode: Agilent.MassSpectrometry.GUI.Plot.PlotModes  # readonly
    PointCount: int  # readonly

    def GetPoint(self, index: int, x: float, y: float) -> None: ...

class SeriesFXData(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.SeriesDataBase
):  # Class
    def __init__(
        self,
        extractor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ExtractorBase,
        data: Agilent.MassSpectrometry.DataAnalysis.IFXData,
    ) -> None: ...

    MaxY: float  # readonly
    PlotMode: Agilent.MassSpectrometry.GUI.Plot.PlotModes  # readonly
    PointCount: int  # readonly

    def GetPoint(self, index: int, x: float, y: float) -> None: ...

class SetupGraphicsContext(System.IDisposable):  # Class
    def __init__(
        self, dataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator
    ) -> None: ...

    ColumnCount: int  # readonly
    CompoundCount: int  # readonly
    Compounds: Iterable[TargetCompoundRowId]  # readonly
    CurrentReviewItemIndex: Optional[int]  # readonly
    DataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator  # readonly
    FillPeaks: bool
    Layout: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.CagLayout
    )  # readonly
    Normalize: bool
    Organize: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.OrganizeType
    )
    Outliers: Iterable[OutlierColumns]  # readonly
    Overlay: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.Overlay
    )
    PeakAnnotations: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PeakAnnotationType
    ]
    PresentationState: (
        Agilent.MassHunter.Quantitative.UIModel.IPresentationState
    )  # readonly
    QualifierInfoLabelType: QualifierInfoLabelType
    RecognitionWindowColor: System.Drawing.Color
    RecognitionWindowDashStyle: System.Drawing.Drawing2D.DashStyle
    ReferenceRTColor: System.Drawing.Color
    ReferenceRTDashStyle: System.Drawing.Drawing2D.DashStyle
    ReviewItemCount: int  # readonly
    ReviewMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewMode
    )
    RowCount: int  # readonly
    SampleCount: int  # readonly
    Samples: Iterable[SampleRowId]  # readonly
    ShowBaselines: bool
    ShowManualIntegrationHandles: bool
    ShowPeakAnnotationNames: bool
    ShowPeakAnnotationUnits: bool
    ShowRecognitionWindow: bool
    ShowReferenceRT: bool
    ShowUncertainBands: bool
    WrapMode: bool

    def AddAllSamplesAllCompounds(self) -> None: ...
    def AddCompounds(self, compounds: Iterable[TargetCompoundRowId]) -> None: ...
    def UpdateOutliers(self) -> None: ...
    def GetReviewItems(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.ReviewItem
    ]: ...
    def ClearCompounds(self) -> None: ...
    def SetOutliers(self, columns: Iterable[OutlierColumns]) -> None: ...
    def GetAvailableOutliers(self) -> Iterable[OutlierColumns]: ...
    def InitConfiguration(self) -> None: ...
    def MatchOutlier(
        self,
        relation: str,
        row: System.Data.DataRow,
        builder: System.Text.StringBuilder,
    ) -> bool: ...
    def ClearSamples(self) -> None: ...
    def Dispose(self) -> None: ...
    def AddSamples(self, samples: Iterable[SampleRowId]) -> None: ...
    def GetExtractor(
        self, row: int, col: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CompoundsAtAGlance.PaneDataExtractor
    ): ...
    def SetupExtractors(self) -> None: ...

class ToolHandlerChromatograms(IToolHandler):  # Class
    def __init__(self) -> None: ...

class ToolHandlerMain(IToolHandler, IToolBeforeDropdownHandler):  # Class
    def __init__(self) -> None: ...

    Ext_CagLayout: str = ...  # static # readonly

class ToolbarsManager(
    System.ComponentModel.ISupportInitialize,
    System.IDisposable,
    ToolbarsManagerBase,
    System.Windows.Forms.IMessageFilter,
    IToolbarsManager,
):  # Class
    def __init__(self, uiState: IUIState) -> None: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def RegisterScriptToolHandler(
        self, tool: str, module: str, setState: str, execute: str
    ) -> None: ...
