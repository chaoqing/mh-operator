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

from . import Model
from .Model import (
    CommandType,
    ICommand,
    ICommandHistory,
    ICommandPrincipal,
    ILogListener,
)

# Stubs for namespace: Agilent.MassSpectrometry.CommandModel

class CodeDomLogFormatter(
    System.IDisposable, Agilent.MassSpectrometry.CommandModel.LogFormatter
):  # Class
    @overload
    def __init__(self, language: str) -> None: ...
    @overload
    def __init__(self, language: str, providerOptions: Dict[str, str]) -> None: ...
    @overload
    def __init__(self, provider: System.CodeDom.Compiler.CodeDomProvider) -> None: ...
    def Format(self, cmd: ICommand) -> str: ...

class CommandActivator(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> ICommand: ...
    def BeginInvoke(
        self, objects: List[Any], callback: System.AsyncCallback, object: Any
    ) -> System.IAsyncResult: ...
    def Invoke(self, objects: List[Any]) -> ICommand: ...

class CommandBase(System.IDisposable, ICommand):  # Class
    Reversible: bool  # readonly
    Type: CommandType  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def EndExecute(self, result: System.IAsyncResult) -> Any: ...
    def Execute(self) -> Any: ...
    def BeginExecute(
        self, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def Dispose(self) -> None: ...

class CommandClassAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

    Name: str  # readonly

    def GetCommandActivator(
        self, type: System.Type
    ) -> Agilent.MassSpectrometry.CommandModel.CommandActivator: ...

class CommandEntryAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self) -> None: ...

class CommandGenericPrincipal(
    Agilent.MassSpectrometry.CommandModel.CommandPrincipal, ICommandPrincipal
):  # Class
    def __init__(self) -> None: ...
    def Logon(self, user: str, roles: List[str]) -> None: ...

class CommandHistory(System.IDisposable, ICommandHistory):  # Class
    def __init__(self, capacity: int) -> None: ...

    CanRedo: bool  # readonly
    CanUndo: bool  # readonly
    Count: int  # readonly
    Principal: ICommandPrincipal
    SuppressDisposeCommands: bool

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def RevokeLogListener(self, listener: ILogListener) -> None: ...
    def Clear(self) -> None: ...
    def RegisterLogListener(self, listener: ILogListener) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> Any: ...
    def BeginInvoke(
        self, cmd: ICommand, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def Dispose(self) -> None: ...
    def Invoke(self, cmd: ICommand) -> Any: ...

    # Nested Types

    class InvokeCommand(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> Any: ...
        def BeginInvoke(
            self, cmd: ICommand, callback: System.AsyncCallback, object: Any
        ) -> System.IAsyncResult: ...
        def Invoke(self, cmd: ICommand) -> Any: ...

class CommandNoPrincipal(ICommandPrincipal):  # Class
    def __init__(self) -> None: ...

class CommandPrincipal(ICommandPrincipal):  # Class
    ...

class CommandTypeNotFoundException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...
    def GetObjectData(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class CommandWindowsPrincipal(
    Agilent.MassSpectrometry.CommandModel.CommandPrincipal, ICommandPrincipal
):  # Class
    def __init__(self) -> None: ...
    def Logon(self) -> None: ...

class CompositeCommand(
    ICommand, System.IDisposable, Agilent.MassSpectrometry.CommandModel.CommandBase
):  # Class
    Count: int  # readonly
    Reversible: bool  # readonly
    Type: CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Add(self, cmd: ICommand) -> Any: ...
    def Undo(self) -> Any: ...

class InvalidCommandDefinitionException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...
    def GetObjectData(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class InvalidCommandParameterException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...
    @overload
    def __init__(self, message: str, type: System.Type) -> None: ...

    ParameterType: System.Type  # readonly

    def GetObjectData(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class LogFormatter(System.IDisposable):  # Class
    def Dispose(self) -> None: ...
    def Format(self, cmd: ICommand) -> str: ...

class LogListener(System.IDisposable, ILogListener):  # Class
    def Dispose(self) -> None: ...
    def Log(self, cmd: ICommand) -> None: ...

class RedoCommand(
    ICommand, System.IDisposable, Agilent.MassSpectrometry.CommandModel.CommandBase
):  # Class
    def __init__(self, history: ICommandHistory) -> None: ...

    Reversible: bool  # readonly
    Type: CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class RuntimeCommand(
    ICommand, System.IDisposable, Agilent.MassSpectrometry.CommandModel.CommandBase
):  # Class
    @overload
    def __init__(
        self,
        history: ICommandHistory,
        getTargetMethodName: str,
        getTargetParameters: List[Any],
        methodName: str,
    ) -> None: ...
    @overload
    def __init__(
        self,
        history: ICommandHistory,
        getTargetMethodName: str,
        getTargetParameters: List[Any],
        methodName: str,
        parameters: List[Any],
    ) -> None: ...
    @overload
    def __init__(
        self,
        history: ICommandHistory,
        getTargetMethodName: str,
        getTargetParameters: List[Any],
        methodName: str,
        parameters: List[Any],
        undoMethodName: str,
        undoParameters: List[Any],
    ) -> None: ...

    Reversible: bool  # readonly
    Type: CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class ScriptCompile:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def GenerateCodeScriptClass(
        nameSpace: System.CodeDom.CodeNamespace,
        className: str,
        baseClassName: str,
        mainMethodName: str,
        scriptCode: System.IO.TextReader,
    ) -> None: ...
    @staticmethod
    def GenerateCodeCommandMethod(
        typeClass: System.CodeDom.CodeTypeDeclaration,
        commandType: System.Type,
        commandName: str,
        constructor: System.Reflection.ConstructorInfo,
    ) -> None: ...
    @staticmethod
    def GenerateCodeCustomStubMethod(
        typeClass: System.CodeDom.CodeTypeDeclaration,
        stubType: System.Type,
        methodInfo: System.Reflection.MethodInfo,
    ) -> None: ...
    @staticmethod
    def GenerateCodeCustomStubProperties(
        typeClass: System.CodeDom.CodeTypeDeclaration,
        stubType: System.Type,
        propertyInfo: System.Reflection.PropertyInfo,
    ) -> None: ...
    @staticmethod
    def GenerateCodeCommandEntries(
        typeClass: System.CodeDom.CodeTypeDeclaration, commandAssemblies: List[str]
    ) -> None: ...
    @staticmethod
    def GenerateCodeScriptBaseClass(
        codeNamespace: System.CodeDom.CodeNamespace,
        className: str,
        mainMethodName: str,
        customStub: Any,
        commandAssemblies: List[str],
    ) -> None: ...
    @staticmethod
    def CreateCompileUnitBaseClass(
        namespaceName: str,
        className: str,
        mainMethodName: str,
        customStub: Any,
        commandAssemblies: List[str],
        imports: List[str],
    ) -> System.CodeDom.CodeCompileUnit: ...
    @staticmethod
    def CreateCompileUnitScriptClass(
        namespaceName: str,
        className: str,
        baseClassName: str,
        mainMethodName: str,
        imports: List[str],
        scriptCode: System.IO.TextReader,
    ) -> System.CodeDom.CodeCompileUnit: ...
    @staticmethod
    def GenerateCodeCustomStubMembers(
        typeClass: System.CodeDom.CodeTypeDeclaration, customStub: Any
    ) -> None: ...

class ScriptCompilerErrors:  # Class
    Count: int  # readonly
    def __getitem__(self, index: int) -> System.CodeDom.Compiler.CompilerError: ...
    def GetErrorNumber(self, index: int) -> str: ...
    def GetErrorText(self, index: int) -> str: ...

class ScriptHost:  # Class
    @staticmethod
    def BeginRun(
        parameters: Agilent.MassSpectrometry.CommandModel.ScriptParameters,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    @staticmethod
    def EndRun(result: System.IAsyncResult) -> Any: ...
    @staticmethod
    def Run(
        parameters: Agilent.MassSpectrometry.CommandModel.ScriptParameters,
    ) -> Any: ...

    # Nested Types

    class AsyncResult(
        Agilent.MassSpectrometry.CommandModel.ScriptMarshalByRefObject,
        System.IDisposable,
        System.IAsyncResult,
    ):  # Class
        def OnScriptEnd(self) -> None: ...

    class RemoteHost(System.MarshalByRefObject, System.IDisposable):  # Class
        @overload
        def __init__(self) -> None: ...
        @overload
        def __init__(self, language: str, providerOptions: Dict[str, str]) -> None: ...

        CompilerErrorCount: int  # readonly
        TempFiles: List[str]  # readonly

        def BeginRun(
            self, parameters: Agilent.MassSpectrometry.CommandModel.ScriptParameters
        ) -> None: ...
        def GetCompilerError(
            self,
            index: int,
            fileName: str,
            line: int,
            column: int,
            errorNumber: str,
            errorText: str,
        ) -> None: ...
        def Dispose(self) -> None: ...
        def EndRun(self) -> Any: ...
        def Run(
            self, parameters: Agilent.MassSpectrometry.CommandModel.ScriptParameters
        ) -> Any: ...

class ScriptMarshalByRefObject(System.MarshalByRefObject, System.IDisposable):  # Class
    def Dispose(self) -> None: ...
    def InitializeLifetimeService(self) -> Any: ...

class ScriptParameters(
    System.IDisposable, Agilent.MassSpectrometry.CommandModel.ScriptMarshalByRefObject
):  # Class
    def __init__(
        self,
        customStub: System.MarshalByRefObject,
        commandContext: Any,
        commandAssemblies: List[str],
        debug: bool,
        language: str,
        scriptCode: System.IO.TextReader,
    ) -> None: ...

    CommandAssemblies: List[str]  # readonly
    CommandContext: Any  # readonly
    CommandProxyAssemblyName: str
    CustomStub: System.MarshalByRefObject  # readonly
    Debug: bool  # readonly
    Imports: List[str]
    Language: str  # readonly
    OutputFolder: str
    ReferenceAssemblies: List[str]
    ScriptCode: System.IO.TextReader
    SkipGenerateCommandProxyClass: bool

    def AddProviderOption(self, key: str, value_: str) -> None: ...

class ScriptProxy:  # Class
    ReturnValue: Any

class ScriptStub(
    System.IDisposable, Agilent.MassSpectrometry.CommandModel.ScriptMarshalByRefObject
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, context: Any, customStub: System.MarshalByRefObject) -> None: ...

    CustomStub: System.MarshalByRefObject  # readonly

    def ExecuteCommand(self, typeName: str, parameters: List[Any]) -> Any: ...
    def ExecuteCommandWithParameterArray(
        self, typeName: str, dummy: int, parameters: List[Any]
    ) -> Any: ...
    def Dispose(self) -> None: ...

class TextWriterLogListener(
    System.IDisposable, ILogListener, Agilent.MassSpectrometry.CommandModel.LogListener
):  # Class
    def __init__(
        self,
        writer: System.IO.TextWriter,
        formatter: Agilent.MassSpectrometry.CommandModel.LogFormatter,
    ) -> None: ...

class UndoCommand(
    ICommand, System.IDisposable, Agilent.MassSpectrometry.CommandModel.CommandBase
):  # Class
    def __init__(self, history: ICommandHistory) -> None: ...

    Reversible: bool  # readonly
    Type: CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...
