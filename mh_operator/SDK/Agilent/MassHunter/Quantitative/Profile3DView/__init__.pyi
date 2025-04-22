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

from . import Remoting
from .HeatMap import HeatMapControl, IHeatMapData
from .PlotControl import IAxisContainer, IPlotSeries, PlotMode

# Stubs for namespace: Agilent.MassHunter.Quantitative.Profile3DView

class App(
    System.Windows.Application,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    @staticmethod
    def Main() -> None: ...

class CommandLine:  # Class
    def __init__(self) -> None: ...

    MZ: float
    RetentionTime: float
    Sample: str
    Singleton: bool

class DelegateCommand(System.Windows.Input.ICommand):  # Class
    def __init__(
        self, exec: System.Action, canexec: System.Func[Any, bool]
    ) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Execute(self, parameter: Any) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class HeatMapAdorner(
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.IFrameworkInputElement,
    System.Windows.IInputElement,
    System.Windows.Markup.IQueryAmbient,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IHaveResources,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Documents.Adorner,
):  # Class
    def __init__(
        self, c: Agilent.MassHunter.Quantitative.Profile3DView.HeatMapControl
    ) -> None: ...

class HeatMapControl(
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.IInputElement,
    IAxisContainer,
    System.Windows.Markup.IQueryAmbient,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IHaveResources,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IFrameworkInputElement,
):  # Class
    def __init__(self) -> None: ...

class HeatMapData(IHeatMapData):  # Class
    def __init__(
        self, model: Agilent.MassHunter.Quantitative.Profile3DView.Model
    ) -> None: ...

    MaxValue: float
    MaxX: float
    MaxY: float
    MinValue: float
    MinX: float
    MinY: float
    XCount: int
    YCount: int

    def GetValue(self, x: int, y: int) -> float: ...

class HeatMapView(
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

class HeatMapViewModel(System.Windows.DependencyObject):  # Class
    def __init__(
        self, model: Agilent.MassHunter.Quantitative.Profile3DView.Model
    ) -> None: ...

    SelectedPointProperty: System.Windows.DependencyProperty  # static # readonly

    Model: Agilent.MassHunter.Quantitative.Profile3DView.Model  # readonly
    SelectedPoint: Optional[System.Windows.Point]

class LeftPanelControl(
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

class MainWindow(
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
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class Model(System.Windows.DependencyObject):  # Class
    def __init__(self) -> None: ...

    CountFormatProperty: System.Windows.DependencyProperty  # static # readonly
    CountRangeProperty: System.Windows.DependencyProperty  # static # readonly
    MZFormatProperty: System.Windows.DependencyProperty  # static # readonly
    MZProperty: System.Windows.DependencyProperty  # static # readonly
    MZRangeProperty: System.Windows.DependencyProperty  # static # readonly
    MaxCountProperty: System.Windows.DependencyProperty  # static # readonly
    MaxMZProperty: System.Windows.DependencyProperty  # static # readonly
    MaxRTProperty: System.Windows.DependencyProperty  # static # readonly
    MinCountProperty: System.Windows.DependencyProperty  # static # readonly
    MinMZProperty: System.Windows.DependencyProperty  # static # readonly
    MinRTProperty: System.Windows.DependencyProperty  # static # readonly
    PointCountProperty: System.Windows.DependencyProperty  # static # readonly
    RTFormatProperty: System.Windows.DependencyProperty  # static # readonly
    RTProperty: System.Windows.DependencyProperty  # static # readonly
    RTRangeProperty: System.Windows.DependencyProperty  # static # readonly
    RangeFactorProperty: System.Windows.DependencyProperty  # static # readonly
    SampleFileNameProperty: System.Windows.DependencyProperty  # static # readonly
    ScanCountProperty: System.Windows.DependencyProperty  # static # readonly
    SelectedViewIndexProperty: System.Windows.DependencyProperty  # static # readonly
    ZValuesProperty: System.Windows.DependencyProperty  # static # readonly

    ChangeRange: System.Windows.Input.ICommand  # readonly
    CountFormat: str
    CountRange: str  # readonly
    HeatMapViewModel: (
        Agilent.MassHunter.Quantitative.Profile3DView.HeatMapViewModel
    )  # readonly
    MZ: Optional[float]
    MZFormat: str
    MZRange: str  # readonly
    MaxCount: Optional[float]
    MaxMZ: Optional[float]
    MaxRT: Optional[float]
    MinCount: Optional[float]
    MinMZ: Optional[float]
    MinRT: Optional[float]
    PointCount: int
    Profile3DViewModel: (
        Agilent.MassHunter.Quantitative.Profile3DView.Profile3DViewModel
    )  # readonly
    RT: Optional[float]
    RTFormat: str
    RTRange: str  # readonly
    RangeFactor: int
    SampleFileName: str
    ScanCount: int
    SelectedViewIndex: int
    ZValues: List[List[float]]

    def Open(self, samplePath: str, mz: float, rt: float) -> None: ...
    def Clear(self) -> None: ...
    def GetChrom(self, x: int) -> List[float]: ...

class PlotControl(
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.Control,
    System.Windows.IInputElement,
    System.Windows.Markup.IQueryAmbient,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IHaveResources,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IFrameworkInputElement,
):  # Class
    def __init__(self) -> None: ...

    InternalMargin: System.Windows.Thickness
    Series: IPlotSeries
    Vertical: bool

class PlotSeriesArr(IPlotSeries):  # Class
    def __init__(self, data: List[float], minX: float, maxX: float) -> None: ...

    Count: int  # readonly
    Pen: System.Windows.Media.Pen  # readonly
    PlotMode: PlotMode  # readonly
    Visible: bool  # readonly

    def GetPoint(self, index: int, x: float, y: float) -> None: ...

class Profile3DControl(
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
    def Clear(self) -> None: ...
    def InitFeature(
        self,
        minx: float,
        maxx: float,
        miny: float,
        maxy: float,
        nx: int,
        ny: int,
        zvalues: List[List[float]],
    ) -> None: ...
    def LoadLogFile(self, file: str) -> None: ...

class Profile3DException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, msg: str) -> None: ...
    @overload
    def __init__(self, msg: str, inner: System.Exception) -> None: ...

class Profile3DViewModel(System.Windows.DependencyObject):  # Class
    def __init__(
        self, model: Agilent.MassHunter.Quantitative.Profile3DView.Model
    ) -> None: ...

    Is3DViewActiveProperty: System.Windows.DependencyProperty  # static # readonly
    MZOffsetProperty: System.Windows.DependencyProperty  # static # readonly
    MZScaleFactorProperty: System.Windows.DependencyProperty  # static # readonly
    RTOffsetProperty: System.Windows.DependencyProperty  # static # readonly
    RTScaleFactorProperty: System.Windows.DependencyProperty  # static # readonly
    ScaleFactorProperty: System.Windows.DependencyProperty  # static # readonly
    ViewportRotationCounterProperty: (
        System.Windows.DependencyProperty
    )  # static # readonly
    ZOffsetProperty: System.Windows.DependencyProperty  # static # readonly
    ZScaleFactorProperty: System.Windows.DependencyProperty  # static # readonly

    ChromatographicView: System.Windows.Input.ICommand  # readonly
    HeatMapView: System.Windows.Input.ICommand  # readonly
    Is3DViewActive: bool  # readonly
    MZOffset: float
    MZScaleFactor: float
    Model: Agilent.MassHunter.Quantitative.Profile3DView.Model  # readonly
    RTOffset: float
    RTScaleFactor: float
    ResetScale: System.Windows.Input.ICommand  # readonly
    ResetViewport: System.Windows.Input.ICommand  # readonly
    ScaleFactor: float
    SpectralView: System.Windows.Input.ICommand  # readonly
    ViewportRotationCounter: int
    ViewportRotationX: float
    ViewportRotationY: float
    ViewportRotationZ: float
    ZOffset: float
    ZScaleFactor: float

class RangeFactorWindow(
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
        self, model: Agilent.MassHunter.Quantitative.Profile3DView.Model
    ) -> None: ...
    def InitializeComponent(self) -> None: ...
