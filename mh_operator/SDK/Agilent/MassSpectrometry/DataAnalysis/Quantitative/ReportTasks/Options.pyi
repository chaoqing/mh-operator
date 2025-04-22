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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportTasks.Options

class ExcelReportControl:  # Class
    def __init__(self) -> None: ...

    Command: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportTasks.Options.ExcelReportControlCommand
    )
    Options: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportTasks.Options.ExcelReportControlOptions
    )

class ExcelReportControlCommand:  # Class
    def __init__(self) -> None: ...

    DestinationFullName: str
    ExcelBinaryPathName: str
    ExcelTemplatePathName: str
    GraphicsPathName: str
    PrinterName: str
    PublishFormat: str
    ReportFileDestination: str
    ReportPrinterDestination: str
    ResultsFullName: str
    UserName: str

class ExcelReportControlOptions:  # Class
    def __init__(self) -> None: ...

    IncludeFooter: bool
    IncludeHeader: bool
    IncludeTitle: bool
    Orientation: str
    TableColumns: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportTasks.Options.ExcelReportControlOptionsTableColumns
    )
    TableSorting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportTasks.Options.ExcelReportControlOptionsTableSorting
    )
    XPages: str
    YPages: str

class ExcelReportControlOptionsTableColumns:  # Class
    def __init__(self) -> None: ...

    Column: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportTasks.Options.ExcelReportControlOptionsTableColumnsColumn
    ]
    Count: str
    TableName: str

class ExcelReportControlOptionsTableColumnsColumn:  # Class
    def __init__(self) -> None: ...

    Format: str
    Index: str
    XPath: str

class ExcelReportControlOptionsTableSorting:  # Class
    def __init__(self) -> None: ...

    Count: str
    Sort: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportTasks.Options.ExcelReportControlOptionsTableSortingSort
    ]
    TableName: str

class ExcelReportControlOptionsTableSortingSort:  # Class
    def __init__(self) -> None: ...

    Column: str
    Index: str
    Order: str
