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
from .Engine import IReportContext
from .Template import (
    IDataBinding,
    IDataFilter,
    IDefaultFont,
    IFieldValue,
    IFont,
    IImage,
    ILength,
    IReportTemplate,
    ITextbox,
    TextboxContentType,
)

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.Extensions

class ConvertUnits:  # Class
    @overload
    @staticmethod
    def ConvertTo(length: ILength, graphics: System.Drawing.Graphics) -> float: ...
    @overload
    @staticmethod
    def ConvertTo(value_: float, graphics: System.Drawing.Graphics) -> ILength: ...

class FontUtils:  # Class
    def __init__(self) -> None: ...

    DefaultFontName: str = ...  # static # readonly

    @staticmethod
    def GetFont(font: IFont, defaultFont: IFont) -> IFont: ...
    @staticmethod
    def GetDefaultFont(
        fonts: List[IDefaultFont], ci: System.Globalization.CultureInfo
    ) -> IFont: ...

class ReportExtension:  # Class
    @staticmethod
    def GetValue(field: IFieldValue, context: IReportContext) -> Any: ...
    @staticmethod
    def ToSignificantDigits(
        value_: float, significant_digits: int, provider: System.IFormatProvider
    ) -> str: ...
    @staticmethod
    def GetFilterString(
        dataBinding: IDataBinding,
        context: IReportContext,
        table: System.Data.DataTable,
        top: IDataFilter,
        belongToGroup: IDataFilter,
    ) -> str: ...
    @staticmethod
    def Process(template: IReportTemplate, context: IReportContext) -> None: ...
    @staticmethod
    def GetFilePath(image: IImage, templateFilePath: str) -> str: ...
    @staticmethod
    def ConvertTo(value_: Any, defaultValue: T) -> T: ...
    @staticmethod
    def GetContentType(textbox: ITextbox) -> TextboxContentType: ...
    @staticmethod
    def ProcessMacro(context: IReportContext, text: str) -> str: ...
    @staticmethod
    def GetText(textbox: ITextbox, context: IReportContext) -> str: ...
