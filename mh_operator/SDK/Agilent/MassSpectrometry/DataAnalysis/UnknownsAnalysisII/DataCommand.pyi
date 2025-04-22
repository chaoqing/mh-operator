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

from .Command import KeyValue
from .DataFile import DataFileBase, TransactionBase

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand

class AddAuxiliaryMethod(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(self, dataFile: DataFileBase, batchID: int, sampleID: int) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddBatch(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(self, dataFile: DataFileBase, batchID: int) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddBlankSubtractionMethod(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        blankSubtractionMethodID: int,
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddComponent(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        values: List[KeyValue],
    ) -> None: ...

    TableName: str  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...

class AddDeconvolutionMethod(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddExactMass(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        exactMassID: int,
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddHit(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddIdentificationMethod(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddIonPeak(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
        values: List[KeyValue],
    ) -> None: ...

    TableName: str  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...

class AddLibrarySearchMethod(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddPeak(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        peakID: int,
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddPeakQualifier(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        qualifierID: int,
        peakID: int,
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddRow(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.DataCommandBase,
):  # Class
    Reversible: bool  # readonly
    TableName: str  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def SetColumn(self, name: str, value_: Any) -> None: ...
    def Redo(self, transaction: TransactionBase) -> None: ...

class AddSample(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(self, dataFile: DataFileBase, batchID: int, sampleID: int) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddTargetCompound(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self, dataFile: DataFileBase, batchID: int, sampleID: int, compoundID: int
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddTargetMatchMethod(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        targetMatchMethodID: int,
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class AddTargetQualifier(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.AddRow,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        qualifierID: int,
    ) -> None: ...

    TableName: str  # readonly

    def Undo(self, transaction: TransactionBase) -> None: ...

class DataCommandBase(System.IDisposable):  # Class
    Reversible: bool  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Redo(self, transaction: TransactionBase) -> None: ...
    def Dispose(self) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...

class RemoveLibrarySearchMethod(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Redo(self, transaction: TransactionBase) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...

class RemoveTargetCompound(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self, dataFile: DataFileBase, batchID: int, sampleID: int, compoundID: int
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Redo(self, transaction: TransactionBase) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...

class SetComponent(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Redo(self, transaction: TransactionBase) -> None: ...
    def SetValue(self, name: str, value_: Any) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...

class SetExactMass(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        exactMassID: int,
        name: str,
        value_: Any,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Redo(self, transaction: TransactionBase) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...

class SetHit(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        name: str,
        value_: Any,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Redo(self, transaction: TransactionBase) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...

class SetIonPeak(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
        name: str,
        value_: Any,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Redo(self, transaction: TransactionBase) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...

class SetSample(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self,
        dataFile: DataFileBase,
        batchID: int,
        sampleID: int,
        name: str,
        value_: Any,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Redo(self, transaction: TransactionBase) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...

class SetTargetCompound(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataCommand.DataCommandBase,
):  # Class
    def __init__(
        self, dataFile: DataFileBase, batchID: int, sampleID: int, compoundID: int
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self, transaction: TransactionBase) -> None: ...
    def Redo(self, transaction: TransactionBase) -> None: ...
    def SetValue(self, name: str, value_: Any) -> None: ...
    def Undo(self, transaction: TransactionBase) -> None: ...
