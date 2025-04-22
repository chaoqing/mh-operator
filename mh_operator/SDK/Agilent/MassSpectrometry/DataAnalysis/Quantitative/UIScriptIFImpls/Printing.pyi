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

from . import UIState

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIFImpls.Printing

class PrintPlotDocument(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PrintGraphicsDocument,
    System.ComponentModel.IComponent,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        uiState: UIState,
        activePlot: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        printerSettings: System.Drawing.Printing.PrinterSettings,
        pageSettings: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils.PlotPageSettings,
        preview: bool,
        reportBuilderTemplate: str,
    ) -> None: ...

    Anchoring: bool
    Column: int
    PageNumber: int  # readonly
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    ReportBuilderTemplate: str  # readonly
    Row: int
    UIState: UIState  # readonly

    def DrawPage(
        self,
        graphics: System.Drawing.Graphics,
        pageBounds: System.Drawing.Rectangle,
        marginBounds: System.Drawing.RectangleF,
        row: int,
        col: int,
    ) -> None: ...
    def RenderGraphics(
        self,
        graphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        x: float,
        y: float,
        w: float,
        h: float,
        name: str,
    ) -> None: ...
    def GetNumPages(self) -> int: ...
    def PrintToPdf(self, stream: System.IO.Stream) -> None: ...
