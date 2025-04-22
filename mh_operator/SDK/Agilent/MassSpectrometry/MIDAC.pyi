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

# Discovered Generic TypeVars:
T = TypeVar("T")
from .DataAnalysis import IConsistency, IRange, IReadOnlyObject, IUnitsAndPrecision

# Stubs for namespace: Agilent.MassSpectrometry.MIDAC

class AbundanceMeasure(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Average: Agilent.MassSpectrometry.MIDAC.AbundanceMeasure = ...  # static # readonly
    Max: Agilent.MassSpectrometry.MIDAC.AbundanceMeasure = ...  # static # readonly
    Sum: Agilent.MassSpectrometry.MIDAC.AbundanceMeasure = ...  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.AbundanceMeasure = (
        ...
    )  # static # readonly

class ApplicableFilters(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AcqTimeRange: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    CompensationField: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    DispersionField: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    DriftTimeRange: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    FragmentationClass: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    FragmentationEnergy: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    FragmentationOpMode: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    FragmentorVoltage: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    IonPolarity: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    IonizationMode: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    MsLevel: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = ...  # static # readonly
    MsScanType: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    MzExclusionRange: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    MzInclusionRange: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    MzOfInterest: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    ScanSegmentRange: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.ApplicableFilters = (
        ...
    )  # static # readonly

class CenterRange(
    Agilent.MassSpectrometry.MIDAC.Range[T],
    Generic[T],
    System.ICloneable,
    Agilent.MassSpectrometry.MIDAC.IRange[T],
    Agilent.MassSpectrometry.MIDAC.ICenterRange[T],
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, zeroWidthValue: T) -> None: ...
    @overload
    def __init__(
        self,
        center: T,
        min: T,
        max: T,
        units: Agilent.MassSpectrometry.MIDAC.MidacUnits,
    ) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.MIDAC.CenterRange) -> None: ...

class ChromatogramType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    BasePeak: Agilent.MassSpectrometry.MIDAC.ChromatogramType = ...  # static # readonly
    ExtractedCompound: Agilent.MassSpectrometry.MIDAC.ChromatogramType = (
        ...
    )  # static # readonly
    ExtractedIon: Agilent.MassSpectrometry.MIDAC.ChromatogramType = (
        ...
    )  # static # readonly
    ExtractedWavelength: Agilent.MassSpectrometry.MIDAC.ChromatogramType = (
        ...
    )  # static # readonly
    InstrumentParameter: Agilent.MassSpectrometry.MIDAC.ChromatogramType = (
        ...
    )  # static # readonly
    MultipleReactionMode: Agilent.MassSpectrometry.MIDAC.ChromatogramType = (
        ...
    )  # static # readonly
    NeutralLoss: Agilent.MassSpectrometry.MIDAC.ChromatogramType = (
        ...
    )  # static # readonly
    SelectedIonMonitoring: Agilent.MassSpectrometry.MIDAC.ChromatogramType = (
        ...
    )  # static # readonly
    Signal: Agilent.MassSpectrometry.MIDAC.ChromatogramType = ...  # static # readonly
    TotalCompound: Agilent.MassSpectrometry.MIDAC.ChromatogramType = (
        ...
    )  # static # readonly
    TotalIon: Agilent.MassSpectrometry.MIDAC.ChromatogramType = ...  # static # readonly
    TotalWavelength: Agilent.MassSpectrometry.MIDAC.ChromatogramType = (
        ...
    )  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.ChromatogramType = (
        ...
    )  # static # readonly

class DevType(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    ALS: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    AnalogDigitalConverter: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    BinaryPump: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    CANValves: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    CE: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    CTC: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    CapillaryPump: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    ChipCube: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    ColumnCompCluster: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    CompactLC1220DAD: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    CompactLC1220GradPump: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    CompactLC1220IsoPump: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    CompactLC1220Sampler: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    CompactLC1220VWD: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    CompactLCColumnOven: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    CompactLCGradPump: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    CompactLCIsoPump: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    CompactLCSampler: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    CompactLCVWD: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    DiodeArrayDetector: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    ElectronCaptureDetector: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    EvaporativeLightScatteringDetector: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    FlameIonizationDetector: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    FlexCube: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    FluorescenceDetector: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    GCDetector: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    HDR: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    IonTrap: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    IsocraticPump: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    LowFlowPump: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    MicroWellPlateSampler: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    Mixed: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    MultiWavelengthDetector: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    NanoPump: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    PumpValveCluster: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    Quadrupole: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    QuadrupoleTimeOfFlight: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    QuaternaryPump: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    RefractiveIndexDetector: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    SFC: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    TandemQuadrupole: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    ThermalConductivityDetector: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    ThermostattedColumnCompartment: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    TimeOfFlight: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    UIB2: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    Unknown: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly
    VariableWavelengthDetector: Agilent.MassSpectrometry.MIDAC.DevType = (
        ...
    )  # static # readonly
    WellPlateSampler: Agilent.MassSpectrometry.MIDAC.DevType = ...  # static # readonly

class DoubleCwRange(
    Agilent.MassSpectrometry.MIDAC.IDoubleRange,
    Agilent.MassSpectrometry.MIDAC.IRange[float],
    System.ICloneable,
    Agilent.MassSpectrometry.MIDAC.ICenterRange[float],
    Agilent.MassSpectrometry.MIDAC.IDoubleCenterRange,
    Agilent.MassSpectrometry.MIDAC.CenterRange[float],
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, center: float) -> None: ...
    @overload
    def __init__(self, center: float, min: float, max: float) -> None: ...
    @overload
    def __init__(
        self,
        center: float,
        min: float,
        max: float,
        units: Agilent.MassSpectrometry.MIDAC.MidacUnits,
    ) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.MIDAC.DoubleCwRange) -> None: ...

class DoubleRange(
    Agilent.MassSpectrometry.MIDAC.IRange[float],
    IRange,
    IReadOnlyObject,
    IConsistency,
    Agilent.MassSpectrometry.MIDAC.Range[float],
    IUnitsAndPrecision,
    System.ICloneable,
    Agilent.MassSpectrometry.MIDAC.IDoubleRange,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, zeroWidthValue: float) -> None: ...
    @overload
    def __init__(self, min: float, max: float) -> None: ...
    @overload
    def __init__(
        self, min: float, max: float, units: Agilent.MassSpectrometry.MIDAC.MidacUnits
    ) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.MIDAC.DoubleRange) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.MIDAC.IDoubleRange) -> None: ...
    @staticmethod
    def EqualRanges(
        rng1: Agilent.MassSpectrometry.MIDAC.IDoubleRange,
        rng2: Agilent.MassSpectrometry.MIDAC.IDoubleRange,
    ) -> bool: ...
    @staticmethod
    def EqualRangeArrays(
        da1: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange],
        da2: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange],
    ) -> bool: ...
    @staticmethod
    def IsNullOrEmpty(range: Agilent.MassSpectrometry.MIDAC.IDoubleRange) -> bool: ...

class FragmentationClass(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    HighEnergy: Agilent.MassSpectrometry.MIDAC.FragmentationClass = (
        ...
    )  # static # readonly
    LowEnergy: Agilent.MassSpectrometry.MIDAC.FragmentationClass = (
        ...
    )  # static # readonly
    Mixed: Agilent.MassSpectrometry.MIDAC.FragmentationClass = ...  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.FragmentationClass = (
        ...
    )  # static # readonly

class FragmentationOpMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    HiLoFrag: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode = (
        ...
    )  # static # readonly
    NonSelective: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode = (
        ...
    )  # static # readonly
    Selective: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode = (
        ...
    )  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode = (
        ...
    )  # static # readonly

class ICenterRange(
    Agilent.MassSpectrometry.MIDAC.IRange[T], System.ICloneable
):  # Interface
    Width: T  # readonly
    WidthPct: T  # readonly
    WidthPpm: T  # readonly

    def SetCenterWidthPpm(self, center: T, widthPpm: T) -> None: ...
    def SetCenterDeltas(self, center: T, deltaLow: T, deltaHigh: T) -> None: ...
    def GetHalfWidths(self, lower: T, upper: T) -> None: ...
    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.ICenterRange: ...
    def SetCenterWidthPct(self, center: T, widthPct: T) -> None: ...
    def SetCenterWidth(self, center: T, width: T) -> None: ...

class IDoubleCenterRange(
    Agilent.MassSpectrometry.MIDAC.ICenterRange[float],
    Agilent.MassSpectrometry.MIDAC.IRange[float],
    System.ICloneable,
    Agilent.MassSpectrometry.MIDAC.IDoubleRange,
):  # Interface
    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IDoubleCenterRange: ...

class IDoubleRange(
    Agilent.MassSpectrometry.MIDAC.IRange[float], System.ICloneable
):  # Interface
    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IDoubleRange: ...

class IIntRange(
    Agilent.MassSpectrometry.MIDAC.IRange[int], System.ICloneable
):  # Interface
    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IIntRange: ...

class IMidacChromDataMs(object):  # Interface
    ChromatogramType: Agilent.MassSpectrometry.MIDAC.ChromatogramType  # readonly
    CompensationFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    DispersionFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    DriftTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]  # readonly
    FragmentationClass: Agilent.MassSpectrometry.MIDAC.FragmentationClass  # readonly
    FragmentationEnergyRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    FragmentationOpMode: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode  # readonly
    FragmentorVoltageRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    IonPolarity: Agilent.MassSpectrometry.MIDAC.Polarity  # readonly
    IonizationMode: Agilent.MassSpectrometry.MIDAC.Ionization  # readonly
    IsCycleSummed: bool  # readonly
    MsLevel: Agilent.MassSpectrometry.MIDAC.MsLevel  # readonly
    MzExclusionRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]  # readonly
    MzInclusionRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]  # readonly
    MzOfInterestRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]  # readonly
    ScanSegmentRange: Agilent.MassSpectrometry.MIDAC.IIntRange  # readonly
    XArray: List[float]  # readonly
    XUnit: Agilent.MassSpectrometry.MIDAC.MidacUnits  # readonly
    YArray: List[float]  # readonly

class IMidacDeviceInfo(object):  # Interface
    DeviceName: str  # readonly
    DeviceType: Agilent.MassSpectrometry.MIDAC.DevType  # readonly
    OrdinalNumber: int  # readonly

    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IMidacDeviceInfo: ...

class IMidacFileInfo(object):  # Interface
    AcquisitionDate: System.DateTime  # readonly
    AcquisitionIsComplete: bool  # readonly
    AcquisitionSofwareVersion: str  # readonly
    FilePath: str  # readonly
    FileUnitConverter: Agilent.MassSpectrometry.MIDAC.IMidacUnitConverter  # readonly
    HasHiLoFragData: bool  # readonly
    InstrumentName: str  # readonly
    MaxAcqTime: float  # readonly
    MaxFlightTimeBin: int  # readonly
    MaxNonTfsMsPerFrame: int  # readonly
    NumFrames: int  # readonly
    TfsMsDetails: Agilent.MassSpectrometry.MIDAC.IMidacMsDetailsSpec  # readonly

    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IMidacFileInfo: ...

class IMidacFrameInfo(object):  # Interface
    AbundRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    AcqTimeRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    DriftBinRange: Agilent.MassSpectrometry.MIDAC.IIntRange  # readonly
    DriftField: float  # readonly
    DriftPressure: float  # readonly
    DriftTemperature: float  # readonly
    DriftTimeRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    FileInfo: Agilent.MassSpectrometry.MIDAC.IMidacFileInfo  # readonly
    FrameNumRange: Agilent.MassSpectrometry.MIDAC.IIntRange  # readonly
    FrameUnitConverter: Agilent.MassSpectrometry.MIDAC.IMidacUnitConverter  # readonly
    MzRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    NumTransients: int  # readonly
    SpectrumDetails: Agilent.MassSpectrometry.MIDAC.IMidacMsDetailsSpec  # readonly
    Tic: float  # readonly
    TimeSegmentId: int  # readonly
    TofBinRange: Agilent.MassSpectrometry.MIDAC.IIntRange  # readonly

    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IMidacFrameInfo: ...

class IMidacMsDetails(object):  # Interface
    AcqTimeRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    AcqTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    CompensationFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DispersionFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DriftTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    FragmentationClass: Agilent.MassSpectrometry.MIDAC.FragmentationClass
    FragmentationEnergyRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    FragmentationOpMode: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode
    FragmentorVoltageRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    IonPolarity: Agilent.MassSpectrometry.MIDAC.Polarity
    IonizationMode: Agilent.MassSpectrometry.MIDAC.Ionization
    MsLevel: Agilent.MassSpectrometry.MIDAC.MsLevel
    MsScanType: Agilent.MassSpectrometry.MIDAC.MsScanType
    MsStorageMode: Agilent.MassSpectrometry.MIDAC.MsStorageMode
    MzExclusionRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    MzInclusionRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    MzOfInterestRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    ScanSegmentRange: Agilent.MassSpectrometry.MIDAC.IIntRange

    def Clear(self) -> None: ...
    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IMidacMsDetails: ...

class IMidacMsDetailsChrom(object):  # Interface
    AcqTimeRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    CompensationFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DispersionFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DriftTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    FragmentationClass: Agilent.MassSpectrometry.MIDAC.FragmentationClass
    FragmentationEnergyRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    FragmentationOpMode: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode
    FragmentorVoltageRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    IonPolarity: Agilent.MassSpectrometry.MIDAC.Polarity
    IonizationMode: Agilent.MassSpectrometry.MIDAC.Ionization
    MsLevel: Agilent.MassSpectrometry.MIDAC.MsLevel
    MsScanType: Agilent.MassSpectrometry.MIDAC.MsScanType
    MsStorageMode: Agilent.MassSpectrometry.MIDAC.MsStorageMode
    MzExclusionRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    MzInclusionRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    MzOfInterestRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    ScanSegmentRange: Agilent.MassSpectrometry.MIDAC.IIntRange

    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IMidacMsDetailsChrom: ...

class IMidacMsDetailsSpec(object):  # Interface
    AbundanceLimit: float
    AcqTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    CompensationFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DispersionFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DriftTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    FragmentationClass: Agilent.MassSpectrometry.MIDAC.FragmentationClass
    FragmentationEnergyRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    FragmentationOpMode: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode
    FragmentorVoltageRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    IonPolarity: Agilent.MassSpectrometry.MIDAC.Polarity
    IonizationMode: Agilent.MassSpectrometry.MIDAC.Ionization
    MsLevel: Agilent.MassSpectrometry.MIDAC.MsLevel
    MsScanType: Agilent.MassSpectrometry.MIDAC.MsScanType
    MsStorageMode: Agilent.MassSpectrometry.MIDAC.MsStorageMode
    MzOfInterestRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    TofBinWidth: float

    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IMidacMsDetailsSpec: ...

class IMidacMsFilters(object):  # Interface
    AcqTimeRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    AcqTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    ApplicableFilters: Agilent.MassSpectrometry.MIDAC.ApplicableFilters
    CompensationFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DispersionFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DriftTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    FragmentationClass: Agilent.MassSpectrometry.MIDAC.FragmentationClass
    FragmentationEnergyRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    FragmentationOpMode: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode
    FragmentorVoltageRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    IonPolarity: Agilent.MassSpectrometry.MIDAC.Polarity
    IonizationMode: Agilent.MassSpectrometry.MIDAC.Ionization
    MsLevel: Agilent.MassSpectrometry.MIDAC.MsLevel
    MsScanType: Agilent.MassSpectrometry.MIDAC.MsScanType
    MsStorageMode: Agilent.MassSpectrometry.MIDAC.MsStorageMode
    MzExclusionRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    MzInclusionRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    MzOfInterestRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    ScanSegmentRange: Agilent.MassSpectrometry.MIDAC.IIntRange

    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IMidacMsFilters: ...

class IMidacMsFiltersChrom(object):  # Interface
    AcqTimeRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    ApplicableFilters: Agilent.MassSpectrometry.MIDAC.ApplicableFilters
    CompensationFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DispersionFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DriftTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    FragmentationClass: Agilent.MassSpectrometry.MIDAC.FragmentationClass
    FragmentationEnergyRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    FragmentationOpMode: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode
    FragmentorVoltageRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    IonPolarity: Agilent.MassSpectrometry.MIDAC.Polarity
    IonizationMode: Agilent.MassSpectrometry.MIDAC.Ionization
    MsLevel: Agilent.MassSpectrometry.MIDAC.MsLevel
    MsScanType: Agilent.MassSpectrometry.MIDAC.MsScanType
    MsStorageMode: Agilent.MassSpectrometry.MIDAC.MsStorageMode
    MzExclusionRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    MzInclusionRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    MzOfInterestRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    ScanSegmentRange: Agilent.MassSpectrometry.MIDAC.IIntRange

    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IMidacMsFiltersChrom: ...

class IMidacMsFiltersSpec(object):  # Interface
    AcqTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    ApplicableFilters: Agilent.MassSpectrometry.MIDAC.ApplicableFilters
    CompensationFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DispersionFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    DriftTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]
    FragmentationClass: Agilent.MassSpectrometry.MIDAC.FragmentationClass
    FragmentationEnergyRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    FragmentationOpMode: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode
    FragmentorVoltageRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange
    IonPolarity: Agilent.MassSpectrometry.MIDAC.Polarity
    IonizationMode: Agilent.MassSpectrometry.MIDAC.Ionization
    MsLevel: Agilent.MassSpectrometry.MIDAC.MsLevel
    MsScanType: Agilent.MassSpectrometry.MIDAC.MsScanType
    MsStorageMode: Agilent.MassSpectrometry.MIDAC.MsStorageMode
    MzOfInterestRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]

    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IMidacMsFiltersSpec: ...

class IMidacPeakFilters(object):  # Interface
    AbsoluteThreshold: float
    MaxNumPeaks: int
    RelativeThresholdPct: float

class IMidacSpecData(object):  # Interface
    AcquiredTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]  # readonly
    DeviceInfo: Agilent.MassSpectrometry.MIDAC.IMidacDeviceInfo  # readonly
    IsAverage: bool  # readonly
    MaxProfilePoints: int  # readonly
    NonZeroPoints: int  # readonly
    SpectrumCount: int  # readonly
    SpectrumFormat: Agilent.MassSpectrometry.MIDAC.MidacSpecFormat  # readonly
    SpectrumType: Agilent.MassSpectrometry.MIDAC.MidacSpecType  # readonly
    XArray: List[float]  # readonly
    XSamplingPeriod: float  # readonly
    XUnit: Agilent.MassSpectrometry.MIDAC.MidacUnits  # readonly
    YArray: List[float]  # readonly

class IMidacSpecDataMs(Agilent.MassSpectrometry.MIDAC.IMidacSpecData):  # Interface
    AbundanceLimit: float  # readonly
    CompensationFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    DispersionFieldRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    DriftTimeRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]  # readonly
    FragmentationClass: Agilent.MassSpectrometry.MIDAC.FragmentationClass  # readonly
    FragmentationEnergyRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    FragmentationOpMode: Agilent.MassSpectrometry.MIDAC.FragmentationOpMode  # readonly
    FragmentorVoltageRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    IonPolarity: Agilent.MassSpectrometry.MIDAC.Polarity  # readonly
    IonizationMode: Agilent.MassSpectrometry.MIDAC.Ionization  # readonly
    MsLevel: Agilent.MassSpectrometry.MIDAC.MsLevel  # readonly
    MsScanType: Agilent.MassSpectrometry.MIDAC.MsScanType  # readonly
    MsStorageMode: Agilent.MassSpectrometry.MIDAC.MsStorageMode  # readonly
    MzOfInterestRanges: List[Agilent.MassSpectrometry.MIDAC.IDoubleRange]  # readonly
    ParentScanIdArray: List[int]  # readonly
    ScanId: int  # readonly

class IMidacUnitConverter(object):  # Interface
    AcqTimeRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange  # readonly
    DriftBinWidth: float  # readonly
    TofBinWidth: float  # readonly
    TofMassCalA: float  # readonly
    TofMassCalTo: float  # readonly

    def SupportsConversion(
        self,
        oldUnits: Agilent.MassSpectrometry.MIDAC.MidacUnits,
        newUnits: Agilent.MassSpectrometry.MIDAC.MidacUnits,
    ) -> bool: ...
    def TofMassCalPolynomial(
        self, coefficients: List[float], tMin: float, tMax: float
    ) -> None: ...
    @overload
    def Convert(
        self,
        oldUnits: Agilent.MassSpectrometry.MIDAC.MidacUnits,
        newUnits: Agilent.MassSpectrometry.MIDAC.MidacUnits,
        value_: float,
    ) -> bool: ...
    @overload
    def Convert(
        self,
        oldUnits: Agilent.MassSpectrometry.MIDAC.MidacUnits,
        newUnits: Agilent.MassSpectrometry.MIDAC.MidacUnits,
        doubleArray: List[float],
    ) -> bool: ...
    @overload
    def Convert(
        self,
        newUnits: Agilent.MassSpectrometry.MIDAC.MidacUnits,
        doubleRange: Agilent.MassSpectrometry.MIDAC.IDoubleRange,
    ) -> bool: ...
    def Equals(
        self, other: Agilent.MassSpectrometry.MIDAC.IMidacUnitConverter
    ) -> bool: ...

class IRange(System.ICloneable):  # Interface
    Center: float  # readonly
    IsEmpty: bool  # readonly
    IsSymmetric: bool  # readonly
    IsZeroWidth: bool  # readonly
    Max: T  # readonly
    Min: T  # readonly
    Units: Agilent.MassSpectrometry.MIDAC.MidacUnits

    def Equals(self, other: Agilent.MassSpectrometry.MIDAC.IRange) -> bool: ...
    @overload
    def Contains(self, value_: T) -> bool: ...
    @overload
    def Contains(self, otherRange: Agilent.MassSpectrometry.MIDAC.IRange) -> bool: ...
    def SetMinMax(self, min: T, max: T) -> None: ...
    def ConstrainTo(
        self, constraintRange: Agilent.MassSpectrometry.MIDAC.IRange
    ) -> None: ...
    def Clear(self) -> None: ...
    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.IRange: ...
    def ToString(self) -> str: ...

class IntRange(
    System.ICloneable,
    Agilent.MassSpectrometry.MIDAC.IIntRange,
    Agilent.MassSpectrometry.MIDAC.Range[int],
    Agilent.MassSpectrometry.MIDAC.IRange[int],
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, zeroWidthValue: int) -> None: ...
    @overload
    def __init__(self, min: int, max: int) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.MIDAC.IntRange) -> None: ...
    @staticmethod
    def EqualRanges(
        rng1: Agilent.MassSpectrometry.MIDAC.IIntRange,
        rng2: Agilent.MassSpectrometry.MIDAC.IIntRange,
    ) -> bool: ...
    @staticmethod
    def IsNullOrEmpty(range: Agilent.MassSpectrometry.MIDAC.IIntRange) -> bool: ...

class Ionization(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Apci: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    Appi: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    CI: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    EI: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    Esi: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    ICP: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    JetStream: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    Maldi: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    Mixed: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    MsChip: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    NanoEsi: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.Ionization = ...  # static # readonly

class MidacNumericPrecisionLibrary:  # Class
    @staticmethod
    def FormatDoubleScientific(value_: float, digits: int) -> str: ...
    @staticmethod
    def FormatFloat(value_: float, digitsAfterDecimal: int) -> str: ...
    @staticmethod
    def UnitAbbrevIsSuffix(
        units: Agilent.MassSpectrometry.MIDAC.MidacUnits, unitStr: str
    ) -> bool: ...
    @staticmethod
    def DigitsAfterDecimal(units: Agilent.MassSpectrometry.MIDAC.MidacUnits) -> int: ...
    @staticmethod
    def FormatDouble(value_: float, digitsAfterDecimal: int) -> str: ...
    @staticmethod
    def SetToDefaults() -> None: ...
    @staticmethod
    def SetDigitsAfterDecimal(
        units: Agilent.MassSpectrometry.MIDAC.MidacUnits, value_: int
    ) -> None: ...

class MidacSpecFormat(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Metadata: Agilent.MassSpectrometry.MIDAC.MidacSpecFormat = ...  # static # readonly
    Peak: Agilent.MassSpectrometry.MIDAC.MidacSpecFormat = ...  # static # readonly
    Profile: Agilent.MassSpectrometry.MIDAC.MidacSpecFormat = ...  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.MidacSpecFormat = (
        ...
    )  # static # readonly
    ZeroBounded: Agilent.MassSpectrometry.MIDAC.MidacSpecFormat = (
        ...
    )  # static # readonly
    ZeroTrimmed: Agilent.MassSpectrometry.MIDAC.MidacSpecFormat = (
        ...
    )  # static # readonly

class MidacSpecType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DriftSpectrum: Agilent.MassSpectrometry.MIDAC.MidacSpecType = (
        ...
    )  # static # readonly
    MassSpectrum: Agilent.MassSpectrometry.MIDAC.MidacSpecType = (
        ...
    )  # static # readonly
    MzSpectrum: Agilent.MassSpectrometry.MIDAC.MidacSpecType = ...  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.MidacSpecType = ...  # static # readonly
    UvVisSpecrum: Agilent.MassSpectrometry.MIDAC.MidacSpecType = (
        ...
    )  # static # readonly

class MidacUnits(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AcqTimeResolution: Agilent.MassSpectrometry.MIDAC.MidacUnits = (
        ...
    )  # static # readonly
    Centigrade: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    CorrectionFactor: Agilent.MassSpectrometry.MIDAC.MidacUnits = (
        ...
    )  # static # readonly
    Counts: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    DriftBinIndex: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    DriftResolution: Agilent.MassSpectrometry.MIDAC.MidacUnits = (
        ...
    )  # static # readonly
    FlightTimeBinIndex: Agilent.MassSpectrometry.MIDAC.MidacUnits = (
        ...
    )  # static # readonly
    FrameNumber: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Mass: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    MassResolution: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    MassToCharge: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Milliseconds: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Minutes: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Mobility: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Nanoseconds: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Noise: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Percent: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Score: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Seconds: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    SignalToNoise: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    SquareAngstrom: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Torr: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    Volts: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly
    VoltsPerCm: Agilent.MassSpectrometry.MIDAC.MidacUnits = ...  # static # readonly

class MsLevel(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    All: Agilent.MassSpectrometry.MIDAC.MsLevel = ...  # static # readonly
    MS: Agilent.MassSpectrometry.MIDAC.MsLevel = ...  # static # readonly
    MSMS: Agilent.MassSpectrometry.MIDAC.MsLevel = ...  # static # readonly

class MsScanType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    All: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly
    AllMS: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly
    AllMSN: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly
    HighResolutionScan: Agilent.MassSpectrometry.MIDAC.MsScanType = (
        ...
    )  # static # readonly
    MultipleReaction: Agilent.MassSpectrometry.MIDAC.MsScanType = (
        ...
    )  # static # readonly
    NeutralGain: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly
    NeutralLoss: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly
    PrecursorIon: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly
    ProductIon: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly
    Scan: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly
    SelectedIon: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly
    TotalIon: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.MsScanType = ...  # static # readonly

class MsStorageMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Mixed: Agilent.MassSpectrometry.MIDAC.MsStorageMode = ...  # static # readonly
    PeakDetectedSpectrum: Agilent.MassSpectrometry.MIDAC.MsStorageMode = (
        ...
    )  # static # readonly
    ProfileSpectrum: Agilent.MassSpectrometry.MIDAC.MsStorageMode = (
        ...
    )  # static # readonly
    Unspecified: Agilent.MassSpectrometry.MIDAC.MsStorageMode = ...  # static # readonly

class Polarity(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Mixed: Agilent.MassSpectrometry.MIDAC.Polarity = ...  # static # readonly
    Negative: Agilent.MassSpectrometry.MIDAC.Polarity = ...  # static # readonly
    Positive: Agilent.MassSpectrometry.MIDAC.Polarity = ...  # static # readonly
    Unassigned: Agilent.MassSpectrometry.MIDAC.Polarity = ...  # static # readonly

class Range(
    Generic[T], System.ICloneable, Agilent.MassSpectrometry.MIDAC.IRange[T]
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, zeroWidthValue: T) -> None: ...
    @overload
    def __init__(self, min: T, max: T) -> None: ...
    @overload
    def __init__(
        self, min: T, max: T, units: Agilent.MassSpectrometry.MIDAC.MidacUnits
    ) -> None: ...
    @overload
    def __init__(self, src: Agilent.MassSpectrometry.MIDAC.Range) -> None: ...
    def Equals(self, obj: Any) -> bool: ...
    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    def Clone(self) -> Agilent.MassSpectrometry.MIDAC.Range: ...
