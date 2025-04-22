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
from . import BatchAttributes, ProgressEventArgs

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance

class AuditTrail(System.IDisposable):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

    CmdNameEditReportMethod: str = ...  # static # readonly
    CmdNameGenerateMethodReport: str = ...  # static # readonly
    CmdNameGenerateReport: str = ...  # static # readonly
    CmdNameValidateUser: str = ...  # static # readonly

    BatchFilePath: str  # readonly
    IsLocked: bool  # readonly
    IsReadOnly: bool  # readonly
    IsTrailing: bool  # readonly

    def AfterNewBatch(self, error: bool) -> None: ...
    def BeforeSaveBatchAs(
        self, batchPath: str, batchFile: str, revisionNumber: str
    ) -> None: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def GetLocalAuditFilePath(
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        batchPath: str,
        batchFile: str,
        revisionNumber: str,
    ) -> str: ...
    def Lock(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet
    ): ...
    def Save(self, batchHashCode: str) -> None: ...
    def BeforeNewBatch(
        self, batchPath: str, batchFile: str, auditTrail: bool, deleteIfExists: bool
    ) -> None: ...
    def BeforeSaveBatch(self) -> None: ...
    def Unlock(self) -> None: ...
    def AfterSaveBatchAs(self, batchHashCode: str, error: bool) -> None: ...
    def AfterOpenBatch(self, error: bool) -> None: ...
    def BeforeCloseBatch(self) -> None: ...
    def AfterCloseBatch(self, error: bool) -> None: ...
    def AfterSaveBatch(self, batchHashCode: str, error: bool) -> None: ...
    def BeforeOpenBatch(
        self,
        batchPath: str,
        batchFile: str,
        revisionNumber: str,
        readOnly: bool,
        batchHashCode: str,
        schemaVersion: int,
    ) -> None: ...
    def AddEntry(
        self,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
        exception: System.Exception,
        reason: str,
    ) -> None: ...

class AuditTrailDataSet(
    System.IDisposable,
    System.ComponentModel.ISupportInitializeNotification,
    System.IServiceProvider,
    System.Data.DataSet,
    System.Xml.Serialization.IXmlSerializable,
    System.Runtime.Serialization.ISerializable,
    System.ComponentModel.IListSource,
    System.ComponentModel.ISupportInitialize,
    System.ComponentModel.IComponent,
):  # Class
    def __init__(self) -> None: ...

    Entry: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryDataTable
    )  # readonly
    Relations: System.Data.DataRelationCollection  # readonly
    SchemaSerializationMode: System.Data.SchemaSerializationMode
    Tables: System.Data.DataTableCollection  # readonly

    @staticmethod
    def GetTypedDataSetSchema(
        xs: System.Xml.Schema.XmlSchemaSet,
    ) -> System.Xml.Schema.XmlSchemaComplexType: ...
    def Clone(self) -> System.Data.DataSet: ...

    # Nested Types

    class EntryDataTable(
        System.ComponentModel.ISupportInitialize,
        Iterable[Any],
        System.ComponentModel.ISupportInitializeNotification,
        System.Xml.Serialization.IXmlSerializable,
        System.ComponentModel.IComponent,
        System.Runtime.Serialization.ISerializable,
        System.Data.TypedTableBase[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRow
        ],
        Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRow
        ],
        System.ComponentModel.IListSource,
        System.IDisposable,
        System.IServiceProvider,
    ):  # Class
        def __init__(self) -> None: ...

        ActionColumn: System.Data.DataColumn  # readonly
        CommentColumn: System.Data.DataColumn  # readonly
        Count: int  # readonly
        ExceptionColumn: System.Data.DataColumn  # readonly
        IDColumn: System.Data.DataColumn  # readonly
        InSessionColumn: System.Data.DataColumn  # readonly
        def __getitem__(
            self, index: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRow
        ): ...
        MessageColumn: System.Data.DataColumn  # readonly
        NameColumn: System.Data.DataColumn  # readonly
        ReasonColumn: System.Data.DataColumn  # readonly
        SucceededColumn: System.Data.DataColumn  # readonly
        TimeColumn: System.Data.DataColumn  # readonly
        UserColumn: System.Data.DataColumn  # readonly

        def RemoveEntryRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRow,
        ) -> None: ...
        @staticmethod
        def GetTypedTableSchema(
            xs: System.Xml.Schema.XmlSchemaSet,
        ) -> System.Xml.Schema.XmlSchemaComplexType: ...
        @overload
        def AddEntryRow(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRow,
        ) -> None: ...
        @overload
        def AddEntryRow(
            self,
            ID: int,
            Name: str,
            User: str,
            Time: System.DateTime,
            Action: str,
            Reason: str,
            Comment: str,
            Succeeded: bool,
            Message: str,
            Exception: str,
            InSession: bool,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRow
        ): ...
        def NewEntryRow(
            self,
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRow
        ): ...
        def Clone(self) -> System.Data.DataTable: ...
        def FindByID(
            self, ID: int
        ) -> (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRow
        ): ...

        EntryRowChanged: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRowChangeEventHandler
        )  # Event
        EntryRowChanging: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRowChangeEventHandler
        )  # Event
        EntryRowDeleted: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRowChangeEventHandler
        )  # Event
        EntryRowDeleting: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRowChangeEventHandler
        )  # Event

    class EntryRow(System.Data.DataRow):  # Class
        Action: str
        Comment: str
        Exception: str
        ID: int
        InSession: bool
        Message: str
        Name: str
        Reason: str
        Succeeded: bool
        Time: System.DateTime
        User: str

        def SetTimeNull(self) -> None: ...
        def IsExceptionNull(self) -> bool: ...
        def IsUserNull(self) -> bool: ...
        def SetUserNull(self) -> None: ...
        def SetCommentNull(self) -> None: ...
        def SetActionNull(self) -> None: ...
        def IsNameNull(self) -> bool: ...
        def IsSucceededNull(self) -> bool: ...
        def IsInSessionNull(self) -> bool: ...
        def IsCommentNull(self) -> bool: ...
        def SetInSessionNull(self) -> None: ...
        def SetSucceededNull(self) -> None: ...
        def IsMessageNull(self) -> bool: ...
        def SetNameNull(self) -> None: ...
        def IsTimeNull(self) -> bool: ...
        def SetExceptionNull(self) -> None: ...
        def SetMessageNull(self) -> None: ...
        def IsActionNull(self) -> bool: ...
        def IsReasonNull(self) -> bool: ...
        def SetReasonNull(self) -> None: ...

    class EntryRowChangeEvent(System.EventArgs):  # Class
        def __init__(
            self,
            row: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRow,
            action: System.Data.DataRowAction,
        ) -> None: ...

        Action: System.Data.DataRowAction  # readonly
        Row: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRow
        )  # readonly

    class EntryRowChangeEventHandler(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRowChangeEvent,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self,
            sender: Any,
            e: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet.EntryRowChangeEvent,
        ) -> None: ...

class AuditTrailException(
    System.Runtime.InteropServices._Exception,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceException,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, msg: str) -> None: ...
    @overload
    def __init__(self, msg: str, innerException: System.Exception) -> None: ...

class AuditTrailFile(System.IDisposable):  # Class
    BatchExtensionBin: str  # static
    BatchExtensionXml: str  # static
    FileExtention: str = ...  # static # readonly
    SsizipExtension: str  # static
    Tag_BatchHashCode: str = ...  # static # readonly
    Tag_HashCode: str = ...  # static # readonly
    Tag_Root: str = ...  # static # readonly
    Tag_Version: str = ...  # static # readonly

    def Dispose(self) -> None: ...
    def Load(
        self,
        stream: System.IO.Stream,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet,
        isInSession: bool,
    ) -> None: ...

class AuditTrailFileBase(System.IDisposable):  # Class
    def __init__(self) -> None: ...

    Tag_HashCode: str = ...  # static # readonly
    Tag_Root: str = ...  # static # readonly
    Tag_Version: str = ...  # static # readonly

    IsReadOnly: bool  # readonly
    IsTrailing: bool  # readonly

    def Create(self, pathName: str, deleteIfExists: bool) -> None: ...
    def Save(self, dataHashCodeTag: str, dataHashCode: str) -> None: ...
    def LoadInSessionEntriesTo(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet,
    ) -> None: ...
    def Open(
        self,
        pathName: str,
        isReadOnly: bool,
        dataHashCodeTag: str,
        dataHashCodeToCheck: str,
    ) -> None: ...
    def Clean(self) -> None: ...
    def LoadTo(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet,
    ) -> None: ...
    def SaveAs(
        self, pathName: str, dataHashCodeTag: str, dataHashCode: str
    ) -> None: ...
    def Dispose(self) -> None: ...
    def AddEntry(
        self,
        user: str,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
        exception: System.Exception,
        reason: str,
    ) -> None: ...

class Command:  # Class
    def __init__(self) -> None: ...

    Name: str
    PrivilegeID: int
    RequireReason: bool
    RequireUserValidation: bool
    Roles: List[str]

class CommandGroup:  # Class
    def __init__(self) -> None: ...

    Commands: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.Command
    ]
    Name: str

class CommandPermissionException(
    System.Runtime.InteropServices._Exception,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceException,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, msg: str) -> None: ...
    @overload
    def __init__(self, msg: str, innerException: System.Exception) -> None: ...

class CommandPrincipalBase(System.IDisposable):  # Class
    LogonRequired: bool  # readonly
    User: str  # readonly

    @overload
    def Logon(self, user: str, domain: str, pwd: str) -> None: ...
    @overload
    def Logon(
        self, user: str, domain: str, pwd: System.Security.SecureString
    ) -> None: ...
    def DuplicateFrom(
        self,
        pricipal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.CommandPrincipalBase,
    ) -> None: ...
    def Copy(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.CommandPrincipalBase
    ): ...
    @overload
    def Validate(self, user: str, pwd: str) -> None: ...
    @overload
    def Validate(self, user: str, pwd: System.Security.SecureString) -> None: ...
    def IsInRole(self, role: str) -> bool: ...
    def Dispose(self) -> None: ...

class CommandWindowsPrincipal(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.CommandPrincipalBase,
):  # Class
    def __init__(self) -> None: ...

    LogonRequired: bool  # readonly
    User: str  # readonly

    @overload
    def Logon(
        self, user: str, domain: str, pwd: System.Security.SecureString
    ) -> None: ...
    @overload
    def Logon(self, user: str, domain: str, pwd: str) -> None: ...
    def DuplicateFrom(
        self,
        pricipal: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.CommandPrincipalBase,
    ) -> None: ...
    def Copy(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.CommandPrincipalBase
    ): ...
    def Impersonate(self) -> System.IDisposable: ...
    @overload
    def Validate(self, user: str, pwd: str) -> None: ...
    @overload
    def Validate(self, user: str, pwd: System.Security.SecureString) -> None: ...
    def IsInRole(self, role: str) -> bool: ...

class ComplianceConfiguration:  # Class
    def __init__(self) -> None: ...

    AlwaysAuditTrail: bool
    DateTime: System.DateTime
    Groups: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.CommandGroup
    ]
    LockApplication: bool
    LockApplicationInterval: int
    LogonRequired: bool
    Redirect: str
    Roles: List[str]
    User: str

    def CheckAndRecover(self) -> None: ...
    def DebugCheck(self) -> None: ...

class ComplianceConfigurationFile:  # Class
    DefaultFilePath: str  # static # readonly

    @overload
    @staticmethod
    def Load(
        path: str, checkHash: bool, recover: bool
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration
    ): ...
    @overload
    @staticmethod
    def Load(
        stream: System.IO.Stream, checkHash: bool, recover: bool
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration
    ): ...
    @staticmethod
    def MergeCommands(
        from_: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration,
        to: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration,
    ) -> None: ...
    @staticmethod
    def GetHiddenCommands() -> List[str]: ...
    @staticmethod
    def CreateDefault() -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration
    ): ...
    @staticmethod
    def IsHiddenCommand(command: str) -> bool: ...
    @overload
    @staticmethod
    def Save(
        path: str,
        map: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration,
    ) -> None: ...
    @overload
    @staticmethod
    def Save(
        stream: System.IO.Stream,
        map: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration,
    ) -> None: ...

class ComplianceException(
    System.Security.SecurityException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, msg: str) -> None: ...
    @overload
    def __init__(self, msg: str, innerException: System.Exception) -> None: ...

class ComplianceFactory:  # Class
    IsInstalled: bool  # static # readonly

    @overload
    @staticmethod
    def CreateInstance(
        name: str,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance: ...
    @overload
    @staticmethod
    def CreateInstance() -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance
    ): ...
    @overload
    @staticmethod
    def CreateInstance(
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance: ...
    @staticmethod
    def Install(type: str) -> None: ...
    @staticmethod
    def GetActiveType() -> str: ...
    @staticmethod
    def GetLogonType() -> int: ...

class ComplianceUtils:  # Class
    @overload
    @staticmethod
    def IsBatchAuditTrail(
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        batchPath: str,
        batchFile: str,
    ) -> bool: ...
    @overload
    @staticmethod
    def IsBatchAuditTrail(
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        batchPath: str,
        batchFile: str,
        batchHashCode: str,
        schemaVersion: int,
    ) -> bool: ...
    @staticmethod
    def ToSecureString(str: str) -> System.Security.SecureString: ...
    @staticmethod
    def ReadBatchHeader(
        batchFilePath: str,
        schemaVersion: int,
        hashCode: str,
        isAuditTrail: bool,
        attrs: BatchAttributes,
    ) -> bool: ...
    @staticmethod
    def DecryptPassword(encrypted: str) -> System.Security.SecureString: ...

class FileInfo(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IFileInfo
):  # Class
    def __init__(self) -> None: ...

    DateCreated: Optional[System.DateTime]
    DateModified: Optional[System.DateTime]
    DateUploaded: Optional[System.DateTime]
    Name: str
    Path: str

class IAuditTrail(object):  # Interface
    AlwaysAuditTrail: bool  # readonly
    IsAuditTrailing: bool  # readonly
    IsReadOnly: bool  # readonly

    def AddEntry(
        self,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
        exception: System.Exception,
    ) -> None: ...
    def SaveAuditTrail(self) -> None: ...
    def UnlockAuditTrail(self) -> None: ...
    def LockAuditTrail(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet
    ): ...

class IBatchFileService(object):  # Interface
    DefaultDataFolder: str  # readonly

    def BeforeNewBatch(
        self, batchFolder: str, batchFile: str, auditTrail: bool
    ) -> None: ...
    def TranslateMethodToLocalPath(
        self, methodPath: str, revisionNumber: str
    ) -> str: ...
    def AfterNewBatch(self, error: bool) -> None: ...
    def AfterOpenBatch(self, error: bool) -> None: ...
    def UploadMethod(self, methodFile: str, revisionNumber: str) -> None: ...
    def CheckoutBatch(self, batchFolder: str, batchFile: str) -> None: ...
    def AfterSaveBatchAs(self, batchHashCode: str, hasError: bool) -> None: ...
    def BeforeClose(self) -> None: ...
    def PrepareLibrary(self, libraryPath: str, revisionNumber: str) -> None: ...
    def GetSampleFileNames(self, batchFolder: str) -> List[str]: ...
    def MethodExists(self, methodPath: str) -> bool: ...
    def BatchFileExists(self, batchFolder: str, batchFile: str) -> bool: ...
    def AfterSaveBatch(self, batchHashCode: str, hasError: bool) -> None: ...
    def UndoCheckoutBatch(self, batchFolder: str, batchFile: str) -> None: ...
    def BeforeOpenBatch(
        self, batchFolder: str, batchFile: str, readOnly: bool, revisionNumber: str
    ) -> None: ...
    def GetBatchFiles(self, folder: str) -> List[str]: ...
    def GetLatestMethodRevisionNumber(self, methodPath: str) -> str: ...
    def GetSampleInfo(self, samplePath: str) -> Dict[str, Any]: ...
    def LibraryExists(self, libratyPath: str) -> bool: ...
    def TranslateBatchToLocalPath(
        self, batchFilePath: str, revisionNumber: str
    ) -> str: ...
    def GetMethodHistory(
        self, methodPath: str
    ) -> Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IRevisionHistory
    ]: ...
    def BeforeSaveBatchAs(self, batchFolder: str, batchFile: str) -> None: ...
    def GetLatestLibraryRevisionNumber(self, libraryPath: str) -> str: ...
    def GetBatchFileInfos(
        self, folder: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IFileInfo
    ]: ...
    def IsMethodFolder(self, methodPath: str) -> bool: ...
    def AfterClose(self, hasError: bool) -> None: ...
    def UploadLibrary(self, libraryPath: str, revisionNumber: str) -> None: ...
    def IsBatchCheckedoutByCurrentUser(
        self, batchFolder: str, batchFile: str
    ) -> bool: ...
    def BeforeSaveBatch(self) -> None: ...
    def AfterCloseMethod(self, methodFile: str) -> None: ...
    def PrepareMethod(self, methodPath: str, revisionNumber: str) -> None: ...
    def SampleFileExists(self, samplePath: str) -> bool: ...
    def GetBatchFilePath(self, batchFolder: str, batchFile: str) -> str: ...
    def PrepareSamples(self, samplePathes: List[str]) -> None: ...
    def PrepareBatch(
        self, batchFolder: str, batchFile: str, progress: System.Action[int, int, str]
    ) -> None: ...
    def GetLatestBatchRevisionNumber(self, batchFolder: str, batchFile: str) -> str: ...

    Progress: System.EventHandler[ProgressEventArgs]  # Event

class ICommandPermission(object):  # Interface
    CommandReason: str
    IsInCommandGroup: bool  # readonly
    UserValidated: bool  # readonly
    UserValidationExecuted: bool

    def UserValidationRequiredCore(self, commandName: str) -> bool: ...
    @overload
    def CheckPreCommandCondition(
        self,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    ) -> None: ...
    @overload
    def CheckPreCommandCondition(self, commandName: str) -> None: ...
    def BeginCommandGroup(self) -> None: ...
    def CommandReasonRequiredCore(self, commandName: str) -> bool: ...
    @overload
    def DemandPermission(
        self,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    ) -> None: ...
    @overload
    def DemandPermission(self, commandName: str) -> None: ...
    def EndCommandGroup(self) -> None: ...
    def CommandReasonRequired(self, commandName: str) -> bool: ...
    @overload
    def HasPermission(
        self,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    ) -> bool: ...
    @overload
    def HasPermission(self, commandName: str) -> bool: ...
    def ValidateUser(
        self, user: str, password: System.Security.SecureString
    ) -> None: ...
    def UserValidationRequired(self, commandName: str) -> bool: ...

    CommandGroupEnded: System.EventHandler  # Event
    CommandGroupStarted: System.EventHandler  # Event

class ICompliance(System.IDisposable):  # Interface
    AuditTrail: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IAuditTrail
    )  # readonly
    BatchFileService: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IBatchFileService
    )  # readonly
    CommandPermission: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICommandPermission
    )  # readonly
    DataStorage: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IDataStorage
    )  # readonly
    DisplayName: str  # readonly
    IsActive: bool  # readonly
    IsLocal: bool  # readonly
    LogonInfo: str  # readonly
    LogonRequired: bool  # readonly
    Name: str  # readonly
    ReportFileService: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IReportFileService
    )  # readonly
    Server: str  # readonly
    UnknownsFileService: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IUnknownsFileService
    )  # readonly
    UserName: str  # readonly
    Version: str  # readonly

    def GetToken(self) -> str: ...
    def GetService(self) -> T: ...
    def Impersonate(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IImpersonationContext
    ): ...
    def CheckConnection(self) -> None: ...
    def CommandEnd(
        self,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    ) -> None: ...
    def InitQuantCommandPermission(self) -> None: ...
    def GetUI(self) -> T: ...
    def LogonXml(self, xml: str) -> None: ...
    @overload
    def Connect(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...
    @overload
    def Connect(self, token: str) -> None: ...
    def ValidateUser(
        self, user: str, password: System.Security.SecureString
    ) -> None: ...
    def CommandStart(
        self,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
    ) -> None: ...

class IComplianceCommand(object):  # Interface
    ActionString: str  # readonly
    Name: str  # readonly

class IComplianceCommandEx(object):  # Interface
    ActionStrings: List[str]  # readonly

class IComplianceLightCommand(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand
):  # Interface
    ...

class IDataStorage(System.IDisposable):  # Interface
    InitialRevisionNumber: str  # readonly
    IsRevisionSupported: bool  # readonly
    OpenFolderSupported: bool  # readonly
    PathSeparator: str  # readonly

    def GetLatestRevisionNumber(self, path: str) -> str: ...
    @overload
    def UploadFile(self, pathName: str) -> None: ...
    @overload
    def UploadFile(self, pathName: str, revisionNumber: str) -> None: ...
    def Combine(self, paths: List[str]) -> str: ...
    @overload
    def DownloadFile(self, pathName: str) -> None: ...
    @overload
    def DownloadFile(self, pathName: str, revisionNumber: str) -> None: ...
    def GetFiles(self, folder: str, searchPattern: str) -> List[str]: ...
    def GetFolderPathName(self, pathName: str) -> str: ...
    def GetFileName(self, pathName: str) -> str: ...
    def GetHistory(
        self, path: str
    ) -> Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IRevisionHistory
    ]: ...
    def GetNextRevisionNumber(self, path: str) -> str: ...
    @overload
    def TranslateToLocalPath(self, path: str) -> str: ...
    @overload
    def TranslateToLocalPath(self, path: str, revisionNumber: str) -> str: ...
    def FileExists(self, path: str) -> bool: ...
    def OpenFolder(self, folderPath: str) -> None: ...
    def FolderExists(self, path: str) -> bool: ...
    def GetFolders(self, folder: str, searchPattern: str) -> List[str]: ...

class IFileInfo(object):  # Interface
    DateCreated: Optional[System.DateTime]  # readonly
    DateModified: Optional[System.DateTime]  # readonly
    DateUploaded: Optional[System.DateTime]  # readonly
    Name: str  # readonly
    Path: str  # readonly

class IFolderInfo(object):  # Interface
    DateModifies: Optional[System.DateTime]  # readonly
    Name: str  # readonly
    Path: str  # readonly

class IImpersonationContext(System.IDisposable):  # Interface
    ...

class ILogonECM(object):  # Interface
    def Logon(
        self,
        server: str,
        domain: str,
        user: str,
        password: System.Security.SecureString,
        accountName: str,
    ) -> None: ...

class ILogonParameters(object):  # Interface
    AccountName: str  # readonly
    ConnectionTicket: str  # readonly
    Domain: str  # readonly
    Server: str  # readonly
    User: str  # readonly
    _Password: System.Security.SecureString  # readonly

class ILogonWindows(object):  # Interface
    def Logon(
        self, user: str, domain: str, password: System.Security.SecureString
    ) -> None: ...

class IPrincipal(object):  # Interface
    def IsInRole(self, role: str) -> bool: ...

class IReportCompliance(object):  # Interface
    Reporting: bool

class IReportFileService(object):  # Interface
    def DownloadFolderToWorkArea(self, path: str) -> None: ...
    def OpenFile(self, path: str) -> None: ...
    def DownloadFileToWorkArea(self, path: str) -> None: ...
    def UploadFileFromWorkArea(self, path: str) -> None: ...
    def GetDefaultOutputFolder(self, batchFolder: str, batchFile: str) -> str: ...
    def Print(self, path: str, printer: str) -> None: ...
    def TranslateToWorkPath(self, path: str) -> str: ...
    def DownloadFileAndUnzipToWorkArea(self, path: str) -> None: ...

class IRevisionHistory(object):  # Interface
    Date: Optional[System.DateTime]  # readonly
    Reason: str  # readonly
    RevisionNumber: str  # readonly
    User: str  # readonly

class IUnknownsFileService(object):  # Interface
    def GetAnalysisFilePath(self, batchFolder: str, analysisFile: str) -> str: ...
    def GetLatestAnalysisRevision(self, batchFolder: str, analysisFile: str) -> str: ...
    def AnalysisFileExists(self, batchFolder: str, analysisFile: str) -> bool: ...
    def TranslateAnalysisToLocalPath(self, path: str, revisionNumber: str) -> str: ...
    def DownloadAnalysisFile(
        self, batchFolder: str, analysisFile: str, revisionNumber: str
    ) -> None: ...
    def CheckoutAnalysis(self, batchFolder: str, batchFile: str) -> None: ...
    def GetAnalysisFileInfos(
        self, folder: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IFileInfo
    ]: ...
    def UploadAnalysisFile(
        self, batchFolder: str, analysisFile: str, revisionNumber: str
    ) -> None: ...
    def UndoCheckoutAnalysis(self, batchFolder: str, batchFile: str) -> None: ...
    def IsAnalysisCheckedoutByCurrentUser(
        self, batchFolder: str, batchFile: str
    ) -> bool: ...
    def GetAnalysisFiles(self, folder: str) -> List[str]: ...

class LogonUtils:  # Class
    @staticmethod
    def InlineLogon(
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ILogonParameters,
    ) -> None: ...
    @staticmethod
    def EncryptPassword(password: str) -> str: ...
    @staticmethod
    def DecryptPassword(encrypted: str) -> System.Security.SecureString: ...
