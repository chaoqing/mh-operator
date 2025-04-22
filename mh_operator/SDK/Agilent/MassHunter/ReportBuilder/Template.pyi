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

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.Template

class Body(
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IBody,
):  # Class
    def __init__(self) -> None: ...

    Items: List[Agilent.MassHunter.ReportBuilder.Template.IReportItem]  # readonly
    _Items: List[Agilent.MassHunter.ReportBuilder.Template.ReportItem]

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        ...

class Borders(Agilent.MassHunter.ReportBuilder.Template.IBorders):  # Class
    def __init__(self) -> None: ...

    Bottom: Agilent.MassHunter.ReportBuilder.Template.ILine  # readonly
    Left: Agilent.MassHunter.ReportBuilder.Template.ILine  # readonly
    Right: Agilent.MassHunter.ReportBuilder.Template.ILine  # readonly
    Top: Agilent.MassHunter.ReportBuilder.Template.ILine  # readonly
    _Bottom: Agilent.MassHunter.ReportBuilder.Template.Line
    _Left: Agilent.MassHunter.ReportBuilder.Template.Line
    _Right: Agilent.MassHunter.ReportBuilder.Template.Line
    _Top: Agilent.MassHunter.ReportBuilder.Template.Line

class BreakLocation(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Between: Agilent.MassHunter.ReportBuilder.Template.BreakLocation = (
        ...
    )  # static # readonly
    BetweenEvery2nd: Agilent.MassHunter.ReportBuilder.Template.BreakLocation = (
        ...
    )  # static # readonly
    BetweenEvery3rd: Agilent.MassHunter.ReportBuilder.Template.BreakLocation = (
        ...
    )  # static # readonly
    End: Agilent.MassHunter.ReportBuilder.Template.BreakLocation = (
        ...
    )  # static # readonly
    Start: Agilent.MassHunter.ReportBuilder.Template.BreakLocation = (
        ...
    )  # static # readonly
    StartAndBetween: Agilent.MassHunter.ReportBuilder.Template.BreakLocation = (
        ...
    )  # static # readonly
    StartAndEnd: Agilent.MassHunter.ReportBuilder.Template.BreakLocation = (
        ...
    )  # static # readonly

class Color(Agilent.MassHunter.ReportBuilder.Template.IColor):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, color: Agilent.MassHunter.ReportBuilder.Template.IColor
    ) -> None: ...
    @overload
    def __init__(self, color: System.Drawing.Color) -> None: ...
    @overload
    def __init__(self, a: int, r: int, g: int, b: int) -> None: ...
    @overload
    def __init__(self, value_: str) -> None: ...

    A: int  # readonly
    B: int  # readonly
    Default: Agilent.MassHunter.ReportBuilder.Template.Color  # static # readonly
    G: int  # readonly
    R: int  # readonly
    Value: str

    def ToString(self) -> str: ...

class DataBinding(Agilent.MassHunter.ReportBuilder.Template.IDataBinding):  # Class
    def __init__(self) -> None: ...

    BindingName: str
    DataBindings: List[
        Agilent.MassHunter.ReportBuilder.Template.IDataBinding
    ]  # readonly
    DataName: str
    Expression: str
    Filters: List[Agilent.MassHunter.ReportBuilder.Template.IDataFilter]  # readonly
    GroupBy: str
    LeftOuterJoin: bool
    Orders: List[Agilent.MassHunter.ReportBuilder.Template.IDataOrder]  # readonly
    ProcessThisLayer: bool
    _DataBindings: List[Agilent.MassHunter.ReportBuilder.Template.DataBinding]
    _Filters: List[Agilent.MassHunter.ReportBuilder.Template.DataFilter]
    _Orders: List[Agilent.MassHunter.ReportBuilder.Template.DataOrder]

class DataFilter(Agilent.MassHunter.ReportBuilder.Template.IDataFilter):  # Class
    def __init__(self) -> None: ...

    ConcatenationType: (
        Agilent.MassHunter.ReportBuilder.Template.DataFilterConcatenationType
    )
    FieldName: str
    FieldValue: Agilent.MassHunter.ReportBuilder.Template.IFieldValue  # readonly
    Operator: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator
    Value: str
    _FieldValue: Agilent.MassHunter.ReportBuilder.Template.FieldValue

class DataFilterConcatenationType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    And: Agilent.MassHunter.ReportBuilder.Template.DataFilterConcatenationType = (
        ...
    )  # static # readonly
    Or: Agilent.MassHunter.ReportBuilder.Template.DataFilterConcatenationType = (
        ...
    )  # static # readonly

class DataFilterOperator(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    BelongToGroup: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    CloseParenthesis: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    Contains: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    Equals: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    Greater: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    GreaterEqual: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    IsNull: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    Less: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    LessEqual: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    NotEquals: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    NotNull: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    OpenParenthesis: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly
    Top: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator = (
        ...
    )  # static # readonly

class DataOrder(Agilent.MassHunter.ReportBuilder.Template.IDataOrder):  # Class
    def __init__(self) -> None: ...

    Ascending: bool
    FieldName: str

class DefaultFont(
    Agilent.MassHunter.ReportBuilder.Template.IFont,
    Agilent.MassHunter.ReportBuilder.Template.Font,
    Agilent.MassHunter.ReportBuilder.Template.IDefaultFont,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        culture: str,
        name: str,
        size: Optional[float],
        italic: Optional[bool],
        strikeout: Optional[bool],
        underline: Optional[bool],
        bold: Optional[bool],
    ) -> None: ...

    Culture: str

class FieldValue(Agilent.MassHunter.ReportBuilder.Template.IFieldValue):  # Class
    def __init__(self) -> None: ...

    BindingName: str
    FieldName: str

class Font(Agilent.MassHunter.ReportBuilder.Template.IFont):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        size: Optional[float],
        italic: Optional[bool],
        strikeout: Optional[bool],
        underline: Optional[bool],
        bold: Optional[bool],
    ) -> None: ...

    Bold: Optional[bool]
    Italic: Optional[bool]
    Name: str
    Size: Optional[float]
    Strikeout: Optional[bool]
    Underline: Optional[bool]

    # Nested Types

    class _Scriptable:  # Class
        Bold: Optional[bool]
        Italic: Optional[bool]
        Name: str
        Size: Optional[float]
        Strikeout: Optional[bool]
        Underline: Optional[bool]

class Footer(
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IHeaderFooter,
    Agilent.MassHunter.ReportBuilder.Template.IFooter,
    Agilent.MassHunter.ReportBuilder.Template.HeaderFooter,
):  # Class
    def __init__(self) -> None: ...

class Graphics(
    Agilent.MassHunter.ReportBuilder.Template.IGraphics,
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
):  # Class
    def __init__(self) -> None: ...

    Height: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Name: str
    Parameters: List[
        Agilent.MassHunter.ReportBuilder.Template.IGraphicsParameter
    ]  # readonly
    Width: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    WidthPercentage: float
    _Height: Agilent.MassHunter.ReportBuilder.Template.Length
    _Parameters: List[Agilent.MassHunter.ReportBuilder.Template.GraphicsParameter]
    _Width: Agilent.MassHunter.ReportBuilder.Template.Length

class GraphicsParameter(
    Agilent.MassHunter.ReportBuilder.Template.IGraphicsParameter
):  # Class
    def __init__(self) -> None: ...

    FieldValue: Agilent.MassHunter.ReportBuilder.Template.IFieldValue  # readonly
    Name: str
    Value: str
    _FieldValue: Agilent.MassHunter.ReportBuilder.Template.FieldValue

class Header(
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IHeaderFooter,
    Agilent.MassHunter.ReportBuilder.Template.HeaderFooter,
    Agilent.MassHunter.ReportBuilder.Template.IHeader,
):  # Class
    def __init__(self) -> None: ...

class HeaderFooter(
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IHeaderFooter,
):  # Class
    def __init__(self) -> None: ...

    BackgroundColor: Agilent.MassHunter.ReportBuilder.Template.IColor  # readonly
    Borders: Agilent.MassHunter.ReportBuilder.Template.IBorders  # readonly
    Center: List[Agilent.MassHunter.ReportBuilder.Template.IReportItem]  # readonly
    Height: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Left: List[Agilent.MassHunter.ReportBuilder.Template.IReportItem]  # readonly
    Right: List[Agilent.MassHunter.ReportBuilder.Template.IReportItem]  # readonly
    _BackgroundColor: Agilent.MassHunter.ReportBuilder.Template.Color
    _Borders: Agilent.MassHunter.ReportBuilder.Template.Borders
    _Center: List[Agilent.MassHunter.ReportBuilder.Template.ReportItem]
    _Height: Agilent.MassHunter.ReportBuilder.Template.Length
    _Left: List[Agilent.MassHunter.ReportBuilder.Template.ReportItem]
    _Right: List[Agilent.MassHunter.ReportBuilder.Template.ReportItem]

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        ...

class HorizontalAlign(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Center: Agilent.MassHunter.ReportBuilder.Template.HorizontalAlign = (
        ...
    )  # static # readonly
    Left: Agilent.MassHunter.ReportBuilder.Template.HorizontalAlign = (
        ...
    )  # static # readonly
    Right: Agilent.MassHunter.ReportBuilder.Template.HorizontalAlign = (
        ...
    )  # static # readonly

class IBody(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    Items: List[Agilent.MassHunter.ReportBuilder.Template.IReportItem]  # readonly

class IBorders(object):  # Interface
    Bottom: Agilent.MassHunter.ReportBuilder.Template.ILine  # readonly
    Left: Agilent.MassHunter.ReportBuilder.Template.ILine  # readonly
    Right: Agilent.MassHunter.ReportBuilder.Template.ILine  # readonly
    Top: Agilent.MassHunter.ReportBuilder.Template.ILine  # readonly

class IColor(object):  # Interface
    A: int  # readonly
    B: int  # readonly
    G: int  # readonly
    R: int  # readonly

class IDataBinding(object):  # Interface
    BindingName: str  # readonly
    DataBindings: List[
        Agilent.MassHunter.ReportBuilder.Template.IDataBinding
    ]  # readonly
    DataName: str  # readonly
    Expression: str  # readonly
    Filters: List[Agilent.MassHunter.ReportBuilder.Template.IDataFilter]  # readonly
    GroupBy: str  # readonly
    LeftOuterJoin: bool  # readonly
    Orders: List[Agilent.MassHunter.ReportBuilder.Template.IDataOrder]  # readonly
    ProcessThisLayer: bool  # readonly

class IDataFilter(object):  # Interface
    ConcatenationType: (
        Agilent.MassHunter.ReportBuilder.Template.DataFilterConcatenationType
    )  # readonly
    FieldName: str  # readonly
    FieldValue: Agilent.MassHunter.ReportBuilder.Template.IFieldValue  # readonly
    Operator: Agilent.MassHunter.ReportBuilder.Template.DataFilterOperator  # readonly
    Value: str  # readonly

class IDataOrder(object):  # Interface
    Ascending: bool  # readonly
    FieldName: str  # readonly

class IDefaultFont(Agilent.MassHunter.ReportBuilder.Template.IFont):  # Interface
    Culture: str  # readonly

class IFieldValue(object):  # Interface
    BindingName: str  # readonly
    FieldName: str  # readonly

class IFont(object):  # Interface
    Bold: Optional[bool]  # readonly
    Italic: Optional[bool]  # readonly
    Name: str  # readonly
    Size: Optional[float]  # readonly
    Strikeout: Optional[bool]  # readonly
    Underline: Optional[bool]  # readonly

class IFooter(
    Agilent.MassHunter.ReportBuilder.Template.IHeaderFooter,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
):  # Interface
    ...

class IGraphics(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    Height: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Name: str  # readonly
    Parameters: List[
        Agilent.MassHunter.ReportBuilder.Template.IGraphicsParameter
    ]  # readonly
    Width: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    WidthPercentage: float  # readonly

class IGraphicsParameter(object):  # Interface
    FieldValue: Agilent.MassHunter.ReportBuilder.Template.IFieldValue  # readonly
    Name: str  # readonly
    Value: str  # readonly

class IHeader(
    Agilent.MassHunter.ReportBuilder.Template.IHeaderFooter,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
):  # Interface
    ...

class IHeaderFooter(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    BackgroundColor: Agilent.MassHunter.ReportBuilder.Template.IColor  # readonly
    Borders: Agilent.MassHunter.ReportBuilder.Template.IBorders  # readonly
    Center: List[Agilent.MassHunter.ReportBuilder.Template.IReportItem]  # readonly
    Height: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Left: List[Agilent.MassHunter.ReportBuilder.Template.IReportItem]  # readonly
    Right: List[Agilent.MassHunter.ReportBuilder.Template.IReportItem]  # readonly

class IImage(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    File: str  # readonly
    Height: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    LockAspectRatio: bool  # readonly
    VerticalAlign: Agilent.MassHunter.ReportBuilder.Template.VerticalAlign  # readonly
    Width: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly

class ILength(object):  # Interface
    def ValueAs(
        self, unit: Agilent.MassHunter.ReportBuilder.Template.LengthUnit
    ) -> float: ...

class ILine(object):  # Interface
    Color: Agilent.MassHunter.ReportBuilder.Template.IColor  # readonly
    Style: Agilent.MassHunter.ReportBuilder.Template.LineStyle  # readonly
    Width: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly

class IList(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    DataBinding: Agilent.MassHunter.ReportBuilder.Template.IDataBinding  # readonly
    Hidden: bool  # readonly
    Items: List[Agilent.MassHunter.ReportBuilder.Template.IReportItem]  # readonly
    PageBreak: Agilent.MassHunter.ReportBuilder.Template.BreakLocation  # readonly

class ILocalizableFieldValue(
    Agilent.MassHunter.ReportBuilder.Template.IFieldValue
):  # Interface
    Localize: bool  # readonly

class IMargins(object):  # Interface
    Bottom: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Left: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Right: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Top: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly

class IPaddings(object):  # Interface
    Bottom: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Left: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Right: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Top: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly

class IPage(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    Body: Agilent.MassHunter.ReportBuilder.Template.IBody  # readonly
    Footer: Agilent.MassHunter.ReportBuilder.Template.IFooter  # readonly
    Header: Agilent.MassHunter.ReportBuilder.Template.IHeader  # readonly
    Margins: Agilent.MassHunter.ReportBuilder.Template.IMargins  # readonly
    Orientation: Agilent.MassHunter.ReportBuilder.Template.PageOrientation  # readonly

class IPrintGraphicsSettings(object):  # Interface
    FitToSheet: bool
    FitToSheetWidth: bool
    Height: Agilent.MassHunter.ReportBuilder.Template.ILength
    UseTemplateSettings: bool
    Width: Agilent.MassHunter.ReportBuilder.Template.ILength

class IReportItem(object):  # Interface
    ID: str  # readonly
    Scriptable: Agilent.MassHunter.ReportBuilder.Template.IScriptable  # readonly

class IReportTemplate(
    Agilent.MassHunter.ReportBuilder.Template.IReportItem
):  # Interface
    AppVersion: str  # readonly
    Copyright: str  # readonly
    DefaultFonts: List[
        Agilent.MassHunter.ReportBuilder.Template.IDefaultFont
    ]  # readonly
    DesignerType: str  # readonly
    EditorVersion: str  # readonly
    Pages: List[Agilent.MassHunter.ReportBuilder.Template.IPage]  # readonly
    SchemaVersion: int  # readonly
    TextSets: Agilent.MassHunter.ReportBuilder.Template.ITextSets  # readonly

class IScriptBox(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    Script: str

class IScriptable(object):  # Interface
    ...

class ITable(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    Columns: List[Agilent.MassHunter.ReportBuilder.Template.ITableColumn]  # readonly
    DataBinding: Agilent.MassHunter.ReportBuilder.Template.IDataBinding  # readonly
    DefaultCellBorders: Agilent.MassHunter.ReportBuilder.Template.IBorders  # readonly
    Flow: bool  # readonly
    HeaderRows: int  # readonly
    Hidden: bool  # readonly
    HorizontalAlign: (
        Agilent.MassHunter.ReportBuilder.Template.HorizontalAlign
    )  # readonly
    KeepTogether: bool  # readonly
    PageBreak: Agilent.MassHunter.ReportBuilder.Template.BreakLocation  # readonly
    Rows: List[Agilent.MassHunter.ReportBuilder.Template.ITableRow]  # readonly
    SpacingBefore: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    WidthPercentage: float  # readonly

class ITableCell(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    BackgroundColor: Agilent.MassHunter.ReportBuilder.Template.IColor  # readonly
    Borders: Agilent.MassHunter.ReportBuilder.Template.IBorders  # readonly
    ColumnSpan: int  # readonly
    Content: Agilent.MassHunter.ReportBuilder.Template.IReportItem  # readonly

class ITableColumn(object):  # Interface
    RelativeWidth: float  # readonly

class ITableRow(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    Cells: List[Agilent.MassHunter.ReportBuilder.Template.ITableCell]  # readonly

class ITextSet(object):  # Interface
    ID: str  # readonly
    TextValues: List[Agilent.MassHunter.ReportBuilder.Template.ITextValue]  # readonly

class ITextSets(object):  # Interface
    Texts: List[Agilent.MassHunter.ReportBuilder.Template.ITextSet]  # readonly

class ITextValue(object):  # Interface
    Culture: str  # readonly
    Value: str  # readonly

class ITextbox(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Interface
    BackgroundColor: Agilent.MassHunter.ReportBuilder.Template.IColor  # readonly
    Color: Agilent.MassHunter.ReportBuilder.Template.IColor  # readonly
    ContentType: Optional[
        Agilent.MassHunter.ReportBuilder.Template.TextboxContentType
    ]  # readonly
    Expression: str
    FieldCaption: Agilent.MassHunter.ReportBuilder.Template.IFieldValue  # readonly
    FieldFormat: Agilent.MassHunter.ReportBuilder.Template.IFieldValue  # readonly
    FieldValue: (
        Agilent.MassHunter.ReportBuilder.Template.ILocalizableFieldValue
    )  # readonly
    Font: Agilent.MassHunter.ReportBuilder.Template.IFont  # readonly
    Format: str
    HorizontalAlign: Agilent.MassHunter.ReportBuilder.Template.HorizontalAlign
    LocalizedText: str
    OutlineLevel: Optional[int]
    Paddings: Agilent.MassHunter.ReportBuilder.Template.IPaddings  # readonly
    Text: str
    VerticalAlign: Agilent.MassHunter.ReportBuilder.Template.VerticalAlign

class Image(
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IImage,
):  # Class
    def __init__(self) -> None: ...

    File: str
    Height: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    LockAspectRatio: bool
    VerticalAlign: Agilent.MassHunter.ReportBuilder.Template.VerticalAlign
    Width: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    _Height: Agilent.MassHunter.ReportBuilder.Template.Length
    _Width: Agilent.MassHunter.ReportBuilder.Template.Length

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        ...

class Length(Agilent.MassHunter.ReportBuilder.Template.ILength):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, value_: float, unit: Agilent.MassHunter.ReportBuilder.Template.LengthUnit
    ) -> None: ...
    @overload
    def __init__(
        self, length: Agilent.MassHunter.ReportBuilder.Template.Length
    ) -> None: ...

    Centimeter: float
    Inch: float
    Millimeter: float
    Point: float
    Presentation: float
    Unit: Agilent.MassHunter.ReportBuilder.Template.LengthUnit
    Value: float
    XmlValue: str

    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(self, len: Agilent.MassHunter.ReportBuilder.Template.Length) -> bool: ...
    def ValueAs(
        self, unit: Agilent.MassHunter.ReportBuilder.Template.LengthUnit
    ) -> float: ...
    def GetHashCode(self) -> int: ...
    def Parse(self, value_: str, ci: System.Globalization.CultureInfo) -> None: ...
    @overload
    def ToString(self) -> str: ...
    @overload
    def ToString(self, ci: System.Globalization.CultureInfo) -> str: ...

class LengthUnit(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Centimeter: Agilent.MassHunter.ReportBuilder.Template.LengthUnit = (
        ...
    )  # static # readonly
    Inch: Agilent.MassHunter.ReportBuilder.Template.LengthUnit = (
        ...
    )  # static # readonly
    Millimeter: Agilent.MassHunter.ReportBuilder.Template.LengthUnit = (
        ...
    )  # static # readonly
    Point: Agilent.MassHunter.ReportBuilder.Template.LengthUnit = (
        ...
    )  # static # readonly
    Presentation: Agilent.MassHunter.ReportBuilder.Template.LengthUnit = (
        ...
    )  # static # readonly

class Line(Agilent.MassHunter.ReportBuilder.Template.ILine):  # Class
    def __init__(self) -> None: ...

    Color: Agilent.MassHunter.ReportBuilder.Template.IColor  # readonly
    Style: Agilent.MassHunter.ReportBuilder.Template.LineStyle
    Width: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    _Color: Agilent.MassHunter.ReportBuilder.Template.Color
    _Width: Agilent.MassHunter.ReportBuilder.Template.Length

class LineStyle(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Dash: Agilent.MassHunter.ReportBuilder.Template.LineStyle = ...  # static # readonly
    Dot: Agilent.MassHunter.ReportBuilder.Template.LineStyle = ...  # static # readonly
    Solid: Agilent.MassHunter.ReportBuilder.Template.LineStyle = (
        ...
    )  # static # readonly

class List(
    Agilent.MassHunter.ReportBuilder.Template.IList,
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
):  # Class
    def __init__(self) -> None: ...

    DataBinding: Agilent.MassHunter.ReportBuilder.Template.IDataBinding  # readonly
    Hidden: bool
    Items: List[Agilent.MassHunter.ReportBuilder.Template.IReportItem]  # readonly
    PageBreak: Agilent.MassHunter.ReportBuilder.Template.BreakLocation
    _DataBinding: Agilent.MassHunter.ReportBuilder.Template.DataBinding
    _Items: List[Agilent.MassHunter.ReportBuilder.Template.ReportItem]

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        ...

class LocalizableFieldValue(
    Agilent.MassHunter.ReportBuilder.Template.IFieldValue,
    Agilent.MassHunter.ReportBuilder.Template.FieldValue,
    Agilent.MassHunter.ReportBuilder.Template.ILocalizableFieldValue,
):  # Class
    def __init__(self) -> None: ...

    Localize: bool

class Margins(Agilent.MassHunter.ReportBuilder.Template.IMargins):  # Class
    def __init__(self) -> None: ...

    Bottom: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Left: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Right: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Top: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    _Bottom: Agilent.MassHunter.ReportBuilder.Template.Length
    _Left: Agilent.MassHunter.ReportBuilder.Template.Length
    _Right: Agilent.MassHunter.ReportBuilder.Template.Length
    _Top: Agilent.MassHunter.ReportBuilder.Template.Length

class Paddings(Agilent.MassHunter.ReportBuilder.Template.IPaddings):  # Class
    def __init__(self) -> None: ...

    Bottom: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Left: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Right: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    Top: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    _Bottom: Agilent.MassHunter.ReportBuilder.Template.Length
    _Left: Agilent.MassHunter.ReportBuilder.Template.Length
    _Right: Agilent.MassHunter.ReportBuilder.Template.Length
    _Top: Agilent.MassHunter.ReportBuilder.Template.Length

class Page(
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IPage,
):  # Class
    def __init__(self) -> None: ...

    Body: Agilent.MassHunter.ReportBuilder.Template.IBody  # readonly
    Footer: Agilent.MassHunter.ReportBuilder.Template.IFooter  # readonly
    Header: Agilent.MassHunter.ReportBuilder.Template.IHeader  # readonly
    Margins: Agilent.MassHunter.ReportBuilder.Template.IMargins  # readonly
    Orientation: Agilent.MassHunter.ReportBuilder.Template.PageOrientation
    _Body: Agilent.MassHunter.ReportBuilder.Template.Body
    _Footer: Agilent.MassHunter.ReportBuilder.Template.Footer
    _Header: Agilent.MassHunter.ReportBuilder.Template.Header
    _Margins: Agilent.MassHunter.ReportBuilder.Template.Margins

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        ...

class PageOrientation(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Landscape: Agilent.MassHunter.ReportBuilder.Template.PageOrientation = (
        ...
    )  # static # readonly
    Portrait: Agilent.MassHunter.ReportBuilder.Template.PageOrientation = (
        ...
    )  # static # readonly

class PageSize(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    A4: Agilent.MassHunter.ReportBuilder.Template.PageSize = ...  # static # readonly
    Letter: Agilent.MassHunter.ReportBuilder.Template.PageSize = (
        ...
    )  # static # readonly

class PrintGraphicsSettings(
    Agilent.MassHunter.ReportBuilder.Template.IPrintGraphicsSettings
):  # Class
    def __init__(self) -> None: ...

    FitToSheet: bool
    FitToSheetWidth: bool
    Height: Agilent.MassHunter.ReportBuilder.Template.ILength
    UseTemplateSettings: bool
    Width: Agilent.MassHunter.ReportBuilder.Template.ILength

class ReportItem(Agilent.MassHunter.ReportBuilder.Template.IReportItem):  # Class
    ID: str
    Scriptable: Agilent.MassHunter.ReportBuilder.Template.IScriptable  # readonly

class ReportTemplate(
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportTemplate,
):  # Class
    def __init__(self) -> None: ...

    CurrentSchemaVersion: int = ...  # static # readonly

    AppVersion: str
    Copyright: str
    DefaultFonts: List[
        Agilent.MassHunter.ReportBuilder.Template.IDefaultFont
    ]  # readonly
    DesignerType: str
    EditorVersion: str
    Pages: List[Agilent.MassHunter.ReportBuilder.Template.IPage]  # readonly
    SchemaVersion: int
    TextSets: Agilent.MassHunter.ReportBuilder.Template.ITextSets  # readonly
    _DefaultFonts: List[Agilent.MassHunter.ReportBuilder.Template.DefaultFont]
    _Pages: List[Agilent.MassHunter.ReportBuilder.Template.Page]
    _TextSets: Agilent.MassHunter.ReportBuilder.Template.TextSets

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        ...

class ScriptBox(
    Agilent.MassHunter.ReportBuilder.Template.IScriptBox,
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
):  # Class
    def __init__(self) -> None: ...

    Script: str

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        ...

class Table(
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
    Agilent.MassHunter.ReportBuilder.Template.ITable,
):  # Class
    def __init__(self) -> None: ...

    Columns: List[Agilent.MassHunter.ReportBuilder.Template.ITableColumn]  # readonly
    DataBinding: Agilent.MassHunter.ReportBuilder.Template.IDataBinding  # readonly
    DefaultCellBorders: Agilent.MassHunter.ReportBuilder.Template.IBorders  # readonly
    Flow: bool
    HeaderRows: int
    Hidden: bool
    HorizontalAlign: Agilent.MassHunter.ReportBuilder.Template.HorizontalAlign
    KeepTogether: bool
    PageBreak: Agilent.MassHunter.ReportBuilder.Template.BreakLocation
    Rows: List[Agilent.MassHunter.ReportBuilder.Template.ITableRow]  # readonly
    SpacingBefore: Agilent.MassHunter.ReportBuilder.Template.ILength  # readonly
    WidthPercentage: float
    _Columns: List[Agilent.MassHunter.ReportBuilder.Template.TableColumn]
    _DataBinding: Agilent.MassHunter.ReportBuilder.Template.DataBinding
    _DefaultCellBorders: Agilent.MassHunter.ReportBuilder.Template.Borders
    _Rows: List[Agilent.MassHunter.ReportBuilder.Template.TableRow]
    _SpacingBefore: Agilent.MassHunter.ReportBuilder.Template.Length

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        ...

class TableCell(
    Agilent.MassHunter.ReportBuilder.Template.ITableCell,
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
):  # Class
    def __init__(self) -> None: ...

    BackgroundColor: Agilent.MassHunter.ReportBuilder.Template.IColor  # readonly
    Borders: Agilent.MassHunter.ReportBuilder.Template.IBorders  # readonly
    ColumnSpan: int
    Content: Agilent.MassHunter.ReportBuilder.Template.IReportItem  # readonly
    _BackgroundColor: Agilent.MassHunter.ReportBuilder.Template.Color
    _Borders: Agilent.MassHunter.ReportBuilder.Template.Borders
    _Content: Agilent.MassHunter.ReportBuilder.Template.ReportItem

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        BackgroundColor: Optional[System.Drawing.Color]

class TableColumn(Agilent.MassHunter.ReportBuilder.Template.ITableColumn):  # Class
    def __init__(self) -> None: ...

    RelativeWidth: float

class TableRow(
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
    Agilent.MassHunter.ReportBuilder.Template.ITableRow,
):  # Class
    def __init__(self) -> None: ...

    Cells: List[Agilent.MassHunter.ReportBuilder.Template.ITableCell]  # readonly
    _Cells: List[Agilent.MassHunter.ReportBuilder.Template.TableCell]

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        ...

class TextSet(Agilent.MassHunter.ReportBuilder.Template.ITextSet):  # Class
    def __init__(self) -> None: ...

    ID: str
    TextValues: List[Agilent.MassHunter.ReportBuilder.Template.ITextValue]  # readonly
    _TextValues: List[Agilent.MassHunter.ReportBuilder.Template.TextValue]

class TextSets(Agilent.MassHunter.ReportBuilder.Template.ITextSets):  # Class
    def __init__(self) -> None: ...

    Texts: List[Agilent.MassHunter.ReportBuilder.Template.ITextSet]  # readonly
    _Texts: List[Agilent.MassHunter.ReportBuilder.Template.TextSet]

class TextValue(Agilent.MassHunter.ReportBuilder.Template.ITextValue):  # Class
    def __init__(self) -> None: ...

    Culture: str
    Value: str

class Textbox(
    Agilent.MassHunter.ReportBuilder.Template.ITextbox,
    Agilent.MassHunter.ReportBuilder.Template.ReportItem,
    Agilent.MassHunter.ReportBuilder.Template.IReportItem,
):  # Class
    def __init__(self) -> None: ...

    BackgroundColor: Agilent.MassHunter.ReportBuilder.Template.IColor  # readonly
    Color: Agilent.MassHunter.ReportBuilder.Template.IColor  # readonly
    ContentType: Optional[Agilent.MassHunter.ReportBuilder.Template.TextboxContentType]
    Expression: str
    FieldCaption: Agilent.MassHunter.ReportBuilder.Template.IFieldValue  # readonly
    FieldFormat: Agilent.MassHunter.ReportBuilder.Template.IFieldValue  # readonly
    FieldValue: (
        Agilent.MassHunter.ReportBuilder.Template.ILocalizableFieldValue
    )  # readonly
    Font: Agilent.MassHunter.ReportBuilder.Template.IFont  # readonly
    Format: str
    HorizontalAlign: Agilent.MassHunter.ReportBuilder.Template.HorizontalAlign
    LocalizedText: str
    OutlineLevel: Optional[int]
    Paddings: Agilent.MassHunter.ReportBuilder.Template.IPaddings  # readonly
    Text: str
    VerticalAlign: Agilent.MassHunter.ReportBuilder.Template.VerticalAlign
    _BackgroundColor: Agilent.MassHunter.ReportBuilder.Template.Color
    _Color: Agilent.MassHunter.ReportBuilder.Template.Color
    _FieldCaption: Agilent.MassHunter.ReportBuilder.Template.FieldValue
    _FieldFormat: Agilent.MassHunter.ReportBuilder.Template.FieldValue
    _FieldValue: Agilent.MassHunter.ReportBuilder.Template.LocalizableFieldValue
    _Font: Agilent.MassHunter.ReportBuilder.Template.Font
    _Paddings: Agilent.MassHunter.ReportBuilder.Template.Paddings

    # Nested Types

    class _Scriptable(Agilent.MassHunter.ReportBuilder.Template.IScriptable):  # Class
        Color: Optional[System.Drawing.Color]
        Font: Agilent.MassHunter.ReportBuilder.Template.Font._Scriptable  # readonly

class TextboxContentType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Expression: Agilent.MassHunter.ReportBuilder.Template.TextboxContentType = (
        ...
    )  # static # readonly
    FieldCaption: Agilent.MassHunter.ReportBuilder.Template.TextboxContentType = (
        ...
    )  # static # readonly
    FieldValue: Agilent.MassHunter.ReportBuilder.Template.TextboxContentType = (
        ...
    )  # static # readonly
    LocalizedText: Agilent.MassHunter.ReportBuilder.Template.TextboxContentType = (
        ...
    )  # static # readonly
    Text: Agilent.MassHunter.ReportBuilder.Template.TextboxContentType = (
        ...
    )  # static # readonly

class VerticalAlign(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Bottom: Agilent.MassHunter.ReportBuilder.Template.VerticalAlign = (
        ...
    )  # static # readonly
    Center: Agilent.MassHunter.ReportBuilder.Template.VerticalAlign = (
        ...
    )  # static # readonly
    Top: Agilent.MassHunter.ReportBuilder.Template.VerticalAlign = (
        ...
    )  # static # readonly
