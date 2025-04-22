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

from .Models import (
    IAppCommandContext,
    ICalibrationRange,
    ICalibrationRangeItem,
    ICalibrationRangeViewModel,
    ICalibrationViewModel,
    ICompoundsViewModel,
    IDynamicCalibrationSetupModel,
    IIonGroupGraphicsViewModel,
    IIonGroupItem,
    IIonGroupPlotSeries,
    IIonGroupViewModel,
    IQualifiersViewModel,
)

# Stubs for namespace: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.ViewModels

class CalibrationRangeItem(ICalibrationRangeItem):  # Class
    def __init__(self, calRange: ICalibrationRange) -> None: ...

    CalibrationRangeID: int  # readonly
    MaxConcentration: Optional[float]  # readonly
    MinConcentration: Optional[float]  # readonly
    QualifierIonGroupIDs: List[int]  # readonly
    TargetCompoundID: int  # readonly
    TargetIonGroupID: Optional[int]  # readonly

class CalibrationRangeViewModel(
    System.Windows.DependencyObject, System.IDisposable, ICalibrationRangeViewModel
):  # Class
    def __init__(self, model: IDynamicCalibrationSetupModel) -> None: ...

    DynamicCalibrationSetupModel: IDynamicCalibrationSetupModel  # readonly

    def Dispose(self) -> None: ...

class CalibrationViewModel(
    System.IDisposable,
    ICalibrationViewModel,
    System.Windows.DependencyObject,
    System.Collections.Generic.IComparer[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.CalibrationRow
    ],
):  # Class
    def __init__(self, model: IDynamicCalibrationSetupModel) -> None: ...

    CalibrationProperty: System.Windows.DependencyProperty  # static

    Calibration: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.CalibrationRow
    ]
    DynamicCalibrationSetupModel: IDynamicCalibrationSetupModel  # readonly
    SortAscending: bool  # readonly
    SortedColumn: str  # readonly

    def SetSort(self, sortColumn: str, sortAscending: bool) -> None: ...
    def Dispose(self) -> None: ...
    def Compare(
        self,
        o1: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.CalibrationRow,
        o2: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.CalibrationRow,
    ) -> int: ...

class CompoundsViewModel(
    ICompoundsViewModel, System.Windows.DependencyObject, System.IDisposable
):  # Class
    def __init__(self, model: IDynamicCalibrationSetupModel) -> None: ...

    TargetCompoundProperty: System.Windows.DependencyProperty  # static

    DynamicCalibrationSetupModel: IDynamicCalibrationSetupModel  # readonly
    TargetCompound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet.TargetCompoundDataTable
    )

    def Dispose(self) -> None: ...

class DynamicCalibrationModel(
    System.Windows.DependencyObject, System.IDisposable, IDynamicCalibrationSetupModel
):  # Class
    def __init__(self) -> None: ...

    CalibrationRangesProperty: System.Windows.DependencyProperty  # static
    CurrentCalibrationRangeProperty: System.Windows.DependencyProperty  # static
    CurrentCompoundProperty: System.Windows.DependencyProperty  # static
    CurrentIonGroupProperty: System.Windows.DependencyProperty  # static
    IonGroupsProperty: System.Windows.DependencyProperty  # static

    AppCommandContext: IAppCommandContext  # readonly
    CalibrationRangeViewModel: ICalibrationRangeViewModel  # readonly
    CalibrationRanges: List[ICalibrationRangeItem]
    CalibrationViewModel: ICalibrationViewModel  # readonly
    CompoundsViewModel: ICompoundsViewModel  # readonly
    CurrentCalibrationRange: ICalibrationRangeItem
    CurrentCompound: System.Data.DataRowView
    CurrentIonGroup: IIonGroupItem
    IonGroupGraphicsViewModel: IIonGroupGraphicsViewModel  # readonly
    IonGroupViewModel: IIonGroupViewModel  # readonly
    IonGroups: List[IIonGroupItem]
    QualifiersViewModel: IQualifiersViewModel  # readonly
    Window: System.Windows.Window

    def Dispose(self) -> None: ...

class IonGroupGraphicsViewModel(
    IIonGroupGraphicsViewModel, System.Windows.DependencyObject, System.IDisposable
):  # Class
    def __init__(self, model: IDynamicCalibrationSetupModel) -> None: ...

    PlotSeriesProperty: System.Windows.DependencyProperty  # static
    SelectedSeriesProperty: System.Windows.DependencyProperty  # static

    DynamicCalibrationSetupModel: IDynamicCalibrationSetupModel  # readonly
    PlotSeries: List[IIonGroupPlotSeries]
    SelectedSeries: IIonGroupPlotSeries

    def Dispose(self) -> None: ...

class IonGroupItem(IIonGroupItem):  # Class
    def __init__(
        self,
        id: int,
        ionGroup: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ICrossSampleIonGroup,
    ) -> None: ...

    ConcentrationRangeString: str  # readonly
    CrossSampleIonGroup: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ICrossSampleIonGroup
    )  # readonly
    IonGroupID: int  # readonly
    MZ: float  # readonly
    TargetCompoundID: int  # readonly
    UnsaturatedRangeString: str  # readonly

class IonGroupViewModel(System.IDisposable, IIonGroupViewModel):  # Class
    def __init__(self, model: IDynamicCalibrationSetupModel) -> None: ...

    DynamicCalibrationSetupModel: IDynamicCalibrationSetupModel  # readonly

    def Dispose(self) -> None: ...

class QualifiersViewModel(
    IQualifiersViewModel, System.Windows.DependencyObject, System.IDisposable
):  # Class
    def __init__(self, model: IDynamicCalibrationSetupModel) -> None: ...

    DynamicCalibrationSetupModel: IDynamicCalibrationSetupModel  # readonly
    TargetQualifier: System.Data.DataView  # readonly

    def Dispose(self) -> None: ...
