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

from .ScriptIfImpls import UIState

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Utils

class CompoundKey(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Utils.CompoundKey
    ]
):  # Class
    def __init__(self, compoundId: int) -> None: ...

    CompoundId: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self, other: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Utils.CompoundKey
    ) -> int: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(
        self, key: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Utils.CompoundKey
    ) -> bool: ...

class SaveLibraryHelper:  # Class
    ...

class ScriptHelper:  # Class
    @staticmethod
    def RunScript(uiState: UIState, file: str) -> None: ...

class SpectrumKey(
    System.IComparable[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Utils.SpectrumKey
    ]
):  # Class
    def __init__(self, compoundId: int, spectrumId: int) -> None: ...

    CompoundId: int  # readonly
    SpectrumId: int  # readonly

    def GetHashCode(self) -> int: ...
    def CompareTo(
        self, other: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Utils.SpectrumKey
    ) -> int: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(
        self, key: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Utils.SpectrumKey
    ) -> bool: ...

class Utilities:  # Class
    @staticmethod
    def CompressedEntryToDataRows(
        library: Agilent.MassSpectrometry.DataAnalysis.MSLibrary,
        index: int,
        compound: System.Data.DataRow,
        spectrum: Agilent.MassSpectrometry.DataAnalysis.LibraryDataSet.SpectrumRow,
    ) -> None: ...
    @staticmethod
    def IsHandlableException(ex: System.Exception) -> bool: ...
    @staticmethod
    def GetColumnHeaderText(columnName: str) -> str: ...
    @staticmethod
    def FindHandlableException(ex: System.Exception) -> System.Exception: ...
    @staticmethod
    def ShowExceptionMessage(
        parent: System.Windows.Forms.IWin32Window, ex: System.Exception
    ) -> None: ...
    @staticmethod
    def FindException(
        ex: System.Exception, list: List[System.Type]
    ) -> System.Exception: ...
    @staticmethod
    def ShowMessage(
        parent: System.Windows.Forms.IWin32Window,
        message: str,
        caption: str,
        buttons: System.Windows.Forms.MessageBoxButtons,
        icon: System.Windows.Forms.MessageBoxIcon,
    ) -> System.Windows.Forms.DialogResult: ...
