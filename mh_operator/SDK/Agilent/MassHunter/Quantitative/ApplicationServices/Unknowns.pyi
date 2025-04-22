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

from . import Chromatogram, IApplicationServiceBase, IDataTableTransfer

# Stubs for namespace: Agilent.MassHunter.Quantitative.ApplicationServices.Unknowns

class IUnknownsAnalysis(IApplicationServiceBase, System.IDisposable):  # Interface
    def AnalyzeAll(self) -> None: ...
    def GetHits(
        self,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: Optional[int],
        componentId: Optional[int],
        hitId: Optional[int],
    ) -> IDataTableTransfer: ...
    def GetIonPeak(
        self,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: Optional[int],
        componentId: Optional[int],
        ionPeakId: Optional[int],
    ) -> IDataTableTransfer: ...
    def GetTargetMatchMethod(
        self, batchID: int, sampleID: int, targetMatchMethodID: Optional[int]
    ) -> IDataTableTransfer: ...
    def GetLibrarySearchMethod(
        self,
        batchID: int,
        sampleID: int,
        identificationMethodID: Optional[int],
        librarySearchMethodID: Optional[int],
    ) -> IDataTableTransfer: ...
    def LoadMethodToAllSamples(self, method: str) -> None: ...
    def GetComponents(
        self,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: Optional[int],
        componentId: Optional[int],
    ) -> IDataTableTransfer: ...
    def GetIdentificationMethod(
        self, batchID: int, sampleID: int, identificationMethodID: Optional[int]
    ) -> IDataTableTransfer: ...
    def GetSamples(
        self, batchId: Optional[int], sampleId: Optional[int]
    ) -> IDataTableTransfer: ...
    def AddSamples(self, sampleFileNames: List[str]) -> None: ...
    def GetTIC(
        self, batchID: int, sampleID: int, scan: str, ionPolarity: str
    ) -> Chromatogram: ...
    def CreateAnlaysis(self, batchFolder: str, analysisName: str) -> None: ...
    def GetDeconvolutionMethod(
        self, batchId: int, sampleId: int, deconvolutionMethodId: Optional[int]
    ) -> IDataTableTransfer: ...

class IUnknownsAnalysisCallback(object):  # Interface
    def AnalysisProgressChanged(
        self,
        batchId: int,
        sampleId: int,
        analysisType: str,
        currentStep: int,
        totalSteps: int,
    ) -> None: ...
