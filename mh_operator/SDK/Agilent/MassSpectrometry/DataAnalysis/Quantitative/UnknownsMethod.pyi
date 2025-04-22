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

from . import Signal
from .Compliance import ICompliance

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UnknownsMethod

class BlankSubtractionControl(
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

    IsDirty: bool

    def ApplyTo(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodDataTable,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def Initialize(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.BlankSubtractionMethodDataTable,
        batchID: int,
        sampleID: int,
    ) -> None: ...
    def Default(self) -> None: ...

class DeconvolutionControl(
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

    IsDirty: bool

    def ApplyTo(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def Initialize(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
        batchID: int,
        sampleID: int,
    ) -> None: ...
    def Default(self) -> None: ...

class IdentificationControl(
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

    ExactMassVisible: bool
    IsDirty: bool

    def ApplyTo(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodDataTable,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def Initialize(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.IdentificationMethodDataTable,
        batchID: int,
        sampleID: int,
    ) -> None: ...
    def Default(self) -> None: ...

class LibrarySearchControl(
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

    IsDirty: bool

    def ApplyTo(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodDataTable,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def Initialize(
        self,
        compliance: ICompliance,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.LibrarySearchMethodDataTable,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
    ) -> None: ...
    def Default(self) -> None: ...

class MethodControl(
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
    def SetDirty(self, dirty: bool) -> None: ...
    def ApplyTo(
        self,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
    ) -> None: ...
    def Initialize(
        self,
        compliance: ICompliance,
        dataSet: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet,
        batchID: int,
        sampleID: int,
        referenceSampleFilePath: str,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    @staticmethod
    def GetSignals(compliance: ICompliance, sampleFilePath: str) -> List[Signal]: ...
    def Default(self) -> None: ...

class MethodPane(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Auxiliary: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UnknownsMethod.MethodPane
    ) = ...  # static # readonly
    BlankSubtraction: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UnknownsMethod.MethodPane
    ) = ...  # static # readonly
    Deconvolution: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UnknownsMethod.MethodPane
    ) = ...  # static # readonly
    Identification: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UnknownsMethod.MethodPane
    ) = ...  # static # readonly
    LibrarySearch: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UnknownsMethod.MethodPane
    ) = ...  # static # readonly
    TargetMatch: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UnknownsMethod.MethodPane
    ) = ...  # static # readonly

class NullableBooleanBinding(System.Windows.Forms.Binding):  # Class
    def __init__(self, propertyName: str, dataSource: Any, dataMember: str) -> None: ...

class PeakDetectionControl(
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

    IsDirty: bool

    def ApplyTo(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def Initialize(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
        batchID: int,
        sampleID: int,
        referenceSignals: List[Signal],
    ) -> None: ...
    def Default(self) -> None: ...

class TICAnalysisSignalDialog(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
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
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

    SignalType: str  # readonly

    def Initialize(self, signalType: str, referenceSignals: List[Signal]) -> None: ...

class TargetMatchControl(
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

    IsDirty: bool

    def ApplyTo(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodDataTable,
    ) -> None: ...
    def HasChanges(self) -> bool: ...
    def Initialize(
        self,
        table: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetMatchMethodDataTable,
        batchID: int,
        sampleID: int,
    ) -> None: ...
    def Default(self) -> None: ...
