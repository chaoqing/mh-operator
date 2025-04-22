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

from .Tools import ITool, ITools, IToolString

# Stubs for namespace: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model

class AvailableToolCategory(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.IAvailableToolCategory
):  # Class
    def __init__(
        self,
        id: str,
        displayName: str,
        tools: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase],
        toolString: IToolString,
    ) -> None: ...

    DisplayName: str  # readonly
    Name: str  # readonly
    Tools: List[ITool]  # readonly

class CustomizeRibbonModel(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.ICustomizeRibbonModel
):  # Class
    def __init__(self) -> None: ...

    CustomizeWindowTargets: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.ICustomizeWindowTarget
    ]  # readonly

    def Save(self, rootFolder: str) -> None: ...
    def ResetToDefault(self) -> None: ...
    def Initialize(self, rootFolder: str) -> None: ...
    def IsDirty(self) -> bool: ...
    @staticmethod
    def CreateTool(
        parent: ITools,
        tool: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase,
        toolString: IToolString,
    ) -> ITool: ...
    @staticmethod
    def CreateTools(
        parent: ITools,
        tools: List[Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase],
        toolString: IToolString,
    ) -> List[ITool]: ...

class CustomizeRibbonTarget(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.ICustomizeRibbonTarget,
    ITools,
):  # Class
    def __init__(self, name: str, toolString: IToolString) -> None: ...

    Children: List[ITool]  # readonly
    DisplayName: str  # readonly
    Name: str  # readonly
    RootTools: ITools  # readonly
    TargetType: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.RibbonTargetType
    )  # readonly

    def MoveDown(self, child: ITool) -> None: ...
    def InitializeRibbon(
        self, ribbon: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Ribbon
    ) -> None: ...
    def MoveUp(self, child: ITool) -> None: ...
    def CanMoveDown(self, tool: ITool) -> bool: ...
    def CanInsert(self, child: ITool) -> bool: ...
    def Remove(self, child: ITool) -> None: ...
    def Commit(self) -> List[Any]: ...
    def Insert(self, child: ITool, after: ITool) -> None: ...
    def CanMoveUp(self, tool: ITool) -> bool: ...

class CustomizeWindowTarget(
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.ICustomizeWindowTarget,
    IToolString,
):  # Class
    def __init__(self, fileName: str, name: str, displayName: str) -> None: ...

    AvailableToolCategories: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.IAvailableToolCategory
    ]  # readonly
    CustomizeRibbonTargets: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.ICustomizeRibbonTarget
    ]  # readonly
    DisplayName: str  # readonly
    FileName: str  # readonly
    Name: str  # readonly
    ToolString: IToolString  # readonly

    def ResetToDefault(self) -> None: ...
    def Initialize(
        self,
        tools: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools,
        defaultTools: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools,
        rmgrWpf: System.Resources.ResourceManager,
        rmgrLegacy: System.Resources.ResourceManager,
    ) -> None: ...
    @overload
    def GetToolbarCaption(
        self, toolbar: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolbarDef
    ) -> str: ...
    @overload
    def GetToolbarCaption(self, id: str) -> str: ...
    def GetCategoryDisplayName(self, cat: str) -> str: ...
    def IsDirty(self) -> bool: ...
    @overload
    def GetToolTooltip(
        self, tool: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
    ) -> str: ...
    @overload
    def GetToolTooltip(self, id: str) -> str: ...
    def CommitTo(
        self, tools: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.Tools
    ) -> None: ...
    def GetContextMenuDisplayName(self, id: str) -> str: ...
    def FindDefaultTool(
        self, id: str
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...
    def GetString(self, id: str, prefix: str, suffix: str) -> str: ...
    @overload
    def GetToolCaption(
        self, tool: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase
    ) -> str: ...
    @overload
    def GetToolCaption(self, id: str) -> str: ...
    def Save(self, rootFolder: str) -> None: ...

class IAvailableToolCategory(object):  # Interface
    DisplayName: str  # readonly
    Name: str  # readonly
    Tools: List[ITool]  # readonly

class ICustomizeRibbonModel(object):  # Interface
    CustomizeWindowTargets: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.ICustomizeWindowTarget
    ]  # readonly

    def ResetToDefault(self) -> None: ...
    def IsDirty(self) -> bool: ...
    def Save(self, rootFolder: str) -> None: ...

class ICustomizeRibbonTarget(object):  # Interface
    DisplayName: str  # readonly
    Name: str  # readonly
    RootTools: ITools  # readonly
    TargetType: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.RibbonTargetType
    )  # readonly

    def Commit(self) -> List[Any]: ...

class ICustomizeWindowTarget(object):  # Interface
    AvailableToolCategories: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.IAvailableToolCategory
    ]  # readonly
    CustomizeRibbonTargets: List[
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.ICustomizeRibbonTarget
    ]  # readonly
    DisplayName: str  # readonly
    Name: str  # readonly
    ToolString: IToolString  # readonly

    def FindDefaultTool(
        self, id: str
    ) -> Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolBase: ...
    def IsDirty(self) -> bool: ...
    def ResetToDefault(self) -> None: ...
    def Save(self, rootFolder: str) -> None: ...

class PaneTarget(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.NotifyPropertyBase,
    System.ComponentModel.INotifyPropertyChanged,
    Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.ICustomizeRibbonTarget,
    ITools,
):  # Class
    def __init__(self, name: str, toolString: IToolString) -> None: ...

    AvailableTools: List[ITool]  # readonly
    Children: List[ITool]  # readonly
    DisplayName: str  # readonly
    Name: str  # readonly
    RootTools: ITools  # readonly
    TargetType: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.RibbonTargetType
    )  # readonly

    def MoveDown(self, child: ITool) -> None: ...
    def AddToolbar(
        self, toolbar: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ToolbarDef
    ) -> None: ...
    def MoveUp(self, child: ITool) -> None: ...
    def CanMoveDown(self, child: ITool) -> bool: ...
    def CanInsert(self, child: ITool) -> bool: ...
    def Remove(self, child: ITool) -> None: ...
    def Commit(self) -> List[Any]: ...
    def Insert(self, child: ITool, after: ITool) -> None: ...
    def CanMoveUp(self, child: ITool) -> bool: ...
    def AddContextMenu(
        self,
        contextMenu: Agilent.MassHunter.Quantitative.ToolbarWPF.Definitions.ContextMenu,
    ) -> None: ...

class RibbonTargetType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Pane: Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.RibbonTargetType = (
        ...
    )  # static # readonly
    Ribbon: (
        Agilent.MassHunter.Quantitative.Startup.Edit.Ribbon.Model.RibbonTargetType
    ) = ...  # static # readonly
