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

from . import (
    BatchAttributes,
    ChromatogramPeakLabelType,
    CompoundIdentificationParams,
    GridExportMode,
    InstrumentType,
    INumericCustomFormat,
    INumericFormat,
    PlotTitleElement,
    PresentationState,
    QuantitationDataSet,
)
from .Compliance import IAuditTrail, ICompliance
from .Grid import GridControlBase
from .UIScriptIF import IAddInManager, IExportPlotParameters, IUIState
from .UnknownsMethod import MethodControl

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs

class AddinsDialog(
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
    def __init__(self, uiState: IUIState, manager: IAddInManager) -> None: ...

class AuditTrailDialog(
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
    def __init__(self, auditTrail: IAuditTrail) -> None: ...

class AuditTrailGrid(
    Infragistics.Win.IUltraControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    Infragistics.Win.IUIElementProvider,
    Infragistics.Win.IUltraControlElement,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISupportInitialize,
    Infragistics.Shared.Serialization.ICodeDomSerializable,
    Infragistics.Win.UIAutomation.IProvideUIAutomation,
    System.Windows.Forms.IWin32Window,
    Infragistics.Win.ISupportPresets,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    Infragistics.Win.AppStyling.ISupportAppStyling,
    Infragistics.Win.IControlElementEventProcessor,
    Infragistics.Win.IUIElementTextProvider,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    Infragistics.Win.CalcEngine.IUltraCalcParticipant,
    System.ComponentModel.ISynchronizeInvoke,
    Infragistics.Win.IValidatorClient,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    Agilent.MassHunter.Quantitative.UIModel.IGridControl,
    Infragistics.Win.Touch.ISupportTouchMetrics,
    System.ComponentModel.IComponent,
    Infragistics.Win.ISelectionManager,
    Infragistics.Win.UltraWinGrid.Design.IGridDesignInfo,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    Infragistics.Win.Touch.IGestureConsumer,
    Infragistics.Shared.IUltraLicensedComponent,
    GridControlBase,
    System.Windows.Forms.IBindableComponent,
    System.IDisposable,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    Infragistics.Win.AutoEditMode.IAutoEditMode,
):  # Class
    def __init__(self) -> None: ...

class AverageQualifierRatiosDialog(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.SelectDataRowsDialog,
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

    CalsChecked: bool
    QCsChecked: bool

class AverageRetentionTimeDialog(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.SelectDataRowsDialog,
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

    Cals: bool
    Qcs: bool
    UseWeightings: bool
    Weight: float

class BatchAttributesDialog(
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
    def Initialize(
        self,
        instrument: InstrumentType,
        attrs: BatchAttributes,
        numericFormat: INumericFormat,
    ) -> None: ...

class BatchFileDialog(System.IDisposable):  # Class
    def __init__(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.BatchFileDialogMode,
    ) -> None: ...

    AllowAuditTrail: bool
    AllowReadonly: bool
    AuditTrail: bool
    AuditTrailCheckboxEnabled: bool
    BatchFile: str  # readonly
    BatchFolder: str  # readonly
    HelpFile: str
    HelpId: int
    InitialDir: str
    Readonly: bool
    Title: str

    def Dispose(self) -> None: ...
    def ShowDialog(self, parent: System.Windows.Forms.IWin32Window) -> bool: ...

class BatchFileDialogMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    New: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.BatchFileDialogMode
    ) = ...  # static # readonly
    Open: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.BatchFileDialogMode
    ) = ...  # static # readonly
    SaveAs: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.BatchFileDialogMode
    ) = ...  # static # readonly

class ChooseSpeciesControl(
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

    TextBoxText: str

    def GetSelectedSpecies(self) -> Iterable[str]: ...
    def GetAvailableSpecies(self) -> Iterable[str]: ...
    def SetAvailableSpecies(self, species: Iterable[str]) -> None: ...
    def SetSelectedSpecies(self, species: Iterable[str]) -> None: ...

    ValidateNewSpecies: System.ComponentModel.CancelEventHandler  # Event

class ChooseSpeciesDialog(
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
    def GetSelectedSpecies(self) -> Iterable[str]: ...
    def SetSelectedSpecies(self, species: List[str]) -> None: ...

class DirectoriesDialog(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    AllowMultiSelect: bool
    Directories: str  # readonly
    DirectoryMustExist: bool
    Extension: str
    FileFilter: str
    HelpFile: str
    HelpTopicId: int
    InitialDir: str
    Readonly: bool
    ReadonlyCheckbox: bool
    Title: str

    def Dispose(self) -> None: ...
    def ShowDialog(self, parent: System.Windows.Forms.IWin32Window) -> bool: ...

class ExportFileDialog(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    ExportMode: GridExportMode
    FileName: str  # readonly
    Filter: str
    FilterIndex: int
    HelpFile: str
    HelpTopicId: int
    InitialDir: str
    OpenFile: bool
    Title: str

    def Dispose(self) -> None: ...
    def ShowDialog(self, parent: System.Windows.Forms.IWin32Window) -> bool: ...

class ExportPlotDialog:  # Class
    @staticmethod
    def ShowDialog(
        parent: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        parameters: IExportPlotParameters,
    ) -> bool: ...

class LibraryDialog(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogBase,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        dialogType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogType,
    ) -> None: ...

    AllowNistLibraries: bool
    ExtraFileFilter: str

    def AllowReferenceLibrary(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class LibraryMethodDialog(
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
    def __init__(self, compliance: ICompliance) -> None: ...

    MethodControl: MethodControl  # readonly
    MethodPath: str  # readonly

    def InitNew(self, referenceSampleFilePath: str) -> None: ...
    def Initialize(
        self, methodPath: str, revisionNumber: str, referenceSampleFilePath: str
    ) -> None: ...

class LogonUserDialog(
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

    Compliance: ICompliance
    Domain: str
    Password: System.Security.SecureString  # readonly
    User: str
    ValidationMode: bool

    Cancel: System.ComponentModel.CancelEventHandler  # Event
    Logon: System.ComponentModel.CancelEventHandler  # Event

class MatrixOverrideControl(
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
    def SaveTo(self, writer: System.IO.TextWriter) -> bool: ...
    def Initialize(self, pstate: PresentationState, value_: str) -> None: ...
    def ValidateItems(self) -> bool: ...

class MethodFileDialog(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogBase,
):  # Class
    @overload
    def __init__(self, saveAs: bool, individualFileExtension: str) -> None: ...
    @overload
    def __init__(self, saveAs: bool, individualFileExtensions: List[str]) -> None: ...

class NumberFormatColumn:  # Class
    def __init__(
        self, name: str, displayText: str, category: str, format: INumericCustomFormat
    ) -> None: ...

    Category: str  # readonly
    CategoryDisplayText: str  # readonly
    DisplayText: str  # readonly
    Format: INumericCustomFormat
    FormatPattern: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    )
    Name: str  # readonly
    Precision: Optional[int]

class NumberFormatControl(
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

    Formats: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatColumn
    ]
    ReadOnly: bool

    def InvalidateContent(self) -> None: ...
    def SetDateTimeMode(self) -> None: ...
    def SetFormat(
        self,
        column: str,
        pattern: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern,
        precision: Optional[int],
    ) -> None: ...
    def PerformAutoResizeColumns(self) -> None: ...
    def SetNumberMode(self) -> None: ...

    ValueChanged: System.EventHandler  # Event

class NumberFormatDateTimeColumnDialog(
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
    def __init__(self, type: System.Type) -> None: ...

    Format: str

    Apply: System.ComponentModel.CancelEventHandler  # Event

class NumberFormatDialog(
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
    def __init__(self, uiState: IUIState) -> None: ...

    Formats: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatColumn
    ]

    def Initialize(self, instrumentType: InstrumentType) -> None: ...

class NumberFormatPattern(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DateTime: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ) = ...  # static # readonly
    Exponential: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ) = ...  # static # readonly
    FixedPoint: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ) = ...  # static # readonly
    General: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ) = ...  # static # readonly
    SignificantFigures: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ) = ...  # static # readonly

class NumberFormatSingleColumnControl(
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

    DefaultFormatPattern: Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ]
    DefaultPrecision: Optional[int]
    FormatPattern: Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ]
    Precision: Optional[int]

    def SetDefault(self) -> None: ...

class NumberFormatSingleColumnDialog(
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

    DefaultFormatPattern: Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ]
    DefaultPrecision: Optional[int]
    FormatPattern: Optional[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.NumberFormatPattern
    ]
    Precision: Optional[int]

    Apply: System.ComponentModel.CancelEventHandler  # Event

class PeakColorsDialog(
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

    Accepted: System.Drawing.Color
    Alternate: System.Drawing.Color
    Inspected: System.Drawing.Color
    ManualIntegrated: System.Drawing.Color
    Rejected: System.Drawing.Color

class PeakLabelsControl(
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

    IsDirty: bool  # readonly
    ShowLabelNames: bool  # readonly
    ShowUnits: bool  # readonly

    def Initialize(
        self,
        instrumentType: InstrumentType,
        types: List[ChromatogramPeakLabelType],
        showLabelNames: bool,
        showUnits: bool,
    ) -> None: ...
    def ClearDirty(self) -> None: ...
    def GetPeakLabelTypes(self) -> List[ChromatogramPeakLabelType]: ...

    PeakLabelsChanged: System.EventHandler  # Event

class PeakLabelsDialog(
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

    PeakLabelsControl: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.PeakLabelsControl
    )  # readonly

class PlotTitleElementControl(
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

    ShowDefaultTitles: bool

    def SetValues(
        self,
        showDefaultTitle: bool,
        availableElements: List[PlotTitleElement],
        elements: List[PlotTitleElement],
    ) -> None: ...
    def GetElements(self) -> List[PlotTitleElement]: ...

class PlotTitleElementDialog(
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

    ShowDefaultTitles: bool

    @overload
    def SetValues(
        self, showDefaultTitle: bool, elements: List[PlotTitleElement]
    ) -> None: ...
    @overload
    def SetValues(
        self,
        showDefaultTitle: bool,
        availableElements: List[PlotTitleElement],
        elements: List[PlotTitleElement],
    ) -> None: ...
    def GetElements(self) -> List[PlotTitleElement]: ...

class RTCalibrationDialog(
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
    def __init__(self, compliance: ICompliance) -> None: ...

    BatchFile: str
    BatchFolder: str
    InitialBatchFolder: str
    InitialLibraryFolder: str
    Library: str
    Output: str

class ReportMethodFileDialog(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogBase,
):  # Class
    def __init__(
        self,
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogType,
        isUnknowns: bool,
    ) -> None: ...

class SampleDirectoriesDialog(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.DirectoriesDialog,
    System.IDisposable,
):  # Class
    def __init__(self) -> None: ...

class SelectDataRowsDialog(
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

    DataView: System.Data.DataView  # readonly
    LabelText: str
    MultiSelect: bool

    def GetSelectedRows(self) -> List[System.Data.DataRow]: ...
    def ClearColumns(self) -> None: ...
    def SetDataView(self, view: System.Data.DataView) -> None: ...
    @overload
    def AddColumn(self, property: str, caption: str) -> None: ...
    @overload
    def AddColumn(
        self, property: str, caption: str, format: INumericCustomFormat
    ) -> None: ...
    def SelectRows(self, condition: str, clearSelection: bool) -> None: ...

class SelectSampleFoldersDialog(
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
    @overload
    def __init__(self, compliance: ICompliance) -> None: ...
    @overload
    def __init__(
        self, compliance: ICompliance, instrumentType: InstrumentType
    ) -> None: ...

    BatchDataTable: QuantitationDataSet.BatchDataTable  # readonly
    BatchFolder: str
    CopySampleEnabled: bool
    MultipleSelection: bool

    def SetSelectedSampleFolders(self, folders: List[str]) -> None: ...
    def GetSelectedSampleFolders(self) -> List[str]: ...
    def InitSamplesInBatch(self, samples: List[str]) -> None: ...
    def GetSamplesInBatch(self) -> List[str]: ...
    def SelectAllSamples(self) -> None: ...

    Initialized: System.EventHandler  # Event

class SelectedMzMarkerDialog(
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

    Color: Optional[System.Drawing.Color]
    Fill: bool
    Size: Optional[int]

class SetupReferenceLibraryDialog(
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
    def __init__(self, uiState: IUIState) -> None: ...

class ShellFileDialogBase(System.IDisposable):  # Class
    def __init__(
        self,
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogType,
    ) -> None: ...

    DefaultExtension: str
    DialogType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogType
    )  # readonly
    EnsurePathExists: bool
    InitialDirectory: str
    Multiselect: bool
    OverwritePrompt: bool
    PathName: str  # readonly
    Readonly: bool
    ReadonlyCheckbox: bool
    Title: str

    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...
    def Dispose(self) -> None: ...
    def AddFilter(
        self,
        name: str,
        filters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogFilter
        ],
    ) -> None: ...
    def ClearFilters(self) -> None: ...

    SaveAsFile: System.ComponentModel.CancelEventHandler  # Event
    SaveAsFolder: System.ComponentModel.CancelEventHandler  # Event

class ShellFileDialogFilter:  # Class
    def __init__(self, extensions: List[str], isFolder: bool) -> None: ...

    Extensions: List[str]
    IsFolder: bool

class ShellFileDialogType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    New: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogType
    ) = ...  # static # readonly
    Open: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogType
    ) = ...  # static # readonly
    SaveAs: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.ShellFileDialogType
    ) = ...  # static # readonly

class ShiftRetentionTimeDialog(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.SelectDataRowsDialog,
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

    AbsoluteShift: float
    RelativeShift: float

class SystemInfoDialog(
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
    @staticmethod
    def ShowSystemInfo(parent: System.Windows.Forms.IWin32Window) -> None: ...

class SystemInfoItem:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, fileVersionInfo: System.Diagnostics.FileVersionInfo) -> None: ...
    @overload
    def __init__(
        self,
        fileVersionInfo: System.Diagnostics.FileVersionInfo,
        assembly: System.Reflection.Assembly,
    ) -> None: ...

    AssemblyConfiguration: str  # readonly
    AssemblyCulture: str  # readonly
    AssemblyTitle: str  # readonly
    ComVisible: Optional[bool]  # readonly
    Comments: str  # readonly
    CompanyName: str  # readonly
    FileDescription: str  # readonly
    FileVersion: str  # readonly
    Guid: str  # readonly
    InternalName: str  # readonly
    IsDebug: Optional[bool]  # readonly
    IsPatched: Optional[bool]  # readonly
    IsPrivateBuild: Optional[bool]  # readonly
    IsSpecialBuild: Optional[bool]  # readonly
    Language: str  # readonly
    LegalCopyright: str  # readonly
    LegalTrademarks: str  # readonly
    Location: str  # readonly
    Name: str  # readonly
    PrivateBuild: str  # readonly
    ProductName: str  # readonly
    ProductVersion: str  # readonly
    SpecialBuild: str  # readonly

class SystemInfoItemCollection(
    Sequence[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.SystemInfoItem],
    System.ComponentModel.IRaiseItemChangedEvents,
    System.ComponentModel.BindingList[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.SystemInfoItem
    ],
    List[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.SystemInfoItem],
    System.ComponentModel.IBindingList,
    System.ComponentModel.ICancelAddNew,
    Iterable[Agilent.MassSpectrometry.DataAnalysis.Quantitative.Dialogs.SystemInfoItem],
    System.ComponentModel.IComponent,
    List[Any],
    Iterable[Any],
    Sequence[Any],
    System.IDisposable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, container: System.ComponentModel.IContainer) -> None: ...

    SynchronizeInvoke: System.ComponentModel.ISynchronizeInvoke

    def Dispose(self) -> None: ...

class UnknownsAnalysisParametersDialog(
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

    ComponentPerceptionParams: (
        Agilent.MassSpectrometry.DataAnalysis.ComponentPerceptionParams
    )
    CompoundIdentificationParams: CompoundIdentificationParams
    HideDisabledPage: bool
    LibrarySearchParams: Agilent.MassSpectrometry.DataAnalysis.LibrarySearchParams
    SeparationTechniqueForDefault: Optional[
        Agilent.MassSpectrometry.DataAnalysis.SeparationTechnique
    ]

    def SelectComponentPerceptionTab(self) -> None: ...
    def SelectCompoundIdentificationTab(self) -> None: ...
    def SelectLibrarySearchTab(self) -> None: ...

class ValidateUserDialog(
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

    Compliance: ICompliance
    Message: str

class ValidateUserReasonDialog(
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

    ActionString: str
    Compliance: ICompliance
    MaxTrial: int
    ReasonEnabled: bool
    ValidateUserEnabled: bool
