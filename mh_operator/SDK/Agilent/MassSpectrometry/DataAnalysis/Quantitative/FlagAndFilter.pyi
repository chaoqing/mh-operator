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

from . import (
    BatchFiles,
    IOutlier,
    OutlierColumns,
    OutlierCompoundType,
    OutlierFilterType,
    QuantitationDataSet,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FlagAndFilter

class FlagFilterManager(
    System.IDisposable, Agilent.MassHunter.Quantitative.UIModel.IFlagFilterManager
):  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly
    Filter: bool
    FilterType: OutlierFilterType
    Flag: bool
    def __getitem__(
        self, index: int
    ) -> Agilent.MassHunter.Quantitative.UIModel.IFlagFilter: ...
    def __getitem__(
        self, column: OutlierColumns
    ) -> Agilent.MassHunter.Quantitative.UIModel.IFlagFilter: ...
    def RemoveAt(self, index: int) -> None: ...
    def SampleFilterMatch(
        self,
        sampleRow: QuantitationDataSet.BatchRow,
        compoundKeys: List[Agilent.MassHunter.Quantitative.UIModel.CompoundKey],
    ) -> bool: ...
    def Initialize(
        self, state: Agilent.MassHunter.Quantitative.UIModel.IPresentationState
    ) -> None: ...
    def Add(
        self,
        ff: Agilent.MassSpectrometry.DataAnalysis.Quantitative.FlagAndFilter.IFlagFilter,
    ) -> None: ...
    def SummaryMatch(
        self,
        sampleRow: QuantitationDataSet.BatchRow,
        compoundKeys: List[Agilent.MassHunter.Quantitative.UIModel.CompoundKey],
        messages: System.Text.StringBuilder,
    ) -> bool: ...
    def EndEdit(self) -> None: ...
    def BeginEdit(self) -> None: ...
    def CompoundFilterMatch(
        self,
        compoundRow: QuantitationDataSet.TargetCompoundRow,
        sampleRows: List[System.Data.DataRow],
    ) -> bool: ...
    def Dispose(self) -> None: ...
    def FlagMatch(
        self,
        relation: str,
        column: str,
        parentRow: System.Data.DataRow,
        row: System.Data.DataRow,
        backColor: System.Drawing.Color,
        foreColor: System.Drawing.Color,
        messages: System.Text.StringBuilder,
    ) -> bool: ...

    Changed: System.EventHandler  # Event

class IFlagFilter(Agilent.MassHunter.Quantitative.UIModel.IFlagFilter):  # Interface
    ...

class OutlierFlagFilter(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.FlagAndFilter.IFlagFilter,
    Agilent.MassHunter.Quantitative.UIModel.IFlagFilter,
):  # Class
    def __init__(self) -> None: ...

    Category: str  # readonly
    ColumnName: str  # readonly
    Enabled: bool
    Name: str  # readonly
    OutlierCompoundType: OutlierCompoundType  # readonly
    OutlierType: OutlierColumns  # readonly
    OutlierValueColumnName: str  # readonly
    OutlierValueRelationName: str  # readonly
    RelationName: str  # readonly

    def Available(
        self, dataset: System.Data.DataSet, batchFiles: BatchFiles, batchId: int
    ) -> bool: ...
    def Initialize(self, outlier: IOutlier) -> None: ...
    def GetMessage(self, row: System.Data.DataRow) -> str: ...
    @staticmethod
    def IsOutlierAvailable(
        dataset: System.Data.DataSet,
        batchFiles: BatchFiles,
        batchId: int,
        outlierColumn: OutlierColumns,
    ) -> bool: ...
    @staticmethod
    def UpdateColors() -> None: ...
    def Match(
        self,
        row: System.Data.DataRow,
        type: OutlierFilterType,
        backColor: System.Drawing.Color,
        foreColor: System.Drawing.Color,
    ) -> bool: ...
