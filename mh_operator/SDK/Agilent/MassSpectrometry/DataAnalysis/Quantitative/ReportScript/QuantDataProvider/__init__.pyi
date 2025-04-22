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

from . import Filters

# Discovered Generic TypeVars:
T = TypeVar("T")
from . import (
    GraphicsRange,
    IFixedGraphics,
    IReportCompliance,
    IReportContext,
    IReportDataProvider,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider

class CalCurveGraphics(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.ICalCurveGraphics,
):  # Class
    def __init__(
        self,
        provider: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.QuantDataProvider,
    ) -> None: ...
    def DrawCalibration(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    def Dispose(self) -> None: ...

class CalCurveWrap(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.ControlWrapBase[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CalCurve
    ]
):  # Class
    def __init__(
        self,
        provider: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.QuantDataProvider,
    ) -> None: ...

class ChromSpecGraphics(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IChromSpecGraphics,
):  # Class
    def __init__(
        self,
        provider: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.QuantDataProvider,
    ) -> None: ...
    @overload
    def DrawCompoundQualifierPeaks(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawCompoundQualifierPeaks(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def DrawPeakAveragedSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def GetReferenceSpectrumRange(
        self, sampleId: int, compoundId: int
    ) -> Optional[GraphicsRange]: ...
    @overload
    def DrawReferenceSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawReferenceSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        drawStructure: bool,
    ) -> iTextSharp.text.Image: ...
    def GetAlternativeTargetHitLibrarySpectrumRange(
        self, sampleId: int, compoundId: int
    ) -> Optional[GraphicsRange]: ...
    def DrawCompoundOriginalPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def DrawStructure(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    def GetPeakAveragedSpectrumRange(
        self, sampleId: int, compoundId: int
    ) -> Optional[GraphicsRange]: ...
    @overload
    def DrawCompoundPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawCompoundPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def DrawOriginalQualifierPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawPeakSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawPeakSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def Dispose(self) -> None: ...
    def DrawAlternativeTargetHitLibrarySpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawQualifierPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawQualifierPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def GetPeakSpectrumRange(
        self, sampleId: int, compoundId: int
    ) -> Optional[GraphicsRange]: ...

class ChromSpecWrap(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.ControlWrapBase[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ChromSpec
    ]
):  # Class
    def __init__(
        self,
        provider: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.QuantDataProvider,
    ) -> None: ...

class ControlWrapBase(Generic[T]):  # Class
    def __init__(
        self,
        provider: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.QuantDataProvider,
    ) -> None: ...
    def GetControl(self) -> T: ...
    def Release(self) -> None: ...
    def Dispose(self) -> None: ...
    def AddRef(self) -> None: ...

class FixedGraphicsFile(IFixedGraphics, System.IDisposable):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, file: str) -> None: ...
    def Dispose(self) -> None: ...

class ICalCurveGraphics(System.IDisposable):  # Interface
    def DrawCalibration(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...

class IChromSpecGraphics(System.IDisposable):  # Interface
    @overload
    def DrawCompoundQualifierPeaks(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawCompoundQualifierPeaks(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def DrawPeakAveragedSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def GetReferenceSpectrumRange(
        self, sampleId: int, compoundId: int
    ) -> Optional[GraphicsRange]: ...
    @overload
    def DrawReferenceSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawReferenceSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        drawStructure: bool,
    ) -> iTextSharp.text.Image: ...
    def GetAlternativeTargetHitLibrarySpectrumRange(
        self, sampleId: int, compoundId: int
    ) -> Optional[GraphicsRange]: ...
    def DrawCompoundOriginalPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def DrawStructure(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    def GetPeakAveragedSpectrumRange(
        self, sampleId: int, compoundId: int
    ) -> Optional[GraphicsRange]: ...
    @overload
    def DrawCompoundPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawCompoundPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawPeakSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawPeakSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def DrawAlternativeTargetHitLibrarySpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawQualifierPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawQualifierPeak(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def GetPeakSpectrumRange(
        self, sampleId: int, compoundId: int
    ) -> Optional[GraphicsRange]: ...

class IDataFilter(object):  # Interface
    FilterString: str  # readonly
    SupportsFilterString: bool  # readonly

    def Match(self, row: System.Data.DataRow) -> bool: ...

class IQuantDataProvider(IReportDataProvider, System.IDisposable):  # Interface
    ApplicationType: str  # readonly
    AuditTrailDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet
    )  # readonly
    BatchAttributes: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.BatchAttributes
    )  # readonly
    BatchFileName: str  # readonly
    BatchFolder: str  # readonly
    BatchID: int  # readonly
    BatchPath: str  # readonly
    CompoundFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IDataFilter
    )
    InstrumentType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType
    )  # readonly
    IsAuditTrailing: bool  # readonly
    SampleFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IDataFilter
    )
    _DataNavigator: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DataNavigator
    )  # readonly

    def GetPeakQualifier(
        self,
        batchId: int,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        peakId: int,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.PeakQualifierRow
    ): ...
    def GetAllSamples(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.BatchRow
    ]: ...
    def CreateCalCurveGraphics(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.ICalCurveGraphics
    ): ...
    def GetSample(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.BatchRow
    ): ...
    def SelectPeakQualifiers(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.PeakQualifierRow
    ]: ...
    def SelectSamples(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.BatchRow
    ]: ...
    def SelectPeaks(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.PeakRow
    ]: ...
    def SelectCompounds(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    ]: ...
    def CreateChromSpecGraphics(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IChromSpecGraphics
    ): ...
    def GetSignals(
        self, batchId: int, sampleId: int
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.SignalRow
    ]: ...
    def CreateSampleGraphics(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.ISampleGraphics
    ): ...
    def GetCompoundChromatogram(self, sampleId: int, compoundId: int) -> Any: ...
    def GetCompound(
        self, batchId: int, sampleId: int, compoundId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    ): ...
    def SelectCalibrations(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.CalibrationRow
    ]: ...
    def GetScanTypes(
        self, batchId: int, sampleId: int
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    def SelectQualifiers(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetQualifierRow
    ]: ...
    def GetTICResponse(
        self, batchId: int, sampleId: int, compoundId: int, istdRT: float
    ) -> float: ...
    def GetQualifier(
        self, batchId: int, sampleId: int, compoundId: int, qualifierId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetQualifierRow
    ): ...
    def GetPeak(
        self, batchId: int, sampleId: int, compoundId: int, peakId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.PeakRow
    ): ...
    def GetAllCompounds(
        self, batchId: int, sampleId: int
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    ]: ...
    def GetCalibration(
        self, batchId: int, sampleId: int, compoundId: int, levelId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.CalibrationRow
    ): ...
    def GetSampleChromatogram(
        self, sampleId: int, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> Any: ...

class IQuantReportScriptTask(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    System.Xml.Serialization.IXmlSerializable,
    System.IDisposable,
):  # Interface
    BatchFile: str
    BatchPath: str
    CompoundIds: List[int]
    FixedGraphicsFile: str
    GraphicsSettingsFile: str
    InstrumentType: str
    Method: str
    OutputFile: str
    PrinterName: str
    SampleIds: List[int]
    Template: str

class ISampleGraphics(System.IDisposable):  # Interface
    @overload
    def GetChromatogramRange(self, sampleId: int) -> GraphicsRange: ...
    @overload
    def GetChromatogramRange(
        self, sampleId: int, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> GraphicsRange: ...
    @overload
    def GetChromatogramRange(
        self, sampleId: int, deviceName: str, ordinalNumber: int, signalName: str
    ) -> GraphicsRange: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
        deviceName: str,
        ordinalNumber: int,
        signalName: str,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
        deviceName: str,
        ordinalNumber: int,
        signalName: str,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...

class QuantDataProvider(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IQuantDataProvider,
    System.IDisposable,
    IReportDataProvider,
):  # Class
    def __init__(
        self,
        presentationState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.PresentationState,
        abort: System.Threading.WaitHandle,
    ) -> None: ...

    ApplicationType: str  # readonly
    AuditTrailDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet
    )  # readonly
    BatchAttributes: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.BatchAttributes
    )  # readonly
    BatchFileName: str  # readonly
    BatchFolder: str  # readonly
    BatchID: int  # readonly
    BatchPath: str  # readonly
    Compliance: IReportCompliance  # readonly
    CompoundFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IDataFilter
    )
    CurrentVersion: str  # readonly
    FixedGraphics: IFixedGraphics
    InstrumentType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType
    )  # readonly
    IsAuditTrailing: bool  # readonly
    MethodPath: str
    ReportContext: IReportContext  # readonly
    SampleFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IDataFilter
    )
    TemplatePath: str
    _DataNavigator: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DataNavigator
    )  # readonly

    def GetPeakQualifier(
        self,
        batchId: int,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        peakId: int,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.PeakQualifierRow
    ): ...
    def GetAllSamples(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.BatchRow
    ]: ...
    def FormatNumber(self, columnName: str, value_: float) -> str: ...
    def CreateCalCurveGraphics(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.ICalCurveGraphics
    ): ...
    def IsAttemptingAbort(self) -> bool: ...
    def TranslateEnumValue(
        self, tableName: str, columnName: str, value_: str
    ) -> str: ...
    def Dispose(self) -> None: ...
    def CheckAbortSignal(self) -> None: ...
    def GetSample(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.BatchRow
    ): ...
    def SelectPeakQualifiers(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.PeakQualifierRow
    ]: ...
    @staticmethod
    def DrawImage(
        writer: iTextSharp.text.pdf.PdfWriter,
        width: float,
        height: float,
        d: System.Action[Agilent.MassSpectrometry.GUI.Plot.IGraphics],
    ) -> iTextSharp.text.Image: ...
    def SelectSamples(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.BatchRow
    ]: ...
    def SelectPeaks(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.PeakRow
    ]: ...
    def GetNumberFormat(self, columnName: str) -> str: ...
    def FormatDateTime(self, columnName: str, value_: System.DateTime) -> str: ...
    def ProgressMessage(self, pageNumber: int, message: str) -> None: ...
    def SelectCompounds(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    ]: ...
    def CreateChromSpecGraphics(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IChromSpecGraphics
    ): ...
    def GetSignals(
        self, batchId: int, sampleId: int
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.SignalRow
    ]: ...
    def CreateSampleGraphics(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.ISampleGraphics
    ): ...
    def GetCompoundChromatogram(self, sampleId: int, compoundId: int) -> Any: ...
    def GetCompound(
        self, batchId: int, sampleId: int, compoundId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    ): ...
    def SelectCalibrations(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.CalibrationRow
    ]: ...
    def GetScanTypes(
        self, batchId: int, sampleId: int
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MSScanType]: ...
    def SelectQualifiers(
        self, filter: str, sort: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetQualifierRow
    ]: ...
    def GetPeak(
        self, batchId: int, sampleId: int, compoundId: int, peakId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.PeakRow
    ): ...
    def GetQualifier(
        self, batchId: int, sampleId: int, compoundId: int, qualifierId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetQualifierRow
    ): ...
    def GetAllCompounds(
        self, batchId: int, sampleId: int
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundRow
    ]: ...
    def GetTICResponse(
        self, batchId: int, sampleId: int, compoundId: int, istdRT: float
    ) -> float: ...
    def GetCalibration(
        self, batchId: int, sampleId: int, compoundId: int, levelId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.CalibrationRow
    ): ...
    def GetSampleChromatogram(
        self, sampleId: int, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> Any: ...

class QuantReportScriptTask(
    System.Xml.Serialization.IXmlSerializable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IQuantReportScriptTask,
):  # Class
    def __init__(self) -> None: ...

    BatchFile: str
    BatchPath: str
    CompoundIds: List[int]
    Context: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskContext
    )
    FixedGraphicsFile: str
    GraphicsSettingsFile: str
    InstrumentType: str
    Method: str
    OutputFile: str
    PrinterName: str
    SampleIds: List[int]
    Template: str

    def Dispose(self) -> None: ...

class SampleDataWrap(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.ControlWrapBase[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleData.SampleDataControl
    ]
):  # Class
    def __init__(
        self,
        provider: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.QuantDataProvider,
    ) -> None: ...

class SampleGraphics(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.ISampleGraphics,
):  # Class
    def __init__(
        self,
        provider: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.QuantDataProvider,
    ) -> None: ...
    @overload
    def GetChromatogramRange(self, sampleId: int) -> GraphicsRange: ...
    @overload
    def GetChromatogramRange(
        self, sampleId: int, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> GraphicsRange: ...
    @overload
    def GetChromatogramRange(
        self, sampleId: int, deviceName: str, ordinalNumber: int, signalName: str
    ) -> GraphicsRange: ...
    def Dispose(self) -> None: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
        deviceName: str,
        ordinalNumber: int,
        signalName: str,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        sampleId: int,
        width: float,
        height: float,
        deviceName: str,
        ordinalNumber: int,
        signalName: str,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...

class SignalRow:  # Class
    def __init__(self) -> None: ...

    BatchID: int
    DeviceName: str  # readonly
    IsMS: bool  # readonly
    OrdinalNumber: int  # readonly
    SampleID: int
    SignalName: str  # readonly

    def ToString(self) -> str: ...
