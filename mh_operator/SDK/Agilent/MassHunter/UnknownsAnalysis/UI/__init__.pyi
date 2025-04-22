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

from . import Controls

# Stubs for namespace: Agilent.MassHunter.UnknownsAnalysis.UI

class App(
    System.Windows.Application,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    @staticmethod
    def Main() -> None: ...

class CommandLine(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.CommandLine
):  # Class
    def __init__(self) -> None: ...

class MainWindow(
    System.Windows.Markup.IAddChild,
    Infragistics.Windows.Ribbon.XamRibbonWindow,
    System.Windows.Markup.IHaveResources,
    System.Windows.IInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.IFrameworkInputElement,
    Infragistics.Windows.Ribbon.IRibbonWindow,
    System.Windows.Media.Composition.DUCE.IResource,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IMainWindow,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.IWindowService,
    System.Windows.Forms.IWin32Window,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...

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
    Handle: System.IntPtr  # readonly
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
    ToolManager: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager
    )  # readonly
    UIContext: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext
    )  # readonly
    UIState: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState
    )  # readonly
    _UIState: Agilent.MassHunter.UnknownsAnalysis.UI.UIState  # readonly

    def Layout4(self) -> None: ...
    def ActivateWindow(self) -> None: ...
    def Layout6(self) -> None: ...
    def DefaultLayout(self) -> None: ...
    def Layout1(self) -> None: ...
    def Layout3(self) -> None: ...
    def Layout2(self) -> None: ...
    def Layout7(self) -> None: ...
    def SetLayout(self, layout: int) -> None: ...
    def SetPaneVisible(self, key: str, visible: bool) -> None: ...
    def LoadLayout(self, stream: System.IO.Stream) -> None: ...
    def InitializeComponent(self) -> None: ...
    def Close(self, forceClose: bool) -> None: ...
    def IsPaneVisible(self, key: str) -> bool: ...
    def BeginInvoke(self, d: System.Delegate, parameters: List[Any]) -> None: ...
    def SaveLayout(self, stream: System.IO.Stream) -> None: ...
    def ShowQuery(self, queryFile: str) -> None: ...
    def Invoke(self, d: System.Delegate, parameters: List[Any]) -> Any: ...
    def Layout5(self) -> None: ...

    PaneVisibleChanged: System.EventHandler  # Event

class ToolHandlerApplicationMenu(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        objState: Any,
    ) -> None: ...
    def SetState(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        objState: Any,
    ) -> None: ...

class ToolHandlerUnknownsWPF(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        objState: Any,
    ) -> None: ...
    def SetState(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        objState: Any,
    ) -> None: ...

class ToolIds:  # Class
    App_File_NewAnalysis: str = ...  # static # readonly
    App_File_OpenAnalysis: str = ...  # static # readonly
    App_File_SaveAnalysisAs: str = ...  # static # readonly
    UnknownsWPF_Analyze_All: str = ...  # static # readonly
    UnknownsWPF_Analyze_AllSamples: str = ...  # static # readonly
    UnknownsWPF_Analyze_Sample: str = ...  # static # readonly
    UnknownsWPF_ComponentsHits: str = ...  # static # readonly
    UnknownsWPF_Import: str = ...  # static # readonly
    UnknownsWPF_Method_Load: str = ...  # static # readonly
    UnknownsWPF_Samples: str = ...  # static # readonly

class ToolManager(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.ToolManagerBase,
):  # Class
    def __init__(
        self,
        ribbon: Infragistics.Windows.Ribbon.XamRibbon,
        uiState: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState,
    ) -> None: ...

    IUIState: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState
    )  # readonly

    def RegisterScriptToolHandler(
        self, id: str, module: str, setState: str, execute: str
    ) -> None: ...
    def ApplicationMenu2010SelectedTabItemChanged(self) -> None: ...
    def GetImage(self, image: str) -> System.Windows.Media.Imaging.BitmapSource: ...
    def GetApplicationMenu2010Content(self, category: str, id: str) -> Any: ...
    def GetToolTooltip(self, id: str) -> str: ...
    @staticmethod
    def _GetImage(image: str) -> System.Windows.Media.Imaging.BitmapSource: ...
    def ApplicationMenu2010Closed(self) -> None: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    @staticmethod
    def DelegateExecute(
        uiState: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        ID: str,
    ) -> None: ...
    @staticmethod
    def DelegateSetToolState(
        uiState: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        ID: str,
    ) -> None: ...
    @overload
    def GetToolCaption(self, id: str) -> str: ...
    @overload
    def GetToolCaption(
        self, id: str, culture: System.Globalization.CultureInfo
    ) -> str: ...

class UIState(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIFImpls.UIState,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState,
):  # Class
    def __init__(
        self, mainWindow: Agilent.MassHunter.UnknownsAnalysis.UI.MainWindow
    ) -> None: ...
