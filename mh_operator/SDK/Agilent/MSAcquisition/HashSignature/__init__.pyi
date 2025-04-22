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

from . import Properties

# Stubs for namespace: Agilent.MSAcquisition.HashSignature

class CHashComponent(Agilent.MSAcquisition.HashSignature.IHashComponent):  # Class
    def __init__(self) -> None: ...

class ENUM_HASH_DATA_TYPE(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ACQ_DATA: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE = (
        ...
    )  # static # readonly
    ACQ_METHOD: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE = (
        ...
    )  # static # readonly
    ACQ_STUDY: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE = (
        ...
    )  # static # readonly
    GENERIC_FOLDER: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE = (
        ...
    )  # static # readonly
    XML_FILE: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE = (
        ...
    )  # static # readonly

class Globals:  # Class
    def __init__(self) -> None: ...

    AlgoVersionAttributeName: str = ...  # static # readonly
    BackupFileExtn: str = ...  # static # readonly
    ChecksumFileName: str = ...  # static # readonly
    ChecksumTagName: str = ...  # static # readonly
    DAMethodFolder: str = ...  # static # readonly
    DataFile_Extn: str = ...  # static # readonly
    DummyHashCode: str = ...  # static # readonly
    FileTagName: str = ...  # static # readonly
    FileToIncludeFromStudyRoot_BioAnalysisXltx: str = ...  # static # readonly
    FileToIncludeFromStudyRoot_MethodByInputFileTxt: str = ...  # static # readonly
    FilesToIncludeFromStudyRoot_FilesWithExtension_QuantScript: str = (
        ...
    )  # static # readonly
    FilesToIncludeFromStudyRoot_StudyLogTxt: str = ...  # static # readonly
    FolderTagName: str = ...  # static # readonly
    HashCodeAttributeName: str = ...  # static # readonly
    MainTagName: str = ...  # static # readonly
    MaxFileLength: int = ...  # static # readonly
    MethodFile_Extn: str = ...  # static # readonly
    NameTagName: str = ...  # static # readonly
    PathDelimeter: str = ...  # static # readonly
    RootFolder: str = ...  # static # readonly
    SSIZIPFile_Extn: str = ...  # static # readonly
    Schema1XMLFileString: str = ...  # static # readonly
    Schema2XMLFileString: str = ...  # static # readonly
    Schema2XMLString: str = ...  # static # readonly
    Schema3XMLFileString: str = ...  # static # readonly
    SchemaVersionAttributeName: str = ...  # static # readonly
    StudyFile_Extn: str = ...  # static # readonly
    SystemFolder: str = ...  # static # readonly
    VersionTagName: str = ...  # static # readonly
    VersionsFolder: str = ...  # static # readonly
    XMLFile_Extn: str = ...  # static # readonly

class IHashComponent(object):  # Interface
    def VerifyHashForFile(
        self,
        hashDataType: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE,
        filePath: str,
    ) -> bool: ...
    def VerifyHashForFolder(
        self,
        hashDataType: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE,
        path: str,
        foldersToInclude: str,
    ) -> bool: ...
    def GenerateHash(self, path: str, foldersToInclude: str) -> None: ...
    def VerifyHashForDataObject(
        self,
        hashDataType: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE,
        path: str,
        foldersToInclude: str,
    ) -> bool: ...
    def GenerateHashForDataObject(
        self,
        hashDataType: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE,
        path: str,
        foldersToInclude: str,
    ) -> None: ...
    def GenerateHashForFolder(
        self,
        hashDataType: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE,
        path: str,
        foldersToInclude: str,
    ) -> None: ...
    def GenerateHashForFile(
        self,
        hashDataType: Agilent.MSAcquisition.HashSignature.ENUM_HASH_DATA_TYPE,
        filePath: str,
    ) -> None: ...
    def VerifyHash(self, path: str, foldersToInclude: str) -> bool: ...
