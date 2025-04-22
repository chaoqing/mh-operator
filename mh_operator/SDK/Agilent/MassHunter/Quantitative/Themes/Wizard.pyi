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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Themes.Wizard

class IWizardContentViewModel(object):  # Interface
    BackButtonCommand: System.Windows.Input.ICommand  # readonly
    BackButtonContent: str  # readonly
    BackButtonVisibility: System.Windows.Visibility  # readonly
    CancelButtonCommand: System.Windows.Input.ICommand  # readonly
    CancelButtonContent: str  # readonly
    CancelButtonVisibility: System.Windows.Visibility  # readonly
    Content: Any  # readonly
    FinishButtonCommand: System.Windows.Input.ICommand  # readonly
    FinishButtonContent: str  # readonly
    FinishButtonVisibility: System.Windows.Visibility  # readonly
    IsEnabled: bool  # readonly
    Label: str  # readonly
    NextButtonCommand: System.Windows.Input.ICommand  # readonly
    NextButtonContent: str  # readonly
    NextButtonVisibility: System.Windows.Visibility  # readonly
    Title: str  # readonly

class IWizardWindowModel(object):  # Interface
    CurrentViewModel: Any
    NavigationSubTitle: str  # readonly
    NavigationTitle: str  # readonly
    ViewModels: List[Any]  # readonly
    WindowTitle: str  # readonly
