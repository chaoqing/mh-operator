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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Report

class GraphicsFileMap:  # Class
    def __init__(self) -> None: ...
    def GetFile(
        self,
        rowID: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
        fileType: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Report.GraphicsFileType,
    ) -> str: ...
    def SetFile(
        self,
        rowID: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.RowID,
        fileType: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Report.GraphicsFileType,
        file: str,
    ) -> None: ...

class GraphicsFileType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ComponentSpectrum: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Report.GraphicsFileType
    ) = ...  # static # readonly
    HitLibrarySpectrum: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Report.GraphicsFileType
    ) = ...  # static # readonly
    SampleChromatogram: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Report.GraphicsFileType
    ) = ...  # static # readonly

class IReportGraphics(System.IDisposable):  # Interface
    def SetContext(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...
    def DrawComponentIonPeaks(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def DrawSampleChromatogram(
        self,
        batchID: int,
        sampleID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def DrawHitLibrarySpectrum(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def DrawComponentSpectrum(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def DrawIonPeakChromatogram(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def DrawComponentChromatogram(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...

class ReportGraphics(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Report.IReportGraphics,
    System.IDisposable,
):  # Class
    def __init__(self) -> None: ...
    def SetContext(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...
    def DrawComponentIonPeaks(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def DrawSampleChromatogram(
        self,
        batchID: int,
        sampleID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def DrawHitLibrarySpectrum(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def DrawComponentSpectrum(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def DrawIonPeakChromatogram(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def DrawComponentChromatogram(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        stream: System.IO.Stream,
        sizeInches: System.Drawing.SizeF,
    ) -> None: ...
    def Dispose(self) -> None: ...

class ResultsWriter:  # Class
    def __init__(
        self,
        dataFile: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataFileBase,
        batchID: Optional[int],
        sampleID: Optional[int],
        writer: System.Xml.XmlWriter,
        fileMap: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Report.GraphicsFileMap,
    ) -> None: ...
    def Write(self) -> None: ...
