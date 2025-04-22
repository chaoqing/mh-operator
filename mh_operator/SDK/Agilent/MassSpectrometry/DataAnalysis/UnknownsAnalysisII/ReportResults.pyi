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

from . import SampleRowID, UnknownsAnalysisDataSet
from .DataFile import DataFileBase
from .UI.Report import GraphicsFileMap, GraphicsFileType, IReportGraphics

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults

class CommandLine:  # Class
    def __init__(self) -> None: ...

    AccountName: str
    AnalysisFile: str
    BatchIDs: str
    BatchPath: str
    CancelEventName: str
    ConnectionTicket: str
    ConsoleTrace: bool
    Culture: str
    Domain: str
    EncryptedPassword: str
    Help: bool
    Local: bool
    Logfile: str
    Method: str
    NoGraphics: bool
    NoLogo: bool
    OutputPath: str
    Password: str
    Printer: str
    PublishFormat: str
    Queue: bool
    ReportFileName: str
    ReporterName: str
    SampleIDs: str
    Server: str
    Template: str
    User: str

class ErrorReportingSettingsSection(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationElementSectionBase
):  # Class
    def __init__(self) -> None: ...

    DumpLogOnNormalExit: bool  # readonly
    EmailAddress: str  # readonly
    Enabled: bool  # readonly

class ExitCode:  # Class
    Canceled: int  # static # readonly
    CommandLineError: int  # static # readonly
    Error: int  # static # readonly
    Ok: int  # static # readonly
    UnknownsError: int  # static # readonly

class GraphicsSizeSettingsSection(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationElementSectionBase
):  # Class
    def __init__(self) -> None: ...
    def GetWidth(self, type: GraphicsFileType, defaultValue: float) -> float: ...
    def GetHeight(self, type: GraphicsFileType, defaultValue: float) -> float: ...

class GraphicsWriter(System.IDisposable):  # Class
    def __init__(
        self,
        generator: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults.ResultsGenerator,
        dataFile: DataFileBase,
        batchID: Optional[int],
        sampleID: Optional[int],
        reportGraphics: IReportGraphics,
        outputPath: str,
        fileMap: GraphicsFileMap,
        allowOverwrite: bool,
    ) -> None: ...
    def Dispose(self) -> None: ...
    def WriteGraphics(self) -> None: ...

class IUnknownsAnalysisDataProvider(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportDataProvider,
    System.IDisposable,
):  # Interface
    AbortEventName: str
    AnalysisFileName: str  # readonly
    AuditTrailDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet
    )  # readonly
    BatchPath: str  # readonly
    IsAuditTrailing: bool  # readonly
    TargetSamples: List[SampleRowID]

    def GetHitsFromMethod(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: Optional[int],
        identificationMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.HitDataTable,
    ) -> int: ...
    def GetPeakQualifier(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        qualifierID: Optional[int],
        peakID: Optional[int],
        table: UnknownsAnalysisDataSet.PeakQualifierDataTable,
    ) -> int: ...
    def GetIonPeak(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        ionPeakID: Optional[int],
        table: UnknownsAnalysisDataSet.IonPeakDataTable,
    ) -> int: ...
    def ExecuteReader(
        self, batchID: int, sampleID: int, select: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults.IUnknownsAnalysisDataReader
    ): ...
    def GetSample(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.SampleDataTable,
    ) -> int: ...
    def GetTargetCompound(
        self,
        batchId: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetCompoundDataTable,
    ) -> int: ...
    def GetTargetMatchMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        targetMatchMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetMatchMethodDataTable,
    ) -> int: ...
    def GetTargetQualifier(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        qualifierID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetQualifierDataTable,
    ) -> int: ...
    def GetPeak(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        peakID: Optional[int],
        table: UnknownsAnalysisDataSet.PeakDataTable,
    ) -> int: ...
    def GetExactMass(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        hitID: Optional[int],
        exactMassID: Optional[int],
        table: UnknownsAnalysisDataSet.ExactMassDataTable,
    ) -> int: ...
    def GetAnalysis(self, table: UnknownsAnalysisDataSet.AnalysisDataTable) -> int: ...
    def CreateGraphics(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults.IUnknownsAnalysisGraphics
    ): ...
    def GetBatch(
        self, batchID: Optional[int], table: UnknownsAnalysisDataSet.BatchDataTable
    ) -> int: ...
    def GetAuxiliaryMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.AuxiliaryMethodDataTable,
    ) -> int: ...
    def GetLibrarySearchMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        identificationMethodID: Optional[int],
        librarySearchMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.LibrarySearchMethodDataTable,
    ) -> int: ...
    def GetIdentificationMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        identificationMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.IdentificationMethodDataTable,
    ) -> int: ...
    def GetHit(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        hitID: Optional[int],
        table: UnknownsAnalysisDataSet.HitDataTable,
    ) -> int: ...
    def GetComponent(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        table: UnknownsAnalysisDataSet.ComponentDataTable,
    ) -> int: ...
    def GetDeconvolutionMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
    ) -> int: ...

class IUnknownsAnalysisDataReader(System.IDisposable):  # Interface
    def __getitem__(self, name: str) -> Any: ...
    def IsDBNull(self, name: str) -> bool: ...
    def Read(self) -> bool: ...

class IUnknownsAnalysisGraphics(System.IDisposable):  # Interface
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchId: int,
        sampleId: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawSampleChromatogram(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchId: int,
        sampleId: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawHitLibrarySpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawHitLibrarySpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawComponentSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawComponentSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def DrawStructure(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    def GetComponentSpectrumRange(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        minx: float,
        maxx: float,
    ) -> None: ...
    def GetSampleChromatogramRange(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.GraphicsRange
    ): ...
    @overload
    def DrawIonPeaks(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawIonPeaks(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        width: float,
        height: float,
        showTIC: bool,
        showComponent: bool,
        showIons: bool,
        showLabels: bool,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawIonPeaks(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        width: float,
        height: float,
        showTIC: bool,
        showComponent: bool,
        showIons: bool,
        showLabels: bool,
        minX: Optional[float],
        maxX: Optional[float],
        minY: Optional[float],
        maxY: Optional[float],
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawEicPeaks(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawEicPeaks(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        width: float,
        height: float,
        minX: Optional[float],
        maxX: Optional[float],
        minY: Optional[float],
        maxY: Optional[float],
    ) -> iTextSharp.text.Image: ...
    def GetHitLibrarySpectrumRange(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        minx: float,
        maxx: float,
    ) -> None: ...
    @overload
    def DrawExtractedSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        width: float,
        height: float,
    ) -> iTextSharp.text.Image: ...
    @overload
    def DrawExtractedSpectrum(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
    ) -> iTextSharp.text.Image: ...

class IUnknownsAnalysisReportBuilderTask(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    System.Xml.Serialization.IXmlSerializable,
    System.IDisposable,
):  # Interface
    AnalysisFile: str
    BatchIDs: List[int]
    BatchPath: str
    Culture: str
    DestinationFile: str
    Local: bool
    ReporterName: str
    SampleIDs: List[int]
    TemplatePath: str

class IUnknownsAnalysisReportMethodTask(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    System.Xml.Serialization.IXmlSerializable,
    System.IDisposable,
):  # Interface
    AnalysisFile: str
    BatchIDs: List[int]
    BatchPath: str
    Culture: str
    MethodPath: str
    OutputPath: str
    ReporterName: str
    SampleIDs: List[int]

class IUnknownsAnalysisReportScriptTask(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    System.Xml.Serialization.IXmlSerializable,
    System.IDisposable,
):  # Interface
    AnalysisFile: str
    BatchIDs: List[int]
    BatchPath: str
    Culture: str
    DestinationFile: str
    MethodPath: str
    OpenPublishedFile: bool
    PrinterName: str
    ReporterName: str
    SampleIDs: List[int]
    TemplatePath: str

class IUnknownsAnalysisReportTask(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    System.Xml.Serialization.IXmlSerializable,
    System.IDisposable,
):  # Interface
    AnalysisFile: str
    BatchID: Optional[int]
    BatchPath: str
    ConnectionTicket: str
    Culture: str
    OutputPath: str
    ReporterName: str
    SampleID: Optional[int]

class ReportBuilderTask(
    System.Xml.Serialization.IXmlSerializable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults.IUnknownsAnalysisReportBuilderTask,
    System.IDisposable,
):  # Class
    def __init__(self) -> None: ...

    Actions: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskAction
    ]  # readonly
    AnalysisFile: str
    BatchIDs: List[int]
    BatchPath: str
    CancelEventName: str
    Context: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskContext
    )
    Culture: str
    DestinationFile: str
    Local: bool
    ProcessingPriority: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.TaskPriority
    )
    ReporterName: str
    SampleIDs: List[int]
    TaskDescription: str  # readonly
    TaskLockName: str  # readonly
    TaskName: str  # readonly
    TemplatePath: str

    def Process(self) -> None: ...
    def GetSchema(self) -> System.Xml.Schema.XmlSchema: ...
    def WriteXml(self, writer: System.Xml.XmlWriter) -> None: ...
    def Dispose(self) -> None: ...
    def ReadXml(self, reader: System.Xml.XmlReader) -> None: ...

class ReportConfiguration:  # Class
    ErrorReportingSettingsSection: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults.ErrorReportingSettingsSection
    )  # readonly
    GraphicsSizeSettingsSection: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults.GraphicsSizeSettingsSection
    )  # readonly
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults.ReportConfiguration
    )  # static # readonly

class ReportMethodTask(
    System.Xml.Serialization.IXmlSerializable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults.IUnknownsAnalysisReportMethodTask,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    System.IDisposable,
):  # Class
    def __init__(self) -> None: ...

    Actions: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskAction
    ]  # readonly
    AnalysisFile: str
    BatchIDs: List[int]
    BatchPath: str
    CancelEventName: str
    Context: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskContext
    )
    Culture: str
    MethodPath: str
    OutputPath: str
    ProcessingPriority: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.TaskPriority
    )
    ReporterName: str
    SampleIDs: List[int]
    TaskDescription: str  # readonly
    TaskLockName: str  # readonly
    TaskName: str  # readonly

    def Process(self) -> None: ...
    def GetSchema(self) -> System.Xml.Schema.XmlSchema: ...
    def WriteXml(self, writer: System.Xml.XmlWriter) -> None: ...
    def Dispose(self) -> None: ...
    def ReadXml(self, reader: System.Xml.XmlReader) -> None: ...

class ReportScriptTask(
    System.Xml.Serialization.IXmlSerializable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults.IUnknownsAnalysisReportScriptTask,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    System.IDisposable,
):  # Class
    def __init__(self) -> None: ...

    Actions: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskAction
    ]  # readonly
    AnalysisFile: str
    BatchIDs: List[int]
    BatchPath: str
    CancelEventName: str
    Context: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskContext
    )
    Culture: str
    DestinationFile: str
    MethodPath: str
    OpenPublishedFile: bool
    PrinterName: str
    ProcessingPriority: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.TaskPriority
    )
    ReporterName: str
    SampleIDs: List[int]
    TaskDescription: str  # readonly
    TaskLockName: str  # readonly
    TaskName: str  # readonly
    TemplatePath: str

    def Process(self) -> None: ...
    def GetSchema(self) -> System.Xml.Schema.XmlSchema: ...
    def WriteXml(self, writer: System.Xml.XmlWriter) -> None: ...
    def Dispose(self) -> None: ...
    def ReadXml(self, reader: System.Xml.XmlReader) -> None: ...

class ResultsGenerator(System.IDisposable):  # Class
    def __init__(
        self,
        batchPath: str,
        analysisFile: str,
        outputPath: str,
        noGraphics: bool,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

    ResultFileName: str = ...  # static # readonly

    BatchID: Optional[int]
    CancelEventName: str
    ReporterName: str
    SampleID: Optional[int]

    def Run(self) -> None: ...
    def Dispose(self) -> None: ...

class UnknownsAnalysisReportTask(
    System.Xml.Serialization.IXmlSerializable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTask,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportResults.IUnknownsAnalysisReportTask,
):  # Class
    def __init__(self) -> None: ...

    AnalysisFile: str
    BatchID: Optional[int]
    BatchPath: str
    CancelEventName: str
    ConnectionTicket: str
    Context: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.IQueuedTaskContext
    )
    Culture: str
    OutputPath: str
    ProcessingPriority: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QueuedTask.TaskPriority
    )
    ReporterName: str
    SampleID: Optional[int]

    def Dispose(self) -> None: ...
