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

# Discovered Generic TypeVars:
T = TypeVar("T")
TFile = TypeVar("TFile")
TItem = TypeVar("TItem")
from . import (
    ProgressEventArgs,
    RowID,
    RowsEventArgs,
    SampleRowID,
    UnknownsAnalysisDataSet,
)
from .DataFile import DataFileBase

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command

class AddComponent(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameter: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AddComponentParameter,
        addIonPeakParameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AddIonPeakParameter
        ],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class AddComponentParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICodeDomParameter,
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly
    Values: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]  # readonly

    def GetActionString(self) -> str: ...
    def GetExpression(self) -> System.CodeDom.CodeExpression: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class AddDeconvolutionMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SetMethods,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

class AddDeconvolutionMethodParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.DeconvolutionMethodParameterBase
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int
    ) -> None: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class AddHit(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameter: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AddHitParameter,
        bestHit: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class AddHitParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICodeDomParameter,
):  # Class
    @overload
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
        emparams: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.ExactMassColumnValuesParameter
        ],
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    ExactMassParameters: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.ExactMassColumnValuesParameter
    ]  # readonly
    HitID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly
    Values: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]  # readonly

    def GetActionString(self) -> str: ...
    def GetExpression(self) -> System.CodeDom.CodeExpression: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class AddIonPeakParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICodeDomParameter,
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    IonPeakID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly
    Values: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]  # readonly

    def GetActionString(self) -> str: ...
    def GetExpression(self) -> System.CodeDom.CodeExpression: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class AddLibrarySearchMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SetMethods,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

class AddLibrarySearchMethodParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.LibrarySearchMethodParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> None: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class AddManualComponent(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AddManualComponentParameter
        ],
        blankComponentID: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.ComponentRowIDParameter,
    ) -> None: ...

    BlankComponentID: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.ComponentRowIDParameter
    )
    Reversible: bool  # readonly

    def Redo(self) -> Any: ...
    def Add(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        start: float,
        end: float,
    ) -> None: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...

class AddManualComponentParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICodeDomParameter,
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        start: float,
        end: float,
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    End: float  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly
    Start: float  # readonly

    def GetExpression(self) -> System.CodeDom.CodeExpression: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class AddSamples(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        samplePathNames: List[str],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class AddTargetCompoundParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.TargetCompoundParameterBase
):  # Class
    def __init__(self, batchID: int, sampleID: int, compoundID: int) -> None: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class AnalysisMessage:  # Class
    def __init__(
        self,
        step: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisProgressStep,
        type: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisMessageType,
        rowID: SampleRowID,
        message: str,
    ) -> None: ...

    Message: str  # readonly
    MessageType: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisMessageType
    )  # readonly
    RowID: SampleRowID  # readonly
    Step: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisProgressStep
    )  # readonly

class AnalysisMessageEventArgs(System.EventArgs):  # Class
    def __init__(
        self,
        message: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisMessage,
    ) -> None: ...

    Message: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisMessage
    )  # readonly

class AnalysisMessageType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Error: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisMessageType
    ) = ...  # static # readonly
    Information: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisMessageType
    ) = ...  # static # readonly
    Warning: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisMessageType
    ) = ...  # static # readonly

class AnalysisProgressChangedEventArgs(System.EventArgs):  # Class
    def __init__(
        self,
        totalSteps: int,
        currentStep: int,
        step: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisProgressStep,
        sample: SampleRowID,
    ) -> None: ...

    CurrentStep: int  # readonly
    Sample: SampleRowID  # readonly
    Step: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisProgressStep
    )  # readonly
    TotalSteps: int  # readonly

class AnalysisProgressStep(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Deconvoluting: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisProgressStep
    ) = ...  # static # readonly
    Identifying: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisProgressStep
    ) = ...  # static # readonly
    MatchingTarget: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisProgressStep
    ) = ...  # static # readonly
    SubtractingBlank: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisProgressStep
    ) = ...  # static # readonly

class AnalysisState(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    BlankSubtracted: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisState
    ) = ...  # static # readonly
    Deconvoluted: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisState
    ) = ...  # static # readonly
    Identified: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisState
    ) = ...  # static # readonly
    Idle: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisState
    ) = ...  # static # readonly
    TargetMatched: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisState
    ) = ...  # static # readonly

class AnalyzeAll(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        reanalyze: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class AnalyzeSamples(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        samples: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
        reanalyze: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        reanalyze: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class ApplicationSettings(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationElementSectionBase
):  # Class
    def __init__(self) -> None: ...

    DefaultDeconvolutionWindowSizeFactors: List[float]  # readonly
    DefaultIntegrator: str  # readonly
    DefaultLibraryPath: str  # readonly
    DefaultMaxNumStoredIonPeaks: int  # readonly
    MaxDatabaseSize: int  # readonly
    MaxDegreeOfParallelism: int  # readonly
    UseIndexedDataAccess: bool  # readonly
    UsePerSampleStorage: bool  # readonly

class AuditTrail(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IAuditTrail
):  # Class
    AlwaysAuditTrail: bool  # readonly
    IsAuditTrailing: bool  # readonly
    IsReadOnly: bool  # readonly

    def AddEntry(
        self,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
        exception: System.Exception,
    ) -> None: ...
    def SaveAuditTrail(self) -> None: ...
    def UnlockAuditTrail(self) -> None: ...
    def LockAuditTrail(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet
    ): ...

class AuxiliaryMethodColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class BlankSubtractAll(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        reanalyze: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class BlankSubtractSamples(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        samples: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
        reanalyze: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        reanalyze: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class BlankSubtractionMethodColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        blankSubtractionMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    BlankSubtractionMethodID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class ClearAllResults(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class ClearResults(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        samples: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class CloseAnalysis(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class CmdConfiguration:  # Class
    ApplicationSettings: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.ApplicationSettings
    )  # readonly
    Initialized: bool  # readonly
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CmdConfiguration
    )  # static # readonly

    def Initialize(self) -> None: ...

class CommandBase(
    Agilent.MassSpectrometry.CommandModel.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    ActionString: str  # readonly
    Name: str  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class CommandContext(
    Agilent.MassSpectrometry.CommandModel.Model.ICommandHistory,
    Agilent.MassSpectrometry.CommandModel.CommandHistory,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        numericFormat: Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericFormat,
    ) -> None: ...

    AnalysisResultsFolder: str = ...  # static # readonly

    AnalysisFileName: str  # readonly
    AuditTrail: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IAuditTrail
    )  # readonly
    BatchFolder: str  # readonly
    Compliance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance
    )  # readonly
    DataFile: DataFileBase  # readonly
    IsCommandRunning: bool  # readonly
    IsDirty: bool  # readonly
    LoadedMethodPath: str
    NumericFormat: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericFormat
    )  # readonly
    SampleCount: int  # readonly

    def OnAnalysisOpening(self, e: System.EventArgs) -> None: ...
    def SaveAnalysis(self) -> None: ...
    def SaveAnalysisAs(self, batchFolder: str, fileName: str) -> None: ...
    def Invoke(
        self, cmd: Agilent.MassSpectrometry.CommandModel.Model.ICommand
    ) -> Any: ...
    def NewAnalysis(
        self, batchFolder: str, fileName: str, auditTrail: bool
    ) -> None: ...
    def AnalysisNeedsConversion(self, batchFolder: str, fileName: str) -> bool: ...
    def OpenLibrary(
        self, librarySearchMethodRow: UnknownsAnalysisDataSet.LibrarySearchMethodRow
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.LibraryFile
    ): ...
    def IdentifySamples(self, samples: List[SampleRowID], reanalyze: bool) -> None: ...
    def AnalyzeSamples(self, samples: List[SampleRowID], reanalyze: bool) -> None: ...
    def TargetMatchAll(self, reanalyze: bool) -> None: ...
    def DeconvoluteAll(self, reanalyze: bool) -> None: ...
    def BlankSubtractAll(self, reanalyze: bool) -> None: ...
    def DeconvoluteSamples(
        self, samples: List[SampleRowID], reanalyze: bool
    ) -> None: ...
    def CompressResults(
        self,
        tasks: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CompressResultsTasks,
        abort: System.Threading.WaitHandle,
    ) -> None: ...
    def AbortAnalysis(self) -> None: ...
    def OpenSampleData(
        self, row: UnknownsAnalysisDataSet.SampleRow
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleDataFile
    ): ...
    @staticmethod
    def GetAnalysisInfo(
        file: str, table: UnknownsAnalysisDataSet.AnalysisDataTable
    ) -> None: ...
    def AnalyzeAll(self, reanalyze: bool) -> None: ...
    def TargetMatchSamples(
        self, samples: List[SampleRowID], reanalyze: bool
    ) -> None: ...
    def HasAccurateMass(self) -> bool: ...
    def IdentifyAll(self, reanalyze: bool) -> None: ...
    def BlankSubtractSamples(
        self, samples: List[SampleRowID], reanalyze: bool
    ) -> None: ...
    def OpenAnalysis(
        self,
        batchFolder: str,
        fileName: str,
        revisionNumber: str,
        readOnly: bool,
        abort: System.Threading.WaitHandle,
    ) -> None: ...
    def CloseAnalysis(self) -> None: ...

    AddSample: System.EventHandler[ProgressEventArgs]  # Event
    AnalysisClosed: System.EventHandler  # Event
    AnalysisClosing: System.EventHandler  # Event
    AnalysisEnd: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SamplesEventArgs
    ]  # Event
    AnalysisMessage: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisMessageEventArgs
    ]  # Event
    AnalysisNew: System.EventHandler  # Event
    AnalysisOpened: System.EventHandler  # Event
    AnalysisOpening: System.EventHandler  # Event
    AnalysisProgressChanged: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.AnalysisProgressChangedEventArgs
    ]  # Event
    AnalysisSaved: System.EventHandler  # Event
    AnalysisSaving: System.EventHandler  # Event
    AnalysisStart: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SamplesEventArgs
    ]  # Event
    ComponentChanged: System.EventHandler  # Event
    ComponentsHitsVisibleChanged: System.EventHandler[RowsEventArgs]  # Event
    ConvertProgress: System.EventHandler[ProgressEventArgs]  # Event
    DataCompressed: System.EventHandler  # Event
    ExactMassChanged: System.EventHandler  # Event
    FileProgress: System.EventHandler[ProgressEventArgs]  # Event
    HitChanged: System.EventHandler  # Event
    ImportQuantBatchProgressChanged: System.EventHandler[ProgressEventArgs]  # Event
    IonPeakChanged: System.EventHandler  # Event
    MethodChanged: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SamplesEventArgs
    ]  # Event
    MethodLoad: System.EventHandler  # Event
    PrimaryHitChange: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.PrimaryHitChangeEventArgs
    ]  # Event
    ResultsClear: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SamplesEventArgs
    ]  # Event
    SampleChanged: System.EventHandler  # Event
    SampleCountChanged: System.EventHandler  # Event

class CommandMethodUtils:  # Class
    @staticmethod
    def GetSampleInfo(pathName: str, values: Dict[str, Any]) -> bool: ...

class CommandParameterArray(
    Generic[T], Agilent.MassSpectrometry.CommandModel.Model.ICodeDomParameter
):  # Class
    def __init__(self, parameters: Iterable[T]) -> None: ...

class CommandParameterBase:  # Class
    RowID: RowID  # readonly

    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class ComponentColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class ComponentHitVisibleParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: Optional[int],
        visible: bool,
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    HitID: Optional[int]  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly
    Visible: bool  # readonly

    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class ComponentRowIDParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICodeDomParameter,
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int, componentID: int
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def GetExpression(self) -> System.CodeDom.CodeExpression: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class CompressResults(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        tasks: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CompressResultsTasks,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Abort(self) -> None: ...
    def GetParameters(self) -> List[Any]: ...

class CompressResultsTasks(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    RemoveInvisibleHitsComponents: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CompressResultsTasks
    ) = ...  # static # readonly
    RemoveNonBestHitComponents: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CompressResultsTasks
    ) = ...  # static # readonly
    RemoveNonHitComponents: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CompressResultsTasks
    ) = ...  # static # readonly
    RemoveNonPrimaryHits: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CompressResultsTasks
    ) = ...  # static # readonly

class DataFileBase(Generic[TItem], System.IDisposable):  # Class
    def Dispose(self) -> None: ...

class DataFileCache(Generic[TItem, TFile], System.IDisposable):  # Class
    def __init__(
        self,
        size: int,
        numericFormat: Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericFormat,
    ) -> None: ...
    def Dispose(self) -> None: ...

class DataFileItemBase(System.IDisposable):  # Class
    def Dispose(self) -> None: ...

class DeconvoluteAll(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        reanalyze: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class DeconvoluteSamples(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        samples: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
        reanalyze: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        reanalyze: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class DeconvolutionMethodColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.DeconvolutionMethodParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class DeconvolutionMethodParameterBase(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int
    ) -> None: ...

    BatchID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

class ExactMassColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        exactMassID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    ExactMassID: int  # readonly
    HitID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class HitColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    HitID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class HitRowIDParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    HitID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def GetExpression(self) -> System.CodeDom.CodeExpression: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class IdentificationMethodColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    IdentificationMethodID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class IdentifyAll(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        reanalyze: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class IdentifySamples(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        samples: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
        reanalyze: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        reanalyze: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class ImportQuantBatch(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchFolder: str,
        batchFile: str,
    ) -> None: ...

    ActionString: str  # readonly
    ActionStrings: List[str]  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class ImportQuantMethod(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        methodPath: str,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class ImportQuantMethodFromBatch(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.ImportQuantMethod,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchFolder: str,
        batchFile: str,
    ) -> None: ...

    ActionString: str  # readonly

class IonPeakColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    IonPeakID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class KeyValue:  # Struct
    def __init__(self, key: str, value_: Any) -> None: ...

    Key: str  # readonly
    Value: Any  # readonly

    def GetHashCode(self) -> int: ...
    @overload
    def Equals(
        self,
        kv: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class LibraryFile(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.DataFileBase[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.LibraryFileItem
    ],
):  # Class
    def __init__(self) -> None: ...

    Library: Agilent.MassSpectrometry.DataAnalysis.ILibrary  # readonly

class LibraryFileItem(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.DataFileItemBase,
):  # Class
    def __init__(self) -> None: ...

class LibrarySearchMethodColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.LibrarySearchMethodParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class LibrarySearchMethodParameterBase(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    BatchID: int  # readonly
    IdentificationMethodID: int  # readonly
    LibrarySearchMethodID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

class LoadMethod(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        methodFile: str,
        rowIds: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        methodFile: str,
        revisionNumber: str,
        rowIds: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class LoadMethodToAllSamples(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        methodFile: str,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        methodFile: str,
        revisionNumber: str,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class NewAnalysis(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchFolder: str,
        fileName: str,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchFolder: str,
        fileName: str,
        auditTrail: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class OpenAnalysis(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchFolder: str,
        fileName: str,
        readOnly: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchFolder: str,
        fileName: str,
        revisionNumber: str,
        readOnly: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def Abort(self) -> None: ...
    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class PrimaryHitChangeEventArgs(System.EventArgs):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        oldPrimaryHitID: Optional[int],
        newPrimaryHitID: Optional[int],
    ) -> None: ...

    BatchID: int  # readonly
    ComponentID: int  # readonly
    DeconvolutionMethodID: int  # readonly
    NewPrimaryHitID: Optional[int]  # readonly
    OldPrimaryHitID: Optional[int]  # readonly
    SampleID: int  # readonly

class Redo(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class RemoveDeconvolutionMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SetMethods,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

class RemoveDeconvolutionMethodParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.DeconvolutionMethodParameterBase
):  # Class
    def __init__(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int
    ) -> None: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class RemoveLibrarySearchMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SetMethods,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

class RemoveLibrarySearchMethodParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.LibrarySearchMethodParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> None: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class RemoveSamples(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        samples: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class RemoveTargetCompoundParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.TargetCompoundParameterBase
):  # Class
    def __init__(self, batchID: int, sampleID: int, compoundID: int) -> None: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class SampleColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class SampleDataCache(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.DataFileCache[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleDataItem,
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleDataFile,
    ],
    System.IDisposable,
):  # Class
    def __init__(
        self,
        size: int,
        numericFormat: Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericFormat,
    ) -> None: ...

    UseIndexedDataAccess: bool  # static

class SampleDataFile(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.DataFileBase[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleDataItem
    ],
):  # Class
    def __init__(self) -> None: ...

    DataAccess: Agilent.MassSpectrometry.DataAnalysis.IDataAccess  # readonly
    Error: str  # readonly
    HasAccurateMass: bool  # readonly
    IsOpen: bool  # readonly

    @overload
    @staticmethod
    def SampleHasAccurateMass(sample: UnknownsAnalysisDataSet.SampleRow) -> bool: ...
    @overload
    @staticmethod
    def SampleHasAccurateMass(path: str) -> bool: ...

class SampleDataItem(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.DataFileItemBase,
):  # Class
    def __init__(self) -> None: ...

class SampleRowIDParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(self, batchID: int, sampleID: int) -> None: ...

    BatchID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class SamplesEventArgs(System.EventArgs):  # Class
    def __init__(self, samples: Iterable[SampleRowID]) -> None: ...

    Samples: Iterable[SampleRowID]  # readonly

class SaveAnalysis(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SaveAnalysisAs(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchFolder: str,
        fileName: str,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SaveMethod(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        methodFile: str,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class SetAuxiliaryMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SetMethods,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

class SetBestHit(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.HitRowIDParameter
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetBlankSubtractionMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SetMethods,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        blankSubtractionMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

class SetComponent(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        name: str,
        value_: Any,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.ComponentColumnValuesParameter
        ],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def SetValue(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...

class SetComponentHitVisible(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.ComponentHitVisibleParameter
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        visible: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        visible: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def SetComponentVisible(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        visible: bool,
    ) -> None: ...
    def SetHitVisible(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        visible: bool,
    ) -> None: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...

class SetDeconvolutionMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SetMethods,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

class SetExactMass(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.ExactMassColumnValuesParameter
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        exactMassID: int,
        name: str,
        value_: Any,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetHit(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        name: str,
        value_: Any,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.HitColumnValuesParameter
        ],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetHitVisible(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        visible: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        visible: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.HitRowIDParameter
        ],
        visible: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def AddHitRow(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
    ) -> None: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...

class SetIdentificationMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SetMethods,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

class SetIonPeak(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.IonPeakColumnValuesParameter
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
        name: str,
        value_: Any,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetLibrarySearchMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SetMethods,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

class SetMethods(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

    ActionString: str  # readonly
    ActionStrings: List[str]  # readonly
    Reversible: bool  # readonly

    def SetLibrarySearchMethod(
        self,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def SetDeconvolutionMethod(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def SetIdentificationMethod(
        self,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def RemoveDeconvolutionMethod(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int
    ) -> None: ...
    def AddLibrarySearchMethod(
        self,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> None: ...
    def AddDeconvolutionMethod(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int
    ) -> None: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetBlankSubtractionMethod(
        self,
        batchID: int,
        sampleID: int,
        blankSubtractionMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def SetAuxiliaryMethod(
        self,
        batchID: int,
        sampleID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def RemoveLibrarySearchMethod(
        self,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> None: ...
    def SetTargetMatchMethod(
        self,
        batchID: int,
        sampleID: int,
        targetMatchMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

class SetSample(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        name: str,
        value_: Any,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleColumnValuesParameter
        ],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def SetValue(
        self,
        batchID: int,
        sampleID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...

class SetTargetMatchMethod(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SetMethods,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommandEx,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        targetMatchMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

class SetTargets(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
        ],
    ) -> None: ...

    Reversible: bool  # readonly

    def AddTargetCompound(
        self, batchID: int, sampleID: int, compoundID: int
    ) -> None: ...
    def RemoveTargetCompound(
        self, batchID: int, sampleID: int, compoundID: int
    ) -> None: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetTargetCompound(
        self,
        batchID: int,
        sampleID: int,
        compoundID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

class TargetCompoundColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.TargetCompoundParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        compoundID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class TargetCompoundParameterBase(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    BatchID: int  # readonly
    CompoundID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly

class TargetMatchAll(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        reanalyze: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class TargetMatchMethodColumnValuesParameter(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandParameterBase
):  # Class
    def __init__(
        self,
        batchID: int,
        sampleID: int,
        targetMatchMethodID: int,
        values: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...

    BatchID: int  # readonly
    RowID: RowID  # readonly
    SampleID: int  # readonly
    TargetMatchMethodID: int  # readonly

    def GetValues(
        self,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
    ]: ...
    def CreateExpression(self) -> System.CodeDom.CodeExpression: ...

class TargetMatchSamples(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        samples: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
        reanalyze: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
        batchID: int,
        sampleID: int,
        reanalyze: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class Undo(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.CommandContext,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
