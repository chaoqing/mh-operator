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
from .Command import CommandContext
from .ReportResults import (
    IUnknownsAnalysisDataProvider,
    IUnknownsAnalysisDataReader,
    IUnknownsAnalysisGraphics,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportDataProvider

class UnknownsAnalysisDataProvider(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportDataProvider,
    System.IDisposable,
    IUnknownsAnalysisDataProvider,
):  # Class
    def __init__(self, context: CommandContext) -> None: ...

    AbortEventName: str
    AnalysisFileName: str  # readonly
    AuditTrailDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet
    )  # readonly
    BatchPath: str  # readonly
    Compliance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportCompliance
    )  # readonly
    CurrentVersion: str  # readonly
    FixedGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IFixedGraphics
    )
    IsAuditTrailing: bool  # readonly
    MethodPath: str
    ReportContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IReportContext
    )  # readonly
    TargetSamples: List[SampleRowID]
    TemplatePath: str

    def GetTargetQualifier(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        qualifierID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetQualifierDataTable,
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
    def GetComponent(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        table: UnknownsAnalysisDataSet.ComponentDataTable,
    ) -> int: ...
    def FormatNumber(self, columnName: str, value_: float) -> str: ...
    def IsAttemptingAbort(self) -> bool: ...
    def GetDeconvolutionMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
    ) -> int: ...
    def TranslateEnumValue(
        self, tableName: str, columnName: str, value_: str
    ) -> str: ...
    def Dispose(self) -> None: ...
    def CheckAbortSignal(self) -> None: ...
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
    def GetBatch(
        self, batchID: Optional[int], table: UnknownsAnalysisDataSet.BatchDataTable
    ) -> int: ...
    def GetNumberFormat(self, columnName: str) -> str: ...
    def GetAuxiliaryMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.AuxiliaryMethodDataTable,
    ) -> int: ...
    def FormatDateTime(self, columnName: str, value_: System.DateTime) -> str: ...
    def GetHitsFromMethod(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: Optional[int],
        identificationMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.HitDataTable,
    ) -> int: ...
    def ProgressMessage(self, pageNumber: int, message: str) -> None: ...
    def GetAnalysis(self, table: UnknownsAnalysisDataSet.AnalysisDataTable) -> int: ...
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
    def GetLibrarySearchMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        identificationMethodID: Optional[int],
        librarySearchMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.LibrarySearchMethodDataTable,
    ) -> int: ...
    def ExecuteReader(
        self, batchID: int, sampleID: int, select: str
    ) -> IUnknownsAnalysisDataReader: ...
    def GetTargetMatchMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        targetMatchMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetMatchMethodDataTable,
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
    def CreateGraphics(self) -> IUnknownsAnalysisGraphics: ...
    def GetPeak(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        peakID: Optional[int],
        table: UnknownsAnalysisDataSet.PeakDataTable,
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
    def GetIdentificationMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        identificationMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.IdentificationMethodDataTable,
    ) -> int: ...

class UnknownsAnalysisDataReader(
    System.IDisposable, IUnknownsAnalysisDataReader
):  # Class
    def __getitem__(self, name: str) -> Any: ...
    def IsDBNull(self, name: str) -> bool: ...
    def Read(self) -> bool: ...
    def Dispose(self) -> None: ...

class UnknownsAnalysisGraphics(System.IDisposable, IUnknownsAnalysisGraphics):  # Class
    def __init__(
        self,
        provider: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.ReportDataProvider.UnknownsAnalysisDataProvider,
    ) -> None: ...
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
        showTic: bool,
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
        showTic: bool,
        showComponent: bool,
        showIons: bool,
        showLabels: bool,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
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
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
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
    def Dispose(self) -> None: ...
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
