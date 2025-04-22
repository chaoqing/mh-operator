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

from . import ComplianceLocal

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DataStorageLocal.UI

class BatchDialog(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IBatchDialog,
    System.IDisposable,
):  # Class
    AllowFileRevisions: bool
    AuditTrail: bool
    BatchFile: str  # readonly
    BatchFolder: str  # readonly
    CheckOut: Optional[bool]  # readonly
    Checkout: bool  # readonly
    FileDialogMode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    )  # readonly
    InitialFolder: str
    ReadOnly: bool  # readonly
    RevisionNumber: str  # readonly
    Title: str

    def Dispose(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class ComplianceConfigurationEdit(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IComplianceConfigurationEdit,
):  # Class
    def __init__(self, compliance: ComplianceLocal) -> None: ...

    AdministrativePrivilegeRequired: bool  # readonly
    CanEditRoles: bool  # readonly

    def Save(
        self,
        config: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration,
    ) -> None: ...
    def Load(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration
    ): ...
    def ResetToDefault(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration
    ): ...
    def PreprocessNewRoleName(self, roleName: str) -> str: ...
    def GetAvailableRoles(self) -> List[str]: ...
    @overload
    def Dispose(self) -> None: ...
    @overload
    def Dispose(self, disposing: bool) -> None: ...
    def Run(self, args: List[str]) -> None: ...

class FileAndFolderDialog(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IFileAndFolderDialog,
):  # Class
    Filters: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileAndFolderFilter
    ]
    InitialFolder: str
    Mode: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode
    )  # readonly
    PathName: str  # readonly
    Title: str

    def Dispose(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class FileDialog(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IFileDialog,
):  # Class
    def __init__(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode,
    ) -> None: ...

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

    def Dispose(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class FolderDialog(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IFolderDialog,
    System.IDisposable,
):  # Class
    def __init__(self) -> None: ...

    InitialFolder: str
    PathName: str  # readonly
    Title: str

    def Dispose(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class LibraryDialog(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.ILibraryDialog,
):  # Class
    def __init__(
        self,
        mode: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.FileDialogMode,
    ) -> None: ...

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
    def Dispose(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class LogonDialog(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.ILogonDialog,
):  # Class
    Compliance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance
    )  # readonly
    Domain: str
    Handle: System.IntPtr  # readonly
    LogonXml: str
    Message: str
    Password: System.Security.SecureString  # readonly
    Server: str
    User: str
    ValidationMode: bool

    def Dispose(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

    Cancel: System.ComponentModel.CancelEventHandler  # Event
    Logon: System.ComponentModel.CancelEventHandler  # Event

class MethodDialog(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IMethodDialog,
):  # Class
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

    def Dispose(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

    SaveAsFolder: System.ComponentModel.CancelEventHandler  # Event

class SampleFileDialog(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.ISampleFileDialog,
    System.IDisposable,
):  # Class
    def __init__(self) -> None: ...

    InitialFolder: str
    MultiSelect: bool
    PathName: str  # readonly
    PathNames: List[str]  # readonly
    Title: str

    def Dispose(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...

class UnknownsFileDialog(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IUnknownsFileDialog,
):  # Class
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

    def Dispose(self) -> None: ...
    def ShowDialog(
        self, parent: System.Windows.Forms.IWin32Window
    ) -> System.Windows.Forms.DialogResult: ...
