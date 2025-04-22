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

# Stubs for namespace: Agilent.MassHunter.ReportCommon

class PDFFontUtil:  # Class
    DefaultBaseFont: iTextSharp.text.pdf.BaseFont  # static # readonly

    @staticmethod
    def FindFontFile(name: str, index: int) -> str: ...
    @staticmethod
    def RegisterFont(name: str) -> None: ...
    @staticmethod
    def ResetDefaultFont() -> None: ...

class PDFPlotGraphics(
    System.IDisposable, Agilent.MassSpectrometry.GUI.Plot.IGraphics
):  # Class
    def __init__(
        self,
        canvas: iTextSharp.text.pdf.PdfContentByte,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

    Clip: System.Drawing.Region
    Graphics: System.Drawing.Graphics  # readonly
    HasGraphics: bool  # readonly
    IgnoreFontName: bool
    PdfContentByte: iTextSharp.text.pdf.PdfContentByte  # readonly

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
    def DrawRectangle(
        self, pen: System.Drawing.Pen, x1: float, y1: float, width: float, height: float
    ) -> None: ...
    def SaveState(self) -> None: ...
    def DrawLines(
        self, pen: System.Drawing.Pen, points: List[System.Drawing.PointF]
    ) -> None: ...
    def DrawEllipse(
        self, pen: System.Drawing.Pen, x: float, y: float, width: float, height: float
    ) -> None: ...
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
    def FillPolygon(
        self, brush: System.Drawing.Brush, points: List[System.Drawing.PointF]
    ) -> None: ...
    def DrawBitmap(
        self,
        bmp: System.Drawing.Bitmap,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def DrawBeziers(
        self, pen: System.Drawing.Pen, points: List[System.Drawing.PointF]
    ) -> None: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def FindFontFile(name: str, index: int) -> str: ...
    def MultiplyTransform(
        self,
        matrix: System.Drawing.Drawing2D.Matrix,
        order: System.Drawing.Drawing2D.MatrixOrder,
    ) -> None: ...
    @overload
    def MeasureString(
        self, text: str, font: System.Drawing.Font
    ) -> System.Drawing.SizeF: ...
    @overload
    def MeasureString(
        self, text: str, font: System.Drawing.Font, width: int
    ) -> System.Drawing.SizeF: ...
