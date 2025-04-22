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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine

class Engine:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def RunScript(
        language: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.ScriptLanguage,
        stream: System.IO.Stream,
        variables: Dict[str, Any],
    ) -> None: ...

class IScriptEngine(object):  # Interface
    Globals: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope
    )  # readonly

    def GetSearchPaths(self) -> Sequence[str]: ...
    def CreateScope(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope
    ): ...
    @overload
    def Execute(
        self, reader: System.IO.TextReader, encoding: System.Text.Encoding
    ) -> Any: ...
    @overload
    def Execute(
        self,
        reader: System.IO.TextReader,
        encoding: System.Text.Encoding,
        scope: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(
        self, stream: System.IO.Stream, encoding: System.Text.Encoding
    ) -> Any: ...
    @overload
    def Execute(
        self,
        stream: System.IO.Stream,
        encoding: System.Text.Encoding,
        scope: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(self, code: System.CodeDom.CodeObject) -> Any: ...
    def SetSearchPaths(self, paths: Sequence[str]) -> None: ...
    def ExecuteFile(
        self,
        file: str,
        scope: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope,
    ) -> Any: ...

class IScriptScope(object):  # Interface
    def SetVariable(self, name: str, value_: Any) -> None: ...

class IronEngine(
    System.MarshalByRefObject,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptEngine,
):  # Class
    @overload
    def __init__(
        self,
        language: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.ScriptLanguage,
    ) -> None: ...
    @overload
    def __init__(self, engine: Any) -> None: ...

    Globals: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope
    )  # readonly
    _Globals: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.ScriptScope
    )  # readonly

    def GetSearchPaths(self) -> Sequence[str]: ...
    @overload
    def CreateScope(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope
    ): ...
    @overload
    def CreateScope(
        self, variables: Dict[str, Any]
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.ScriptScope
    ): ...
    @overload
    def Execute(
        self, reader: System.IO.TextReader, encoding: System.Text.Encoding
    ) -> Any: ...
    @overload
    def Execute(
        self,
        reader: System.IO.TextReader,
        encoding: System.Text.Encoding,
        iscope: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(
        self, stream: System.IO.Stream, encoding: System.Text.Encoding
    ) -> Any: ...
    @overload
    def Execute(
        self,
        stream: System.IO.Stream,
        encoding: System.Text.Encoding,
        iscope: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(self, code: System.CodeDom.CodeObject) -> Any: ...
    def SetSearchPaths(self, paths: Sequence[str]) -> None: ...
    def LoadAssembly(self, assembly: System.Reflection.Assembly) -> None: ...
    def Dispose(self) -> None: ...
    def ExecuteFile(
        self,
        file: str,
        iscope: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope,
    ) -> Any: ...

class ScriptLanguage(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    IronPython: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.ScriptLanguage
    ) = ...  # static # readonly

class ScriptScope(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptScope
):  # Class
    def GetVariableNames(self) -> Iterable[str]: ...
    def RemoveVariable(self, name: str) -> None: ...
    def GetVariable(self, name: str) -> Any: ...
    def ContainsVariable(self, name: str) -> bool: ...
    def SetVariable(self, name: str, value_: Any) -> None: ...
