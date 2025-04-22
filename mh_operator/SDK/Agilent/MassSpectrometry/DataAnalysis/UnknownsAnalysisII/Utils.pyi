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

from . import IBlankHits, UnknownsAnalysisDataSet
from .Command import CommandContext

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Utils

class BlankHits(System.IDisposable, IBlankHits):  # Class
    def __init__(self, context: CommandContext) -> None: ...

    BlankSampleCount: int  # readonly

    def HasBlankHits(
        self,
        hit: UnknownsAnalysisDataSet.HitRow,
        parentComponent: UnknownsAnalysisDataSet.ComponentRow,
        modelIonPeak: UnknownsAnalysisDataSet.IonPeakRow,
        method: UnknownsAnalysisDataSet.BlankSubtractionMethodRow,
    ) -> bool: ...
    def Dispose(self) -> None: ...

class LibraryMzValues(System.IDisposable):  # Class
    def __init__(self, context: CommandContext) -> None: ...
    def Dispose(self) -> None: ...
    def GetLibraryMzValues(
        self, lsmrows: List[UnknownsAnalysisDataSet.LibrarySearchMethodRow]
    ) -> System.Collections.Generic.List[float]: ...
