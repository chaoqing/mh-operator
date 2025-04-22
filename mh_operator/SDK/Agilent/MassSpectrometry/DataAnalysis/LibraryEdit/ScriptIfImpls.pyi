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

from .ScriptIf import (
    ICompliance,
    ILibraryAccess,
    IMainForm,
    IScriptEngine,
    IScriptInterface,
    IScriptProgress,
    IScriptScope,
    IUIState,
)
from .Utils import SpectrumKey

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIfImpls

class Compliance(System.MarshalByRefObject, ICompliance):  # Class
    ConnectionTicket: str  # readonly
    IsActive: bool  # readonly
    IsLocal: bool  # readonly
    Name: str  # readonly
    User: str  # readonly

class LibraryAccess(
    System.MarshalByRefObject, System.IDisposable, ILibraryAccess
):  # Class
    CompoundCount: int  # readonly
    Format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat  # readonly

    def Base64ToDoubleArray(self, base64: str) -> List[float]: ...
    def ExportTOJCAMP(self, file: str, spectrumKeys: List[SpectrumKey]) -> None: ...
    def GetSpectrumIds(self, compoundId: int) -> List[int]: ...
    def GetCompoundProperty(self, compoundId: int, name: str) -> Any: ...
    def GetSpectrumProperty(
        self, compoundId: int, spectrumId: int, name: str
    ) -> Any: ...
    def GetCompoundId(self, index: int) -> int: ...
    def DoubleArrayToBase64(self, values: List[float]) -> str: ...
    def Dispose(self) -> None: ...

class ScriptEngine(
    IScriptEngine, System.MarshalByRefObject, System.IDisposable
):  # Class
    CurrentScope: IScriptScope  # readonly
    DebugMode: bool  # readonly
    Engine: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptEngine
    )  # readonly
    Globals: IScriptScope  # readonly
    IsRunning: bool  # readonly

    def CreateScope(self) -> IScriptScope: ...
    @overload
    def Execute(
        self,
        reader: System.IO.TextReader,
        encoding: System.Text.Encoding,
        scope: IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(
        self,
        stream: System.IO.Stream,
        encoding: System.Text.Encoding,
        scope: IScriptScope,
    ) -> Any: ...
    @staticmethod
    def SetDebugEngine(
        engine: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IronEngine,
        initEngine: System.Action[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IronEngine,
            Any,
        ],
    ) -> None: ...
    def Dispose(self) -> None: ...
    def ExecuteFile(self, file: str, scope: IScriptScope) -> Any: ...

class ScriptInterface(
    IScriptInterface, System.MarshalByRefObject, System.IDisposable
):  # Class
    Compliance: ICompliance  # readonly
    LibraryAccess: ILibraryAccess  # readonly
    MainForm: IMainForm  # readonly
    ScriptEngine: IScriptEngine  # readonly
    ScriptProgress: IScriptProgress  # readonly
    UIState: IUIState  # readonly
    _ScriptInterface: IScriptInterface  # readonly

    def Dispose(self) -> None: ...
    def _GetPrivateProfileString(
        self, section: str, key: str, defaultValue: str, fileName: str
    ) -> str: ...
    def _WritePrivateProfileString(
        self, section: str, key: str, value_: str, fileName: str
    ) -> int: ...

class ScriptProgress(
    System.MarshalByRefObject, System.IDisposable, IScriptProgress
):  # Class
    CancellationPending: bool  # readonly
    IsVisible: bool  # readonly
    Marquee: bool
    Message: str
    ProgressMaximum: int
    ProgressStep: int
    ProgressValue: int

    def Dispose(self) -> None: ...
    def Cancel(self) -> None: ...

class UIState(System.MarshalByRefObject, IUIState, System.IDisposable):  # Class
    CanRedo: bool  # readonly
    CanUndo: bool  # readonly
    Format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat  # readonly
    HasLibrary: bool  # readonly
    IsCommandRunning: bool  # readonly
    IsDirty: bool  # readonly
    IsReadOnly: bool  # readonly
    LibraryAccess: ILibraryAccess  # readonly
    LibraryName: str  # readonly
    LibraryPath: str  # readonly
    MainForm: IMainForm  # readonly
    ScriptEngine: IScriptEngine  # readonly
    ScriptInterface: IScriptInterface  # readonly
    ScriptProgress: IScriptProgress  # readonly
    SelectedCompoundCount: int  # readonly
    SelectedCompounds: Iterable[int]  # readonly
    _ScriptInterface: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIfImpls.ScriptInterface
    )  # readonly

    def SelectCompounds(self, compoundIds: Iterable[int]) -> None: ...
    def ClearCompoundSelection(self) -> None: ...
    @overload
    def Dispose(self) -> None: ...
    @overload
    def Dispose(self, disposing: bool) -> None: ...
    def ShowAboutBox(self) -> None: ...
    def GetTools(self, id: str) -> List[Any]: ...
