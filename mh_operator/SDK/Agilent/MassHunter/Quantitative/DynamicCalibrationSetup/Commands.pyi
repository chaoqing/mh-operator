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

# Stubs for namespace: Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Commands

class AddCalibrationRange(
    System.IDisposable,
    Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Commands.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: IAppCommandContext,
        targetCompoundID: int,
        targetIonGroupID: int,
        minConcentration: Optional[float],
        maxConcentration: Optional[float],
    ) -> None: ...
    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class AddQualifierToCalibrationRange(
    System.IDisposable,
    Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Commands.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: IAppCommandContext,
        targetCompoundID: int,
        calibrationRangeID: int,
        ionGroupID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class AppCommandBase(
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.CommandModel.CommandBase,
):  # Class
    AppCommandContext: IAppCommandContext  # readonly
    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class AppCommandContext(
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.CommandHistory,
    Agilent.MassSpectrometry.CommandModel.Model.ICommandHistory,
    IAppCommandContext,
):  # Class
    def __init__(self) -> None: ...

    BatchGlobalFeatureAnalysis: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.BatchGlobalFeatureAnalysis
    )  # readonly
    IsBatchOpen: bool  # readonly
    MethodDataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.MethodDataSet
    )  # readonly
    QuantAppCommandContext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.AppCommandContext
    )  # readonly

    def RemoveCalibrationRange(
        self, targetCompoundID: int, calibrationRangeID: int
    ) -> None: ...
    def CloseBatch(self) -> None: ...
    def NewCalibrationRange(self, targetCompoundID: int) -> ICalibrationRange: ...
    def SaveMethod(self, pathName: str) -> None: ...
    def Analyze(self) -> None: ...
    def AddCalibrationRange(self, range: ICalibrationRange) -> None: ...
    def OpenBatch(self, batchFolder: str, batchFile: str, analyze: bool) -> None: ...
    @staticmethod
    def CalcAverageResponseRatio(
        target: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ICrossSampleIonGroup,
        qualifier: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ICrossSampleIonGroup,
    ) -> float: ...
    def GetCalibrationRanges(
        self, targetCompoundID: int
    ) -> List[ICalibrationRange]: ...
    @staticmethod
    def CalcAverateMZ(
        ionGroup: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DynamicQuant.ICrossSampleIonGroup,
    ) -> float: ...
    def GetCalibrationRange(
        self, targetCompoundID: int, calibrationRangeID: int
    ) -> ICalibrationRange: ...

    Analyzed: System.EventHandler  # Event
    Analyzing: System.EventHandler  # Event
    BatchClosed: System.EventHandler  # Event
    BatchOpened: System.EventHandler  # Event
    CalibrationRangesChanged: System.EventHandler  # Event
    Progress: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ProgressEventArgs
    ]  # Event

class CloseBatch(
    System.IDisposable,
    Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Commands.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: IAppCommandContext) -> None: ...
    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class OpenBatch(
    System.IDisposable,
    Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Commands.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: IAppCommandContext,
        batchFolder: str,
        batchFile: str,
        analyze: bool,
    ) -> None: ...
    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...

class SaveMethod(
    System.IDisposable,
    Agilent.MassHunter.Quantitative.DynamicCalibrationSetup.Commands.AppCommandBase,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(self, context: IAppCommandContext, methodPath: str) -> None: ...
    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
