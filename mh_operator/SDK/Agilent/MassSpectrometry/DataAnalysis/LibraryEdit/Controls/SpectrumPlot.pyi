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

from . import TitledPanel

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Controls.SpectrumPlot

class SpectrumPlotControl(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    Agilent.MassSpectrometry.GUI.Plot.PlotControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

    CanCopy: bool  # readonly
    CanCut: bool  # readonly
    CanDelete: bool  # readonly
    CanPaste: bool  # readonly
    DrawMolecularStructure: bool
    MaxNumRowsPerPage: int
    SelectedSpectrumKeys: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Utils.SpectrumKey
    ]  # readonly
    UIContext: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.UIContext

    def Copy(self) -> None: ...
    def GetAutoScaleRangeY(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane, minX: float, maxX: float
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def GetAutoScaleRangeX(
        self, pane: Agilent.MassSpectrometry.GUI.Plot.Pane
    ) -> Agilent.MassSpectrometry.GUI.Plot.PlotRange: ...
    def Cut(self) -> None: ...
    def Delete(self) -> None: ...
    def Paste(self) -> None: ...

    # Nested Types

    class QualSpectra:  # Class
        def __init__(self) -> None: ...

        DetailsArray: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Controls.SpectrumPlot.SpectrumPlotControl.QualSpectraDetails
        ]

    class QualSpectraDetails:  # Class
        def __init__(self) -> None: ...

        CollisionEnergy: Optional[float]
        FragmentorVoltage: Optional[float]
        FxData: (
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Controls.SpectrumPlot.SpectrumPlotControl.QualSpectraFxData
        )
        InstrumentType: str
        IonPolarity: Optional[Agilent.MassSpectrometry.DataAnalysis.IonPolarity]
        IonizationMode: Optional[Agilent.MassSpectrometry.DataAnalysis.IonizationMode]
        RetentionTime: Optional[float]
        ScanType: Optional[Agilent.MassSpectrometry.DataAnalysis.MSScanType]
        SelectedMz: Optional[float]
        name: str

    class QualSpectraFxData:  # Class
        def __init__(self) -> None: ...

        Points: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Controls.SpectrumPlot.SpectrumPlotControl.QualSpectraFxDataPoint
        ]

    class QualSpectraFxDataPoint:  # Class
        def __init__(self) -> None: ...

        i: int
        x: float
        y: float

class SpectrumPlotPane(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    TitledPanel,
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
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

    SpectrumPlotControl: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Controls.SpectrumPlot.SpectrumPlotControl
    )  # readonly
