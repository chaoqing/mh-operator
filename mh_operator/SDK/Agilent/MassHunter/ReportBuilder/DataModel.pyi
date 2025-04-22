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

from .Template import (
    BreakLocation,
    DataFilterOperator,
    HorizontalAlign,
    LengthUnit,
    LineStyle,
    PageOrientation,
    TextboxContentType,
    VerticalAlign,
)

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.DataModel

class IBorders(Agilent.MassHunter.ReportBuilder.DataModel.IReportObject):  # Interface
    Bottom: Agilent.MassHunter.ReportBuilder.DataModel.ILine  # readonly
    Left: Agilent.MassHunter.ReportBuilder.DataModel.ILine  # readonly
    Right: Agilent.MassHunter.ReportBuilder.DataModel.ILine  # readonly
    Top: Agilent.MassHunter.ReportBuilder.DataModel.ILine  # readonly

class IDataBinding(
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject
):  # Interface
    BindingName: str  # readonly
    ChildDataBinding: (
        Agilent.MassHunter.ReportBuilder.DataModel.IDataBinding
    )  # readonly
    DataName: str  # readonly
    Expression: str  # readonly
    Filters: List[Agilent.MassHunter.ReportBuilder.DataModel.IDataFilter]  # readonly
    Orders: List[Agilent.MassHunter.ReportBuilder.DataModel.IDataOrder]  # readonly

class IDataBindingContainer(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
):  # Interface
    DataBinding: Agilent.MassHunter.ReportBuilder.DataModel.IDataBinding  # readonly

class IDataFilter(
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject
):  # Interface
    FieldName: str  # readonly
    FieldValue: Agilent.MassHunter.ReportBuilder.DataModel.IFieldValue  # readonly
    Operator: DataFilterOperator  # readonly
    Value: str  # readonly

class IDataOrder(Agilent.MassHunter.ReportBuilder.DataModel.IReportObject):  # Interface
    Ascending: bool  # readonly
    FieldName: str  # readonly

class IFieldValue(
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject
):  # Interface
    BindingName: str  # readonly
    FieldName: str  # readonly
    Parent: Agilent.MassHunter.ReportBuilder.DataModel.ISelectable  # readonly

class IFont(Agilent.MassHunter.ReportBuilder.DataModel.IReportObject):  # Interface
    Bold: Optional[bool]  # readonly
    Italic: Optional[bool]  # readonly
    Name: str  # readonly
    Size: Optional[float]  # readonly
    Strikeout: Optional[bool]  # readonly
    Underline: Optional[bool]  # readonly

class IGraphics(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
):  # Interface
    Height: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly
    Name: str  # readonly
    Parameters: List[
        Agilent.MassHunter.ReportBuilder.DataModel.IGraphicsParameter
    ]  # readonly
    Width: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly
    WidthPercentage: float  # readonly

class IGraphicsParameter(
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject
):  # Interface
    FieldValue: Agilent.MassHunter.ReportBuilder.DataModel.IFieldValue  # readonly
    Name: str  # readonly
    Value: str  # readonly

class IHeaderFooter(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer,
):  # Interface
    BackgroundColor: System.Drawing.Color
    Borders: Agilent.MassHunter.ReportBuilder.DataModel.IBorders  # readonly
    Center: Agilent.MassHunter.ReportBuilder.DataModel.IHeaderFooterContent  # readonly
    Height: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly
    Left: Agilent.MassHunter.ReportBuilder.DataModel.IHeaderFooterContent  # readonly
    Page: Agilent.MassHunter.ReportBuilder.DataModel.IPage  # readonly
    Right: Agilent.MassHunter.ReportBuilder.DataModel.IHeaderFooterContent  # readonly

class IHeaderFooterContent(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
):  # Interface
    ...

class IImage(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
):  # Interface
    File: str  # readonly
    Height: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly

class ILength(object):  # Interface
    Unit: LengthUnit  # readonly
    Value: float  # readonly

    def ValueAs(self, unit: LengthUnit) -> float: ...
    def ToString(self, culture: System.Globalization.CultureInfo) -> str: ...

class ILine(Agilent.MassHunter.ReportBuilder.DataModel.IReportObject):  # Interface
    Color: System.Drawing.Color  # readonly
    LineStyle: LineStyle  # readonly
    Width: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly

class IList(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
    Agilent.MassHunter.ReportBuilder.DataModel.IDataBindingContainer,
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
):  # Interface
    Hidden: bool  # readonly
    PageBreak: BreakLocation  # readonly

class ILocalizableFieldValue(
    Agilent.MassHunter.ReportBuilder.DataModel.IFieldValue,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
):  # Interface
    Localize: bool  # readonly

class ILocalizedText(
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject
):  # Interface
    Key: str  # readonly

class IMargins(Agilent.MassHunter.ReportBuilder.DataModel.IReportObject):  # Interface
    Bottom: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly
    Left: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly
    Right: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly
    Top: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly

class IPaddings(Agilent.MassHunter.ReportBuilder.DataModel.IReportObject):  # Interface
    Bottom: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly
    Left: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly
    Right: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly
    Top: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly

class IPage(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer,
):  # Interface
    Footer: Agilent.MassHunter.ReportBuilder.DataModel.IHeaderFooter  # readonly
    Header: Agilent.MassHunter.ReportBuilder.DataModel.IHeaderFooter  # readonly
    Margins: Agilent.MassHunter.ReportBuilder.DataModel.IMargins  # readonly
    PageOrientation: PageOrientation  # readonly

class IReport(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer,
):  # Interface
    Copyright: str  # readonly
    DesignerType: str  # readonly
    EditorVersion: str  # readonly
    IsDirty: bool  # readonly
    Pages: List[Agilent.MassHunter.ReportBuilder.DataModel.IPage]  # readonly
    SchemaVersion: int  # readonly
    TemplateFilePath: str  # readonly
    TextSets: Agilent.MassHunter.ReportBuilder.DataModel.ITextSets  # readonly

    def FindNewID(self, basename: str) -> str: ...

class IReportObject(object):  # Interface
    Report: Agilent.MassHunter.ReportBuilder.DataModel.IReport  # readonly

class IScriptBox(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
):  # Interface
    Script: str

class ISelectable(
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject
):  # Interface
    Container: (
        Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer
    )  # readonly
    DisplayTypeName: str  # readonly
    ID: str  # readonly

class ISelectableContainer(
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject
):  # Interface
    Count: int  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassHunter.ReportBuilder.DataModel.ISelectable: ...
    def CanInsertScriptBox(self) -> bool: ...
    def CanInsertImage(self) -> bool: ...
    def IndexOf(
        self, selectable: Agilent.MassHunter.ReportBuilder.DataModel.ISelectable
    ) -> int: ...
    def CanInsertGraphics(self) -> bool: ...
    def CanInsertTable(self) -> bool: ...
    def CanInsertList(self) -> bool: ...
    def CanInsertTextbox(self) -> bool: ...
    def FindByID(
        self, id: str
    ) -> Agilent.MassHunter.ReportBuilder.DataModel.ISelectable: ...

class ITable(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
    Agilent.MassHunter.ReportBuilder.DataModel.IDataBindingContainer,
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
):  # Interface
    ColumnCount: int  # readonly
    Columns: str  # readonly
    DefaultCellBorders: Agilent.MassHunter.ReportBuilder.DataModel.IBorders  # readonly
    Flow: bool  # readonly
    HeaderRows: int  # readonly
    Hidden: bool  # readonly
    HorizontalAlign: HorizontalAlign  # readonly
    KeepTogether: bool  # readonly
    PageBreak: BreakLocation  # readonly
    RelativeColumnWidths: str  # readonly
    SpacingBefore: Agilent.MassHunter.ReportBuilder.DataModel.ILength  # readonly
    WidthPercentage: float  # readonly

class ITableCell(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer,
):  # Interface
    Borders: Agilent.MassHunter.ReportBuilder.DataModel.IBorders  # readonly
    ColumnSpan: int  # readonly
    Content: Agilent.MassHunter.ReportBuilder.DataModel.ISelectable  # readonly
    Row: Agilent.MassHunter.ReportBuilder.DataModel.ITableRow  # readonly

class ITableCellContent(object):  # Interface
    Borders: Agilent.MassHunter.ReportBuilder.DataModel.IBorders  # readonly
    ColumnSpan: int  # readonly

class ITableRow(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
):  # Interface
    Table: Agilent.MassHunter.ReportBuilder.DataModel.ITable  # readonly

class ITextSets(object):  # Interface
    def GetValue(self, name: str, culture: str, value_: str) -> bool: ...
    def SetValue(self, name: str, culture: str, value_: str) -> None: ...
    def Remove(self, name: str, culture: str) -> None: ...
    def Exists(self, name: str, culture: str) -> bool: ...
    def GetNames(self) -> List[str]: ...

class ITextbox(
    Agilent.MassHunter.ReportBuilder.DataModel.ISelectable,
    Agilent.MassHunter.ReportBuilder.DataModel.IReportObject,
):  # Interface
    BackgroundColor: System.Drawing.Color  # readonly
    Color: System.Drawing.Color  # readonly
    ContentType: TextboxContentType  # readonly
    Expression: str  # readonly
    FieldCaption: Agilent.MassHunter.ReportBuilder.DataModel.IFieldValue  # readonly
    FieldFormat: Agilent.MassHunter.ReportBuilder.DataModel.IFieldValue  # readonly
    FieldValue: (
        Agilent.MassHunter.ReportBuilder.DataModel.ILocalizableFieldValue
    )  # readonly
    Font: Agilent.MassHunter.ReportBuilder.DataModel.IFont  # readonly
    Format: str  # readonly
    HorizontalAlign: HorizontalAlign  # readonly
    LocalizedText: Agilent.MassHunter.ReportBuilder.DataModel.ILocalizedText  # readonly
    OutlineLevel: Optional[int]  # readonly
    Paddings: Agilent.MassHunter.ReportBuilder.DataModel.IPaddings  # readonly
    Text: str  # readonly
    VerticalAlign: VerticalAlign  # readonly
