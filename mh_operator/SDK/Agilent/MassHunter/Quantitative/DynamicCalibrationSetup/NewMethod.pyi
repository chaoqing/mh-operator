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

# Stubs for namespace: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod

class AdductItem:  # Class
    def __init__(self, name: str) -> None: ...

    IsChecked: bool
    Name: str

class CalibrationSampleModel(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self) -> None: ...

    AcqDateTime: System.DateTime
    FileName: str
    IsSelected: bool
    LevelConcentration: Optional[float]
    LevelName: str
    SampleName: str

    def Clone(
        self,
    ) -> (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.CalibrationSampleModel
    ): ...

class NewMethodAcrossCalibrationsModel(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        window: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.NewMethodFromCalibrationsWindow,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

    Adducts: List[str]
    AdductsCommand: System.Windows.Input.ICommand  # readonly
    AdductsStr: str
    BatchPath: str
    BatchPathCommand: System.Windows.Input.ICommand  # readonly
    CalibrationSamples: List[
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.CalibrationSampleModel
    ]
    CalibrationSamplesCommand: System.Windows.Input.ICommand  # readonly
    DestinationMethodName: str
    ImportBatchCommand: System.Windows.Input.ICommand  # readonly
    LibraryPath: str
    NumberOfQualifiers: int
    NumberOfSelectedCalibrationSamples: str  # readonly
    NumberOfSelectedTargetCompounds: str  # readonly
    ReferenceLibraryCommand: System.Windows.Input.ICommand  # readonly
    TargetCompounds: List[
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.TargetCompoundModel
    ]
    TargetCompoundsCommand: System.Windows.Input.ICommand  # readonly

    def _CreateMethod(
        self,
        dlg: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs2.ProgressDialog,
    ) -> bool: ...
    def SetBatchFolder(self, batchFolder: str) -> None: ...
    def ValidateTargetCompounds(
        self,
        compounds: List[
            Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.TargetCompoundModel
        ],
    ) -> None: ...
    def CreateMethod(self) -> bool: ...
    def ValidateCalibrationSamples(
        self,
        samples: List[
            Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.CalibrationSampleModel
        ],
    ) -> None: ...

class NewMethodFromCalibrationsWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class SelectAdductsModel(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self) -> None: ...

    Items: List[
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.AdductItem
    ]  # readonly
    SelectedAdducts: List[str]

class SelectAdductsWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class SelectCalibrationsModel:  # Class
    def __init__(
        self,
        calibrations: List[
            Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.CalibrationSampleModel
        ],
    ) -> None: ...

    CalibrationSamples: List[
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.CalibrationSampleModel
    ]

class SelectCalibrationsWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class TargetCompoundModel(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self) -> None: ...

    CAS: str
    CompoundName: str
    Formula: str
    IsSelected: bool
    RetentionTime: Optional[float]

    def Clone(
        self,
    ) -> (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.TargetCompoundModel
    ): ...

class TargetCompoundsModel(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        window: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.TargetCompoundsWindow,
        compounds: List[
            Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.TargetCompoundModel
        ],
    ) -> None: ...

    CommandAdd: System.Windows.Input.ICommand  # readonly
    CommandDelete: System.Windows.Input.ICommand  # readonly
    CommandImportLibrary: System.Windows.Input.ICommand  # readonly
    CommandOK: System.Windows.Input.ICommand  # readonly
    CommandSelectAll: System.Windows.Input.ICommand  # readonly
    TargetCompounds: List[
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.NewMethod.TargetCompoundModel
    ]

class TargetCompoundsWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...
