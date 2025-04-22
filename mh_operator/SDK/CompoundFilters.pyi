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
    IIsotopeClusterBase,
    IModificationUnit,
)
from .Agilent.MassSpectrometry.DataAnalysis.MassHunter import (
    CompoundFilterParameters,
    FilterStatus,
)
from .BasicTypes import GenericCompound, MfeCompound, Protein
from .Mathematics import RangeDouble, RangeInt

# Stubs for namespace: CompoundFilters

class AbsoluteAbundanceFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.AbsoluteAbundanceFilter.Parameter
    ) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_minAbundace: float

        FilterStatus: FilterStatus
        Name: str  # readonly

        @overload
        def Equals(self, obj: Any) -> bool: ...
        @overload
        def Equals(
            self, other: CompoundFilters.AbsoluteAbundanceFilter.Parameter
        ) -> bool: ...
        def GetHashCode(self) -> int: ...
        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def Clone(self) -> CompoundFilters.AbsoluteAbundanceFilter.Parameter: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class AbundanceFilter:  # Class
    def __init__(self, p: CompoundFilters.AbundanceFilter.Parameter) -> None: ...
    def Filter(
        self, inputCompounds: List[Any]
    ) -> List[CompoundFilters.IFilterable]: ...

    # Nested Types

    class Parameter:  # Class
        def __init__(self) -> None: ...

        m_maxCount: int
        m_minAbsoluteAbundance: float
        m_minRelativeAbundance: float
        m_status: FilterStatus
        m_useHeight: bool

        Name: str  # readonly

        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...
        def FromOldFormat(self, element: System.Xml.XmlElement) -> None: ...

class ChargeStateFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.ChargeStateFilter.Parameter
    ) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_fullRangeRequired: bool
        m_maxChargeCount: int
        m_minChargeCount: int

        FilterStatus: FilterStatus
        Name: str  # readonly

        @overload
        def Equals(self, obj: Any) -> bool: ...
        @overload
        def Equals(
            self, other: CompoundFilters.ChargeStateFilter.Parameter
        ) -> bool: ...
        def GetHashCode(self) -> int: ...
        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def Clone(self) -> CompoundFilters.ChargeStateFilter.Parameter: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class CommutableFilter:  # Class
    def __init__(self, parmeter: CompoundFilters.IFilterParameter) -> None: ...

    IsApplied: bool  # readonly

    def Pass(self, c: CompoundFilters.IFilterable) -> bool: ...

class CompositionFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.CompositionFilter.Parameter
    ) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_heightVariation: float

        ElementCountRanges: Dict[str, RangeInt]
        FilterStatus: FilterStatus
        MinPeakNeeded: int  # readonly
        Name: str  # readonly

        @overload
        def Equals(self, obj: Any) -> bool: ...
        @overload
        def Equals(
            self, other: CompoundFilters.CompositionFilter.Parameter
        ) -> bool: ...
        def GetHashCode(self) -> int: ...
        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def Clone(self) -> CompoundFilters.CompositionFilter.Parameter: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class CompoundFilterXml:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def FromXml(
        siblings: System.Xml.XmlNodeList, data: CompoundFilterParameters
    ) -> None: ...
    @staticmethod
    def ToXml(
        document: System.Xml.XmlDocument, data: CompoundFilterParameters
    ) -> System.Xml.XmlElement: ...

class CompoundFilters:  # Class
    def __init__(
        self, parameters: CompoundFilters.ICompoundFilterParameters
    ) -> None: ...

    LargeMZ: float  # static # readonly
    LargeRT: float  # static # readonly

    def FilterCompounds(self, compounds: List[MfeCompound]) -> List[MfeCompound]: ...

class GenericCompoundFilters:  # Class
    def __init__(
        self, parameters: CompoundFilters.IGenericCompoundFilterParameters
    ) -> None: ...
    def FilterCompounds(
        self, compounds: List[GenericCompound]
    ) -> List[GenericCompound]: ...

class ICompoundFilterParameters(
    CompoundFilters.IGenericCompoundFilterParameters
):  # Interface
    ChargeStateParameters: CompoundFilters.ChargeStateFilter.Parameter  # readonly
    IsotopePatternParameters: CompoundFilters.IsotopePatternFilter.Parameter  # readonly
    MinIonCountParamters: CompoundFilters.MinIonCountFilter.Parameter  # readonly
    NeutralModificationParameters: (
        CompoundFilters.NeutralModificationFilter.Parameter
    )  # readonly
    QualityScoreParameters: CompoundFilters.QualityScoreFilter.Parameter  # readonly
    TimePeakWidthParameters: CompoundFilters.PeakRtWidthFilter.Parameter  # readonly
    UunknownMassParameters: CompoundFilters.UnknownMassFilter.Parameter  # readonly

class IFilterParameter(object):  # Interface
    FilterStatus: FilterStatus  # readonly

class IFilterable(object):  # Interface
    Abundance: float  # readonly
    Height: float  # readonly
    Mass: float  # readonly
    QualityScore: float  # readonly
    RetentionTime: float  # readonly
    RetentionTimePeakWidth: float  # readonly

class IFilterableMfe(CompoundFilters.IFilterable):  # Interface
    IonCount: int  # readonly
    IsotopeClusters: Sequence[IIsotopeClusterBase]  # readonly

    def GetZStates(self) -> System.Collections.Generic.HashSet[int]: ...

class IGenericCompoundFilterParameters(object):  # Interface
    AbundanceParameters: CompoundFilters.AbundanceFilter.Parameter  # readonly
    LocationRangeParameters: CompoundFilters.LocationRangeFilter.Parameter  # readonly
    MassDefectParameters: CompoundFilters.MassDefectFilter.Parameter  # readonly
    SpecialMassParameters: CompoundFilters.SpecialMassFilter.Parameter  # readonly
    SpecialTimeParameters: CompoundFilters.SpecialTimeFilter.Parameter  # readonly

class IProteinFilterParameters(
    CompoundFilters.IGenericCompoundFilterParameters
):  # Interface
    QualityScoreParameters: CompoundFilters.QualityScoreFilter.Parameter  # readonly
    TimePeakWidthParameters: CompoundFilters.PeakRtWidthFilter.Parameter  # readonly

class IsotopePatternFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.IsotopePatternFilter.Parameter
    ) -> None: ...
    def Score(self, compound: MfeCompound) -> float: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_formula: str
        m_massAccuracyCoefficients: List[float]
        m_pattern: List[float]
        m_patternUncertainty: List[float]
        m_relativeIntensityUncertainty: float

        FilterStatus: FilterStatus  # readonly
        Name: str  # readonly
        Status: FilterStatus

        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...
        def CheckIntegraty(self) -> bool: ...

class LocationRangeFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.LocationRangeFilter.Parameter
    ) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_massRange: RangeDouble
        m_rtRange: RangeDouble

        FilterStatus: FilterStatus
        Name: str  # readonly

        @overload
        def Equals(self, obj: Any) -> bool: ...
        @overload
        def Equals(
            self, other: CompoundFilters.LocationRangeFilter.Parameter
        ) -> bool: ...
        def GetHashCode(self) -> int: ...
        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def Clone(self) -> CompoundFilters.LocationRangeFilter.Parameter: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class MassDefectFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.MassDefectFilter.Parameter
    ) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_intercept: float
        m_peptideLike: bool
        m_slope: float
        m_toleranceInterceptForNegativeDeviation: float
        m_toleranceInterceptForPositiveDeviation: float
        m_toleranceSlopeForNegativeDeviation: float
        m_toleranceSlopeForPositiveDeviation: float

        FilterStatus: FilterStatus
        Name: str  # readonly

        @overload
        def Equals(self, obj: Any) -> bool: ...
        @overload
        def Equals(self, other: CompoundFilters.MassDefectFilter.Parameter) -> bool: ...
        def GetHashCode(self) -> int: ...
        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def Clone(self) -> CompoundFilters.MassDefectFilter.Parameter: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class MinIonCountFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(self, p: CompoundFilters.MinIonCountFilter.Parameter) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_minIonCount: int

        FilterStatus: FilterStatus
        Name: str  # readonly

        @overload
        def Equals(self, obj: Any) -> bool: ...
        @overload
        def Equals(
            self, other: CompoundFilters.MinIonCountFilter.Parameter
        ) -> bool: ...
        def GetHashCode(self) -> int: ...
        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def Clone(self) -> CompoundFilters.MinIonCountFilter.Parameter: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class NeutralModificationFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.NeutralModificationFilter.Parameter
    ) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_modificationList: System.Collections.Generic.HashSet[IModificationUnit]

        FilterStatus: FilterStatus
        Name: str  # readonly

        @overload
        def Equals(self, obj: Any) -> bool: ...
        @overload
        def Equals(
            self, other: CompoundFilters.NeutralModificationFilter.Parameter
        ) -> bool: ...
        def GetHashCode(self) -> int: ...
        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def Clone(self) -> CompoundFilters.NeutralModificationFilter.Parameter: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class PeakRtWidthFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.PeakRtWidthFilter.Parameter
    ) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_maxWidth: float
        m_minWidth: float

        FilterStatus: FilterStatus

class ProteinFilters:  # Class
    def __init__(
        self, parameters: CompoundFilters.IProteinFilterParameters
    ) -> None: ...
    def FilterProteins(self, compounds: List[Protein]) -> List[Protein]: ...

class QualityScoreFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.QualityScoreFilter.Parameter
    ) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_maxScore: float
        m_minScore: float

        FilterStatus: FilterStatus
        Name: str  # readonly

        @overload
        def Equals(self, obj: Any) -> bool: ...
        @overload
        def Equals(
            self, other: CompoundFilters.QualityScoreFilter.Parameter
        ) -> bool: ...
        def GetHashCode(self) -> int: ...
        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def Clone(self) -> CompoundFilters.QualityScoreFilter.Parameter: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class SpecialMassFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.SpecialMassFilter.Parameter
    ) -> None: ...

    # Nested Types

    class Parameter(
        CompoundFilters.IFilterParameter, CompoundFilters.SpecialValueFilterParameter
    ):  # Class
        def __init__(self) -> None: ...
        def Clone(self) -> CompoundFilters.SpecialMassFilter.Parameter: ...

class SpecialTimeFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(
        self, parameter: CompoundFilters.SpecialTimeFilter.Parameter
    ) -> None: ...

    # Nested Types

    class Parameter(
        CompoundFilters.IFilterParameter, CompoundFilters.SpecialValueFilterParameter
    ):  # Class
        def __init__(self) -> None: ...

class SpecialValueFilterParameter(CompoundFilters.IFilterParameter):  # Class
    m_rangeList: List[RangeDouble]
    m_toleranceCoefficients: List[float]
    m_valueList: Sequence[float]

    FilterStatus: FilterStatus
    Name: str  # readonly

    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(self, other: CompoundFilters.SpecialValueFilterParameter) -> bool: ...
    @staticmethod
    def RunFilter(
        theValue: float, parameter: CompoundFilters.SpecialValueFilterParameter
    ) -> bool: ...
    def GetHashCode(self) -> int: ...
    def FromXml(self, element: System.Xml.XmlElement) -> None: ...
    def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

class TimeMassFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(self, parameter: CompoundFilters.TimeMassFilter.Parameter) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        m_massToleranceCoefficients: List[float]
        m_timeToleranceCoefficients: List[float]
        m_usage: CompoundFilters.TimeMassFilter.Usage
        m_valueList: List[CompoundFilters.TimeMassFilter.TimeMassData]

        FilterStatus: FilterStatus
        Name: str  # readonly

        @overload
        def Equals(self, obj: Any) -> bool: ...
        @overload
        def Equals(self, other: CompoundFilters.TimeMassFilter.Parameter) -> bool: ...
        def GetHashCode(self) -> int: ...
        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def Clone(self) -> CompoundFilters.TimeMassFilter.Parameter: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...

    class TimeMassData:  # Struct
        def __init__(self, time: float, mass: float) -> None: ...

        Mass: float
        Time: float

        def GetHashCode(self) -> int: ...
        @overload
        def Equals(self, obj: Any) -> bool: ...
        @overload
        def Equals(
            self, other: CompoundFilters.TimeMassFilter.TimeMassData
        ) -> bool: ...

    class Usage(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
        Both: CompoundFilters.TimeMassFilter.Usage = ...  # static # readonly
        MassOnly: CompoundFilters.TimeMassFilter.Usage = ...  # static # readonly
        TimeOnly: CompoundFilters.TimeMassFilter.Usage = ...  # static # readonly

class UnknownMassFilter(CompoundFilters.CommutableFilter):  # Class
    def __init__(self, p: CompoundFilters.UnknownMassFilter.Parameter) -> None: ...

    # Nested Types

    class Parameter(CompoundFilters.IFilterParameter):  # Class
        def __init__(self) -> None: ...

        FilterStatus: FilterStatus
        Name: str  # readonly

        def FromXml(self, element: System.Xml.XmlElement) -> None: ...
        def ToXml(self, doc: System.Xml.XmlDocument) -> System.Xml.XmlElement: ...
