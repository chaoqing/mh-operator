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

from . import Printing, Utils

# Discovered Generic TypeVars:
T = TypeVar("T")

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2

class AddInAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, applicationName: str, addInType: System.Type) -> None: ...

    AddInType: System.Type  # readonly
    ApplicationName: str  # readonly

class AddInConfigurationElement:  # Class
    Enabled: bool
    IsScript: bool  # readonly
    PathName: str  # readonly
    Type: str  # readonly

    def Equals(
        self,
        element: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.AddInConfigurationElement,
    ) -> bool: ...
    def Clone(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.AddInConfigurationElement
    ): ...

class AddInConfigurationSection(System.Configuration.ConfigurationSection):  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly
    def __getitem__(
        self, index: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.AddInConfigurationElement
    ): ...
    def Contains(self, pathName: str, type: str, isScript: bool) -> bool: ...
    def GetElement(
        self, pathName: str, type: str, isScript: bool
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.AddInConfigurationElement
    ): ...
    def Add(
        self, pathName: str, type: str, isScript: bool
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.AddInConfigurationElement
    ): ...

class AddInManager(System.IDisposable):  # Class
    def __init__(self, state: Any) -> None: ...

    AddInsTabID: str = ...  # static # readonly

    Count: int  # readonly
    RibbonSharedRibbonTabCaption: str  # static # readonly
    State: Any  # readonly

    def Contains(self, id: str) -> bool: ...
    def GetScriptEngine(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.IAddInScriptEngine
    ): ...
    def GetType(self, id: str) -> str: ...
    def IsEnabled(self, id: str) -> bool: ...
    def GetAddIn(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.IAddIn: ...
    @staticmethod
    def GetAddInID(pathName: str, type: str) -> str: ...
    def LoadScript(self, scriptPath: str) -> None: ...
    def CreateScriptAddin(
        self, pathName: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.IAddIn: ...
    def Clear(self) -> None: ...
    def Enable(
        self, id: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.IAddIn: ...
    def GetPathName(self, id: str) -> str: ...
    def LoadAssembly(self, assemblyPath: str, appName: str) -> int: ...
    def Dispose(self) -> None: ...
    def GetIDs(self) -> List[str]: ...
    def Disable(self, id: str) -> None: ...
    def IsScript(self, id: str) -> bool: ...

class ConfigurationArrayElement(
    Generic[T], System.Xml.Serialization.IXmlSerializable
):  # Class
    Count: int  # readonly
    def __getitem__(self, index: int) -> T: ...
    def __setitem__(self, index: int, value_: T) -> None: ...
    @overload
    def Equals(self, obj: Any) -> bool: ...
    @overload
    def Equals(
        self,
        element: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationArrayElement,
    ) -> bool: ...
    def Add(self, t: T) -> None: ...
    def Clear(self) -> None: ...
    def AddRange(self, e: Iterable[T]) -> None: ...
    def GetHashCode(self) -> int: ...
    def GetSchema(self) -> System.Xml.Schema.XmlSchema: ...
    def WriteXml(self, writer: System.Xml.XmlWriter) -> None: ...
    def ReadXml(self, reader: System.Xml.XmlReader) -> None: ...
    def SetArray(self, array: List[T]) -> None: ...
    def ToArray(self) -> List[T]: ...

class ConfigurationColorArrayElement(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationArrayElement[
        System.Drawing.Color
    ],
    System.Xml.Serialization.IXmlSerializable,
):  # Class
    def __init__(self) -> None: ...

class ConfigurationElementSectionBase(
    System.Configuration.ConfigurationSection
):  # Class
    def __init__(self) -> None: ...

class ConfigurationStringArrayElement(
    System.Xml.Serialization.IXmlSerializable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationArrayElement[
        str
    ],
):  # Class
    def __init__(self) -> None: ...

class ControlHelpMap(System.IDisposable):  # Class
    @overload
    def __init__(
        self, control: System.Windows.Forms.Control, helpFile: str, helpId: int
    ) -> None: ...
    @overload
    def __init__(
        self, dialog: System.Windows.Forms.CommonDialog, helpFile: str, helpId: int
    ) -> None: ...

    HelpId: int  # readonly

    def Dispose(self) -> None: ...
    def ShowHelp(self) -> None: ...

class ControlHtmlHelpMap(System.IDisposable):  # Class
    def __init__(
        self,
        control: System.Windows.Forms.Control,
        root: str,
        subfolder: str,
        html: str,
        topic: str,
    ) -> None: ...
    def Dispose(self) -> None: ...
    def ShowHelp(self) -> None: ...

class DelayDeleteFile:  # Class
    def __init__(self, file: str) -> None: ...

class EnumItem(Generic[T]):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, t: T, displayText: str) -> None: ...

    DisplayText: str  # readonly
    Value: T  # readonly

    def ToString(self) -> str: ...

class GridUtils:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def SetVisibleColumns(
        view: System.Windows.Forms.DataGridView, columns: List[str]
    ) -> None: ...

class HelpUtils:  # Class
    @staticmethod
    def ShowHtmlHelp(
        helproot: str, subfolder: str, htmlfile: str, topic: str
    ) -> bool: ...
    @staticmethod
    def GetLastTimeHelpLaunched() -> System.DateTime: ...

    # Nested Types

    class ActivateOptions(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        DesignMode: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.HelpUtils.ActivateOptions
        ) = ...  # static # readonly
        NoErrorUI: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.HelpUtils.ActivateOptions
        ) = ...  # static # readonly
        NoSplashScreen: (
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.HelpUtils.ActivateOptions
        ) = ...  # static # readonly

class IAddIn(object):  # Interface
    DisplayName: str  # readonly
    Enabled: bool  # readonly

    def Uninitialize(self, state: Any) -> None: ...
    def Initialize(self, state: Any) -> None: ...
    def Execute(self, parameters: List[Any]) -> Any: ...

class IAddInScriptEngine(object):  # Interface
    def ExecuteFile(self, file: str) -> Any: ...

class IdleDetector(System.IDisposable, System.Windows.Forms.IMessageFilter):  # Class
    def __init__(
        self, inputElement: System.Windows.IInputElement, seconds: int
    ) -> None: ...
    def PreFilterMessage(self, m: System.Windows.Forms.Message) -> bool: ...
    def Dispose(self) -> None: ...
    def ChangeIdleTime(self, newIdleTime: int) -> None: ...

    IsIdle: System.EventHandler  # Event

class NotifyPropertyBase(System.ComponentModel.INotifyPropertyChanged):  # Class
    def VerifyPropertyName(self, propertyName: str) -> None: ...

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class RelayCommand(System.Windows.Input.ICommand):  # Class
    @overload
    def __init__(self, execute: System.Action) -> None: ...
    @overload
    def __init__(
        self, execute: System.Action, canExecute: System.Func[Any, bool]
    ) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Execute(self, parameter: Any) -> None: ...
    def NotifyCanExecuteChanged(self) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class StringNumberComparer(
    System.Collections.Generic.IComparer[str], System.Collections.IComparer
):  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def _Compare(x: str, y: str) -> int: ...
    @overload
    def Compare(self, x: str, y: str) -> int: ...
    @overload
    def Compare(self, x: Any, y: Any) -> int: ...

class Utilities:  # Class
    CustomerHome: str  # static # readonly

    @staticmethod
    def WriteRowToCsv(
        row: System.Windows.Forms.DataGridViewRow,
        writer: System.IO.TextWriter,
        delimiter: str,
    ) -> None: ...
    @staticmethod
    def GetFolder(folder: str) -> str: ...
    @staticmethod
    def ToSignificantDigits(value_: float, significantDigits: int) -> str: ...
    @staticmethod
    def GetAssemblyAttribute(assembly: System.Reflection.Assembly) -> T: ...
    @staticmethod
    def ParseTokens(
        line: str, delimiter: str
    ) -> System.Collections.Generic.List[str]: ...
    @staticmethod
    def WriteColumnHeadersToCsv(
        grid: System.Windows.Forms.DataGridView,
        writer: System.IO.TextWriter,
        delimiter: str,
    ) -> None: ...
    @staticmethod
    def WriteCsv(
        grid: System.Windows.Forms.DataGridView,
        writer: System.IO.TextWriter,
        delimiter: str,
    ) -> None: ...
    @staticmethod
    def GetDirectoryName(path: str) -> str: ...
    @staticmethod
    def EnumArrayToString(values: List[T], separator: str) -> str: ...
    @staticmethod
    def FindKnownExceptions(
        ex: System.Exception, knownTypes: List[System.Type]
    ) -> List[System.Exception]: ...
    @staticmethod
    def WriteCsvToken(
        token: str, delimiter: str, writer: System.IO.TextWriter
    ) -> None: ...
    @staticmethod
    def CultureIsKindOf(
        ci: System.Globalization.CultureInfo, cultureName: str
    ) -> bool: ...
    @staticmethod
    def StringToEnumArray(value_: str, separator: str) -> List[T]: ...
    @staticmethod
    def CopyFolder(source: str, destination: str) -> None: ...
    @staticmethod
    def GetCsvEncoding(
        ci: System.Globalization.CultureInfo,
    ) -> System.Text.Encoding: ...
    @staticmethod
    def GetHelpFilePath(basePath: str, fileName: str) -> str: ...
    @overload
    @staticmethod
    def ShowMessage(
        parent: System.Windows.Forms.IWin32Window,
        message: str,
        title: str,
        buttons: System.Windows.Forms.MessageBoxButtons,
        icon: System.Windows.Forms.MessageBoxIcon,
    ) -> System.Windows.Forms.DialogResult: ...
    @overload
    @staticmethod
    def ShowMessage(
        parent: System.Windows.Forms.IWin32Window,
        message: str,
        title: str,
        buttons: System.Windows.Forms.MessageBoxButtons,
        icon: System.Windows.Forms.MessageBoxIcon,
        helpFilePath: str,
        helpId: int,
    ) -> System.Windows.Forms.DialogResult: ...
    @staticmethod
    def CreatePen(
        color: System.Drawing.Color,
        dashStyle: System.Drawing.Drawing2D.DashStyle,
        weight: float,
    ) -> System.Drawing.Pen: ...

class WaitCursor(System.IDisposable):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, ctrl: System.Windows.Forms.Control) -> None: ...
    def Dispose(self) -> None: ...

class WaitCursorWPF(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def Dispose(self) -> None: ...

class Win32Window(System.Windows.Forms.IWin32Window):  # Class
    @overload
    def __init__(self, window: System.Windows.Window) -> None: ...
    @overload
    def __init__(self, handle: System.IntPtr) -> None: ...

    Handle: System.IntPtr  # readonly

    @staticmethod
    def GetParentHandle(parent: System.Windows.Forms.IWin32Window) -> System.IntPtr: ...
