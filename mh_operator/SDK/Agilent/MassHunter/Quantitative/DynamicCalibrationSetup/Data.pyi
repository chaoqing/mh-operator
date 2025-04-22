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

from .Models import IAppCommandContext, ICalibrationRange

# Stubs for namespace: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Data

class CalibrationRange(ICalibrationRange):  # Class
    def __init__(self, targetCompoundID: int, calibrationRangeID: int) -> None: ...

    CalibrationRangeID: int  # readonly
    MaxConcentration: Optional[float]
    MinConcentration: Optional[float]
    QualifierIonGroupIDs: List[int]
    TargetCompoundID: int  # readonly
    TargetIonGroupID: Optional[int]

    def AddQualifierIonGroupID(self, id: int) -> None: ...
    def RemoveQualifierIonGroupID(self, id: int) -> None: ...

class DataCmdAddQualifierToCalibrationRange(
    Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Data.DataCmdBase
):  # Class
    def __init__(
        self,
        context: IAppCommandContext,
        targetCompoundID: int,
        calibrationRangeID: int,
        ionGroupID: int,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class DataCmdBase:  # Class
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class DataCmdNewCalibrationRange(
    Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Data.DataCmdBase
):  # Class
    def __init__(self, context: IAppCommandContext, targetCompoundID: int) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class DataCmdSetCalibrationRangeProperty(
    Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Data.DataCmdBase
):  # Class
    def __init__(self, target: Any, name: str, value_: Any) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
