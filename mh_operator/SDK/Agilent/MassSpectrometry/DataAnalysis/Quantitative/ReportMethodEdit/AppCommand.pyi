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

from .Utils import (
    CompoundGraphicsKey,
    CompoundGraphicsRangeColumnValueParameter,
    FormattingColumnValueParameter,
    FormattingKey,
    KeyValue,
    PrePostProcessColumnValueParameter,
    PrePostProcessKey,
    ReportColumnValueParameter,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand

class AppCommandBase(
    Agilent.MassSpectrometry.CommandModel.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    ActionString: str  # readonly
    Name: str  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class ApplicationType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    QuantAnalysis: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.ApplicationType
    ) = ...  # static # readonly
    UnknownsAnalysis: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.ApplicationType
    ) = ...  # static # readonly
    Unspecified: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.ApplicationType
    ) = ...  # static # readonly

class Context(
    Agilent.MassSpectrometry.CommandModel.Model.ICommandHistory,
    Agilent.MassSpectrometry.CommandModel.CommandHistory,
    System.IDisposable,
):  # Class
    def __init__(self) -> None: ...

    AuditTrail: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IAuditTrail
    )  # readonly
    Compliance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance
    )  # readonly
    CurrentReportID: int  # readonly
    IsDirty: bool  # readonly
    PathName: str  # readonly
    ReportMethodDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet
    )  # readonly

    def Invoke(
        self, cmd: Agilent.MassSpectrometry.CommandModel.Model.ICommand
    ) -> Any: ...
    def NewMethod(self) -> None: ...

    CalibrationGraphicsPropertiesChanged: System.EventHandler  # Event
    CompoundGraphicsRangeCountChanged: System.EventHandler  # Event
    CompoundGraphicsRangePropertiesChanged: System.EventHandler  # Event
    FormattingCountChanged: System.EventHandler  # Event
    FormattingPropertiesChanged: System.EventHandler  # Event
    GraphicsRangePropertiesChanged: System.EventHandler  # Event
    MethodClosed: System.EventHandler  # Event
    MethodClosing: System.EventHandler  # Event
    MethodOpened: System.EventHandler  # Event
    MethodOpening: System.EventHandler  # Event
    MethodSaved: System.EventHandler  # Event
    PeakChromatogramGraphicsPropertiesChanged: System.EventHandler  # Event
    PeakQualifiersGraphicsPropertiesChanged: System.EventHandler  # Event
    PeakSpectrumGraphicsPropertiesChanged: System.EventHandler  # Event
    PrePostProcessCountChanged: System.EventHandler  # Event
    PrePostProcessPropertiesChanged: System.EventHandler  # Event
    ReportPropertiesChanged: System.EventHandler  # Event
    SampleChromatogramGraphicsPropertiesChanged: System.EventHandler  # Event

class Delete(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        formattings: List[FormattingKey],
        formattingProperties: List[FormattingColumnValueParameter],
        prePostProcesses: List[PrePostProcessKey],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def DeleteFormatting(self, reportID: int, formattingID: int) -> None: ...
    def DeleteFormattingProperty(
        self, reportID: int, formattingID: int, name: str
    ) -> None: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def DeletePrePostProcessProperty(
        self, reportID: int, prePostProcessID: int
    ) -> None: ...

class NewFormattings(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[FormattingColumnValueParameter],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def AddFormatting(
        self, reportId: int, formattingId: int, values: List[KeyValue]
    ) -> None: ...
    def Redo(self) -> Any: ...
    @staticmethod
    def FindNewID(
        ds: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> int: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...

class NewMethod(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class NewPrePostProcess(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        reportID: int,
        prePostProcessID: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        reportID: int,
        prePostProcessID: int,
        values: List[KeyValue],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    @staticmethod
    def FindNewID(
        ds: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> int: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, name: str, value_: Any) -> None: ...

class Open(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        pathName: str,
        revisionNumber: str,
        readOnly: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class RedoCommand(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class Save(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SaveAs(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        pathName: str,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        pathName: str,
        ok: bool,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetCalibrationGraphicsProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.SetGraphicsPropertiesBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[ReportColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    PropertyCount: int  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, reportID: int, name: str, value_: Any) -> None: ...

class SetFormattingProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[FormattingColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(
        self, reportID: int, formattingID: int, name: str, value_: Any
    ) -> None: ...

class SetGraphicsPropertiesBase(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    def SetProperty(self, reportID: int, name: str, value_: Any) -> None: ...

class SetGraphicsRanges(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        graphicsRangeProperties: List[ReportColumnValueParameter],
        deleteCompoundGraphicsKeys: List[CompoundGraphicsKey],
        newCompoundGraphicsKeys: List[CompoundGraphicsKey],
        compoundGraphicsProperties: List[CompoundGraphicsRangeColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def SetCompoundGraphicsProperty(
        self, reportID: int, compoundGraphicsID: int, name: str, value_: Any
    ) -> None: ...
    def AddCompoundGraphicsRange(
        self, reportID: int, compoundGraphicsID: int
    ) -> None: ...
    def DeleteCompoundGraphicsRange(
        self, reportID: int, compoundGraphicsID: int
    ) -> None: ...
    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def SetGraphicsRange(self, reportID: int, name: str, value_: Any) -> None: ...

class SetPeakChromatogramGraphicsProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.SetGraphicsPropertiesBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[ReportColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    PropertyCount: int  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, reportID: int, name: str, value_: Any) -> None: ...

class SetPeakQualifiersGraphicsProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.SetGraphicsPropertiesBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[ReportColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    PropertyCount: int  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, reportID: int, name: str, value_: Any) -> None: ...

class SetPeakSpectrumGraphicsProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.SetGraphicsPropertiesBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[ReportColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    PropertyCount: int  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, reportID: int, name: str, value_: Any) -> None: ...

class SetPrePostProcessProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[PrePostProcessColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(
        self, reportID: int, prePostProcessID: int, name: str, value_: Any
    ) -> None: ...

class SetReportProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[ReportColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, reportID: int, name: str, value_: Any) -> None: ...

class SetSampleChromatogramGraphicsProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.SetGraphicsPropertiesBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[ReportColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    PropertyCount: int  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, reportID: int, name: str, value_: Any) -> None: ...

class SetUnknownsIonPeakGraphicsProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.SetGraphicsPropertiesBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[ReportColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    PropertyCount: int  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, reportID: int, name: str, value_: Any) -> None: ...

class SetUnknownsSampleChromatogramGraphicsProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.SetGraphicsPropertiesBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[ReportColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    PropertyCount: int  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, reportID: int, name: str, value_: Any) -> None: ...

class SetUnknownsSpectrumGraphicsProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.SetGraphicsPropertiesBase,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
        parameters: List[ReportColumnValueParameter],
    ) -> None: ...

    ActionString: str  # readonly
    PropertyCount: int  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, reportID: int, name: str, value_: Any) -> None: ...

class UndoCommand(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.AppCommand.Context,
    ) -> None: ...

    ActionString: str  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...
