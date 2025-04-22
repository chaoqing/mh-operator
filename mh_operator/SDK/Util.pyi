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

# Stubs for namespace: Util

class ApplicationInfo:  # Class
    def __init__(self) -> None: ...

    AppDataFolder: str  # static

class Ascii:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def FromString(s: str, arrayLength: int) -> List[int]: ...
    @staticmethod
    def ToString(aBuff: List[int], iOffSet: int, iLengthToRead: int) -> str: ...

class EditablePersistantDocument:  # Class
    def __init__(
        self,
        defaultStorageFolder: str,
        DocumentName: str,
        FileExtension: str,
        fileType: str,
        documentType: str,
    ) -> None: ...

    FilePath: str  # readonly

    @overload
    def SaveEditing(self) -> bool: ...
    @overload
    def SaveEditing(
        self, confirmingFirst: bool
    ) -> Util.EditablePersistantDocument.SaveStatus: ...
    def MarkAsEdited(self) -> None: ...
    def SaveAs(self) -> None: ...
    @overload
    def LoadDocument(self) -> bool: ...
    @overload
    def LoadDocument(self, filePath: str) -> None: ...
    def Save(self) -> None: ...

    # Nested Types

    class SaveStatus(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        NoAbort: Util.EditablePersistantDocument.SaveStatus = ...  # static # readonly
        NoContinue: Util.EditablePersistantDocument.SaveStatus = (
            ...
        )  # static # readonly
        Yes: Util.EditablePersistantDocument.SaveStatus = ...  # static # readonly

class IProgressable(object):  # Interface
    StepCount: int  # readonly

    def StepIt(self, stepIndex: int) -> bool: ...

class ListPacker:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def Unpack(code: List[int], bitSize: int) -> List[int]: ...
    @staticmethod
    def Pack(list: List[int], bitSize: int) -> List[int]: ...

class StringUtilities:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def ExtractFileName(fullFilePath: str) -> str: ...
    @staticmethod
    def FindMatchingGeneralParenthesis(data: str, parenthesis1Pos: int) -> int: ...
    @staticmethod
    def ExtractFolder(fullFilePath: str) -> str: ...
    @staticmethod
    def FormatLargeNumber(i: int) -> str: ...
    @staticmethod
    def TrimGeneralParentheses(input: str) -> str: ...
    @staticmethod
    def ExtractExtensionlessFileName(fullPath: str) -> str: ...
    @staticmethod
    def TrimLeadingInteger(input: str) -> str: ...
    @staticmethod
    def TrimTrailingInteger(input: str) -> str: ...
    @staticmethod
    def ExtractFileExtension(fileName: str) -> str: ...
    @staticmethod
    def ReplaceHtmlCharacters(text: str) -> str: ...
