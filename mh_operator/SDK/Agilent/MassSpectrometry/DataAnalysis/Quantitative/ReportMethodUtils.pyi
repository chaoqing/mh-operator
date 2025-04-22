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

from .Compliance import ICompliance
from .ReportMethod import ReportMethodDataSet

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils

class FilteringOperator(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Equal: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FilteringOperator
    ) = ...  # static # readonly
    Greater: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FilteringOperator
    ) = ...  # static # readonly
    GreaterOrEqual: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FilteringOperator
    ) = ...  # static # readonly
    IsNull: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FilteringOperator
    ) = ...  # static # readonly
    Less: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FilteringOperator
    ) = ...  # static # readonly
    LessOrEqual: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FilteringOperator
    ) = ...  # static # readonly
    NotEqual: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FilteringOperator
    ) = ...  # static # readonly
    NotNull: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FilteringOperator
    ) = ...  # static # readonly

class FilteringType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Compound: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FilteringType
    ) = ...  # static # readonly
    Sample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FilteringType
    ) = ...  # static # readonly

class FormattingType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Batch: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FormattingType
    ) = ...  # static # readonly
    SingleSample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.FormattingType
    ) = ...  # static # readonly

class MethodFileIO:  # Class
    Ext_MethodFile_Quant: str = ...  # static # readonly
    Ext_MethodFile_Unknowns: str = ...  # static # readonly
    Ext_MethodFolder: str = ...  # static # readonly
    UnifiedMethod_File: str = ...  # static # readonly
    UnifiedMethod_Path_Quant: str = ...  # static # readonly
    UnifiedMethod_Path_Unknowns: str = ...  # static # readonly

    @overload
    @staticmethod
    def Read(
        dataset: ReportMethodDataSet,
        path: str,
        isUnknowns: bool,
        checkVersion: bool,
        checkHashCode: bool,
    ) -> None: ...
    @overload
    @staticmethod
    def Read(
        dataset: ReportMethodDataSet,
        stream: System.IO.Stream,
        isUnknowns: bool,
        checkVersion: bool,
        checkHashcode: bool,
    ) -> None: ...
    @overload
    @staticmethod
    def Read(
        dataset: ReportMethodDataSet,
        stream: System.IO.Stream,
        isUnknowns: bool,
        checkVersion: bool,
        checkHashcode: bool,
        autoUpgrade: bool,
        hashCodeRead: str,
    ) -> None: ...

class PrePostProcessClass(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Pool: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PrePostProcessClass
    ) = ...  # static # readonly
    PostFormatting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PrePostProcessClass
    ) = ...  # static # readonly
    PostReport: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PrePostProcessClass
    ) = ...  # static # readonly
    PreFormatting: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PrePostProcessClass
    ) = ...  # static # readonly
    PreReport: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PrePostProcessClass
    ) = ...  # static # readonly

class PrePostProcessType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Custom: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PrePostProcessType
    ) = ...  # static # readonly
    DeleteGraphicsFiles: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PrePostProcessType
    ) = ...  # static # readonly

class PublishFormat(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CSV: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PublishFormat
    ) = ...  # static # readonly
    PDF: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PublishFormat
    ) = ...  # static # readonly
    TEXT: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PublishFormat
    ) = ...  # static # readonly
    XLSX: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PublishFormat
    ) = ...  # static # readonly
    XPS: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.PublishFormat
    ) = ...  # static # readonly

class ReportMethodException(
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

class ReportType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Batch: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.ReportType
    ) = ...  # static # readonly
    SingleSample: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodUtils.ReportType
    ) = ...  # static # readonly

class Utilities:  # Class
    @staticmethod
    def GetColors(colors: str) -> List[System.Drawing.Color]: ...
    @overload
    @staticmethod
    def SetupUnknownsSettings(
        row: ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow,
        settings: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ChromatogramSettings,
    ) -> None: ...
    @overload
    @staticmethod
    def SetupUnknownsSettings(
        row: ReportMethodDataSet.UnknownsIonPeaksGraphicsRow,
        settings: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.IonPeaksSettings,
    ) -> None: ...
    @overload
    @staticmethod
    def SetupUnknownsSettings(
        row: ReportMethodDataSet.UnknownsSpectrumGraphicsRow,
        settings: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.SpectrumSettings,
    ) -> None: ...
    @staticmethod
    def IsBuilderTemplate(compliance: ICompliance, templatePath: str) -> bool: ...
    @staticmethod
    def IsScriptTemplate(compliance: ICompliance, templatePath: str) -> bool: ...
    @staticmethod
    def GetColorString(colors: List[System.Drawing.Color]) -> str: ...
    @staticmethod
    def IsExcelTemplate(template: str) -> bool: ...
    @staticmethod
    def HasExcelTemplates(table: ReportMethodDataSet.FormattingDataTable) -> bool: ...
    @staticmethod
    def Upgrade(dataset: ReportMethodDataSet, isUnknowns: bool) -> None: ...
    @overload
    @staticmethod
    def SetDefaults(
        uscgr: ReportMethodDataSet.UnknownsSampleChromatogramGraphicsRow, reportID: int
    ) -> None: ...
    @overload
    @staticmethod
    def SetDefaults(
        row: ReportMethodDataSet.UnknownsIonPeaksGraphicsRow, reportID: int
    ) -> None: ...
    @overload
    @staticmethod
    def SetDefaults(
        row: ReportMethodDataSet.UnknownsSpectrumGraphicsRow, reportID: int
    ) -> None: ...
