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

from .Agilent.MassSpectrometry.DataAnalysis import IFunction, Molecule
from .BasicTypes import PeakList

# Stubs for namespace: IsotopePatternCalculator

class CalculatorBase:  # Class
    ...

class IIsotopePattern(object):  # Interface
    DeltaMZ: float  # readonly
    MZAtMax: float  # readonly
    MZCentroid: float  # readonly
    MZMono: float  # readonly
    MZStandardDeviationSquared: float  # readonly
    Peaks: PeakList  # readonly
    SignalEnd: int  # readonly
    Spectrum: List[float]  # readonly
    StartMZ: float  # readonly

class IsotopePatternCalculatorAlgebra(
    IsotopePatternCalculator.CalculatorBase, IsotopePatternCalculator.IIsotopePattern
):  # Class
    @overload
    def __init__(
        self,
        molecule: Molecule,
        z: int,
        userParameter: IsotopePatternCalculator.IsotopePatternCalculatorParameters,
    ) -> None: ...
    @overload
    def __init__(
        self,
        elementCounts: Dict[int, float],
        maxPeakCount: int,
        m0: float,
        userParameter: IsotopePatternCalculator.IsotopePatternCalculatorParameters,
    ) -> None: ...

    DeltaMZ: float  # readonly
    MZAtMax: float  # readonly
    MZCentroid: float  # readonly
    MZMono: float  # readonly
    MZStandardDeviationSquared: float  # readonly
    Peaks: PeakList  # readonly
    SignalEnd: int  # readonly
    Spectrum: List[float]  # readonly
    StartMZ: float  # readonly

class IsotopePatternCalculatorFFT(
    IsotopePatternCalculator.CalculatorBase, IsotopePatternCalculator.IIsotopePattern
):  # Class
    def __init__(
        self,
        neutralMolecule: Molecule,
        z: int,
        userParameter: IsotopePatternCalculator.IsotopePatternCalculatorParameters,
    ) -> None: ...

    DeltaMZ: float  # readonly
    MZAtMax: float  # readonly
    MZCentroid: float  # readonly
    MZMono: float  # readonly
    MZStandardDeviationSquared: float  # readonly
    Peaks: PeakList  # readonly
    SignalEnd: int  # readonly
    Spectrum: List[float]  # readonly
    StartMZ: float  # readonly

class IsotopePatternCalculatorParameters:  # Class
    def __init__(self) -> None: ...

    MinSamplingRate: float
    PeakWidthFunction: IFunction
    ResolveFineStructure: bool

    def InitializeForTOF(self) -> None: ...
