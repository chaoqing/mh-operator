# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    division,
    generators,
    nested_scopes,
    print_function,
    unicode_literals,
    with_statement,
)

import datetime

from mh_operator.legacy.common import (
    DataTableBase,
    DataTablesBase,
    RowBase,
    field_decorator,
    table_property,
)


class BatchRow(RowBase):
    """Represents a row for the Batch table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def TargetBatchDataPath(self):
        # type: () -> str | None
        return self._values[1]

    @field_decorator(index=2)
    def TargetBatchFileName(self):
        # type: () -> str | None
        return self._values[2]

    @field_decorator(index=3)
    def AppSchemaVersion(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def SchemaVersion(self):
        # type: () -> int | None
        return self._values[4]

    @field_decorator(index=5)
    def DataVersion(self):
        # type: () -> int | None
        return self._values[5]

    @field_decorator(index=6)
    def BatchState(self):
        # type: () -> str | None
        return self._values[6]

    @field_decorator(index=7)
    def AnalystName(self):
        # type: () -> str | None
        return self._values[7]

    @field_decorator(index=8)
    def AnalysisTimeStamp(self):
        # type: () -> datetime.datetime | None
        return self._values[8]

    @field_decorator(index=9)
    def FeatureDetection(self):
        # type: () -> bool | None
        return self._values[9]

    @field_decorator(index=10)
    def ReferenceWindow(self):
        # type: () -> float | None
        return self._values[10]

    @field_decorator(index=11)
    def ReferenceWindowPercentOrMinutes(self):
        # type: () -> str | None
        return self._values[11]

    @field_decorator(index=12)
    def NonReferenceWindow(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def NonReferenceWindowPercentOrMinutes(self):
        # type: () -> str | None
        return self._values[13]

    @field_decorator(index=14)
    def CorrelationWindow(self):
        # type: () -> float | None
        return self._values[14]

    @field_decorator(index=15)
    def ApplyMultiplierTarget(self):
        # type: () -> bool | None
        return self._values[15]

    @field_decorator(index=16)
    def ApplyMultiplierSurrogate(self):
        # type: () -> bool | None
        return self._values[16]

    @field_decorator(index=17)
    def ApplyMultiplierISTD(self):
        # type: () -> bool | None
        return self._values[17]

    @field_decorator(index=18)
    def ApplyMultiplierMatrixSpike(self):
        # type: () -> bool | None
        return self._values[18]

    @field_decorator(index=19)
    def IgnorePeaksNotFound(self):
        # type: () -> bool | None
        return self._values[19]

    @field_decorator(index=20)
    def RelativeISTD(self):
        # type: () -> bool | None
        return self._values[20]

    @field_decorator(index=21)
    def AuditTrail(self):
        # type: () -> bool | None
        return self._values[21]

    @field_decorator(index=22)
    def RefLibraryPathFileName(self):
        # type: () -> str | None
        return self._values[22]

    @field_decorator(index=23)
    def RefLibraryPatternPathFileName(self):
        # type: () -> str | None
        return self._values[23]

    @field_decorator(index=24)
    def LibraryMethodPathFileName(self):
        # type: () -> str | None
        return self._values[24]

    @field_decorator(index=25)
    def ReferencePatternLibraryPathFileName(self):
        # type: () -> str | None
        return self._values[25]

    @field_decorator(index=26)
    def CCMaximumElapsedTimeInHours(self):
        # type: () -> float | None
        return self._values[26]

    @field_decorator(index=27)
    def BracketingType(self):
        # type: () -> str | None
        return self._values[27]

    @field_decorator(index=28)
    def StandardAddition(self):
        # type: () -> bool | None
        return self._values[28]

    @field_decorator(index=29)
    def DynamicBackgroundSubtraction(self):
        # type: () -> bool | None
        return self._values[29]

    @field_decorator(index=30)
    def DAMethodPathFileNameOrigin(self):
        # type: () -> str | None
        return self._values[30]

    @field_decorator(index=31)
    def DAMethodLastAppliedTimeStamp(self):
        # type: () -> datetime.datetime | None
        return self._values[31]

    @field_decorator(index=32)
    def CalibrationLastUpdatedTimeStamp(self):
        # type: () -> datetime.datetime | None
        return self._values[32]

    @field_decorator(index=33)
    def AnalyzeQuantVersion(self):
        # type: () -> str | None
        return self._values[33]


class BatchDataTable(DataTableBase[BatchRow]):
    """Represents the Batch table, containing BatchRow objects."""

    pass


class SampleRow(RowBase):
    """Represents a row for the Sample table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def AcqDateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[2]

    @field_decorator(index=3)
    def AcqDateTimeLocal(self):
        # type: () -> Any | None
        return self._values[3]

    @field_decorator(index=4)
    def AcqMethodFileName(self):
        # type: () -> str | None
        return self._values[4]

    @field_decorator(index=5)
    def AcqMethodPathName(self):
        # type: () -> str | None
        return self._values[5]

    @field_decorator(index=6)
    def AcqOperator(self):
        # type: () -> str | None
        return self._values[6]

    @field_decorator(index=7)
    def Barcode(self):
        # type: () -> str | None
        return self._values[7]

    @field_decorator(index=8)
    def Comment(self):
        # type: () -> str | None
        return self._values[8]

    @field_decorator(index=9)
    def DataFileName(self):
        # type: () -> str | None
        return self._values[9]

    @field_decorator(index=10)
    def DataPathName(self):
        # type: () -> str | None
        return self._values[10]

    @field_decorator(index=11)
    def Dilution(self):
        # type: () -> float | None
        return self._values[11]

    @field_decorator(index=12)
    def ExpectedBarCode(self):
        # type: () -> str | None
        return self._values[12]

    @field_decorator(index=13)
    def InjectorVolume(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def InstrumentName(self):
        # type: () -> str | None
        return self._values[14]

    @field_decorator(index=15)
    def InstrumentType(self):
        # type: () -> str | None
        return self._values[15]

    @field_decorator(index=16)
    def ISTDDilution(self):
        # type: () -> float | None
        return self._values[16]

    @field_decorator(index=17)
    def MatrixSpikeDilution(self):
        # type: () -> float | None
        return self._values[17]

    @field_decorator(index=18)
    def MatrixSpikeGroup(self):
        # type: () -> str | None
        return self._values[18]

    @field_decorator(index=19)
    def MatrixType(self):
        # type: () -> str | None
        return self._values[19]

    @field_decorator(index=20)
    def PlateCode(self):
        # type: () -> str | None
        return self._values[20]

    @field_decorator(index=21)
    def PlatePosition(self):
        # type: () -> str | None
        return self._values[21]

    @field_decorator(index=22)
    def RackCode(self):
        # type: () -> str | None
        return self._values[22]

    @field_decorator(index=23)
    def RackPosition(self):
        # type: () -> str | None
        return self._values[23]

    @field_decorator(index=24)
    def SampleAmount(self):
        # type: () -> float | None
        return self._values[24]

    @field_decorator(index=25)
    def SampleInformation(self):
        # type: () -> str | None
        return self._values[25]

    @field_decorator(index=26)
    def SampleGroup(self):
        # type: () -> str | None
        return self._values[26]

    @field_decorator(index=27)
    def SampleName(self):
        # type: () -> str | None
        return self._values[27]

    @field_decorator(index=28)
    def SamplePosition(self):
        # type: () -> str | None
        return self._values[28]

    @field_decorator(index=29)
    def SamplePrepFileName(self):
        # type: () -> str | None
        return self._values[29]

    @field_decorator(index=30)
    def SamplePrepPathName(self):
        # type: () -> str | None
        return self._values[30]

    @field_decorator(index=31)
    def SampleType(self):
        # type: () -> str | None
        return self._values[31]

    @field_decorator(index=32)
    def SamplingDateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[32]

    @field_decorator(index=33)
    def SamplingTime(self):
        # type: () -> float | None
        return self._values[33]

    @field_decorator(index=34)
    def SurrogateDilution(self):
        # type: () -> float | None
        return self._values[34]

    @field_decorator(index=35)
    def TotalSampleAmount(self):
        # type: () -> float | None
        return self._values[35]

    @field_decorator(index=36)
    def TrayName(self):
        # type: () -> str | None
        return self._values[36]

    @field_decorator(index=37)
    def TuneFileLastTimeStamp(self):
        # type: () -> datetime.datetime | None
        return self._values[37]

    @field_decorator(index=38)
    def TuneFileName(self):
        # type: () -> str | None
        return self._values[38]

    @field_decorator(index=39)
    def TunePathName(self):
        # type: () -> str | None
        return self._values[39]

    @field_decorator(index=40)
    def UserDefined(self):
        # type: () -> str | None
        return self._values[40]

    @field_decorator(index=41)
    def UserDefined1(self):
        # type: () -> str | None
        return self._values[41]

    @field_decorator(index=42)
    def UserDefined2(self):
        # type: () -> str | None
        return self._values[42]

    @field_decorator(index=43)
    def UserDefined3(self):
        # type: () -> str | None
        return self._values[43]

    @field_decorator(index=44)
    def UserDefined4(self):
        # type: () -> str | None
        return self._values[44]

    @field_decorator(index=45)
    def UserDefined5(self):
        # type: () -> str | None
        return self._values[45]

    @field_decorator(index=46)
    def UserDefined6(self):
        # type: () -> str | None
        return self._values[46]

    @field_decorator(index=47)
    def UserDefined7(self):
        # type: () -> str | None
        return self._values[47]

    @field_decorator(index=48)
    def UserDefined8(self):
        # type: () -> str | None
        return self._values[48]

    @field_decorator(index=49)
    def UserDefined9(self):
        # type: () -> str | None
        return self._values[49]

    @field_decorator(index=50)
    def Vial(self):
        # type: () -> int | None
        return self._values[50]

    @field_decorator(index=51)
    def AnalysisState(self):
        # type: () -> str | None
        return self._values[51]

    @field_decorator(index=52)
    def GraphicsSampleChromatogram(self):
        # type: () -> str | None
        return self._values[52]


class SampleDataTable(DataTableBase[SampleRow]):
    """Represents the Sample table, containing SampleRow objects."""

    pass


class ComponentRow(RowBase):
    """Represents a row for the Component table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def DeconvolutionMethodID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def ComponentID(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def PrimaryHitID(self):
        # type: () -> int | None
        return self._values[4]

    @field_decorator(index=5)
    def ModelIonPeakID(self):
        # type: () -> int | None
        return self._values[5]

    @field_decorator(index=6)
    def ComponentName(self):
        # type: () -> str | None
        return self._values[6]

    @field_decorator(index=7)
    def BasePeakID(self):
        # type: () -> int | None
        return self._values[7]

    @field_decorator(index=8)
    def IsManuallyIntegrated(self):
        # type: () -> bool | None
        return self._values[8]

    @field_decorator(index=9)
    def IsBackgroundSubtracted(self):
        # type: () -> bool | None
        return self._values[9]

    @field_decorator(index=10)
    def BestHit(self):
        # type: () -> bool | None
        return self._values[10]

    @field_decorator(index=11)
    def BestHitOverridden(self):
        # type: () -> bool | None
        return self._values[11]

    @field_decorator(index=12)
    def Area(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def EndX(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def Height(self):
        # type: () -> float | None
        return self._values[14]

    @field_decorator(index=15)
    def IsAccurateMass(self):
        # type: () -> bool | None
        return self._values[15]

    @field_decorator(index=16)
    def RetentionTime(self):
        # type: () -> float | None
        return self._values[16]

    @field_decorator(index=17)
    def RetentionIndex(self):
        # type: () -> float | None
        return self._values[17]

    @field_decorator(index=18)
    def SpectrumAbundances(self):
        # type: () -> str | None
        return self._values[18]

    @field_decorator(index=19)
    def SpectrumMZs(self):
        # type: () -> str | None
        return self._values[19]

    @field_decorator(index=20)
    def StartX(self):
        # type: () -> float | None
        return self._values[20]

    @field_decorator(index=21)
    def XArray(self):
        # type: () -> str | None
        return self._values[21]

    @field_decorator(index=22)
    def YArray(self):
        # type: () -> str | None
        return self._values[22]

    @field_decorator(index=23)
    def ShapeQuality(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def DeconvolutedHeight(self):
        # type: () -> float | None
        return self._values[24]

    @field_decorator(index=25)
    def AreaPercent(self):
        # type: () -> float | None
        return self._values[25]

    @field_decorator(index=26)
    def AreaPercentMax(self):
        # type: () -> float | None
        return self._values[26]

    @field_decorator(index=27)
    def Visible(self):
        # type: () -> bool | None
        return self._values[27]

    @field_decorator(index=28)
    def UserDefined(self):
        # type: () -> str | None
        return self._values[28]

    @field_decorator(index=29)
    def UserCustomCalculation(self):
        # type: () -> float | None
        return self._values[29]

    @field_decorator(index=30)
    def GraphicsComponentSpectrum(self):
        # type: () -> str | None
        return self._values[30]

    @field_decorator(index=31)
    def TargetedDeconvolution_IdentificationMethodID(self):
        # type: () -> int | None
        return self._values[31]

    @field_decorator(index=32)
    def TargetedDeconvolution_LibrarySearchMethodID(self):
        # type: () -> int | None
        return self._values[32]

    @field_decorator(index=33)
    def TargetedDeconvolution_LibraryEntryID(self):
        # type: () -> int | None
        return self._values[33]


class ComponentDataTable(DataTableBase[ComponentRow]):
    """Represents the Component table, containing ComponentRow objects."""

    pass


class HitRow(RowBase):
    """Represents a row for the Hit table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def DeconvolutionMethodID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def ComponentID(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def HitID(self):
        # type: () -> int | None
        return self._values[4]

    @field_decorator(index=5)
    def AgilentID(self):
        # type: () -> str | None
        return self._values[5]

    @field_decorator(index=6)
    def IdentificationMethodID(self):
        # type: () -> int | None
        return self._values[6]

    @field_decorator(index=7)
    def LibrarySearchMethodID(self):
        # type: () -> int | None
        return self._values[7]

    @field_decorator(index=8)
    def LibraryEntryID(self):
        # type: () -> int | None
        return self._values[8]

    @field_decorator(index=9)
    def TargetCompoundID(self):
        # type: () -> int | None
        return self._values[9]

    @field_decorator(index=10)
    def CASNumber(self):
        # type: () -> str | None
        return self._values[10]

    @field_decorator(index=11)
    def CompoundName(self):
        # type: () -> str | None
        return self._values[11]

    @field_decorator(index=12)
    def EstimatedConcentration(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def Formula(self):
        # type: () -> str | None
        return self._values[13]

    @field_decorator(index=14)
    def KEGGID(self):
        # type: () -> str | None
        return self._values[14]

    @field_decorator(index=15)
    def LibraryMatchScore(self):
        # type: () -> float | None
        return self._values[15]

    @field_decorator(index=16)
    def LibraryRetentionIndex(self):
        # type: () -> float | None
        return self._values[16]

    @field_decorator(index=17)
    def LibraryRetentionTime(self):
        # type: () -> float | None
        return self._values[17]

    @field_decorator(index=18)
    def LibraryCompoundDescription(self):
        # type: () -> str | None
        return self._values[18]

    @field_decorator(index=19)
    def MolecularWeight(self):
        # type: () -> float | None
        return self._values[19]

    @field_decorator(index=20)
    def RTMismatchPenalty(self):
        # type: () -> float | None
        return self._values[20]

    @field_decorator(index=21)
    def RetentionIndex(self):
        # type: () -> float | None
        return self._values[21]

    @field_decorator(index=22)
    def MassMatchScore(self):
        # type: () -> float | None
        return self._values[22]

    @field_decorator(index=23)
    def MassAbundanceScore(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def MassAccuracyScore(self):
        # type: () -> float | None
        return self._values[24]

    @field_decorator(index=25)
    def MassSpacingScore(self):
        # type: () -> float | None
        return self._values[25]

    @field_decorator(index=26)
    def Visible(self):
        # type: () -> bool | None
        return self._values[26]

    @field_decorator(index=27)
    def BlankSubtracted(self):
        # type: () -> bool | None
        return self._values[27]

    @field_decorator(index=28)
    def RemovedDuplicateMZs(self):
        # type: () -> str | None
        return self._values[28]

    @field_decorator(index=29)
    def ResponseFactorForEstimation(self):
        # type: () -> float | None
        return self._values[29]

    @field_decorator(index=30)
    def MonoIsotopicMass(self):
        # type: () -> float | None
        return self._values[30]

    @field_decorator(index=31)
    def NumberOfExactMasses(self):
        # type: () -> int | None
        return self._values[31]

    @field_decorator(index=32)
    def UserDefined(self):
        # type: () -> str | None
        return self._values[32]

    @field_decorator(index=33)
    def UserCustomCalculation(self):
        # type: () -> float | None
        return self._values[33]

    @field_decorator(index=34)
    def GraphicsHitLibrarySpectrum(self):
        # type: () -> str | None
        return self._values[34]


class HitDataTable(DataTableBase[HitRow]):
    """Represents the Hit table, containing HitRow objects."""

    pass


class IonPeakRow(RowBase):
    """Represents a row for the IonPeak table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def DeconvolutionMethodID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def ComponentID(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def IonPeakID(self):
        # type: () -> int | None
        return self._values[4]

    @field_decorator(index=5)
    def TargetCompoundID(self):
        # type: () -> int | None
        return self._values[5]

    @field_decorator(index=6)
    def TargetQualifierID(self):
        # type: () -> int | None
        return self._values[6]

    @field_decorator(index=7)
    def Area(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def DeconvolutedArea(self):
        # type: () -> float | None
        return self._values[8]

    @field_decorator(index=9)
    def DeconvolutedHeight(self):
        # type: () -> float | None
        return self._values[9]

    @field_decorator(index=10)
    def EndX(self):
        # type: () -> float | None
        return self._values[10]

    @field_decorator(index=11)
    def FullWidthHalfMaximum(self):
        # type: () -> float | None
        return self._values[11]

    @field_decorator(index=12)
    def Height(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def IonPolarity(self):
        # type: () -> str | None
        return self._values[13]

    @field_decorator(index=14)
    def MZ(self):
        # type: () -> float | None
        return self._values[14]

    @field_decorator(index=15)
    def PeakStatus(self):
        # type: () -> str | None
        return self._values[15]

    @field_decorator(index=16)
    def RetentionTime(self):
        # type: () -> float | None
        return self._values[16]

    @field_decorator(index=17)
    def Saturated(self):
        # type: () -> bool | None
        return self._values[17]

    @field_decorator(index=18)
    def ScanType(self):
        # type: () -> str | None
        return self._values[18]

    @field_decorator(index=19)
    def SelectedMZ(self):
        # type: () -> float | None
        return self._values[19]

    @field_decorator(index=20)
    def Sharpness(self):
        # type: () -> float | None
        return self._values[20]

    @field_decorator(index=21)
    def SignalToNoiseRatio(self):
        # type: () -> float | None
        return self._values[21]

    @field_decorator(index=22)
    def StartX(self):
        # type: () -> float | None
        return self._values[22]

    @field_decorator(index=23)
    def Symmetry(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def XArray(self):
        # type: () -> str | None
        return self._values[24]

    @field_decorator(index=25)
    def YArray(self):
        # type: () -> str | None
        return self._values[25]

    @field_decorator(index=26)
    def UserCustomCalculation(self):
        # type: () -> float | None
        return self._values[26]


class IonPeakDataTable(DataTableBase[IonPeakRow]):
    """Represents the IonPeak table, containing IonPeakRow objects."""

    pass


class DeconvolutionMethodRow(RowBase):
    """Represents a row for the DeconvolutionMethod table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def DeconvolutionMethodID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def Algorithm(self):
        # type: () -> str | None
        return self._values[3]

    @field_decorator(index=4)
    def ChromRangeHigh(self):
        # type: () -> float | None
        return self._values[4]

    @field_decorator(index=5)
    def ChromRangeLow(self):
        # type: () -> float | None
        return self._values[5]

    @field_decorator(index=6)
    def EICPeakThreshold(self):
        # type: () -> float | None
        return self._values[6]

    @field_decorator(index=7)
    def EICSNRThreshold(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def ExcludedMZs(self):
        # type: () -> str | None
        return self._values[8]

    @field_decorator(index=9)
    def LeftMZDelta(self):
        # type: () -> float | None
        return self._values[9]

    @field_decorator(index=10)
    def ModelShapePercentile(self):
        # type: () -> float | None
        return self._values[10]

    @field_decorator(index=11)
    def MZDeltaUnits(self):
        # type: () -> str | None
        return self._values[11]

    @field_decorator(index=12)
    def RetentionTimeBinSize(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def RightMZDelta(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def UseIntegerMZValues(self):
        # type: () -> bool | None
        return self._values[14]

    @field_decorator(index=15)
    def MaxSpectrumPeaksPerChromPeak(self):
        # type: () -> int | None
        return self._values[15]

    @field_decorator(index=16)
    def SpectrumPeakThreshold(self):
        # type: () -> float | None
        return self._values[16]

    @field_decorator(index=17)
    def UseLargestPeakShape(self):
        # type: () -> bool | None
        return self._values[17]

    @field_decorator(index=18)
    def WindowSizeFactor(self):
        # type: () -> float | None
        return self._values[18]

    @field_decorator(index=19)
    def TICAnalysis(self):
        # type: () -> bool | None
        return self._values[19]

    @field_decorator(index=20)
    def ChromPeakThreshold(self):
        # type: () -> float | None
        return self._values[20]

    @field_decorator(index=21)
    def ChromSNRThreshold(self):
        # type: () -> float | None
        return self._values[21]

    @field_decorator(index=22)
    def UseAreaFilterAbsolute(self):
        # type: () -> bool | None
        return self._values[22]

    @field_decorator(index=23)
    def AreaFilterAbsolute(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def UseAreaFilterRelative(self):
        # type: () -> bool | None
        return self._values[24]

    @field_decorator(index=25)
    def AreaFilterRelative(self):
        # type: () -> float | None
        return self._values[25]

    @field_decorator(index=26)
    def UseHeightFilterAbsolute(self):
        # type: () -> bool | None
        return self._values[26]

    @field_decorator(index=27)
    def HeightFilterAbsolute(self):
        # type: () -> float | None
        return self._values[27]

    @field_decorator(index=28)
    def UseHeightFilterRelative(self):
        # type: () -> bool | None
        return self._values[28]

    @field_decorator(index=29)
    def HeightFilterRelative(self):
        # type: () -> float | None
        return self._values[29]

    @field_decorator(index=30)
    def MaxNumPeaks(self):
        # type: () -> int | None
        return self._values[30]

    @field_decorator(index=31)
    def LargestPeaksRankedBy(self):
        # type: () -> str | None
        return self._values[31]

    @field_decorator(index=32)
    def RefineComponents(self):
        # type: () -> bool | None
        return self._values[32]

    @field_decorator(index=33)
    def MaxNumStoredIonPeaks(self):
        # type: () -> int | None
        return self._values[33]

    @field_decorator(index=34)
    def Integrator(self):
        # type: () -> str | None
        return self._values[34]

    @field_decorator(index=35)
    def Screening(self):
        # type: () -> bool | None
        return self._values[35]

    @field_decorator(index=36)
    def TargetedDeconvolution(self):
        # type: () -> bool | None
        return self._values[36]

    @field_decorator(index=37)
    def MinShapeQuality(self):
        # type: () -> float | None
        return self._values[37]

    @field_decorator(index=38)
    def MinNumPeaks(self):
        # type: () -> int | None
        return self._values[38]

    @field_decorator(index=39)
    def TICAnalysisSignalType(self):
        # type: () -> str | None
        return self._values[39]


class DeconvolutionMethodDataTable(DataTableBase[DeconvolutionMethodRow]):
    """Represents the DeconvolutionMethod table, containing DeconvolutionMethodRow objects."""

    pass


class LibrarySearchMethodRow(RowBase):
    """Represents a row for the LibrarySearchMethod table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def IdentificationMethodID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def LibrarySearchMethodID(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def LibraryFile(self):
        # type: () -> str | None
        return self._values[4]

    @field_decorator(index=5)
    def LibraryPath(self):
        # type: () -> str | None
        return self._values[5]

    @field_decorator(index=6)
    def LibraryType(self):
        # type: () -> str | None
        return self._values[6]

    @field_decorator(index=7)
    def ScreeningEnabled(self):
        # type: () -> bool | None
        return self._values[7]

    @field_decorator(index=8)
    def ScreeningType(self):
        # type: () -> str | None
        return self._values[8]

    @field_decorator(index=9)
    def NISTCompatibility(self):
        # type: () -> bool | None
        return self._values[9]

    @field_decorator(index=10)
    def PureWeightFactor(self):
        # type: () -> float | None
        return self._values[10]

    @field_decorator(index=11)
    def SearchOrder(self):
        # type: () -> int | None
        return self._values[11]

    @field_decorator(index=12)
    def RTCalibration(self):
        # type: () -> str | None
        return self._values[12]

    @field_decorator(index=13)
    def RTMatchFactorType(self):
        # type: () -> str | None
        return self._values[13]

    @field_decorator(index=14)
    def RTMaxPenalty(self):
        # type: () -> float | None
        return self._values[14]

    @field_decorator(index=15)
    def RTPenaltyType(self):
        # type: () -> str | None
        return self._values[15]

    @field_decorator(index=16)
    def RTRange(self):
        # type: () -> float | None
        return self._values[16]

    @field_decorator(index=17)
    def RTRangeNoPenalty(self):
        # type: () -> float | None
        return self._values[17]

    @field_decorator(index=18)
    def SpectrumThreshold(self):
        # type: () -> float | None
        return self._values[18]

    @field_decorator(index=19)
    def RemoveDuplicateHits(self):
        # type: () -> bool | None
        return self._values[19]

    @field_decorator(index=20)
    def AccurateMassTolerance(self):
        # type: () -> float | None
        return self._values[20]


class LibrarySearchMethodDataTable(DataTableBase[LibrarySearchMethodRow]):
    """Represents the LibrarySearchMethod table, containing LibrarySearchMethodRow objects."""

    pass


class IdentificationMethodRow(RowBase):
    """Represents a row for the IdentificationMethod table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def IdentificationMethodID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def MaxHitCount(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def MaxMZ(self):
        # type: () -> float | None
        return self._values[4]

    @field_decorator(index=5)
    def MinMatchScore(self):
        # type: () -> float | None
        return self._values[5]

    @field_decorator(index=6)
    def MinMZ(self):
        # type: () -> float | None
        return self._values[6]

    @field_decorator(index=7)
    def RatioPercentUncertainty(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def MultiLibrarySearchType(self):
        # type: () -> str | None
        return self._values[8]

    @field_decorator(index=9)
    def LibrarySearchType(self):
        # type: () -> str | None
        return self._values[9]

    @field_decorator(index=10)
    def PerformExactMass(self):
        # type: () -> bool | None
        return self._values[10]

    @field_decorator(index=11)
    def ExactMassAllowMultiplyChargedIons(self):
        # type: () -> bool | None
        return self._values[11]

    @field_decorator(index=12)
    def ExactMassMaxIonsPerSpectrum(self):
        # type: () -> int | None
        return self._values[12]

    @field_decorator(index=13)
    def ExactMassMinRelativeAbundance(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def ExactMassMZDelta(self):
        # type: () -> float | None
        return self._values[14]

    @field_decorator(index=15)
    def ExactMassMinMZDelta(self):
        # type: () -> float | None
        return self._values[15]

    @field_decorator(index=16)
    def ExactMassPeakSelectionWeighting(self):
        # type: () -> str | None
        return self._values[16]


class IdentificationMethodDataTable(DataTableBase[IdentificationMethodRow]):
    """Represents the IdentificationMethod table, containing IdentificationMethodRow objects."""

    pass


class TargetCompoundRow(RowBase):
    """Represents a row for the TargetCompound table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def CompoundID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def AgilentID(self):
        # type: () -> str | None
        return self._values[3]

    @field_decorator(index=4)
    def AverageResponseFactor(self):
        # type: () -> float | None
        return self._values[4]

    @field_decorator(index=5)
    def CASNumber(self):
        # type: () -> str | None
        return self._values[5]

    @field_decorator(index=6)
    def CellAcceleratorVoltage(self):
        # type: () -> float | None
        return self._values[6]

    @field_decorator(index=7)
    def CollisionEnergy(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def CompoundApproved(self):
        # type: () -> bool | None
        return self._values[8]

    @field_decorator(index=9)
    def CompoundGroup(self):
        # type: () -> str | None
        return self._values[9]

    @field_decorator(index=10)
    def CompoundName(self):
        # type: () -> str | None
        return self._values[10]

    @field_decorator(index=11)
    def CompoundType(self):
        # type: () -> str | None
        return self._values[11]

    @field_decorator(index=12)
    def ConcentrationUnits(self):
        # type: () -> str | None
        return self._values[12]

    @field_decorator(index=13)
    def FragmentorVoltage(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def Integrator(self):
        # type: () -> str | None
        return self._values[14]

    @field_decorator(index=15)
    def InstrumentType(self):
        # type: () -> str | None
        return self._values[15]

    @field_decorator(index=16)
    def IonPolarity(self):
        # type: () -> str | None
        return self._values[16]

    @field_decorator(index=17)
    def IonSource(self):
        # type: () -> str | None
        return self._values[17]

    @field_decorator(index=18)
    def ISTDCompoundID(self):
        # type: () -> int | None
        return self._values[18]

    @field_decorator(index=19)
    def ISTDConcentration(self):
        # type: () -> float | None
        return self._values[19]

    @field_decorator(index=20)
    def ISTDFlag(self):
        # type: () -> bool | None
        return self._values[20]

    @field_decorator(index=21)
    def KEGGID(self):
        # type: () -> str | None
        return self._values[21]

    @field_decorator(index=22)
    def LeftRetentionTimeDelta(self):
        # type: () -> float | None
        return self._values[22]

    @field_decorator(index=23)
    def LibraryMatchScore(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def MatrixSpikeConcentration(self):
        # type: () -> float | None
        return self._values[24]

    @field_decorator(index=25)
    def MolecularFormula(self):
        # type: () -> str | None
        return self._values[25]

    @field_decorator(index=26)
    def Multiplier(self):
        # type: () -> float | None
        return self._values[26]

    @field_decorator(index=27)
    def MZ(self):
        # type: () -> float | None
        return self._values[27]

    @field_decorator(index=28)
    def MZAdditional(self):
        # type: () -> str | None
        return self._values[28]

    @field_decorator(index=29)
    def MZExtractionWindowUnits(self):
        # type: () -> str | None
        return self._values[29]

    @field_decorator(index=30)
    def MZExtractionWindowFilterLeft(self):
        # type: () -> float | None
        return self._values[30]

    @field_decorator(index=31)
    def MZExtractionWindowFilterRight(self):
        # type: () -> float | None
        return self._values[31]

    @field_decorator(index=32)
    def MZScanRangeHigh(self):
        # type: () -> float | None
        return self._values[32]

    @field_decorator(index=33)
    def MZScanRangeLow(self):
        # type: () -> float | None
        return self._values[33]

    @field_decorator(index=34)
    def NoiseOfRawSignal(self):
        # type: () -> float | None
        return self._values[34]

    @field_decorator(index=35)
    def PrimaryHitPeakID(self):
        # type: () -> str | None
        return self._values[35]

    @field_decorator(index=36)
    def QuantitateByHeight(self):
        # type: () -> bool | None
        return self._values[36]

    @field_decorator(index=37)
    def ReferenceMSPathName(self):
        # type: () -> str | None
        return self._values[37]

    @field_decorator(index=38)
    def RelativeISTDMultiplier(self):
        # type: () -> float | None
        return self._values[38]

    @field_decorator(index=39)
    def RetentionTime(self):
        # type: () -> float | None
        return self._values[39]

    @field_decorator(index=40)
    def RetentionTimeDeltaUnits(self):
        # type: () -> str | None
        return self._values[40]

    @field_decorator(index=41)
    def RetentionTimeWindow(self):
        # type: () -> float | None
        return self._values[41]

    @field_decorator(index=42)
    def RetentionTimeWindowUnits(self):
        # type: () -> str | None
        return self._values[42]

    @field_decorator(index=43)
    def RightRetentionTimeDelta(self):
        # type: () -> float | None
        return self._values[43]

    @field_decorator(index=44)
    def ScanType(self):
        # type: () -> str | None
        return self._values[44]

    @field_decorator(index=45)
    def SelectedMZ(self):
        # type: () -> float | None
        return self._values[45]

    @field_decorator(index=46)
    def UncertaintyRelativeOrAbsolute(self):
        # type: () -> str | None
        return self._values[46]

    @field_decorator(index=47)
    def UserDefined(self):
        # type: () -> str | None
        return self._values[47]

    @field_decorator(index=48)
    def UserDefined1(self):
        # type: () -> str | None
        return self._values[48]

    @field_decorator(index=49)
    def UserDefined2(self):
        # type: () -> str | None
        return self._values[49]

    @field_decorator(index=50)
    def UserDefined3(self):
        # type: () -> str | None
        return self._values[50]

    @field_decorator(index=51)
    def UserDefined4(self):
        # type: () -> str | None
        return self._values[51]

    @field_decorator(index=52)
    def CompoundMath(self):
        # type: () -> str | None
        return self._values[52]

    @field_decorator(index=53)
    def UserAnnotation(self):
        # type: () -> str | None
        return self._values[53]

    @field_decorator(index=54)
    def UserCustomCalculation(self):
        # type: () -> float | None
        return self._values[54]

    @field_decorator(index=55)
    def RetentionIndex(self):
        # type: () -> float | None
        return self._values[55]

    @field_decorator(index=56)
    def ID(self):
        # type: () -> int | None
        return self._values[56]


class TargetCompoundDataTable(DataTableBase[TargetCompoundRow]):
    """Represents the TargetCompound table, containing TargetCompoundRow objects."""

    pass


class PeakRow(RowBase):
    """Represents a row for the Peak table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def CompoundID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def PeakID(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def Area(self):
        # type: () -> float | None
        return self._values[4]

    @field_decorator(index=5)
    def CalculatedConcentration(self):
        # type: () -> float | None
        return self._values[5]

    @field_decorator(index=6)
    def CoelutionScore(self):
        # type: () -> float | None
        return self._values[6]

    @field_decorator(index=7)
    def FinalConcentration(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def FullWidthHalfMaximum(self):
        # type: () -> float | None
        return self._values[8]

    @field_decorator(index=9)
    def Height(self):
        # type: () -> float | None
        return self._values[9]

    @field_decorator(index=10)
    def IntegrationMetricQualityFlags(self):
        # type: () -> str | None
        return self._values[10]

    @field_decorator(index=11)
    def IntegrationStartTime(self):
        # type: () -> float | None
        return self._values[11]

    @field_decorator(index=12)
    def IntegrationEndTime(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def Noise(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def ManuallyIntegrated(self):
        # type: () -> bool | None
        return self._values[14]

    @field_decorator(index=15)
    def MassAccuracy(self):
        # type: () -> float | None
        return self._values[15]

    @field_decorator(index=16)
    def MassMatchScore(self):
        # type: () -> float | None
        return self._values[16]

    @field_decorator(index=17)
    def MatrixSpikePercentRecovery(self):
        # type: () -> float | None
        return self._values[17]

    @field_decorator(index=18)
    def MZ(self):
        # type: () -> float | None
        return self._values[18]

    @field_decorator(index=19)
    def Plates(self):
        # type: () -> int | None
        return self._values[19]

    @field_decorator(index=20)
    def QValueComputed(self):
        # type: () -> int | None
        return self._values[20]

    @field_decorator(index=21)
    def RetentionIndex(self):
        # type: () -> float | None
        return self._values[21]

    @field_decorator(index=22)
    def RetentionTime(self):
        # type: () -> float | None
        return self._values[22]

    @field_decorator(index=23)
    def RetentionTimeDifference(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def ResolutionFront(self):
        # type: () -> float | None
        return self._values[24]

    @field_decorator(index=25)
    def ResolutionRear(self):
        # type: () -> float | None
        return self._values[25]

    @field_decorator(index=26)
    def SaturationRecoveryRatio(self):
        # type: () -> float | None
        return self._values[26]

    @field_decorator(index=27)
    def SignalToNoiseRatio(self):
        # type: () -> float | None
        return self._values[27]

    @field_decorator(index=28)
    def SurrogatePercentRecovery(self):
        # type: () -> float | None
        return self._values[28]

    @field_decorator(index=29)
    def Symmetry(self):
        # type: () -> float | None
        return self._values[29]

    @field_decorator(index=30)
    def TargetResponse(self):
        # type: () -> float | None
        return self._values[30]

    @field_decorator(index=31)
    def UserCustomCalculation(self):
        # type: () -> float | None
        return self._values[31]

    @field_decorator(index=32)
    def UserCustomCalculation1(self):
        # type: () -> float | None
        return self._values[32]

    @field_decorator(index=33)
    def UserCustomCalculation2(self):
        # type: () -> float | None
        return self._values[33]

    @field_decorator(index=34)
    def UserCustomCalculation3(self):
        # type: () -> float | None
        return self._values[34]

    @field_decorator(index=35)
    def UserCustomCalculation4(self):
        # type: () -> float | None
        return self._values[35]

    @field_decorator(index=36)
    def Width(self):
        # type: () -> float | None
        return self._values[36]

    @field_decorator(index=37)
    def ReferenceLibraryMatchScore(self):
        # type: () -> float | None
        return self._values[37]

    @field_decorator(index=38)
    def Purity(self):
        # type: () -> float | None
        return self._values[38]


class PeakDataTable(DataTableBase[PeakRow]):
    """Represents the Peak table, containing PeakRow objects."""

    pass


class TargetQualifierRow(RowBase):
    """Represents a row for the TargetQualifier table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def CompoundID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def QualifierID(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def CollisionEnergy(self):
        # type: () -> float | None
        return self._values[4]

    @field_decorator(index=5)
    def FragmentorVoltage(self):
        # type: () -> float | None
        return self._values[5]

    @field_decorator(index=6)
    def MZ(self):
        # type: () -> float | None
        return self._values[6]

    @field_decorator(index=7)
    def MZExtractionWindowUnits(self):
        # type: () -> str | None
        return self._values[7]

    @field_decorator(index=8)
    def MZExtractionWindowFilterLeft(self):
        # type: () -> float | None
        return self._values[8]

    @field_decorator(index=9)
    def MZExtractionWindowFilterRight(self):
        # type: () -> float | None
        return self._values[9]

    @field_decorator(index=10)
    def RelativeResponse(self):
        # type: () -> float | None
        return self._values[10]

    @field_decorator(index=11)
    def SelectedMZ(self):
        # type: () -> float | None
        return self._values[11]

    @field_decorator(index=12)
    def Uncertainty(self):
        # type: () -> float | None
        return self._values[12]


class TargetQualifierDataTable(DataTableBase[TargetQualifierRow]):
    """Represents the TargetQualifier table, containing TargetQualifierRow objects."""

    pass


class PeakQualifierRow(RowBase):
    """Represents a row for the PeakQualifier table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def CompoundID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def QualifierID(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def PeakID(self):
        # type: () -> int | None
        return self._values[4]

    @field_decorator(index=5)
    def Area(self):
        # type: () -> float | None
        return self._values[5]

    @field_decorator(index=6)
    def FullWidthHalfMaximum(self):
        # type: () -> float | None
        return self._values[6]

    @field_decorator(index=7)
    def Height(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def Noise(self):
        # type: () -> str | None
        return self._values[8]

    @field_decorator(index=9)
    def ManuallyIntegrated(self):
        # type: () -> bool | None
        return self._values[9]

    @field_decorator(index=10)
    def QualifierResponseRatio(self):
        # type: () -> float | None
        return self._values[10]

    @field_decorator(index=11)
    def RetentionTime(self):
        # type: () -> float | None
        return self._values[11]

    @field_decorator(index=12)
    def SignalToNoiseRatio(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def Symmetry(self):
        # type: () -> float | None
        return self._values[13]


class PeakQualifierDataTable(DataTableBase[PeakQualifierRow]):
    """Represents the PeakQualifier table, containing PeakQualifierRow objects."""

    pass


class AnalysisRow(RowBase):
    """Represents a row for the Analysis table."""

    @field_decorator(index=0)
    def AnalysisID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SchemaVersion(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def AnalystName(self):
        # type: () -> str | None
        return self._values[2]

    @field_decorator(index=3)
    def AnalysisTime(self):
        # type: () -> datetime.datetime | None
        return self._values[3]

    @field_decorator(index=4)
    def DataVersion(self):
        # type: () -> int | None
        return self._values[4]

    @field_decorator(index=5)
    def ReportTime(self):
        # type: () -> datetime.datetime | None
        return self._values[5]

    @field_decorator(index=6)
    def StoreResultsPerSample(self):
        # type: () -> bool | None
        return self._values[6]

    @field_decorator(index=7)
    def AppVersion(self):
        # type: () -> str | None
        return self._values[7]

    @field_decorator(index=8)
    def BatchPath(self):
        # type: () -> str | None
        return self._values[8]

    @field_decorator(index=9)
    def AnalysisFileName(self):
        # type: () -> str | None
        return self._values[9]


class AnalysisDataTable(DataTableBase[AnalysisRow]):
    """Represents the Analysis table, containing AnalysisRow objects."""

    pass


class TargetMatchMethodRow(RowBase):
    """Represents a row for the TargetMatchMethod table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def TargetMatchMethodID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def TargetFinalConcentrationRequired(self):
        # type: () -> bool | None
        return self._values[3]

    @field_decorator(index=4)
    def TargetResponseRequired(self):
        # type: () -> bool | None
        return self._values[4]

    @field_decorator(index=5)
    def TargetQualifierIonRatiosWithinRangeRequired(self):
        # type: () -> bool | None
        return self._values[5]

    @field_decorator(index=6)
    def TargetQualifierIonRequired(self):
        # type: () -> bool | None
        return self._values[6]

    @field_decorator(index=7)
    def HitContainsQuantifierIon(self):
        # type: () -> bool | None
        return self._values[7]

    @field_decorator(index=8)
    def HitContainsQualifierIons(self):
        # type: () -> bool | None
        return self._values[8]

    @field_decorator(index=9)
    def HitQualifierRatioWithinRange(self):
        # type: () -> bool | None
        return self._values[9]

    @field_decorator(index=10)
    def HitWithinTargetRTWindow(self):
        # type: () -> bool | None
        return self._values[10]

    @field_decorator(index=11)
    def ManualResponseFactor(self):
        # type: () -> float | None
        return self._values[11]

    @field_decorator(index=12)
    def MatchCompoundName(self):
        # type: () -> bool | None
        return self._values[12]

    @field_decorator(index=13)
    def MatchCASNumber(self):
        # type: () -> bool | None
        return self._values[13]

    @field_decorator(index=14)
    def HitConcentrationEstimation(self):
        # type: () -> str | None
        return self._values[14]


class TargetMatchMethodDataTable(DataTableBase[TargetMatchMethodRow]):
    """Represents the TargetMatchMethod table, containing TargetMatchMethodRow objects."""

    pass


class AuxiliaryMethodRow(RowBase):
    """Represents a row for the AuxiliaryMethod table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def MZExtractIons(self):
        # type: () -> str | None
        return self._values[2]

    @field_decorator(index=3)
    def MZExtractionWindowFilterLeft(self):
        # type: () -> float | None
        return self._values[3]

    @field_decorator(index=4)
    def MZExtractionWindowFilterRight(self):
        # type: () -> float | None
        return self._values[4]

    @field_decorator(index=5)
    def MZExtractionWindowUnits(self):
        # type: () -> str | None
        return self._values[5]


class AuxiliaryMethodDataTable(DataTableBase[AuxiliaryMethodRow]):
    """Represents the AuxiliaryMethod table, containing AuxiliaryMethodRow objects."""

    pass


class BlankSubtractionMethodRow(RowBase):
    """Represents a row for the BlankSubtractionMethod table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def BlankSubtractionMethodID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def PerformBlankSubtraction(self):
        # type: () -> bool | None
        return self._values[3]

    @field_decorator(index=4)
    def PeakThresholdType(self):
        # type: () -> str | None
        return self._values[4]

    @field_decorator(index=5)
    def PeakThreshold(self):
        # type: () -> float | None
        return self._values[5]

    @field_decorator(index=6)
    def RTWindowType(self):
        # type: () -> str | None
        return self._values[6]

    @field_decorator(index=7)
    def RTWindow(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def RTWindowFWHM(self):
        # type: () -> float | None
        return self._values[8]


class BlankSubtractionMethodDataTable(DataTableBase[BlankSubtractionMethodRow]):
    """Represents the BlankSubtractionMethod table, containing BlankSubtractionMethodRow objects."""

    pass


class ExactMassRow(RowBase):
    """Represents a row for the ExactMass table."""

    @field_decorator(index=0)
    def BatchID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def SampleID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def DeconvolutionMethodID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def ComponentID(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def HitID(self):
        # type: () -> int | None
        return self._values[4]

    @field_decorator(index=5)
    def ExactMassID(self):
        # type: () -> int | None
        return self._values[5]

    @field_decorator(index=6)
    def MassSource(self):
        # type: () -> float | None
        return self._values[6]

    @field_decorator(index=7)
    def MassExact(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def MassDeltaPpm(self):
        # type: () -> float | None
        return self._values[8]

    @field_decorator(index=9)
    def MassDeltaMda(self):
        # type: () -> float | None
        return self._values[9]

    @field_decorator(index=10)
    def FragmentFormula(self):
        # type: () -> str | None
        return self._values[10]

    @field_decorator(index=11)
    def Abundance(self):
        # type: () -> float | None
        return self._values[11]

    @field_decorator(index=12)
    def RelativeAbundance(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def Charge(self):
        # type: () -> int | None
        return self._values[13]

    @field_decorator(index=14)
    def IsUnique(self):
        # type: () -> bool | None
        return self._values[14]


class ExactMassDataTable(DataTableBase[ExactMassRow]):
    """Represents the ExactMass table, containing ExactMassRow objects."""

    pass


ProcessedColumns = (
    ComponentRow.SampleID,
    ComponentRow.StartX,
    ComponentRow.RetentionTime,
    ComponentRow.EndX,
    HitRow.CompoundName,
    HitRow.CASNumber,
    HitRow.Formula,
    HitRow.LibraryMatchScore,
    HitRow.MolecularWeight,
    ComponentRow.Area,
    ComponentRow.Height,
    HitRow.EstimatedConcentration,
)


class DataTables(DataTablesBase):
    @table_property(BatchDataTable)
    def Batch(self):
        pass

    @table_property(SampleDataTable)
    def Sample(self):
        pass

    @table_property(ComponentDataTable)
    def Component(self):
        pass

    @table_property(HitDataTable)
    def Hit(self):
        pass

    @table_property(IonPeakDataTable)
    def IonPeak(self):
        pass

    @table_property(DeconvolutionMethodDataTable)
    def DeconvolutionMethod(self):
        pass

    @table_property(LibrarySearchMethodDataTable)
    def LibrarySearchMethod(self):
        pass

    @table_property(IdentificationMethodDataTable)
    def IdentificationMethod(self):
        pass

    @table_property(TargetCompoundDataTable)
    def TargetCompound(self):
        pass

    @table_property(PeakDataTable)
    def Peak(self):
        pass

    @table_property(TargetQualifierDataTable)
    def TargetQualifier(self):
        pass

    @table_property(PeakQualifierDataTable)
    def PeakQualifier(self):
        pass

    @table_property(AnalysisDataTable)
    def Analysis(self):
        pass

    @table_property(TargetMatchMethodDataTable)
    def TargetMatchMethod(self):
        pass

    @table_property(AuxiliaryMethodDataTable)
    def AuxiliaryMethod(self):
        pass

    @table_property(BlankSubtractionMethodDataTable)
    def BlankSubtractionMethod(self):
        pass

    @table_property(ExactMassDataTable)
    def ExactMass(self):
        pass

    def ComponentsWithBestPrimaryHit(self, batch_id=0, sample_id=None):
        # type: (int, int) -> dict
        component_table = self.Component
        hit_table = self.Hit

        component_table_keys = [
            "BatchID",
            "SampleID",
            "DeconvolutionMethodID",
            "ComponentID",
        ]
        hit_table_keys = component_table_keys + ["HitID"]
        hit_table_index = {
            k: r for r, k in enumerate(zip(*[hit_table[c] for c in hit_table_keys]))
        }

        component_rows, hit_rows = zip(
            *[
                (r, hit_table_index[(bid, sid, did, cid, hid)])
                # each row in component table
                for r, (bid, sid, did, cid, hid, ok) in enumerate(
                    zip(
                        *[
                            component_table[c]
                            for c in component_table_keys + ["PrimaryHitID", "BestHit"]
                        ]
                    )
                )
                # only selected batch/sample and best primary hit
                if ok and bid == batch_id and (sample_id is None or sid == sample_id)
            ]
        )

        components_with_best_primary_hit = {
            k: [v[r] for r in component_rows] for k, v in component_table.items()
        }
        components_with_best_primary_hit.update(
            **{
                k: [v[r] for r in hit_rows]
                for k, v in hit_table.items()
                if k not in hit_table_keys
            }
        )
        return components_with_best_primary_hit

    def to_json(self, processed=False):
        # type: (bool) -> str
        backup_tables = self.tables
        popped_table = None
        try:
            if processed:
                columns = [c.fget.__name__ for c in ProcessedColumns]
                popped_table = self.ComponentsWithBestPrimaryHit()

                self.tables = {
                    "ComponentsWithBestPrimaryHit": dict(
                        (k, popped_table[k]) for k in columns if k in popped_table
                    )
                }
            else:
                popped_table = self.tables.pop("ComponentsWithBestPrimaryHit", {})
            return super(DataTables, self).to_json()
        finally:
            self.tables = backup_tables
            if not popped_table:
                self.tables["ComponentsWithBestPrimaryHit"] = popped_table
