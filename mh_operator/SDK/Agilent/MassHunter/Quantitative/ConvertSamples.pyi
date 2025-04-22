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

# Stubs for namespace: Agilent.MassHunter.Quantitative.ConvertSamples

class App(
    System.Windows.Application,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    @staticmethod
    def Main() -> None: ...

class CommandLine:  # Class
    def __init__(self) -> None: ...

    BatchFolder: str
    Culture: str

class ConvertSamplesContext(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CreateBatch: (
        Agilent.MassHunter.Quantitative.ConvertSamples.ConvertSamplesContext
    ) = ...  # static # readonly
    OpenBatchOrApplyMethod: (
        Agilent.MassHunter.Quantitative.ConvertSamples.ConvertSamplesContext
    ) = ...  # static # readonly

class ConvertTofDataControl(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    def SetBatchFolder(self, batchFolder: str) -> None: ...
    def SetSamples(self, batchFolder: str, samplePaths: List[str]) -> None: ...

class ConvertTofDataModel(System.ComponentModel.INotifyPropertyChanged):  # Class
    def __init__(
        self, model: Agilent.MassHunter.Quantitative.ConvertSamples.Model
    ) -> None: ...

    AlwaysConvert: bool
    AlwaysConvertEnabled: bool  # readonly
    BatchFolder: str
    CanConvert: bool  # readonly
    CanDeleteFD: bool  # readonly
    CanDeleteTDA: bool  # readonly
    ConvertToFD: bool
    ConvertToTDA: bool
    DeleteFD: bool
    DeleteTDA: bool
    Model: Agilent.MassHunter.Quantitative.ConvertSamples.Model  # readonly
    Samples: List[
        Agilent.MassHunter.Quantitative.ConvertSamples.ConvertTofDataSample
    ]  # readonly

    def Clear(self) -> None: ...
    @overload
    def SetSamples(self, batchFolder: str, samplePaths: List[str]) -> None: ...
    @overload
    def SetSamples(self, batchFolder: str) -> None: ...
    def UpdateSamples(self) -> None: ...

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class ConvertTofDataSample:  # Class
    def __init__(
        self, model: Agilent.MassHunter.Quantitative.ConvertSamples.ConvertTofDataModel
    ) -> None: ...

    AcqDateTime: Optional[System.DateTime]
    CanConvertToFD: bool
    CanConvertToTDA: bool
    DataFileName: str
    FeatureDetected: bool
    IsSelected: bool
    PathName: str
    SampleGroup: str
    SampleName: str
    TDAConverted: bool

class ConvertUtils:  # Class
    @staticmethod
    def GetSampleInfo(
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        samples: List[str],
    ) -> List[Agilent.MassHunter.Quantitative.ConvertSamples.ConvertTofDataSample]: ...
    @staticmethod
    def DoesBatchRequireFD(
        bds: Agilent.MassSpectrometry.DataAnalysis.Quantitative.BatchDataSet,
        batchId: int,
    ) -> bool: ...
    @staticmethod
    def CheckTofData(
        samplePaths: List[str],
        hasTOFSamples: bool,
        hasSamplesWithoutFD: bool,
        hasSamplesWithoutTDA: bool,
    ) -> None: ...
    @overload
    @staticmethod
    def CheckSamplesAndShowConvertWindow(
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> bool: ...
    @overload
    @staticmethod
    def CheckSamplesAndShowConvertWindow(
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
        requireFD: bool,
        useProfile: bool,
    ) -> bool: ...
    @overload
    @staticmethod
    def CheckSamplesAndShowConvertWindow(
        parent: System.Windows.Forms.IWin32Window,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        batchFolder: str,
        samplePathNames: List[str],
        context: Agilent.MassHunter.Quantitative.ConvertSamples.ConvertSamplesContext,
        requireFD: bool,
        useProfile: bool,
    ) -> bool: ...
    @staticmethod
    def DoesBatchUseProfile(
        bds: Agilent.MassSpectrometry.DataAnalysis.Quantitative.BatchDataSet,
        batchId: int,
    ) -> bool: ...

class Converter:  # Class
    def __init__(self) -> None: ...
    def DetectFeatures(
        self,
        samplePath: str,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...
    def ConvertToTDA(
        self,
        samplePath: str,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...
    def Abort(self) -> None: ...

class MainWindow(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IWindowService,
    Infragistics.Windows.Ribbon.IRibbonWindow,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Animation.IAnimatable,
    System.ComponentModel.ISupportInitialize,
    Infragistics.Windows.Ribbon.XamRibbonWindow,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...
    def InitializeComponent(self) -> None: ...
    def SetBatchFolder(self, batchFolder: str) -> None: ...
    def SetSamples(self, batchFolder: str, samplePaths: List[str]) -> None: ...
    def ShowDialogAndInitialize(
        self, batchPath: str, samplePaths: List[str]
    ) -> Optional[bool]: ...

class Model(System.ComponentModel.INotifyPropertyChanged):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        window: Agilent.MassHunter.Quantitative.ConvertSamples.MainWindow,
    ) -> None: ...

    CanAbort: bool  # readonly
    CanBack: bool  # readonly
    CanClose: bool  # readonly
    CanConvert: bool  # readonly
    ControllVisibility: System.Windows.Visibility  # readonly
    ConvertTofDataModel: (
        Agilent.MassHunter.Quantitative.ConvertSamples.ConvertTofDataModel
    )  # readonly
    ElapsedTime: str  # readonly
    Progress: float  # readonly
    ProgressText: str  # readonly
    ProgressVisibility: System.Windows.Visibility  # readonly

    def BeginConvert(self) -> System.IAsyncResult: ...
    def Abort(self) -> None: ...

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class RemoteConverter(System.MarshalByRefObject, System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def InitializeLifetimeService(self) -> Any: ...
    def ConvertToTDA(self, samplePath: str) -> None: ...
    def DetectFeatures(self, samplePath: str) -> None: ...
    def Abort(self) -> None: ...
    def Dispose(self) -> None: ...
