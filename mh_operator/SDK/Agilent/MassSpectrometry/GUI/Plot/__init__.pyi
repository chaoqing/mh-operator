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

from . import Events, Exactify, TofDataBrowser
from .Events import DrawPaneEventArgs, ZoomHistoryEventArgs

# Stubs for namespace: Agilent.MassSpectrometry.GUI.Plot

class Axis(System.IDisposable):  # Class
    SeparateExponentFormat: str = ...  # static # readonly

    Bounds: System.Drawing.Rectangle  # readonly
    Clip: bool
    Color: System.Drawing.Color
    DashStyle: System.Drawing.Drawing2D.DashStyle
    EndPoint: System.Drawing.Point  # readonly
    ExponentLabelOffset: int
    Extent: int
    IsHorizontal: bool  # readonly
    IsLogScale: bool
    IsSecondary: bool  # readonly
    LineThickness: int
    MajorTickInterval: float
    MajorTickLabelVisible: bool
    MajorTickSize: int
    MajorTickVisible: bool
    Marker: Agilent.MassSpectrometry.GUI.Plot.AxisMarker  # readonly
    MaxClipValue: Optional[float]
    MaxValue: float
    MinValue: float
    MinorTickLabelVisible: bool
    MinorTickSize: int
    MinorTickVisible: bool
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    PreferredRangeLimit: Agilent.MassSpectrometry.GUI.Plot.PlotRange  # readonly
    StartPoint: System.Drawing.Point  # readonly
    TickLabelColor: System.Drawing.Color
    TickLabelFont: System.Drawing.Font
    TickLabelFormat: str
    TickLabelHorizontalAlignment: System.Drawing.StringAlignment
    TickLabelVerticalAlignment: System.Drawing.StringAlignment
    Title: Agilent.MassSpectrometry.GUI.Plot.TitleBase  # readonly
    Visible: bool

    def DataToCoordinate(self, d: float) -> int: ...
    def CoordinateToData(self, c: int) -> float: ...
    def ExponentTickString(self, y: float, log: float, rootFormat: str) -> str: ...
    def DataToCoordinateD(self, d: float) -> float: ...
    def AutoScale(self) -> None: ...
    def PaneCoordinateToControlCoordinate(self, c: int) -> int: ...
    def ControlCoordinateToPaneCoordinate(self, c: int) -> int: ...
    def TickString(self, data: float) -> str: ...
    def Dispose(self) -> None: ...

class AxisMarker:  # Class
    Color: System.Drawing.Color
    Size: int
    Type: Agilent.MassSpectrometry.GUI.Plot.AxisMarkerType
    Value: float
    Visible: bool

class AxisMarkerType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Triangle: Agilent.MassSpectrometry.GUI.Plot.AxisMarkerType = (
        ...
    )  # static # readonly

class BoxRubberBand(
    Agilent.MassSpectrometry.EventManipulating.Model.IRubberBand,
    System.IDisposable,
    Agilent.MassSpectrometry.EventManipulating.RubberBand,
):  # Class
    @overload
    def __init__(self, startPoint: System.Drawing.Point) -> None: ...
    @overload
    def __init__(
        self, startPoint: System.Drawing.Point, region: System.Drawing.Rectangle
    ) -> None: ...

    Region: System.Drawing.Rectangle  # readonly
    StartPoint: System.Drawing.Point  # readonly

    def MoveTo(
        self, ctrl: System.Windows.Forms.Control, position: System.Drawing.Point
    ) -> None: ...

class BoxZoomEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    Agilent.MassSpectrometry.GUI.Plot.PlotEventManipulatorBase,
    System.IDisposable,
):  # Class
    def __init__(
        self, context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext
    ) -> None: ...
    def OnDragEnd(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...
    def OnDragStart(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        startPoint: System.Drawing.Point,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...
    def OnMouseMove(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...

class CircleMarker(Agilent.MassSpectrometry.GUI.Plot.FillableMarker):  # Class
    def __init__(self) -> None: ...
    def Draw(self, plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane) -> None: ...

class DefaultEventManipulatorBase(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    Agilent.MassSpectrometry.GUI.Plot.PlotEventManipulatorBase,
    System.IDisposable,
):  # Class
    def __init__(
        self, context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext
    ) -> None: ...
    def OnKeyDown(self, sender: Any, e: System.Windows.Forms.KeyEventArgs) -> None: ...

class FillBoxRubberBand(
    Agilent.MassSpectrometry.EventManipulating.Model.IRubberBand,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.BoxRubberBand,
):  # Class
    @overload
    def __init__(self, startPoint: System.Drawing.Point) -> None: ...
    @overload
    def __init__(
        self, startPoint: System.Drawing.Point, region: System.Drawing.Rectangle
    ) -> None: ...

class FillableMarker(Agilent.MassSpectrometry.GUI.Plot.Marker):  # Class
    LineColor: System.Drawing.Color
    LineWidth: int
    LineWidthF: float

class GraphicsHelper:  # Class
    @staticmethod
    def FillRectangleInvert(
        g: System.Drawing.Graphics,
        left: int,
        top: int,
        right: int,
        bottom: int,
        color: System.Drawing.Color,
    ) -> None: ...
    @staticmethod
    def DrawLineInvert(
        g: System.Drawing.Graphics,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        color: System.Drawing.Color,
    ) -> None: ...
    @staticmethod
    def CreateInvertBitmap(
        bmp: System.Drawing.Bitmap, rectangle: System.Drawing.Rectangle
    ) -> System.Drawing.Bitmap: ...
    @staticmethod
    def DrawRectangleInvert(
        g: System.Drawing.Graphics,
        left: int,
        top: int,
        right: int,
        bottom: int,
        color: System.Drawing.Color,
    ) -> None: ...
    @staticmethod
    def DrawStringInvert(
        g: System.Drawing.Graphics,
        s: str,
        font: System.Drawing.Font,
        color: System.Drawing.Color,
        x: int,
        y: int,
    ) -> None: ...
    @staticmethod
    def DrawPlotControlImage(
        ctrl: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        rectangle: System.Drawing.Rectangle,
        rectangleInvert: System.Drawing.Rectangle,
    ) -> None: ...
    @staticmethod
    def DrawStringBottomUp(
        g: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        text: str,
        font: System.Drawing.Font,
        br: System.Drawing.Brush,
        bounds: System.Drawing.RectangleF,
        sf: System.Drawing.StringFormat,
    ) -> None: ...

class GraphicsWrap(Agilent.MassSpectrometry.GUI.Plot.IGraphics):  # Class
    def __init__(self, g: System.Drawing.Graphics) -> None: ...

    Clip: System.Drawing.Region
    Graphics: System.Drawing.Graphics  # readonly
    HasGraphics: bool  # readonly

    @overload
    def FillRectangle(
        self, brush: System.Drawing.Brush, rect: System.Drawing.RectangleF
    ) -> None: ...
    @overload
    def FillRectangle(
        self,
        brush: System.Drawing.Brush,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def DrawRectangle(
        self, pen: System.Drawing.Pen, x: float, y: float, width: float, height: float
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
        self, pen: System.Drawing.Pen, x1: float, y1: float, x2: float, y2: float
    ) -> None: ...
    @overload
    def DrawLine(
        self,
        pen: System.Drawing.Pen,
        p1: System.Drawing.PointF,
        p2: System.Drawing.PointF,
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
        rect: System.Drawing.RectangleF,
        format: System.Drawing.StringFormat,
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

class Gridlines:  # Class
    Color: System.Drawing.Color
    DashStyle: System.Drawing.Drawing2D.DashStyle
    Thickness: int
    Visible: bool

class HitTestInfo:  # Class
    def __init__(self) -> None: ...

    Column: int
    Pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    Row: int
    Type: Agilent.MassSpectrometry.GUI.Plot.HitTestType

class HitTestType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    LinkedXAxis: Agilent.MassSpectrometry.GUI.Plot.HitTestType = (
        ...
    )  # static # readonly
    LinkedXAxisTitle: Agilent.MassSpectrometry.GUI.Plot.HitTestType = (
        ...
    )  # static # readonly
    LinkedY2Axis: Agilent.MassSpectrometry.GUI.Plot.HitTestType = (
        ...
    )  # static # readonly
    LinkedYAxis: Agilent.MassSpectrometry.GUI.Plot.HitTestType = (
        ...
    )  # static # readonly
    LinkedYAxisTitle: Agilent.MassSpectrometry.GUI.Plot.HitTestType = (
        ...
    )  # static # readonly
    LowerLeft: Agilent.MassSpectrometry.GUI.Plot.HitTestType = ...  # static # readonly
    PlotArea: Agilent.MassSpectrometry.GUI.Plot.HitTestType = ...  # static # readonly
    TopTitle: Agilent.MassSpectrometry.GUI.Plot.HitTestType = ...  # static # readonly
    XAxis: Agilent.MassSpectrometry.GUI.Plot.HitTestType = ...  # static # readonly
    XAxisMarker: Agilent.MassSpectrometry.GUI.Plot.HitTestType = (
        ...
    )  # static # readonly
    XAxisTitle: Agilent.MassSpectrometry.GUI.Plot.HitTestType = ...  # static # readonly
    Y2Axis: Agilent.MassSpectrometry.GUI.Plot.HitTestType = ...  # static # readonly
    Y2AxisTitle: Agilent.MassSpectrometry.GUI.Plot.HitTestType = (
        ...
    )  # static # readonly
    YAxis: Agilent.MassSpectrometry.GUI.Plot.HitTestType = ...  # static # readonly
    YAxisMarker: Agilent.MassSpectrometry.GUI.Plot.HitTestType = (
        ...
    )  # static # readonly
    YAxisTitle: Agilent.MassSpectrometry.GUI.Plot.HitTestType = ...  # static # readonly

class ICustomDrawPeakLabels(object):  # Interface
    def DrawLabel(
        self,
        plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane,
        font: System.Drawing.Font,
        rect: System.Drawing.RectangleF,
        color: System.Drawing.Color,
        text: str,
        x: float,
        y: float,
    ) -> None: ...
    def MeasureLabel(
        self,
        plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane,
        font: System.Drawing.Font,
        text: str,
        x: float,
        y: float,
    ) -> System.Drawing.RectangleF: ...

class ICustomDrawPeakLabelsEx(object):  # Interface
    def DrawLabel(
        self,
        plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane,
        font: System.Drawing.Font,
        rect: System.Drawing.RectangleF,
        color: System.Drawing.Color,
        text: str,
        x: float,
        y: float,
        series: int,
        peakIndex: int,
    ) -> None: ...
    def MeasureLabel(
        self,
        plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane,
        font: System.Drawing.Font,
        text: str,
        x: float,
        y: float,
        series: int,
        peakIndex: int,
    ) -> System.Drawing.RectangleF: ...

class IGraphics(object):  # Interface
    Clip: System.Drawing.Region
    Graphics: System.Drawing.Graphics  # readonly
    HasGraphics: bool  # readonly

    @overload
    def FillRectangle(
        self, brush: System.Drawing.Brush, rect: System.Drawing.RectangleF
    ) -> None: ...
    @overload
    def FillRectangle(
        self,
        brush: System.Drawing.Brush,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def DrawRectangle(
        self, pen: System.Drawing.Pen, x: float, y: float, width: float, height: float
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
        self, pen: System.Drawing.Pen, x1: float, y1: float, x2: float, y2: float
    ) -> None: ...
    @overload
    def DrawLine(
        self,
        pen: System.Drawing.Pen,
        p1: System.Drawing.PointF,
        p2: System.Drawing.PointF,
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
        rect: System.Drawing.RectangleF,
        format: System.Drawing.StringFormat,
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

class IManualIntegration(object):  # Interface
    def HitTest(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, point: System.Drawing.Point
    ) -> Agilent.MassSpectrometry.GUI.Plot.ManualIntegrationType: ...
    def GetRubberBandPoints(
        self,
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        startPoint: System.Drawing.Point,
        point: System.Drawing.Point,
        modifierKeys: System.Windows.Forms.Keys,
    ) -> List[System.Drawing.Point]: ...
    def EndIntegration(
        self,
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        startPoint: System.Drawing.Point,
        point: System.Drawing.Point,
        modifierKeys: System.Windows.Forms.Keys,
    ) -> None: ...
    def StartIntegration(
        self,
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        point: System.Drawing.Point,
        modifierKeys: System.Windows.Forms.Keys,
    ) -> None: ...

class IMarkerData(object):  # Interface
    def GetMarker(
        self,
        index: int,
        x: float,
        y: float,
        marker: Agilent.MassSpectrometry.GUI.Plot.Marker,
    ) -> None: ...
    def GetCount(self) -> int: ...
    def DisplayMarker(self, index: int) -> bool: ...

class IPeakData(object):  # Interface
    def DisplayLabel(
        self, series: int, peak: int, label: str, color: System.Drawing.Color
    ) -> bool: ...
    def GetPeakCount(self, series: int) -> int: ...
    def GetPeak(self, series: int, peak: int, x: float, y: float) -> None: ...
    def DisplayMarker(
        self, series: int, peak: int, marker: Agilent.MassSpectrometry.GUI.Plot.Marker
    ) -> bool: ...
    def Fill(
        self,
        series: int,
        peak: int,
        startPlotIndex: int,
        endPlotIndex: int,
        startBaselineX: float,
        startBaselineY: float,
        endBaselineX: float,
        endBaselineY: float,
        baselineColor: System.Drawing.Color,
        fillColor: System.Drawing.Color,
    ) -> bool: ...

class IPlotBar(object):  # Interface
    def GetBarWidth(self, series: int, index: int) -> float: ...
    def GetLineColor(self, series: int, index: int) -> System.Drawing.Color: ...
    def GetFillColor(self, series: int, index: int) -> System.Drawing.Color: ...
    def GetWidthIsVdc(self, series: int, index: int) -> bool: ...

class IPlotData(object):  # Interface
    def GetPointCount(self, series: int) -> int: ...
    def GetSeriesCount(self) -> int: ...
    def DisplaySeries(self, series: int) -> bool: ...
    def GetPoint(self, series: int, pointIndex: int, x: float, y: float) -> None: ...
    def GetSeriesLineStyle(
        self,
        series: int,
        mode: Agilent.MassSpectrometry.GUI.Plot.PlotModes,
        color: System.Drawing.Color,
        style: System.Drawing.Drawing2D.DashStyle,
        width: int,
    ) -> None: ...

class IPlotDataAxisAssoc(object):  # Interface
    def IsSecondaryY(self, series: int) -> bool: ...

class IPlotDataF(object):  # Interface
    def GetSeriesLineStyleF(
        self,
        series: int,
        mode: Agilent.MassSpectrometry.GUI.Plot.PlotModes,
        color: System.Drawing.Color,
        style: System.Drawing.Drawing2D.DashStyle,
        width: float,
    ) -> None: ...

class IPlotDataLineStyleSegments(object):  # Interface
    def GetSegment(
        self,
        series: int,
        segment: int,
        startIndex: int,
        endIndex: int,
        color: System.Drawing.Color,
        style: System.Drawing.Drawing2D.DashStyle,
        width: int,
    ) -> None: ...
    def GetSegmentCount(self, series: int) -> int: ...

class IPlotDataLineStyleSegmentsF(object):  # Interface
    def GetSegment(
        self,
        series: int,
        segment: int,
        startIndex: int,
        endIndex: int,
        color: System.Drawing.Color,
        style: System.Drawing.Drawing2D.DashStyle,
        width: float,
    ) -> None: ...

class IPlotShiftData(object):  # Interface
    def ShiftX(self, series: int) -> int: ...
    def ShiftY(self, series: int) -> int: ...

class LinkedAxis(System.IDisposable, Agilent.MassSpectrometry.GUI.Plot.Axis):  # Class
    Bounds: System.Drawing.Rectangle  # readonly
    Color: System.Drawing.Color
    DashStyle: System.Drawing.Drawing2D.DashStyle
    Extent: int
    Index: int  # readonly
    IsHorizontal: bool  # readonly
    IsLogScale: bool
    IsSecondary: bool  # readonly
    LineThickness: int
    MajorTickLabelVisible: bool
    MajorTickVisible: bool
    MaxValue: float
    MinValue: float
    MinorTickLabelVisible: bool
    MinorTickVisible: bool
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    PreferredRangeLimit: Agilent.MassSpectrometry.GUI.Plot.PlotRange  # readonly
    TickLabelColor: System.Drawing.Color
    TickLabelFont: System.Drawing.Font
    TickLabelFormat: str
    TickLabelHorizontalAlignment: System.Drawing.StringAlignment
    TickLabelVerticalAlignment: System.Drawing.StringAlignment
    Title: Agilent.MassSpectrometry.GUI.Plot.TitleBase  # readonly
    Visible: bool

    def CoordinateToData(self, c: int) -> float: ...
    def PaneCoordinateToControlCoordinate(self, c: int) -> int: ...
    def AutoScale(self) -> None: ...
    def ControlCoordinateToPaneCoordinate(self, c: int) -> int: ...

class LinkedAxisCollection(
    Iterable[Any],
    System.IDisposable,
    Iterable[Agilent.MassSpectrometry.GUI.Plot.LinkedAxis],
):  # Class
    Clip: bool
    Count: int  # readonly
    Extent: int
    IsHorizontal: bool  # readonly
    IsSecondary: bool  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.GUI.Plot.LinkedAxis: ...
    LinkAll: bool
    Pivot: bool
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    TitlesFont: System.Drawing.Font
    TitlesVisible: bool
    Visible: bool

    def GetEnumerator(self) -> Iterator[Any]: ...
    def Dispose(self) -> None: ...

class ManualIntegrationEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    Agilent.MassSpectrometry.GUI.Plot.PlotEventManipulatorBase,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext,
        manualIntegration: Agilent.MassSpectrometry.GUI.Plot.IManualIntegration,
    ) -> None: ...
    def OnDragEnd(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...
    def OnDragStart(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        startPoint: System.Drawing.Point,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...
    def OnKeyDown(self, sender: Any, e: System.Windows.Forms.KeyEventArgs) -> None: ...
    def OnKeyUp(self, sender: Any, e: System.Windows.Forms.KeyEventArgs) -> None: ...

class ManualIntegrationRubberBand(
    Agilent.MassSpectrometry.EventManipulating.Model.IRubberBand,
    System.IDisposable,
    Agilent.MassSpectrometry.EventManipulating.RubberBand,
):  # Class
    def __init__(
        self,
        manualIntegration: Agilent.MassSpectrometry.GUI.Plot.IManualIntegration,
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        startPoint: System.Drawing.Point,
        defaultCursor: System.Windows.Forms.Cursor,
    ) -> None: ...
    def MoveTo(
        self, ctrl: System.Windows.Forms.Control, position: System.Drawing.Point
    ) -> None: ...

class ManualIntegrationType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    EndPoint: Agilent.MassSpectrometry.GUI.Plot.ManualIntegrationType = (
        ...
    )  # static # readonly
    NewPeak: Agilent.MassSpectrometry.GUI.Plot.ManualIntegrationType = (
        ...
    )  # static # readonly
    StartPoint: Agilent.MassSpectrometry.GUI.Plot.ManualIntegrationType = (
        ...
    )  # static # readonly

class Marker:  # Class
    Color: System.Drawing.Color
    MaxX: float  # readonly
    MinX: float  # readonly
    Size: int
    SizeF: float
    X: float
    Y: float

    def Draw(self, plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane) -> None: ...

class ObjectTrack:  # Class
    @staticmethod
    def Created(obj: Any) -> None: ...
    @staticmethod
    def Disposed(obj: Any) -> None: ...
    @staticmethod
    def Dump() -> None: ...
    @staticmethod
    def Finalized(obj: Any) -> None: ...

class Pane(System.IDisposable):  # Class
    AxisX: Agilent.MassSpectrometry.GUI.Plot.PaneAxis  # readonly
    AxisY: Agilent.MassSpectrometry.GUI.Plot.PaneAxis  # readonly
    AxisY2: Agilent.MassSpectrometry.GUI.Plot.PaneAxis  # readonly
    BackColor: System.Drawing.Color
    BorderWidth: int
    Bounds: System.Drawing.Rectangle  # readonly
    Column: int  # readonly
    DrawMarkers: bool
    DrawPeakMarkers: bool
    FillPeaks: bool
    Height: int  # readonly
    Linked: bool
    Location: System.Drawing.Point  # readonly
    MarkerData: Agilent.MassSpectrometry.GUI.Plot.IMarkerData
    PeakData: Agilent.MassSpectrometry.GUI.Plot.IPeakData
    PeakLabels: Agilent.MassSpectrometry.GUI.Plot.PeakLabels  # readonly
    PlotArea: Agilent.MassSpectrometry.GUI.Plot.PlotArea  # readonly
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    PlotData: Agilent.MassSpectrometry.GUI.Plot.IPlotData
    RightMargin: int
    Row: int  # readonly
    Selected: bool
    Title: Agilent.MassSpectrometry.GUI.Plot.PaneTitle  # readonly
    Width: int  # readonly
    XLinked: bool
    YLinked: bool
    YLinkedVertically: bool

    def ControlPointToPanePoint(
        self, p: System.Drawing.Point
    ) -> System.Drawing.Point: ...
    def SetDirty(self) -> None: ...
    def Paint(
        self,
        g: System.Drawing.Graphics,
        left: int,
        top: int,
        width: int,
        height: int,
        clipRectangle: System.Drawing.Rectangle,
    ) -> None: ...
    def DataToPoint(self, x: float, y: float) -> System.Drawing.Point: ...
    def HitTest(
        self, p: System.Drawing.Point
    ) -> Agilent.MassSpectrometry.GUI.Plot.HitTestType: ...
    def PanePointToControlPoint(
        self, p: System.Drawing.Point
    ) -> System.Drawing.Point: ...
    def EnsureVisible(self) -> None: ...
    @overload
    def DrawTo(
        self,
        g: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        left: int,
        top: int,
        width: int,
        height: int,
    ) -> None: ...
    @overload
    def DrawTo(
        self, g: System.Drawing.Graphics, left: int, top: int, width: int, height: int
    ) -> None: ...
    @overload
    def DrawTo(
        self,
        g: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        left: int,
        top: int,
        width: int,
        height: int,
        ignoreLinkedAxes: bool,
        paintBackground: bool,
    ) -> None: ...
    @overload
    def DrawTo(
        self,
        g: System.Drawing.Graphics,
        left: int,
        top: int,
        width: int,
        height: int,
        ignoreLinkedAxes: bool,
        paintBackground: bool,
    ) -> None: ...
    @overload
    def DrawTo(
        self,
        g: System.Drawing.Graphics,
        left: int,
        top: int,
        width: int,
        height: int,
        ignoreLinkedAxisX: bool,
        ignoreLinkedAxisY: bool,
        ignoreLinkedAxisY2: bool,
        paintBackground: bool,
    ) -> None: ...
    @overload
    def DrawTo(
        self,
        g: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        left: int,
        top: int,
        width: int,
        height: int,
        ignoreLinkedAxisX: bool,
        ignoreLinkedAxisY: bool,
        ignoreLinkedAxisY2: bool,
        paintBackground: bool,
    ) -> None: ...
    def DataToPointF(self, x: float, y: float) -> System.Drawing.PointF: ...
    def Dispose(self) -> None: ...
    def Invalidate(self) -> None: ...
    def PointToData(self, point: System.Drawing.Point, x: float, y: float) -> None: ...

class PaneAxis(System.IDisposable, Agilent.MassSpectrometry.GUI.Plot.Axis):  # Class
    Bounds: System.Drawing.Rectangle  # readonly
    Color: System.Drawing.Color
    DashStyle: System.Drawing.Drawing2D.DashStyle
    DrawZeroLine: bool
    Extent: int
    IsHorizontal: bool  # readonly
    IsLogScale: bool
    IsSecondary: bool  # readonly
    LineThickness: int
    MajorGridlines: Agilent.MassSpectrometry.GUI.Plot.Gridlines  # readonly
    MajorTickLabelVisible: bool
    MajorTickVisible: bool
    MaxValue: float
    MinValue: float
    MinorGridlines: Agilent.MassSpectrometry.GUI.Plot.Gridlines  # readonly
    MinorTickLabelVisible: bool
    MinorTickVisible: bool
    Pane: Agilent.MassSpectrometry.GUI.Plot.Pane  # readonly
    PlotControl: Agilent.MassSpectrometry.GUI.Plot.PlotControl  # readonly
    PreferredRangeLimit: Agilent.MassSpectrometry.GUI.Plot.PlotRange  # readonly
    TickLabelColor: System.Drawing.Color
    TickLabelFont: System.Drawing.Font
    TickLabelFormat: str
    TickLabelHorizontalAlignment: System.Drawing.StringAlignment
    TickLabelVerticalAlignment: System.Drawing.StringAlignment
    Title: Agilent.MassSpectrometry.GUI.Plot.TitleBase  # readonly
    Visible: bool

    def PaneCoordinateToControlCoordinate(self, c: int) -> int: ...
    def AutoScale(self) -> None: ...
    def ControlCoordinateToPaneCoordinate(self, c: int) -> int: ...

class PaneCollection(System.IDisposable, Iterable[Any]):  # Class
    ColumnCount: int
    def __getitem__(
        self, row: int, column: int
    ) -> Agilent.MassSpectrometry.GUI.Plot.Pane: ...
    def __setitem__(
        self, row: int, column: int, value_: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> None: ...
    RowCount: int

    def Contains(self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane) -> bool: ...
    def Clear(self) -> None: ...
    def CreateNew(self) -> Agilent.MassSpectrometry.GUI.Plot.Pane: ...
    def Dispose(self) -> None: ...
    @overload
    def SetDimension(self, rowCount: int, columnCount: int) -> None: ...
    @overload
    def SetDimension(
        self,
        rowCount: int,
        columnCount: int,
        disposeUnusedPanes: bool,
        createNewPanes: bool,
    ) -> None: ...

class PaneDataObject:  # Class
    @overload
    @staticmethod
    def PutPaneImageOnClipboard(
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
    ) -> None: ...
    @overload
    @staticmethod
    def PutPaneImageOnClipboard(
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        dataObject: System.Windows.Forms.DataObject,
    ) -> None: ...
    @overload
    @staticmethod
    def PutPageImageOnClipboard(
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
    ) -> None: ...
    @overload
    @staticmethod
    def PutPageImageOnClipboard(
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        dataObject: System.Windows.Forms.DataObject,
    ) -> None: ...

class PaneRange:  # Struct
    def __init__(
        self,
        x: Agilent.MassSpectrometry.GUI.Plot.PlotRange,
        y: Agilent.MassSpectrometry.GUI.Plot.PlotRange,
    ) -> None: ...

    XRange: Agilent.MassSpectrometry.GUI.Plot.PlotRange
    YRange: Agilent.MassSpectrometry.GUI.Plot.PlotRange

    def GetHashCode(self) -> int: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(self, range: Agilent.MassSpectrometry.GUI.Plot.PaneRange) -> bool: ...

class PaneSelectionMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Multiple: Agilent.MassSpectrometry.GUI.Plot.PaneSelectionMode = (
        ...
    )  # static # readonly
    Single: Agilent.MassSpectrometry.GUI.Plot.PaneSelectionMode = (
        ...
    )  # static # readonly

class PaneTitle(Agilent.MassSpectrometry.GUI.Plot.TitleBase):  # Class
    Alignment: System.Drawing.StringAlignment
    BackColor: System.Drawing.Color
    Bounds: System.Drawing.Rectangle  # readonly
    Color: System.Drawing.Color
    Extent: int
    Font: System.Drawing.Font
    LineAlignment: System.Drawing.StringAlignment
    Orientation: Agilent.MassSpectrometry.GUI.Plot.TextOrientation
    Text: str
    Trimming: System.Drawing.StringTrimming
    Visible: bool
    Wrap: bool

    def SetTabStops(self, firstTabOffset: float, tabStops: List[float]) -> None: ...
    def GetTabStops(self, firstTabOffset: float) -> List[float]: ...
    def SetExtentWithoutInvalidate(self, extent: int) -> None: ...

class PeakBaseRegionsMarker(Agilent.MassSpectrometry.GUI.Plot.Marker):  # Class
    def __init__(self) -> None: ...

    Base1End: Optional[float]
    Base1Start: Optional[float]
    Base2End: Optional[float]
    Base2Start: Optional[float]
    BaselineOffset: float
    BaselineStandardDiviation: float
    BoldTrace: bool
    BoldTraceWidth: float
    DisplayBoxes: bool
    DisplayTickMarks: bool
    EndX: float
    EndY: float
    MaxX: float  # readonly
    MinX: float  # readonly
    PlotData: Agilent.MassSpectrometry.GUI.Plot.IPlotData
    Series: int
    StartX: float
    StartY: float
    TickMarkColor: System.Drawing.Color

    def Draw(self, plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane) -> None: ...

class PeakLabelMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    All: Agilent.MassSpectrometry.GUI.Plot.PeakLabelMode = ...  # static # readonly
    HighestPeaks: Agilent.MassSpectrometry.GUI.Plot.PeakLabelMode = (
        ...
    )  # static # readonly
    NonOverlap: Agilent.MassSpectrometry.GUI.Plot.PeakLabelMode = (
        ...
    )  # static # readonly

class PeakLabels:  # Class
    CustomDraw: Agilent.MassSpectrometry.GUI.Plot.ICustomDrawPeakLabels
    CustomDrawEx: Agilent.MassSpectrometry.GUI.Plot.ICustomDrawPeakLabelsEx
    Font: System.Drawing.Font
    Mode: Agilent.MassSpectrometry.GUI.Plot.PeakLabelMode
    ModeParameter: int
    Vertical: bool
    Visible: bool

class PlotArea:  # Class
    BackColor: System.Drawing.Color
    BottomMargin: int
    Bounds: System.Drawing.Rectangle  # readonly
    InnerBounds: System.Drawing.Rectangle  # readonly

class PlotControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.Control,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

    MinXZoomRange: float = ...  # static # readonly
    MinYZoomRange: float = ...  # static # readonly

    AnchorColumns: int
    AnchorPaneMargin: int
    AnchorRows: int
    AnchorSeparator: bool
    DefaultPlotAreaBackColor: System.Drawing.Color
    DrawingRectangle: System.Drawing.Rectangle  # readonly
    FirstVisibleColumn: int
    FirstVisibleRow: int
    LinkedAxesX: Agilent.MassSpectrometry.GUI.Plot.LinkedAxisCollection  # readonly
    LinkedAxesY: Agilent.MassSpectrometry.GUI.Plot.LinkedAxisCollection  # readonly
    LinkedAxesY2: Agilent.MassSpectrometry.GUI.Plot.LinkedAxisCollection  # readonly
    LinkedAxesYVertically: (
        Agilent.MassSpectrometry.GUI.Plot.LinkedAxisCollection
    )  # readonly
    NumColumnsPerPage: int
    NumRowsPerPage: int
    PaneBorderColor: System.Drawing.Color
    PaneSelectionMode: Agilent.MassSpectrometry.GUI.Plot.PaneSelectionMode
    Panes: Agilent.MassSpectrometry.GUI.Plot.PaneCollection  # readonly
    PanesRectangle: System.Drawing.Rectangle  # readonly
    SelectedPaneBorderColor: System.Drawing.Color
    SuppressOmitDrawing: bool
    ZoomHistory: Agilent.MassSpectrometry.GUI.Plot.ZoomHistory  # readonly

    def UnselectAllPanes(self) -> None: ...
    def GetPreferredYRangeLimit(
        self, row: int, column: int
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def EndInit(self) -> None: ...
    def PaneIndexFromPoint(
        self, point: System.Drawing.Point, row: int, column: int
    ) -> None: ...
    @overload
    def DrawPageTo(
        self, g: System.Drawing.Graphics, rect: System.Drawing.Rectangle
    ) -> None: ...
    @overload
    def DrawPageTo(
        self,
        g: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        rect: System.Drawing.Rectangle,
    ) -> None: ...
    @overload
    def DrawPageTo(
        self,
        g: System.Drawing.Graphics,
        rect: System.Drawing.Rectangle,
        startRow: int,
        startCol: int,
    ) -> None: ...
    @overload
    def DrawPageTo(
        self,
        g: System.Drawing.Graphics,
        rect: System.Drawing.Rectangle,
        startRow: int,
        startCol: int,
        paintBackground: bool,
    ) -> None: ...
    @overload
    def DrawPageTo(
        self,
        g: System.Drawing.Graphics,
        rect: System.Drawing.Rectangle,
        startRow: int,
        startCol: int,
        paintBackground: bool,
        anchoring: bool,
    ) -> None: ...
    @overload
    def DrawPageTo(
        self,
        g: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        rect: System.Drawing.Rectangle,
        startRow: int,
        startCol: int,
        paintBackground: bool,
    ) -> None: ...
    @overload
    def DrawPageTo(
        self,
        g: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        rect: System.Drawing.Rectangle,
        startRow: int,
        startCol: int,
        paintBackground: bool,
        anchoring: bool,
    ) -> None: ...
    def GetAutoScaleRangeX(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def PrintPage(
        self,
        g: System.Drawing.Graphics,
        clientRectangle: System.Drawing.Rectangle,
        startRow: int,
        startCol: int,
    ) -> None: ...
    def BeginInit(self) -> None: ...
    def HitTest(
        self, point: System.Drawing.Point
    ) -> Agilent.MassSpectrometry.GUI.Plot.HitTestInfo: ...
    def PaneFromPoint(
        self, point: System.Drawing.Point
    ) -> Agilent.MassSpectrometry.GUI.Plot.Pane: ...
    def EnsureRowVisible(self, row: int) -> None: ...
    def GetSelectedPanes(self) -> List[Agilent.MassSpectrometry.GUI.Plot.Pane]: ...
    def CreateFillPeakBrush(
        self,
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        series: int,
        peakIndex: int,
        color: System.Drawing.Color,
    ) -> System.Drawing.Brush: ...
    def EnsureColumnVisible(self, column: int) -> None: ...
    def ShowContextMenu(self) -> None: ...
    def GetSelectedPane(self) -> Agilent.MassSpectrometry.GUI.Plot.Pane: ...
    def AutoScaleAxis(self, axis: Agilent.MassSpectrometry.GUI.Plot.Axis) -> None: ...
    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetPreferredXRangeLimit(
        self, row: int, column: int
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetAutoScaleRangeY2(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetLabelFormat(self, vertical: bool) -> System.Drawing.StringFormat: ...
    def GetSelectedPanesCount(self) -> int: ...
    @overload
    @staticmethod
    def Intersect(
        r1: System.Drawing.Rectangle, r2: System.Drawing.Rectangle
    ) -> bool: ...
    @overload
    @staticmethod
    def Intersect(
        r: System.Drawing.Rectangle, left: int, top: int, width: int, height: int
    ) -> bool: ...

    BeforeDrawPane: System.EventHandler[DrawPaneEventArgs]  # Event
    DisplayContextMenu: System.EventHandler  # Event
    DrawPane: System.EventHandler[DrawPaneEventArgs]  # Event
    FirstVisibleColumnChanged: System.EventHandler  # Event
    FirstVisibleRowChanged: System.EventHandler  # Event
    PaneDimensionChanged: System.EventHandler  # Event
    PaneSelectionChanged: System.EventHandler  # Event
    ZoomHistoryChanged: System.EventHandler[ZoomHistoryEventArgs]  # Event

class PlotEventManipulatorBase(
    Agilent.MassSpectrometry.EventManipulating.EventManipulator,
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
):  # Class
    def __init__(
        self, context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext
    ) -> None: ...

    HorizontalShiftCursor: System.Windows.Forms.Cursor  # static # readonly
    HorizontalStretchCursor: System.Windows.Forms.Cursor  # static # readonly
    VerticalShiftCursor: System.Windows.Forms.Cursor  # static # readonly
    VerticalStretchCursor: System.Windows.Forms.Cursor  # static # readonly

    def OnMouseDown(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnDragStart(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        startPoint: System.Drawing.Point,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...
    def OnMouseMove(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseWheel(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnDoubleClick(self, sender: Any, e: System.EventArgs) -> None: ...
    def OnDragEnd(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...

class PlotModes(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Bar: Agilent.MassSpectrometry.GUI.Plot.PlotModes = ...  # static # readonly
    Connected: Agilent.MassSpectrometry.GUI.Plot.PlotModes = ...  # static # readonly
    Line: Agilent.MassSpectrometry.GUI.Plot.PlotModes = ...  # static # readonly
    Point: Agilent.MassSpectrometry.GUI.Plot.PlotModes = ...  # static # readonly

class PlotPane:  # Class
    def __init__(
        self,
        pane: Agilent.MassSpectrometry.GUI.Plot.Pane,
        g: Agilent.MassSpectrometry.GUI.Plot.IGraphics,
        bounds: System.Drawing.Rectangle,
    ) -> None: ...

    AreaHeight: float  # readonly
    AreaLeft: float  # readonly
    AreaTop: float  # readonly
    AreaWidth: float  # readonly
    CurrentSeriesIsSecondaryY: bool  # readonly
    Graphics: System.Drawing.Graphics  # readonly
    IGraphics: Agilent.MassSpectrometry.GUI.Plot.IGraphics  # readonly
    MaxX: float  # readonly
    MaxY: float  # readonly
    MinX: float  # readonly
    MinY: float  # readonly
    Pane: Agilent.MassSpectrometry.GUI.Plot.Pane  # readonly

    def DataToWindowY(self, y: float) -> int: ...
    def DataToWindowX(self, x: float) -> int: ...
    def DataToWindowY2D(self, y: float) -> float: ...
    def DataToWindowYD(self, y: float) -> float: ...
    def DataToWindowXD(self, x: float) -> float: ...
    def DataToWindowY2(self, y: float) -> int: ...

class PlotRange:  # Struct
    def __init__(self, minValue: float, maxValue: float) -> None: ...

    Default: Agilent.MassSpectrometry.GUI.Plot.PlotRange  # static # readonly
    Empty: Agilent.MassSpectrometry.GUI.Plot.PlotRange  # static # readonly
    IsEmpty: bool  # readonly
    Max: float
    Min: float

    def GetHashCode(self) -> int: ...
    @staticmethod
    def FindIndex(
        data: Agilent.MassSpectrometry.GUI.Plot.IPlotData,
        series: int,
        start: int,
        end: int,
        x: float,
    ) -> int: ...
    @overload
    def Equals(self, range: Agilent.MassSpectrometry.GUI.Plot.PlotRange) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class RectangleMarker(Agilent.MassSpectrometry.GUI.Plot.FillableMarker):  # Class
    def __init__(self) -> None: ...
    def Draw(self, plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane) -> None: ...

class ShiftEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    Agilent.MassSpectrometry.GUI.Plot.PlotEventManipulatorBase,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext,
        axis: Agilent.MassSpectrometry.GUI.Plot.Axis,
        startPoint: System.Drawing.Point,
    ) -> None: ...
    def OnDragStart(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        startPoint: System.Drawing.Point,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...
    def OnEnd(self) -> None: ...
    def OnMouseMove(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnStart(self) -> None: ...

class StretchEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    Agilent.MassSpectrometry.GUI.Plot.PlotEventManipulatorBase,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext,
        axis: Agilent.MassSpectrometry.GUI.Plot.Axis,
        startPoint: System.Drawing.Point,
    ) -> None: ...
    def OnDragStart(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        startPoint: System.Drawing.Point,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...
    def OnEnd(self) -> None: ...
    def OnMouseMove(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnStart(self) -> None: ...

class TextOrientation(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Horizontal: Agilent.MassSpectrometry.GUI.Plot.TextOrientation = (
        ...
    )  # static # readonly
    VerticalBottomUp: Agilent.MassSpectrometry.GUI.Plot.TextOrientation = (
        ...
    )  # static # readonly
    VerticalTopDown: Agilent.MassSpectrometry.GUI.Plot.TextOrientation = (
        ...
    )  # static # readonly

class TitleBase:  # Class
    Alignment: System.Drawing.StringAlignment
    BackColor: System.Drawing.Color
    Bounds: System.Drawing.Rectangle  # readonly
    Color: System.Drawing.Color
    Extent: int
    Font: System.Drawing.Font
    LineAlignment: System.Drawing.StringAlignment
    Orientation: Agilent.MassSpectrometry.GUI.Plot.TextOrientation
    Text: str
    Trimming: System.Drawing.StringTrimming
    Visible: bool

    def SetTabStops(self, firstTabOffset: float, tabStops: List[float]) -> None: ...
    def GetTabStops(self, firstTabOffset: float) -> List[float]: ...

class TriangleMarker(Agilent.MassSpectrometry.GUI.Plot.FillableMarker):  # Class
    def __init__(self) -> None: ...
    def Draw(self, plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane) -> None: ...

class VerticalLineMarker(Agilent.MassSpectrometry.GUI.Plot.Marker):  # Class
    def __init__(self) -> None: ...

    StartY: float

    def Draw(self, plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane) -> None: ...

class WheelStretchEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    Agilent.MassSpectrometry.GUI.Plot.PlotEventManipulatorBase,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        axis: Agilent.MassSpectrometry.GUI.Plot.Axis,
    ) -> None: ...
    def OnMouseWheel(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnKeyDown(self, sender: Any, e: System.Windows.Forms.KeyEventArgs) -> None: ...
    def OnKeyUp(self, sender: Any, e: System.Windows.Forms.KeyEventArgs) -> None: ...

class XRangeFillBoxRubberBand(
    Agilent.MassSpectrometry.EventManipulating.Model.IRubberBand,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.BoxRubberBand,
):  # Class
    def __init__(
        self, startPoint: System.Drawing.Point, region: System.Drawing.Rectangle
    ) -> None: ...

class XRangeFillColorBoxRubberBand(
    Agilent.MassSpectrometry.EventManipulating.Model.IRubberBand,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.BoxRubberBand,
):  # Class
    def __init__(
        self,
        startPoint: System.Drawing.Point,
        region: System.Drawing.Rectangle,
        lineColor: System.Drawing.Color,
        fillColor: System.Drawing.Color,
    ) -> None: ...
    def Erase(self) -> None: ...

class XRangeMarker(Agilent.MassSpectrometry.GUI.Plot.FillableMarker):  # Class
    def __init__(self) -> None: ...

    Width: float

    def Draw(self, plotPane: Agilent.MassSpectrometry.GUI.Plot.PlotPane) -> None: ...

class XRangeSelectEventManipulatorBase(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    Agilent.MassSpectrometry.GUI.Plot.PlotEventManipulatorBase,
    System.IDisposable,
):  # Class
    def __init__(
        self, context: Agilent.MassSpectrometry.EventManipulating.Model.IEventContext
    ) -> None: ...
    def OnDragEnd(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...
    def OnDragStart(
        self,
        control: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        startPoint: System.Drawing.Point,
        e: System.Windows.Forms.MouseEventArgs,
    ) -> None: ...

class ZoomHistory:  # Class
    CanRezoom: bool  # readonly
    CanUnzoom: bool  # readonly
    Capacity: int

    def Push(self, oldZoomInfo: Agilent.MassSpectrometry.GUI.Plot.ZoomInfo) -> None: ...
    def Clear(self) -> None: ...
    def Rezoom(self) -> None: ...
    def Unzoom(self) -> None: ...

class ZoomInfo(System.IDisposable):  # Class
    def __init__(
        self, control: Agilent.MassSpectrometry.GUI.Plot.PlotControl
    ) -> None: ...
    def __getitem__(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> Agilent.MassSpectrometry.GUI.Plot.PaneRange: ...
    Panes: Iterable[Agilent.MassSpectrometry.GUI.Plot.Pane]  # readonly

    def Contains(self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane) -> bool: ...
    def Dispose(self) -> None: ...
    def Unzoom(
        self, control: Agilent.MassSpectrometry.GUI.Plot.PlotControl
    ) -> None: ...
