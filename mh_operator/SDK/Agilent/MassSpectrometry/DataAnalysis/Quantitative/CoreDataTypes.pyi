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

from . import DoubleRange, IntRange, PlotTitles, Transition

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes

class ChromDataBuffer(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IChromSpecData,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IChromDataBuffer,
):  # Class
    @overload
    def __init__(
        self,
        firstCycleNumber: int,
        rt: System.Collections.Generic.List[float],
        cycleNumberRange: IntRange,
    ) -> None: ...
    @overload
    def __init__(
        self, xArray: List[float], yArray: List[float], cycleNumberRange: IntRange
    ) -> None: ...
    @overload
    def __init__(self, xArray: List[float], yArray: List[float]) -> None: ...

    Count: int  # readonly
    HasData: bool  # readonly
    HasGaps: bool  # readonly
    LastCycleNumber: int  # readonly
    NScanLinesForSpectrum: int  # readonly
    XArray: List[float]  # readonly
    YArray: List[float]  # readonly

    def Sort(self) -> None: ...
    @overload
    def AddChromDataSegment(
        self,
        abundances: System.Collections.Generic.List[float],
        startIndex: int,
        endIndex: int,
        startingCycleNumber: int,
    ) -> None: ...
    @overload
    def AddChromDataSegment(
        self,
        abundances: System.Collections.Generic.List[float],
        cycleNumbers: System.Collections.Generic.List[int],
        startIndex: int,
        endIndex: int,
    ) -> None: ...
    @overload
    def AddChromDataSegment(
        self,
        abundances: List[float],
        cycleNumbers: List[int],
        startIndex: int,
        endIndex: int,
    ) -> None: ...
    def AddChromDataSegment_CheckMaxMz(
        self,
        abundances: List[float],
        mzValues: List[float],
        cycleNumbers: List[int],
        startIndex: int,
        endIndex: int,
        maxMz: float,
    ) -> None: ...
    def AddChromDataSegment_CheckMinMz(
        self,
        abundances: List[float],
        mzValues: List[float],
        cycleNumbers: List[int],
        startIndex: int,
        endIndex: int,
        minMz: float,
    ) -> None: ...
    def AddDataSegment(
        self,
        seg: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.ChromDataBuffer,
    ) -> None: ...
    def AddDataPoint(self, abundance: float, cycleNumber: int) -> None: ...
    def AddChromDataSegment_CheckMinMaxMz(
        self,
        abundances: List[float],
        mzValues: List[float],
        cycleNumbers: List[int],
        startIndex: int,
        endIndex: int,
        minMz: float,
        maxMz: float,
    ) -> None: ...

class ChromSpecData(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IChromSpecData
):  # Class
    @overload
    def __init__(self, xArray: List[float], yArray: List[float]) -> None: ...
    @overload
    def __init__(
        self, xArray: List[float], yArray: List[float], hasGaps: bool
    ) -> None: ...
    @overload
    def __init__(
        self, xArray: List[float], yArray: List[float], scanCount: int
    ) -> None: ...
    @overload
    def __init__(
        self,
        xList: System.Collections.Generic.List[float],
        yList: System.Collections.Generic.List[float],
    ) -> None: ...
    @overload
    def __init__(
        self,
        xList: System.Collections.Generic.List[float],
        yList: System.Collections.Generic.List[float],
        scanCount: int,
    ) -> None: ...
    @overload
    def __init__(self, xyData: Dict[float, float]) -> None: ...
    @overload
    def __init__(self, xyData: Dict[float, float], scanCount: int) -> None: ...
    @overload
    def __init__(self) -> None: ...

    Count: int  # readonly
    HasData: bool  # readonly
    HasGaps: bool  # readonly
    NScanLinesForSpectrum: int  # readonly
    XArray: List[float]  # readonly
    YArray: List[float]  # readonly

    def Sort(self) -> None: ...
    def AddDataSegment(
        self,
        moreData: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.ChromSpecData,
    ) -> None: ...

class IChromDataBuffer(object):  # Interface
    def AddDataPoint(self, abundance: float, cycleNumber: int) -> None: ...
    def AddChromDataSegment(
        self,
        abundances: List[float],
        cycleNumbers: List[int],
        startIndex: int,
        endIndex: int,
    ) -> None: ...

class IChromSpecData(object):  # Interface
    Count: int  # readonly
    HasData: bool  # readonly
    HasGaps: bool  # readonly
    NScanLinesForSpectrum: int  # readonly
    XArray: List[float]  # readonly
    YArray: List[float]  # readonly

    def Sort(self) -> None: ...

class IQuantMSScanInfo(object):  # Interface
    AverageScanStep: float  # readonly
    Polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity  # readonly
    ScanTypes: Agilent.MassSpectrometry.DataAnalysis.MSScanType  # readonly

    def GetPolarities(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.IonPolarity
    ]: ...
    def GetMZs(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        selectedMZ: float,
    ) -> System.Collections.Generic.List[float]: ...
    def GetScanTypes(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ]: ...
    def GetPolarity(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> Agilent.MassSpectrometry.DataAnalysis.IonPolarity: ...
    def GetMRMTransitions(
        self,
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...
    def GetSelectedMZs(
        self, scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    ) -> System.Collections.Generic.List[float]: ...
    def GetTransitions(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
    ) -> Dict[float, System.Collections.Generic.List[Transition]]: ...

class QuantChromatogram(
    Agilent.MassSpectrometry.DataAnalysis.IFXArrayStore,
    Agilent.MassSpectrometry.DataAnalysis.IFXStore,
    Agilent.MassSpectrometry.DataAnalysis.IXYStore,
    Agilent.MassSpectrometry.DataAnalysis.IConsistency,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantXYData,
    Agilent.MassSpectrometry.DataAnalysis.IXYData,
    Agilent.MassSpectrometry.DataAnalysis.IFXData,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
    Agilent.MassSpectrometry.DataAnalysis.IUnitsConverter,
    Agilent.MassSpectrometry.DataAnalysis.IChromatogram,
    System.ICloneable,
):  # Class
    def __init__(
        self,
        chromData: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IChromSpecData,
        dataSourcePath: str,
        chromFilter: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom,
    ) -> None: ...

    ChromFilter: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom  # readonly

    @overload
    def InitTitle(
        self,
        titles: PlotTitles,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        dataDirectory: str,
        smoothing: bool,
    ) -> None: ...
    @overload
    def InitTitle(
        self,
        titles: PlotTitles,
        deviceName: str,
        signalName: str,
        signalDescription: str,
        signalRange: DoubleRange,
        referenceRange: DoubleRange,
        dataDirectory: str,
        smoothing: bool,
    ) -> None: ...

class QuantDataSource(
    Agilent.MassSpectrometry.DataAnalysis.IConsistency,
    System.ICloneable,
    Agilent.MassSpectrometry.DataAnalysis.IDataSource,
):  # Class
    def __init__(self) -> None: ...

class QuantDataUnits(
    Agilent.MassSpectrometry.DataAnalysis.IConsistency,
    System.ICloneable,
    Agilent.MassSpectrometry.DataAnalysis.IDataUnits,
):  # Class
    QuantChromUnits: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantDataUnits
    )  # static

class QuantFileInfo(
    System.ICloneable, Agilent.MassSpectrometry.DataAnalysis.IBDAFileInformation
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        dataFileName: str,
        scanFileInfo: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantMSScanFileInfo,
        separationType: Agilent.MassSpectrometry.DataAnalysis.SeparationTechnique,
        msDataPresent: bool,
        nonMsDataPresent: bool,
    ) -> None: ...

class QuantMSChromatogram(
    Agilent.MassSpectrometry.DataAnalysis.IXYStore,
    Agilent.MassSpectrometry.DataAnalysis.IChromatogram,
    Agilent.MassSpectrometry.DataAnalysis.IFXData,
    System.ICloneable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantChromatogram,
    Agilent.MassSpectrometry.DataAnalysis.IXYData,
    Agilent.MassSpectrometry.DataAnalysis.ISpectralChromatogram,
    Agilent.MassSpectrometry.DataAnalysis.IFXStore,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
    Agilent.MassSpectrometry.DataAnalysis.IConsistency,
    Agilent.MassSpectrometry.DataAnalysis.IFXArrayStore,
    Agilent.MassSpectrometry.DataAnalysis.IMSChromatogram,
    Agilent.MassSpectrometry.DataAnalysis.IUnitsConverter,
):  # Class
    def __init__(
        self,
        chromData: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IChromSpecData,
        timeSegments: Agilent.MassSpectrometry.DataAnalysis.RangeCollection,
        dataSourcePath: str,
        chromFilter: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom,
    ) -> None: ...

class QuantMSScanFileInfo(
    Agilent.MassSpectrometry.DataAnalysis.IBDAMSScanFileInformation,
    Iterable[Any],
    System.ICloneable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        polarity: Agilent.MassSpectrometry.DataAnalysis.IonPolarity,
        scanTypeInfo: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantMSScanTypeInfo
        ],
    ) -> None: ...

class QuantMSScanTypeInfo(
    Agilent.MassSpectrometry.DataAnalysis.IBDAMSScanTypeInformation, System.ICloneable
):  # Class
    def __init__(
        self,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        scanInfo: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IQuantMSScanInfo,
    ) -> None: ...

    QuantScanInfo: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IQuantMSScanInfo
    )  # readonly

    def Clone(self) -> Any: ...

class QuantMassSpectrum(
    Agilent.MassSpectrometry.DataAnalysis.IFXData,
    Agilent.MassSpectrometry.DataAnalysis.IXYStore,
    System.ICloneable,
    Agilent.MassSpectrometry.DataAnalysis.ISpectrum,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantSpectrum,
    Agilent.MassSpectrometry.DataAnalysis.IUnitsConverter,
    Agilent.MassSpectrometry.DataAnalysis.IFXStore,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
    Agilent.MassSpectrometry.DataAnalysis.IXYData,
    Agilent.MassSpectrometry.DataAnalysis.IMassSpectrum,
    Agilent.MassSpectrometry.DataAnalysis.IConsistency,
    Agilent.MassSpectrometry.DataAnalysis.IFXArrayStore,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        specData: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IChromSpecData,
        filter: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum,
        dataSourcePath: str,
        isProfileData: bool,
    ) -> None: ...

    ContributingRtRanges: System.Collections.Generic.List[DoubleRange]  # readonly

    @overload
    def InitTitle(self, titles: PlotTitles, dataDirectory: str) -> None: ...
    @overload
    def InitTitle(
        self, titles: PlotTitles, dataDirectory: str, scanStep: float
    ) -> None: ...

class QuantNoiseResult(
    Agilent.MassSpectrometry.DataAnalysis.IResult,
    Agilent.MassSpectrometry.DataAnalysis.INoiseResult,
    System.ICloneable,
):  # Class
    def __init__(self) -> None: ...

    NoiseMultiplier: float
    NoiseRegions: Agilent.MassSpectrometry.DataAnalysis.RangeCollection
    NoiseType: Agilent.MassSpectrometry.DataAnalysis.NoiseType
    NoiseValue: float
    SignalType: Agilent.MassSpectrometry.DataAnalysis.ResultAttribute

    def ClearCompoundResultAttributes(
        self, cpd: Agilent.MassSpectrometry.DataAnalysis.ICompound
    ) -> None: ...
    def ContainIDResult(self) -> bool: ...
    def WriteXML(self, writer: System.Xml.XmlWriter) -> None: ...
    def SynchronizeCompoundResultAttributes(
        self, cpd: Agilent.MassSpectrometry.DataAnalysis.ICompound
    ) -> None: ...

class QuantPSet(
    Iterable[Any],
    System.ICloneable,
    Agilent.MassSpectrometry.DataAnalysis.ICollectionElement,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
    Agilent.MassSpectrometry.DataAnalysis.IParameter,
    Agilent.MassSpectrometry.DataAnalysis.IParameterSet,
):  # Class
    ...

class QuantPSetChromPeakFilter(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantPSet,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
    Agilent.MassSpectrometry.DataAnalysis.IPSetPeakFilter,
    Agilent.MassSpectrometry.DataAnalysis.IParameterSet,
    Agilent.MassSpectrometry.DataAnalysis.ICollectionElement,
    Agilent.MassSpectrometry.DataAnalysis.IParameter,
    System.ICloneable,
    Iterable[Any],
):  # Class
    def __init__(self) -> None: ...

class QuantPSetExtractChrom(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantPSet,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
    Agilent.MassSpectrometry.DataAnalysis.IParameterSet,
    Agilent.MassSpectrometry.DataAnalysis.ICollectionElement,
    Agilent.MassSpectrometry.DataAnalysis.IParameter,
    Agilent.MassSpectrometry.DataAnalysis.IPSetExtractChrom,
    System.ICloneable,
    Iterable[Any],
):  # Class
    def __init__(self) -> None: ...

    CompoundName: str
    IntegratorName: str
    NeedTitle: bool
    NoiseMultiplier: float
    NoiseType: str
    Smoothing: bool
    UseEicIfEmptyFeatureChrom: bool

class QuantPSetExtractSpectrum(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantPSet,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
    Agilent.MassSpectrometry.DataAnalysis.IParameterSet,
    Agilent.MassSpectrometry.DataAnalysis.ICollectionElement,
    Agilent.MassSpectrometry.DataAnalysis.IParameter,
    System.ICloneable,
    Iterable[Any],
    Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum,
):  # Class
    def __init__(self) -> None: ...

    CompoundName: str
    DeviceName: str
    MzRanges: System.Collections.Generic.List[DoubleRange]
    NeedTitle: bool
    NoiseThreshold: float
    ReferenceWavelength: Agilent.MassSpectrometry.DataAnalysis.IRange
    SaturationThreshold: float
    SaturationTrackingMzRanges: System.Collections.Generic.List[DoubleRange]
    SignalName: str
    SignalWavelength: Agilent.MassSpectrometry.DataAnalysis.IRange
    UseReference: bool

class QuantPSetSignalToNoise(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantPSet,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
    Agilent.MassSpectrometry.DataAnalysis.IParameterSet,
    Agilent.MassSpectrometry.DataAnalysis.ICollectionElement,
    Agilent.MassSpectrometry.DataAnalysis.IParameter,
    System.ICloneable,
    Iterable[Any],
    Agilent.MassSpectrometry.DataAnalysis.IPSetSignalToNoise,
):  # Class
    def __init__(self) -> None: ...

class QuantPlotPreferences:  # Class
    def __init__(self) -> None: ...

    DrawingMode: Agilent.MassSpectrometry.DataAnalysis.DrawingMode
    XAxisLabel: str
    YAxisLabel: str

class QuantSpectrum(
    Agilent.MassSpectrometry.DataAnalysis.IFXArrayStore,
    Agilent.MassSpectrometry.DataAnalysis.IFXStore,
    Agilent.MassSpectrometry.DataAnalysis.IXYStore,
    Agilent.MassSpectrometry.DataAnalysis.IConsistency,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.QuantXYData,
    Agilent.MassSpectrometry.DataAnalysis.IXYData,
    Agilent.MassSpectrometry.DataAnalysis.IFXData,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
    Agilent.MassSpectrometry.DataAnalysis.IUnitsConverter,
    Agilent.MassSpectrometry.DataAnalysis.ISpectrum,
    System.ICloneable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        specData: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IChromSpecData,
        filter: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum,
        dataSourcePath: str,
    ) -> None: ...

    SpecFilter: Agilent.MassSpectrometry.DataAnalysis.IPSetExtractSpectrum  # readonly

    def InitTitle(
        self, titles: PlotTitles, dataDirectory: str, scanStep: float
    ) -> None: ...

class QuantXYData(
    Agilent.MassSpectrometry.DataAnalysis.IXYStore,
    Agilent.MassSpectrometry.DataAnalysis.IUnitsConverter,
    Agilent.MassSpectrometry.DataAnalysis.IFXData,
    System.ICloneable,
    Agilent.MassSpectrometry.DataAnalysis.IFXStore,
    Agilent.MassSpectrometry.DataAnalysis.IFXArrayStore,
    Agilent.MassSpectrometry.DataAnalysis.IXYData,
    Agilent.MassSpectrometry.DataAnalysis.IConsistency,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, xArray: List[float], yArray: List[float]) -> None: ...

    Count: int  # readonly
    HasGaps: bool  # readonly

    def GetYArray(self, copy: bool) -> List[float]: ...
    def GetXArray(self, copy: bool) -> List[float]: ...

class QuantXYDataDescription(
    System.ICloneable,
    Agilent.MassSpectrometry.DataAnalysis.IDescription,
    Agilent.MassSpectrometry.DataAnalysis.IConvertibleValueContainer,
    Agilent.MassSpectrometry.DataAnalysis.IConsistency,
):  # Class
    def __init__(self) -> None: ...

class QuantXYLimits(
    System.ICloneable,
    Agilent.MassSpectrometry.DataAnalysis.IFXLimits,
    Agilent.MassSpectrometry.DataAnalysis.IXYLimits,
    Agilent.MassSpectrometry.DataAnalysis.IConsistency,
):  # Class
    ...

class SparseChromDataBuffer(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IChromDataBuffer
):  # Class
    def __init__(
        self,
        cycleNumbers: System.Collections.Generic.List[int],
        rtValues: System.Collections.Generic.List[float],
    ) -> None: ...

    XValues: List[float]  # readonly
    YValues: List[float]  # readonly

    def AddDataPoint(self, abundance: float, cycleNumber: int) -> None: ...
    def AddChromDataSegment(
        self,
        abundances: List[float],
        cycleNumbers: List[int],
        minIndex: int,
        maxIndex: int,
    ) -> None: ...

class TofSpecData(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.CoreDataTypes.IChromSpecData
):  # Class
    def __init__(
        self,
        mzValues: List[float],
        abundances: List[float],
        rtRanges: System.Collections.Generic.List[DoubleRange],
        scanCount: int,
    ) -> None: ...

    Count: int  # readonly
    HasData: bool  # readonly
    HasGaps: bool  # readonly
    NScanLinesForSpectrum: int  # readonly
    RtRanges: System.Collections.Generic.List[DoubleRange]  # readonly
    XArray: List[float]  # readonly
    YArray: List[float]  # readonly

    def Sort(self) -> None: ...
