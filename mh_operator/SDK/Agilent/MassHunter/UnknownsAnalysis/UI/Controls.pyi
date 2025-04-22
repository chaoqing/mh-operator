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

# Stubs for namespace: Agilent.MassHunter.UnknownsAnalysis.UI.Controls

class ContextMenuBridge:  # Class
    def __init__(
        self,
        toolManager: Agilent.MassHunter.Quantitative.ToolbarWPF.ToolManager.IToolManager,
        control: System.Windows.Forms.Control,
        id: str,
    ) -> None: ...

class NewAnalysisViewModel(
    Agilent.MassHunter.Quantitative.Controls.NewBatch.NewBatchViewModel
):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...
    def DoBrowse(self, folder: str) -> None: ...
    def GetDataFiles(
        self, folder: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IFileInfo
    ]: ...

class OpenAnalysisViewModel(
    Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewModel
):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...
    def DoBrowse(self, folder: str) -> None: ...
    def GetDataFiles(
        self, folder: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IFileInfo
    ]: ...

class OpenRecentViewItemContextMenu(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
):  # Class
    def __init__(
        self,
        viewModel: Agilent.MassHunter.UnknownsAnalysis.UI.Controls.OpenAnalysisViewModel,
        uiState: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.ScriptIF.IUIState,
    ) -> None: ...
    def InitializeComponent(self) -> None: ...

class SaveAnalysisAsViewModel(
    Agilent.MassHunter.Quantitative.Controls.SaveAs.SaveAsViewModel
):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...
    def CheckFileExtension(self, filename: str) -> str: ...
    def DoBrowse(self, folder: str) -> None: ...
    def GetDataFiles(
        self, folder: str
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IFileInfo
    ]: ...
