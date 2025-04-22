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
    Common,
    EicPeaks,
    Model,
    Properties,
    Query,
    Remoting,
    Report,
    ScriptIF,
    ScriptIFImpls,
    Tools,
)

# Discovered Generic TypeVars:
T = TypeVar("T")
from . import ComponentRowID, ExactMassRowID, SampleRowID, UnknownsAnalysisDataSet
from .Command import CommandContext, SetMethods
from .Common import LibrarySearchSite
from .Configuration import (
    ChromatogramSettings,
    IonPeaksSettings,
    PlotUserSettingsSectionBase,
    SpectrumSettings,
)
from .DataFile import DataFileBase
from .Model import (
    IAnalysisMessageGridView,
    IAnalysisMessageTableControl,
    IChromatogramControl,
    IChromatogramView,
    IComponentGridView,
    IComponentTableControl,
    IComponentTableView,
    IEicPeaksControl,
    IEicPeaksView,
    IExactMassGridView,
    IExactMassTableControl,
    IGridControlBase,
    IIonPeaksControl,
    IIonPeaksView,
    IIonPeakTableView,
    IIonPeakViewItem,
    IMainWindow,
    IPlotControlBase,
    ISampleGridView,
    ISampleTableControl,
    ISelectedRanges,
    ISpectrumControl,
    ISpectrumView,
    IStructureControl,
    IUIContext,
)
from .ScriptIF import ChromatogramViewMode, IUIState

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI

class AddInsDialog(
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
    def __init__(self, uiState: IUIState) -> None: ...

class AdvancedAuxiliaryControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
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
    def Initialize(self, uiContext: IUIContext, hasAccurateMass: bool) -> None: ...
    def DoApply(self, cmd: SetMethods) -> bool: ...
    def HasChanges(self) -> bool: ...
    def UpdateTable(self) -> None: ...
    def Default(self) -> None: ...

class AdvancedBlankSubtractionControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
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
    def Initialize(self, uiContext: IUIContext, hasAccurateMass: bool) -> None: ...
    def DoApply(self, cmd: SetMethods) -> bool: ...
    def HasChanges(self) -> bool: ...
    def UpdateTable(self) -> None: ...
    def Default(self) -> None: ...

class AdvancedDeconvolutionControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
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
    def Initialize(self, uiContext: IUIContext, hasAccurateMass: bool) -> None: ...
    def DoApply(self, cmd: SetMethods) -> bool: ...
    def HasChanges(self) -> bool: ...
    def UpdateTable(self) -> None: ...
    def Default(self) -> None: ...

class AdvancedIdentificationControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
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
    def Initialize(self, uiContext: IUIContext, hasAccurateMass: bool) -> None: ...
    def DoApply(self, cmd: SetMethods) -> bool: ...
    def HasChanges(self) -> bool: ...
    def UpdateTable(self) -> None: ...
    def Default(self) -> None: ...

class AdvancedLibrarySearchControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
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
    def Initialize(self, uiContext: IUIContext, hasAccurateMass: bool) -> None: ...
    def DoApply(self, cmd: SetMethods) -> bool: ...
    def HasChanges(self) -> bool: ...
    def UpdateTable(self) -> None: ...
    def Default(self) -> None: ...

class AdvancedTargetMatchControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
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
    def DoApply(self, cmd: SetMethods) -> bool: ...
    def Initialize(self, uiContext: IUIContext, hasAccurateMass: bool) -> None: ...
    def HasChanges(self) -> bool: ...
    def Default(self) -> None: ...

class AlternativeExactMassDialog(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class AlternativeExactMassModel(System.Windows.DependencyObject):  # Class
    def __init__(self, uiContext: IUIContext) -> None: ...

    CandidatesProperty: System.Windows.DependencyProperty  # static # readonly
    MassSourceProperty: System.Windows.DependencyProperty  # static # readonly
    ParentFormulaProperty: System.Windows.DependencyProperty  # static # readonly

    Candidates: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ExactMassCandidate
    ]
    MassSource: Optional[float]
    ParentFormula: str

    def Initialize(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        exactMassID: int,
    ) -> None: ...
    def Apply(self, parent: System.Windows.Forms.IWin32Window) -> bool: ...

class AnalysisFileDialog(System.IDisposable):  # Class
    def __init__(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.AnalysisFileDialogMode,
    ) -> None: ...

    AllowAuditTrail: bool
    AllowReadOnly: bool
    AnalysisFile: str  # readonly
    AuditTrail: bool
    AuditTrailCheckboxEnabled: bool
    BatchFolder: str  # readonly
    HelpFile: str
    HelpTopicId: int
    InitialDir: str
    ReadOnly: bool

    def Dispose(self) -> None: ...
    def ShowDialog(self, parent: System.Windows.Forms.IWin32Window) -> bool: ...

class AnalysisFileDialogMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    New: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.AnalysisFileDialogMode
    ) = ...  # static # readonly
    Open: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.AnalysisFileDialogMode
    ) = ...  # static # readonly
    SaveAs: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.AnalysisFileDialogMode
    ) = ...  # static # readonly

class AnalysisMessageGridView(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    IAnalysisMessageGridView,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.ComponentModel.ISupportInitialize,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
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

    DataGridView: System.Windows.Forms.DataGridView  # readonly

    def Initialize(self, parent: IMainWindow, uiContext: IUIContext) -> None: ...

class AnalysisMessageTableControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    IAnalysisMessageTableControl,
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

    AnalysisMessageGridView: IAnalysisMessageGridView  # readonly

class AppContext(System.Windows.Forms.ApplicationContext, System.IDisposable):  # Class
    def __init__(self) -> None: ...

    IsDisposed: bool  # readonly
    UIState: IUIState  # readonly

    def Initialize(
        self,
        initInfo: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.AppInitInfo,
    ) -> None: ...
    @overload
    @staticmethod
    def ShowErrorMessage(
        ex: System.Exception, mainForm: IMainWindow, console: bool
    ) -> None: ...
    @overload
    @staticmethod
    def ShowErrorMessage(
        message: str, mainForm: IMainWindow, console: bool
    ) -> None: ...
    @staticmethod
    def InitCulture(culture: str) -> None: ...
    @staticmethod
    def GetExceptionMesage(ex: System.Exception) -> str: ...
    @staticmethod
    def InitSplash() -> (
        Agilent.MassHunter.Quantitative.Controls.SplashScreen.SplashScreenModel
    ): ...

class AppInitInfo:  # Class
    def __init__(self) -> None: ...

    AccountName: str
    AccurateMassExtension: bool
    AnalysisFile: str
    ApplicationService: str
    CommandLog: bool
    ConnectionTicket: str
    Console: bool
    Constants: List[str]
    Domain: str
    NoLogo: bool
    Password: System.Security.SecureString
    RemoteServer: str
    ScriptFiles: List[str]
    Server: str
    User: str

class ChooseDirectoryCell(
    System.IDisposable, System.ICloneable, System.Windows.Forms.DataGridViewTextBoxCell
):  # Class
    def __init__(self) -> None: ...
    def PositionEditingControl(
        self,
        setLocation: bool,
        setSize: bool,
        cellBounds: System.Drawing.Rectangle,
        cellClip: System.Drawing.Rectangle,
        cellStyle: System.Windows.Forms.DataGridViewCellStyle,
        singleVerticalBorderAdded: bool,
        singleHorizontalBorderAdded: bool,
        isFirstDisplayedColumn: bool,
        isFirstDisplayedRow: bool,
    ) -> None: ...

class ChooseLibraryFileCell(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ChooseDirectoryCell,
    System.IDisposable,
    System.ICloneable,
):  # Class
    def __init__(self) -> None: ...

class ChooseLibraryPathCell(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ChooseDirectoryCell,
    System.IDisposable,
    System.ICloneable,
):  # Class
    def __init__(self) -> None: ...

class ChromatogramControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    IChromatogramControl,
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

    ChromatogramView: IChromatogramView  # readonly

class ChromatogramDefaultEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.DefaultEventManipulatorBase,
):  # Class
    def __init__(
        self,
        uiContext: IUIContext,
        context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext,
    ) -> None: ...
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...

class ChromatogramSelectRangeEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.DefaultEventManipulatorBase,
):  # Class
    def __init__(
        self,
        uiContext: IUIContext,
        context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext,
    ) -> None: ...
    def OnDragEnd(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...
    def OnEnd(self) -> None: ...
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...

class ChromatogramSettingsControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage,
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
        self, view: IChromatogramView, settings: ChromatogramSettings
    ) -> None: ...

class ChromatogramView(
    System.Windows.Forms.ISupportOleDropSource,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.PlotControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.IComponent,
    System.Windows.Forms.IDropTarget,
    IChromatogramView,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.IWin32Window,
    IPlotControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
):  # Class
    def __init__(self) -> None: ...

    CanAutoScaleXY: bool  # readonly
    ChromatogramViewMode: ChromatogramViewMode
    Settings: ChromatogramSettings  # readonly
    ShowComponents: bool
    ShowEics: bool
    ShowSelectedComponents: bool
    ShowTic: bool
    UIContext: IUIContext  # readonly
    _PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly

    def Initialize(self, context: IUIContext) -> None: ...
    def AutoScaleY(self) -> None: ...
    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def UpdateSettings(self) -> None: ...
    @overload
    def DrawPaneTo(
        self,
        graphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        row: int,
        col: int,
        left: int,
        top: int,
        width: int,
        height: int,
        xrange: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
        yrange: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
    ) -> None: ...
    @overload
    def DrawPaneTo(
        self,
        graphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        row: int,
        col: int,
        left: int,
        top: int,
        width: int,
        height: int,
    ) -> None: ...
    def UpdatePeakLabels(self) -> None: ...
    def UpdateSeriesVisibility(self) -> None: ...
    def AutoScaleXY(self) -> None: ...
    def UpdatePeakLabelSettings(self) -> None: ...

class ChromatogramWalkEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.DefaultEventManipulatorBase,
):  # Class
    def __init__(
        self,
        uiContext: IUIContext,
        context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext,
    ) -> None: ...
    def OnMouseDown(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnEnd(self) -> None: ...
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnKeyDown(self, sender: Any, e: System.Windows.Forms.KeyEventArgs) -> None: ...
    def OnDragEnd(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...

class ColumnsDialog(
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
        columns: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ColumnsDialogColumn
        ],
        visibleColumns: List[str],
        defaultVisibleColumns: List[str],
    ) -> None: ...
    def GetVisibleColumns(self) -> List[str]: ...

class ColumnsDialogColumn:  # Class
    def __init__(self, column: str, displayName: str, category: str) -> None: ...

    Category: str  # readonly
    Column: str  # readonly
    DisplayName: str  # readonly

    def ToString(self) -> str: ...

class CommandLine:  # Class
    def __init__(self) -> None: ...

    AccountName: str
    AnalysisFile: str
    ApplicationService: str
    CommandLog: bool
    ConnectionTicket: str
    Culture: str
    DefineConstants: List[str]
    Domain: str
    EncryptedPassword: str
    Help: bool
    Password: str
    RemoteServer: str
    ScriptFiles: List[str]
    Server: str
    User: str
    _Password: System.Security.SecureString  # readonly

class ComponentFilter(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    All: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentFilter = (
        ...
    )  # static # readonly
    BackgroundSubtracted: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentFilter
    ) = ...  # static # readonly
    Hit: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentFilter = (
        ...
    )  # static # readonly
    ManualComponents: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentFilter
    ) = ...  # static # readonly
    NonHit: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentFilter
    ) = ...  # static # readonly
    NonTarget: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentFilter
    ) = ...  # static # readonly
    Target: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentFilter
    ) = ...  # static # readonly

class ComponentGridView(
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.IComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.IWin32Window,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    System.ComponentModel.ISupportInitialize,
    IComponentGridView,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    IGridControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
):  # Class
    def __init__(self) -> None: ...

    CanDeleteComponentsHits: bool  # readonly
    CanSetBestHits: bool  # readonly
    DataGridView: System.Windows.Forms.DataGridView  # readonly
    SelectedComponentBackColor: System.Drawing.Color
    SelectedComponentForeColor: System.Drawing.Color

    def Initialize(self, uiContext: IUIContext) -> None: ...
    def ExportTableToLibrary(
        self,
        allComponents: bool,
        autoCompoundNames: bool,
        nonHitPrefix: str,
        nonHitAddIndex: bool,
    ) -> None: ...
    def SetBestHits(self) -> None: ...
    def GetVisibleColumns(self) -> List[str]: ...
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
    def SelectNearestComponent(self, rt: float) -> None: ...

class ComponentHitID(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentHitID
    ]
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: Optional[int],
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    HitID: Optional[int]  # readonly
    SampleID: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self,
        other: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentHitID,
    ) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class ComponentHitIDs(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentHitID: ...
    def IsComponentSelected(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int, componentID: int
    ) -> bool: ...
    def GetSelectedCompoundHitID(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentHitID: ...
    def Clear(self) -> None: ...
    def Select(
        self,
        selection: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentHitID
        ],
        clear: bool,
    ) -> None: ...
    def Dispose(self) -> None: ...

class ComponentSpectrum:  # Class
    @overload
    def __init__(self, crow: UnknownsAnalysisDataSet.ComponentRow) -> None: ...
    @overload
    def __init__(self, arrayX: str, arrayY: str) -> None: ...
    def FindAbundance(self, x: float) -> float: ...

class ComponentTableControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    IComponentTableControl,
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

    ComponentGridView: IComponentGridView  # readonly
    SelectedComponentBackColor: System.Drawing.Color
    SelectedComponentForeColor: System.Drawing.Color

class ComponentTableView(System.IDisposable, IComponentTableView):  # Class
    def __init__(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
    ) -> None: ...

    BestHitsOnly: bool
    BestPrimaryHitsOnly: bool
    BlankSubtractedHits: bool
    Count: int  # readonly
    Filter: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentFilter
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentHitID: ...
    PrimaryHitsOnly: bool

    def GetWhereClause(self) -> str: ...
    def GetCount(
        self,
        batchId: int,
        sampleId: int,
        filter: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentFilter,
        blankSubtracted: bool,
        bestHitsOnly: bool,
        primaryHitsOnly: bool,
    ) -> int: ...
    def Dispose(self) -> None: ...

    TableChanged: System.EventHandler  # Event

class DataGridViewBase(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.DataGridView,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
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
    CanCopy: bool  # readonly
    CanSetColumnFormat: bool  # readonly

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
    def SetColumnFormat(self) -> None: ...

class DeconvolutionControl(
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
    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
        batchID: int,
        sampleID: int,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def ApplyToAllSamples(
        self, samples: UnknownsAnalysisDataSet.SampleDataTable, cmd: SetMethods
    ) -> bool: ...
    def Default(self) -> None: ...
    def Apply(self, cmd: SetMethods) -> bool: ...

class DrawPeakLabelsX(
    Agilent.MassSpectrometry.GUI.Plot.ICustomDrawPeakLabelsEx
):  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def _MeasureLabel(
        plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane,
        font: System.Drawing.Font,
        text: str,
        x: float,
        y: float,
        series: int,
        peakIndex: int,
    ) -> System.Drawing.RectangleF: ...
    def DrawLabel(
        self,
        plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane,
        font: System.Drawing.Font,
        rect: System.Drawing.RectangleF,
        color: System.Drawing.Color,
        text: str,
        x: float,
        y: float,
        series: int,
        peakIndex: int,
    ) -> None: ...
    def MeasureLabel(
        self,
        plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane,
        font: System.Drawing.Font,
        text: str,
        x: float,
        y: float,
        series: int,
        peakIndex: int,
    ) -> System.Drawing.RectangleF: ...

class EicPeaksControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    IEicPeaksControl,
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

    EicPeaksView: IEicPeaksView  # readonly

class EicPeaksView(
    System.Windows.Forms.ISupportOleDropSource,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.PlotControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.IComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.IWin32Window,
    IPlotControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    IEicPeaksView,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
):  # Class
    def __init__(self) -> None: ...

    CanAutoScaleXY: bool  # readonly
    _PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly

    def Initialize(self, uiContext: IUIContext, mainWindow: IMainWindow) -> None: ...
    def UpdateSettings(self) -> None: ...
    def AutoScaleXY(self) -> None: ...

class ExactMassCandidate(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        model: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.AlternativeExactMassModel,
    ) -> None: ...

    Abundance: float
    Charge: int
    ExactMass: float
    FragmentFormula: str
    IsSelectedMass: bool
    MassDeltaMda: float
    MassDeltaPpm: float
    RelativeAbundance: float

class ExactMassGridView(
    System.Windows.Forms.ISupportOleDropSource,
    IExactMassGridView,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.IComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.IWin32Window,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    IGridControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
):  # Class
    def __init__(self) -> None: ...

    DataGridView: System.Windows.Forms.DataGridView  # readonly

    def CanShowAlternativeExactMassDialog(self) -> bool: ...
    def Initialize(self, mainWindow: IMainWindow) -> None: ...
    def ShowAlternativeExactMassDialog(self) -> None: ...
    def ShowColumnsDialog(self) -> None: ...

class ExactMassIDs(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly
    def __getitem__(self, index: int) -> ExactMassRowID: ...
    def Clear(self) -> None: ...
    def Dispose(self) -> None: ...
    def Select(self, selection: Iterable[ExactMassRowID], clear: bool) -> None: ...

class ExactMassTableControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    IExactMassTableControl,
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

    ExactMassGridView: IExactMassGridView  # readonly

class ExitCode(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    ErrorConfiguration: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ExitCode
    ) = ...  # static # readonly
    ErrorGeneral: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ExitCode
    ) = ...  # static # readonly
    ErrorUnknown: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ExitCode
    ) = ...  # static # readonly
    NoError: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ExitCode = (
        ...
    )  # static # readonly

class Expander(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Panel,
    System.Windows.Forms.Layout.IArrangedElement,
):  # Class
    def __init__(self) -> None: ...

    IsExpanded: bool
    Text: str

    IsExpandedChanged: System.EventHandler  # Event

class ExportLibrary(System.IDisposable):  # Class
    def __init__(
        self,
        view: System.Windows.Forms.DataGridView,
        allComponents: bool,
        autoCompoundNames: bool,
        nonHitCompoundNamesPrefix: str,
        nonHitCompoundNamesAddIndex: bool,
        context: CommandContext,
    ) -> None: ...
    def DoExport(self) -> None: ...
    def Dispose(self) -> None: ...

class ExportQuantMethod(System.IDisposable):  # Class
    def __init__(
        self,
        view: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentGridView,
        destination: str,
        allComponents: bool,
        autoCompundNames: bool,
        prefix: str,
        addIndex: bool,
        ionMode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodFromLibraryIonMode,
        numQualifiers: int,
    ) -> None: ...
    def DoExport(self) -> None: ...
    def Dispose(self) -> None: ...

class GridUtils:  # Class
    @staticmethod
    def GetHeaderText(table: str, column: str) -> str: ...
    @staticmethod
    def GetEnumTypeFromColumn(tableName: str, columnName: str) -> System.Type: ...
    @staticmethod
    def TranslateEnumValue(enumType: System.Type, value_: str) -> str: ...

class HelpUtils:  # Class
    @staticmethod
    def ShowHelp(isWPF: bool, html: str) -> None: ...

class HitGridView(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
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
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
    ) -> None: ...

class HitTableControl(
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

    HitGridView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.HitGridView
    )  # readonly

class IdentificationControl(
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
    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
        batchID: int,
        sampleID: int,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def ApplyToAllSamples(
        self, samples: UnknownsAnalysisDataSet.SampleDataTable, cmd: SetMethods
    ) -> bool: ...
    def Default(self) -> None: ...
    def Apply(self, cmd: SetMethods) -> bool: ...

class IonPeakTableView(System.IDisposable, IIonPeakTableView):  # Class
    def __init__(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
    ) -> None: ...

    Count: int  # readonly
    def __getitem__(self, index: int) -> IIonPeakViewItem: ...
    def FindItem(self, mz: float) -> int: ...
    def ShowDefaultIons(self) -> None: ...
    def ToggleVisible(self, index: int) -> bool: ...
    def AddIon(self, mz: float) -> None: ...
    def FindNearestItem(self, mz: float) -> int: ...
    def Clear(self) -> None: ...
    def CountVisibleItems(self) -> int: ...
    def UpdateColors(self) -> None: ...
    def Dispose(self) -> None: ...

    VisibleIonPeaksChanged: System.EventHandler  # Event

class IonPeakViewItem(IIonPeakViewItem):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
        mz: float,
        abundance: float,
    ) -> None: ...

    Abundance: float  # readonly
    BatchID: int  # readonly
    Color: System.Drawing.Color
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    IonPeakID: int  # readonly
    MZ: float  # readonly
    SampleID: int  # readonly
    Visible: bool  # readonly

class IonPeaksControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    IIonPeaksControl,
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

    IonPeaksView: IIonPeaksView  # readonly

class IonPeaksSettingsControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage,
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
    def __init__(self, view: IIonPeaksView, settings: IonPeaksSettings) -> None: ...

class IonPeaksView(
    System.Windows.Forms.ISupportOleDropSource,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.PlotControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.IComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.IWin32Window,
    IIonPeaksView,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    System.ComponentModel.ISupportInitialize,
    IPlotControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
):  # Class
    def __init__(self) -> None: ...

    CanAutoScaleXY: bool  # readonly
    ComponentSeries: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.PlotSeriesBase
    )  # readonly
    Settings: IonPeaksSettings  # readonly
    ShowComponent: bool
    ShowLabels: bool
    ShowTIC: bool
    UIContext: IUIContext  # readonly
    _PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly

    def Initialize(self, uiContext: IUIContext) -> None: ...
    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def BuildLabels(
        self, g: Agilent.MassSpectrometry.GUI.Plot.IGraphics, font: System.Drawing.Font
    ) -> None: ...
    def UpdateSettings(self) -> None: ...
    def UpdatePane(self) -> None: ...
    def AutoScaleXY(self) -> None: ...

class LibrarySearchControl(
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
    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def ApplyToAllSamples(
        self, samples: UnknownsAnalysisDataSet.SampleDataTable, cmd: SetMethods
    ) -> bool: ...
    def Default(self) -> None: ...
    def Apply(self, cmd: SetMethods) -> bool: ...

class MainForm(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    IMainWindow,
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
    def __init__(self, context: CommandContext) -> None: ...

    ActivePane: str  # readonly
    AddInManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.AddInManager
    )  # readonly
    AnalysisMessageTableControl: IAnalysisMessageTableControl  # readonly
    ChromatogramControl: IChromatogramControl  # readonly
    ComponentTableControl: IComponentTableControl  # readonly
    DockManager: Infragistics.Win.UltraWinDock.UltraDockManager  # readonly
    EicPeaksControl: IEicPeaksControl  # readonly
    ExactMassTableControl: IExactMassTableControl  # readonly
    IonPeaksControl: IIonPeaksControl  # readonly
    SampleTableControl: ISampleTableControl  # readonly
    ScriptControl: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.ScriptControl
    )  # readonly
    SpectrumControl: ISpectrumControl  # readonly
    StructureControl: IStructureControl  # readonly
    Title: str
    ToolManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager
    )  # readonly
    UIContext: IUIContext  # readonly
    UIState: IUIState  # readonly

    def Layout4(self) -> None: ...
    def ActivateWindow(self) -> None: ...
    def Layout6(self) -> None: ...
    def DefaultLayout(self) -> None: ...
    def Layout1(self) -> None: ...
    def Layout3(self) -> None: ...
    def Layout2(self) -> None: ...
    @staticmethod
    def AppendGridLayouts(
        doc: System.Xml.XmlDocument,
        parent: System.Xml.XmlElement,
        name: str,
        grid: System.Windows.Forms.DataGridView,
    ) -> None: ...
    def Layout7(self) -> None: ...
    @staticmethod
    def LoadGridLayouts(
        nav: System.Xml.XPath.XPathNavigator, view: System.Windows.Forms.DataGridView
    ) -> None: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def SetLayout(self, layout: int) -> None: ...
    def SetPaneVisible(self, key: str, visible: bool) -> None: ...
    def Close(self, forceClose: bool) -> None: ...
    def IsPaneVisible(self, key: str) -> bool: ...
    def BeginInvoke(self, d: System.Delegate, parameters: List[Any]) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def ShowQuery(self, queryFile: str) -> None: ...
    def Layout5(self) -> None: ...

    PaneVisibleChanged: System.EventHandler  # Event

class MainWindowTitleHandler(System.IDisposable):  # Class
    def __init__(self, context: IUIContext, mainWindow: IMainWindow) -> None: ...
    def Dispose(self) -> None: ...
    def UpdateTitle(self) -> None: ...

class MethodAdvancedDialog(
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
    def __init__(self, uiContext: IUIContext) -> None: ...

    ShowStandard: bool  # readonly

class MethodControl(
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
    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
        batchID: int,
        sampleID: int,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def ApplyToAllSamples(self) -> bool: ...
    def Default(self) -> None: ...
    def Apply(self) -> None: ...

class MethodDialog(
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
    def __init__(self, uiContext: IUIContext) -> None: ...

    ShowAdvanced: bool  # readonly

class MethodPane(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Auxiliary: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.MethodPane
    ) = ...  # static # readonly
    BlankSubtraction: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.MethodPane
    ) = ...  # static # readonly
    Deconvolution: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.MethodPane
    ) = ...  # static # readonly
    Identification: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.MethodPane
    ) = ...  # static # readonly
    LibrarySearch: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.MethodPane
    ) = ...  # static # readonly
    TargetMatch: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.MethodPane
    ) = ...  # static # readonly

class NumberFormatSingleColumnDialogWithAccurateMass(
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

    DefaultFormatPattern: Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ]
    DefaultFormatPatternAccurateMass: Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ]
    DefaultPrecision: Optional[int]
    DefaultPrecisionAccurateMass: Optional[int]
    FormatPattern: Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ]
    FormatPatternAccurateMass: Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ]
    HasAccurateMass: bool
    Precision: Optional[int]
    PrecisionAccurateMass: Optional[int]

    Apply: System.ComponentModel.CancelEventHandler  # Event

class PlotControlBase(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    Agilent.MassSpectrometry.GUI.Plot.PlotControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def PrintDialog(
        self,
        pageSettings: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PlotPageSettings,
    ) -> None: ...
    def DrawPaneTo(
        self,
        graphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        row: int,
        col: int,
        left: int,
        top: int,
        width: int,
        height: int,
    ) -> None: ...
    def SetContextMenuInternal(
        self, contextMenu: System.Windows.Forms.ContextMenuStrip
    ) -> None: ...
    def PrintPreview(
        self,
        pageSettings: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PlotPageSettings,
    ) -> None: ...
    @staticmethod
    def BuildLabel(label: str, unitLabel: str) -> str: ...

class PlotSeriesBase:  # Class
    def __init__(
        self,
        type: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType,
    ) -> None: ...

    Color: System.Drawing.Color
    Count: int  # readonly
    IsBar: bool  # readonly
    LineStyle: System.Drawing.Drawing2D.DashStyle
    PeakCount: int  # readonly
    PlotMode: Agilent.MassSpectrometry.GUI.Plot.PlotModes  # readonly
    SeriesType: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType
    )  # readonly
    ShiftX: int  # readonly
    ShiftY: int  # readonly
    StyleSegmentCount: int  # readonly
    Title: str  # readonly
    Visible: bool

    @overload
    def FindNearestIndex(self, x: float) -> int: ...
    @overload
    def FindNearestIndex(self, x: float, s: int, e: int) -> int: ...
    def DisplayPeakLabel(
        self, index: int, label: str, color: System.Drawing.Color
    ) -> bool: ...
    def CalcYFromX(self, px: float) -> float: ...
    def GetBarFillColor(self, index: int) -> System.Drawing.Color: ...
    def GetBarWidth(self, index: int) -> float: ...
    def PeakMarker(self, peak: int) -> Agilent.MassSpectrometry.GUI.Plot.Marker: ...
    def GetPeak(self, index: int, x: float, y: float) -> None: ...
    def GetPoint(self, index: int, x: float, y: float) -> None: ...
    def GetStyleSegment(
        self,
        index: int,
        startIndex: int,
        endIndex: int,
        color: System.Drawing.Color,
        style: System.Drawing.Drawing2D.DashStyle,
        width: int,
    ) -> None: ...
    def GetBarWidthIsVdc(self, index: int) -> bool: ...
    def GetBarLineColor(self, index: int) -> System.Drawing.Color: ...

class PlotSettingsController(System.IDisposable):  # Class
    def __init__(
        self,
        settings: PlotUserSettingsSectionBase,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        comboBoxBackgroundColor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.ColorComboBox,
        comboBoxForegroundColor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.ColorComboBox,
        comboBoxGridlinesColor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.ColorComboBox,
        comboBoxFontFamilies: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.FontFamilyComboBox,
        comboBoxFontSize: System.Windows.Forms.ComboBox,
        checkBoxFontBold: System.Windows.Forms.CheckBox,
        checkBoxFontItalic: System.Windows.Forms.CheckBox,
    ) -> None: ...
    def Initialize(self) -> None: ...
    def DoDefault(self) -> None: ...
    def Dispose(self) -> None: ...
    def Apply(self) -> None: ...

class PrinterSettingsSingleton(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    PrinterSettings: System.Drawing.Printing.PrinterSettings  # readonly

    def Dispose(self) -> None: ...

class SampleGridView(
    System.Windows.Forms.ISupportOleDropSource,
    ISampleGridView,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.IComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.IWin32Window,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    IGridControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
):  # Class
    def __init__(self) -> None: ...

    DataGridView: System.Windows.Forms.DataGridView  # readonly

    def Initialize(self, context: IUIContext) -> None: ...
    def StoreVisibleColumns(self) -> None: ...
    def ShowColumnsDialog(self) -> None: ...

class SampleTableControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    ISampleTableControl,
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

    SampleGridView: ISampleGridView  # readonly

class SelectedRange:  # Class
    def __init__(
        self, srid: SampleRowID, range: Agilent.MassSpectrometry.GUI.Plot.PlotRange
    ) -> None: ...

    Range: Agilent.MassSpectrometry.GUI.Plot.PlotRange  # readonly
    SampleRowID: SampleRowID  # readonly

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class SelectedRanges(System.IDisposable, ISelectedRanges):  # Class
    def __init__(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
    ) -> None: ...

    Count: int  # readonly
    HasTempSelection: bool  # readonly

    def GetTempSelection(
        self,
        srid: SampleRowID,
        range: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
    ) -> None: ...
    def SetTempSelection(
        self,
        srid: SampleRowID,
        range: Optional[Agilent.MassSpectrometry.GUI.Plot.PlotRange],
    ) -> None: ...
    def HitTest(
        self, batchID: int, sampleID: int, x: float
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
    def Dispose(self) -> None: ...
    def GetSamples(self) -> Iterable[SampleRowID]: ...

    SelectionChanged: System.EventHandler  # Event
    TempSelectionChanged: System.EventHandler  # Event

class SelectedSampleIDs(Iterable[Any], Iterable[SampleRowID]):  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly
    First: SampleRowID  # readonly

    def GetEnumerator(self) -> Iterator[SampleRowID]: ...
    def IsSampleSelected(self, batchID: int, sampleID: int) -> bool: ...
    def SelectSamples(self, samples: Iterable[SampleRowID]) -> bool: ...
    def Clear(self) -> None: ...
    def Dispose(self) -> None: ...

class SeriesType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Component: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType
    ) = ...  # static # readonly
    ComponentSpectrum: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType
    ) = ...  # static # readonly
    EIC: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType = (
        ...
    )  # static # readonly
    ExtractedSpectrum: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType
    ) = ...  # static # readonly
    IonPeak: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType = (
        ...
    )  # static # readonly
    LibrarySpectrum: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType
    ) = ...  # static # readonly
    PatternSpectrum: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType
    ) = ...  # static # readonly
    SIM: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType = (
        ...
    )  # static # readonly
    Signal: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType = (
        ...
    )  # static # readonly
    TIC: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.SeriesType = (
        ...
    )  # static # readonly

class SpectrumControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    ISpectrumControl,
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

    SpectrumView: ISpectrumView  # readonly

class SpectrumSettingsControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage,
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
    def __init__(self, view: ISpectrumView, settings: SpectrumSettings) -> None: ...

class SpectrumView(
    System.Windows.Forms.ISupportOleDropSource,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.PlotControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    ISpectrumView,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.IComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.IWin32Window,
    IPlotControlBase,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
):  # Class
    def __init__(self) -> None: ...

    CanAutoScaleXY: bool  # readonly
    CanCopy: bool  # readonly
    HeadToTailView: bool
    Settings: SpectrumSettings  # readonly
    ShowExtractedSpectrum: bool
    UIContext: IUIContext  # readonly
    _PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly

    def GetActiveObject(self) -> T: ...
    def Initialize(self, uiContext: IUIContext) -> None: ...
    def Copy(self) -> None: ...
    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def UpdateSettings(self) -> None: ...
    def DrawPaneTo(
        self,
        graphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        row: int,
        col: int,
        left: int,
        top: int,
        width: int,
        height: int,
    ) -> None: ...
    def GetAutoScaleRangeX(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetPreferredYRangeLimit(
        self, row: int, column: int
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def AutoScaleXY(self) -> None: ...

class SpectrumViewDefaultEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.DefaultEventManipulatorBase,
):  # Class
    def __init__(
        self, context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext
    ) -> None: ...
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseDoubleClick(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...

class StructureControl(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    IStructureControl,
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
    Control: System.Windows.Forms.Control  # readonly
    HasStructure: bool  # readonly

    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
    ) -> None: ...
    def Copy(self) -> None: ...
    def CreateMetafile(
        self, rect: System.Drawing.Rectangle, stream: System.IO.Stream
    ) -> System.Drawing.Imaging.Metafile: ...
    def DrawStructure(self, graphics: System.Drawing.Graphics) -> None: ...
    def DrawTo(
        self,
        graphics: System.Drawing.Graphics,
        color: System.Drawing.Color,
        rect: System.Drawing.Rectangle,
    ) -> None: ...

class TargetGridView(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.DataGridViewBase,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
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
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
    ) -> None: ...
    def ShowColumnsDialog(self) -> None: ...

class TargetMatchControl(
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
    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
        batchID: int,
        sampleID: int,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def ApplyToAllSamples(
        self, samples: UnknownsAnalysisDataSet.SampleDataTable, cmd: SetMethods
    ) -> bool: ...
    def Default(self) -> None: ...
    def Apply(self, cmd: SetMethods) -> bool: ...

class TargetTableControl(
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

    TargetGridView: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.TargetGridView
    )  # readonly

    def Initialize(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
    ) -> None: ...

class UIContext(System.IDisposable, IUIContext):  # Class
    def __init__(self, context: CommandContext) -> None: ...

    AccurateMassExtension: bool
    BlankComponent: ComponentRowID
    CommandContext: CommandContext  # readonly
    ComponentTableView: IComponentTableView  # readonly
    DataFile: DataFileBase  # readonly
    IonPeakTableView: IIonPeakTableView  # readonly
    IsWPF: bool
    LibrarySearchSite: LibrarySearchSite  # readonly
    SelectedComponentHitCount: int  # readonly
    SelectedExactMassCount: int  # readonly
    SelectedRanges: ISelectedRanges  # readonly
    SelectedSampleCount: int  # readonly
    SelectedSamples: Iterable[SampleRowID]  # readonly
    SelectingSamples: bool  # readonly
    SingleSelectedSampleRowID: SampleRowID  # readonly
    SynchronizeInvoke: System.ComponentModel.ISynchronizeInvoke  # readonly
    WalkingChromatogramRanges: ISelectedRanges  # readonly

    def IsComponentSelected(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int, componentID: int
    ) -> bool: ...
    def IdleInvoke(self, del_: System.Delegate, parameters: List[Any]) -> None: ...
    def GetSelectedExactMass(self, index: int) -> ExactMassRowID: ...
    def SelectSamples(self, selection: Iterable[SampleRowID]) -> None: ...
    def SelectComponentHits(
        self,
        selection: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentHitID
        ],
        clear: bool,
    ) -> None: ...
    def IsSelected(self, batchID: int, sampleID: int) -> bool: ...
    def GetSelectedComponentHitID(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ComponentHitID: ...
    def SelectExactMasses(
        self, rows: Iterable[ExactMassRowID], clear: bool
    ) -> None: ...
    def Dispose(self) -> None: ...

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

class WalkChromatogramRubberBand(
    Agilent.MassSpectrometry.EventManipulating.Model.IRubberBand,
    System.IDisposable,
    Agilent.MassSpectrometry.EventManipulating.RubberBand,
):  # Class
    def __init__(
        self,
        uiContext: IUIContext,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        startPoint: System.Drawing.Point,
        lineColor: System.Drawing.Color,
    ) -> None: ...

    LastRT: float  # readonly
    Pane: Agilent.MassSpectrometry.GUI.Plot.Pane  # readonly
    Series: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.PlotSeriesBase
    )  # readonly

    def MoveTo(
        self, ctrl: System.Windows.Forms.Control, point: System.Drawing.Point
    ) -> None: ...

class XRangeRubberBand(
    Agilent.MassSpectrometry.EventManipulating.Model.IRubberBand,
    System.IDisposable,
    Agilent.MassSpectrometry.EventManipulating.RubberBand,
):  # Class
    def __init__(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        startPoint: System.Drawing.Point,
        lineColor: System.Drawing.Color,
        fillColor: System.Drawing.Color,
    ) -> None: ...

class ts:  # Class
    TraceDebug: bool  # static # readonly
    TraceError: bool  # static # readonly
    TraceInfo: bool  # static # readonly
    TraceVerbose: bool  # static # readonly
    TraceWarning: bool  # static # readonly
