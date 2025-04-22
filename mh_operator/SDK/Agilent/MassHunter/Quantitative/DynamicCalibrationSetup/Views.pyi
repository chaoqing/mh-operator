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

from .Models import ICalibrationRangeItem, IIonGroupPlotSeries

# Stubs for namespace: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Views

class CalibrationRangeView(
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

class CalibrationView(
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

class CompoundsView(
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

class IonGroupPlotControl(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    System.Windows.Controls.Control,
    System.Windows.Media.Animation.IAnimatable,
    Agilent.MassHunter.Quantitative.PlotControl.IAxisContainer,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...

    PlotSeriesProperty: System.Windows.DependencyProperty  # static
    SelectedRangeProperty: System.Windows.DependencyProperty  # static
    SelectedSeriesProperty: System.Windows.DependencyProperty  # static

    PlotSeries: List[IIonGroupPlotSeries]
    SelectedRange: ICalibrationRangeItem
    SelectedSeries: IIonGroupPlotSeries

    @staticmethod
    def IsIntersect(
        p1x: float,
        p1y: float,
        p2x: float,
        p2y: float,
        p3x: float,
        p3y: float,
        p4x: float,
        p4y: float,
        p5x: float,
        p5y: float,
        p6x: float,
        p6y: float,
    ) -> bool: ...
    @staticmethod
    def CCW(
        x0: float, y0: float, x1: float, y1: float, x2: float, y2: float
    ) -> int: ...
    def RecalcRects(self) -> None: ...
    def CreateTypeface(self) -> System.Windows.Media.Typeface: ...
    @staticmethod
    def Norm(x: float, y: float) -> float: ...
    @staticmethod
    def Dot(x1: float, y1: float, x2: float, y2: float) -> float: ...
    @staticmethod
    def Cross(x1: float, y1: float, x2: float, y2: float) -> float: ...
    def Invalidate(self) -> None: ...

class IonGroupView(
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

    DataGrid: System.Windows.Controls.DataGrid  # readonly

    def InitializeComponent(self) -> None: ...

class QualifiersView(
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
