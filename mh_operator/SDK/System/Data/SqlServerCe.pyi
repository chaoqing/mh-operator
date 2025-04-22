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

# Stubs for namespace: System.Data.SqlServerCe

class AddOption(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    CreateDatabase: System.Data.SqlServerCe.AddOption = ...  # static # readonly
    ExistingDatabase: System.Data.SqlServerCe.AddOption = ...  # static # readonly

class CommitMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Deferred: System.Data.SqlServerCe.CommitMode = ...  # static # readonly
    Immediate: System.Data.SqlServerCe.CommitMode = ...  # static # readonly

class DbInsertOptions(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    KeepCurrentPosition: System.Data.SqlServerCe.DbInsertOptions = (
        ...
    )  # static # readonly
    PositionOnInsertedRow: System.Data.SqlServerCe.DbInsertOptions = (
        ...
    )  # static # readonly

class DbRangeOptions(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Default: System.Data.SqlServerCe.DbRangeOptions = ...  # static # readonly
    ExcludeNulls: System.Data.SqlServerCe.DbRangeOptions = ...  # static # readonly
    ExclusiveEnd: System.Data.SqlServerCe.DbRangeOptions = ...  # static # readonly
    ExclusiveStart: System.Data.SqlServerCe.DbRangeOptions = ...  # static # readonly
    InclusiveEnd: System.Data.SqlServerCe.DbRangeOptions = ...  # static # readonly
    InclusiveStart: System.Data.SqlServerCe.DbRangeOptions = ...  # static # readonly
    Match: System.Data.SqlServerCe.DbRangeOptions = ...  # static # readonly
    Prefix: System.Data.SqlServerCe.DbRangeOptions = ...  # static # readonly

class DbSeekOptions(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    After: System.Data.SqlServerCe.DbSeekOptions = ...  # static # readonly
    AfterEqual: System.Data.SqlServerCe.DbSeekOptions = ...  # static # readonly
    Before: System.Data.SqlServerCe.DbSeekOptions = ...  # static # readonly
    BeforeEqual: System.Data.SqlServerCe.DbSeekOptions = ...  # static # readonly
    FirstEqual: System.Data.SqlServerCe.DbSeekOptions = ...  # static # readonly
    LastEqual: System.Data.SqlServerCe.DbSeekOptions = ...  # static # readonly

class DropOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DropDatabase: System.Data.SqlServerCe.DropOption = ...  # static # readonly
    LeaveDatabase: System.Data.SqlServerCe.DropOption = ...  # static # readonly
    UnregisterSubscription: System.Data.SqlServerCe.DropOption = (
        ...
    )  # static # readonly

class ExchangeType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    BiDirectional: System.Data.SqlServerCe.ExchangeType = ...  # static # readonly
    Upload: System.Data.SqlServerCe.ExchangeType = ...  # static # readonly

class NetworkType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DefaultNetwork: System.Data.SqlServerCe.NetworkType = ...  # static # readonly
    MultiProtocol: System.Data.SqlServerCe.NetworkType = ...  # static # readonly
    TcpIpSockets: System.Data.SqlServerCe.NetworkType = ...  # static # readonly

class OnStartTableDownload(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        ar: System.IAsyncResult,
        tableName: str,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, ar: System.IAsyncResult, tableName: str) -> None: ...

class OnStartTableUpload(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        ar: System.IAsyncResult,
        tableName: str,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, ar: System.IAsyncResult, tableName: str) -> None: ...

class OnSynchronization(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        ar: System.IAsyncResult,
        percentComplete: int,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, ar: System.IAsyncResult, percentComplete: int) -> None: ...

class PurgeType(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    CsnBased: System.Data.SqlServerCe.PurgeType = ...  # static # readonly
    Max: System.Data.SqlServerCe.PurgeType = ...  # static # readonly
    TimeBased: System.Data.SqlServerCe.PurgeType = ...  # static # readonly

class RdaBatchOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    BatchingOff: System.Data.SqlServerCe.RdaBatchOption = ...  # static # readonly
    BatchingOn: System.Data.SqlServerCe.RdaBatchOption = ...  # static # readonly

class RdaTrackOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    TrackingOff: System.Data.SqlServerCe.RdaTrackOption = ...  # static # readonly
    TrackingOffWithIndexes: System.Data.SqlServerCe.RdaTrackOption = (
        ...
    )  # static # readonly
    TrackingOn: System.Data.SqlServerCe.RdaTrackOption = ...  # static # readonly
    TrackingOnWithIndexes: System.Data.SqlServerCe.RdaTrackOption = (
        ...
    )  # static # readonly

class RepairOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DeleteCorruptedRows: System.Data.SqlServerCe.RepairOption = ...  # static # readonly
    RecoverAllOrFail: System.Data.SqlServerCe.RepairOption = ...  # static # readonly
    RecoverAllPossibleRows: System.Data.SqlServerCe.RepairOption = (
        ...
    )  # static # readonly
    RecoverCorruptedRows: System.Data.SqlServerCe.RepairOption = (
        ...
    )  # static # readonly

class ResultSetEnumerator(Iterator[Any]):  # Class
    def __init__(self, resultSet: System.Data.SqlServerCe.SqlCeResultSet) -> None: ...

    Current: System.Data.SqlServerCe.SqlCeUpdatableRecord  # readonly

    def MoveNext(self) -> bool: ...
    def Reset(self) -> None: ...

class ResultSetOptions(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Insensitive: System.Data.SqlServerCe.ResultSetOptions = ...  # static # readonly
    Scrollable: System.Data.SqlServerCe.ResultSetOptions = ...  # static # readonly
    Sensitive: System.Data.SqlServerCe.ResultSetOptions = ...  # static # readonly
    Updatable: System.Data.SqlServerCe.ResultSetOptions = ...  # static # readonly

class ResultSetSensitivity(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Asensitive: System.Data.SqlServerCe.ResultSetSensitivity = ...  # static # readonly
    Insensitive: System.Data.SqlServerCe.ResultSetSensitivity = ...  # static # readonly
    Sensitive: System.Data.SqlServerCe.ResultSetSensitivity = ...  # static # readonly

class ResultSetView(
    Iterable[Any],
    List[Any],
    System.ComponentModel.IBindingList,
    System.IDisposable,
    System.ComponentModel.ITypedList,
    Sequence[Any],
):  # Class
    Columns: List[str]
    Ordinals: List[int]

    ListChanged: System.ComponentModel.ListChangedEventHandler  # Event

class RowView(
    System.ComponentModel.IDataErrorInfo,
    System.ComponentModel.IEditableObject,
    System.IDisposable,
):  # Class
    UpdatableRecord: System.Data.SqlServerCe.SqlCeUpdatableRecord  # readonly

    def GetHashCode(self) -> int: ...
    def Dispose(self) -> None: ...
    def Equals(self, other: Any) -> bool: ...

class SecurityType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    DBAuthentication: System.Data.SqlServerCe.SecurityType = ...  # static # readonly
    NTAuthentication: System.Data.SqlServerCe.SecurityType = ...  # static # readonly

class SnapshotTransferType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    FTP: System.Data.SqlServerCe.SnapshotTransferType = ...  # static # readonly
    UNC: System.Data.SqlServerCe.SnapshotTransferType = ...  # static # readonly

class SqlCeChangeTracking(System.IDisposable):  # Class
    @overload
    def __init__(
        self, transaction: System.Data.SqlServerCe.SqlCeTransaction
    ) -> None: ...
    @overload
    def __init__(self, connection: System.Data.SqlServerCe.SqlCeConnection) -> None: ...
    def PurgeTombstoneTableData(
        self,
        tableName: str,
        pType: System.Data.SqlServerCe.PurgeType,
        retentionValue: int,
    ) -> None: ...
    def EnableTracking(
        self,
        tableName: str,
        trackingKeyType: System.Data.SqlServerCe.TrackingKeyType,
        trackingOptions: System.Data.SqlServerCe.TrackingOptions,
    ) -> None: ...
    @staticmethod
    def UpgradePublicTracking(connectionString: str) -> bool: ...
    def PurgeTransactionSequenceData(
        self, pType: System.Data.SqlServerCe.PurgeType, retentionValue: int
    ) -> None: ...
    def DisableTracking(self, tableName: str) -> None: ...
    @overload
    def Dispose(self) -> None: ...
    @overload
    def Dispose(self, disposing: bool) -> None: ...
    def PackTombstoneKey(
        self, tableName: str, columnValues: List[Any]
    ) -> List[int]: ...
    def GetTrackingOptions(
        self, tableName: str, trackingOptions: System.Data.SqlServerCe.TrackingOptions
    ) -> bool: ...
    def GetLastCommittedCsn(self) -> int: ...
    def UnpackTombstoneKey(
        self, tableName: str, tombstoneKey: List[int]
    ) -> List[Any]: ...

class SqlCeCommand(
    System.Data.IDbCommand,
    System.IDisposable,
    System.Data.Common.DbCommand,
    System.ComponentModel.IComponent,
    System.ICloneable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, commandText: str) -> None: ...
    @overload
    def __init__(
        self, commandText: str, connection: System.Data.SqlServerCe.SqlCeConnection
    ) -> None: ...
    @overload
    def __init__(
        self,
        commandText: str,
        connection: System.Data.SqlServerCe.SqlCeConnection,
        transaction: System.Data.SqlServerCe.SqlCeTransaction,
    ) -> None: ...

    CommandText: str
    CommandTimeout: int
    CommandType: System.Data.CommandType
    Connection: System.Data.SqlServerCe.SqlCeConnection
    DesignTimeVisible: bool
    IndexName: str
    Parameters: System.Data.SqlServerCe.SqlCeParameterCollection  # readonly
    Transaction: System.Data.SqlServerCe.SqlCeTransaction
    UpdatedRowSource: System.Data.UpdateRowSource

    def CreateParameter(self) -> System.Data.SqlServerCe.SqlCeParameter: ...
    def ExecuteScalar(self) -> Any: ...
    @overload
    def ExecuteReader(self) -> System.Data.SqlServerCe.SqlCeDataReader: ...
    @overload
    def ExecuteReader(
        self, behavior: System.Data.CommandBehavior
    ) -> System.Data.SqlServerCe.SqlCeDataReader: ...
    def SetRange(
        self,
        dbRangeOptions: System.Data.SqlServerCe.DbRangeOptions,
        startData: List[Any],
        endData: List[Any],
    ) -> None: ...
    def Prepare(self) -> None: ...
    def ExecuteNonQuery(self) -> int: ...
    @overload
    def ExecuteResultSet(
        self, options: System.Data.SqlServerCe.ResultSetOptions
    ) -> System.Data.SqlServerCe.SqlCeResultSet: ...
    @overload
    def ExecuteResultSet(
        self,
        options: System.Data.SqlServerCe.ResultSetOptions,
        resultSet: System.Data.SqlServerCe.SqlCeResultSet,
    ) -> System.Data.SqlServerCe.SqlCeResultSet: ...
    def Cancel(self) -> None: ...

class SqlCeCommandBuilder(
    System.Data.Common.DbCommandBuilder,
    System.IDisposable,
    System.ComponentModel.IComponent,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, adapter: System.Data.SqlServerCe.SqlCeDataAdapter) -> None: ...

    CatalogLocation: System.Data.Common.CatalogLocation
    CatalogSeparator: str
    ConflictOption: System.Data.ConflictOption
    DataAdapter: System.Data.SqlServerCe.SqlCeDataAdapter
    QuotePrefix: str
    QuoteSuffix: str
    SchemaSeparator: str

    def UnquoteIdentifier(self, quotedIdentifier: str) -> str: ...
    def GetUpdateCommand(self) -> System.Data.SqlServerCe.SqlCeCommand: ...
    def GetInsertCommand(self) -> System.Data.SqlServerCe.SqlCeCommand: ...
    def GetDeleteCommand(self) -> System.Data.SqlServerCe.SqlCeCommand: ...
    def QuoteIdentifier(self, unquotedIdentifier: str) -> str: ...

class SqlCeConnection(
    System.IDisposable,
    System.Data.Common.DbConnection,
    System.Data.IDbConnection,
    System.ComponentModel.IComponent,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, connectionString: str) -> None: ...

    ConnectionString: str
    ConnectionTimeout: int  # readonly
    DataSource: str  # readonly
    Database: str  # readonly
    DatabaseIdentifier: str  # readonly
    ServerVersion: str  # readonly
    State: System.Data.ConnectionState  # readonly

    def Open(self) -> None: ...
    @overload
    def GetSchema(self) -> System.Data.DataTable: ...
    @overload
    def GetSchema(self, collectionName: str) -> System.Data.DataTable: ...
    @overload
    def GetSchema(
        self, collectionName: str, restrictionValues: List[str]
    ) -> System.Data.DataTable: ...
    def Close(self) -> None: ...
    def CreateCommand(self) -> System.Data.SqlServerCe.SqlCeCommand: ...
    @overload
    def BeginTransaction(
        self, isolationLevel: System.Data.IsolationLevel
    ) -> System.Data.SqlServerCe.SqlCeTransaction: ...
    @overload
    def BeginTransaction(self) -> System.Data.SqlServerCe.SqlCeTransaction: ...
    def Dispose(self) -> None: ...
    def EnlistTransaction(self, SysTrans: System.Transactions.Transaction) -> None: ...
    def GetDatabaseInfo(
        self,
    ) -> System.Collections.Generic.List[
        System.Collections.Generic.KeyValuePair[str, str]
    ]: ...
    def ChangeDatabase(self, value_: str) -> None: ...

    FlushFailure: System.Data.SqlServerCe.SqlCeFlushFailureEventHandler  # Event
    InfoMessage: System.Data.SqlServerCe.SqlCeInfoMessageEventHandler  # Event
    StateChange: System.Data.StateChangeEventHandler  # Event

class SqlCeConnectionStringBuilder(
    System.Data.Common.DbConnectionStringBuilder,
    Dict[Any, Any],
    Iterable[Any],
    Sequence[Any],
    System.ComponentModel.ICustomTypeDescriptor,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, connectionString: str) -> None: ...

    AutoshrinkThreshold: int
    CaseSensitive: bool
    DataSource: str
    DefaultLockEscalation: int
    DefaultLockTimeout: int
    Encrypt: bool
    EncryptionMode: str
    Enlist: bool
    FileMode: str
    FlushInterval: int
    InitialLcid: int
    IsFixedSize: bool  # readonly
    def __getitem__(self, keyword: str) -> Any: ...
    def __setitem__(self, keyword: str, value_: Any) -> None: ...
    Keys: Sequence[Any]  # readonly
    MaxBufferSize: int
    MaxDatabaseSize: int
    Password: str
    PersistSecurityInfo: bool
    TempFileMaxSize: int
    TempFilePath: str
    Values: Sequence[Any]  # readonly

    def ShouldSerialize(self, keyword: str) -> bool: ...
    def ContainsKey(self, keyword: str) -> bool: ...
    def Clear(self) -> None: ...
    def TryGetValue(self, keyword: str, value_: Any) -> bool: ...
    def Remove(self, keyword: str) -> bool: ...

class SqlCeDataAdapter(
    System.Data.Common.DbDataAdapter,
    System.Data.IDbDataAdapter,
    System.Data.IDataAdapter,
    System.IDisposable,
    System.ICloneable,
    System.ComponentModel.IComponent,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, selectCommand: System.Data.SqlServerCe.SqlCeCommand) -> None: ...
    @overload
    def __init__(self, selectCommandText: str, selectConnectionString: str) -> None: ...
    @overload
    def __init__(
        self,
        selectCommandText: str,
        selectConnection: System.Data.SqlServerCe.SqlCeConnection,
    ) -> None: ...

    DeleteCommand: System.Data.SqlServerCe.SqlCeCommand
    InsertCommand: System.Data.SqlServerCe.SqlCeCommand
    SelectCommand: System.Data.SqlServerCe.SqlCeCommand
    UpdateCommand: System.Data.SqlServerCe.SqlCeCommand

    def Dispose(self) -> None: ...

    RowUpdated: System.Data.SqlServerCe.SqlCeRowUpdatedEventHandler  # Event
    RowUpdating: System.Data.SqlServerCe.SqlCeRowUpdatingEventHandler  # Event

class SqlCeDataReader(
    System.Data.IDataReader,
    System.Data.IDataRecord,
    System.IDisposable,
    Iterable[Any],
    System.Data.Common.DbDataReader,
):  # Class
    Depth: int  # readonly
    FieldCount: int  # readonly
    HasRows: bool  # readonly
    HiddenFieldCount: int  # readonly
    IsClosed: bool  # readonly
    def __getitem__(self, index: int) -> Any: ...
    def __getitem__(self, name: str) -> Any: ...
    RecordsAffected: int  # readonly

    def GetSqlInt32(self, ordinal: int) -> System.Data.SqlTypes.SqlInt32: ...
    def GetString(self, ordinal: int) -> str: ...
    def GetSqlDouble(self, ordinal: int) -> System.Data.SqlTypes.SqlDouble: ...
    def GetName(self, index: int) -> str: ...
    def GetDateTime(self, ordinal: int) -> System.DateTime: ...
    def GetSqlBinary(self, ordinal: int) -> System.Data.SqlTypes.SqlBinary: ...
    def GetSchemaTable(self) -> System.Data.DataTable: ...
    def GetSqlSingle(self, ordinal: int) -> System.Data.SqlTypes.SqlSingle: ...
    def GetSqlInt64(self, ordinal: int) -> System.Data.SqlTypes.SqlInt64: ...
    def GetOrdinal(self, name: str) -> int: ...
    def GetChars(
        self,
        ordinal: int,
        dataIndex: int,
        buffer: List[str],
        bufferIndex: int,
        length: int,
    ) -> int: ...
    def Dispose(self) -> None: ...
    def GetSqlDecimal(self, ordinal: int) -> System.Data.SqlTypes.SqlDecimal: ...
    def GetInt32(self, ordinal: int) -> int: ...
    def GetByte(self, ordinal: int) -> int: ...
    def GetDecimal(self, ordinal: int) -> System.Decimal: ...
    def GetSqlMoney(self, ordinal: int) -> System.Data.SqlTypes.SqlMoney: ...
    def Read(self) -> bool: ...
    def IsDBNull(self, ordinal: int) -> bool: ...
    def GetGuid(self, ordinal: int) -> System.Guid: ...
    def GetBoolean(self, ordinal: int) -> bool: ...
    def GetSqlGuid(self, ordinal: int) -> System.Data.SqlTypes.SqlGuid: ...
    def GetSqlDateTime(self, ordinal: int) -> System.Data.SqlTypes.SqlDateTime: ...
    def GetDouble(self, ordinal: int) -> float: ...
    def NextResult(self) -> bool: ...
    def Close(self) -> None: ...
    def GetSqlBoolean(self, ordinal: int) -> System.Data.SqlTypes.SqlBoolean: ...
    def GetInt64(self, ordinal: int) -> int: ...
    def GetChar(self, ordinal: int) -> str: ...
    def GetSqlByte(self, ordinal: int) -> System.Data.SqlTypes.SqlByte: ...
    def GetProviderSpecificFieldType(self, ordinal: int) -> System.Type: ...
    def GetValues(self, values: List[Any]) -> int: ...
    def GetSqlInt16(self, ordinal: int) -> System.Data.SqlTypes.SqlInt16: ...
    def GetBytes(
        self,
        ordinal: int,
        dataIndex: int,
        buffer: List[int],
        bufferIndex: int,
        length: int,
    ) -> int: ...
    def GetDataTypeName(self, index: int) -> str: ...
    def GetEnumerator(self) -> Iterator[Any]: ...
    def GetInt16(self, ordinal: int) -> int: ...
    def GetFloat(self, ordinal: int) -> float: ...
    def Seek(
        self, dbSeekOptions: System.Data.SqlServerCe.DbSeekOptions, index: List[Any]
    ) -> bool: ...
    def GetFieldType(self, ordinal: int) -> System.Type: ...
    def GetSqlString(self, ordinal: int) -> System.Data.SqlTypes.SqlString: ...
    def GetValue(self, ordinal: int) -> Any: ...

class SqlCeEngine(System.IDisposable):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, connectionString: str) -> None: ...

    LocalConnectionString: str

    def Repair(
        self, connectionString: str, options: System.Data.SqlServerCe.RepairOption
    ) -> None: ...
    def Compact(self, connectionString: str) -> None: ...
    def Shrink(self) -> None: ...
    def CreateDatabase(self) -> None: ...
    @overload
    def Verify(self) -> bool: ...
    @overload
    def Verify(self, option: System.Data.SqlServerCe.VerifyOption) -> bool: ...
    @overload
    def Upgrade(self) -> None: ...
    @overload
    def Upgrade(self, destConnectionString: str) -> None: ...
    def Dispose(self) -> None: ...

class SqlCeError:  # Class
    ErrorParameters: List[str]  # readonly
    HResult: int  # readonly
    Message: str  # readonly
    NativeError: int  # readonly
    NumericErrorParameters: List[int]  # readonly
    Source: str  # readonly

    def ToString(self) -> str: ...

class SqlCeErrorCollection(Iterable[Any], Sequence[Any]):  # Class
    Count: int  # readonly
    def __getitem__(self, index: int) -> System.Data.SqlServerCe.SqlCeError: ...
    def GetEnumerator(self) -> Iterator[Any]: ...
    def CopyTo(self, array: System.Array, index: int) -> None: ...

class SqlCeException(
    System.Runtime.InteropServices._Exception,
    System.Data.Common.DbException,
    System.Runtime.Serialization.ISerializable,
):  # Class
    Errors: System.Data.SqlServerCe.SqlCeErrorCollection  # readonly
    HResult: int  # readonly
    Message: str  # readonly
    NativeError: int  # readonly
    Source: str  # readonly

    def GetObjectData(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class SqlCeFlushFailureEventArgs(System.EventArgs):  # Class
    Errors: System.Data.SqlServerCe.SqlCeErrorCollection  # readonly
    Message: str  # readonly

    def ToString(self) -> str: ...

class SqlCeFlushFailureEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: System.Data.SqlServerCe.SqlCeFlushFailureEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self, sender: Any, e: System.Data.SqlServerCe.SqlCeFlushFailureEventArgs
    ) -> None: ...

class SqlCeInfoMessageEventArgs(System.EventArgs):  # Class
    Errors: System.Data.SqlServerCe.SqlCeErrorCollection  # readonly
    Message: str  # readonly

    def ToString(self) -> str: ...

class SqlCeInfoMessageEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: System.Data.SqlServerCe.SqlCeInfoMessageEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self, sender: Any, e: System.Data.SqlServerCe.SqlCeInfoMessageEventArgs
    ) -> None: ...

class SqlCeInvalidDatabaseFormatException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Data.SqlServerCe.SqlCeException,
):  # Class
    def GetObjectData(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class SqlCeLockTimeoutException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Data.SqlServerCe.SqlCeException,
):  # Class
    def GetObjectData(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class SqlCeParameter(
    System.ICloneable,
    System.Data.IDataParameter,
    System.Data.IDbDataParameter,
    System.Data.Common.DbParameter,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str, value_: Any) -> None: ...
    @overload
    def __init__(self, name: str, dataType: System.Data.SqlDbType) -> None: ...
    @overload
    def __init__(
        self, name: str, dataType: System.Data.SqlDbType, size: int
    ) -> None: ...
    @overload
    def __init__(
        self, name: str, dataType: System.Data.SqlDbType, size: int, sourceColumn: str
    ) -> None: ...
    @overload
    def __init__(
        self,
        parameterName: str,
        dbType: System.Data.SqlDbType,
        size: int,
        isNullable: bool,
        precision: int,
        scale: int,
        sourceColumn: str,
        sourceVersion: System.Data.DataRowVersion,
        value_: Any,
    ) -> None: ...
    @overload
    def __init__(
        self,
        parameterName: str,
        dbType: System.Data.SqlDbType,
        size: int,
        direction: System.Data.ParameterDirection,
        isNullable: bool,
        precision: int,
        scale: int,
        sourceColumn: str,
        sourceVersion: System.Data.DataRowVersion,
        value_: Any,
    ) -> None: ...

    DbType: System.Data.DbType
    Direction: System.Data.ParameterDirection
    IsNullable: bool
    Offset: int
    ParameterName: str
    Precision: int
    Scale: int
    Size: int
    SourceColumn: str
    SourceColumnNullMapping: bool
    SourceVersion: System.Data.DataRowVersion
    SqlDbType: System.Data.SqlDbType
    Value: Any

    def ResetDbType(self) -> None: ...
    def ToString(self) -> str: ...

class SqlCeParameterCollection(
    List[Any],
    System.Data.IDataParameterCollection,
    Iterable[Any],
    Sequence[Any],
    System.Data.Common.DbParameterCollection,
):  # Class
    Count: int  # readonly
    IsFixedSize: bool  # readonly
    IsReadOnly: bool  # readonly
    IsSynchronized: bool  # readonly
    def __getitem__(self, index: int) -> System.Data.SqlServerCe.SqlCeParameter: ...
    def __setitem__(
        self, index: int, value_: System.Data.SqlServerCe.SqlCeParameter
    ) -> None: ...
    def __getitem__(
        self, parameterName: str
    ) -> System.Data.SqlServerCe.SqlCeParameter: ...
    def __setitem__(
        self, parameterName: str, value_: System.Data.SqlServerCe.SqlCeParameter
    ) -> None: ...
    SyncRoot: Any  # readonly

    def GetEnumerator(self) -> Iterator[Any]: ...
    @overload
    def Contains(self, value_: str) -> bool: ...
    @overload
    def Contains(self, value_: Any) -> bool: ...
    def CopyTo(self, array: System.Array, index: int) -> None: ...
    @overload
    def Add(self, value_: Any) -> int: ...
    @overload
    def Add(
        self, value_: System.Data.SqlServerCe.SqlCeParameter
    ) -> System.Data.SqlServerCe.SqlCeParameter: ...
    @overload
    def Add(
        self, parameterName: str, value_: Any
    ) -> System.Data.SqlServerCe.SqlCeParameter: ...
    @overload
    def Add(
        self, parameterName: str, type: System.Data.SqlDbType
    ) -> System.Data.SqlServerCe.SqlCeParameter: ...
    @overload
    def Add(
        self, parameterName: str, type: System.Data.SqlDbType, size: int
    ) -> System.Data.SqlServerCe.SqlCeParameter: ...
    @overload
    def Add(
        self,
        parameterName: str,
        type: System.Data.SqlDbType,
        size: int,
        sourceColumn: str,
    ) -> System.Data.SqlServerCe.SqlCeParameter: ...
    def Clear(self) -> None: ...
    def AddRange(self, values: System.Array) -> None: ...
    @overload
    def IndexOf(self, parameterName: str) -> int: ...
    @overload
    def IndexOf(self, value_: Any) -> int: ...
    def Remove(self, value_: Any) -> None: ...
    def AddWithValue(
        self, parameterName: str, value_: Any
    ) -> System.Data.SqlServerCe.SqlCeParameter: ...
    def Insert(self, index: int, value_: Any) -> None: ...
    @overload
    def RemoveAt(self, index: int) -> None: ...
    @overload
    def RemoveAt(self, parameterName: str) -> None: ...

class SqlCeProviderFactory(
    System.IServiceProvider, System.Data.Common.DbProviderFactory
):  # Class
    def __init__(self) -> None: ...

    Instance: System.Data.SqlServerCe.SqlCeProviderFactory  # static # readonly

    def CreateDataAdapter(self) -> System.Data.Common.DbDataAdapter: ...
    def CreateParameter(self) -> System.Data.Common.DbParameter: ...
    def CreateCommandBuilder(self) -> System.Data.Common.DbCommandBuilder: ...
    def CreateConnection(self) -> System.Data.Common.DbConnection: ...
    def CreateCommand(self) -> System.Data.Common.DbCommand: ...
    def CreateConnectionStringBuilder(
        self,
    ) -> System.Data.Common.DbConnectionStringBuilder: ...

class SqlCeRemoteDataAccess(System.IDisposable):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, internetUrl: str, localConnectionString: str) -> None: ...
    @overload
    def __init__(
        self,
        internetUrl: str,
        internetLogin: str,
        internetPassword: str,
        localConnectionString: str,
    ) -> None: ...

    CompressionLevel: int
    ConnectTimeout: int
    ConnectionManager: bool
    ConnectionRetryTimeout: int
    InternetLogin: str
    InternetPassword: str
    InternetProxyLogin: str
    InternetProxyPassword: str
    InternetProxyServer: str
    InternetUrl: str
    LocalConnectionString: str
    ReceiveTimeout: int
    SendTimeout: int

    @overload
    def Pull(
        self, localTableName: str, sqlSelectString: str, oleDBConnectionString: str
    ) -> None: ...
    @overload
    def Pull(
        self,
        localTableName: str,
        sqlSelectString: str,
        oleDBConnectionString: str,
        trackOption: System.Data.SqlServerCe.RdaTrackOption,
    ) -> None: ...
    @overload
    def Pull(
        self,
        localTableName: str,
        sqlSelectString: str,
        oleDBConnectionString: str,
        trackOption: System.Data.SqlServerCe.RdaTrackOption,
        errorTable: str,
    ) -> None: ...
    @overload
    def Push(self, localTableName: str, oleDBConnectionString: str) -> None: ...
    @overload
    def Push(
        self,
        localTableName: str,
        oleDBConnectionString: str,
        batchOption: System.Data.SqlServerCe.RdaBatchOption,
    ) -> None: ...
    def Dispose(self) -> None: ...
    def SubmitSql(self, sqlString: str, oleDBConnectionString: str) -> None: ...

class SqlCeReplication(System.IDisposable):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        internetUrl: str,
        internetLogin: str,
        internetPassword: str,
        publisher: str,
        publisherDatabase: str,
        publisherLogin: str,
        publisherPassword: str,
        publication: str,
        subscriber: str,
        subscriberConnectionString: str,
    ) -> None: ...
    @overload
    def __init__(
        self,
        internetUrl: str,
        internetLogin: str,
        internetPassword: str,
        publisher: str,
        publisherDatabase: str,
        publication: str,
        subscriber: str,
        subscriberConnectionString: str,
    ) -> None: ...

    CompressionLevel: int
    ConnectTimeout: int
    ConnectionManager: bool
    ConnectionRetryTimeout: int
    Distributor: str
    DistributorAddress: str
    DistributorLogin: str
    DistributorNetwork: System.Data.SqlServerCe.NetworkType
    DistributorPassword: str
    DistributorSecurityMode: System.Data.SqlServerCe.SecurityType
    ExchangeType: System.Data.SqlServerCe.ExchangeType
    HostName: str
    InternetLogin: str
    InternetPassword: str
    InternetProxyLogin: str
    InternetProxyPassword: str
    InternetProxyServer: str
    InternetUrl: str
    LoginTimeout: int
    PostSyncCleanup: int
    ProfileName: str
    Publication: str
    Publisher: str
    PublisherAddress: str
    PublisherChanges: int  # readonly
    PublisherConflicts: int  # readonly
    PublisherDatabase: str
    PublisherLogin: str
    PublisherNetwork: System.Data.SqlServerCe.NetworkType
    PublisherPassword: str
    PublisherSecurityMode: System.Data.SqlServerCe.SecurityType
    QueryTimeout: int
    ReceiveTimeout: int
    SendTimeout: int
    SnapshotTransferType: System.Data.SqlServerCe.SnapshotTransferType
    Subscriber: str
    SubscriberChanges: int  # readonly
    SubscriberConflicts: int  # readonly
    SubscriberConnectionString: str
    Validate: System.Data.SqlServerCe.ValidateType

    @overload
    def BeginSynchronize(
        self, onSyncCompletion: System.AsyncCallback, state: Any
    ) -> System.IAsyncResult: ...
    @overload
    def BeginSynchronize(
        self,
        onSyncCompletion: System.AsyncCallback,
        onStartTableUpload: System.Data.SqlServerCe.OnStartTableUpload,
        onStartTableDownload: System.Data.SqlServerCe.OnStartTableDownload,
        onSynchronization: System.Data.SqlServerCe.OnSynchronization,
        state: Any,
    ) -> System.IAsyncResult: ...
    def CancelSynchronize(self) -> None: ...
    def AddSubscription(self, addOption: System.Data.SqlServerCe.AddOption) -> None: ...
    def LoadProperties(self) -> bool: ...
    def DropSubscription(
        self, dropOption: System.Data.SqlServerCe.DropOption
    ) -> None: ...
    def EndSynchronize(self, ar: System.IAsyncResult) -> None: ...
    def SaveProperties(self) -> None: ...
    def Dispose(self) -> None: ...
    def Synchronize(self) -> None: ...
    def ReinitializeSubscription(self, uploadBeforeReinitialize: bool) -> None: ...

class SqlCeResultSet(
    System.Data.SqlServerCe.SqlCeDataReader,
    System.Data.IDataReader,
    System.Data.IDataRecord,
    System.IDisposable,
    Iterable[Any],
    System.ComponentModel.IListSource,
):  # Class
    def __getitem__(self, index: int) -> Any: ...
    def __getitem__(self, name: str) -> Any: ...
    ResultSetView: System.Data.SqlServerCe.ResultSetView  # readonly
    Scrollable: bool  # readonly
    Sensitivity: System.Data.SqlServerCe.ResultSetSensitivity  # readonly
    Updatable: bool  # readonly

    def GetSqlInt32(self, ordinal: int) -> System.Data.SqlTypes.SqlInt32: ...
    def GetString(self, ordinal: int) -> str: ...
    def ReadFirst(self) -> bool: ...
    def SetChars(
        self,
        ordinal: int,
        dataIndex: int,
        buffer: List[str],
        bufferIndex: int,
        length: int,
    ) -> None: ...
    def SetSqlString(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlString
    ) -> None: ...
    def GetSqlDouble(self, ordinal: int) -> System.Data.SqlTypes.SqlDouble: ...
    def GetDateTime(self, ordinal: int) -> System.DateTime: ...
    def SetSqlBinary(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlBinary
    ) -> None: ...
    def GetSqlBinary(self, ordinal: int) -> System.Data.SqlTypes.SqlBinary: ...
    def SetSqlInt32(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlInt32
    ) -> None: ...
    def GetSqlSingle(self, ordinal: int) -> System.Data.SqlTypes.SqlSingle: ...
    def GetSqlInt64(self, ordinal: int) -> System.Data.SqlTypes.SqlInt64: ...
    def GetChars(
        self,
        ordinal: int,
        dataIndex: int,
        buffer: List[str],
        bufferIndex: int,
        length: int,
    ) -> int: ...
    def SetSqlInt64(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlInt64
    ) -> None: ...
    def ReadPrevious(self) -> bool: ...
    def SetSqlBoolean(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlBoolean
    ) -> None: ...
    def GetSqlDecimal(self, ordinal: int) -> System.Data.SqlTypes.SqlDecimal: ...
    def SetInt32(self, ordinal: int, value_: int) -> None: ...
    def SetSqlMoney(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlMoney
    ) -> None: ...
    def GetInt32(self, ordinal: int) -> int: ...
    def GetByte(self, ordinal: int) -> int: ...
    def GetDecimal(self, ordinal: int) -> System.Decimal: ...
    def GetSqlMoney(self, ordinal: int) -> System.Data.SqlTypes.SqlMoney: ...
    def ReadAbsolute(self, position: int) -> bool: ...
    def SetBoolean(self, ordinal: int, value_: bool) -> None: ...
    def SetByte(self, ordinal: int, value_: int) -> None: ...
    def IsDBNull(self, ordinal: int) -> bool: ...
    def SetDecimal(self, ordinal: int, value_: System.Decimal) -> None: ...
    def SetDouble(self, ordinal: int, value_: float) -> None: ...
    def SetGuid(self, ordinal: int, value_: System.Guid) -> None: ...
    def GetGuid(self, ordinal: int) -> System.Guid: ...
    def GetBoolean(self, ordinal: int) -> bool: ...
    def CreateRecord(self) -> System.Data.SqlServerCe.SqlCeUpdatableRecord: ...
    def GetSqlGuid(self, ordinal: int) -> System.Data.SqlTypes.SqlGuid: ...
    def GetSqlDateTime(self, ordinal: int) -> System.Data.SqlTypes.SqlDateTime: ...
    def SetDateTime(self, ordinal: int, value_: System.DateTime) -> None: ...
    def GetDouble(self, ordinal: int) -> float: ...
    def SetSqlDateTime(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlDateTime
    ) -> None: ...
    def SetSqlDecimal(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlDecimal
    ) -> None: ...
    def SetChar(self, ordinal: int, c: str) -> None: ...
    def SetInt64(self, ordinal: int, value_: int) -> None: ...
    def SetObjectRef(self, ordinal: int, buffer: Any) -> None: ...
    def SetString(self, ordinal: int, value_: str) -> None: ...
    def SetFloat(self, ordinal: int, value_: float) -> None: ...
    def GetSqlMetaData(self, ordinal: int) -> System.Data.SqlServerCe.SqlMetaData: ...
    def GetSqlBoolean(self, ordinal: int) -> System.Data.SqlTypes.SqlBoolean: ...
    def SetDefault(self, ordinal: int) -> None: ...
    def GetInt64(self, ordinal: int) -> int: ...
    def Delete(self) -> None: ...
    def SetSqlSingle(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlSingle
    ) -> None: ...
    def GetSqlByte(self, ordinal: int) -> System.Data.SqlTypes.SqlByte: ...
    def GetValues(self, values: List[Any]) -> int: ...
    def SetInt16(self, ordinal: int, value_: int) -> None: ...
    def GetSqlInt16(self, ordinal: int) -> System.Data.SqlTypes.SqlInt16: ...
    def GetBytes(
        self,
        ordinal: int,
        dataIndex: int,
        buffer: List[int],
        bufferIndex: int,
        length: int,
    ) -> int: ...
    def SetValues(self, values: List[Any]) -> int: ...
    def SetBytes(
        self,
        ordinal: int,
        dataIndex: int,
        buffer: List[int],
        bufferIndex: int,
        length: int,
    ) -> None: ...
    def SetSqlInt16(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlInt16
    ) -> None: ...
    def GetEnumerator(self) -> Iterator[Any]: ...
    def GetInt16(self, ordinal: int) -> int: ...
    def GetFloat(self, ordinal: int) -> float: ...
    def ReadLast(self) -> bool: ...
    def ReadRelative(self, position: int) -> bool: ...
    @overload
    def Insert(self, record: System.Data.SqlServerCe.SqlCeUpdatableRecord) -> None: ...
    @overload
    def Insert(
        self,
        record: System.Data.SqlServerCe.SqlCeUpdatableRecord,
        options: System.Data.SqlServerCe.DbInsertOptions,
    ) -> None: ...
    def SetValue(self, ordinal: int, value_: Any) -> None: ...
    def SetSqlDouble(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlDouble
    ) -> None: ...
    def Update(self) -> None: ...
    def SetSqlGuid(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlGuid
    ) -> None: ...
    def SetSqlByte(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlByte
    ) -> None: ...
    def GetSqlString(self, ordinal: int) -> System.Data.SqlTypes.SqlString: ...
    def GetValue(self, ordinal: int) -> Any: ...
    def IsSetAsDefault(self, ordinal: int) -> bool: ...

class SqlCeRowUpdatedEventArgs(System.Data.Common.RowUpdatedEventArgs):  # Class
    def __init__(
        self,
        dataRow: System.Data.DataRow,
        command: System.Data.IDbCommand,
        statementType: System.Data.StatementType,
        tableMapping: System.Data.Common.DataTableMapping,
    ) -> None: ...

    Command: System.Data.SqlServerCe.SqlCeCommand  # readonly

class SqlCeRowUpdatedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: System.Data.SqlServerCe.SqlCeRowUpdatedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self, sender: Any, e: System.Data.SqlServerCe.SqlCeRowUpdatedEventArgs
    ) -> None: ...

class SqlCeRowUpdatingEventArgs(System.Data.Common.RowUpdatingEventArgs):  # Class
    def __init__(
        self,
        dataRow: System.Data.DataRow,
        command: System.Data.IDbCommand,
        statementType: System.Data.StatementType,
        tableMapping: System.Data.Common.DataTableMapping,
    ) -> None: ...

    Command: System.Data.SqlServerCe.SqlCeCommand

class SqlCeRowUpdatingEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: System.Data.SqlServerCe.SqlCeRowUpdatingEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self, sender: Any, e: System.Data.SqlServerCe.SqlCeRowUpdatingEventArgs
    ) -> None: ...

class SqlCeTransaction(
    System.Data.IDbTransaction, System.IDisposable, System.Data.Common.DbTransaction
):  # Class
    CurrentTransactionBsn: int  # readonly
    IsolationLevel: System.Data.IsolationLevel  # readonly
    TrackingContext: System.Guid

    def Dispose(self) -> None: ...
    @overload
    def Commit(self) -> None: ...
    @overload
    def Commit(self, mode: System.Data.SqlServerCe.CommitMode) -> None: ...
    def Rollback(self) -> None: ...

class SqlCeTransactionInProgressException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Data.SqlServerCe.SqlCeException,
):  # Class
    def GetObjectData(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class SqlCeType:  # Class
    SqlDbType: System.Data.SqlDbType  # readonly

    def ToString(self) -> str: ...

class SqlCeUpdatableRecord(System.Data.IDataRecord):  # Class
    FieldCount: int  # readonly
    HiddenFieldCount: int  # readonly
    def __getitem__(self, ordinal: int) -> Any: ...
    def __setitem__(self, ordinal: int, value_: Any) -> None: ...
    def __getitem__(self, name: str) -> Any: ...
    def __setitem__(self, name: str, value_: Any) -> None: ...
    Updatable: bool  # readonly

    def GetSqlInt32(self, ordinal: int) -> System.Data.SqlTypes.SqlInt32: ...
    def GetString(self, ordinal: int) -> str: ...
    def SetChars(
        self,
        ordinal: int,
        dataIndex: int,
        buffer: List[str],
        bufferIndex: int,
        length: int,
    ) -> None: ...
    def SetSqlString(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlString
    ) -> None: ...
    def GetSqlDouble(self, ordinal: int) -> System.Data.SqlTypes.SqlDouble: ...
    def GetName(self, ordinal: int) -> str: ...
    def GetDateTime(self, ordinal: int) -> System.DateTime: ...
    def SetSqlBinary(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlBinary
    ) -> None: ...
    def GetSqlBinary(self, ordinal: int) -> System.Data.SqlTypes.SqlBinary: ...
    def SetSqlInt32(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlInt32
    ) -> None: ...
    def GetSqlSingle(self, ordinal: int) -> System.Data.SqlTypes.SqlSingle: ...
    def GetSqlInt64(self, ordinal: int) -> System.Data.SqlTypes.SqlInt64: ...
    def GetOrdinal(self, name: str) -> int: ...
    def GetChars(
        self,
        ordinal: int,
        dataIndex: int,
        buffer: List[str],
        bufferIndex: int,
        length: int,
    ) -> int: ...
    def SetSqlInt64(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlInt64
    ) -> None: ...
    def SetSqlBoolean(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlBoolean
    ) -> None: ...
    def GetSqlDecimal(self, ordinal: int) -> System.Data.SqlTypes.SqlDecimal: ...
    def SetInt32(self, ordinal: int, value_: int) -> None: ...
    def SetSqlMoney(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlMoney
    ) -> None: ...
    def GetInt32(self, ordinal: int) -> int: ...
    def GetByte(self, ordinal: int) -> int: ...
    def GetDecimal(self, ordinal: int) -> System.Decimal: ...
    def GetSqlMoney(self, ordinal: int) -> System.Data.SqlTypes.SqlMoney: ...
    def SetBoolean(self, ordinal: int, value_: bool) -> None: ...
    def SetByte(self, ordinal: int, value_: int) -> None: ...
    def SetDecimal(self, ordinal: int, value_: System.Decimal) -> None: ...
    def IsDBNull(self, ordinal: int) -> bool: ...
    def GetSqlCharsRef(self, ordinal: int) -> System.Data.SqlTypes.SqlChars: ...
    def SetDouble(self, ordinal: int, value_: float) -> None: ...
    def SetGuid(self, ordinal: int, value_: System.Guid) -> None: ...
    def GetGuid(self, ordinal: int) -> System.Guid: ...
    def GetBoolean(self, ordinal: int) -> bool: ...
    def GetSqlGuid(self, ordinal: int) -> System.Data.SqlTypes.SqlGuid: ...
    def SetDateTime(self, ordinal: int, value_: System.DateTime) -> None: ...
    def GetSqlDateTime(self, ordinal: int) -> System.Data.SqlTypes.SqlDateTime: ...
    def SetSqlDateTime(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlDateTime
    ) -> None: ...
    def GetDouble(self, ordinal: int) -> float: ...
    def SetSqlDecimal(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlDecimal
    ) -> None: ...
    def SetChar(self, ordinal: int, value_: str) -> None: ...
    def GetSqlBytesRef(self, ordinal: int) -> System.Data.SqlTypes.SqlBytes: ...
    def SetInt64(self, ordinal: int, value_: int) -> None: ...
    def SetObjectRef(self, ordinal: int, value_: Any) -> None: ...
    def SetString(self, ordinal: int, value_: str) -> None: ...
    def SetFloat(self, ordinal: int, value_: float) -> None: ...
    def GetSqlMetaData(self, ordinal: int) -> System.Data.SqlServerCe.SqlMetaData: ...
    def GetSqlBoolean(self, ordinal: int) -> System.Data.SqlTypes.SqlBoolean: ...
    def SetDefault(self, ordinal: int) -> None: ...
    def GetInt64(self, ordinal: int) -> int: ...
    def GetChar(self, ordinal: int) -> str: ...
    def SetSqlSingle(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlSingle
    ) -> None: ...
    def GetSqlByte(self, ordinal: int) -> System.Data.SqlTypes.SqlByte: ...
    def GetValues(self, values: List[Any]) -> int: ...
    def SetInt16(self, ordinal: int, value_: int) -> None: ...
    def GetSqlInt16(self, ordinal: int) -> System.Data.SqlTypes.SqlInt16: ...
    def GetBytes(
        self,
        ordinal: int,
        dataIndex: int,
        buffer: List[int],
        bufferIndex: int,
        length: int,
    ) -> int: ...
    def SetValues(self, values: List[Any]) -> int: ...
    def GetDataTypeName(self, ordinal: int) -> str: ...
    def SetBytes(
        self,
        ordinal: int,
        dataIndex: int,
        buffer: List[int],
        bufferIndex: int,
        length: int,
    ) -> None: ...
    def SetSqlInt16(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlInt16
    ) -> None: ...
    def GetInt16(self, ordinal: int) -> int: ...
    def SetValue(self, ordinal: int, value_: Any) -> None: ...
    def GetFloat(self, ordinal: int) -> float: ...
    def GetFieldType(self, ordinal: int) -> System.Type: ...
    def SetSqlDouble(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlDouble
    ) -> None: ...
    def GetData(self, ordinal: int) -> System.Data.IDataReader: ...
    def SetSqlGuid(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlGuid
    ) -> None: ...
    def SetSqlByte(
        self, ordinal: int, value_: System.Data.SqlTypes.SqlByte
    ) -> None: ...
    def GetSqlString(self, ordinal: int) -> System.Data.SqlTypes.SqlString: ...
    def GetValue(self, ordinal: int) -> Any: ...
    def IsSetAsDefault(self, ordinal: int) -> bool: ...

class SqlMetaData:  # Class
    @overload
    def __init__(self, name: str, dbType: System.Data.SqlDbType) -> None: ...
    @overload
    def __init__(
        self, name: str, dbType: System.Data.SqlDbType, maxLength: int
    ) -> None: ...
    @overload
    def __init__(
        self, name: str, dbType: System.Data.SqlDbType, precision: int, scale: int
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        dbType: System.Data.SqlDbType,
        maxLength: int,
        locale: int,
        compareOptions: System.Data.SqlTypes.SqlCompareOptions,
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        dbType: System.Data.SqlDbType,
        maxLength: int,
        precision: int,
        scale: int,
        localeId: int,
        compareOptions: System.Data.SqlTypes.SqlCompareOptions,
        userDefinedType: System.Type,
    ) -> None: ...

    CompareOptions: System.Data.SqlTypes.SqlCompareOptions  # readonly
    DbType: System.Data.DbType  # readonly
    LocaleId: int  # readonly
    Max: int  # static # readonly
    MaxLength: int  # readonly
    Name: str  # readonly
    Precision: int  # readonly
    Scale: int  # readonly
    SqlDbType: System.Data.SqlDbType  # readonly
    TypeName: str  # readonly

    @overload
    def Adjust(self, value_: int) -> int: ...
    @overload
    def Adjust(self, value_: int) -> int: ...
    @overload
    def Adjust(self, value_: int) -> int: ...
    @overload
    def Adjust(self, value_: float) -> float: ...
    @overload
    def Adjust(self, value_: float) -> float: ...
    @overload
    def Adjust(self, value_: str) -> str: ...
    @overload
    def Adjust(self, value_: System.Decimal) -> System.Decimal: ...
    @overload
    def Adjust(self, value_: System.DateTime) -> System.DateTime: ...
    @overload
    def Adjust(self, value_: System.Guid) -> System.Guid: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlBoolean
    ) -> System.Data.SqlTypes.SqlBoolean: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlByte
    ) -> System.Data.SqlTypes.SqlByte: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlInt16
    ) -> System.Data.SqlTypes.SqlInt16: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlInt32
    ) -> System.Data.SqlTypes.SqlInt32: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlInt64
    ) -> System.Data.SqlTypes.SqlInt64: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlSingle
    ) -> System.Data.SqlTypes.SqlSingle: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlDouble
    ) -> System.Data.SqlTypes.SqlDouble: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlMoney
    ) -> System.Data.SqlTypes.SqlMoney: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlDateTime
    ) -> System.Data.SqlTypes.SqlDateTime: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlDecimal
    ) -> System.Data.SqlTypes.SqlDecimal: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlString
    ) -> System.Data.SqlTypes.SqlString: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlBinary
    ) -> System.Data.SqlTypes.SqlBinary: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlGuid
    ) -> System.Data.SqlTypes.SqlGuid: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlChars
    ) -> System.Data.SqlTypes.SqlChars: ...
    @overload
    def Adjust(
        self, value_: System.Data.SqlTypes.SqlBytes
    ) -> System.Data.SqlTypes.SqlBytes: ...
    @overload
    def Adjust(self, value_: Any) -> Any: ...
    @overload
    def Adjust(self, value_: bool) -> bool: ...
    @overload
    def Adjust(self, value_: int) -> int: ...
    @overload
    def Adjust(self, value_: List[int]) -> List[int]: ...
    @overload
    def Adjust(self, value_: str) -> str: ...
    @overload
    def Adjust(self, value_: List[str]) -> List[str]: ...

class TrackingKeyType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Guid: System.Data.SqlServerCe.TrackingKeyType = ...  # static # readonly
    Max: System.Data.SqlServerCe.TrackingKeyType = ...  # static # readonly
    PrimaryKey: System.Data.SqlServerCe.TrackingKeyType = ...  # static # readonly

class TrackingOptions(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    All: System.Data.SqlServerCe.TrackingOptions = ...  # static # readonly
    Delete: System.Data.SqlServerCe.TrackingOptions = ...  # static # readonly
    Insert: System.Data.SqlServerCe.TrackingOptions = ...  # static # readonly
    Max: System.Data.SqlServerCe.TrackingOptions = ...  # static # readonly
    Update: System.Data.SqlServerCe.TrackingOptions = ...  # static # readonly

class ValidateType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    NoValidation: System.Data.SqlServerCe.ValidateType = ...  # static # readonly
    RowCountOnly: System.Data.SqlServerCe.ValidateType = ...  # static # readonly

class VerifyOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Default: System.Data.SqlServerCe.VerifyOption = ...  # static # readonly
    Enhanced: System.Data.SqlServerCe.VerifyOption = ...  # static # readonly
