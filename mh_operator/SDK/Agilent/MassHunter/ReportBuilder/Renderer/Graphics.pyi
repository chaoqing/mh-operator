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

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.Renderer.Graphics

class Canvas(
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.IGraphics,
    Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
    Agilent.MassSpectrometry.GUI.Plot.GraphicsWrap,
):  # Class
    def __init__(self, gr: System.Drawing.Graphics) -> None: ...

    IgnoreFontName: bool

    def DrawImage(
        self,
        image: System.Drawing.Image,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def GetGraphics(self) -> T: ...
    def DrawXps(self, stream: System.IO.Stream) -> None: ...
    def ConvertBounds(
        self, bounds: System.Drawing.RectangleF
    ) -> System.Drawing.RectangleF: ...
    def Dispose(self) -> None: ...

class Renderer(
    System.IDisposable, Agilent.MassHunter.ReportBuilder.Engine.IReportRenderer
):  # Class
    @overload
    def __init__(
        self,
        graphics: System.Drawing.Graphics,
        pageBound: System.Drawing.RectangleF,
        marginBound: System.Drawing.RectangleF,
    ) -> None: ...
    @overload
    def __init__(
        self,
        graphics: System.Drawing.Graphics,
        pageBound: System.Drawing.RectangleF,
        marginBound: System.Drawing.RectangleF,
        pageNum: int,
        totalPages: int,
    ) -> None: ...

    Context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext

    def RenderImage(
        self, image: Agilent.MassHunter.ReportBuilder.Template.IImage
    ) -> None: ...
    def StartDocument(self) -> None: ...
    def PageBreak(self) -> None: ...
    def RenderTable(
        self, numColumns: int
    ) -> Agilent.MassHunter.ReportBuilder.Engine.ITableRenderer: ...
    def RenderGraphics(
        self, graphics: Agilent.MassHunter.ReportBuilder.Template.IGraphics
    ) -> None: ...
    def RenderText(
        self, textbox: Agilent.MassHunter.ReportBuilder.Template.ITextbox
    ) -> None: ...
    def EndDocument(self) -> None: ...
    def SetPage(
        self, page: Agilent.MassHunter.ReportBuilder.Template.IPage
    ) -> None: ...
    def Dispose(self) -> None: ...

class TableRenderer(Agilent.MassHunter.ReportBuilder.Engine.ITableRenderer):  # Class
    def __init__(
        self, renderer: Agilent.MassHunter.ReportBuilder.Renderer.Graphics.Renderer
    ) -> None: ...
    def SetColumnWidths(self, widths: List[float]) -> None: ...
    def EndTable(self) -> None: ...
    def SetProperties(
        self, table: Agilent.MassHunter.ReportBuilder.Template.ITable
    ) -> None: ...
    def StartHeader(self) -> None: ...
    def EndHeader(self) -> None: ...
    def AddCell(
        self, cell: Agilent.MassHunter.ReportBuilder.Template.ITableCell
    ) -> None: ...
    def EndRow(self) -> None: ...
