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

# Stubs for namespace: Agilent.MassHunter.UnknownsAnalysis.ComponentComparisonTable

class ComparisonItem:  # Class
    def __init__(self) -> None: ...

    Background: System.Windows.Media.Brush  # readonly
    ComponentHit1: (
        Agilent.MassHunter.UnknownsAnalysis.ComponentComparisonTable.ComponentHit
    )
    ComponentHit2: (
        Agilent.MassHunter.UnknownsAnalysis.ComponentComparisonTable.ComponentHit
    )
    RT: float  # readonly

class ComponentComparisonControl(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class ComponentComparisonWindow(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IWindowService,
    Infragistics.Windows.Ribbon.IRibbonWindow,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Animation.IAnimatable,
    System.ComponentModel.ISupportInitialize,
    Infragistics.Windows.Ribbon.XamRibbonWindow,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(
        self,
        mainWindow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IMainWindow,
    ) -> None: ...
    def Configure(self) -> None: ...
    def Export(self) -> None: ...
    def Refresh(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    @staticmethod
    def GetInstance(
        mainWindow: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IMainWindow,
    ) -> (
        Agilent.MassHunter.UnknownsAnalysis.ComponentComparisonTable.ComponentComparisonWindow
    ): ...

class ComponentHit:  # Class
    def __init__(self) -> None: ...

    Area: Optional[float]
    BatchID: int
    ComponentID: int
    CompoundName: str
    DataFile: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataFileBase
    )
    DeconvolutionMethodID: int
    HitID: Optional[int]
    IdentificationMethodID: Optional[int]
    LibraryEntryID: Optional[int]
    LibrarySearchMethodID: Optional[int]
    RetentionTime: float
    SampleID: int

class ConfigureModel(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self, model: Agilent.MassHunter.UnknownsAnalysis.ComponentComparisonTable.Model
    ) -> None: ...

    RTBinSize: float

class ConfigureWindow(
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
    def __init__(
        self,
        window: Agilent.MassHunter.UnknownsAnalysis.ComponentComparisonTable.ComponentComparisonWindow,
    ) -> None: ...
    def InitializeComponent(self) -> None: ...

class Model(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Model.IUIContext,
    ) -> None: ...

    CommandContext: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext
    )  # readonly
    FileName1: str
    FileName2: str
    Items: List[
        Agilent.MassHunter.UnknownsAnalysis.ComponentComparisonTable.ComparisonItem
    ]
    RTBinSize: float
    SampleName1: str
    SampleName2: str

    def Process(self) -> None: ...
    def Clean(self) -> None: ...

class ToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        uiState: Any,
    ) -> None: ...
    def SetState(
        self,
        toolState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolState,
        uiState: Any,
    ) -> None: ...

class ToolIds:  # Class
    ...

class ToolManager(
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolManager,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar.IToolbarsManager,
    Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.ToolManagerBase,
):  # Class
    def __init__(
        self, ribbon: Infragistics.Windows.Ribbon.XamRibbon, uiState: Any
    ) -> None: ...
    def GetToolCaption(self, id: str) -> str: ...
    def RegisterScriptCategoryHandler(
        self, category: str, module: str, setState: str, execute: str
    ) -> None: ...
    def RegisterScriptToolHandler(
        self, id: str, module: str, setState: str, execute: str
    ) -> None: ...
    def GetImage(self, image: str) -> System.Windows.Media.Imaging.BitmapSource: ...
