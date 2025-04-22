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

from . import IPeakData, IPlotData, PlotModes

# Stubs for namespace: Agilent.MassSpectrometry.GUI.Plot.Exactify

class SpectrumPlotData(System.IDisposable, IPlotData, IPeakData):  # Class
    def __init__(self) -> None: ...
    def GetPointCount(self, series: int) -> int: ...
    def GetSeriesCount(self) -> int: ...
    def DisplaySeries(self, series: int) -> bool: ...
    def RemoveSeries(self, index: int) -> None: ...
    def GetPoint(self, series: int, pointIndex: int, x: float, y: float) -> None: ...
    def GetYRange(self, minY: float, maxY: float) -> None: ...
    @overload
    def AddSeries(
        self,
        color: System.Drawing.Color,
        mode: PlotModes,
        points: List[System.Drawing.PointF],
    ) -> None: ...
    @overload
    def AddSeries(
        self,
        color: System.Drawing.Color,
        mode: PlotModes,
        points: List[System.Drawing.PointF],
        formulas: List[Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula],
        multiplicities: List[int],
        mzDeltasPpm: List[float],
    ) -> None: ...
    def GetXRange(self, minX: float, maxX: float) -> None: ...
    def Dispose(self) -> None: ...
    def GetSeriesLineStyle(
        self,
        series: int,
        mode: PlotModes,
        color: System.Drawing.Color,
        style: System.Drawing.Drawing2D.DashStyle,
        width: int,
    ) -> None: ...
