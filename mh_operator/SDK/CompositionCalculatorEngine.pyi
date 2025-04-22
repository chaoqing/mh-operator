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

from .Agilent.MassSpectrometry.DataAnalysis import (
    FormulaGenerationRules,
    FormulaGenerator,
    IComposition,
    IIonSpeciesDetails,
    IModificationSpecies,
    IPrecursor,
    IsotopePattern,
    ITargetFormulaTracker,
    MassIsotopeChoice,
    SpectralPeak,
)
from .BasicTypes import FragmentIon

# Stubs for namespace: CompositionCalculatorEngine

class ChemicalElementLimitsFactory:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def ChemicalElementLimits(
        massChoice: MassIsotopeChoice, rules: FormulaGenerationRules
    ) -> CompositionCalculatorEngine.IChemicalElementLimits: ...

class FragmentFormulaGenerator:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def GetProductsForGivenPrecursor(
        precursorFormula: str,
        spectrum: List[FragmentIon],
        productMassAccuray: List[float],
        precursorSpecies: IModificationSpecies,
        parameters: FormulaGenerator.UserParameters,
    ) -> IPrecursor: ...
    @staticmethod
    def GetPrecursors(
        spectrum: List[FragmentIon],
        precursorPeaks: List[SpectralPeak],
        precursorSpecies: IModificationSpecies,
        precursorLowestIsotopeMZ: float,
        precursorZ: int,
        parameters: FormulaGenerator.UserParameters,
        productMassAccuray: List[float],
        precursorNeutralMass: float,
    ) -> List[IPrecursor]: ...

class IChemicalElementLimits(object):  # Interface
    def MaxWtFraction(self, elementSymbol: str, neutralMass: float) -> float: ...
    def MinCount(self, elementSymbol: str, neutralMass: float) -> int: ...
    def MaxCount(self, elementSymbol: str, neutralMass: float) -> int: ...

class IInternalComposition(IComposition):  # Interface
    IsotopePattern: IsotopePattern
    IsotopePatternIonSpecies: IIonSpeciesDetails
    ModificationSpecies: IModificationSpecies

    def SetMatchingScore(self, v: float) -> None: ...
    def SetErrors(
        self, averageMzError: float, heightError: float, s1Error: float, s2Error: float
    ) -> None: ...
    def SetScoreDetail(
        self, monoMassScore: float, intensityPatternScore: float, mzSpacingScore: float
    ) -> None: ...

class TargetFormulaTracker(ITargetFormulaTracker):  # Class
    def __init__(self) -> None: ...
