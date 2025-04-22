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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand

class DataCommandBase(System.IDisposable):  # Class
    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Dispose(self) -> None: ...
    def Undo(self) -> Any: ...

class DeleteCompoundGraphicsRange(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        ds: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        compoundGraphicsID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class DeleteFormatting(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        ds: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        formattingID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class DeletePrePostProcess(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        ds: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        prePostProcessID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewCalibrationGraphics(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewCompoundGraphicsRange(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        ds: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        compoundGraphicsID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewFormatting(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        formattingID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewGraphicsRange(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewPeakChromatogramGraphics(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewPeakQualifiersGraphics(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewPeakSpectrumGraphics(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewPrePostProcess(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        prePostProcessID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewSampleChromatogramGraphics(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewUnknownsIonPeakGraphicsProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewUnknownsSampleChromatogramGraphics(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class NewUnknownsSpectrumGraphicsProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Undo(self) -> Any: ...

class SetCalibrationGraphicsProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetCompoundGraphicsRangeProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        compoundGraphicsID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetFormattingProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        formattingID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetGraphicsRangeProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetPeakChromatogramGraphicsProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetPeakQualifiersGraphicsProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetPeakSpectrumGraphicsProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetPrePostProcessProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        prePostProcessID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetPropertyBase(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class SetReportProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        name: str,
        value_: Any,
    ) -> None: ...
    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...

class SetSampleChromatogramGraphicsProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetUnknownsIonPeakGraphicsProperties(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetUnknownsSampleChromatogramGraphicsProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        name: str,
        value_: Any,
    ) -> None: ...

class SetUnknownsSpectrumGraphicsProperty(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethodEdit.DataCommand.SetPropertyBase,
):  # Class
    def __init__(
        self,
        dataset: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportMethod.ReportMethodDataSet,
        reportID: int,
        name: str,
        value_: Any,
    ) -> None: ...
