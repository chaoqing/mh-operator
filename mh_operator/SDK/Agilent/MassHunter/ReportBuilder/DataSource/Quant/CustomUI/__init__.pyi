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

from . import GraphicsControls, InsertList, InsertTable

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI

class CustomUI(Agilent.MassHunter.ReportBuilder.DataSource.ICustomUI):  # Class
    def __init__(
        self,
        dataSourceDesigner: Agilent.MassHunter.ReportBuilder.DataSource.IDataSourceDesigner,
    ) -> None: ...
    def CanExecuteSystemCommand(
        self,
        app: Agilent.MassHunter.ReportBuilder.Application.IApplication,
        cmdid: str,
        parameter: Any,
        canExecute: bool,
    ) -> bool: ...
    def ExecuteSystemCommand(
        self,
        app: Agilent.MassHunter.ReportBuilder.Application.IApplication,
        cmdid: str,
        parameter: Any,
    ) -> bool: ...
    def GetCustomCommandGroups(
        self, application: Agilent.MassHunter.ReportBuilder.Application.IApplication
    ) -> List[Agilent.MassHunter.ReportBuilder.DataSource.ICustomCommandGroup]: ...

class IWizardViewModel(object):  # Interface
    def ButtonPushed(
        self,
        button: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.WizardButton,
    ) -> None: ...
    def ButtonEnabled(
        self,
        button: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.WizardButton,
    ) -> bool: ...

    ButtonChanged: System.EventHandler  # Event

class NotifyPropertyChangedBase(System.ComponentModel.INotifyPropertyChanged):  # Class
    def VerifyPropertyName(self, propertyName: str) -> None: ...

    PropertyChanged: System.ComponentModel.PropertyChangedEventHandler  # Event

class RelayCommand(System.Windows.Input.ICommand):  # Class
    @overload
    def __init__(self, execute: System.Action) -> None: ...
    @overload
    def __init__(
        self, execute: System.Action, canExecute: System.Predicate
    ) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def RaiseCanExecuteChanged(self) -> None: ...
    def Execute(self, parameter: Any) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class Utils:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def GetUniqueBindingName(
        container: Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer,
        name: str,
    ) -> str: ...
    @staticmethod
    def FindBindingName(
        container: Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer,
        name: str,
    ) -> Agilent.MassHunter.ReportBuilder.DataModel.IDataBindingContainer: ...
    @staticmethod
    def FindParentBindingContainer(
        container: Agilent.MassHunter.ReportBuilder.DataModel.ISelectableContainer,
        dataName: str,
        binding: Agilent.MassHunter.ReportBuilder.DataModel.IDataBinding,
    ) -> Agilent.MassHunter.ReportBuilder.DataModel.IDataBindingContainer: ...

class WizardButton(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Back: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.WizardButton = (
        ...
    )  # static # readonly
    Cancel: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.WizardButton = (
        ...
    )  # static # readonly
    Finish: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.WizardButton = (
        ...
    )  # static # readonly
    Next: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.WizardButton = (
        ...
    )  # static # readonly

class WizardResult(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Canceled: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.WizardResult
    ) = ...  # static # readonly
    Finished: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.WizardResult
    ) = ...  # static # readonly
