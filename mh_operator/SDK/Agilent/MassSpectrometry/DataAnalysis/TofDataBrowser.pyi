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

from . import IChromPeak, IFXData, IonPolarity, MSScanType
from .FD import Feature, IScanSpace, Ridge, ScanConditions
from .FeatureDataAccess import RidgeSet
from .Quantitative import ITimeToMassConversion, QuantDataAccess, ScanRecord

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser

class BaselineRegion:  # Class
    ...

class CentroidSpectrum:  # Class
    def __init__(
        self,
        profileSpectrum: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.ProfileSpectrum,
    ) -> None: ...

    BasePeakIndex: int  # readonly
    Count: int  # readonly
    IsMassSpectrum: bool  # readonly
    XArray: List[float]  # readonly
    YArray: List[float]  # readonly

class CentroidType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AbundanceWeighted: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidType
    ) = ...  # static # readonly
    Parabolic: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidType = (
        ...
    )  # static # readonly

class CentroidingFinishedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, e: System.EventArgs) -> None: ...

class CentroidingScanRecordEventArgs:  # Class
    def __init__(self, scanRecordIndex: int) -> None: ...

    ScanRecordIndex: int  # readonly

class CentroidingScanRecordEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidingScanRecordEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidingScanRecordEventArgs,
    ) -> None: ...

class CentroidingStartingEventArgs:  # Class
    def __init__(self, sampleDataPath: str, nScanRecords: int) -> None: ...

    NumScanRecords: int  # readonly
    SampleDataPath: str  # readonly

class CentroidingStartingEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidingStartingEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidingStartingEventArgs,
    ) -> None: ...

class FeatureDetectionFinishedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, e: System.EventArgs) -> None: ...

class FeatureDetectionScanRecordEventArgs:  # Class
    def __init__(self, scanRecordIndex: int) -> None: ...

    ScanRecordIndex: int  # readonly

class FeatureDetectionStartedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, e: System.EventArgs) -> None: ...

class FeatureDetectionStartingEventArgs:  # Class
    def __init__(self, sampleDataPath: str, nScanRecords: int) -> None: ...

    NumScanRecords: int  # readonly
    SampleDataPath: str  # readonly

class InterpolationType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Linear: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.InterpolationType = (
        ...
    )  # static # readonly
    Quadratic: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.InterpolationType
    ) = ...  # static # readonly

class MassCalResults:  # Class
    AValues: List[float]  # readonly
    AverageA: float  # readonly
    AverageT0: float  # readonly
    T0Values: List[float]  # readonly

class MassCalibrationOptions:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, optionsFile: str) -> None: ...

    DoMassCal: bool
    MaxRefMzDelta: float
    MinFoundRefMzsForTradFit: int
    MinFoundRefMzsPerRange: int
    ReferenceMassFilePath: str
    WriteMassCalResults: bool
    WriteRefMzResiduals: bool

class MassCalibrator:  # Class
    def __init__(
        self,
        dataAccess: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.SpectrumDataAccess,
        options: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.MassCalibrationOptions,
    ) -> None: ...

    MassCalResults: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.MassCalResults
    )  # readonly
    MzSearchRangeDeltas: List[float]  # readonly
    RefMzCount: int  # readonly
    ReferenceMZs: List[float]  # readonly

    def ReadReferenceMasses(self, refMassFilePath: str) -> bool: ...
    def GetReferenceMassData(
        self, refMassIndex: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.ReferenceMassData: ...
    def SetMzSearchRange(self, mzSearchRangeDelta: float) -> None: ...

class PeakRegion:  # Class
    ...

class PeakShape:  # Class
    ...

class PeakShapeFit:  # Class
    ...

class ProfileDataCentroider:  # Class
    def __init__(
        self,
        dataNavigator: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.SampleDataNavigator,
        massCal: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.MassCalibrator,
    ) -> None: ...

    Cancelled: bool  # readonly
    MassCalibration: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.MassCalibrator
    )  # readonly
    ScanRecordCount: int  # readonly

    def CancelCentroiding(self) -> None: ...
    def CentroidSampleData(self) -> None: ...

    CentroidingFinished: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidingFinishedEventHandler
    )  # Event
    CentroidingScanRecordStarting: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidingScanRecordEventHandler
    )  # Event
    CentroidingStarting: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidingStartingEventHandler
    )  # Event

class ProfileDataFeatureDetector:  # Class
    def __init__(
        self,
        dataNavigator: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.SampleDataNavigator,
    ) -> None: ...

    Cancelled: bool  # readonly
    FeatureCount: int  # readonly
    IsFeatureDataPresent: bool  # readonly
    ProcessingTime: System.TimeSpan  # readonly
    RidgeCount: int  # readonly
    SampleDataPath: str  # readonly

    def Start(self) -> None: ...
    def Cancel(self) -> None: ...

    FeatureDetectionFinished: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.FeatureDetectionFinishedEventHandler
    )  # Event
    FeatureDetectionStarted: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.FeatureDetectionStartedEventHandler
    )  # Event
    RidgeDetectionCancelled: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.RidgeDetectionCancelledEventHandler
    )  # Event
    RidgeDetectionFinished: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.RidgeDetectionFinishedEventHandler
    )  # Event
    RidgeDetectionScanRecordProcessing: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.RidgeDetectionScanRecordEventHandler
    )  # Event
    RidgeDetectionStarting: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.RidgeDetectionStartingEventHandler
    )  # Event

class ProfileSpectrum:  # Class
    Count: int  # readonly
    IsMassSpectrum: bool  # readonly
    ScanRecord: ScanRecord  # readonly
    TimeToMassConversion: ITimeToMassConversion  # readonly
    XArray: List[float]  # readonly
    YArray: List[float]  # readonly

    def ConvertMassToFlightTime(self, mass: float) -> float: ...
    def WriteCSV(self, sw: System.IO.StreamWriter) -> None: ...
    def FindPeaks(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.ProfileSpectrumPeak
    ]: ...

class ProfileSpectrumPeak:  # Class
    ApexIndex: int  # readonly
    CenterX: float  # readonly
    EndBaselineY: float  # readonly
    EndIndex: int  # readonly
    EndX: float  # readonly
    Height: float  # readonly
    InterpolatedPeakX: float  # readonly
    InterpolatedPeakY: float  # readonly
    IsMerged: bool  # readonly
    IsSaturated: bool  # readonly
    PeakRegion: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.PeakRegion
    )  # readonly
    PointCount: int  # readonly
    StartBaselineY: float  # readonly
    StartIndex: int  # readonly
    StartX: float  # readonly

class ProfileSpectrumPeakFinder:  # Class
    @overload
    def __init__(self, timeToMass: ITimeToMassConversion) -> None: ...
    @overload
    def __init__(
        self,
        options: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.SpectrumPeakFinderOptions,
        timeToMass: ITimeToMassConversion,
    ) -> None: ...

    YMax: int  # readonly
    YMin: int  # readonly

    def FindSpectrumPeaks(
        self, xArray: List[float], yArray: List[float], satLimit: float
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.ProfileSpectrumPeak
    ]: ...

class ReferenceMassData:  # Class
    def __init__(
        self,
        massCal: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.MassCalibrator,
        refMzIndex: int,
        nScanLines: int,
    ) -> None: ...

    AbundanceFitResiduals: List[float]  # readonly
    AbundanceProfile: List[float]  # readonly
    MzDeltaProfile: List[float]  # readonly
    PointCount: int  # readonly
    ReferenceMass: float  # readonly
    ReferenceMassIndex: int  # readonly

    def ExcludeInterferenceRegions(
        self, peakList: System.Collections.Generic.List[IChromPeak]
    ) -> None: ...
    def FillInTheGaps(self) -> None: ...
    def FitAbundanceProfile(self) -> bool: ...
    def AddScanLineData(
        self, scanLineIndex: int, scanTime: float, mzDelta: float, abundance: float
    ) -> None: ...
    def InitExclusionMap(self) -> None: ...
    def IsExcluded(self, scanIndex: int) -> bool: ...
    @overload
    def FindAbundancePeaks(self) -> System.Collections.Generic.List[IChromPeak]: ...
    @overload
    def FindAbundancePeaks(
        self, xArray: List[float]
    ) -> System.Collections.Generic.List[IChromPeak]: ...

class RidgeDetectionCancelledEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, e: System.EventArgs) -> None: ...

class RidgeDetectionFinishedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: System.EventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, sender: Any, e: System.EventArgs) -> None: ...

class RidgeDetectionScanRecordEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.FeatureDetectionScanRecordEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.FeatureDetectionScanRecordEventArgs,
    ) -> None: ...

class RidgeDetectionStartingEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.FeatureDetectionStartingEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.FeatureDetectionStartingEventArgs,
    ) -> None: ...

class RidgeFeatureInfo:  # Class
    Features: System.Collections.Generic.List[Feature]  # readonly
    Ridge: Ridge  # readonly
    ScanSpace: IScanSpace  # readonly

class SampleDataNavigator(System.IDisposable):  # Class
    def __init__(self, sampleDataDir: str) -> None: ...

    CollisionEnergy: float  # readonly
    CurrentRT: float  # readonly
    CycleNumber: int  # readonly
    DataAccess: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.SpectrumDataAccess
    )  # readonly
    FragmentorVoltage: float  # readonly
    MultipleScanConditions: bool  # readonly
    MzOfInterest: float  # readonly
    Polarity: IonPolarity  # readonly
    PolarityString: str  # readonly
    RidgeSet: RidgeSet  # readonly
    SampleDataDir: str  # readonly
    ScanConditions: ScanConditions  # readonly
    ScanID: int  # readonly
    ScanIndex: int  # readonly
    ScanRecordCount: int  # readonly
    ScanType: MSScanType  # readonly

    @overload
    def GetCentroidTofSpectrum(
        self,
        profileSpectrum: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.ProfileSpectrum,
    ) -> Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidSpectrum: ...
    @overload
    def GetCentroidTofSpectrum(
        self, scanIndex: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidSpectrum: ...
    def GetScanConditionsString(self) -> str: ...
    def GetCenteredDataRange(
        self, firstPointIndex: int, centerScanIndex: int, nScans: int, nPoints: int
    ) -> List[List[float]]: ...
    def ClearSpectrumCache(self) -> None: ...
    def GetTofSpectrum(
        self, scanIndex: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.ProfileSpectrum: ...
    def GetDataRange(
        self, firstScanIndex: int, firstPointIndex: int, nScans: int, nPoints: int
    ) -> List[List[float]]: ...
    def GetPrevScanIndex_SameScanConditions(self) -> int: ...
    def CaptureRidgeInfo(
        self, scanIndex: int, x: float, xIsMass: bool
    ) -> Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.RidgeFeatureInfo: ...
    def GetCentroidMassSpectrum(
        self, scanIndex: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidSpectrum: ...
    def XtoScanIndex(self, x: float, xNearestScanLine: float) -> int: ...
    def SameScanConditions(self, scanConditions: ScanConditions) -> bool: ...
    def Dispose(self) -> None: ...
    def GetTIC(self) -> IFXData: ...
    def GetNextScanIndex_SameScanConditions(self) -> int: ...
    def GetMassSpectrum(
        self, scanIndex: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.ProfileSpectrum: ...

class SpectrumDataAccess:  # Class
    def __init__(self) -> None: ...

    IsAccurateMass: bool  # readonly
    PeakFinderOptions: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.SpectrumPeakFinderOptions
    )  # readonly
    QuantDataAccess: QuantDataAccess  # readonly
    RecordCount: int  # readonly
    SampleDataPath: str  # readonly

    def GetAbundanceArrayFromScanRecord(
        self, scanNumber: int, firstPointIndex: int, nPoints: int
    ) -> List[float]: ...
    def Open(self, sampleDataPath: str) -> None: ...
    def GetScanTimeForScanRecord(self, scanNumber: int) -> float: ...
    def GetNextScanIndexForSameScanConditions(
        self, scanIndex: int, scanConditions: ScanConditions
    ) -> int: ...
    def GetScanConditionsForScanRecord(self, scanNumber: int) -> ScanConditions: ...
    def GetScanRecordByScanIndex(self, scanNumber: int) -> ScanRecord: ...
    def ExportProfileSpectrum(self, scanNumber: int) -> None: ...
    def CaptureApexSpacingHistogram(self, scanNumber: int) -> None: ...
    def Close(self) -> None: ...
    def ExportProfileSpectra(self, scanNumbers: List[int]) -> None: ...
    def GetApexSpacingHistogram(self, scanRecord: ScanRecord) -> List[int]: ...
    def GetProfileDataForScanRecord(
        self, scanNumber: int, applyMassCal: bool
    ) -> Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.ProfileSpectrum: ...
    def GetPrevScanIndexForSameScanConditions(
        self, scanIndex: int, scanConditions: ScanConditions
    ) -> int: ...

class SpectrumPeakFinderOptions:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, optionsFile: str) -> None: ...

    ApplyMassStepFiltering: bool
    CentroidType: Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.CentroidType
    InterpolationType: (
        Agilent.MassSpectrometry.DataAnalysis.TofDataBrowser.InterpolationType
    )
    ResolveShoulderPeaks: bool
    WriteApexList: bool
    WriteHistogram: bool
    WritePeakShapes: bool
