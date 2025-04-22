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

from .Commands import AppContext
from .Utils import SpectrumKey

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf

class ICompliance(object):  # Interface
    ConnectionTicket: str  # readonly
    IsActive: bool  # readonly
    IsLocal: bool  # readonly
    Name: str  # readonly
    User: str  # readonly

class ICompoundGridPane(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IPane
):  # Interface
    CanExportToJCAMP: bool  # readonly
    IsInSearchMode: bool  # readonly
    RowCount: int  # readonly
    SelectedRowIndices: List[int]  # readonly

    def ShowColumnsDialog(self) -> None: ...
    def ExportToJCAMP(self, file: str) -> None: ...
    def GetCompoundId(self, rowIndex: int) -> int: ...
    def ShowSearchDialog(self) -> None: ...
    def ClearSearch(self) -> None: ...
    def SelectRows(self, indices: List[int]) -> None: ...

class ILibraryAccess(object):  # Interface
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

class IMainForm(System.Windows.Forms.IWin32Window):  # Interface
    ActivePane: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IPane
    )  # readonly
    CompoundGridPane: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.ICompoundGridPane
    )  # readonly
    IsRtl: bool  # readonly
    SpectrumPlotPane: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.ISpectrumPlotPane
    )  # readonly
    SpectrumPropertiesPane: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.ISpectrumPropertiesPane
    )  # readonly

    def ShowLibraryPropertiesDialog(self) -> None: ...
    def Close(self) -> None: ...

class IPane(object):  # Interface
    CanCopy: bool  # readonly
    CanCut: bool  # readonly
    CanDelete: bool  # readonly
    CanPaste: bool  # readonly

    def Paste(self) -> None: ...
    def Copy(self) -> None: ...
    def Cut(self) -> None: ...
    def Delete(self) -> None: ...

class IScriptEngine(object):  # Interface
    CurrentScope: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptScope
    )  # readonly
    DebugMode: bool  # readonly
    Engine: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ScriptEngine.IScriptEngine
    )  # readonly
    Globals: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptScope
    )  # readonly
    IsRunning: bool  # readonly

    def CreateScope(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptScope: ...
    def ExecuteFile(
        self,
        file: str,
        scope: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(
        self,
        reader: System.IO.TextReader,
        encoding: System.Text.Encoding,
        scope: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptScope,
    ) -> Any: ...
    @overload
    def Execute(
        self,
        stream: System.IO.Stream,
        encoding: System.Text.Encoding,
        scope: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptScope,
    ) -> Any: ...

class IScriptInterface(object):  # Interface
    Compliance: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.ICompliance
    )  # readonly
    LibraryAccess: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.ILibraryAccess
    )  # readonly
    MainForm: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IMainForm
    )  # readonly
    ScriptEngine: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptEngine
    )  # readonly
    ScriptProgress: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptProgress
    )  # readonly
    UIState: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IUIState
    )  # readonly
    _ScriptInterface: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptInterface
    )  # readonly

    def _GetPrivateProfileString(
        self, section: str, key: str, defaultValue: str, fileName: str
    ) -> str: ...
    def _WritePrivateProfileString(
        self, section: str, key: str, value_: str, fileName: str
    ) -> int: ...

class IScriptProgress(object):  # Interface
    CancellationPending: bool  # readonly
    IsVisible: bool  # readonly
    Marquee: bool
    Message: str
    ProgressMaximum: int
    ProgressStep: int
    ProgressValue: int

    def Cancel(self) -> None: ...

class IScriptScope(object):  # Interface
    def GetVariableNames(self) -> Iterable[str]: ...
    def RemoveVariable(self, name: str) -> None: ...
    def GetVariable(self, name: str) -> Any: ...
    def ContainsVariable(self, name: str) -> bool: ...
    def SetVariable(self, name: str, value_: Any) -> None: ...

class ISpectrumPlotPane(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IPane
):  # Interface
    DrawMolecularStructure: bool
    MaxNumRowsPerPage: int
    SelectedSpectrumKeys: System.Collections.Generic.List[SpectrumKey]  # readonly

class ISpectrumPropertiesPane(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IPane
):  # Interface
    Visible: bool

class IUIState(object):  # Interface
    AppContext: AppContext  # readonly
    CanRedo: bool  # readonly
    CanUndo: bool  # readonly
    Format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat  # readonly
    HasLibrary: bool  # readonly
    IsCommandRunning: bool  # readonly
    IsDirty: bool  # readonly
    IsReadOnly: bool  # readonly
    LibraryAccess: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.ILibraryAccess
    )  # readonly
    LibraryName: str  # readonly
    LibraryPath: str  # readonly
    MainForm: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IMainForm
    )  # readonly
    ScriptInterface: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptInterface
    )  # readonly
    ScriptProgress: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ScriptIf.IScriptProgress
    )  # readonly
    SelectedCompoundCount: int  # readonly
    SelectedCompounds: Iterable[int]  # readonly

    def ClearCompoundSelection(self) -> None: ...
    def ShowAboutBox(self) -> None: ...
    def GetTools(self, id: str) -> List[Any]: ...
    def SelectCompounds(self, compoundIds: Iterable[int]) -> None: ...
