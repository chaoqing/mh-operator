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

from . import IBlankHits, IReportProgress, SampleRowID
from .Command import CommandContext
from .Utils import LibraryMzValues

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Analysis

class AnalysisTaskScheduler(System.Threading.Tasks.TaskScheduler):  # Class
    def __init__(self) -> None: ...

    MaximumConcurrencyLevel: int  # readonly

class AnalyzeSample(IReportProgress):  # Class
    def __init__(
        self,
        context: CommandContext,
        abort: System.Threading.ManualResetEvent,
        batchID: int,
        sampleID: int,
        reanalyze: bool,
        libraryMzValues: LibraryMzValues,
        blankHits: IBlankHits,
        taskScheduler: System.Threading.Tasks.TaskScheduler,
    ) -> None: ...

    SampleRowID: SampleRowID  # readonly

    def ClearProgress(self) -> None: ...
    def ClearTargetMatchResults(self) -> None: ...
    @overload
    def Identify(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Identify(self) -> None: ...
    def FinishProgress(self) -> None: ...
    def ClearDeconvolutionResults(self) -> None: ...
    def ClearBlankSubtraction(self) -> None: ...
    @staticmethod
    def IsBlank(sampleType: str) -> bool: ...
    @overload
    def TargetMatch(self, result: System.IAsyncResult) -> None: ...
    @overload
    def TargetMatch(self) -> None: ...
    def ClearIdentificationResults(self) -> None: ...
    @overload
    def Deconvolute(self, result: System.IAsyncResult) -> None: ...
    @overload
    def Deconvolute(self) -> None: ...
    def ReportProgress(self, totalSteps: int, currentStep: int) -> None: ...
    @overload
    def BlankSubtract(self, tasks: List[System.Threading.Tasks.Task[None]]) -> None: ...
    @overload
    def BlankSubtract(self) -> None: ...
