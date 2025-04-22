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

from .PlotControl import IPeaks, IPlotBar, IPlotSeries, PlotAxesControl, PlotPeakSeries
from .UIModel import IDataNavigator

# Stubs for namespace: Agilent.MassHunter.Quantitative.Screening

class ItemStatus(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Error: Agilent.MassHunter.Quantitative.Screening.ItemStatus = (
        ...
    )  # static # readonly
    Good: Agilent.MassHunter.Quantitative.Screening.ItemStatus = (
        ...
    )  # static # readonly
    Warning: Agilent.MassHunter.Quantitative.Screening.ItemStatus = (
        ...
    )  # static # readonly

class SampleItem:  # Class
    def __init__(self, sampleID: int, name: str) -> None: ...

    Name: str  # readonly
    SampleID: int  # readonly

    def ToString(self) -> str: ...

class ScreeningControl(
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

class ScreeningTable(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Controls.DataGrid,
    System.Windows.Media.Animation.IAnimatable,
    MS.Internal.Controls.IGeneratorHost,
    System.ComponentModel.ISupportInitialize,
    System.Windows.IInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.IFrameworkInputElement,
    System.Windows.Controls.Primitives.IContainItemStorage,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class ScreeningTableItem:  # Class
    def __init__(self) -> None: ...

    BatchID: int  # readonly
    CASNumber: str  # readonly
    CompoundID: int  # readonly
    CompoundName: str  # readonly
    ExpectedRetentionTime: float  # readonly
    FinalConcentration: Optional[float]  # readonly
    MZ: float  # readonly
    MassAccuracy: Optional[float]  # readonly
    MassMatchScore: Optional[float]  # readonly
    MolecularFormula: str  # readonly
    NumberOfQualifiedIons: int  # readonly
    OutlierCount: int  # readonly
    OutlierMassAccuracy: bool  # readonly
    OutlierMassMatchScore: bool  # readonly
    OutlierNumberOfQualifiedIons: bool  # readonly
    OutlierReferenceLibraryMatchScore: bool  # readonly
    OutlierRetentionTimeDifference: bool  # readonly
    PeakRetentionTime: Optional[float]  # readonly
    ReferenceLibraryMatchScore: Optional[float]  # readonly
    RetentionTimeDifference: Optional[float]  # readonly
    SampleID: int  # readonly
    Status: Agilent.MassHunter.Quantitative.Screening.ItemStatus  # readonly

    def Initialize(
        self,
        compound: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow,
        peak: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.PeakRow,
        useReferenceLibraryMatchScore: bool,
        useMassMatchScore: bool,
        useQualifierRatio: bool,
    ) -> None: ...

class ScreeningTableModel(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        table: Agilent.MassHunter.Quantitative.Screening.ScreeningTable,
        navigator: IDataNavigator,
    ) -> None: ...

    CompoundCountCheck: int  # readonly
    CompoundCountError: int  # readonly
    CompoundCountTotal: int  # readonly
    CompoundCountWarning: int  # readonly
    Items: List[
        Agilent.MassHunter.Quantitative.Screening.ScreeningTableItem
    ]  # readonly
    ShowGreenItems: bool
    ShowMassMatchScore: bool
    ShowOrangeItems: bool
    ShowRedItems: bool
    ShowReferenceLibraryMatchScore: bool
    UseQualifierRatio: bool
    View: System.ComponentModel.ICollectionView  # readonly

    def UpdateSample(self, sampleID: int) -> None: ...
    def Disconnect(self) -> None: ...
    def UpdateData(self) -> None: ...

class ScreeningWindow(
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
    IstotopeSpectrumVisible: bool

    def InitGC(self) -> None: ...
    def InitLC(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    def ShowAndActivate(self) -> None: ...
    @staticmethod
    def GetInstance(
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> Agilent.MassHunter.Quantitative.Screening.ScreeningWindow: ...

class SpectrumAverageHandler(
    Agilent.MassHunter.Quantitative.Screening.SpectrumHandlerBase
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Screening.SpectrumHandler,
        plot: PlotAxesControl,
    ) -> None: ...
    def _UpdateData(self) -> None: ...
    @staticmethod
    def GetXRange(
        serieses: Iterable[IPlotSeries], minx: float, maxx: float
    ) -> None: ...

class SpectrumHandler:  # Class
    def __init__(
        self,
        plot: PlotAxesControl,
        simplifiedPlot: PlotAxesControl,
        isotopePlot: PlotAxesControl,
        dataNavigator: IDataNavigator,
    ) -> None: ...

    DataNavigator: IDataNavigator  # readonly
    SpectrumAverageHandler: (
        Agilent.MassHunter.Quantitative.Screening.SpectrumAverageHandler
    )  # readonly
    SpectrumError: str  # readonly
    SpectrumIsotopeHandler: (
        Agilent.MassHunter.Quantitative.Screening.SpectrumIsotopeHandler
    )  # readonly
    SpectrumSimplifiedHandler: (
        Agilent.MassHunter.Quantitative.Screening.SpectrumSimplifiedHandler
    )  # readonly

    def GetSpectrum(self) -> Agilent.MassSpectrometry.DataAnalysis.ISpectrum: ...
    @staticmethod
    def SetPlotTitle(plot: PlotAxesControl, title: str) -> None: ...
    def Disconnect(self) -> None: ...
    @staticmethod
    def ClearPlot(plot: PlotAxesControl) -> None: ...
    def GetReferenceLibrarySpectrum(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.ISpectrum: ...

class SpectrumHandlerBase:  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Screening.SpectrumHandler,
        plot: PlotAxesControl,
    ) -> None: ...

    PlotAxesControl: PlotAxesControl  # readonly

    def Disconnect(self) -> None: ...

class SpectrumIsotopeHandler(
    Agilent.MassHunter.Quantitative.Screening.SpectrumHandlerBase
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Screening.SpectrumHandler,
        plot: PlotAxesControl,
    ) -> None: ...
    def _UpdateData(self) -> None: ...

    # Nested Types

    class BarSeries(PlotPeakSeries, IPlotSeries, IPlotBar, IPeaks):  # Class
        def __init__(self) -> None: ...
        def SetIonsMatch(
            self, ionsMatch: Iterable[Agilent.MassSpectrometry.IIonMatch]
        ) -> None: ...
        def GetBarRange(self, index: int, start: float, end: float) -> None: ...
        def GetPeakLabelBrush(self, index: int) -> System.Windows.Media.Brush: ...
        def GetLinePen(self, index: int) -> System.Windows.Media.Pen: ...
        def GetFillBrush(self, index: int) -> System.Windows.Media.Brush: ...

class SpectrumSimplifiedHandler(
    Agilent.MassHunter.Quantitative.Screening.SpectrumHandlerBase
):  # Class
    def __init__(
        self,
        parent: Agilent.MassHunter.Quantitative.Screening.SpectrumHandler,
        plot: PlotAxesControl,
    ) -> None: ...
    def _UpdateData(self) -> None: ...

class ToolbarHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        toolbar: System.Windows.Controls.ToolBar,
        tableModel: Agilent.MassHunter.Quantitative.Screening.ScreeningTableModel,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...

    Command_NextSample: System.Windows.Input.ICommand  # readonly
    Command_PrevSample: System.Windows.Input.ICommand  # readonly
    TableModel: (
        Agilent.MassHunter.Quantitative.Screening.ScreeningTableModel
    )  # readonly

    def NextSample(self, p: Any) -> None: ...
    def CanPrevSample(self, p: Any) -> bool: ...
    def PrevSample(self, p: Any) -> None: ...
    def CanNextSample(self, p: Any) -> bool: ...
    def Disconnect(self) -> None: ...
