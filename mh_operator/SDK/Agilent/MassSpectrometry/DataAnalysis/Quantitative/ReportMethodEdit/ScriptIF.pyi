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
from .UI import UIContext, ViewMode
from .Utils import IImportCompounds

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.ScriptIF

class IEditView(object):  # Interface
    CanCopy: bool  # readonly
    CanCut: bool  # readonly
    CanDelete: bool  # readonly
    CanPaste: bool  # readonly
    CanRedo: Optional[bool]  # readonly
    CanUndo: Optional[bool]  # readonly

    def Redo(self) -> None: ...
    def Undo(self) -> None: ...
    def Copy(self) -> None: ...
    def Cut(self) -> None: ...
    def Paste(self) -> None: ...
    def Delete(self) -> None: ...

class IMainForm(System.Windows.Forms.IWin32Window):  # Interface
    CurrentView: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.ScriptIF.IEditView
    )  # readonly
    IsInEditMode: bool  # readonly
    TemplatesView: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.ScriptIF.ITemplatesView
    )  # readonly
    ViewMode: ViewMode

class ITemplatesView(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.ScriptIF.IEditView
):  # Interface
    def CanRemoveTemplates(self) -> bool: ...
    def RemoveTemplates(self) -> None: ...

class IUIState(object):  # Interface
    ApplicationType: ApplicationType  # readonly
    CanRedo: bool  # readonly
    CanUndo: bool  # readonly
    ImportCompounds: IImportCompounds  # readonly
    IsDirty: bool  # readonly
    MainForm: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.ScriptIF.IMainForm
    )  # readonly
    PathName: str  # readonly
    _UIContext: UIContext  # readonly

    def ExecuteCommand(self, command: str, parameters: List[Any]) -> Any: ...
    def Redo(self) -> None: ...
    def Undo(self) -> None: ...
    def ExitApplication(self, forceExit: bool) -> None: ...
