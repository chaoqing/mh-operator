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
    Commands,
    Configurations,
    Controls,
    DataAccess,
    Remoting,
    ScriptIf,
    ScriptIfImpls,
    ToolHandlers,
    Utils,
)
from .Commands import AppContext
from .Controls import MainForm
from .Quantitative.Compliance import ICompliance
from .Utils import CompoundKey, SpectrumKey

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit

class CommandLine:  # Class
    def __init__(self) -> None: ...

    AccountName: str
    CommandLog: str
    ConnectionTicket: str
    Console: bool
    Culture: str
    Domain: str
    EncryptedPassword: str
    Help: bool
    Library: str
    Password: str
    ScriptFiles: List[str]
    Server: str
    User: str

    def Initialize(self, compliance: ICompliance) -> MainForm: ...
    def SetCulture(self) -> None: ...
    def InitCompliance(self, mainForm: MainForm) -> bool: ...
    def RunScripts(self, form: MainForm) -> bool: ...
    def Run(self, form: MainForm) -> None: ...

class ConsoleCommandLine:  # Class
    def __init__(self) -> None: ...

    AccountName: str
    ConnectionTicket: str
    Culture: str
    Domain: str
    EncryptedPassword: str
    Help: bool
    NoLogo: bool
    Password: str
    ScriptFiles: List[str]
    Server: str
    User: str

    def Run(self, compliance: ICompliance) -> int: ...

class Definitions:  # Class
    JcampFileExtension: str = ...  # static # readonly
    NormalizedAbundance: float = ...  # static # readonly

    BinaryFileExtension: str  # static # readonly
    CompressedLibraryExtension: str  # static # readonly
    PatternRefLibraryExtension: str  # static # readonly
    RefLibraryExtension: str  # static # readonly
    XmlFileExtension: str  # static # readonly

class LibraryEditException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(
        self, ci: System.Globalization.CultureInfo, format: str, parameters: List[Any]
    ) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class UIContext(System.IDisposable):  # Class
    def __init__(self, compliance: ICompliance) -> None: ...

    AppContext: AppContext  # readonly
    SelectedCompoundCount: int  # readonly
    SelectedCompoundKeys: Iterable[CompoundKey]  # readonly
    SelectedSpectrumCount: int  # readonly
    SelectedSpectrumKeys: Iterable[SpectrumKey]  # readonly

    def ClearCompoundSelection(self) -> None: ...
    def SelectSpectra(self, keys: Iterable[SpectrumKey]) -> None: ...
    def Dispose(self) -> None: ...
    def SelectCompounds(self, keys: Iterable[CompoundKey]) -> None: ...
