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

from . import ComponentHitID
from .Model import IUIContext
from .ScriptIF import IUIState

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools

class AnalysisDialog(
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
    def DeconvoluteSamples(
        self,
        samples: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
        reanalyze: bool,
    ) -> None: ...
    def AnalyzeAll(self, reanalyze: bool) -> None: ...
    def TargetMatchSamples(
        self,
        samples: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
        reanalyze: bool,
    ) -> None: ...
    def AnalyzeSamples(
        self,
        samples: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
        reanalyze: bool,
    ) -> None: ...
    def DeconvoluteAll(self, reanalyze: bool) -> None: ...
    def IdentifySamples(
        self,
        samples: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
        reanalyze: bool,
    ) -> None: ...
    def TargetMatchAll(self, reanalyze: bool) -> None: ...
    def IdentifyAll(self, reanalyze: bool) -> None: ...
    def BlankSubtractSamples(
        self,
        samples: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
        reanalyze: bool,
    ) -> None: ...
    def Cancel(self) -> None: ...
    def BlankSubtractAll(self, reanalyze: bool) -> None: ...

class AnalysisProgressDataSet(
    System.IDisposable,
    System.ComponentModel.ISupportInitializeNotification,
    System.IServiceProvider,
    System.Data.DataSet,
    System.Xml.Serialization.IXmlSerializable,
    System.Runtime.Serialization.ISerializable,
    System.ComponentModel.IListSource,
    System.ComponentModel.ISupportInitialize,
    System.ComponentModel.IComponent,
):  # Class
    def __init__(self) -> None: ...

    Relations: System.Data.DataRelationCollection  # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleDataTable
    )  # readonly
    SchemaSerializationMode: System.Data.SchemaSerializationMode
    Tables: System.Data.DataTableCollection  # readonly

    @staticmethod
    def GetTypedDataSetSchema(
        xs: System.Xml.Schema.XmlSchemaSet,
    ) -> System.Xml.Schema.XmlSchemaComplexType: ...
    def Clone(self) -> System.Data.DataSet: ...

    # Nested Types

    class SampleDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRow
        ],
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        BatchIDColumn: System.Data.DataColumn  # readonly
        BlankSubtractionColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        DeconvolutionColumn: System.Data.DataColumn  # readonly
        IdentificationColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRow
        ): ...
        SampleIDColumn: System.Data.DataColumn  # readonly
        SampleNameColumn: System.Data.DataColumn  # readonly
        TargetMatchColumn: System.Data.DataColumn  # readonly

        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddSampleRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRow,
        ) -> None: ...
        @overload
        def AddSampleRow(
            self,
            BatchID: int,
            SampleID: int,
            SampleName: str,
            Deconvolution: float,
            Identification: float,
            BlankSubtraction: float,
            TargetMatch: float,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRow
        ): ...
        def FindByBatchIDSampleID(
            self, BatchID: int, SampleID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def NewSampleRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRow
        ): ...
        def RemoveSampleRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRow,
        ) -> None: ...

        SampleRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRowChangeEventHandler
        )  # Event
        SampleRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRowChangeEventHandler
        )  # Event
        SampleRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRowChangeEventHandler
        )  # Event
        SampleRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRowChangeEventHandler
        )  # Event

    class SampleRow(System.Data.DataRow):  # Class
        BatchID: int
        BlankSubtraction: float
        Deconvolution: float
        Identification: float
        SampleID: int
        SampleName: str
        TargetMatch: float

        def IsTargetMatchNull(self) -> bool: ...
        def IsIdentificationNull(self) -> bool: ...
        def SetIdentificationNull(self) -> None: ...
        def IsDeconvolutionNull(self) -> bool: ...
        def SetBlankSubtractionNull(self) -> None: ...
        def IsBlankSubtractionNull(self) -> bool: ...
        def IsSampleNameNull(self) -> bool: ...
        def SetDeconvolutionNull(self) -> None: ...
        def SetSampleNameNull(self) -> None: ...
        def SetTargetMatchNull(self) -> None: ...

    class SampleRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRow
        )  # readonly

    class SampleRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.AnalysisProgressDataSet.SampleRowChangeEvent,
        ) -> None: ...

class CompressResultsDialog(
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

class ExportComponentTableDialog(
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

    DestinationType: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.ExportDestinationType
    )
    ExportAllComponents: bool  # readonly
    NonHitAutoCompoundNames: bool  # readonly
    NonHitCompoundNameAddIndex: bool  # readonly
    NonHitCompoundNamePrefix: str  # readonly

class ExportDestinationType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Csv: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.ExportDestinationType
    ) = ...  # static # readonly
    Library: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.ExportDestinationType
    ) = ...  # static # readonly
    QuantMethod: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Tools.ExportDestinationType
    ) = ...  # static # readonly

class ExportQuantMethodDialog(
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
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

    DestinationPath: str
    IonMode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodFromLibraryIonMode
    NumQualifiers: int

class GenerateReport(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand
):  # Class
    def __init__(self) -> None: ...

    ActionString: str  # readonly
    Method: str
    Name: str  # readonly
    OutputPath: str

class LoadMethodDialog(
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

class ReportDialog(
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

    AllSamples: bool
    GenerateNow: bool
    Method: str
    OpenReportFolder: bool
    OutputPath: str
    StartQueueViewer: bool

    @staticmethod
    def GenerateDefaultOutputDirectory(
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        batchFolder: str,
        analysisFile: str,
    ) -> str: ...

class TargetCompoundsDialog(
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
    def __init__(self, uiContext: IUIContext) -> None: ...

    IsEditable: bool  # readonly

    @staticmethod
    def FindTargetCompoundByHit(
        dataFile: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataFileBase,
        hit: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.HitRow,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UnknownsAnalysisDataSet.TargetCompoundRow
    ): ...
    def InitBySample(self, batchID: int, sampleID: int) -> None: ...
    def AddISTDByHits(self, ids: List[ComponentHitID]) -> None: ...
    def AddISTDByHit(self, chid: ComponentHitID) -> None: ...

class ToolHandlerAnalyze(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def CompressResults(uiState: IUIState) -> None: ...

class ToolHandlerChromatogram(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerComponent(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerEdit(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerEicPeaks(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerExactMass(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
        objState: Any,
    ) -> None: ...
    def SetState(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
        objState: Any,
    ) -> None: ...

class ToolHandlerFile(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IDropDownHandler,
):  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def SaveAnalysis(uiState: IUIState) -> bool: ...
    @staticmethod
    def PushRecentAnaysisFile(path: str) -> None: ...
    @staticmethod
    def SetMaxRecentAnalysisFiles(max: int) -> None: ...
    @staticmethod
    def SaveAnalysisAs(
        uiState: IUIState, batchFolder: str, analysisFile: str
    ) -> bool: ...
    @staticmethod
    def RemoveRecentAnalysisFile(path: str) -> None: ...
    @staticmethod
    def GetRecentAnalysisFiles() -> List[str]: ...
    @staticmethod
    def OpenAnalysis(
        uiState: IUIState,
        batchFolder: str,
        fileName: str,
        revisionNumber: str,
        readOnly: bool,
    ) -> bool: ...
    @overload
    @staticmethod
    def NewAnalysis(uiState: IUIState) -> None: ...
    @overload
    @staticmethod
    def NewAnalysis(
        uiState: IUIState, batchFolder: str, fileName: str, auditTrail: bool
    ) -> bool: ...
    @staticmethod
    def OpenAnalysisFromPath(
        state: IUIState, file: str, readOnly: bool
    ) -> System.Exception: ...
    @staticmethod
    def CloseAnalysis(uiState: IUIState) -> bool: ...

class ToolHandlerHelp(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerIonPeaks(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerReport(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerSample(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerScript(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...
    def Execute(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
        objUiState: Any,
    ) -> None: ...
    def SetState(
        self,
        tool: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.ITool,
        uiState: Any,
    ) -> None: ...

class ToolHandlerSpectrum(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolHandlerTools(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IDropDownHandler,
):  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def RunScript(uiState: IUIState, scriptFiles: List[str]) -> None: ...

class ToolHandlerView(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ToolsUtils:  # Class
    @overload
    @staticmethod
    def ExecuteCommand(
        parent: System.Windows.Forms.IWin32Window,
        cmd: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    ) -> bool: ...
    @overload
    @staticmethod
    def ExecuteCommand(
        parent: System.Windows.Forms.IWin32Window,
        cmd: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
        ret: Any,
    ) -> bool: ...
