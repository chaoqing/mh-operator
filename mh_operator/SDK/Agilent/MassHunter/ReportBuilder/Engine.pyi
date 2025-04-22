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
from .DataSource import IDataSource
from .Template import (
    BreakLocation,
    IDataBinding,
    IGraphics,
    IImage,
    IPage,
    IPrintGraphicsSettings,
    IReportItem,
    IReportTemplate,
    IScriptable,
    ITable,
    ITableCell,
    ITextbox,
    PageSize,
)

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.Engine

class IGraphicsCanvas(object):  # Interface
    IgnoreFontName: bool

    def ConvertBounds(
        self, bounds: System.Drawing.RectangleF
    ) -> System.Drawing.RectangleF: ...
    def DrawImage(
        self,
        image: System.Drawing.Image,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def GetGraphics(self) -> T: ...

class IRenderingEvents(object):  # Interface
    def Render(
        self,
        evt: Agilent.MassHunter.ReportBuilder.Engine.RenderingEvent,
        context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext,
        item: IReportItem,
        renderingObject: Any,
    ) -> bool: ...

class IReportContext(object):  # Interface
    ComplianceDisplayName: str
    ComplianceName: str
    ComplianceServer: str
    CurrentBoundObject: Any  # readonly
    CurrentVersion: str  # readonly
    DataSource: IDataSource  # readonly
    PageSize: PageSize
    PreviewAborted: bool
    PreviewMaxNumPages: int
    PrintGraphicsSettings: IPrintGraphicsSettings  # readonly
    Renderer: Agilent.MassHunter.ReportBuilder.Engine.IReportRenderer  # readonly
    ScriptEngine: Agilent.MassHunter.ReportBuilder.Engine.IScriptEngine  # readonly
    StartDateTime: System.DateTime  # readonly
    Template: IReportTemplate  # readonly
    TemplateFilePath: str  # readonly
    UserName: str

    def PopBoundObject(self, dataBindingName: str) -> None: ...
    @overload
    def LocalizeText(self, key: str) -> str: ...
    @overload
    def LocalizeText(
        self, culture: System.Globalization.CultureInfo, key: str, value_: str
    ) -> bool: ...
    def HasCustomMacro(self, key: str) -> bool: ...
    def PopDataBinding(self, dataBinding: IDataBinding) -> None: ...
    def ProcessCustomMacros(self, value_: str) -> str: ...
    def PushBoundObject(self, dataBindingName: str, value_: Any) -> None: ...
    def FindDataBinding(self, name: str) -> IDataBinding: ...
    def PushDataBinding(self, dataBinding: IDataBinding) -> None: ...
    def CheckAbort(self) -> None: ...
    def GetCustomMacro(self, key: str) -> str: ...
    def GetBoundObject(self, dataBindingName: str) -> Any: ...
    def SetCustomMacro(self, key: str, value_: str) -> None: ...

class IReportRenderer(System.IDisposable):  # Interface
    Context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext

    def RenderImage(self, image: IImage) -> None: ...
    def StartDocument(self) -> None: ...
    def PageBreak(self) -> None: ...
    def RenderTable(
        self, numColumns: int
    ) -> Agilent.MassHunter.ReportBuilder.Engine.ITableRenderer: ...
    def RenderGraphics(self, graphics: IGraphics) -> None: ...
    def RenderText(self, textbox: ITextbox) -> None: ...
    def EndDocument(self) -> None: ...
    def SetPage(self, page: IPage) -> None: ...

class IReportScriptContext(object):  # Interface
    ComplianceDisplayName: str  # readonly
    ComplianceName: str  # readonly
    ComplianceServer: str  # readonly
    CurrentPage: int  # readonly
    CurrentVersion: str  # readonly
    DataSource: IDataSource  # readonly
    StartDateTime: System.DateTime  # readonly
    TemplateFilePath: str  # readonly
    TotalPages: int  # readonly
    UserName: str  # readonly

    def LocalizeText(self, text: str) -> str: ...

class IScriptEngine(object):  # Interface
    def RemoveVariable(self, name: str) -> None: ...
    def PushTemplateItem(self, id: str, item: IScriptable) -> None: ...
    def SetVariable(self, name: str, value_: Any) -> None: ...
    def PopTemplateItem(self, id: str, item: IScriptable) -> None: ...
    def Eval(self, expression: str) -> Any: ...

class ITableRenderer(object):  # Interface
    def SetColumnWidths(self, widths: List[float]) -> None: ...
    def EndTable(self) -> None: ...
    def SetProperties(self, table: ITable) -> None: ...
    def StartHeader(self) -> None: ...
    def EndHeader(self) -> None: ...
    def AddCell(self, cell: ITableCell) -> None: ...
    def EndRow(self) -> None: ...

class Macros:  # Class
    def __init__(self) -> None: ...

    CurrentVersion: str = ...  # static # readonly
    GeneratedDATE: str = ...  # static # readonly
    GeneratedDate: str = ...  # static # readonly
    GeneratedDateTime: str = ...  # static # readonly
    GeneratedTime: str = ...  # static # readonly
    Page: str = ...  # static # readonly
    Pages: str = ...  # static # readonly

class ProcessReport:  # Class
    def __init__(
        self,
        template: IReportTemplate,
        context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext,
    ) -> None: ...

    ReportContext: Agilent.MassHunter.ReportBuilder.Engine.IReportContext  # readonly
    ReportTemplate: IReportTemplate  # readonly

    def ProcessPage(self, page: IPage) -> None: ...
    @staticmethod
    def ProcessBinding(
        parentBinding: IDataBinding,
        dataBinding: IDataBinding,
        pageBreak: BreakLocation,
        context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext,
        renderer: Agilent.MassHunter.ReportBuilder.Engine.IReportRenderer,
        action: System.Action,
    ) -> None: ...
    def Process(self) -> None: ...

class ProcessTable:  # Class
    @staticmethod
    def Process(
        table: ITable,
        renderer: Agilent.MassHunter.ReportBuilder.Engine.IReportRenderer,
        tableRenderer: Agilent.MassHunter.ReportBuilder.Engine.ITableRenderer,
    ) -> None: ...

class RenderingEvent(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    TableCell: Agilent.MassHunter.ReportBuilder.Engine.RenderingEvent = (
        ...
    )  # static # readonly
    TextBox: Agilent.MassHunter.ReportBuilder.Engine.RenderingEvent = (
        ...
    )  # static # readonly

class ReportContext(Agilent.MassHunter.ReportBuilder.Engine.IReportContext):  # Class
    def __init__(
        self,
        templateFilePath: str,
        template: IReportTemplate,
        dataSource: IDataSource,
        renderer: Agilent.MassHunter.ReportBuilder.Engine.IReportRenderer,
        startDateTime: System.DateTime,
        abort: System.Threading.WaitHandle,
    ) -> None: ...

    ComplianceDisplayName: str
    ComplianceName: str
    ComplianceServer: str
    CurrentBoundObject: Any  # readonly
    CurrentVersion: str  # readonly
    DataSource: IDataSource  # readonly
    PageSize: PageSize
    PreviewAborted: bool
    PreviewMaxNumPages: int
    PrintGraphicsSettings: IPrintGraphicsSettings  # readonly
    Renderer: Agilent.MassHunter.ReportBuilder.Engine.IReportRenderer  # readonly
    ScriptEngine: Agilent.MassHunter.ReportBuilder.Engine.IScriptEngine  # readonly
    StartDateTime: System.DateTime  # readonly
    Template: IReportTemplate  # readonly
    TemplateFilePath: str  # readonly
    UserName: str

    def PopBoundObject(self, dataBindingName: str) -> None: ...
    @overload
    def LocalizeText(self, name: str) -> str: ...
    @overload
    def LocalizeText(
        self, culture: System.Globalization.CultureInfo, name: str, value_: str
    ) -> bool: ...
    @staticmethod
    def GetCurrentVersion() -> str: ...
    def HasCustomMacro(self, key: str) -> bool: ...
    def PopDataBinding(self, dataBinding: IDataBinding) -> None: ...
    def ProcessCustomMacros(self, value_: str) -> str: ...
    def PushBoundObject(self, dataBindingName: str, value_: Any) -> None: ...
    def FindDataBinding(self, name: str) -> IDataBinding: ...
    def PushDataBinding(self, dataBinding: IDataBinding) -> None: ...
    def CheckAbort(self) -> None: ...
    def GetCustomMacro(self, key: str) -> str: ...
    def GetBoundObject(self, dataBindingName: str) -> Any: ...
    def SetCustomMacro(self, key: str, value_: str) -> None: ...

class ReportScriptContext(
    Agilent.MassHunter.ReportBuilder.Engine.IReportScriptContext
):  # Class
    ComplianceDisplayName: str  # readonly
    ComplianceName: str  # readonly
    ComplianceServer: str  # readonly
    CurrentPage: int  # readonly
    CurrentVersion: str  # readonly
    DataSource: IDataSource  # readonly
    StartDateTime: System.DateTime  # readonly
    TemplateFilePath: str  # readonly
    TotalPages: int  # readonly
    UserName: str  # readonly

    def LocalizeText(self, text: str) -> str: ...

class ScriptEngine(Agilent.MassHunter.ReportBuilder.Engine.IScriptEngine):  # Class
    def __init__(self) -> None: ...
    def RemoveVariable(self, name: str) -> None: ...
    def PushTemplateItem(self, id: str, item: IScriptable) -> None: ...
    def SetVariable(self, name: str, value_: Any) -> None: ...
    def PopTemplateItem(self, id: str, item: IScriptable) -> None: ...
    def Eval(self, expression: str) -> Any: ...
