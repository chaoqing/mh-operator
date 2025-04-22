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

from . import Chromatogram, IApplicationServiceBase, IDataTransfer

# Stubs for namespace: Agilent.MassHunter.Quantitative.ApplicationServices.MRMOptimizer

class ICEOptimizer(IApplicationServiceBase, System.IDisposable):  # Interface
    def GetSamples(self) -> List[str]: ...
    def OpenSamples(self, samplePathes: List[str]) -> None: ...
    def GetSamplePeaks(
        self, samplePath: str
    ) -> IDataTransfer[
        Agilent.MassHunter.Quantitative.ApplicationServices.MRMOptimizer.TransitionPeak
    ]: ...
    def GetOptimizedTransitions(
        self,
    ) -> IDataTransfer[
        Agilent.MassHunter.Quantitative.ApplicationServices.MRMOptimizer.TransitionPeak
    ]: ...

class IProductIonIdentifier(IApplicationServiceBase, System.IDisposable):  # Interface
    def GetSamplePeaksWithScanType(
        self, samplePath: str, scanType: str, ionPolarity: str
    ) -> IDataTransfer[
        Agilent.MassHunter.Quantitative.ApplicationServices.MRMOptimizer.TransitionPeak
    ]: ...
    def GetPeakSpectrum(
        self,
        samplePathName: str,
        ionPolarity: str,
        ms1: float,
        ce: Optional[float],
        fragmentor: Optional[float],
        rtStart: float,
        rtEnd: float,
    ) -> Agilent.MassHunter.Quantitative.ApplicationServices.MRMOptimizer.Spectrum: ...
    def OpenSamples(self, samplePathes: List[str]) -> None: ...
    def GetSamples(self) -> List[str]: ...
    def GetTIC(
        self, samplePath: str, scanType: str, ionPolarity: str
    ) -> Chromatogram: ...
    def GetSamplePeaks(
        self, samplePath: str
    ) -> IDataTransfer[
        Agilent.MassHunter.Quantitative.ApplicationServices.MRMOptimizer.TransitionPeak
    ]: ...

class Spectrum:  # Class
    def __init__(self) -> None: ...

    XValues: List[float]
    YValues: List[float]

class TransitionPeak:  # Class
    def __init__(self) -> None: ...

    AcquiredDwellTime: Optional[float]
    Area: Optional[float]
    ChromXValues: List[float]
    ChromYValues: List[float]
    CollisionEnergy: Optional[float]
    CompoundName: str
    DeltaEMV: Optional[float]
    EndX: Optional[float]
    EndY: Optional[float]
    FragmentorVoltage: Optional[float]
    Gain: Optional[float]
    Height: Optional[float]
    IonPolarity: str
    Ms1: float
    Ms1Resolution: str
    Ms2: float
    Ms2Resolution: str
    OptimizedDwellTime: Optional[float]
    RetentionTime: Optional[float]
    ScanMode: str
    ScanSegment: int
    StartX: Optional[float]
    StartY: Optional[float]
    TimeSegment: int
