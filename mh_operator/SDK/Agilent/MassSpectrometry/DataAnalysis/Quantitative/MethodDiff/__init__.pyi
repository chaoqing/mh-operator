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

from . import Properties
from .Compliance import ICompliance, ILogonParameters
from .UIUtils2 import ConfigurationElementSectionBase

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff

class App(
    System.Windows.Application,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def Main() -> None: ...

class AppConfig:  # Class
    ApplicationSettings: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.ApplicationSettings
    )  # readonly
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.AppConfig
    )  # static # readonly
    UserSettings: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.UserSettings
    )  # readonly

    def Save(self) -> None: ...

class ApplicationSettings(ConfigurationElementSectionBase):  # Class
    def __init__(self) -> None: ...

    DumpLogOnNormalExit: bool  # readonly
    ErrorReportingEmailAddress: str  # readonly
    ErrorReportingEnabled: bool  # readonly

class CmdLine(ILogonParameters):  # Class
    def __init__(self) -> None: ...

    AccountName: str
    CompareMode: bool
    ConnectionTicket: str
    Culture: str
    Domain: str
    EncryptedPassword: str
    Help: bool
    HistoryMode: bool
    Methods: List[str]
    Password: str
    Server: str
    User: str
    _Password: System.Security.SecureString  # readonly

class DiffInfo:  # Class
    def __init__(self) -> None: ...

    Column: str
    Description: str
    DiffType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.DiffType
    Table: str
    Value1: Any
    Value2: Any

class DiffType(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Deleted: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.DiffType = (
        ...
    )  # static # readonly
    Inserted: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.DiffType = (
        ...
    )  # static # readonly
    Modified: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.DiffType = (
        ...
    )  # static # readonly

class DiffWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class DiffWindowModel:  # Class
    def __init__(self) -> None: ...

    Differences: Iterable[Any]
    Pathname1: str
    Pathname2: str

class DirDiffInfo:  # Class
    def __init__(
        self,
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodItemType,
    ) -> None: ...

    CanShowDetails: bool  # readonly
    Differences: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.DiffInfo
    ]
    Different: bool  # readonly
    DisplayName: str
    File1Exists: bool
    File2Exists: bool
    RelativePath: str
    Type: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodItemType
    )  # readonly

class MainWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...
    def OpenMethods(self, method1: str, method2: str) -> None: ...

class MethodHistoryItem(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(
        self,
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodItemType,
    ) -> None: ...

    DisplayName: str
    RelativePath: str
    RevisionDifferences: System.Collections.ObjectModel.ObservableCollection[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodHistoryItemRevision
    ]  # readonly
    Type: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodItemType
    )  # readonly

class MethodHistoryItemRevision:  # Class
    def __init__(self) -> None: ...

    CanShowDetails: bool  # readonly
    Date: Optional[System.DateTime]
    Differences: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.DiffInfo
    ]
    File1Exists: bool
    File2Exists: bool
    Identical: bool  # readonly
    Reason: str
    Revision1: str
    Revision2: str
    User: str

class MethodHistoryModel(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self) -> None: ...

    CommandBrowse: System.Windows.Input.ICommand  # readonly
    CommandGenerateHistory: System.Windows.Input.ICommand  # readonly
    CommandReport: System.Windows.Input.ICommand  # readonly
    Compliance: ICompliance
    Items: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodHistoryItem
    ]  # readonly
    MethodPath: str
    Progress: float  # readonly
    ProgressMessage: str
    Revisions: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodHistoryRevision
    ]  # readonly
    ShowDetailsCommand: System.Windows.Input.ICommand  # readonly
    Window: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodHistoryWindow
    )

    def GenerateHistory(self) -> None: ...

class MethodHistoryRevision:  # Class
    def __init__(self) -> None: ...

    Date: Optional[System.DateTime]
    Reason: str
    RevisionNumber: str
    User: str
    _Date: str  # readonly

class MethodHistoryWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def OpenMethod(self, method: str) -> None: ...
    def InitializeComponent(self) -> None: ...

class MethodItemType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Quant: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodItemType
    ) = ...  # static # readonly
    QuantReport: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodItemType
    ) = ...  # static # readonly
    Unknowns: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodItemType
    ) = ...  # static # readonly
    UnknownsReport: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodItemType
    ) = ...  # static # readonly

class Model(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
):  # Class
    def __init__(self) -> None: ...

    BrowseCommand: System.Windows.Input.ICommand  # readonly
    CloseCommand: System.Windows.Input.ICommand  # readonly
    CompareCommand: System.Windows.Input.ICommand  # readonly
    Compliance: ICompliance
    DirectoryDifferences: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.DirDiffInfo
    ]  # readonly
    GridVisibility: System.Windows.Visibility  # readonly
    Pathname1: str
    Pathname2: str
    Revision1: str
    Revision2: str
    RevisionVisibility: System.Windows.Visibility  # readonly
    ShowDetailsCommand: System.Windows.Input.ICommand  # readonly
    Window: Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MainWindow

    def Compare(self) -> None: ...
    @staticmethod
    def _CompareFiles(
        path1: str, path2: str
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.DiffInfo
    ]: ...

class NotifyPropertyBase(System.ComponentModel.INotifyPropertyChanged):  # Class
    def VerifyPropertyName(self, propertyName: str) -> None: ...

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class ProgressWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class RelayCommand(System.Windows.Input.ICommand):  # Class
    @overload
    def __init__(self, execute: System.Action) -> None: ...
    @overload
    def __init__(
        self, execute: System.Action, canExecute: System.Predicate
    ) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Execute(self, parameter: Any) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class Report(iTextSharp.text.pdf.IPdfPageEvent):  # Class
    def __init__(
        self, compliance: ICompliance, methodPath: str, stream: System.IO.Stream
    ) -> None: ...
    @staticmethod
    def RegisterFont(name: str) -> None: ...
    def OnEndPage(
        self, writer: iTextSharp.text.pdf.PdfWriter, document: iTextSharp.text.Document
    ) -> None: ...
    def OnGenericTag(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        rect: iTextSharp.text.Rectangle,
        text: str,
    ) -> None: ...
    def OnOpenDocument(
        self, writer: iTextSharp.text.pdf.PdfWriter, document: iTextSharp.text.Document
    ) -> None: ...
    def OnParagraph(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
    ) -> None: ...
    def OnSection(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
        depth: int,
        title: iTextSharp.text.Paragraph,
    ) -> None: ...
    @staticmethod
    def GetFont(name: str) -> iTextSharp.text.Font: ...
    def OnChapterEnd(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
    ) -> None: ...
    def OnStartPage(
        self, writer: iTextSharp.text.pdf.PdfWriter, document: iTextSharp.text.Document
    ) -> None: ...
    def OnChapter(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
        title: iTextSharp.text.Paragraph,
    ) -> None: ...
    def OnCloseDocument(
        self, writer: iTextSharp.text.pdf.PdfWriter, document: iTextSharp.text.Document
    ) -> None: ...
    @staticmethod
    def GetDefaultFontNameByCulture(ci: System.Globalization.CultureInfo) -> str: ...
    def OnParagraphEnd(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
    ) -> None: ...
    def OnSectionEnd(
        self,
        writer: iTextSharp.text.pdf.PdfWriter,
        document: iTextSharp.text.Document,
        paragraphPosition: float,
    ) -> None: ...
    def Generate(
        self,
        revisions: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodHistoryRevision
        ],
        items: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDiff.MethodHistoryItem
        ],
    ) -> None: ...

class SelectAllCommand(System.Windows.Input.ICommand):  # Class
    def __init__(self) -> None: ...
    def IterateRecords(
        self, records: Infragistics.Windows.DataPresenter.RecordCollectionBase
    ) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Execute(self, parameter: Any) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class UserSettings(ConfigurationElementSectionBase):  # Class
    def __init__(self) -> None: ...

    LastMethodFolder: str
