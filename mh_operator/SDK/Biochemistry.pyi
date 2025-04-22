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

from .Agilent.MassSpectrometry.DataAnalysis import MassIsotopeChoice, SpectralPeak
from .IsotopePatternCalculator import (
    IIsotopePattern,
    IsotopePatternCalculatorParameters,
)
from .Mathematics import RangeDouble, RangeInt
from .Mfe import IsotopeCharacter

# Stubs for namespace: Biochemistry

class AminoAcids(Biochemistry.SuperAtomSet):  # Class
    def __init__(self) -> None: ...

class ChargeState:  # Struct
    def __init__(self, z: int, type: Biochemistry.ChargeState.Type) -> None: ...

    ChargeType: Biochemistry.ChargeState.Type
    Z: int

    ChargeCount: int

    def GetIonMass(self, neutralMass: float) -> float: ...
    def MZ2NeutrolMass(self, mz: float) -> float: ...

    # Nested Types

    class Type(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
        Electron: Biochemistry.ChargeState.Type = ...  # static # readonly
        Proton: Biochemistry.ChargeState.Type = ...  # static # readonly
        Unknown: Biochemistry.ChargeState.Type = ...  # static # readonly

class CompositionModel:  # Class
    A2DominatingMass: float  # readonly
    CarbonMassFraction: float  # readonly
    CarbonMassFractionRange: RangeDouble  # readonly

    def CalculateIsotopePattern(self, m0: float) -> List[SpectralPeak]: ...
    def GetIsotopeMassOffset(self, isotopeIndex: int, m0: float) -> float: ...
    def GetIsotopePattern(
        self, m0: float, userParameter: IsotopePatternCalculatorParameters
    ) -> IIsotopePattern: ...
    def AllowsMass(self, mass: float) -> bool: ...
    @staticmethod
    def CreateModel(
        isotopeCharacter: IsotopeCharacter,
    ) -> Biochemistry.CompositionModel: ...
    def GetAverageMassFromLowestMass(self, lowestMass: float) -> float: ...
    def GetCarbonRange(self, mass: float) -> RangeInt: ...
    def GetMaxMissingLeadingPeakAllowrance(self, mass: float) -> int: ...

class CompoundMass:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def PossibleAsIon(mass: float) -> bool: ...
    @staticmethod
    def PossibleAsNeutralLoss(mass: float) -> bool: ...

class Constants:  # Class
    def __init__(self) -> None: ...

    AverageIsotopeMassIncrement: float  # static # readonly
    ElectronMass: float  # static # readonly
    KIonMass: float  # static # readonly
    NaIonMass: float  # static # readonly
    ProtonMass: float  # static # readonly

class DoubleBondEquivalency:  # Class
    def __init__(self) -> None: ...
    def GetValue(self, element: str) -> float: ...

class ElementContentLimits:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def MaxN(compoundMass: float) -> float: ...
    @staticmethod
    def MaxS(compoundMass: float) -> float: ...
    @staticmethod
    def MaxCl(compoundMass: float) -> float: ...
    @staticmethod
    def MinHCount(compoundMass: float) -> int: ...
    @staticmethod
    def MinCCount(compoundMass: float) -> int: ...
    @staticmethod
    def MaxF(compoundMass: float) -> float: ...
    @staticmethod
    def MaxNa(compoundMass: float) -> float: ...
    @staticmethod
    def MaxC(compoundMass: float) -> float: ...
    @staticmethod
    def MaxBr(compoundMass: float) -> float: ...
    @staticmethod
    def MaxO(compoundMass: float) -> float: ...
    @staticmethod
    def MaxH(compoundMass: float) -> float: ...

class ElementMassCalculator:  # Class
    def __init__(self, massChoice: MassIsotopeChoice) -> None: ...
    def GetMass(self, symbol: str) -> float: ...

class ElementPickerControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UserControl,
):  # Class
    def __init__(self) -> None: ...

    Elements: System.Collections.Generic.List[str]

class ElementProperty:  # Class
    AverageMass: int  # readonly
    ElementProperties: Dict[str, Biochemistry.ElementProperty]  # static # readonly
    ImplicitValence: bool  # readonly
    MetalCode: Biochemistry.ElementProperty.MetalStatus  # readonly

    def GetValences(self, z: int) -> List[int]: ...

    # Nested Types

    class MetalStatus(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        Metal: Biochemistry.ElementProperty.MetalStatus = ...  # static # readonly
        Metal2: Biochemistry.ElementProperty.MetalStatus = ...  # static # readonly
        NonMetal: Biochemistry.ElementProperty.MetalStatus = ...  # static # readonly

class EmpiricalConstants:  # Class
    def __init__(self) -> None: ...

    MinCarbonWeightContent: float  # static # readonly
    MinCarbonWeightContentAveragine: float  # static # readonly

class GlycanModel(Biochemistry.CompositionModel):  # Class
    def __init__(self) -> None: ...

    A2DominatingMass: float  # readonly
    CarbonMassFractionRange: RangeDouble  # readonly

    def GetIsotopeMassOffset(self, isotopeIndex: int, m0: float) -> float: ...

class NaturalMolecule(Iterable[Any]):  # Class
    def __init__(self) -> None: ...

    AtomCount: int  # readonly
    CentroidMass: float  # readonly
    DoubleBondEquivalent: float  # readonly
    ElectronCount: int  # readonly
    Formula: str  # readonly
    LowestIsotopeMass: float  # readonly
    LowestIsotopeNominalMass: int  # readonly
    MonoisotopicMass: float  # readonly
    MonoisotopicNominalMass: int  # readonly
    RelativeDoubleBondEquivalent: float  # readonly

    def GetEnumerator(self) -> Iterator[Any]: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(self, another: Biochemistry.NaturalMolecule) -> bool: ...
    @overload
    def Add(self, another: Biochemistry.NaturalMolecule) -> None: ...
    @overload
    def Add(self, another: Biochemistry.NaturalMolecule, count: int) -> None: ...
    def GetAtomCountOf(self, atomicNumber: int) -> int: ...
    def IsSubsetOf(self, potentialParent: Biochemistry.NaturalMolecule) -> bool: ...
    @overload
    def AddElements(self, symbol: str, amount: int) -> None: ...
    @overload
    def AddElements(self, atomicNumber: int, amount: int) -> None: ...
    def GetHashCode(self) -> int: ...
    @staticmethod
    def Parse(formula: str) -> Biochemistry.NaturalMolecule: ...
    def Clone(self) -> Biochemistry.NaturalMolecule: ...

class RadioactiveIsotopes:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def GetMass(symbol: str, nucleonNumber: int, mass: float) -> bool: ...

class Ribonucleotides(Biochemistry.SuperAtomSet):  # Class
    def __init__(self) -> None: ...

class SuperAtomSet:  # Class
    def __init__(self) -> None: ...
    def GetElectronCount(self, symbol: str) -> int: ...
    def Contains(self, symbol: str) -> bool: ...
    def GetMass(self, symbol: str, massChoice: MassIsotopeChoice) -> float: ...
