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

from . import ILibrary, LibraryDataSet
from .MFS import MolecularFormula

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Exactify

class AmbiguousPeakResolutionForm(
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
    def __init__(
        self,
        peakMapRecord: Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakMappingRecord,
    ) -> None: ...

    IsPeakDeleted: bool  # readonly
    IsSelectionModified: bool  # readonly
    SelectedCharge: int  # readonly
    SelectedFragment: MolecularFormula  # readonly

class DefaultEventManipulator(
    Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    System.IDisposable,
    Agilent.MassSpectrometry.GUI.Plot.DefaultEventManipulatorBase,
):  # Class
    def __init__(
        self, context: Agilent.MassSpectrometry.EventManipulating.EventContext
    ) -> None: ...
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseMove(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...

class DeletePeakDialog(
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
    def __init__(
        self, peak: Agilent.MassSpectrometry.DataAnalysis.Exactify.ExactMassIon
    ) -> None: ...

class ExactMassIon:  # Class
    Abundance: float  # readonly
    Charge: int  # readonly
    FragmentFinder: (
        Agilent.MassSpectrometry.DataAnalysis.Exactify.FragmentFindingAlgorithm
    )  # readonly
    IsAmbiguous: bool  # readonly
    MZ: float  # readonly
    MzDeltaPpm: float  # readonly
    ParentFormula: MolecularFormula  # readonly
    RelativeAbundance: float  # readonly
    SelectedFragment: MolecularFormula  # readonly
    SourceMz: float  # readonly

class Exactify:  # Class
    @overload
    def __init__(
        self,
        library: ILibrary,
        exParams: Agilent.MassSpectrometry.DataAnalysis.Exactify.ExactifyParams,
    ) -> None: ...
    @overload
    def __init__(self, library: ILibrary, sessionFilePath: str) -> None: ...

    ErrorMessage: str  # readonly
    ExactMassLibrary: ILibrary  # readonly
    ExactifyParams: (
        Agilent.MassSpectrometry.DataAnalysis.Exactify.ExactifyParams
    )  # readonly
    IsCancelled: bool  # readonly
    IsModified: bool  # readonly
    IsRestored: bool  # readonly
    NumSpectraProcessed: int  # readonly
    SourceLibrary: ILibrary  # readonly

    def SaveExactMassLibrary(self) -> None: ...
    def RunLibrary(self) -> None: ...
    def SaveSession(self, sessionFilePath: str) -> None: ...
    def GetSpectrumMappingRecord(
        self, spectrum: LibraryDataSet.SpectrumRow
    ) -> Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumMappingRecord: ...
    def DeleteSpectrumPeak(
        self,
        peakMapRecord: Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakMappingRecord,
    ) -> bool: ...
    def GetMzUniquenessCount(self, mz: float) -> int: ...
    def SetSelectedFragment(
        self,
        peakMapRecord: Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakMappingRecord,
        selectedFragment: MolecularFormula,
        charge: int,
    ) -> bool: ...
    def CleanUp(self) -> None: ...
    def RestoreSession(self, sessionFilePath: str) -> None: ...
    def RunSpectrum(self, spectrumIndex: int) -> None: ...
    def IsExactSpectrumModified(self, spectrumIndex: int) -> bool: ...
    def RunNewCompounds(self) -> None: ...
    def RestoreDeletedPeak(
        self,
        peakMapRecord: Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakMappingRecord,
    ) -> bool: ...
    def Cancel(self) -> None: ...

    LibraryProcessed: (
        Agilent.MassSpectrometry.DataAnalysis.Exactify.LibraryProcessedEventHandler
    )  # Event
    SpectrumProcessed: (
        Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumProcessedEventHandler
    )  # Event

class ExactifyLog:  # Class
    @staticmethod
    def GetCompoundName(compound: LibraryDataSet.CompoundRow) -> str: ...

class ExactifyParams:  # Class
    def __init__(self) -> None: ...

    AllowMultiplyChargedIons: bool
    DisableLogging: bool
    KeepAmbiguouslyMappedIons: bool
    LogFilePath: str
    MaxIonsPerSpectrum: int
    MinMzDelta: float
    MinRelativeAbundance: float
    MzDeltaPpm: float
    OutputLibraryPath: str
    UseChemSpider: bool
    Weighting: Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakWeighting

    def GetMzDelta(self, mz: float) -> float: ...

class ExactifySession:  # Class
    def __init__(
        self,
        library: ILibrary,
        exactMassLibrary: ILibrary,
        exParams: Agilent.MassSpectrometry.DataAnalysis.Exactify.ExactifyParams,
        results: Agilent.MassSpectrometry.DataAnalysis.Exactify.LibraryMappingRecord,
        log: Agilent.MassSpectrometry.DataAnalysis.Exactify.ExactifyLog,
    ) -> None: ...
    def Restore(
        self,
        sessionFilePath: str,
        owner: Agilent.MassSpectrometry.DataAnalysis.Exactify.Exactify,
    ) -> None: ...
    def Save(self, sessionFilePath: str) -> None: ...

class FindSpectrumDialog(
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
    def __init__(
        self, mainForm: Agilent.MassSpectrometry.DataAnalysis.Exactify.MainForm
    ) -> None: ...

class FragmentFindingAlgorithm(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ChemSpider: (
        Agilent.MassSpectrometry.DataAnalysis.Exactify.FragmentFindingAlgorithm
    ) = ...  # static # readonly
    FragmentGenerator: (
        Agilent.MassSpectrometry.DataAnalysis.Exactify.FragmentFindingAlgorithm
    ) = ...  # static # readonly

class LibraryChangedDialog(
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
    def __init__(self, exit: bool) -> None: ...

class LibraryMappingRecord:  # Class
    ...

class LibraryProcessedEventArgs(System.EventArgs):  # Class
    ExactMassLibrary: ILibrary  # readonly
    SourceLibrary: ILibrary  # readonly

class LibraryProcessedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.Exactify.LibraryProcessedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.Exactify.LibraryProcessedEventArgs,
    ) -> None: ...

class MainForm(
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

class MultipleCandidateFragments:  # Class
    CandidateFragmentList: System.Collections.Generic.List[MolecularFormula]  # readonly
    Charge: int  # readonly
    Mass: float  # readonly
    MassRange: float  # readonly
    ParentFormula: MolecularFormula  # readonly
    SelectedFragment: MolecularFormula  # readonly
    SourceMZ: float  # readonly

    def Contains(self, fragment: MolecularFormula) -> bool: ...

class ParametersForm(
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

class ProgressDlg(
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
    def __init__(
        self,
        parent: Agilent.MassSpectrometry.DataAnalysis.Exactify.MainForm,
        exactify: Agilent.MassSpectrometry.DataAnalysis.Exactify.Exactify,
        numSpectra: int,
    ) -> None: ...

class SpectrumMappingRecord:  # Class
    CompoundFormula: MolecularFormula  # readonly
    NumProcessedPeaks: int  # readonly
    SpectrumRow: LibraryDataSet.SpectrumRow  # readonly

    def GetMappedExactMzValues(self) -> System.Collections.Generic.List[float]: ...
    def GetMappedSourceMzValues(self) -> System.Collections.Generic.List[float]: ...
    def GetPeakMappingRecordByExactMz(
        self, exactMz: float
    ) -> Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakMappingRecord: ...
    def GetPeakMappingRecords(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakMappingRecord
    ]: ...
    def GetPeakMappingRecord(
        self, mz: float
    ) -> Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakMappingRecord: ...

class SpectrumPeakMappingRecord:  # Class
    AutoSelectedExactMassIon: (
        Agilent.MassSpectrometry.DataAnalysis.Exactify.ExactMassIon
    )  # readonly
    ExactMassIon: (
        Agilent.MassSpectrometry.DataAnalysis.Exactify.ExactMassIon
    )  # readonly
    IsManuallySelected: bool  # readonly
    IsMapped: bool  # readonly
    IsMappedToUniqueFragment: bool  # readonly
    MultipleCandidateFragmentsCount: int  # readonly
    NoCandidateFragmentsCount: int  # readonly
    NoFragmentsInRangeCount: int  # readonly
    PeakDeleted: bool
    SourceMZ: float  # readonly
    SpectrumMappingRecord: (
        Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumMappingRecord
    )  # readonly

    def GetCandidateFragments(
        self, charge: int
    ) -> System.Collections.Generic.List[MolecularFormula]: ...
    def GetMultipleCandidateFragments(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Exactify.MultipleCandidateFragments
    ]: ...

class SpectrumPeakWeighting(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    EqualWeight: (
        Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakWeighting
    ) = ...  # static # readonly
    Mass: Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakWeighting = (
        ...
    )  # static # readonly
    Mass2: Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakWeighting = (
        ...
    )  # static # readonly
    Mass3: Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumPeakWeighting = (
        ...
    )  # static # readonly

class SpectrumProcessedEventArgs(System.EventArgs):  # Class
    SpectrumIndex: int  # readonly
    SpectrumRow: LibraryDataSet.SpectrumRow  # readonly

class SpectrumProcessedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumProcessedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        args: Agilent.MassSpectrometry.DataAnalysis.Exactify.SpectrumProcessedEventArgs,
    ) -> None: ...
