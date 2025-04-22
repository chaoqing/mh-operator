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

# Stubs for namespace: Agilent.MassSpectrometry.CommandModel.Model

class CommandType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Data: Agilent.MassSpectrometry.CommandModel.Model.CommandType = (
        ...
    )  # static # readonly
    UndoRedo: Agilent.MassSpectrometry.CommandModel.Model.CommandType = (
        ...
    )  # static # readonly
    View: Agilent.MassSpectrometry.CommandModel.Model.CommandType = (
        ...
    )  # static # readonly

class ICodeDomExpandParameter(
    Agilent.MassSpectrometry.CommandModel.Model.ICodeDomParameter
):  # Interface
    def GetPreCommandStatements(
        self, counter: int
    ) -> System.CodeDom.CodeStatementCollection: ...

class ICodeDomParameter(object):  # Interface
    def GetExpression(self) -> System.CodeDom.CodeExpression: ...

class ICommand(System.IDisposable):  # Interface
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def Execute(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...

class ICommandHistory(System.IDisposable):  # Interface
    CanRedo: bool  # readonly
    CanUndo: bool  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def RevokeLogListener(
        self, listener: Agilent.MassSpectrometry.CommandModel.Model.ILogListener
    ) -> None: ...
    def Clear(self) -> None: ...
    def RegisterLogListener(
        self, listener: Agilent.MassSpectrometry.CommandModel.Model.ILogListener
    ) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> Any: ...
    def BeginInvoke(
        self,
        cmd: Agilent.MassSpectrometry.CommandModel.Model.ICommand,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self, cmd: Agilent.MassSpectrometry.CommandModel.Model.ICommand
    ) -> Any: ...

class ICommandPermission(object):  # Interface
    def CheckUserRole(self) -> None: ...

class ICommandPrincipal(object):  # Interface
    def CheckPermission(
        self, command: Agilent.MassSpectrometry.CommandModel.Model.ICommandPermission
    ) -> None: ...
    def HasPermission(
        self, command: Agilent.MassSpectrometry.CommandModel.Model.ICommandPermission
    ) -> bool: ...

class ILogListener(object):  # Interface
    def Log(
        self, cmd: Agilent.MassSpectrometry.CommandModel.Model.ICommand
    ) -> None: ...
