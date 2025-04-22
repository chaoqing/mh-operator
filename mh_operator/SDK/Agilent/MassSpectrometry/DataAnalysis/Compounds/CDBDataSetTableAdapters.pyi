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

from . import CDBDataSet

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Compounds.CDBDataSetTableAdapters

class CompoundsTableAdapter(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.ComponentModel.Component,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...

    ClearBeforeFill: bool

    @overload
    def Update(self, dataTable: CDBDataSet.CompoundsDataTable) -> int: ...
    @overload
    def Update(self, dataSet: CDBDataSet) -> int: ...
    @overload
    def Update(self, dataRow: System.Data.DataRow) -> int: ...
    @overload
    def Update(self, dataRows: List[System.Data.DataRow]) -> int: ...
    @overload
    def Update(
        self,
        p1: str,
        p2: str,
        p3: str,
        p4: float,
        p5: Optional[float],
        p6: Optional[bool],
        p7: Optional[bool],
        p8: str,
        p9: str,
        p10: str,
        p11: str,
        p12: str,
        p13: str,
        p14: Optional[int],
        p15: str,
        p16: str,
        p17: Optional[System.DateTime],
        p18: Optional[System.DateTime],
        p19: Optional[System.DateTime],
        p20: Optional[float],
        p21: int,
    ) -> int: ...
    def GetData(self) -> CDBDataSet.CompoundsDataTable: ...
    def Insert(
        self,
        p1: str,
        p2: str,
        p3: str,
        p4: float,
        p5: Optional[float],
        p6: Optional[bool],
        p7: Optional[bool],
        p8: str,
        p9: str,
        p10: str,
        p11: str,
        p12: str,
        p13: str,
        p14: Optional[int],
        p15: str,
        p16: str,
        p17: Optional[System.DateTime],
        p18: Optional[System.DateTime],
        p19: Optional[System.DateTime],
        p20: Optional[float],
    ) -> int: ...
    def Delete(self, p1: int) -> int: ...
    def Fill(self, dataTable: CDBDataSet.CompoundsDataTable) -> int: ...

class LibraryTableAdapter(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.ComponentModel.Component,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...

    ClearBeforeFill: bool

    @overload
    def Update(self, dataTable: CDBDataSet.LibraryDataTable) -> int: ...
    @overload
    def Update(self, dataSet: CDBDataSet) -> int: ...
    @overload
    def Update(self, dataRow: System.Data.DataRow) -> int: ...
    @overload
    def Update(self, dataRows: List[System.Data.DataRow]) -> int: ...
    @overload
    def Update(
        self,
        p1: str,
        p2: str,
        p3: str,
        p4: str,
        p5: str,
        p6: Optional[int],
        p7: Optional[int],
        p8: Optional[bool],
        p9: Optional[System.DateTime],
        p10: Optional[System.DateTime],
        p11: int,
    ) -> int: ...
    def GetData(self) -> CDBDataSet.LibraryDataTable: ...
    def Insert(
        self,
        p1: str,
        p2: str,
        p3: str,
        p4: str,
        p5: str,
        p6: Optional[int],
        p7: Optional[int],
        p8: Optional[bool],
        p9: Optional[System.DateTime],
        p10: Optional[System.DateTime],
    ) -> int: ...
    def Delete(self, p1: int) -> int: ...
    def Fill(self, dataTable: CDBDataSet.LibraryDataTable) -> int: ...

class SpectraTableAdapter(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.ComponentModel.Component,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self) -> None: ...

    ClearBeforeFill: bool

    @overload
    def Update(self, dataTable: CDBDataSet.SpectraDataTable) -> int: ...
    @overload
    def Update(self, dataSet: CDBDataSet) -> int: ...
    @overload
    def Update(self, dataRow: System.Data.DataRow) -> int: ...
    @overload
    def Update(self, dataRows: List[System.Data.DataRow]) -> int: ...
    @overload
    def Update(
        self,
        p1: int,
        p2: str,
        p3: str,
        p4: Optional[float],
        p5: Optional[float],
        p6: Optional[float],
        p7: Optional[float],
        p8: Optional[float],
        p9: str,
        p10: str,
        p11: str,
        p12: Optional[int],
        p13: str,
        p14: Optional[System.DateTime],
        p15: Optional[System.DateTime],
        p16: str,
        p17: int,
        p18: int,
    ) -> int: ...
    @overload
    def Update(
        self,
        p2: str,
        p3: str,
        p4: Optional[float],
        p5: Optional[float],
        p6: Optional[float],
        p7: Optional[float],
        p8: Optional[float],
        p9: str,
        p10: str,
        p11: str,
        p12: Optional[int],
        p13: str,
        p14: Optional[System.DateTime],
        p15: Optional[System.DateTime],
        p16: str,
        p17: int,
        p18: int,
    ) -> int: ...
    def GetData(self) -> CDBDataSet.SpectraDataTable: ...
    def Insert(
        self,
        p1: int,
        p2: str,
        p3: str,
        p4: Optional[float],
        p5: Optional[float],
        p6: Optional[float],
        p7: Optional[float],
        p8: Optional[float],
        p9: str,
        p10: str,
        p11: str,
        p12: Optional[int],
        p13: str,
        p14: Optional[System.DateTime],
        p15: Optional[System.DateTime],
        p16: str,
    ) -> int: ...
    def Delete(self, p1: int, p2: int) -> int: ...
    def Fill(self, dataTable: CDBDataSet.SpectraDataTable) -> int: ...

class TableAdapterUtils:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def CreateParamater() -> Any: ...
    @staticmethod
    def GetSelectCommand(
        columnMappings: System.Data.Common.DataColumnMappingCollection, tableName: str
    ) -> str: ...
    @staticmethod
    def GetUpdateCommand() -> Any: ...
    @staticmethod
    def GetInsertCommand() -> Any: ...
    @staticmethod
    def GetIndexOfParameter() -> Any: ...
