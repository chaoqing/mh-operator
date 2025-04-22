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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CefFileIO

class CefFileReader:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def Open(
        fullFileName: str,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.CefFileIO.ICefFile: ...

class ICefCompound(object):  # Interface
    BasePeakAbundance: str  # readonly
    CasNumber: str  # readonly
    FeatureFindingAlgorithm: str  # readonly
    Formula: str  # readonly
    Name: str  # readonly
    NeutralMass: float  # readonly
    RetentionTimeInMinutes: float  # readonly

    def GetFragmentIonConfirmation(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CefFileIO.ICefFragmentIonConfirmation
    ): ...
    def GetSpectrum(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.CefFileIO.ICefSpectrum: ...

class ICefFile(System.IDisposable):  # Interface
    def GetNextCompound(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.CefFileIO.ICefCompound: ...
    def GCQTOF(self) -> bool: ...

class ICefFragmentIonConfirmation(object):  # Interface
    FragmentIonPeaks: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CefFileIO.ICefFragmentIonPeak
    ]
    IonPolarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity

class ICefFragmentIonPeak(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CefFileIO.ICefPeak,
    System.IComparable,
):  # Interface
    CoelutionScore: Optional[float]  # readonly
    CollisionEnergy: Optional[float]  # readonly
    FragmentorVoltage: Optional[float]  # readonly
    LibraryAbundance: Optional[float]  # readonly

class ICefPeak(System.IComparable):  # Interface
    Intensity: float  # readonly
    MZ: float  # readonly

class ICefSpectrum(object):  # Interface
    CollisionEnergy: Optional[float]  # readonly
    FragmentorVoltage: Optional[float]  # readonly
    IonPolarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    MzOfInterest: float  # readonly
    Peaks: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CefFileIO.ICefPeak
    ]
    ScanType: str
    Type: str
