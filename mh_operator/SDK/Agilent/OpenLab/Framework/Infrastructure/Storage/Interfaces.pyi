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

# Discovered Generic TypeVars:
T = TypeVar("T")

# Stubs for namespace: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces

class AcquiredDateCondition(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition
):  # Class
    def __init__(
        self,
        dateCondition: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange,
    ) -> None: ...

    AcquiredDateSearchRange: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange
    )  # readonly

class AcquisitionOperatorCondition(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition
):  # Class
    def __init__(self, userName: str) -> None: ...

    UserName: str  # readonly

class DateSearchRange:  # Class
    @overload
    def __init__(
        self,
        dateRange: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange,
    ) -> None: ...
    @overload
    def __init__(
        self,
        date: System.DateTime,
        relation: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.DateRelation,
    ) -> None: ...

    Date: Optional[System.DateTime]  # readonly
    DateRange: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange
    )  # readonly
    Relation: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.DateRelation
    )  # readonly

    # Nested Types

    class DateRelation(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        After: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.DateRelation
        ) = ...  # static # readonly
        Before: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.DateRelation
        ) = ...  # static # readonly
        Undefined: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.DateRelation
        ) = ...  # static # readonly

    class FixedDateRange(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        LastMonth: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange
        ) = ...  # static # readonly
        LastWeek: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange
        ) = ...  # static # readonly
        LastYear: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange
        ) = ...  # static # readonly
        ThisMonth: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange
        ) = ...  # static # readonly
        ThisWeek: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange
        ) = ...  # static # readonly
        ThisYear: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange
        ) = ...  # static # readonly
        Today: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange
        ) = ...  # static # readonly
        Undefined: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange
        ) = ...  # static # readonly
        Yesterday: (
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange.FixedDateRange
        ) = ...  # static # readonly

class FileNameCondition(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition
):  # Class
    def __init__(self, fileNamePattern: str) -> None: ...

    FileNamePattern: str  # readonly

class GenericFileAttributes(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Hidden: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFileAttributes
    ) = ...  # static # readonly
    ReadOnly: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFileAttributes
    ) = ...  # static # readonly
    System: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFileAttributes
    ) = ...  # static # readonly

class GenericFileInfo(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFileInfo
):  # Class
    Attributes: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFileAttributes
    )  # readonly
    CreationTime: Optional[System.DateTime]  # readonly
    LastModifiedTime: Optional[System.DateTime]  # readonly
    Length: int  # readonly
    Name: str  # readonly
    Path: str  # readonly

    def IsAttributeSet(
        self,
        attributes: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFileAttributes,
    ) -> bool: ...

class GenericFolderAttributes(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Archived: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes
    ) = ...  # static # readonly
    CanBeProjectFolder: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes
    ) = ...  # static # readonly
    CanBeStorageFolder: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes
    ) = ...  # static # readonly
    CanContainFiles: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes
    ) = ...  # static # readonly
    CreateFolderSupported: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes
    ) = ...  # static # readonly
    ReadOnly: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes
    ) = ...  # static # readonly
    Root: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes
    ) = ...  # static # readonly

class GenericFolderInfo(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFolderInfo
):  # Class
    Attributes: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes
    )  # readonly
    CreationTime: Optional[System.DateTime]  # readonly
    Name: str  # readonly
    Path: str  # readonly

    def IsAttributeSet(
        self,
        attributes: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes,
    ) -> bool: ...

class GenericPathComparer(System.Collections.Generic.IEqualityComparer[str]):  # Class
    def __init__(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        caseSensitive: bool,
    ) -> None: ...
    def GetHashCode(self, obj: str) -> int: ...
    def Equals(self, x: str, y: str) -> bool: ...

class IFileVersionInfo(object):  # Interface
    AbsolutePath: str  # readonly
    CheckinComment: str  # readonly
    Created: Optional[System.DateTime]  # readonly
    CreatedBy: str  # readonly
    FileVersion: str  # readonly
    IsCurrentVersion: bool  # readonly
    VersionLabel: str  # readonly

class IGenericFileInfo(object):  # Interface
    Attributes: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFileAttributes
    )  # readonly
    CreationTime: Optional[System.DateTime]  # readonly
    LastModifiedTime: Optional[System.DateTime]  # readonly
    Length: int  # readonly
    Name: str  # readonly
    Path: str  # readonly

    def IsAttributeSet(
        self,
        attributes: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFileAttributes,
    ) -> bool: ...

class IGenericFolderInfo(object):  # Interface
    Attributes: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes
    )  # readonly
    CreationTime: Optional[System.DateTime]  # readonly
    Name: str  # readonly
    Path: str  # readonly

    def IsAttributeSet(
        self,
        attributes: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.GenericFolderAttributes,
    ) -> bool: ...

class IPathHelper(object):  # Interface
    MaxPathElementLength: int  # readonly
    MaxPathLength: int  # readonly

    def GetRelativePath(self, absolutePath: str, relativeTo: str) -> str: ...
    def GetFileNameWithoutExtension(self, filePath: str) -> str: ...
    def Combine(self, elements: List[str]) -> str: ...
    def Split(self, path: str) -> List[str]: ...
    def GetFileExtension(self, filePath: str) -> str: ...
    def GetDirectoryName(self, path: str) -> str: ...
    def GetFileName(self, filePath: str) -> str: ...
    def IsSubpathOf(self, path: str, subpath: str) -> bool: ...
    def IsPathValid(self, path: str) -> bool: ...
    def GetPathComparer(self) -> System.Collections.Generic.IEqualityComparer[str]: ...
    def GetInvalidPathChars(self) -> List[str]: ...
    def IsPathRooted(self, path: str) -> bool: ...
    def NormalizePath(self, path: str) -> str: ...
    def GetPathWithoutFileName(self, path: str) -> str: ...
    def GetParentFolderName(self, path: str) -> str: ...
    def GetParentFolderPath(self, path: str) -> str: ...
    def GetInvalidFileNameChars(self) -> List[str]: ...

class ISearchCondition(object):  # Interface
    ...

class ISearchParameters(object):  # Interface
    ResultAttributes: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute
    ]  # readonly
    ResultsPerPage: int  # readonly
    SearchQuery: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchQuery
    )  # readonly
    SortAttribute: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute
    )  # readonly
    SortDirection: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchResultSortDirection
    )  # readonly
    StartPage: int  # readonly

class ISearchQuery(object):  # Interface
    SearchConditions: Iterable[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition
    ]  # readonly

    def AddSearchConditions(
        self,
        newSearchConditions: Iterable[
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition
        ],
    ) -> Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchQuery: ...
    def AddSearchCondition(
        self,
        searchCondition: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition,
    ) -> Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchQuery: ...

class ISearchResult(object):  # Interface
    Path: str  # readonly

    def GetResultsValueAsString(
        self,
        searchAttribute: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute,
    ) -> str: ...
    def GetResultsValue(
        self,
        searchAttribute: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute[
            T
        ],
    ) -> T: ...
    def HasResultsValue(
        self,
        searchAttribute: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute,
    ) -> bool: ...

class ISearchResults(object):  # Interface
    HasMoreResults: bool  # readonly
    Results: Iterable[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchResult
    ]  # readonly

class ISearchable(object):  # Interface
    def Search(
        self,
        searchParameters: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchParameters,
    ) -> Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchResults: ...
    def SearchAsync(
        self,
        searchParameters: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchParameters,
        cancellationToken: System.Threading.CancellationToken,
    ) -> System.Threading.Tasks.Task[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchResults
    ]: ...

class IStorageBrowser(object):  # Interface
    RootFolderNames: Iterable[str]  # readonly

    def GetFolderPathNamesAsync(
        self,
        folderPath: str,
        searchPattern: str,
        cancellationToken: System.Threading.CancellationToken,
    ) -> System.Threading.Tasks.Task[List[str]]: ...
    def GetFileVersionsAsync(
        self, filePath: str, cancellationToken: System.Threading.CancellationToken
    ) -> System.Threading.Tasks.Task[
        List[
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IFileVersionInfo
        ]
    ]: ...
    def GetRootFolder(
        self, path: str
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFolderInfo
    ): ...
    def GetFilePathNames(
        self, folderPath: str, searchPattern: str = ...
    ) -> List[str]: ...
    def GetFolderInfos(
        self, folderPath: str
    ) -> List[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFolderInfo
    ]: ...
    def GetFileInfoAsync(
        self, filePath: str, cancellationToken: System.Threading.CancellationToken
    ) -> System.Threading.Tasks.Task[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFileInfo
    ]: ...
    def GetFileInfo(
        self, filePath: str
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFileInfo
    ): ...
    def GetCurrentDirectory(
        self,
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFolderInfo
    ): ...
    def GetFileVersions(
        self, filePath: str
    ) -> List[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IFileVersionInfo
    ]: ...
    def GetFilePathNamesAsync(
        self,
        folderPath: str,
        searchPattern: str,
        cancellationToken: System.Threading.CancellationToken,
    ) -> System.Threading.Tasks.Task[List[str]]: ...
    def GetLastestFileVersion(
        self, filePath: str
    ) -> Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo: ...
    def GetFileInfos(
        self, folderPath: str
    ) -> List[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFileInfo
    ]: ...
    def GetFolderInfo(
        self, folderPath: str
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFolderInfo
    ): ...
    @overload
    def GetFileMetaData(self, filePath: str) -> str: ...
    @overload
    def GetFileMetaData(
        self,
        filePath: str,
        version: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
    ) -> str: ...
    def GetFolderPathNames(
        self, folderPath: str, searchPattern: str = ...
    ) -> List[str]: ...
    def GetParentFolder(
        self, fileOrFolderPath: str
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFolderInfo
    ): ...

class IStorageCapabilities(object):  # Interface
    SupportsSearch: bool  # readonly
    SupportsVersions: bool  # readonly

class IStorageFileAccess(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper
):  # Interface
    def ExistsAsync(
        self, path: str, cancellationToken: System.Threading.CancellationToken
    ) -> System.Threading.Tasks.Task[bool]: ...
    def IsFolder(self, path: str) -> bool: ...
    def IsFile(self, path: str) -> bool: ...
    @overload
    def OpenFile(self, path: str) -> System.IO.Stream: ...
    @overload
    def OpenFile(
        self,
        path: str,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
    ) -> System.IO.Stream: ...
    def IsFileAsync(
        self, path: str, cancellationToken: System.Threading.CancellationToken
    ) -> System.Threading.Tasks.Task[bool]: ...
    def IsFolderAsync(
        self, path: str, cancellationToken: System.Threading.CancellationToken
    ) -> System.Threading.Tasks.Task[bool]: ...
    def Exists(self, path: str) -> bool: ...
    @overload
    def OpenFileAsync(
        self, path: str, cancellationToken: System.Threading.CancellationToken = ...
    ) -> System.Threading.Tasks.Task[System.IO.Stream]: ...
    @overload
    def OpenFileAsync(
        self,
        path: str,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
        cancellationToken: System.Threading.CancellationToken = ...,
    ) -> System.Threading.Tasks.Task[System.IO.Stream]: ...
    @overload
    def SaveFile(self, path: str, data: System.IO.Stream) -> None: ...
    @overload
    def SaveFile(
        self,
        path: str,
        data: System.IO.Stream,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
    ) -> None: ...
    def DeleteFile(self, path: str) -> None: ...

class IStorageFileSetAccess(object):  # Interface
    def RemoveFileAsync(
        self, fileSetPath: str, fileNameOrPath: str
    ) -> System.Threading.Tasks.Task[None]: ...
    @overload
    def AddFileAsync(
        self, fileSetPath: str, fileNameOrPath: str
    ) -> System.Threading.Tasks.Task[None]: ...
    @overload
    def AddFileAsync(
        self,
        fileSetPath: str,
        fileNameOrPath: str,
        version: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
    ) -> System.Threading.Tasks.Task[None]: ...
    def GetFileVersion(
        self, fileSetPath: str, fileNameOrPath: str
    ) -> Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo: ...
    @overload
    def SetVersionAsync(
        self,
        fileSetPath: str,
        fileNameOrPath: str,
        version: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
    ) -> System.Threading.Tasks.Task[None]: ...
    @overload
    def SetVersionAsync(
        self,
        fileSetPath: str,
        fileNamesOrPaths: Iterable[str],
        version: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
    ) -> System.Threading.Tasks.Task[None]: ...
    @overload
    def SetVersionAsync(
        self,
        fileSetPath: str,
        versionMap: Mapping[
            str, Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo
        ],
    ) -> System.Threading.Tasks.Task[None]: ...
    def GetFileVersions(
        self, fileSetPath: str
    ) -> Mapping[
        str, Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo
    ]: ...
    def CreateFileSet(self, fileSetPath: str) -> None: ...
    def BufferedUploadFileSetAsync(
        self,
        fileSetPath: str,
        version: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
    ) -> System.Threading.Tasks.Task[None]: ...
    def UploadFileSetAsync(
        self,
        fileSetPath: str,
        version: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
        cancellationToken: System.Threading.CancellationToken,
    ) -> System.Threading.Tasks.Task[None]: ...

class IStorageProvider(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageBrowser,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageRepositoryAccess,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageFileAccess,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchable,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageCapabilities,
):  # Interface
    DefaultWorkArea: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageWorkAreaAccess
    )  # readonly
    Id: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.StorageType
    )  # readonly

    def CloseWorkArea(self, workAreaName: str) -> None: ...
    @overload
    def GetWorkArea(
        self, workAreaName: str
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageWorkAreaAccess
    ): ...
    @overload
    def GetWorkArea(
        self, hostname: str, workAreaName: str
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageWorkAreaAccess
    ): ...
    def IsStorageAvailableAsync(
        self, cancellationToken: System.Threading.CancellationToken
    ) -> System.Threading.Tasks.Task[System.Tuple[bool, str]]: ...

class IStorageRepositoryAccess(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageFileAccess,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
):  # Interface
    @overload
    def CreateFolder(
        self, folderPath: str
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFolderInfo
    ): ...
    @overload
    def CreateFolder(
        self, parentFolderPath: str, newFolderName: str
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFolderInfo
    ): ...
    @overload
    def OpenFile(self, path: str, workAreaName: str) -> System.IO.Stream: ...
    @overload
    def OpenFile(
        self,
        path: str,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
        workAreaName: str,
    ) -> System.IO.Stream: ...
    @overload
    def OpenFileAsync(
        self,
        path: str,
        workAreaName: str,
        cancellationToken: System.Threading.CancellationToken,
    ) -> System.Threading.Tasks.Task[System.IO.Stream]: ...
    @overload
    def OpenFileAsync(
        self,
        path: str,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
        workAreaName: str,
        cancellationToken: System.Threading.CancellationToken,
    ) -> System.Threading.Tasks.Task[System.IO.Stream]: ...
    @overload
    def SaveFileBuffered(self, path: str, data: System.IO.Stream) -> None: ...
    @overload
    def SaveFileBuffered(
        self, path: str, data: System.IO.Stream, workAreaName: str
    ) -> None: ...
    @overload
    def SaveFileBuffered(
        self,
        path: str,
        data: System.IO.Stream,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
    ) -> None: ...
    @overload
    def SaveFileBuffered(
        self,
        path: str,
        data: System.IO.Stream,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
        workAreaName: str,
    ) -> None: ...
    @overload
    def SaveFile(
        self, path: str, data: System.IO.Stream, workAreaName: str
    ) -> None: ...
    @overload
    def SaveFile(
        self,
        path: str,
        data: System.IO.Stream,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
        workAreaName: str,
    ) -> None: ...
    def CreateFolderAsync(
        self,
        folderPath: str,
        cancellationToken: System.Threading.CancellationToken = ...,
    ) -> System.Threading.Tasks.Task[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFolderInfo
    ]: ...
    def DeleteFolder(self, folderPath: str) -> None: ...

class IStorageRepositoryTransfer(object):  # Interface
    @overload
    def DownloadFile(self, path: str) -> None: ...
    @overload
    def DownloadFile(
        self,
        path: str,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
    ) -> None: ...
    @overload
    def UploadFileAsync(
        self, path: str, cancellationToken: System.Threading.CancellationToken = ...
    ) -> System.Threading.Tasks.Task[None]: ...
    @overload
    def UploadFileAsync(
        self,
        path: str,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
        cancellationToken: System.Threading.CancellationToken = ...,
    ) -> System.Threading.Tasks.Task[None]: ...
    @overload
    def DownloadFileAsync(
        self, path: str, cancellationToken: System.Threading.CancellationToken = ...
    ) -> System.Threading.Tasks.Task[None]: ...
    @overload
    def DownloadFileAsync(
        self,
        path: str,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
        cancellationToken: System.Threading.CancellationToken = ...,
    ) -> System.Threading.Tasks.Task[None]: ...
    def RequiresUpload(self, path: str) -> bool: ...
    @overload
    def UploadFileBufferedAsync(
        self, path: str
    ) -> System.Threading.Tasks.Task[None]: ...
    @overload
    def UploadFileBufferedAsync(
        self,
        path: str,
        versionInfo: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo,
    ) -> System.Threading.Tasks.Task[None]: ...

class IStorageWorkAreaAccess(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageFileAccess,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageFileSetAccess,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageRepositoryTransfer,
):  # Interface
    Name: str  # readonly

    @overload
    def ExportFile(self, sourcePath: str) -> str: ...
    @overload
    def ExportFile(self, sourcePath: str, targetPath: str) -> None: ...
    def GetFiles(self, folderPath: str) -> Iterable[str]: ...
    def CopyFile(self, sourcePath: str, targetPath: str) -> None: ...
    def GetHashValue(self, filePath: str) -> str: ...
    def CreateFile(self, path: str) -> System.IO.Stream: ...
    def MoveFile(self, sourcePath: str, targetPath: str) -> None: ...
    def OpenWrite(self, path: str) -> System.IO.Stream: ...
    def ImportFile(self, sourcePath: str, targetPath: str) -> None: ...
    def GetFolders(self, folderPath: str) -> Iterable[str]: ...

class ITransferProcess(System.IAsyncResult):  # Interface
    IsCanceled: bool  # readonly
    PercentOfProgress: int  # readonly

class IVersionStorageProvider(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageProvider,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageBrowser,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageRepositoryAccess,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageFileAccess,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchable,
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IStorageCapabilities,
):  # Interface
    def GetVersionedFileInfo(
        self, filePath: str
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IVersionedFileInfo
    ): ...
    @overload
    def GetFileHistory(
        self, filePath: str
    ) -> List[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IFileVersionInfo
    ]: ...
    @overload
    def GetFileHistory(
        self, filePath: str, versionLabel: str
    ) -> List[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IFileVersionInfo
    ]: ...
    def GetVersionedFolderInfos(
        self, folderPath: str
    ) -> List[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IVersionedFolderInfo
    ]: ...
    def GetVersionedFileInfos(
        self, folderPath: str
    ) -> List[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IVersionedFileInfo
    ]: ...
    def GetVersionedFolderInfo(
        self, folderPath: str
    ) -> (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IVersionedFolderInfo
    ): ...

class IVersionedFileInfo(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFileInfo
):  # Interface
    CheckoutBy: str  # readonly
    StateAttributes: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionedState
    )  # readonly
    VersionLabel: str  # readonly

class IVersionedFolderInfo(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IGenericFolderInfo
):  # Interface
    CreatedBy: str  # readonly
    LastModifiedBy: str  # readonly

class LastProcessedDateCondition(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition
):  # Class
    def __init__(
        self,
        dateSearchRange: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange,
    ) -> None: ...

    LastProcessedDateSearchRange: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.DateSearchRange
    )  # readonly

class MethodContentType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Unknown: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.MethodContentType
    ) = ...  # static # readonly

class MethodStatusType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Draft: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.MethodStatusType
    ) = ...  # static # readonly
    Final: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.MethodStatusType
    ) = ...  # static # readonly
    Reviewed: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.MethodStatusType
    ) = ...  # static # readonly

class PathCondition(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition
):  # Class
    def __init__(self, path: str) -> None: ...

    Path: str  # readonly

class ResultContentType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Sequence: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ResultContentType
    ) = ...  # static # readonly
    SingleSample: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ResultContentType
    ) = ...  # static # readonly
    Undefined: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ResultContentType
    ) = ...  # static # readonly

class SaveOptions:  # Class
    def __init__(self) -> None: ...

    Reason: str
    UploadMode: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.UploadMode
    Version: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionInfo
    WorkAreaName: str

class SearchAttribute:  # Class
    Name: str  # readonly

class SearchAttribute(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute,
    Generic[T],
):  # Class
    def __init__(self, name: str) -> None: ...

    SearchAttributeType: System.Type  # readonly

class SearchAttributes:  # Class
    AcquisitionInstrument: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute[str]
    )  # static # readonly
    AcquisitionOperator: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute[str]
    )  # static # readonly
    AcquisitionTime: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute[
            System.DateTime
        ]
    )  # static # readonly
    FileName: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute[str]
    )  # static # readonly
    FilePath: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute[str]
    )  # static # readonly
    ResultContentType: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ResultContentType
    ]  # static # readonly
    SampleName: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute[str]
    )  # static # readonly
    SequenceName: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute[str]
    )  # static # readonly

class SearchParameters(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchParameters
):  # Class
    @overload
    def __init__(
        self,
        resultsPerPage: int,
        searchQuery: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchQuery,
        startPage: int,
    ) -> None: ...
    @overload
    def __init__(
        self,
        resultsPerPage: int,
        searchQuery: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchQuery,
        startPage: int,
        resultAttributes: System.Collections.Generic.List[
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute
        ],
        sortAttribute: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute,
        sortDirection: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchResultSortDirection,
    ) -> None: ...

    ResultAttributes: System.Collections.Generic.List[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute
    ]
    ResultsPerPage: int
    SearchQuery: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchQuery
    )
    SortAttribute: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchAttribute
    )
    SortDirection: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchResultSortDirection
    )
    StartPage: int

class SearchQuery(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchQuery
):  # Class
    def __init__(self) -> None: ...

    SearchConditions: Iterable[
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition
    ]  # readonly

    def AddSearchConditions(
        self,
        newSearchConditions: Iterable[
            Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition
        ],
    ) -> Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchQuery: ...
    def AddSearchCondition(
        self,
        searchCondition: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition,
    ) -> Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchQuery: ...

class SearchResultSortDirection(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Ascending: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchResultSortDirection
    ) = ...  # static # readonly
    Descending: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.SearchResultSortDirection
    ) = ...  # static # readonly

class StorageType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DataStore: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.StorageType
    ) = ...  # static # readonly
    Local: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.StorageType = (
        ...
    )  # static # readonly
    Unsupported: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.StorageType
    ) = ...  # static # readonly

class UploadMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Buffered: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.UploadMode = (
        ...
    )  # static # readonly
    Immediate: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.UploadMode
    ) = ...  # static # readonly

class VerbatimCondition(
    Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.ISearchCondition
):  # Class
    def __init__(self, queryText: str) -> None: ...

    QueryText: str  # readonly

class VersionInfo:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, label: str) -> None: ...
    @overload
    def __init__(self, label: str, timestamp: System.DateTime) -> None: ...
    @overload
    def __init__(self, timestamp: System.DateTime) -> None: ...

    VersionLabel: str  # readonly

class VersionedState(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CheckedOut: (
        Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.VersionedState
    ) = ...  # static # readonly
