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

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.Renderer.Pdf

class Graphics(
    System.IDisposable, Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas
):  # Class
    def __init__(
        self,
        renderer: Agilent.MassHunter.ReportBuilder.Renderer.Pdf.Renderer,
        baseFont: iTextSharp.text.pdf.BaseFont,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

    IgnoreFontName: bool
    PdfPTable: iTextSharp.text.pdf.PdfPTable  # readonly
    PdfTemplate: iTextSharp.text.pdf.PdfTemplate  # readonly

    def ConvertBounds(
        self, bounds: System.Drawing.RectangleF
    ) -> System.Drawing.RectangleF: ...
    def Dispose(self) -> None: ...
    def DrawImage(
        self,
        image: System.Drawing.Image,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def GetGraphics(self) -> T: ...

class PageEvent(iTextSharp.text.pdf.IPdfPageEvent):  # Class
    def __init__(
        self,
        renderer: Agilent.MassHunter.ReportBuilder.Renderer.Pdf.Renderer,
        header: Agilent.MassHunter.ReportBuilder.Template.IHeader,
        footer: Agilent.MassHunter.ReportBuilder.Template.IFooter,
    ) -> None: ...

    Footer: Agilent.MassHunter.ReportBuilder.Template.IFooter  # readonly
    Header: Agilent.MassHunter.ReportBuilder.Template.IHeader  # readonly

    def OnEndPage(
        self, writer: iTextSharp.text.pdf.PdfWriter, document: iTextSharp.text.Document
    ) -> None: ...
    def OnGenericTag(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        rect: iTextSharp.text.Rectangle,
        text: str,
    ) -> None: ...
    def OnOpenDocument(
        self, writer: iTextSharp.text.pdf.PdfWriter, document: iTextSharp.text.Document
    ) -> None: ...
    def OnParagraph(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
    ) -> None: ...
    def OnSection(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
        depth: int,
        title: iTextSharp.text.Paragraph,
    ) -> None: ...
    def OnChapterEnd(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
    ) -> None: ...
    def OnStartPage(
        self, writer: iTextSharp.text.pdf.PdfWriter, document: iTextSharp.text.Document
    ) -> None: ...
    def OnChapter(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
        title: iTextSharp.text.Paragraph,
    ) -> None: ...
    def OnCloseDocument(
        self, writer: iTextSharp.text.pdf.PdfWriter, document: iTextSharp.text.Document
    ) -> None: ...
    def OnParagraphEnd(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
    ) -> None: ...
    def OnSectionEnd(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
    ) -> None: ...

class Renderer(
    System.IDisposable, Agilent.MassHunter.ReportBuilder.Engine.IReportRenderer
):  # Class
    def __init__(self, stream: System.IO.Stream) -> None: ...

    Context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext
    Document: iTextSharp.text.Document  # readonly
    PdfWriter: iTextSharp.text.pdf.PdfWriter  # readonly
    UseTextAsOutlineId: bool

    def RenderImage(
        self, image: Agilent.MassHunter.ReportBuilder.Template.IImage
    ) -> None: ...
    def StartDocument(self) -> None: ...
    def PageBreak(self) -> None: ...
    def GetImage(self, path: str) -> iTextSharp.text.Image: ...
    def GetFont(
        self,
        font: Agilent.MassHunter.ReportBuilder.Template.IFont,
        color: Agilent.MassHunter.ReportBuilder.Template.IColor,
    ) -> iTextSharp.text.Font: ...
    def RenderTable(
        self, numColumns: int
    ) -> Agilent.MassHunter.ReportBuilder.Engine.ITableRenderer: ...
    def RenderGraphics(
        self, graphics: Agilent.MassHunter.ReportBuilder.Template.IGraphics
    ) -> None: ...
    @staticmethod
    def GetColor(
        color: Agilent.MassHunter.ReportBuilder.Template.IColor,
    ) -> iTextSharp.text.BaseColor: ...
    def RenderText(
        self, textbox: Agilent.MassHunter.ReportBuilder.Template.ITextbox
    ) -> None: ...
    def EndDocument(self) -> None: ...
    def SetPage(
        self, page: Agilent.MassHunter.ReportBuilder.Template.IPage
    ) -> None: ...
    def Dispose(self) -> None: ...
    @overload
    def CreateTextChunk(
        self, text: str, font: iTextSharp.text.Font, outlineLevel: Optional[int]
    ) -> iTextSharp.text.Chunk: ...
    @overload
    def CreateTextChunk(
        self,
        text: str,
        font: iTextSharp.text.Font,
        outlineId: str,
        outlineLevel: Optional[int],
    ) -> iTextSharp.text.Chunk: ...

class TableRenderer(Agilent.MassHunter.ReportBuilder.Engine.ITableRenderer):  # Class
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

class XpsGraphics(
    System.IDisposable, Agilent.MassHunter.ReportBuilder.Common.Engine.IGraphicsXps
):  # Class
    def __init__(
        self, renderer: Agilent.MassHunter.ReportBuilder.Renderer.Pdf.Renderer
    ) -> None: ...

    DebugMode: bool  # static # readonly

    @staticmethod
    def GetTempFileName() -> str: ...
    def Add(self, stream: System.IO.Stream) -> None: ...
    def Dispose(self) -> None: ...
