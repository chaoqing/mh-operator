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

# Stubs for namespace: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models

class IAppCommandContext(
    Agilent.MassSpectrometry.CommandModel.Model.ICommandHistory, System.IDisposable
):  # Interface
    BatchGlobalFeatureAnalysis: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchGlobalFeatureAnalysis
    )  # readonly
    IsBatchOpen: bool  # readonly
    MethodDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDataSet
    )  # readonly
    QuantAppCommandContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AppCommandContext
    )  # readonly

    def RemoveCalibrationRange(
        self, targetCompoundID: int, calibrationRangeID: int
    ) -> None: ...
    def CloseBatch(self) -> None: ...
    def NewCalibrationRange(
        self, targetCompoundID: int
    ) -> (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.ICalibrationRange
    ): ...
    def SaveMethod(self, pathName: str) -> None: ...
    def AddCalibrationRange(
        self,
        range: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.ICalibrationRange,
    ) -> None: ...
    def OpenBatch(self, batchFolder: str, batchFile: str, analyze: bool) -> None: ...
    def GetCalibrationRanges(
        self, targetCompoundID: int
    ) -> List[
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.ICalibrationRange
    ]: ...
    def GetCalibrationRange(
        self, targetCompoundID: int, calibrationRangeID: int
    ) -> (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.ICalibrationRange
    ): ...

    Analyzed: System.EventHandler  # Event
    Analyzing: System.EventHandler  # Event
    BatchClosed: System.EventHandler  # Event
    BatchOpened: System.EventHandler  # Event
    CalibrationRangesChanged: System.EventHandler  # Event
    Progress: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ProgressEventArgs
    ]  # Event

class ICalibrationRange(object):  # Interface
    CalibrationRangeID: int  # readonly
    MaxConcentration: Optional[float]
    MinConcentration: Optional[float]
    QualifierIonGroupIDs: List[int]  # readonly
    TargetCompoundID: int  # readonly
    TargetIonGroupID: Optional[int]

    def AddQualifierIonGroupID(self, id: int) -> None: ...
    def RemoveQualifierIonGroupID(self, id: int) -> None: ...

class ICalibrationRangeItem(object):  # Interface
    CalibrationRangeID: int  # readonly
    MaxConcentration: Optional[float]  # readonly
    MinConcentration: Optional[float]  # readonly
    QualifierIonGroupIDs: List[int]  # readonly
    TargetCompoundID: int  # readonly
    TargetIonGroupID: Optional[int]  # readonly

class ICalibrationRangeViewModel(object):  # Interface
    DynamicCalibrationSetupModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IDynamicCalibrationSetupModel
    )  # readonly

class ICalibrationViewModel(object):  # Interface
    Calibration: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.CalibrationRow
    ]  # readonly
    DynamicCalibrationSetupModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IDynamicCalibrationSetupModel
    )  # readonly

    def SetSort(self, sortColumn: str, ascending: bool) -> None: ...

class ICompoundsViewModel(object):  # Interface
    DynamicCalibrationSetupModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IDynamicCalibrationSetupModel
    )  # readonly
    TargetCompound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundDataTable
    )  # readonly

class IDynamicCalibrationSetupModel(System.IDisposable):  # Interface
    AppCommandContext: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IAppCommandContext
    )  # readonly
    CalibrationRangeViewModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.ICalibrationRangeViewModel
    )  # readonly
    CalibrationRanges: List[
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.ICalibrationRangeItem
    ]  # readonly
    CalibrationViewModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.ICalibrationViewModel
    )  # readonly
    CompoundsViewModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.ICompoundsViewModel
    )  # readonly
    CurrentCalibrationRange: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.ICalibrationRangeItem
    )
    CurrentCompound: System.Data.DataRowView
    CurrentIonGroup: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IIonGroupItem
    )
    IonGroupViewModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IIonGroupViewModel
    )  # readonly
    IonGroups: List[
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IIonGroupItem
    ]  # readonly
    QualifiersViewModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IQualifiersViewModel
    )  # readonly
    Window: System.Windows.Window

class IIonGroupGraphicsViewModel(object):  # Interface
    DynamicCalibrationSetupModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IDynamicCalibrationSetupModel
    )  # readonly

class IIonGroupItem(object):  # Interface
    ConcentrationRangeString: str  # readonly
    CrossSampleIonGroup: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ICrossSampleIonGroup
    )  # readonly
    IonGroupID: int  # readonly
    TargetCompoundID: int  # readonly

class IIonGroupPlotSeries(
    Agilent.MassHunter.Quantitative.PlotControl.IPlotSeries
):  # Interface
    Item: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IIonGroupItem
    )  # readonly

class IIonGroupViewModel(object):  # Interface
    DynamicCalibrationSetupModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IDynamicCalibrationSetupModel
    )  # readonly

class IQualifiersViewModel(object):  # Interface
    DynamicCalibrationSetupModel: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Models.IDynamicCalibrationSetupModel
    )  # readonly
    TargetQualifier: System.Data.DataView  # readonly
