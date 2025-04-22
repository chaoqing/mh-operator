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

from .Commands import ConversionType
from .Utils import SpectrumKey

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess

class CdbAccess(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.LibraryAccessBase,
):  # Class
    def __init__(
        self,
        library: Agilent.MassSpectrometry.DataAnalysis.PCDLibrary,
        revisionNumber: str,
        lockKey: Any,
    ) -> None: ...

    CompoundCount: int  # readonly
    IsAccurateMass: bool
    IsReadOnly: bool  # readonly
    SpectrumCount: int  # readonly
    SuggestedConversionType: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SuggestedConversionType
    )  # readonly

    def DeleteSpectrum(self, compoundId: int, spectrumId: int) -> None: ...
    def GetLibraryProperty(self, name: str) -> Any: ...
    def Sort(
        self,
        properties: List[str],
        ascending: bool,
        progress: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.LibraryAccessReportSort,
        abort: System.Threading.WaitHandle,
    ) -> None: ...
    def SpectrumDisplayIndexOf(self, compoundId: int, spectrumId: int) -> int: ...
    def GetSpectrumTitle(self, compoundId: int, spectrumId: int) -> str: ...
    def SetSpectrumProperty(
        self, compoundId: int, spectrumId: int, name: str, value_: Any
    ) -> None: ...
    def NewSpectrum(self, compoundId: int, spectrumId: int) -> None: ...
    def GetCompoundIdFromIndex(self, dataIndex: int) -> int: ...
    def SetLibraryProperty(self, name: str, value_: Any) -> None: ...
    def GetSpectrumProperty(
        self, compoundId: int, spectrumId: int, name: str
    ) -> Any: ...
    def GetSpectrumIds(self, compoundId: int) -> List[int]: ...
    def DeleteCompound(self, compoundId: int) -> None: ...
    def GetCompoundProperty(self, compoundId: int, name: str) -> Any: ...
    def ExportToJCAMP(self, file: str, spectrumKeys: List[SpectrumKey]) -> None: ...
    def SetCompoundProperty(self, compoundId: int, name: str, value_: Any) -> None: ...
    def Exists(self, compoundId: int, spectrumId: int) -> bool: ...
    def SaveAs(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        library: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        converesion: ConversionType,
    ) -> None: ...
    def FindNextNewCompoundId(self) -> int: ...
    def NewCompound(self, compoundId: int, displayIndex: int) -> None: ...
    def Save(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

class CompressLibraryAccess(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.LibraryAccessBase,
):  # Class
    def __init__(
        self,
        library: Agilent.MassSpectrometry.DataAnalysis.MSLibrary,
        revisionNumber: str,
        lockKey: Any,
    ) -> None: ...

    CompoundCount: int  # readonly
    IsAccurateMass: bool
    SpectrumCount: int  # readonly
    SuggestedConversionType: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SuggestedConversionType
    )  # readonly

    def DeleteSpectrum(self, compoundId: int, spectrumId: int) -> None: ...
    def GetLibraryProperty(self, name: str) -> Any: ...
    def SpectrumDisplayIndexOf(self, compoundId: int, spectrumId: int) -> int: ...
    def GetSpectrumTitle(self, compoundId: int, spectrumId: int) -> str: ...
    def SetSpectrumProperty(
        self, compoundId: int, spectrumId: int, name: str, value_: Any
    ) -> None: ...
    def NewSpectrum(self, compoundId: int, spectrumId: int) -> None: ...
    def GetCompoundIdFromIndex(self, dataIndex: int) -> int: ...
    def SetLibraryProperty(self, name: str, value_: Any) -> None: ...
    def GetSpectrumProperty(
        self, compoundId: int, spectrumId: int, name: str
    ) -> Any: ...
    def GetSpectrumIds(self, compoundId: int) -> List[int]: ...
    def DeleteCompound(self, compoundId: int) -> None: ...
    def GetCompoundProperty(self, compoundId: int, name: str) -> Any: ...
    def ExportToJCAMP(self, file: str, spectrumKeys: List[SpectrumKey]) -> None: ...
    def SetCompoundProperty(self, compoundId: int, name: str, value_: Any) -> None: ...
    def Exists(self, compoundId: int, spectrumId: int) -> bool: ...
    def SaveAs(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        library: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        conversion: ConversionType,
    ) -> None: ...
    def FindNextNewCompoundId(self) -> int: ...
    def NewCompound(self, compoundId: int, displayIndex: int) -> None: ...
    def Save(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

class ContainsOperator(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
):  # Class
    def __init__(self, ignoreCase: bool) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class DataSetAccess(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.LibraryAccessBase,
):  # Class
    def __init__(
        self,
        library: Agilent.MassSpectrometry.DataAnalysis.ILibrary,
        revisionNumber: str,
        lockKey: Any,
    ) -> None: ...

    CompoundCount: int  # readonly
    IsAccurateMass: bool
    MassSpecLibrary: Agilent.MassSpectrometry.DataAnalysis.MassSpecLibrary  # readonly
    SpectrumCount: int  # readonly
    SuggestedConversionType: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SuggestedConversionType
    )  # readonly

    def DeleteSpectrum(self, compoundId: int, spectrumId: int) -> None: ...
    def GetLibraryProperty(self, name: str) -> Any: ...
    def SpectrumDisplayIndexOf(self, compoundId: int, spectrumId: int) -> int: ...
    def GetSpectrumTitle(self, compoundId: int, spectrumId: int) -> str: ...
    def SetSpectrumProperty(
        self, compoundId: int, spectrumId: int, name: str, value_: Any
    ) -> None: ...
    def NewSpectrum(self, compoundId: int, spectrumId: int) -> None: ...
    def GetCompoundIdFromIndex(self, dataIndex: int) -> int: ...
    def SetLibraryProperty(self, name: str, value_: Any) -> None: ...
    def GetSpectrumProperty(
        self, compoundId: int, spectrumId: int, name: str
    ) -> Any: ...
    def GetSpectrumIds(self, compoundId: int) -> List[int]: ...
    def DeleteCompound(self, compoundId: int) -> None: ...
    def GetCompoundProperty(self, compoundId: int, name: str) -> Any: ...
    def ExportToJCAMP(self, file: str, spectrumKeys: List[SpectrumKey]) -> None: ...
    def SetCompoundProperty(self, compoundId: int, name: str, value_: Any) -> None: ...
    def Exists(self, compoundId: int, spectrumId: int) -> bool: ...
    def SaveAs(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        library: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        conversion: ConversionType,
    ) -> None: ...
    def FindNextNewCompoundId(self) -> int: ...
    def Convert(
        self, infoType: Agilent.MassSpectrometry.DataAnalysis.LibraryRTInfoType
    ) -> None: ...
    def NewCompound(self, compoundId: int, displayIndex: int) -> None: ...
    def Save(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

class DisplayList(System.IDisposable):  # Class
    def Dispose(self) -> None: ...

class EqualOperator(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
):  # Class
    def __init__(self, ignoreCase: bool) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class GreaterEqualOperator(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class GreaterOperator(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class IsNullOperator(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class LessEqualOperator(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class LessOperator(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class LibraryAccessBase(System.MarshalByRefObject, System.IDisposable):  # Class
    AutoClose: bool
    CompoundCount: int  # readonly
    DisplayedCompoundCount: int  # readonly
    IsAccurateMass: bool
    IsReadOnly: bool  # readonly
    LibraryPath: str
    SpectrumCount: int  # readonly
    StorageFormat: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat  # readonly
    SuggestedConversionType: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SuggestedConversionType
    )  # readonly

    def FindNextNewCompoundId(self) -> int: ...
    def GetSpectrumProperty(
        self, compoundId: int, spectrumId: int, name: str
    ) -> Any: ...
    def Sort(
        self,
        properties: List[str],
        ascending: bool,
        progress: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.LibraryAccessReportSort,
        abort: System.Threading.WaitHandle,
    ) -> None: ...
    def Exists(self, compoundId: int, spectrumId: int) -> bool: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def OpenLibrary(
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        path: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        revisionNumber: str,
        readOnly: bool,
        lockKey: Any,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.LibraryAccessBase
    ): ...
    def GetSpectrumTitle(self, compoundId: int, spectrumId: int) -> str: ...
    def GetLibraryProperty(self, name: str) -> Any: ...
    def GetSpectrumIds(self, compoundId: int) -> List[int]: ...
    def GetCompoundIdFromIndex(self, dataIndex: int) -> int: ...
    def Save(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...
    def NewCompound(self, compoundId: int, displayIndex: int) -> None: ...
    def Search(
        self,
        conditions: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchConditions,
        progress: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.LibraryAccessReportSearch,
        abort: System.Threading.WaitHandle,
    ) -> None: ...
    def SetLibraryProperty(self, name: str, value_: Any) -> None: ...
    def GetCompoundIdFromDisplayIndex(self, displayIndex: int) -> int: ...
    @staticmethod
    def CreateLibrary(
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        path: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        lockKey: Any,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.LibraryAccessBase
    ): ...
    def DeleteCompound(self, compoundId: int) -> None: ...
    def ClearSearch(self) -> None: ...
    def SetCompoundProperty(self, compoundId: int, name: str, value_: Any) -> None: ...
    def NewSpectrum(self, compoundId: int, spectrumId: int) -> None: ...
    def DeleteSpectrum(self, compoundId: int, spectrumId: int) -> None: ...
    def GetCompoundProperty(self, compoundId: int, name: str) -> Any: ...
    def SpectrumDisplayIndexOf(self, compoundId: int, spectrumId: int) -> int: ...
    def SetSpectrumProperty(
        self, compoundId: int, spectrumId: int, name: str, value_: Any
    ) -> None: ...
    def ExportToJCAMP(self, file: str, spectrumKeys: List[SpectrumKey]) -> None: ...
    def CompoundDisplayIndexOf(self, compoundId: int) -> int: ...
    def SaveAs(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        library: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        conversion: ConversionType,
    ) -> None: ...

class LibraryAccessReportSearch(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        percent: float,
        countChanged: bool,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, percent: float, countChanged: bool) -> None: ...

class LibraryAccessReportSort(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self, percent: float, callback: System.AsyncCallback, object: Any
    ) -> System.IAsyncResult: ...
    def Invoke(self, percent: float) -> None: ...

class NotContainsOperator(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
):  # Class
    def __init__(self, ignoreCase: bool) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class NotEqualOperator(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
):  # Class
    def __init__(self, ignoreCase: bool) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class NotNullOperator(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class SearchCondition:  # Class
    def __init__(
        self,
        property: str,
        isSpectrum: bool,
        type: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType,
        value_: Any,
        ignoreCase: Optional[bool],
    ) -> None: ...
    def Match(
        self,
        access: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.LibraryAccessBase,
        compoundId: int,
    ) -> bool: ...

class SearchConditions:  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly

    def Match(
        self,
        access: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.LibraryAccessBase,
        compoundId: int,
    ) -> bool: ...
    def Add(
        self,
        condition: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchCondition,
    ) -> None: ...

class SearchOperator:  # Class
    def Match(self, value1: Any, value2: Any) -> bool: ...
    @staticmethod
    def Create(
        type: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType,
        ignoreStringCase: Optional[bool],
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperator
    ): ...
    @staticmethod
    def RequiresValue(
        type: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType,
    ) -> bool: ...

class SearchOperatorType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Contains: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType
    ) = ...  # static # readonly
    Equal: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType
    ) = ...  # static # readonly
    Greater: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType
    ) = ...  # static # readonly
    GreaterEqual: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType
    ) = ...  # static # readonly
    IsNull: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType
    ) = ...  # static # readonly
    Less: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType
    ) = ...  # static # readonly
    LessEqual: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType
    ) = ...  # static # readonly
    NotContains: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType
    ) = ...  # static # readonly
    NotEqual: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType
    ) = ...  # static # readonly
    NotNull: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SearchOperatorType
    ) = ...  # static # readonly

class SuggestedConversionType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    RTRI_L_RI: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SuggestedConversionType
    ) = ...  # static # readonly
    RTRI_L_RTL: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SuggestedConversionType
    ) = ...  # static # readonly
    RTRI_XML: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.DataAccess.SuggestedConversionType
    ) = ...  # static # readonly
