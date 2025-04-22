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
from .AppCommand import AppCommandBase, SetGraphicsPropertiesBase

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Utils

class ComboBoxItem:  # Class
    def __init__(self, value_: Any, displayText: str) -> None: ...

    DisplayText: str  # readonly
    Value: Any  # readonly

class CommandParameterArray(
    Generic[T], Agilent.MassSpectrometry.CommandModel.Model.ICodeDomParameter
):  # Class
    def __init__(self, parameters: Iterable[T]) -> None: ...

class CommandParameterBase:  # Class
    ...

class CompoundGraphicsKey(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Utils.CommandParameterBase
):  # Class
    def __init__(self, reportID: int, compoundGraphicsID: int) -> None: ...

    CompoundGraphicsID: int  # readonly
    ReportID: int  # readonly

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class CompoundGraphicsRangeColumnValueParameter(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Utils.CommandParameterBase
):  # Class
    def __init__(
        self, reportID: int, compoundGraphicsID: int, name: str, value_: Any
    ) -> None: ...

    CompoundGraphicsID: int  # readonly
    Name: str  # readonly
    ReportID: int  # readonly
    Value: Any  # readonly

class FormattingColumnValueParameter(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Utils.CommandParameterBase
):  # Class
    def __init__(
        self, reportID: int, formattingID: int, name: str, value_: Any
    ) -> None: ...

    FormattingID: int  # readonly
    Name: str  # readonly
    ReportID: int  # readonly
    Value: Any  # readonly

class FormattingKey(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Utils.CommandParameterBase
):  # Class
    def __init__(self, reportID: int, formattingID: int) -> None: ...

    FormattingID: int  # readonly
    ReportID: int  # readonly

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class IImportCompounds(object):  # Interface
    Count: int  # readonly

    def GetProperty(self, index: int, propertyName: str) -> Any: ...

class KeyValue(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Utils.CommandParameterBase
):  # Class
    def __init__(self, key: str, value_: Any) -> None: ...

    Key: str  # readonly
    Value: Any  # readonly

    def GetHashCode(self) -> int: ...
    @overload
    def Equals(
        self,
        kv: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Utils.KeyValue,
    ) -> bool: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...

class PrePostProcessColumnValueParameter(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Utils.CommandParameterBase
):  # Class
    def __init__(
        self, reportID: int, prePostProcessID: int, name: str, value_: Any
    ) -> None: ...

    Name: str  # readonly
    PrePostProcessID: int  # readonly
    ReportID: int  # readonly
    Value: Any  # readonly

class PrePostProcessKey(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Utils.CommandParameterBase
):  # Class
    def __init__(self, reportID: int, prePostProcessID: int) -> None: ...

    PrePostProcessID: int  # readonly
    ReportID: int  # readonly

class ReportColumnValueParameter(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.Utils.CommandParameterBase
):  # Class
    def __init__(self, reportID: int, name: str, value_: Any) -> None: ...

    Name: str  # readonly
    ReportID: int  # readonly
    Value: Any  # readonly

class Utilities:  # Class
    @overload
    @staticmethod
    def SetColor(
        cmd: SetGraphicsPropertiesBase,
        reportID: int,
        comboBox: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.ColorComboBox,
        row: System.Data.DataRow,
        name: str,
    ) -> None: ...
    @overload
    @staticmethod
    def SetColor(
        cmd: SetGraphicsPropertiesBase,
        reportID: int,
        color: Optional[System.Drawing.Color],
        row: System.Data.DataRow,
        name: str,
    ) -> None: ...
    @staticmethod
    def SetPrimitiveValue(
        cmd: SetGraphicsPropertiesBase,
        reportID: int,
        value_: T,
        row: System.Data.DataRow,
        name: str,
    ) -> None: ...
    @overload
    @staticmethod
    def ConvertColors(
        row: System.Data.DataRow, column: System.Data.DataColumn
    ) -> List[System.Drawing.Color]: ...
    @overload
    @staticmethod
    def ConvertColors(
        row: System.Data.DataRow, name: str
    ) -> List[System.Drawing.Color]: ...
    @staticmethod
    def SetEnumArrayValue(
        cmd: SetGraphicsPropertiesBase,
        reportID: int,
        values: List[T],
        row: System.Data.DataRow,
        name: str,
    ) -> None: ...
    @overload
    @staticmethod
    def ConvertEnum(
        row: System.Data.DataRow, column: System.Data.DataColumn
    ) -> System.Nullable[T]: ...
    @overload
    @staticmethod
    def ConvertEnum(row: System.Data.DataRow, name: str) -> System.Nullable[T]: ...
    @overload
    @staticmethod
    def ConvertEnums(
        row: System.Data.DataRow, column: System.Data.DataColumn
    ) -> List[T]: ...
    @overload
    @staticmethod
    def ConvertEnums(row: System.Data.DataRow, name: str) -> List[T]: ...
    @staticmethod
    def GetMeasurement(
        tb: System.Windows.Forms.TextBox, value_: Optional[float]
    ) -> bool: ...
    @staticmethod
    def ExecuteCommand(
        parent: System.Windows.Forms.Control, cmd: AppCommandBase
    ) -> bool: ...
    @staticmethod
    def BuildColorArrayString(values: List[System.Drawing.Color]) -> str: ...
    @overload
    @staticmethod
    def ConvertColor(
        row: System.Data.DataRow, column: System.Data.DataColumn
    ) -> Optional[System.Drawing.Color]: ...
    @overload
    @staticmethod
    def ConvertColor(
        row: System.Data.DataRow, name: str
    ) -> Optional[System.Drawing.Color]: ...
    @overload
    @staticmethod
    def ConvertColor(color: str) -> Optional[System.Drawing.Color]: ...
    @staticmethod
    def SetColors(
        cmd: SetGraphicsPropertiesBase,
        reportID: int,
        colors: List[System.Drawing.Color],
        row: System.Data.DataRow,
        name: str,
    ) -> None: ...
    @overload
    @staticmethod
    def SetMeasurement(
        tb: System.Windows.Forms.TextBox, row: System.Data.DataRow, name: str
    ) -> None: ...
    @overload
    @staticmethod
    def SetMeasurement(
        cmd: SetGraphicsPropertiesBase,
        reportID: int,
        tb: System.Windows.Forms.TextBox,
        row: System.Data.DataRow,
        name: str,
    ) -> bool: ...
    @staticmethod
    def BuildEnumArrayString(values: List[T]) -> str: ...
