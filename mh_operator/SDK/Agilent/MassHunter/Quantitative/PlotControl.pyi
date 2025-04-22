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

# Stubs for namespace: Agilent.MassHunter.Quantitative.PlotControl

class Axis(System.Windows.DependencyObject):  # Class
    def __init__(
        self,
        container: Agilent.MassHunter.Quantitative.PlotControl.IAxisContainer,
        location: Agilent.MassHunter.Quantitative.PlotControl.AxisLocation,
    ) -> None: ...

    LabelColorProperty: System.Windows.DependencyProperty  # static
    LineColorProperty: System.Windows.DependencyProperty  # static
    MaxValueProperty: System.Windows.DependencyProperty  # static
    MinValueProperty: System.Windows.DependencyProperty  # static
    TickLabelFormatProperty: System.Windows.DependencyProperty  # static
    TickLabelVerticalProperty: System.Windows.DependencyProperty  # static
    TitleLocationProperty: System.Windows.DependencyProperty  # static
    TitleProperty: System.Windows.DependencyProperty  # static
    VisibilityProperty: System.Windows.DependencyProperty  # static

    IsLog: bool
    LabelColor: System.Windows.Media.Color
    LineColor: System.Windows.Media.Color
    Location: Agilent.MassHunter.Quantitative.PlotControl.AxisLocation  # readonly
    MaxValue: float
    MinValue: float
    TickLabelExponential: bool
    TickLabelFormat: str
    TickLabelVertical: bool
    Title: str
    TitleLocation: Agilent.MassHunter.Quantitative.PlotControl.TitleLocation
    Visibility: System.Windows.Visibility

    def Render(
        self,
        gr: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        clipRect: System.Windows.Rect,
        rect: System.Windows.Rect,
    ) -> None: ...
    def CalcHeight(self) -> float: ...

class AxisLabelInfo:  # Class
    def __init__(self) -> None: ...

    Brush: System.Windows.Media.Brush
    CultureInfo: System.Globalization.CultureInfo
    ExponentialTickLabel: bool
    FlowDirection: System.Windows.FlowDirection
    FontSize: float
    GridlineMode: Agilent.MassHunter.Quantitative.PlotControl.GridlineMode
    Location: Agilent.MassHunter.Quantitative.PlotControl.AxisLocation
    PlotControl: Agilent.MassHunter.Quantitative.PlotControl.PlotControl
    TickLabelFormat: str
    TickSize: float
    TypeFace: System.Windows.Media.Typeface

    def GetTickLabel(self, value_: float) -> str: ...

class AxisLocation(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Bottom: Agilent.MassHunter.Quantitative.PlotControl.AxisLocation = (
        ...
    )  # static # readonly
    Left: Agilent.MassHunter.Quantitative.PlotControl.AxisLocation = (
        ...
    )  # static # readonly
    Right: Agilent.MassHunter.Quantitative.PlotControl.AxisLocation = (
        ...
    )  # static # readonly
    Top: Agilent.MassHunter.Quantitative.PlotControl.AxisLocation = (
        ...
    )  # static # readonly

class ClipState(Agilent.MassHunter.Quantitative.PlotControl.GraphicsState):  # Class
    def __init__(self, clip: System.Windows.Rect) -> None: ...
    def Push(self, canvas: iTextSharp.text.pdf.PdfContentByte) -> None: ...
    def Pop(self, canvas: iTextSharp.text.pdf.PdfContentByte) -> None: ...

class DrawAxis:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def CalcHorizontalAxisHeight(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        labelInfo: Agilent.MassHunter.Quantitative.PlotControl.AxisLabelInfo,
    ) -> float: ...
    @staticmethod
    def DrawXAxis(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        clipRect: System.Windows.Rect,
        rect: System.Windows.Rect,
        minValue: float,
        maxValue: float,
        pen: System.Windows.Media.Pen,
        labelInfo: Agilent.MassHunter.Quantitative.PlotControl.AxisLabelInfo,
    ) -> None: ...
    @staticmethod
    def DrawXAxisLog(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        clipRect: System.Windows.Rect,
        rect: System.Windows.Rect,
        minValue: float,
        maxValue: float,
        pen: System.Windows.Media.Pen,
        labelInfo: Agilent.MassHunter.Quantitative.PlotControl.AxisLabelInfo,
    ) -> None: ...
    @staticmethod
    def CalcTickIntervalLog(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        minValue: float,
        maxValue: float,
        labelInfo: Agilent.MassHunter.Quantitative.PlotControl.AxisLabelInfo,
        areaWidth: float,
        start: float,
        factor: float,
    ) -> None: ...
    @staticmethod
    def CalcTickInterval(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        minValue: float,
        maxValue: float,
        labelInfo: Agilent.MassHunter.Quantitative.PlotControl.AxisLabelInfo,
        areaSize: System.Windows.Size,
        orientation: System.Windows.Controls.Orientation,
        desiredSize: float,
    ) -> float: ...
    @staticmethod
    def MeasureVerticalTickLabels(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        minValue: float,
        maxValue: float,
        interval: float,
        labelInfo: Agilent.MassHunter.Quantitative.PlotControl.AxisLabelInfo,
        areaHeight: float,
    ) -> float: ...
    @staticmethod
    def DrawYAxis(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        clipRect: System.Windows.Rect,
        rect: System.Windows.Rect,
        minValue: float,
        maxValue: float,
        pen: System.Windows.Media.Pen,
        labelInfo: Agilent.MassHunter.Quantitative.PlotControl.AxisLabelInfo,
    ) -> None: ...

class DrawPeakLabels:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def DrawStringBottomUp(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        text: str,
        culture: System.Globalization.CultureInfo,
        flow: System.Windows.FlowDirection,
        typeface: System.Windows.Media.Typeface,
        emSize: float,
        brush: System.Windows.Media.Brush,
        alignment: System.Windows.TextAlignment,
        trimming: System.Windows.TextTrimming,
        pos: System.Windows.Point,
    ) -> None: ...
    @staticmethod
    def DrawNonOverlap(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        peaks: Agilent.MassHunter.Quantitative.PlotControl.IPeaks,
        drawInfo: Agilent.MassHunter.Quantitative.PlotControl.DrawPeakLabelsInfo,
        dataRect: System.Windows.Rect,
        rect: System.Windows.Rect,
        clipRect: System.Windows.Rect,
    ) -> None: ...

class DrawPeakLabelsInfo:  # Class
    def __init__(self) -> None: ...

    CultureInfo: System.Globalization.CultureInfo
    FontSize: float
    Typeface: System.Windows.Media.Typeface
    Vertical: bool

class DrawPlot:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def DrawLog(
        gr: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        pen: System.Windows.Media.Pen,
        series: Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries,
        minX: float,
        maxX: float,
        minY: float,
        maxY: float,
        rect: System.Windows.Rect,
    ) -> None: ...
    @overload
    @staticmethod
    def FindNearestIndex(
        series: Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries, x: float
    ) -> int: ...
    @overload
    @staticmethod
    def FindNearestIndex(
        series: Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries,
        x: float,
        start: int,
        end: int,
    ) -> int: ...
    @staticmethod
    def GetSnapPoint(
        series: Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries, sx: float
    ) -> Optional[System.Windows.Point]: ...
    @staticmethod
    def DrawBar(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        series: Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries,
        bar: Agilent.MassHunter.Quantitative.PlotControl.IPlotBar,
        minX: float,
        maxX: float,
        minY: float,
        maxY: float,
        rect: System.Windows.Rect,
    ) -> None: ...
    @staticmethod
    def CoordinateToDataY(
        coord: float, minData: float, maxData: float, minCoord: float, maxCoord: float
    ) -> float: ...
    @staticmethod
    def CoordinateToDataX(
        coord: float, minData: float, maxData: float, minCoord: float, maxCoord: float
    ) -> float: ...
    @staticmethod
    def Draw(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        pen: System.Windows.Media.Pen,
        series: Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries,
        minX: float,
        maxX: float,
        minY: float,
        maxY: float,
        rect: System.Windows.Rect,
        drawVertical: bool,
    ) -> None: ...
    @staticmethod
    def DrawSpectrum(
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        pen: System.Windows.Media.Pen,
        series: Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries,
        minX: float,
        maxX: float,
        minY: float,
        maxY: float,
        rect: System.Windows.Rect,
    ) -> None: ...
    @staticmethod
    def DataToCoordinateLog(
        data: float, minData: float, maxData: float, minCoord: float, maxCoord: float
    ) -> float: ...
    @staticmethod
    def DataToCoordinateY(
        data: float, minData: float, maxData: float, minCoord: float, maxCoord: float
    ) -> float: ...
    @staticmethod
    def DataToCoordinateX(
        data: float, minData: float, maxData: float, minCoord: float, maxCoord: float
    ) -> float: ...

class DrawingContextGraphics(
    System.IDisposable, Agilent.MassHunter.Quantitative.PlotControl.IGraphics
):  # Class
    def __init__(self, dc: System.Windows.Media.DrawingContext) -> None: ...
    def DrawRectangle(
        self,
        brush: System.Windows.Media.Brush,
        pen: System.Windows.Media.Pen,
        rectangle: System.Windows.Rect,
    ) -> None: ...
    @overload
    def DrawText(
        self,
        ft: System.Windows.Media.FormattedText,
        brush: System.Windows.Media.Brush,
        p: System.Windows.Point,
    ) -> None: ...
    @overload
    def DrawText(
        self,
        text: str,
        culture: System.Globalization.CultureInfo,
        flow: System.Windows.FlowDirection,
        typeface: System.Windows.Media.Typeface,
        emSize: float,
        brush: System.Windows.Media.Brush,
        alignment: System.Windows.TextAlignment,
        trimming: System.Windows.TextTrimming,
        maxTextWidth: Optional[float],
        pos: System.Windows.Point,
    ) -> None: ...
    def DrawPolyline(
        self, pen: System.Windows.Media.Pen, points: List[System.Windows.Point]
    ) -> None: ...
    def DrawEllipse(
        self,
        br: System.Windows.Media.Brush,
        pen: System.Windows.Media.Pen,
        center: System.Windows.Point,
        radiusX: float,
        radiusY: float,
    ) -> None: ...
    def DrawLine(
        self,
        pen: System.Windows.Media.Pen,
        s: System.Windows.Point,
        e: System.Windows.Point,
    ) -> None: ...
    def DrawPolygon(
        self,
        br: System.Windows.Media.Brush,
        pen: System.Windows.Media.Pen,
        points: List[System.Windows.Point],
    ) -> None: ...
    def Pop(self) -> None: ...
    def PushClip(self, rect: System.Windows.Rect) -> None: ...
    def PushGuidelineSet(self, gs: System.Windows.Media.GuidelineSet) -> None: ...
    def PushTransform(self, t: System.Windows.Media.Transform) -> None: ...
    def Dispose(self) -> None: ...
    @overload
    def MeasureString(
        self, text: str, typeface: System.Windows.Media.Typeface, size: float
    ) -> System.Windows.Size: ...
    @overload
    def MeasureString(
        self,
        text: str,
        typeface: System.Windows.Media.Typeface,
        size: float,
        width: float,
    ) -> System.Windows.Size: ...

class GraphicsState:  # Class
    def __init__(self) -> None: ...
    def Push(self, canvas: iTextSharp.text.pdf.PdfContentByte) -> None: ...
    def Pop(self, canvas: iTextSharp.text.pdf.PdfContentByte) -> None: ...

class GridPlotBehavior(
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.Behavior[
        Agilent.MassHunter.Quantitative.PlotControl.GridPlotContent
    ],
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    def __init__(self) -> None: ...

class GridPlotContent(
    System.Windows.Controls.Primitives.IScrollInfo,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    System.Windows.Controls.Control,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...

    AxisLabelBrushProperty: System.Windows.DependencyProperty  # static # readonly
    AxisLineBrushProperty: System.Windows.DependencyProperty  # static # readonly
    ColumnOffsetProperty: System.Windows.DependencyProperty  # static # readonly
    DataSourceProperty: System.Windows.DependencyProperty  # static # readonly
    LinkAxesXProperty: System.Windows.DependencyProperty  # static # readonly
    NumColumnsPerPageProperty: System.Windows.DependencyProperty  # static # readonly
    NumRowsPerPageProperty: System.Windows.DependencyProperty  # static # readonly
    PaneBorderBrushProperty: System.Windows.DependencyProperty  # static # readonly
    PaneBorderThicknessProperty: System.Windows.DependencyProperty  # static # readonly
    PaneMarginProperty: System.Windows.DependencyProperty  # static # readonly
    PaneSelectionModeProperty: System.Windows.DependencyProperty  # static # readonly
    RowOffsetProperty: System.Windows.DependencyProperty  # static # readonly
    SelectedPaneBorderBrushProperty: (
        System.Windows.DependencyProperty
    )  # static # readonly
    TickLabelFontSizeProperty: System.Windows.DependencyProperty  # static # readonly
    TickSizeProperty: System.Windows.DependencyProperty  # static # readonly
    TitleFontSizeProperty: System.Windows.DependencyProperty  # static # readonly

    AxisLabelBrush: System.Windows.Media.Brush
    AxisLineBrush: System.Windows.Media.Brush
    CanHorizontallyScroll: bool
    CanVerticallyScroll: bool
    ColumnOffset: int
    DataSource: System.Array[Any]
    ExtentHeight: float  # readonly
    ExtentWidth: float  # readonly
    HorizontalOffset: float  # readonly
    def __getitem__(
        self, rowIndex: int, columnIndex: int
    ) -> Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane: ...
    def __setitem__(
        self,
        rowIndex: int,
        columnIndex: int,
        value_: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane,
    ) -> None: ...
    LinkAxesX: bool
    NumColumns: int  # readonly
    NumColumnsPerPage: int
    NumRows: int  # readonly
    NumRowsPerPage: int
    PaneBorderBrush: System.Windows.Media.Brush
    PaneBorderThickness: float
    PaneMargin: float
    PaneSelectionMode: Agilent.MassHunter.Quantitative.PlotControl.PaneSelectionMode
    RowOffset: int
    ScrollOwner: System.Windows.Controls.ScrollViewer
    SelectedPaneBorderBrush: System.Windows.Media.Brush
    TickLabelFontSize: float
    TickSize: float
    TitleExtent: float
    TitleFontSize: float
    VerticalOffset: float  # readonly
    ViewportHeight: float  # readonly
    ViewportWidth: float  # readonly
    XAxisExtent: float
    YAxisExtent: float

    def DrawPage(
        self,
        drawingContext: System.Windows.Media.DrawingContext,
        rect: System.Windows.Rect,
        rowOffset: int,
        columnOffset: int,
        numRowsPerPage: int,
        numColumnsPerPage: int,
    ) -> None: ...
    def AutoScalePaneY(
        self, pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane
    ) -> None: ...
    def UnselectAllPanes(self) -> None: ...
    def DrawPane(
        self,
        drawingContext: System.Windows.Media.DrawingContext,
        rect: System.Windows.Rect,
        pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane,
        dataSource: Any,
    ) -> None: ...
    def GetLinkedRangeX(
        self, index: int
    ) -> Agilent.MassHunter.Quantitative.PlotControl.LinkedRange: ...
    def GetAutoScaleRange(
        self,
        pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane,
        vertical: bool,
    ) -> Agilent.MassHunter.Quantitative.PlotControl.Range: ...
    def ShiftSelectPanes(
        self, pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane
    ) -> None: ...
    def UpdateDimension(self) -> None: ...
    def SelectPane(
        self,
        pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane,
        select: bool,
        add: bool,
    ) -> None: ...
    def LineLeft(self) -> None: ...
    def PageLeft(self) -> None: ...
    def DrawBaseline(
        self,
        series: Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries,
        pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane,
        rect: System.Windows.Rect,
        sx: float,
        sy: float,
        ex: float,
        ey: float,
        pen: System.Windows.Media.Pen,
    ) -> List[System.Windows.Point]: ...
    def PageRight(self) -> None: ...
    def PageUp(self) -> None: ...
    def PageDown(self) -> None: ...
    def MakeVisible(
        self, visual: System.Windows.Media.Visual, rectangle: System.Windows.Rect
    ) -> System.Windows.Rect: ...
    def AutoScalePaneX(
        self, pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane
    ) -> None: ...
    def LineUp(self) -> None: ...
    def LineDown(self) -> None: ...
    def SetHorizontalOffset(self, offset: float) -> None: ...
    def LineRight(self) -> None: ...
    def GetSelectedPanes(
        self,
    ) -> List[Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane]: ...
    def MouseWheelLeft(self) -> None: ...
    def EnsurePaneVisible(self, row: int, column: int) -> None: ...
    def MouseWheelRight(self) -> None: ...
    def MouseWheelUp(self) -> None: ...
    def SetVerticalOffset(self, offset: float) -> None: ...
    def GetPaneFromPoint(
        self, point: System.Windows.Point
    ) -> Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane: ...
    def MouseWheelDown(self) -> None: ...

class GridPlotHitTest:  # Struct
    Location: Agilent.MassHunter.Quantitative.PlotControl.HitTestLocation
    Pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane

class GridPlotPane(System.Windows.DependencyObject):  # Class
    def __init__(
        self,
        content: Agilent.MassHunter.Quantitative.PlotControl.GridPlotContent,
        row: int,
        column: int,
    ) -> None: ...

    MaxXProperty: System.Windows.DependencyProperty  # static # readonly
    MaxYProperty: System.Windows.DependencyProperty  # static # readonly
    MinXProperty: System.Windows.DependencyProperty  # static # readonly
    MinYProperty: System.Windows.DependencyProperty  # static # readonly

    Bounds: System.Windows.Rect  # readonly
    Column: int  # readonly
    IsSelected: bool
    MaxX: float
    MaxY: float
    MinX: float
    MinY: float
    PlotAreaBounds: System.Windows.Rect  # readonly
    Row: int  # readonly
    Title: str
    TitleBounds: System.Windows.Rect  # readonly
    XAxisBounds: System.Windows.Rect  # readonly
    YAxisBounds: System.Windows.Rect  # readonly

class GridPlotShiftAxisAdorner(
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
        self,
        plot: Agilent.MassHunter.Quantitative.PlotControl.GridPlotContent,
        pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane,
        start: System.Windows.Point,
        vertical: bool,
    ) -> None: ...

class GridPlotStretchAxisAdorner(
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
        self,
        plot: Agilent.MassHunter.Quantitative.PlotControl.GridPlotContent,
        pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane,
        startPoint: System.Windows.Point,
        vertical: bool,
    ) -> None: ...

class GridPlotZoomAdorner(
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
        self,
        plot: Agilent.MassHunter.Quantitative.PlotControl.GridPlotContent,
        pane: Agilent.MassHunter.Quantitative.PlotControl.GridPlotPane,
        startPoint: System.Windows.Point,
    ) -> None: ...

class GridlineMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Visible: Agilent.MassHunter.Quantitative.PlotControl.GridlineMode = (
        ...
    )  # static # readonly
    ZeroLineOnly: Agilent.MassHunter.Quantitative.PlotControl.GridlineMode = (
        ...
    )  # static # readonly

class HitTestLocation(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    PlotArea: Agilent.MassHunter.Quantitative.PlotControl.HitTestLocation = (
        ...
    )  # static # readonly
    Title: Agilent.MassHunter.Quantitative.PlotControl.HitTestLocation = (
        ...
    )  # static # readonly
    XAxis: Agilent.MassHunter.Quantitative.PlotControl.HitTestLocation = (
        ...
    )  # static # readonly
    YAxis: Agilent.MassHunter.Quantitative.PlotControl.HitTestLocation = (
        ...
    )  # static # readonly

class IAxisContainer(object):  # Interface
    FontSize: float  # readonly

    def RecalcRects(self) -> None: ...
    def Invalidate(self) -> None: ...
    def CreateTypeface(self) -> System.Windows.Media.Typeface: ...

class IGraphics(object):  # Interface
    def DrawRectangle(
        self,
        brush: System.Windows.Media.Brush,
        pen: System.Windows.Media.Pen,
        rectangle: System.Windows.Rect,
    ) -> None: ...
    def DrawText(
        self,
        text: str,
        culture: System.Globalization.CultureInfo,
        flow: System.Windows.FlowDirection,
        typeface: System.Windows.Media.Typeface,
        emSize: float,
        brush: System.Windows.Media.Brush,
        alignment: System.Windows.TextAlignment,
        trimming: System.Windows.TextTrimming,
        maxTextWidth: Optional[float],
        pos: System.Windows.Point,
    ) -> None: ...
    def DrawPolyline(
        self, pen: System.Windows.Media.Pen, points: List[System.Windows.Point]
    ) -> None: ...
    def DrawEllipse(
        self,
        br: System.Windows.Media.Brush,
        pen: System.Windows.Media.Pen,
        center: System.Windows.Point,
        radiusX: float,
        radiusY: float,
    ) -> None: ...
    def DrawLine(
        self,
        pen: System.Windows.Media.Pen,
        s: System.Windows.Point,
        e: System.Windows.Point,
    ) -> None: ...
    def DrawPolygon(
        self,
        brush: System.Windows.Media.Brush,
        pen: System.Windows.Media.Pen,
        points: List[System.Windows.Point],
    ) -> None: ...
    def Pop(self) -> None: ...
    def PushClip(self, rect: System.Windows.Rect) -> None: ...
    def PushGuidelineSet(self, gs: System.Windows.Media.GuidelineSet) -> None: ...
    def PushTransform(self, transform: System.Windows.Media.Transform) -> None: ...
    @overload
    def MeasureString(
        self, text: str, typeface: System.Windows.Media.Typeface, emSize: float
    ) -> System.Windows.Size: ...
    @overload
    def MeasureString(
        self,
        text: str,
        typeface: System.Windows.Media.Typeface,
        emSize: float,
        width: float,
    ) -> System.Windows.Size: ...

class IPeaks(object):  # Interface
    PeakCount: int  # readonly
    PeakLabelsVisible: bool  # readonly

    def GetPeakBaselinePen(self, index: int) -> System.Windows.Media.Pen: ...
    def GetPeakLabel(self, index: int) -> str: ...
    def GetPeak(self, index: int) -> System.Windows.Point: ...
    def GetPeakLabelBrush(self, index: int) -> System.Windows.Media.Brush: ...
    def GetPeakFillBrush(self, index: int) -> System.Windows.Media.Brush: ...
    def GetBaseline(
        self, index: int, start: System.Windows.Point, end: System.Windows.Point
    ) -> None: ...

class IPlotBar(object):  # Interface
    def GetBarRange(self, index: int, start: float, end: float) -> None: ...
    def GetFillBrush(self, index: int) -> System.Windows.Media.Brush: ...
    def GetLinePen(self, index: int) -> System.Windows.Media.Pen: ...

class IPlotSeries(object):  # Interface
    Count: int  # readonly
    Pen: System.Windows.Media.Pen  # readonly
    PlotMode: Agilent.MassHunter.Quantitative.PlotControl.PlotMode  # readonly
    Visible: bool  # readonly

    def GetPoint(self, index: int, x: float, y: float) -> None: ...

class IZoomHistory(object):  # Interface
    CanRezoom: bool  # readonly
    CanUnzoom: bool  # readonly
    Capacity: int

    def Push(self) -> None: ...
    def Clear(self) -> None: ...
    def Rezoom(self) -> None: ...
    def Unzoom(self) -> None: ...

class LinkedRange(System.Windows.DependencyObject):  # Class
    def __init__(self) -> None: ...

    MaxValueProperty: System.Windows.DependencyProperty  # static # readonly
    MinValueProperty: System.Windows.DependencyProperty  # static # readonly

    MaxBinding: System.Windows.Data.Binding  # readonly
    MaxValue: float
    MinBinding: System.Windows.Data.Binding  # readonly
    MinValue: float

class MS(System.IO.MemoryStream, System.IDisposable):  # Class
    def __init__(self) -> None: ...

class PDFGraphics(
    System.IDisposable, Agilent.MassHunter.Quantitative.PlotControl.IGraphics
):  # Class
    def __init__(
        self,
        canvas: iTextSharp.text.pdf.PdfContentByte,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

    IgnoreFontName: bool

    @staticmethod
    def RegisterFont(name: str) -> None: ...
    def DrawRectangle(
        self,
        brush: System.Windows.Media.Brush,
        pen: System.Windows.Media.Pen,
        rectangle: System.Windows.Rect,
    ) -> None: ...
    @overload
    def DrawText(
        self,
        ft: System.Windows.Media.FormattedText,
        brush: System.Windows.Media.Brush,
        pos: System.Windows.Point,
    ) -> None: ...
    @overload
    def DrawText(
        self,
        text: str,
        culture: System.Globalization.CultureInfo,
        flow: System.Windows.FlowDirection,
        typeface: System.Windows.Media.Typeface,
        emSize: float,
        brush: System.Windows.Media.Brush,
        alignment: System.Windows.TextAlignment,
        trimming: System.Windows.TextTrimming,
        maxTextWidth: Optional[float],
        pos: System.Windows.Point,
    ) -> None: ...
    def DrawPolyline(
        self, pen: System.Windows.Media.Pen, points: List[System.Windows.Point]
    ) -> None: ...
    def DrawEllipse(
        self,
        br: System.Windows.Media.Brush,
        pen: System.Windows.Media.Pen,
        center: System.Windows.Point,
        radiusX: float,
        radiusY: float,
    ) -> None: ...
    def DrawLine(
        self,
        pen: System.Windows.Media.Pen,
        s: System.Windows.Point,
        e: System.Windows.Point,
    ) -> None: ...
    def DrawPolygon(
        self,
        brush: System.Windows.Media.Brush,
        pen: System.Windows.Media.Pen,
        points: List[System.Windows.Point],
    ) -> None: ...
    def Pop(self) -> None: ...
    def PushClip(self, rect: System.Windows.Rect) -> None: ...
    def PushGuidelineSet(self, gs: System.Windows.Media.GuidelineSet) -> None: ...
    def WPFtoPDF(
        self, element: System.Windows.FrameworkElement, w: float, h: float
    ) -> iTextSharp.text.Image: ...
    def PushTransform(self, transform: System.Windows.Media.Transform) -> None: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def FindFontFile(name: str, index: int) -> str: ...
    @overload
    def MeasureString(
        self, text: str, typeface: System.Windows.Media.Typeface, emSize: float
    ) -> System.Windows.Size: ...
    @overload
    def MeasureString(
        self,
        text: str,
        typeface: System.Windows.Media.Typeface,
        emSize: float,
        width: float,
    ) -> System.Windows.Size: ...

class PaneAxis(
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

    AxisLocationProperty: System.Windows.DependencyProperty  # static # readonly
    ExponentialTickLabelProperty: System.Windows.DependencyProperty  # static # readonly
    GridlineModeProperty: System.Windows.DependencyProperty  # static # readonly
    LabelBrushProperty: System.Windows.DependencyProperty  # static # readonly
    LineBrushProperty: System.Windows.DependencyProperty  # static # readonly
    MaxProperty: System.Windows.DependencyProperty  # static # readonly
    MinProperty: System.Windows.DependencyProperty  # static # readonly

    Arranging: bool
    AutoScaleMax: float
    AutoScaleMin: float
    AxisLocation: Agilent.MassHunter.Quantitative.PlotControl.AxisLocation
    ExponentialTickLabel: bool
    GridlineMode: Agilent.MassHunter.Quantitative.PlotControl.GridlineMode
    IsVertical: bool  # readonly
    LabelBrush: System.Windows.Media.Brush
    LineBrush: System.Windows.Media.Brush
    Max: float
    MeasuringGraphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics
    Min: float
    PlotControl: Agilent.MassHunter.Quantitative.PlotControl.PlotControl

    def DoAutoScale(self) -> None: ...
    def RenderAxis(
        self,
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        rect: System.Windows.Rect,
    ) -> None: ...

    AutoScale: System.EventHandler[
        Agilent.MassHunter.Quantitative.PlotControl.RangeEventArgs
    ]  # Event

class PaneAxisShiftAdorner(
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
        self,
        plotControl: Agilent.MassHunter.Quantitative.PlotControl.PlotControl,
        axis: Agilent.MassHunter.Quantitative.PlotControl.PaneAxis,
        startPoint: System.Windows.Point,
    ) -> None: ...

class PaneAxisStretchAdorner(
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
        self,
        plotControl: Agilent.MassHunter.Quantitative.PlotControl.PlotControl,
        axis: Agilent.MassHunter.Quantitative.PlotControl.PaneAxis,
        startPoint: System.Windows.Point,
    ) -> None: ...

class PaneSelectionMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Multiple: Agilent.MassHunter.Quantitative.PlotControl.PaneSelectionMode = (
        ...
    )  # static # readonly
    Single: Agilent.MassHunter.Quantitative.PlotControl.PaneSelectionMode = (
        ...
    )  # static # readonly

class PlotAxesControl(
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

    BottomAxis: Agilent.MassHunter.Quantitative.PlotControl.PaneAxis  # readonly
    BottomAxisLabel: System.Windows.Controls.TextBlock  # readonly
    LeftAxis: Agilent.MassHunter.Quantitative.PlotControl.PaneAxis  # readonly
    LeftAxisLabel: System.Windows.Controls.TextBlock  # readonly
    PlotControl: Agilent.MassHunter.Quantitative.PlotControl.PlotControl  # readonly
    Title: System.Windows.FrameworkElement

    def ClearAllBindings(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    def RenderData(
        self,
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        rect: System.Windows.Rect,
    ) -> None: ...

class PlotAxesControlBehavior(
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.IAttachedObject,
    System.Windows.Interactivity.Behavior[
        Agilent.MassHunter.Quantitative.PlotControl.PlotAxesControl
    ],
):  # Class
    def __init__(self) -> None: ...

    StartPoint: Optional[System.Windows.Point]

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

    DataSourceProperty: System.Windows.DependencyProperty  # static # readonly
    GridlinesBrushProperty: System.Windows.DependencyProperty  # static # readonly
    MaxXProperty: System.Windows.DependencyProperty  # static # readonly
    MaxYProperty: System.Windows.DependencyProperty  # static # readonly
    MinXProperty: System.Windows.DependencyProperty  # static # readonly
    MinYProperty: System.Windows.DependencyProperty  # static # readonly
    XGridlinesValuesProperty: System.Windows.DependencyProperty  # static # readonly
    YGridlinesValuesProperty: System.Windows.DependencyProperty  # static # readonly

    Arranging: bool
    DataSource: Any
    GridlinesBrush: System.Windows.Media.Brush
    MaxX: float
    MaxY: float
    MinX: float
    MinY: float
    PeakLabelsVertical: bool
    XGridlinesValues: List[float]
    YGridlinesValues: List[float]
    ZoomHistory: Agilent.MassHunter.Quantitative.PlotControl.IZoomHistory  # readonly

    def RenderSeriesTo(
        self,
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        series: Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries,
        rect: System.Windows.Rect,
    ) -> None: ...
    def RenderTo(
        self,
        graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics,
        rect: System.Windows.Rect,
    ) -> None: ...

    RenderData: System.EventHandler[
        Agilent.MassHunter.Quantitative.PlotControl.RenderDataEventArgs
    ]  # Event
    RenderSeries: System.EventHandler[
        Agilent.MassHunter.Quantitative.PlotControl.RenderSeriesEventArgs
    ]  # Event

class PlotControlZoomAdorner(
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
        self,
        plot: Agilent.MassHunter.Quantitative.PlotControl.PlotControl,
        startPoint: System.Windows.Point,
    ) -> None: ...

class PlotControlZoomHistory(
    Agilent.MassHunter.Quantitative.PlotControl.IZoomHistory
):  # Class
    def __init__(
        self, plotControl: Agilent.MassHunter.Quantitative.PlotControl.PlotControl
    ) -> None: ...

    CanRezoom: bool  # readonly
    CanUnzoom: bool  # readonly
    Capacity: int

    def Push(self) -> None: ...
    def Clear(self) -> None: ...
    def Rezoom(self) -> None: ...
    def Unzoom(self) -> None: ...

class PlotMode(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Bar: Agilent.MassHunter.Quantitative.PlotControl.PlotMode = ...  # static # readonly
    Connected: Agilent.MassHunter.Quantitative.PlotControl.PlotMode = (
        ...
    )  # static # readonly
    Line: Agilent.MassHunter.Quantitative.PlotControl.PlotMode = (
        ...
    )  # static # readonly

class PlotPeakSeries(
    Agilent.MassHunter.Quantitative.PlotControl.PointArrayPlotSeries,
    Agilent.MassHunter.Quantitative.PlotControl.IPeaks,
    Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries,
):  # Class
    def __init__(self) -> None: ...

    PeakCount: int  # readonly
    PeakLabelsVisible: bool

    def GetPeakBaselinePen(self, index: int) -> System.Windows.Media.Pen: ...
    def GetPeakLabel(self, index: int) -> str: ...
    def AddPeak(
        self,
        location: System.Windows.Point,
        start: System.Windows.Point,
        end: System.Windows.Point,
        fillBrush: System.Windows.Media.Brush,
        baselinePen: System.Windows.Media.Pen,
        label: str,
        labelBrush: System.Windows.Media.Brush,
    ) -> None: ...
    def GetPeak(self, index: int) -> System.Windows.Point: ...
    def GetPeakLabelBrush(self, index: int) -> System.Windows.Media.Brush: ...
    def ClearPeaks(self) -> None: ...
    def GetPeakFillBrush(self, index: int) -> System.Windows.Media.Brush: ...
    def GetBaseline(
        self, index: int, start: System.Windows.Point, end: System.Windows.Point
    ) -> None: ...

class PointArrayPlotSeries(
    Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries
):  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly
    Offset: float
    Pen: System.Windows.Media.Pen
    PlotMode: Agilent.MassHunter.Quantitative.PlotControl.PlotMode
    Points: List[System.Windows.Point]
    Scale: float
    Tag: Any
    Visible: bool

    def GetPoint(self, index: int, x: float, y: float) -> None: ...
    @overload
    def Normalize(self, maxValue: float) -> None: ...
    @overload
    def Normalize(self, minValue: float, maxValue: float) -> None: ...

class Range:  # Class
    def __init__(self) -> None: ...

    Max: float
    Min: float

class RangeEventArgs(System.EventArgs):  # Class
    def __init__(self) -> None: ...

    Handled: bool
    Range: Agilent.MassHunter.Quantitative.PlotControl.Range

class RenderDataEventArgs(System.EventArgs):  # Class
    def __init__(self) -> None: ...

    Graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics  # readonly
    Handled: bool
    Rect: System.Windows.Rect  # readonly

class RenderSeriesEventArgs(System.EventArgs):  # Class
    def __init__(self) -> None: ...

    Graphics: Agilent.MassHunter.Quantitative.PlotControl.IGraphics  # readonly
    Handled: bool
    Rect: System.Windows.Rect  # readonly
    Series: Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries  # readonly

class TitleLocation(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Center: Agilent.MassHunter.Quantitative.PlotControl.TitleLocation = (
        ...
    )  # static # readonly
    Far: Agilent.MassHunter.Quantitative.PlotControl.TitleLocation = (
        ...
    )  # static # readonly
    Near: Agilent.MassHunter.Quantitative.PlotControl.TitleLocation = (
        ...
    )  # static # readonly

class TransformState(
    Agilent.MassHunter.Quantitative.PlotControl.GraphicsState
):  # Class
    def __init__(self, transform: System.Windows.Media.Transform) -> None: ...
    def Push(self, canvas: iTextSharp.text.pdf.PdfContentByte) -> None: ...
    def Pop(self, canvas: iTextSharp.text.pdf.PdfContentByte) -> None: ...

class Utils:  # Class
    @overload
    @staticmethod
    def HitTest(
        plot: Agilent.MassHunter.Quantitative.PlotControl.GridPlotContent,
        point: System.Windows.Point,
    ) -> Agilent.MassHunter.Quantitative.PlotControl.GridPlotHitTest: ...
    @overload
    @staticmethod
    def HitTest(
        control: Agilent.MassHunter.Quantitative.PlotControl.PlotAxesControl,
        position: System.Windows.Point,
    ) -> Agilent.MassHunter.Quantitative.PlotControl.HitTestLocation: ...
    @overload
    @staticmethod
    def HitTest(
        element: System.Windows.FrameworkElement, point: System.Windows.Point
    ) -> bool: ...
