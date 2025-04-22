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

from . import Context

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands

class CancelNewCompound(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class CommandBase(
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.CommandModel.CommandBase,
):  # Class
    Context: Context  # readonly

class CommitNewCompound(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class CompositeCommandBase(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    Count: int  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class Delete(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CompositeCommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def DeleteNewCompoundColumn(self, columnName: str) -> None: ...
    def DeleteNewCompound(self) -> None: ...
    def DeleteCompound(self, compoundName: str) -> None: ...
    def GetParameters(self) -> List[Any]: ...
    def DeleteColumn(self, compoundName: str, columnName: str) -> None: ...

class DeleteCompound(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context, compoundName: str) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class NewFile(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class OpenFile(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context, file: str, readOnly: bool) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class Paste(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CompositeCommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def StartNewCompound(self) -> None: ...
    def SetNewCompoundColumn(self, name: str, value_: Any) -> None: ...
    def SetCompoundColumn(self, compoundName: str, name: str, value_: Any) -> None: ...
    def GetParameters(self) -> List[Any]: ...
    def CommitNewCompound(self) -> None: ...

class SaveFile(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SaveFileAs(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context, file: str) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetCompoundColumn(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self, context: Context, compoundName: str, name: str, value_: Any
    ) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetNewCompoundColumn(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context, name: str, value_: Any) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetSampleColumn(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self, context: Context, sampleName: str, name: str, value_: Any
    ) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class StartNewCompound(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportFixedGraphics.Commands.CommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: Context, name: str, value_: Any) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...
