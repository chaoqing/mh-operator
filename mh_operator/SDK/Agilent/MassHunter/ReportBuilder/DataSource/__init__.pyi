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

from . import Quant, Unknowns

# Discovered Generic TypeVars:
T = TypeVar("T")
from .Application import IApplication
from .Engine import IGraphicsCanvas, IReportContext
from .Template import HorizontalAlign, IDataBinding, IReportTemplate

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.DataSource

class CustomCommand(
    Agilent.MassHunter.ReportBuilder.DataSource.ICustomCommand
):  # Class
    def __init__(
        self, label: str, tooltip: str, command: System.Windows.Input.ICommand
    ) -> None: ...

    Command: System.Windows.Input.ICommand  # readonly
    Label: str  # readonly
    Tooltip: str  # readonly

class CustomCommandGroup(
    Agilent.MassHunter.ReportBuilder.DataSource.ICustomCommandGroup
):  # Class
    def __init__(
        self,
        label: str,
        commands: List[Agilent.MassHunter.ReportBuilder.DataSource.ICustomCommand],
    ) -> None: ...

    Label: str  # readonly

    def GetCommands(
        self, app: IApplication
    ) -> List[Agilent.MassHunter.ReportBuilder.DataSource.ICustomCommand]: ...

class DataSourceDesignerType(System.IDisposable):  # Class
    def GetType(self, designerTypeName: str) -> System.Type: ...
    @staticmethod
    def GetTypes() -> Iterable[str]: ...
    @staticmethod
    def UninstallDesigners(name: str) -> None: ...
    @staticmethod
    def SetDesignerFolder(name: str, type: str, folder: str) -> None: ...
    @staticmethod
    def GetDesignerDefinitionFolder() -> str: ...
    @staticmethod
    def GetDesignerType(
        type: str,
    ) -> Agilent.MassHunter.ReportBuilder.DataSource.DataSourceDesignerType: ...
    @staticmethod
    def GetDisplayName(type: str, ci: System.Globalization.CultureInfo) -> str: ...
    def Dispose(self) -> None: ...
    @staticmethod
    def InstallDesigners(
        name: str, items: List[Agilent.MassHunter.ReportBuilder.DataSource.DesignerItem]
    ) -> None: ...

class DataSourceGraphicsEnumValue(
    Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceGraphicsEnumValue
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, value_: str, displayText: str) -> None: ...

    DisplayText: str
    Value: str

class DataSourceGraphicsParameter(
    Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceGraphicsParameter
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        category: str,
        displayName: str,
        parameterType: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType,
        acceptsFieldValue: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterAcceptsFieldValue,
    ) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        category: str,
        displayName: str,
        parameterType: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType,
        acceptsFieldValue: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterAcceptsFieldValue,
        enumValues: List[
            Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceGraphicsEnumValue
        ],
    ) -> None: ...

    AcceptsFieldValue: (
        Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterAcceptsFieldValue
    )
    Category: str
    Description: str
    DisplayName: str
    EnumValues: List[
        Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceGraphicsEnumValue
    ]
    HasCustomEditor: bool
    Name: str
    ParameterType: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType

    def GetCustomEditor(
        self, application: IApplication, editorBaseType: System.Type
    ) -> Any: ...

class DefaultDataSource(
    Agilent.MassHunter.ReportBuilder.DataSource.IDataSource
):  # Class
    def __init__(self) -> None: ...
    def DrawGraphics(
        self,
        canvas: IGraphicsCanvas,
        x: float,
        y: float,
        width: float,
        height: float,
        name: str,
        parameters: List[System.Collections.Generic.KeyValuePair[str, Any]],
    ) -> None: ...
    def GetFieldCaption(self, dataName: str, fieldName: str) -> str: ...
    def Select(
        self, context: IReportContext, dataBinding: IDataBinding
    ) -> List[Any]: ...
    def LocalizeFieldValue(self, dataName: str, fieldName: str, value_: Any) -> str: ...
    def GetFieldFormat(self, dataName: str, fieldName: str) -> str: ...

class DefaultDataSourceDesigner(
    System.IDisposable, Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceDesigner
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, dataset: System.Data.DataSet) -> None: ...

    DataSourceType: System.Type  # readonly
    DisplayName: str  # readonly
    Name: str  # readonly

    def GetFieldNames(self, dataName: str) -> List[str]: ...
    def GetDataNames(self) -> List[str]: ...
    def Dispose(self) -> None: ...
    def GetCustomUI(self) -> T: ...

class DesignerDefinition:  # Class
    def __init__(self) -> None: ...

    Designers: List[Agilent.MassHunter.ReportBuilder.DataSource.DesignerItem]

class DesignerItem(System.Xml.Serialization.IXmlSerializable):  # Class
    def __init__(self) -> None: ...

    Folder: str
    Name: str
    Type: str

    def SetDisplayName(self, culture: str, displayName: str) -> None: ...
    def GetSchema(self) -> System.Xml.Schema.XmlSchema: ...
    def GetDisplayName(self, culture: System.Globalization.CultureInfo) -> str: ...
    def WriteXml(self, writer: System.Xml.XmlWriter) -> None: ...
    def ReadXml(self, reader: System.Xml.XmlReader) -> None: ...

class FieldFormat:  # Struct
    def __init__(
        self, format: Agilent.MassHunter.ReportBuilder.DataSource.FieldFormat
    ) -> None: ...

    FixedFormat: str
    HorizontalAlign: HorizontalAlign
    UseFieldFormat: bool

class GraphicsParameterAcceptsFieldValue(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Both: (
        Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterAcceptsFieldValue
    ) = ...  # static # readonly
    FieldValueOnly: (
        Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterAcceptsFieldValue
    ) = ...  # static # readonly
    ValueOnly: (
        Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterAcceptsFieldValue
    ) = ...  # static # readonly

class GraphicsParameterType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Boolean: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType = (
        ...
    )  # static # readonly
    Color: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType = (
        ...
    )  # static # readonly
    Custom: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType = (
        ...
    )  # static # readonly
    Double: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType = (
        ...
    )  # static # readonly
    Enum: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType = (
        ...
    )  # static # readonly
    Int: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType = (
        ...
    )  # static # readonly
    String: Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType = (
        ...
    )  # static # readonly

class ICustomCommand(object):  # Interface
    Command: System.Windows.Input.ICommand  # readonly
    Label: str  # readonly
    Tooltip: str  # readonly

class ICustomCommandGroup(object):  # Interface
    Label: str  # readonly

    def GetCommands(
        self, app: IApplication
    ) -> List[Agilent.MassHunter.ReportBuilder.DataSource.ICustomCommand]: ...

class ICustomUI(object):  # Interface
    def CanExecuteSystemCommand(
        self, app: IApplication, systemCommand: str, parameter: Any, canExecute: bool
    ) -> bool: ...
    def ExecuteSystemCommand(
        self, app: IApplication, systemCommand: str, parameter: Any
    ) -> bool: ...
    def GetCustomCommandGroups(
        self, app: IApplication
    ) -> List[Agilent.MassHunter.ReportBuilder.DataSource.ICustomCommandGroup]: ...

class IDataSource(object):  # Interface
    def DrawGraphics(
        self,
        canvas: IGraphicsCanvas,
        x: float,
        y: float,
        width: float,
        height: float,
        name: str,
        parameters: List[System.Collections.Generic.KeyValuePair[str, Any]],
    ) -> None: ...
    def GetFieldCaption(self, dataName: str, fieldName: str) -> str: ...
    def Select(
        self, context: IReportContext, dataBinding: IDataBinding
    ) -> List[Any]: ...
    def LocalizeFieldValue(self, dataName: str, fieldName: str, value_: Any) -> str: ...
    def GetFieldFormat(self, dataName: str, fieldName: str) -> str: ...

class IDataSourceDesigner(System.IDisposable):  # Interface
    DataSourceType: System.Type  # readonly

    def GetFieldNames(self, dataName: str) -> List[str]: ...
    def GetDataNames(self) -> List[str]: ...
    def GetCustomUI(self) -> T: ...

class IDataSourceGraphicsEdit(object):  # Interface
    def GetGraphicsNames(self) -> List[str]: ...
    def GetDisplayName(self, name: str) -> str: ...
    def GetParameters(
        self, name: str
    ) -> List[
        Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceGraphicsParameter
    ]: ...

class IDataSourceGraphicsEnumValue(object):  # Interface
    DisplayText: str  # readonly
    Value: str  # readonly

class IDataSourceGraphicsParameter(object):  # Interface
    AcceptsFieldValue: (
        Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterAcceptsFieldValue
    )  # readonly
    Category: str  # readonly
    Description: str  # readonly
    DisplayName: str  # readonly
    EnumValues: List[
        Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceGraphicsEnumValue
    ]  # readonly
    HasCustomEditor: bool  # readonly
    Name: str  # readonly
    ParameterType: (
        Agilent.MassHunter.ReportBuilder.DataSource.GraphicsParameterType
    )  # readonly

    def GetCustomEditor(
        self, application: IApplication, editorBasetype: System.Type
    ) -> Any: ...

class IDataSourceTableFormat(object):  # Interface
    def DefaultFieldFormat(
        self,
        dataName: str,
        fieldName: str,
        format: Agilent.MassHunter.ReportBuilder.DataSource.FieldFormat,
    ) -> bool: ...

class IReportPreview(object):  # Interface
    def GeneratePreview(
        self,
        templatePath: str,
        template: IReportTemplate,
        parameterFile: str,
        outputPath: str,
    ) -> None: ...
    def SetupPreview(
        self, parameterPath: str, parent: System.Windows.Window, alwaysShowUI: bool
    ) -> bool: ...

class IValidateTemplate(object):  # Interface
    def ValidateTemplate(
        self,
        context: Agilent.MassHunter.ReportBuilder.DataSource.ValidateTemplateContext,
        template: IReportTemplate,
        application: IApplication,
    ) -> bool: ...

class ValidateTemplateContext(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    OpenTemplate: (
        Agilent.MassHunter.ReportBuilder.DataSource.ValidateTemplateContext
    ) = ...  # static # readonly
    SaveTemplate: (
        Agilent.MassHunter.ReportBuilder.DataSource.ValidateTemplateContext
    ) = ...  # static # readonly
