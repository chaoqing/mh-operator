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

from . import UnknownsAnalysisDataSet
from .Command import CompressResultsTasks, KeyValue

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile

class BulkInsertBase(System.IDisposable):  # Class
    def Insert(self, values: List[KeyValue]) -> None: ...
    def Dispose(self) -> None: ...

class DataFileBase(System.IDisposable):  # Class
    FilePath: str  # readonly
    IsAuditTrailing: bool  # readonly
    IsOpen: bool  # readonly
    IsReadOnly: bool  # readonly

    def GetIdentificationMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        identificationMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.IdentificationMethodDataTable,
    ) -> int: ...
    def BeginTransaction(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase
    ): ...
    def GetTargetQualifier(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        qualifierID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetQualifierDataTable,
    ) -> int: ...
    def RemoveAuxiliaryMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def RemoveTargetQualifier(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        qualifierID: int,
    ) -> int: ...
    def GetPeakQualifier(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        qualifierID: Optional[int],
        peakID: Optional[int],
        table: UnknownsAnalysisDataSet.PeakQualifierDataTable,
    ) -> int: ...
    def RemoveIdentificationMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
    ) -> int: ...
    def GetSamplesAndAuxiliaryMethods(self, table: System.Data.DataTable) -> None: ...
    def GetComponent(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        table: UnknownsAnalysisDataSet.ComponentDataTable,
    ) -> int: ...
    def GetSamplesAndIdentificationMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def GetCount(self, batchID: int, sampleID: int, table: str, where: str) -> int: ...
    def CreateBulkInsertExactMass(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def RemoveSample(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def ClearBlankSubtrationResults(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def GetDeconvolutionMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
    ) -> int: ...
    def Dispose(self) -> None: ...
    def CreateBulkInsertComponent(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def GetSample(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.SampleDataTable,
    ) -> int: ...
    def GetTargetCompound(
        self,
        batchId: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetCompoundDataTable,
    ) -> int: ...
    def ClearHits(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def GetSamplesAndTargetMatchMethods(self, table: System.Data.DataTable) -> None: ...
    def GetBatch(
        self, batchID: Optional[int], table: UnknownsAnalysisDataSet.BatchDataTable
    ) -> int: ...
    def NewFile(self, filePath: str, auditTrail: bool) -> None: ...
    def Save(self, progress: System.Action[int, str]) -> None: ...
    def GetSamplesAndLibrarySearchMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def GetSamplesAndDeconvolutionMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def CreateBulkInsertHit(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def InsertRow(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        table: str,
        values: List[KeyValue],
    ) -> int: ...
    def RemoveHit(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
    ) -> int: ...
    def GetAuxiliaryMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.AuxiliaryMethodDataTable,
    ) -> int: ...
    def ClearIonPeaks(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def GetHitsFromMethod(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: Optional[int],
        identificationMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.HitDataTable,
    ) -> int: ...
    def RemoveExactMass(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        exactMassID: int,
    ) -> int: ...
    def RemoveBatch(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
    ) -> int: ...
    def FindMaxComponentID(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int
    ) -> int: ...
    def GetAnalysis(self, table: UnknownsAnalysisDataSet.AnalysisDataTable) -> int: ...
    def GetExactMass(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        hitID: Optional[int],
        exactMassID: Optional[int],
        table: UnknownsAnalysisDataSet.ExactMassDataTable,
    ) -> int: ...
    def RemovePeakQualifier(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        qualifierID: int,
        peakID: int,
    ) -> int: ...
    def RemoveLibrarySearchMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> int: ...
    def RemovePeak(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        peakID: int,
    ) -> int: ...
    def UnlockAuditTrail(self) -> None: ...
    def GetTargetCompoundsAndPeaks(
        self, batchID: int, sampleID: int, table: System.Data.DataTable
    ) -> None: ...
    def AddEntry(
        self,
        user: str,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
        exception: System.Exception,
        reason: str,
    ) -> None: ...
    def GetBlankSubtractionMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.BlankSubtractionMethodDataTable,
    ) -> int: ...
    def GetLibrarySearchMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        identificationMethodID: Optional[int],
        librarySearchMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.LibrarySearchMethodDataTable,
    ) -> int: ...
    @overload
    def ExecuteReader(
        self, batchID: int, sampleID: int, select: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataReaderBase
    ): ...
    @overload
    def ExecuteReader(
        self, batchID: int, sampleID: int, select: str, parameters: List[KeyValue]
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataReaderBase
    ): ...
    def RemoveBlankSubtractionMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        blankSubtractionID: int,
    ) -> int: ...
    def RemoveComponent(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
    ) -> int: ...
    def RemoveDeconvolutionMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
    ) -> int: ...
    def CompressResults(
        self,
        compressLevel: CompressResultsTasks,
        abort: System.Threading.WaitHandle,
        progress: System.Action[int, str],
    ) -> None: ...
    def RemoveTargetCompound(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
    ) -> int: ...
    def GetSampleCount(self, batchID: Optional[int]) -> int: ...
    def LockAuditTrail(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet
    ): ...
    def GetTargetMatchMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        targetMatchMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetMatchMethodDataTable,
    ) -> int: ...
    def GetComponentsAndHitsAndTargetCompounds(
        self, batchID: int, sampleID: int, table: System.Data.DataTable
    ) -> None: ...
    def CloseFile(self) -> None: ...
    def GetIonPeak(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        ionPeakID: Optional[int],
        table: UnknownsAnalysisDataSet.IonPeakDataTable,
    ) -> int: ...
    def Open(
        self,
        filePath: str,
        isReadOnly: bool,
        abort: System.Threading.WaitHandle,
        progress: System.Action[int, str],
    ) -> None: ...
    def SetValues(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        table: str,
        values: List[KeyValue],
        where: List[KeyValue],
    ) -> int: ...
    def RunQuery(self, query: str, table: System.Data.DataTable) -> None: ...
    def EndTransaction(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        commit: bool,
    ) -> None: ...
    def CreateBulkInsertIonPeak(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def GetHit(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        hitID: Optional[int],
        table: UnknownsAnalysisDataSet.HitDataTable,
    ) -> int: ...
    def GetMethod(
        self, batchID: int, sampleID: int, dataSet: UnknownsAnalysisDataSet
    ) -> None: ...
    def GetPeak(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        peakID: Optional[int],
        table: UnknownsAnalysisDataSet.PeakDataTable,
    ) -> int: ...
    def FindMaxBatchID(self) -> int: ...
    def ClearMethods(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def GetSamplesAndBlankSubtractionMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def ClearTargetMatchResults(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def ClearExactMass(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def ClearResults(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def RemoveIonPeak(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
    ) -> int: ...
    def RemoveTargetMatchMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        targetMatchMethodID: int,
    ) -> int: ...
    def GetComponentAndModelIonPeak(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        compTable: UnknownsAnalysisDataSet.ComponentDataTable,
        ipTable: UnknownsAnalysisDataSet.IonPeakDataTable,
    ) -> None: ...
    def ClearComponents(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def FindMaxSampleID(self, batchID: int) -> int: ...
    def SaveAs(
        self, filePath: str, progress: System.Action[int, str], upload: System.Action
    ) -> None: ...
    def ClearTable(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        table: str,
        where: str,
    ) -> int: ...

class DataFileSql(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataFileBase,
):  # Class
    IsOpen: bool  # readonly

    def GetIdentificationMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        identificationMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.IdentificationMethodDataTable,
    ) -> int: ...
    def BeginTransaction(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase
    ): ...
    def GetTargetQualifier(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        qualifierID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetQualifierDataTable,
    ) -> int: ...
    def RemoveAuxiliaryMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def RemoveTargetQualifier(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        qualifierID: int,
    ) -> int: ...
    def GetPeakQualifier(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        qualifierID: Optional[int],
        peakID: Optional[int],
        table: UnknownsAnalysisDataSet.PeakQualifierDataTable,
    ) -> int: ...
    def RemoveIdentificationMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
    ) -> int: ...
    def GetSamplesAndAuxiliaryMethods(self, table: System.Data.DataTable) -> None: ...
    def GetComponent(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        table: UnknownsAnalysisDataSet.ComponentDataTable,
    ) -> int: ...
    def GetSamplesAndIdentificationMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def RemoveSample(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def ClearBlankSubtrationResults(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def GetDeconvolutionMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
    ) -> int: ...
    def GetSample(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.SampleDataTable,
    ) -> int: ...
    def GetTargetCompound(
        self,
        batchId: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetCompoundDataTable,
    ) -> int: ...
    def ClearHits(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def GetSamplesAndTargetMatchMethods(self, table: System.Data.DataTable) -> None: ...
    def GetBatch(
        self, batchID: Optional[int], table: UnknownsAnalysisDataSet.BatchDataTable
    ) -> int: ...
    def GetSamplesAndLibrarySearchMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def GetSamplesAndDeconvolutionMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def InsertRow(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        table: str,
        values: List[KeyValue],
    ) -> int: ...
    def RemoveHit(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
    ) -> int: ...
    def GetAuxiliaryMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.AuxiliaryMethodDataTable,
    ) -> int: ...
    def ClearIonPeaks(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def GetHitsFromMethod(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: Optional[int],
        identificationMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.HitDataTable,
    ) -> int: ...
    def RemoveExactMass(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        exactMassID: int,
    ) -> int: ...
    def RemoveBatch(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
    ) -> int: ...
    def FindMaxComponentID(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int
    ) -> int: ...
    def GetAnalysis(self, table: UnknownsAnalysisDataSet.AnalysisDataTable) -> int: ...
    def GetExactMass(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        hitID: Optional[int],
        exactMassID: Optional[int],
        table: UnknownsAnalysisDataSet.ExactMassDataTable,
    ) -> int: ...
    def RemovePeakQualifier(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        qualifierID: int,
        peakID: int,
    ) -> int: ...
    def RemoveLibrarySearchMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> int: ...
    def RemovePeak(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        peakID: int,
    ) -> int: ...
    def GetTargetCompoundsAndPeaks(
        self, batchID: int, sampleID: int, table: System.Data.DataTable
    ) -> None: ...
    def GetBlankSubtractionMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.BlankSubtractionMethodDataTable,
    ) -> int: ...
    def GetLibrarySearchMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        identificationMethodID: Optional[int],
        librarySearchMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.LibrarySearchMethodDataTable,
    ) -> int: ...
    def RemoveComponent(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
    ) -> int: ...
    def RemoveDeconvolutionMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
    ) -> int: ...
    def RemoveBlankSubtractionMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        blankSubtractionID: int,
    ) -> int: ...
    def RemoveTargetCompound(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
    ) -> int: ...
    def GetSampleCount(self, batchID: Optional[int]) -> int: ...
    def GetTargetMatchMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        targetMatchMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetMatchMethodDataTable,
    ) -> int: ...
    def GetComponentsAndHitsAndTargetCompounds(
        self, batchID: int, sampleID: int, table: System.Data.DataTable
    ) -> None: ...
    def GetIonPeak(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        ionPeakID: Optional[int],
        table: UnknownsAnalysisDataSet.IonPeakDataTable,
    ) -> int: ...
    def SetValues(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        table: str,
        values: List[KeyValue],
        where: List[KeyValue],
    ) -> int: ...
    def RunQuery(self, query: str, table: System.Data.DataTable) -> None: ...
    def EndTransaction(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        commit: bool,
    ) -> None: ...
    def GetHit(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        hitID: Optional[int],
        table: UnknownsAnalysisDataSet.HitDataTable,
    ) -> int: ...
    def GetMethod(
        self, batchID: int, sampleID: int, dataSet: UnknownsAnalysisDataSet
    ) -> None: ...
    def GetPeak(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        peakID: Optional[int],
        table: UnknownsAnalysisDataSet.PeakDataTable,
    ) -> int: ...
    def FindMaxBatchID(self) -> int: ...
    def ClearMethods(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def GetSamplesAndBlankSubtractionMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def ClearTargetMatchResults(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def ClearExactMass(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def ClearResults(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def RemoveIonPeak(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
    ) -> int: ...
    def RemoveTargetMatchMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        targetMatchMethodID: int,
    ) -> int: ...
    def GetComponentAndModelIonPeak(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        compTable: UnknownsAnalysisDataSet.ComponentDataTable,
        ipTable: UnknownsAnalysisDataSet.IonPeakDataTable,
    ) -> None: ...
    def ClearComponents(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def FindMaxSampleID(self, batchID: int) -> int: ...
    def ClearTable(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        table: str,
        where: str,
    ) -> int: ...

class DataFileSqlCe(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataFileSql,
):  # Class
    def __init__(self) -> None: ...

    FilePath: str  # readonly
    IsAuditTrailing: bool  # readonly
    IsReadOnly: bool  # readonly
    MaxDatabaseSize: int  # static

    def LockAuditTrail(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet
    ): ...
    def Save(self, progress: System.Action[int, str]) -> None: ...
    def Open(
        self,
        filePath: str,
        isReadOnly: bool,
        abort: System.Threading.WaitHandle,
        progress: System.Action[int, str],
    ) -> None: ...
    def CreateBulkInsertIonPeak(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def CreateBulkInsertComponent(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    @overload
    def ExecuteReader(
        self, batchID: int, sampleID: int, select: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataReaderBase
    ): ...
    @overload
    def ExecuteReader(
        self, batchID: int, sampleID: int, select: str, parameters: List[KeyValue]
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataReaderBase
    ): ...
    def CreateBulkInsertHit(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def NewFile(self, filePath: str, auditTrail: bool) -> None: ...
    def CompressResults(
        self,
        tasks: CompressResultsTasks,
        abort: System.Threading.WaitHandle,
        progress: System.Action[int, str],
    ) -> None: ...
    def GetCount(self, batchID: int, sampleID: int, table: str, where: str) -> int: ...
    def CreateBulkInsertExactMass(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def UnlockAuditTrail(self) -> None: ...
    def SaveAs(
        self, filePath: str, progress: System.Action[int, str], upload: System.Action
    ) -> None: ...
    def CloseFile(self) -> None: ...
    def AddEntry(
        self,
        user: str,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
        exception: System.Exception,
        reason: str,
    ) -> None: ...

class DataFileSqlCePerSample(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataFileBase,
):  # Class
    def __init__(self) -> None: ...

    FilePath: str  # readonly
    IsAuditTrailing: bool  # readonly
    IsOpen: bool  # readonly
    IsReadOnly: bool  # readonly

    def GetIdentificationMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        identificationMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.IdentificationMethodDataTable,
    ) -> int: ...
    def BeginTransaction(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase
    ): ...
    def GetTargetQualifier(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        qualifierID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetQualifierDataTable,
    ) -> int: ...
    def RemoveAuxiliaryMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def RemoveTargetQualifier(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        qualifierID: int,
    ) -> int: ...
    def GetPeakQualifier(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        qualifierID: Optional[int],
        peakID: Optional[int],
        table: UnknownsAnalysisDataSet.PeakQualifierDataTable,
    ) -> int: ...
    def RemoveIdentificationMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
    ) -> int: ...
    def GetSamplesAndAuxiliaryMethods(self, table: System.Data.DataTable) -> None: ...
    def GetComponent(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        table: UnknownsAnalysisDataSet.ComponentDataTable,
    ) -> int: ...
    def GetSamplesAndIdentificationMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def GetCount(self, batchID: int, sampleID: int, table: str, where: str) -> int: ...
    def CreateBulkInsertExactMass(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def RemoveSample(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def ClearBlankSubtrationResults(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    @staticmethod
    def ResultsStoredPerSample(path: str) -> bool: ...
    def GetDeconvolutionMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.DeconvolutionMethodDataTable,
    ) -> int: ...
    def CreateBulkInsertComponent(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def GetSample(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.SampleDataTable,
    ) -> int: ...
    def GetTargetCompound(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetCompoundDataTable,
    ) -> int: ...
    def ClearHits(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def GetSamplesAndTargetMatchMethods(self, table: System.Data.DataTable) -> None: ...
    def GetBatch(
        self, batchID: Optional[int], table: UnknownsAnalysisDataSet.BatchDataTable
    ) -> int: ...
    def NewFile(self, filePath: str, auditTrail: bool) -> None: ...
    def Save(self, progress: System.Action[int, str]) -> None: ...
    def GetSamplesAndLibrarySearchMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def GetSamplesAndDeconvolutionMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def CreateBulkInsertHit(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def InsertRow(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        table: str,
        values: List[KeyValue],
    ) -> int: ...
    def RemoveHit(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
    ) -> int: ...
    def GetAuxiliaryMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.AuxiliaryMethodDataTable,
    ) -> int: ...
    def ClearIonPeaks(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def GetHitsFromMethod(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: Optional[int],
        identificationMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.HitDataTable,
    ) -> int: ...
    def RemoveExactMass(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        hitID: int,
        exactMassID: int,
    ) -> int: ...
    def RemoveBatch(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
    ) -> int: ...
    def FindMaxComponentID(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int
    ) -> int: ...
    def GetAnalysis(self, table: UnknownsAnalysisDataSet.AnalysisDataTable) -> int: ...
    def GetExactMass(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        hitID: Optional[int],
        exactMassID: Optional[int],
        table: UnknownsAnalysisDataSet.ExactMassDataTable,
    ) -> int: ...
    def RemovePeakQualifier(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        qualifierID: int,
        peakID: int,
    ) -> int: ...
    def RemoveLibrarySearchMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        identificationMethodID: int,
        librarySearchMethodID: int,
    ) -> int: ...
    def RemovePeak(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
        peakID: int,
    ) -> int: ...
    def UnlockAuditTrail(self) -> None: ...
    def GetTargetCompoundsAndPeaks(
        self, batchID: int, sampleID: int, table: System.Data.DataTable
    ) -> None: ...
    def AddEntry(
        self,
        user: str,
        command: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.IComplianceCommand,
        exception: System.Exception,
        reason: str,
    ) -> None: ...
    def GetBlankSubtractionMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        table: UnknownsAnalysisDataSet.BlankSubtractionMethodDataTable,
    ) -> int: ...
    def GetLibrarySearchMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        identificationMethodID: Optional[int],
        librarySearchMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.LibrarySearchMethodDataTable,
    ) -> int: ...
    @overload
    def ExecuteReader(
        self, batchID: int, sampleID: int, select: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataReaderBase
    ): ...
    @overload
    def ExecuteReader(
        self, batchID: int, sampleID: int, select: str, parameters: List[KeyValue]
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.DataReaderBase
    ): ...
    @staticmethod
    def ReadAnalysisInfo(
        file: str, table: UnknownsAnalysisDataSet.AnalysisDataTable
    ) -> None: ...
    def RemoveBlankSubtractionMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        blankSubtractionID: int,
    ) -> int: ...
    def RemoveComponent(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
    ) -> int: ...
    def CompressResults(
        self,
        tasks: CompressResultsTasks,
        abort: System.Threading.WaitHandle,
        progress: System.Action[int, str],
    ) -> None: ...
    def RemoveDeconvolutionMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
    ) -> int: ...
    def RemoveTargetCompound(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        compoundID: int,
    ) -> int: ...
    def GetSampleCount(self, batchID: Optional[int]) -> int: ...
    def LockAuditTrail(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.AuditTrailDataSet
    ): ...
    def GetTargetMatchMethod(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        targetMatchMethodID: Optional[int],
        table: UnknownsAnalysisDataSet.TargetMatchMethodDataTable,
    ) -> int: ...
    def GetComponentsAndHitsAndTargetCompounds(
        self, batchID: int, sampleID: int, table: System.Data.DataTable
    ) -> None: ...
    def CloseFile(self) -> None: ...
    def GetIonPeak(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        ionPeakID: Optional[int],
        table: UnknownsAnalysisDataSet.IonPeakDataTable,
    ) -> int: ...
    def Open(
        self,
        filePath: str,
        isReadOnly: bool,
        abort: System.Threading.WaitHandle,
        progress: System.Action[int, str],
    ) -> None: ...
    def SetValues(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        table: str,
        values: List[KeyValue],
        where: List[KeyValue],
    ) -> int: ...
    def RunQuery(self, query: str, table: System.Data.DataTable) -> None: ...
    def EndTransaction(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        commit: bool,
    ) -> None: ...
    def CreateBulkInsertIonPeak(
        self, batchId: int, sampleId: int
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase
    ): ...
    def GetHit(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        deconvolutionMethodID: Optional[int],
        componentID: Optional[int],
        hitID: Optional[int],
        table: UnknownsAnalysisDataSet.HitDataTable,
    ) -> int: ...
    def GetMethod(
        self, batchID: int, sampleID: int, dataSet: UnknownsAnalysisDataSet
    ) -> None: ...
    def GetPeak(
        self,
        batchID: Optional[int],
        sampleID: Optional[int],
        compoundID: Optional[int],
        peakID: Optional[int],
        table: UnknownsAnalysisDataSet.PeakDataTable,
    ) -> int: ...
    def FindMaxBatchID(self) -> int: ...
    def ClearMethods(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def GetSamplesAndBlankSubtractionMethods(
        self, table: System.Data.DataTable
    ) -> None: ...
    def ClearTargetMatchResults(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def ClearExactMass(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def ClearResults(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: Optional[int],
        sampleID: Optional[int],
    ) -> int: ...
    def RemoveIonPeak(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        ionPeakID: int,
    ) -> int: ...
    def RemoveTargetMatchMethod(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
        targetMatchMethodID: int,
    ) -> int: ...
    def GetComponentAndModelIonPeak(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodID: int,
        componentID: int,
        compTable: UnknownsAnalysisDataSet.ComponentDataTable,
        ipTable: UnknownsAnalysisDataSet.IonPeakDataTable,
    ) -> None: ...
    def ClearComponents(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        batchID: int,
        sampleID: int,
    ) -> int: ...
    def FindMaxSampleID(self, batchID: int) -> int: ...
    def SaveAs(
        self,
        filePath: str,
        progress: System.Action[int, str],
        actionUpload: System.Action,
    ) -> None: ...
    def ClearTable(
        self,
        transaction: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.TransactionBase,
        table: str,
        where: str,
    ) -> int: ...

class DataReaderBase(System.IDisposable):  # Class
    def __getitem__(self, name: str) -> Any: ...
    def IsDBNull(self, name: str) -> bool: ...
    def Read(self) -> bool: ...
    def Dispose(self) -> None: ...

class SqlCeBulkInsert(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.DataFile.BulkInsertBase,
    System.IDisposable,
):  # Class
    def Insert(self, values: List[KeyValue]) -> None: ...

class TransactionBase(System.IDisposable):  # Class
    def Dispose(self) -> None: ...
    def Commit(self) -> None: ...
    def Rollback(self) -> None: ...
