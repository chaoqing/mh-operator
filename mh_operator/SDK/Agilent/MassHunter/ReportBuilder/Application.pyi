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

from .DataModel import (
    IGraphicsParameter,
    IList,
    IReport,
    ISelectable,
    ISelectableContainer,
    ITable,
)
from .Template import IList, ITable

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.Application

class IAppCommand(object):  # Interface
    def Execute(self) -> Any: ...

class IApplication(object):  # Interface
    MainWindow: System.Windows.Window  # readonly
    Report: IReport  # readonly
    Selected: ISelectable  # readonly

    def CreateInsertSelectableCommand(
        self,
    ) -> Agilent.MassHunter.ReportBuilder.Application.IInsertSelectableCommand: ...
    def CreateSetGraphicsParametersCommand(
        self,
    ) -> Agilent.MassHunter.ReportBuilder.Application.ISetGraphicsParametersCommand: ...
    def ExecuteCommand(
        self,
        command: Agilent.MassHunter.ReportBuilder.Application.IAppCommand,
        ret: Any,
    ) -> bool: ...
    def CanInsert(
        self,
        canInsert: System.Func[ISelectableContainer, bool],
        container: ISelectableContainer,
        index: int,
    ) -> bool: ...

class IInsertSelectableCommand(
    Agilent.MassHunter.ReportBuilder.Application.IAppCommand
):  # Interface
    def InsertTable(
        self, container: ISelectableContainer, index: int, table: ITable
    ) -> ITable: ...
    def InsertList(
        self, container: ISelectableContainer, index: int, list: IList
    ) -> IList: ...
    def InsertGraphics(
        self,
        container: ISelectableContainer,
        index: int,
        name: str,
        parameterNames: List[str],
    ) -> None: ...

class ISetGraphicsParametersCommand(
    Agilent.MassHunter.ReportBuilder.Application.IAppCommand
):  # Interface
    def SetParameter(self, parameter: IGraphicsParameter, value_: Any) -> None: ...

class SystemCommands:  # Class
    Alignment_Bottom: str = ...  # static # readonly
    Alignment_HCenter: str = ...  # static # readonly
    Alignment_Left: str = ...  # static # readonly
    Alignment_Right: str = ...  # static # readonly
    Alignment_Top: str = ...  # static # readonly
    Alignment_VCenter: str = ...  # static # readonly
    Edit_DataBindings: str = ...  # static # readonly
    Edit_Delete: str = ...  # static # readonly
    Edit_MoveDown: str = ...  # static # readonly
    Edit_MoveUp: str = ...  # static # readonly
    Edit_Redo: str = ...  # static # readonly
    Edit_TableColumns: str = ...  # static # readonly
    Edit_Undo: str = ...  # static # readonly
    File_Exit: str = ...  # static # readonly
    File_New: str = ...  # static # readonly
    File_Open: str = ...  # static # readonly
    File_Save: str = ...  # static # readonly
    File_SaveAs: str = ...  # static # readonly
    Font_Bold: str = ...  # static # readonly
    Font_Italic: str = ...  # static # readonly
    Font_Underline: str = ...  # static # readonly
    Help_About: str = ...  # static # readonly
    Help_Help: str = ...  # static # readonly
    Insert_Graphics: str = ...  # static # readonly
    Insert_Image: str = ...  # static # readonly
    Insert_List: str = ...  # static # readonly
    Insert_Page: str = ...  # static # readonly
    Insert_ScriptBox: str = ...  # static # readonly
    Insert_Table: str = ...  # static # readonly
    Insert_TableRow: str = ...  # static # readonly
    Insert_Textbox: str = ...  # static # readonly
    Preview_Preview: str = ...  # static # readonly
    Preview_Setup: str = ...  # static # readonly
