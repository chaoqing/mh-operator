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

from . import QuantDataProvider
from .Compliance import ICompliance, IImpersonationContext
from .ScriptEngine import IronEngine

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript

class GraphicsRange:  # Struct
    def __init__(self, min: float, max: float) -> None: ...

    Max: float  # readonly
    Min: float  # readonly

class IFixedGraphics(object):  # Interface
    def GetSampleRangeX(
        self, sampleName: str
    ) -> Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.GraphicsRange
    ]: ...
    def GetSampleRangeY(
        self, sampleName: str
    ) -> Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.GraphicsRange
    ]: ...
    def GetCompoundRangeMz(
        self, compoundName: str
    ) -> Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.GraphicsRange
    ]: ...
    def GetCompoundRangeX(
        self, compoundName: str
    ) -> Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.GraphicsRange
    ]: ...
    def GetCompoundRangeY(
        self, compoundName: str
    ) -> Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.GraphicsRange
    ]: ...

class IImpersonateContext(System.IDisposable):  # Interface
    ...

class IReportCompliance(object):  # Interface
    ComplianceDisplayName: str  # readonly
    ComplianceName: str  # readonly
    Server: str  # readonly
    UserName: str  # readonly

    def TranslateToLocalPath(self, pathName: str) -> str: ...
    def Impersonate(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IImpersonateContext
    ): ...

class IReportContext(object):  # Interface
    ComplianceDisplayName: str  # readonly
    ComplianceName: str  # readonly
    ComplianceServer: str  # readonly
    OutputPath: str
    PreferredPageSize: str
    UserName: str  # readonly

    def CreateReportPlot(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportPlot
    ): ...

class IReportDataProvider(object):  # Interface
    Compliance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportCompliance
    )  # readonly
    CurrentVersion: str  # readonly
    FixedGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IFixedGraphics
    )
    MethodPath: str
    ReportContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportContext
    )  # readonly
    TemplatePath: str

    def ProgressMessage(self, pageNumber: int, message: str) -> None: ...
    def CheckAbortSignal(self) -> None: ...
    def FormatNumber(self, columnName: str, value_: float) -> str: ...
    def IsAttemptingAbort(self) -> bool: ...
    def FormatDateTime(self, columnName: str, value_: System.DateTime) -> str: ...
    def TranslateEnumValue(
        self, tableName: str, columnName: str, value_: str
    ) -> str: ...
    def GetNumberFormat(self, columnName: str) -> str: ...

class IReportPlot(object):  # Interface
    BottomAxisTitle: str
    LeftAxisTitle: str
    MaxX: float
    MaxY: float
    MinX: float
    MinY: float
    Title: str

    def ClearSeries(self) -> None: ...
    def AutoScale(self) -> None: ...
    def AddSeries(
        self,
        series: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportPlotSeries,
    ) -> None: ...
    def Draw(
        self, writer: iTextSharp.text.pdf.PdfWriter, width: float, height: float
    ) -> iTextSharp.text.Image: ...
    def CreateSeries(
        self, data: Any
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportPlotSeries
    ): ...

class IReportPlotSeries(object):  # Interface
    _Series: Any  # readonly

    @overload
    def Normalize(self, max: float) -> None: ...
    @overload
    def Normalize(self, min: float, max: float) -> None: ...

class IReportScript(System.IDisposable):  # Interface
    DataProvider: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportDataProvider
    )
    PreferredPageSize: str

    def Process(self, file: str) -> None: ...

class ImpersonationContext(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IImpersonateContext,
    System.IDisposable,
):  # Class
    def __init__(self, ictx: IImpersonationContext) -> None: ...
    def Dispose(self) -> None: ...

class ProviderOption:  # Class
    def __init__(self) -> None: ...

    Name: str
    Value: str

class ReportCompliance(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportCompliance
):  # Class
    def __init__(self, compliance: ICompliance) -> None: ...

    ComplianceDisplayName: str  # readonly
    ComplianceName: str  # readonly
    Server: str  # readonly
    UserName: str  # readonly

    def TranslateToLocalPath(self, pathName: str) -> str: ...
    def Impersonate(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IImpersonateContext
    ): ...

class ReportContext(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportContext
):  # Class
    def __init__(self, compliance: ICompliance) -> None: ...

    ComplianceDisplayName: str  # readonly
    ComplianceName: str  # readonly
    ComplianceServer: str  # readonly
    OutputPath: str
    PreferredPageSize: str
    UserName: str  # readonly

    def CreateReportPlot(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportPlot
    ): ...

class ReportDefinition:  # Class
    def __init__(self) -> None: ...

    Codes: List[str]
    Copyright: str
    Cultures: List[str]
    Debug: bool
    Language: str
    PageSizes: List[str]
    ProviderOptions: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.ProviderOption
    ]
    PublishFormats: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.ReportPublishFormat
    ]
    References: List[str]
    Type: str

class ReportPlot(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportPlot
):  # Class
    def __init__(self) -> None: ...

    BottomAxisTitle: str
    LeftAxisTitle: str
    MaxX: float
    MaxY: float
    MinX: float
    MinY: float
    Title: str

    def ClearSeries(self) -> None: ...
    def AutoScale(self) -> None: ...
    def AddSeries(
        self,
        series: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportPlotSeries,
    ) -> None: ...
    def Draw(
        self, writer: iTextSharp.text.pdf.PdfWriter, width: float, height: float
    ) -> iTextSharp.text.Image: ...
    def CreateSeries(
        self, data: Any
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportPlotSeries
    ): ...

class ReportPlotSeries(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportPlotSeries
):  # Class
    def __init__(
        self, fxdata: Agilent.MassSpectrometry.DataAnalysis.IFXData
    ) -> None: ...

    _Series: Any  # readonly

    @overload
    def Normalize(self, min: float, max: float) -> None: ...
    @overload
    def Normalize(self, max: float) -> None: ...

class ReportPublishFormat:  # Class
    def __init__(self) -> None: ...

    Extension: str
    Name: str

class ReportScriptEngine:  # Class
    FilesToClean: List[str]  # static # readonly

    @staticmethod
    def CreateReportScript(
        pathName: str,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportScript
    ): ...
    @staticmethod
    def LoadTemplate(
        pathName: str,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.ReportDefinition
    ): ...

class ReportScriptException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, ex: System.Exception) -> None: ...

class ReportScriptPython(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportScript,
):  # Class
    def __init__(self) -> None: ...

    AbortHandleName: str
    DataProvider: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportDataProvider
    )
    Files: List[str]
    PreferredPageSize: str
    ReportContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportContext
    )
    ResourceAssemblyPath: str

    @staticmethod
    def GetDebugEngine() -> IronEngine: ...
    def Process(self, file: str) -> None: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def SetDebugEngine(debugEngine: IronEngine) -> None: ...

class Utils:  # Class
    @staticmethod
    def GetDefaultPageSize(
        ci: System.Globalization.CultureInfo,
    ) -> iTextSharp.text.Rectangle: ...
    @staticmethod
    def GetPageSize(name: str) -> iTextSharp.text.Rectangle: ...
    @staticmethod
    def ProgressMessage(pageNumber: int, message: str) -> None: ...
    @staticmethod
    def DrawImage(
        writer: iTextSharp.text.pdf.PdfWriter,
        width: float,
        height: float,
        d: System.Action[Agilent.MassHunter.Quantitative.PlotControl.IGraphics],
    ) -> iTextSharp.text.Image: ...
