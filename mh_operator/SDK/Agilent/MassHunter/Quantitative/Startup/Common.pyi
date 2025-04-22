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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Common

class BatchTable(
    System.IEquatable[Agilent.MassHunter.Quantitative.Startup.Common.BatchTable]
):  # Class
    def __init__(self) -> None: ...

    CurrentSchemaVersion: int  # static # readonly
    FileName: str = ...  # static # readonly

    DefaultBatchSingleMode: bool
    DefaultBatchTableViewMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.TableViewMode
    )
    SchemaVersion: int
    VisibleColumns: List[Agilent.MassHunter.Quantitative.Startup.Common.VisibleColumns]

    def SaveTo(self, stream: System.IO.Stream) -> None: ...
    def Equals(
        self, bt: Agilent.MassHunter.Quantitative.Startup.Common.BatchTable
    ) -> bool: ...
    @staticmethod
    def Load(
        filepath: str,
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.BatchTable: ...
    @staticmethod
    def CreateDefault() -> (
        Agilent.MassHunter.Quantitative.Startup.Common.BatchTable
    ): ...
    def SetupBatchTable(self) -> None: ...

class ColumnLabel(
    System.IEquatable[Agilent.MassHunter.Quantitative.Startup.Common.ColumnLabel]
):  # Class
    def __init__(self) -> None: ...

    Hidden: bool
    Labels: List[Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText]
    Name: str
    Relation: str

    def FindLocalizableText(
        self, culture: System.Globalization.CultureInfo
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText: ...
    def Equals(
        self, label: Agilent.MassHunter.Quantitative.Startup.Common.ColumnLabel
    ) -> bool: ...

class ColumnLabels(
    System.IEquatable[Agilent.MassHunter.Quantitative.Startup.Common.ColumnLabels]
):  # Class
    def __init__(self) -> None: ...

    CurrentSchemaVersion: int  # static # readonly
    FileName_QuantDefault: str = ...  # static # readonly

    Labels: List[Agilent.MassHunter.Quantitative.Startup.Common.ColumnLabel]
    SchemaVersion: int

    def SaveTo(self, stream: System.IO.Stream) -> None: ...
    def Equals(
        self, labels: Agilent.MassHunter.Quantitative.Startup.Common.ColumnLabels
    ) -> bool: ...
    @overload
    @staticmethod
    def Load(
        filepath: str,
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.ColumnLabels: ...
    @overload
    @staticmethod
    def Load(
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        filepath: str,
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.ColumnLabels: ...
    def SetupQuantColumnLabels(
        self,
        instrumentType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType,
    ) -> None: ...
    @staticmethod
    def CreateDefault() -> (
        Agilent.MassHunter.Quantitative.Startup.Common.ColumnLabels
    ): ...

class Deploy:  # Class
    def __init__(self) -> None: ...

    CurrentSchemaVeresion: int  # static # readonly
    FileExt: str = ...  # static # readonly

    Configurations: List[
        Agilent.MassHunter.Quantitative.Startup.Common.DeployConfiguration
    ]
    Embedded: bool
    SchemaVersion: int

    @staticmethod
    def GenerateDeployment(
        pathName: str,
        startupRootFolder: str,
        configurationsToArchilve: List[str],
        embed: bool,
    ) -> None: ...
    @staticmethod
    def ExtractDeployment(
        pathName: str,
        destinationFolder: str,
        configurationCallback: System.Action[
            Agilent.MassHunter.Quantitative.Startup.Common.DeployConfiguration
        ],
    ) -> None: ...

class DeployConfiguration:  # Class
    def __init__(self) -> None: ...

    Name: str
    PathName: str

class LocalizableText(
    System.IEquatable[Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText]
):  # Class
    def __init__(self) -> None: ...

    Culture: str
    Value: str
    _Culture: System.Globalization.CultureInfo  # readonly

    @staticmethod
    def FindLocalizableText(
        texts: List[Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText],
        culture: System.Globalization.CultureInfo,
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText: ...
    @staticmethod
    def MatchCulture(
        ci: System.Globalization.CultureInfo, textci: System.Globalization.CultureInfo
    ) -> bool: ...
    @overload
    @staticmethod
    def Equals(
        lt: Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText,
    ) -> bool: ...
    @overload
    @staticmethod
    def Equals(
        arr1: List[Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText],
        arr2: List[Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText],
    ) -> bool: ...

class OutlierSetting(
    System.IEquatable[Agilent.MassHunter.Quantitative.Startup.Common.OutlierSetting]
):  # Class
    def __init__(self) -> None: ...

    Hidden: bool
    Labels: List[Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText]
    OutlierColumn: Agilent.MassSpectrometry.DataAnalysis.Quantitative.OutlierColumns

    def Equals(
        self, o: Agilent.MassHunter.Quantitative.Startup.Common.OutlierSetting
    ) -> bool: ...

class Outliers(
    System.IEquatable[Agilent.MassHunter.Quantitative.Startup.Common.Outliers]
):  # Class
    def __init__(self) -> None: ...

    CurrentSchemaVersion: int  # static # readonly
    FileName: str = ...  # static # readonly

    OutlierSettings: List[Agilent.MassHunter.Quantitative.Startup.Common.OutlierSetting]
    SchemaVersion: int

    def SaveTo(self, stream: System.IO.Stream) -> None: ...
    def Equals(
        self, o: Agilent.MassHunter.Quantitative.Startup.Common.Outliers
    ) -> bool: ...
    @staticmethod
    def Load(
        filepath: str,
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.Outliers: ...
    @staticmethod
    def CreateDefault() -> Agilent.MassHunter.Quantitative.Startup.Common.Outliers: ...
    def SetupConfiguration(self) -> None: ...

class SampleTypeLabel(
    System.IEquatable[Agilent.MassHunter.Quantitative.Startup.Common.SampleTypeLabel]
):  # Class
    def __init__(self) -> None: ...

    Labels: List[Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText]
    SampleType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.SampleType
    Visible: bool

    def FindLabel(
        self, culture: System.Globalization.CultureInfo
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText: ...
    def Equals(
        self, st: Agilent.MassHunter.Quantitative.Startup.Common.SampleTypeLabel
    ) -> bool: ...

class SampleTypes(
    System.IEquatable[Agilent.MassHunter.Quantitative.Startup.Common.SampleTypes]
):  # Class
    def __init__(self) -> None: ...

    CurrentSchemaVersion: int  # static # readonly
    FileName_QuantDefault: str = ...  # static # readonly

    SampleTypeLabels: List[
        Agilent.MassHunter.Quantitative.Startup.Common.SampleTypeLabel
    ]
    SchemaVersion: int

    def SaveTo(self, stream: System.IO.Stream) -> None: ...
    def Equals(
        self, sts: Agilent.MassHunter.Quantitative.Startup.Common.SampleTypes
    ) -> bool: ...
    @staticmethod
    def Load(
        filepath: str,
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.SampleTypes: ...
    @staticmethod
    def CreateDefault() -> (
        Agilent.MassHunter.Quantitative.Startup.Common.SampleTypes
    ): ...
    def SetupConfiguration(self, culture: System.Globalization.CultureInfo) -> None: ...

class Startup(
    System.IEquatable[Agilent.MassHunter.Quantitative.Startup.Common.Startup]
):  # Class
    def __init__(self) -> None: ...

    CurrentSchemaVersion: int  # static # readonly
    FileName: str = ...  # static # readonly
    FileName_WpfCagToolsDefault: str = ...  # static # readonly
    FileName_WpfCiwToolsDefault: str = ...  # static # readonly
    FileName_WpfToolsDefault: str = ...  # static # readonly

    AllowFlexibleDocking: bool
    DisplayNames: List[Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText]
    Instrument: str
    SchemaVersion: int
    StartupLocation: str  # readonly
    _Instrument: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType
    )  # readonly

    def SaveTo(self, stream: System.IO.Stream) -> None: ...
    def Equals(
        self, startup: Agilent.MassHunter.Quantitative.Startup.Common.Startup
    ) -> bool: ...
    @staticmethod
    def Load(
        startupLocation: str,
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.Startup: ...
    @staticmethod
    def CreateDefault(
        folderName: str,
        instrument: Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType,
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.Startup: ...
    def GetDisplayName(
        self, culture: System.Globalization.CultureInfo
    ) -> Agilent.MassHunter.Quantitative.Startup.Common.LocalizableText: ...

class StartupException(
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
    def __init__(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class VisibleColumns:  # Class
    def __init__(self) -> None: ...

    Columns: List[str]
    Relation: str
    SingleMode: bool
    TableViewMode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.TableViewMode

    def GetHashCode(self) -> int: ...
    @staticmethod
    def ArrayEquals(
        arr1: List[Agilent.MassHunter.Quantitative.Startup.Common.VisibleColumns],
        arr2: List[Agilent.MassHunter.Quantitative.Startup.Common.VisibleColumns],
    ) -> bool: ...
    @staticmethod
    def StringArrayEquals(arr1: List[str], arr2: List[str]) -> bool: ...
    def Equals(self, obj: Any) -> bool: ...
