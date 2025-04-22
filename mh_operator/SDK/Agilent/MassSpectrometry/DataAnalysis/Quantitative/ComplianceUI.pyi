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

from .Compliance import ComplianceConfiguration, ICompliance

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI

class FileAndFolderFilter:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        name: str,
        items: List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileAndFolderFilterItem
        ],
    ) -> None: ...

    FilterItems: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileAndFolderFilterItem
    ]
    Name: str

class FileAndFolderFilterItem:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, isFolder: bool, extensions: List[str]) -> None: ...

    Extensions: List[str]
    IsFolder: bool

class FileDialogMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    New: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    ) = ...  # static # readonly
    Open: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    ) = ...  # static # readonly
    SaveAs: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    ) = ...  # static # readonly

class IBatchDialog(System.IDisposable):  # Interface
    AllowFileRevisions: bool
    AuditTrail: bool
    BatchFile: str  # readonly
    BatchFolder: str  # readonly
    FileDialogMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    )  # readonly
    InitialFolder: str
    ReadOnly: bool  # readonly
    RevisionNumber: str  # readonly
    Title: str

    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class IComplianceConfigurationEdit(System.IDisposable):  # Interface
    CanEditRoles: bool  # readonly

    def Save(self, config: ComplianceConfiguration) -> None: ...
    def Load(self) -> ComplianceConfiguration: ...
    def ResetToDefault(self) -> ComplianceConfiguration: ...
    def PreprocessNewRoleName(self, roleName: str) -> str: ...
    def GetAvailableRoles(self) -> List[str]: ...
    def Run(self, args: List[str]) -> None: ...

class IComplianceUI(object):  # Interface
    Compliance: ICompliance  # readonly

    def CreateComplianceConfigurationEdit(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IComplianceConfigurationEdit
    ): ...
    def CreateFileAndFolderDialog(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IFileAndFolderDialog
    ): ...
    def CreateLibraryDialog(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.ILibraryDialog
    ): ...
    def CreateSampleFileDialog(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.ISampleFileDialog
    ): ...
    def CreateMethodDialog(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IMethodDialog
    ): ...
    def CreateUnknownsFileDialog(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IUnknownsFileDialog
    ): ...
    def CreateFileDialog(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IFileDialog
    ): ...
    def CreateLogonDialog(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.ILogonDialog
    ): ...
    def CreateFolderDialog(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IFolderDialog
    ): ...
    def CreateBatchDialog(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IBatchDialog
    ): ...

class IFileAndFolderDialog(System.IDisposable):  # Interface
    Filters: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileAndFolderFilter
    ]
    InitialFolder: str
    Mode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    )  # readonly
    PathName: str  # readonly
    Title: str

    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class IFileDialog(System.IDisposable):  # Interface
    DefaultExtension: str
    DefaultFileName: str
    FileMustExists: bool
    Filters: str
    InitialFolder: str
    Mode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    )  # readonly
    MultiSelect: bool
    OverwritePrompt: bool
    PathName: str  # readonly
    PathNames: List[str]  # readonly
    Title: str

    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class IFolderDialog(System.IDisposable):  # Interface
    InitialFolder: str
    PathName: str  # readonly
    Title: str

    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class ILibraryDialog(System.IDisposable):  # Interface
    AllowFileRevisions: bool
    AllowNistLibraries: bool
    ExtraFileFilter: str
    InitialFolder: str
    Mode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    )  # readonly
    PathName: str  # readonly
    RevisionNumber: str  # readonly
    Title: str

    def AllowReferenceLibrary(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class ILogonDialog(System.IDisposable):  # Interface
    Compliance: ICompliance  # readonly
    Domain: str
    Handle: System.IntPtr  # readonly
    LogonXml: str  # readonly
    Message: str
    Password: System.Security.SecureString  # readonly
    Server: str
    User: str
    ValidationMode: bool

    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

    Cancel: System.ComponentModel.CancelEventHandler  # Event
    Logon: System.ComponentModel.CancelEventHandler  # Event

class IMethodDialog(System.IDisposable):  # Interface
    AllowFileRevisions: bool
    FileDialogMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    )  # readonly
    FileMustNotExist: bool
    IndividualFileExtensions: List[str]
    InitialFolder: str
    PathName: str  # readonly
    RevisionNumber: str  # readonly
    Title: str

    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

    SaveAsFolder: System.ComponentModel.CancelEventHandler  # Event

class ISampleFileDialog(System.IDisposable):  # Interface
    InitialFolder: str
    MultiSelect: bool
    PathName: str  # readonly
    PathNames: List[str]  # readonly
    Title: str

    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class IUnknownsFileDialog(System.IDisposable):  # Interface
    AllowFileRevisions: bool
    AnalysisFile: str  # readonly
    AuditTrail: bool
    BatchFolder: str  # readonly
    FileDialogMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    )  # readonly
    InitialFolder: str
    ReadOnly: bool  # readonly
    RevisionNumber: str  # readonly
    Title: str

    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...
