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

from .PlotControl import Axis, IAxisContainer

# Stubs for namespace: Agilent.MassHunter.Quantitative.HeatMap

class HeatMapControl(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    IAxisContainer,
    System.Windows.Controls.Control,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...

    InternalMarginChanged: System.EventHandler
    MonochromeProperty: System.Windows.DependencyProperty  # static # readonly

    AxisX: Axis  # readonly
    AxisY: Axis  # readonly
    Data: Agilent.MassHunter.Quantitative.HeatMap.IHeatMapData
    Monochrome: bool

    def RecalcRects(self) -> None: ...
    def CreateTypeface(self) -> System.Windows.Media.Typeface: ...
    def GetImageMargin(self) -> System.Windows.Thickness: ...
    def GetRenderingPoint(self, x: float, y: float) -> System.Windows.Point: ...
    def GetDataPoint(self, x: float, y: float) -> System.Windows.Point: ...
    def GetGraphicsRect(self) -> System.Windows.Rect: ...
    def Invalidate(self) -> None: ...

class IHeatMapData(object):  # Interface
    MaxValue: float  # readonly
    MaxX: float  # readonly
    MaxY: float  # readonly
    MinValue: float  # readonly
    MinX: float  # readonly
    MinY: float  # readonly
    XCount: int  # readonly
    YCount: int  # readonly

    def GetValue(self, x: int, y: int) -> float: ...
