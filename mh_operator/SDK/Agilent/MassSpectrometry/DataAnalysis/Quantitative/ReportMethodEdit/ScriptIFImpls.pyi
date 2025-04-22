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

from .AppCommand import ApplicationType
from .ScriptIF import IEditView, IMainForm, ITemplatesView, IUIState
from .UI import UIContext, ViewMode
from .Utils import IImportCompounds

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.ScriptIFImpls

class MainForm(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.ScriptIFImpls.ScriptIFImplsBase,
    IMainForm,
    System.Windows.Forms.IWin32Window,
):  # Class
    CurrentView: IEditView  # readonly
    Handle: System.IntPtr  # readonly
    IsInEditMode: bool  # readonly
    TemplatesView: ITemplatesView  # readonly
    ViewMode: ViewMode

class ScriptIFImplsBase(System.MarshalByRefObject):  # Class
    ...

class TemplatesView(
    ITemplatesView,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.ScriptIFImpls.ScriptIFImplsBase,
    IEditView,
):  # Class
    CanCopy: bool  # readonly
    CanCut: bool  # readonly
    CanDelete: bool  # readonly
    CanPaste: bool  # readonly
    CanRedo: Optional[bool]  # readonly
    CanUndo: Optional[bool]  # readonly

    def Redo(self) -> None: ...
    def Undo(self) -> None: ...
    def Copy(self) -> None: ...
    def RemoveTemplates(self) -> None: ...
    def CanRemoveTemplates(self) -> bool: ...
    def Cut(self) -> None: ...
    def Paste(self) -> None: ...
    def Delete(self) -> None: ...

class UIState(
    IUIState,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.ScriptIFImpls.ScriptIFImplsBase,
):  # Class
    ApplicationType: ApplicationType  # readonly
    CanRedo: bool  # readonly
    CanUndo: bool  # readonly
    ImportCompounds: IImportCompounds  # readonly
    IsDirty: bool  # readonly
    MainForm: IMainForm  # readonly
    PathName: str  # readonly
    _UIContext: UIContext  # readonly

    def ExecuteCommand(self, name: str, parameters: List[Any]) -> Any: ...
    def Redo(self) -> None: ...
    def Undo(self) -> None: ...
    def ExitApplication(self, forceExit: bool) -> None: ...
