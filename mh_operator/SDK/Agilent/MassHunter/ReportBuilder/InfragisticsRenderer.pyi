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
from .Engine import IGraphicsCanvas, IReportContext, IReportRenderer, ITableRenderer
from .Template import IGraphics, IImage, IPage, ITextbox

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.InfragisticsRenderer

class BrushKey:  # Class
    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class Canvas(
    Agilent.MassSpectrometry.GUI.Plot.IGraphics, IGraphicsCanvas, System.IDisposable
):  # Class
    Clip: System.Drawing.Region
    Graphics: System.Drawing.Graphics  # readonly
    HasGraphics: bool  # readonly
    IgnoreFontName: bool

    @overload
    def FillRectangle(
        self,
        brush: System.Drawing.Brush,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def FillRectangle(
        self, brush: System.Drawing.Brush, rect: System.Drawing.RectangleF
    ) -> None: ...
    def DrawImage(
        self,
        image: System.Drawing.Image,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def DrawRectangle(
        self, pen: System.Drawing.Pen, x1: float, y1: float, x2: float, y2: float
    ) -> None: ...
    def SaveState(self) -> None: ...
    def DrawLines(
        self, pen: System.Drawing.Pen, points: List[System.Drawing.PointF]
    ) -> None: ...
    def DrawEllipse(
        self, pen: System.Drawing.Pen, x: float, y: float, width: float, height: float
    ) -> None: ...
    def GetGraphics(self) -> T: ...
    def RestoreState(self) -> None: ...
    def FillEllipse(
        self,
        brush: System.Drawing.Brush,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def DrawLine(
        self,
        pen: System.Drawing.Pen,
        p1: System.Drawing.PointF,
        p2: System.Drawing.PointF,
    ) -> None: ...
    @overload
    def DrawLine(
        self, pen: System.Drawing.Pen, x1: float, y1: float, x2: float, y2: float
    ) -> None: ...
    def DrawPolygon(
        self, pen: System.Drawing.Pen, points: List[System.Drawing.PointF]
    ) -> None: ...
    @overload
    def DrawString(
        self,
        text: str,
        font: System.Drawing.Font,
        br: System.Drawing.Brush,
        x: float,
        y: float,
        format: System.Drawing.StringFormat,
    ) -> None: ...
    @overload
    def DrawString(
        self,
        text: str,
        font: System.Drawing.Font,
        br: System.Drawing.Brush,
        rect: System.Drawing.RectangleF,
        format: System.Drawing.StringFormat,
    ) -> None: ...
    def DrawXps(self, stream: System.IO.Stream) -> None: ...
    def FillPolygon(
        self, brush: System.Drawing.Brush, points: List[System.Drawing.PointF]
    ) -> None: ...
    def ConvertBounds(
        self, bounds: System.Drawing.RectangleF
    ) -> System.Drawing.RectangleF: ...
    def DrawBitmap(
        self,
        bitmap: System.Drawing.Bitmap,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def DrawBeziers(
        self, pen: System.Drawing.Pen, points: List[System.Drawing.PointF]
    ) -> None: ...
    def Dispose(self) -> None: ...
    def MultiplyTransform(
        self,
        matrix: System.Drawing.Drawing2D.Matrix,
        order: System.Drawing.Drawing2D.MatrixOrder,
    ) -> None: ...
    @overload
    def MeasureString(
        self, text: str, font: System.Drawing.Font, width: int
    ) -> System.Drawing.SizeF: ...
    @overload
    def MeasureString(
        self, text: str, font: System.Drawing.Font
    ) -> System.Drawing.SizeF: ...

class Renderer(IReportRenderer, System.IDisposable):  # Class
    def __init__(
        self,
        stream: System.IO.Stream,
        format: Infragistics.Documents.Reports.Report.FileFormat,
    ) -> None: ...

    Context: IReportContext

    def RenderImage(self, image: IImage) -> None: ...
    def StartDocument(self) -> None: ...
    def PageBreak(self) -> None: ...
    def RenderTable(self, numColumns: int) -> ITableRenderer: ...
    def RenderGraphics(self, graphics: IGraphics) -> None: ...
    def RenderText(self, textbox: ITextbox) -> None: ...
    def EndDocument(self) -> None: ...
    def SetPage(self, page: IPage) -> None: ...
    def Dispose(self) -> None: ...
