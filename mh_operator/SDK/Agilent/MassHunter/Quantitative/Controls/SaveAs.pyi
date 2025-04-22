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

from . import IApplicationMenu2010Content
from .OpenBatch import BrowseDataStorageViewModel, OpenBatchViewModel, OpenBatchViewType

# Stubs for namespace: Agilent.MassHunter.Quantitative.Controls.SaveAs

class BrowseDataStorageView(
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
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...

class BrowseDataStorageViewModel:  # Class
    def __init__(
        self, model: Agilent.MassHunter.Quantitative.Controls.SaveAs.SaveAsViewModel
    ) -> None: ...

    BatchFileProperty: System.Windows.DependencyProperty  # static # readonly

    BatchFile: str
    SaveAsViewModel: (
        Agilent.MassHunter.Quantitative.Controls.SaveAs.SaveAsViewModel
    )  # readonly
    SaveBatchAsCommand: System.Windows.Input.ICommand  # readonly

class SaveAsView(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    IApplicationMenu2010Content,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(
        self, model: Agilent.MassHunter.Quantitative.Controls.SaveAs.SaveAsViewModel
    ) -> None: ...
    def InitializeComponent(self) -> None: ...
    def SetSize(self, width: float, height: float) -> None: ...

class SaveAsViewModel(OpenBatchViewModel):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

    CurrentViewType: OpenBatchViewType

    def CheckFileExtension(self, filename: str) -> str: ...
    def DoBrowse(self, folder: str) -> None: ...

class SaveBatchAsCommand(System.Windows.Input.ICommand):  # Class
    def __init__(
        self,
        model: Agilent.MassHunter.Quantitative.Controls.SaveAs.BrowseDataStorageViewModel,
    ) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Execute(self, parameter: Any) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event
