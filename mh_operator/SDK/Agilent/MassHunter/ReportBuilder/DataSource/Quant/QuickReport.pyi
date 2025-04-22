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

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.DataSource.Quant.QuickReport

class QuickReportDataSource(
    System.IDisposable, Agilent.MassHunter.ReportBuilder.DataSource.IDataSource
):  # Class
    def __init__(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
        dataNavigator: Agilent.MassHunter.Quantitative.UIModel.IDataNavigator,
        renderGraphics: System.Action[
            Agilent.MassSpectrometry.GUI.Plot.IGraphics, float, float, float, float, str
        ],
    ) -> None: ...
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
    def GetFieldCaption(self, dataName: str, fieldName: str) -> str: ...
    def Select(
        self,
        context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext,
        dataBinding: Agilent.MassHunter.ReportBuilder.Template.IDataBinding,
    ) -> List[Any]: ...
    def LocalizeFieldValue(self, dataName: str, fieldName: str, value_: Any) -> str: ...
    def GetFieldFormat(self, dataName: str, fieldName: str) -> str: ...
    def Dispose(self) -> None: ...

class QuickReportDataSourceDesigner(
    System.IDisposable, Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceDesigner
):  # Class
    def __init__(self) -> None: ...

    DataSourceType: System.Type  # readonly
    DisplayName: str  # readonly
    Name: str  # readonly

    def GetFieldNames(self, dataName: str) -> List[str]: ...
    def GetDataNames(self) -> List[str]: ...
    def GetParameterCategoryDisplayName(self, category: str) -> str: ...
    def GetParameterDisplayName(self, name: str) -> str: ...
    def Dispose(self) -> None: ...
    def GetCustomCommandGroups(
        self, application: Agilent.MassHunter.ReportBuilder.Application.IApplication
    ) -> List[Agilent.MassHunter.ReportBuilder.DataSource.ICustomCommandGroup]: ...
    def GetCustomUI(self) -> T: ...
