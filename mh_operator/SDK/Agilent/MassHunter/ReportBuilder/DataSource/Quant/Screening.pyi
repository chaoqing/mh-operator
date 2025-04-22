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
from . import IQuantDataSourceBase

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.DataSource.Quant.Screening

class DataSourceDesigner(
    Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceDesigner,
    System.IDisposable,
    Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceGraphicsEdit,
):  # Class
    def __init__(self) -> None: ...

    DataSourceType: System.Type  # readonly

    def GetFieldNames(self, dataName: str) -> List[str]: ...
    def GetDataNames(self) -> List[str]: ...
    def GetGraphicsNames(self) -> List[str]: ...
    def GetDisplayName(self, name: str) -> str: ...
    def GetParameters(
        self, name: str
    ) -> List[
        Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceGraphicsParameter
    ]: ...
    def Dispose(self) -> None: ...
    def GetCustomUI(self) -> T: ...

class ScreeningDataSource(
    IQuantDataSourceBase,
    Agilent.MassHunter.ReportBuilder.DataSource.IDataSource,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        state: Agilent.MassSpectrometry.DataAnalysis.Quantitative.PresentationState,
    ) -> None: ...

    BatchFile: str  # readonly
    BatchFolder: str  # readonly
    CompoundFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IDataFilter
    )
    DataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet
    )  # readonly
    FixedGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IFixedGraphics
    )
    GCMode: bool
    LCMode: bool
    PresentationState: (
        Agilent.MassHunter.Quantitative.UIModel.IPresentationState
    )  # readonly
    SampleFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IDataFilter
    )

    def DrawGraphics(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        x: float,
        y: float,
        width: float,
        height: float,
        name: str,
        parameters: List[System.Collections.Generic.KeyValuePair[str, Any]],
    ) -> None: ...
    @staticmethod
    def InitSampleResultTable(table: System.Data.DataTable) -> None: ...
    def GetFieldCaption(self, dataName: str, fieldName: str) -> str: ...
    def Select(
        self,
        context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext,
        dataBinding: Agilent.MassHunter.ReportBuilder.Template.IDataBinding,
    ) -> List[Any]: ...
    @staticmethod
    def InitCompoundResultTable(table: System.Data.DataTable) -> None: ...
    def LocalizeFieldValue(self, dataName: str, fieldName: str, value_: Any) -> str: ...
    def GetFieldFormat(self, dataName: str, fieldName: str) -> str: ...
    def Dispose(self) -> None: ...
