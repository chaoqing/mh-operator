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

from . import MainWindow
from .Models import IAppCommandContext, IDynamicCalibrationSetupModel

# Stubs for namespace: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.ScriptIF

class IMainWindow(object):  # Interface
    _Window: System.Windows.Window  # readonly

    def Close(self) -> None: ...

class IUIState(object):  # Interface
    CommandContext: IAppCommandContext  # readonly
    DynamicCalibrationSetupModel: IDynamicCalibrationSetupModel  # readonly
    MainWindow: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.ScriptIF.IMainWindow
    )  # readonly

class MainWindow(
    Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.ScriptIF.IMainWindow
):  # Class
    def __init__(self, window: MainWindow) -> None: ...

    _Window: System.Windows.Window  # readonly

    def Close(self) -> None: ...

class UIState(
    Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.ScriptIF.IUIState
):  # Class
    def __init__(
        self, mainWindow: MainWindow, model: IDynamicCalibrationSetupModel
    ) -> None: ...

    CommandContext: IAppCommandContext  # readonly
    DynamicCalibrationSetupModel: IDynamicCalibrationSetupModel  # readonly
    MainWindow: (
        Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.ScriptIF.IMainWindow
    )  # readonly
