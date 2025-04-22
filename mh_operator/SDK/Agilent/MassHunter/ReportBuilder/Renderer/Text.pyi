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

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.Renderer.Text

class Renderer(
    System.IDisposable, Agilent.MassHunter.ReportBuilder.Engine.IReportRenderer
):  # Class
    def __init__(self, writer: System.IO.TextWriter, delimiter: str) -> None: ...

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
