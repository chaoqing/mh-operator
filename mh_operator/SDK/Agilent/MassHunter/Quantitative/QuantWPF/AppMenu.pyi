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

# Stubs for namespace: Agilent.MassHunter.Quantitative.QuantWPF.AppMenu

class ExportGraphicsView(
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

class ExportGraphicsViewModel:  # Class
    def __init__(self) -> None: ...

class ExportTableFileTypeItem:  # Class
    def __init__(self) -> None: ...

    Description: str
    Extension: str
    Image: System.Windows.Media.Imaging.BitmapSource  # readonly
    Label: str  # readonly
    Name: str

class ExportTableView(
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

class ExportTableViewModel:  # Class
    def __init__(
        self, model: Agilent.MassHunter.Quantitative.QuantWPF.AppMenu.ExportViewModel
    ) -> None: ...

    ExportCommand: System.Windows.Input.ICommand  # readonly
    ExportEntireTable: bool
    ExportSelectedRows: bool
    FileTypes: List[
        Agilent.MassHunter.Quantitative.QuantWPF.AppMenu.ExportTableFileTypeItem
    ]  # readonly
    OpenExportedFile: bool
    SelectedFileType: (
        Agilent.MassHunter.Quantitative.QuantWPF.AppMenu.ExportTableFileTypeItem
    )

class ExportView(
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

class ExportViewModel(System.Windows.DependencyObject):  # Class
    def __init__(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...

    CurrentViewModelProperty: System.Windows.DependencyProperty  # static # readonly
    ItemsProperty: System.Windows.DependencyProperty  # static # readonly

    CurrentViewModel: Any
    Items: List[Agilent.MassHunter.Quantitative.QuantWPF.AppMenu.ExportViewModel.Item]
    SelectedPaneID: str

    def GetView(
        self,
    ) -> Agilent.MassHunter.Quantitative.QuantWPF.AppMenu.ExportView: ...
    def InitItems(self) -> None: ...

    # Nested Types

    class Item:  # Class
        def __init__(self, paneId: str, label: str) -> None: ...

        Label: str
        PaneID: str

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
        viewModel: Agilent.MassHunter.Quantitative.Controls.OpenBatch.OpenBatchViewModel,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...
    def InitializeComponent(self) -> None: ...
