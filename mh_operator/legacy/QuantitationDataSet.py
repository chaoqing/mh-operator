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

from mh_operator.legacy.common import DataTableBase, RowBase, field_decorator


class BatchRow(RowBase):
    """Represents a row for the Batch table."""

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
    def BalanceOverride(self):
        # type: () -> str | None
        return self._values[7]

    @field_decorator(index=8)
    def Barcode(self):
        # type: () -> str | None
        return self._values[8]

    @field_decorator(index=9)
    def CalibrationReferenceSampleID(self):
        # type: () -> int | None
        return self._values[9]

    @field_decorator(index=10)
    def Comment(self):
        # type: () -> str | None
        return self._values[10]

    @field_decorator(index=11)
    def Completed(self):
        # type: () -> bool | None
        return self._values[11]

    @field_decorator(index=12)
    def DADateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[12]

    @field_decorator(index=13)
    def DAMethodFileName(self):
        # type: () -> str | None
        return self._values[13]

    @field_decorator(index=14)
    def DAMethodPathName(self):
        # type: () -> str | None
        return self._values[14]

    @field_decorator(index=15)
    def DataFileName(self):
        # type: () -> str | None
        return self._values[15]

    @field_decorator(index=16)
    def DataPathName(self):
        # type: () -> str | None
        return self._values[16]

    @field_decorator(index=17)
    def Dilution(self):
        # type: () -> float | None
        return self._values[17]

    @field_decorator(index=18)
    def DualInjector(self):
        # type: () -> bool | None
        return self._values[18]

    @field_decorator(index=19)
    def DualInjectorAcqDateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[19]

    @field_decorator(index=20)
    def DualInjectorBarcode(self):
        # type: () -> str | None
        return self._values[20]

    @field_decorator(index=21)
    def DualInjectorExpectedBarcode(self):
        # type: () -> str | None
        return self._values[21]

    @field_decorator(index=22)
    def DualInjectorVial(self):
        # type: () -> int | None
        return self._values[22]

    @field_decorator(index=23)
    def DualInjectorVolume(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def EquilibrationTime(self):
        # type: () -> float | None
        return self._values[24]

    @field_decorator(index=25)
    def ExpectedBarcode(self):
        # type: () -> str | None
        return self._values[25]

    @field_decorator(index=26)
    def GraphicSampleChromatogram(self):
        # type: () -> str | None
        return self._values[26]

    @field_decorator(index=27)
    def InjectionsPerPosition(self):
        # type: () -> int | None
        return self._values[27]

    @field_decorator(index=28)
    def InjectorVolume(self):
        # type: () -> float | None
        return self._values[28]

    @field_decorator(index=29)
    def InstrumentName(self):
        # type: () -> str | None
        return self._values[29]

    @field_decorator(index=30)
    def InstrumentType(self):
        # type: () -> str | None
        return self._values[30]

    @field_decorator(index=31)
    def ISTDDilution(self):
        # type: () -> float | None
        return self._values[31]

    @field_decorator(index=32)
    def LevelName(self):
        # type: () -> str | None
        return self._values[32]

    @field_decorator(index=33)
    def Locked(self):
        # type: () -> bool | None
        return self._values[33]

    @field_decorator(index=34)
    def MatrixSpikeDilution(self):
        # type: () -> float | None
        return self._values[34]

    @field_decorator(index=35)
    def MatrixSpikeGroup(self):
        # type: () -> str | None
        return self._values[35]

    @field_decorator(index=36)
    def MatrixType(self):
        # type: () -> str | None
        return self._values[36]

    @field_decorator(index=37)
    def OutlierCCTime(self):
        # type: () -> str | None
        return self._values[37]

    @field_decorator(index=38)
    def PlateCode(self):
        # type: () -> str | None
        return self._values[38]

    @field_decorator(index=39)
    def PlatePosition(self):
        # type: () -> str | None
        return self._values[39]

    @field_decorator(index=40)
    def QuantitationMessage(self):
        # type: () -> str | None
        return self._values[40]

    @field_decorator(index=41)
    def RackCode(self):
        # type: () -> str | None
        return self._values[41]

    @field_decorator(index=42)
    def RackPosition(self):
        # type: () -> str | None
        return self._values[42]

    @field_decorator(index=43)
    def RunStartValvePositionDescription(self):
        # type: () -> str | None
        return self._values[43]

    @field_decorator(index=44)
    def RunStartValvePositionNumber(self):
        # type: () -> str | None
        return self._values[44]

    @field_decorator(index=45)
    def RunStopValvePositionDescription(self):
        # type: () -> str | None
        return self._values[45]

    @field_decorator(index=46)
    def RunStopValvePositionNumber(self):
        # type: () -> str | None
        return self._values[46]

    @field_decorator(index=47)
    def SampleAmount(self):
        # type: () -> float | None
        return self._values[47]

    @field_decorator(index=48)
    def SampleApproved(self):
        # type: () -> bool | None
        return self._values[48]

    @field_decorator(index=49)
    def SampleGroup(self):
        # type: () -> str | None
        return self._values[49]

    @field_decorator(index=50)
    def SampleInformation(self):
        # type: () -> str | None
        return self._values[50]

    @field_decorator(index=51)
    def SampleName(self):
        # type: () -> str | None
        return self._values[51]

    @field_decorator(index=52)
    def SamplePosition(self):
        # type: () -> str | None
        return self._values[52]

    @field_decorator(index=53)
    def SamplePrepFileName(self):
        # type: () -> str | None
        return self._values[53]

    @field_decorator(index=54)
    def SamplePrepPathName(self):
        # type: () -> str | None
        return self._values[54]

    @field_decorator(index=55)
    def SampleType(self):
        # type: () -> str | None
        return self._values[55]

    @field_decorator(index=56)
    def SamplingDateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[56]

    @field_decorator(index=57)
    def SamplingTime(self):
        # type: () -> float | None
        return self._values[57]

    @field_decorator(index=58)
    def SequenceFileName(self):
        # type: () -> str | None
        return self._values[58]

    @field_decorator(index=59)
    def SequencePathName(self):
        # type: () -> str | None
        return self._values[59]

    @field_decorator(index=60)
    def SurrogateDilution(self):
        # type: () -> float | None
        return self._values[60]

    @field_decorator(index=61)
    def TotalSampleAmount(self):
        # type: () -> float | None
        return self._values[61]

    @field_decorator(index=62)
    def TuneFileLastTimeStamp(self):
        # type: () -> datetime.datetime | None
        return self._values[62]

    @field_decorator(index=63)
    def TuneFileName(self):
        # type: () -> str | None
        return self._values[63]

    @field_decorator(index=64)
    def TunePathName(self):
        # type: () -> str | None
        return self._values[64]

    @field_decorator(index=65)
    def TrayName(self):
        # type: () -> str | None
        return self._values[65]

    @field_decorator(index=66)
    def UserDefined(self):
        # type: () -> str | None
        return self._values[66]

    @field_decorator(index=67)
    def UserDefined1(self):
        # type: () -> str | None
        return self._values[67]

    @field_decorator(index=68)
    def UserDefined2(self):
        # type: () -> str | None
        return self._values[68]

    @field_decorator(index=69)
    def UserDefined3(self):
        # type: () -> str | None
        return self._values[69]

    @field_decorator(index=70)
    def UserDefined4(self):
        # type: () -> str | None
        return self._values[70]

    @field_decorator(index=71)
    def UserDefined5(self):
        # type: () -> str | None
        return self._values[71]

    @field_decorator(index=72)
    def UserDefined6(self):
        # type: () -> str | None
        return self._values[72]

    @field_decorator(index=73)
    def UserDefined7(self):
        # type: () -> str | None
        return self._values[73]

    @field_decorator(index=74)
    def UserDefined8(self):
        # type: () -> str | None
        return self._values[74]

    @field_decorator(index=75)
    def UserDefined9(self):
        # type: () -> str | None
        return self._values[75]

    @field_decorator(index=76)
    def Vial(self):
        # type: () -> int | None
        return self._values[76]


class BatchDataTable(DataTableBase[BatchRow]):
    """Represents the Batch table, containing BatchRow objects."""

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
    def AccuracyLimitMultiplierLOQ(self):
        # type: () -> float | None
        return self._values[3]

    @field_decorator(index=4)
    def AccuracyMaximumPercentDeviation(self):
        # type: () -> float | None
        return self._values[4]

    @field_decorator(index=5)
    def AgilentID(self):
        # type: () -> str | None
        return self._values[5]

    @field_decorator(index=6)
    def AlternativePeakCriteria(self):
        # type: () -> str | None
        return self._values[6]

    @field_decorator(index=7)
    def AlternativePeakID(self):
        # type: () -> int | None
        return self._values[7]

    @field_decorator(index=8)
    def AreaCorrectionFactor(self):
        # type: () -> float | None
        return self._values[8]

    @field_decorator(index=9)
    def AreaCorrectionSelectedMZ(self):
        # type: () -> float | None
        return self._values[9]

    @field_decorator(index=10)
    def AreaCorrectionMZ(self):
        # type: () -> float | None
        return self._values[10]

    @field_decorator(index=11)
    def AverageRelativeRetentionTime(self):
        # type: () -> float | None
        return self._values[11]

    @field_decorator(index=12)
    def AverageResponseFactor(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def AverageResponseFactorRSD(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def BlankResponseOffset(self):
        # type: () -> float | None
        return self._values[14]

    @field_decorator(index=15)
    def CalibrationRangeFilter(self):
        # type: () -> str | None
        return self._values[15]

    @field_decorator(index=16)
    def CalibrationReferenceCompoundID(self):
        # type: () -> int | None
        return self._values[16]

    @field_decorator(index=17)
    def CapacityFactorLimit(self):
        # type: () -> float | None
        return self._values[17]

    @field_decorator(index=18)
    def CASNumber(self):
        # type: () -> str | None
        return self._values[18]

    @field_decorator(index=19)
    def CCISTDResponseRatioLimitHigh(self):
        # type: () -> float | None
        return self._values[19]

    @field_decorator(index=20)
    def CCISTDResponseRatioLimitLow(self):
        # type: () -> float | None
        return self._values[20]

    @field_decorator(index=21)
    def CCResponseRatioLimitHigh(self):
        # type: () -> float | None
        return self._values[21]

    @field_decorator(index=22)
    def CCResponseRatioLimitLow(self):
        # type: () -> float | None
        return self._values[22]

    @field_decorator(index=23)
    def CellAcceleratorVoltage(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def CoelutionScoreLimit(self):
        # type: () -> float | None
        return self._values[24]

    @field_decorator(index=25)
    def CollisionEnergy(self):
        # type: () -> float | None
        return self._values[25]

    @field_decorator(index=26)
    def CollisionEnergyDelta(self):
        # type: () -> float | None
        return self._values[26]

    @field_decorator(index=27)
    def ColumnVoidTime(self):
        # type: () -> float | None
        return self._values[27]

    @field_decorator(index=28)
    def CompoundApproved(self):
        # type: () -> bool | None
        return self._values[28]

    @field_decorator(index=29)
    def CompoundGroup(self):
        # type: () -> str | None
        return self._values[29]

    @field_decorator(index=30)
    def CompoundMath(self):
        # type: () -> str | None
        return self._values[30]

    @field_decorator(index=31)
    def CompoundName(self):
        # type: () -> str | None
        return self._values[31]

    @field_decorator(index=32)
    def CompoundType(self):
        # type: () -> str | None
        return self._values[32]

    @field_decorator(index=33)
    def ConcentrationUnits(self):
        # type: () -> str | None
        return self._values[33]

    @field_decorator(index=34)
    def CurveFit(self):
        # type: () -> str | None
        return self._values[34]

    @field_decorator(index=35)
    def CurveFitFormula(self):
        # type: () -> str | None
        return self._values[35]

    @field_decorator(index=36)
    def CurveFitLimitHigh(self):
        # type: () -> float | None
        return self._values[36]

    @field_decorator(index=37)
    def CurveFitLimitLow(self):
        # type: () -> float | None
        return self._values[37]

    @field_decorator(index=38)
    def CurveFitMinimumR2(self):
        # type: () -> float | None
        return self._values[38]

    @field_decorator(index=39)
    def CurveFitOrigin(self):
        # type: () -> str | None
        return self._values[39]

    @field_decorator(index=40)
    def CurveFitR2(self):
        # type: () -> float | None
        return self._values[40]

    @field_decorator(index=41)
    def CurveFitStatus(self):
        # type: () -> str | None
        return self._values[41]

    @field_decorator(index=42)
    def CurveFitWeight(self):
        # type: () -> str | None
        return self._values[42]

    @field_decorator(index=43)
    def DilutionHighestConcentration(self):
        # type: () -> float | None
        return self._values[43]

    @field_decorator(index=44)
    def DilutionPattern(self):
        # type: () -> str | None
        return self._values[44]

    @field_decorator(index=45)
    def DynamicTargetCompoundID(self):
        # type: () -> int | None
        return self._values[45]

    @field_decorator(index=46)
    def DynamicTargetRank(self):
        # type: () -> int | None
        return self._values[46]

    @field_decorator(index=47)
    def ExpectedConcentration(self):
        # type: () -> float | None
        return self._values[47]

    @field_decorator(index=48)
    def FragmentorVoltage(self):
        # type: () -> float | None
        return self._values[48]

    @field_decorator(index=49)
    def FragmentorVoltageDelta(self):
        # type: () -> float | None
        return self._values[49]

    @field_decorator(index=50)
    def FullWidthHalfMaximumLimitHigh(self):
        # type: () -> float | None
        return self._values[50]

    @field_decorator(index=51)
    def FullWidthHalfMaximumLimitLow(self):
        # type: () -> float | None
        return self._values[51]

    @field_decorator(index=52)
    def GraphicPeakChromatogram(self):
        # type: () -> str | None
        return self._values[52]

    @field_decorator(index=53)
    def GraphicPeakQualifiers(self):
        # type: () -> str | None
        return self._values[53]

    @field_decorator(index=54)
    def GraphicPeakSpectrum(self):
        # type: () -> str | None
        return self._values[54]

    @field_decorator(index=55)
    def GraphicTargetCompoundCalibration(self):
        # type: () -> str | None
        return self._values[55]

    @field_decorator(index=56)
    def ID(self):
        # type: () -> int | None
        return self._values[56]

    @field_decorator(index=57)
    def IntegrationParameters(self):
        # type: () -> str | None
        return self._values[57]

    @field_decorator(index=58)
    def IntegrationParametersModified(self):
        # type: () -> bool | None
        return self._values[58]

    @field_decorator(index=59)
    def Integrator(self):
        # type: () -> str | None
        return self._values[59]

    @field_decorator(index=60)
    def IonPolarity(self):
        # type: () -> str | None
        return self._values[60]

    @field_decorator(index=61)
    def IonSource(self):
        # type: () -> str | None
        return self._values[61]

    @field_decorator(index=62)
    def ISTDCompoundID(self):
        # type: () -> int | None
        return self._values[62]

    @field_decorator(index=63)
    def ISTDConcentration(self):
        # type: () -> float | None
        return self._values[63]

    @field_decorator(index=64)
    def ISTDFlag(self):
        # type: () -> bool | None
        return self._values[64]

    @field_decorator(index=65)
    def ISTDResponseLimitHigh(self):
        # type: () -> float | None
        return self._values[65]

    @field_decorator(index=66)
    def ISTDResponseLimitLow(self):
        # type: () -> float | None
        return self._values[66]

    @field_decorator(index=67)
    def ISTDResponseMaximumPercentDeviation(self):
        # type: () -> float | None
        return self._values[67]

    @field_decorator(index=68)
    def ISTDResponseMinimumPercentDeviation(self):
        # type: () -> float | None
        return self._values[68]

    @field_decorator(index=69)
    def KEGGID(self):
        # type: () -> str | None
        return self._values[69]

    @field_decorator(index=70)
    def LeftRetentionTimeDelta(self):
        # type: () -> float | None
        return self._values[70]

    @field_decorator(index=71)
    def LibraryMatchScore(self):
        # type: () -> float | None
        return self._values[71]

    @field_decorator(index=72)
    def LibraryMatchScoreMinimum(self):
        # type: () -> float | None
        return self._values[72]

    @field_decorator(index=73)
    def LibraryRetentionIndex(self):
        # type: () -> float | None
        return self._values[73]

    @field_decorator(index=74)
    def LibraryRetentionTime(self):
        # type: () -> float | None
        return self._values[74]

    @field_decorator(index=75)
    def LimitOfDetection(self):
        # type: () -> float | None
        return self._values[75]

    @field_decorator(index=76)
    def LimitOfQuantitation(self):
        # type: () -> float | None
        return self._values[76]

    @field_decorator(index=77)
    def LinearResponseRangeMax(self):
        # type: () -> float | None
        return self._values[77]

    @field_decorator(index=78)
    def LinearResponseRangeMin(self):
        # type: () -> float | None
        return self._values[78]

    @field_decorator(index=79)
    def MassAccuracyLimit(self):
        # type: () -> float | None
        return self._values[79]

    @field_decorator(index=80)
    def MassMatchScoreMinimum(self):
        # type: () -> float | None
        return self._values[80]

    @field_decorator(index=81)
    def MatrixAConcentrationLimitHigh(self):
        # type: () -> float | None
        return self._values[81]

    @field_decorator(index=82)
    def MatrixAConcentrationLimitLow(self):
        # type: () -> float | None
        return self._values[82]

    @field_decorator(index=83)
    def MatrixBConcentrationLimitHigh(self):
        # type: () -> float | None
        return self._values[83]

    @field_decorator(index=84)
    def MatrixBConcentrationLimitLow(self):
        # type: () -> float | None
        return self._values[84]

    @field_decorator(index=85)
    def MatrixSpikeBConcentration(self):
        # type: () -> float | None
        return self._values[85]

    @field_decorator(index=86)
    def MatrixSpikeBPercentRecoveryMaximum(self):
        # type: () -> float | None
        return self._values[86]

    @field_decorator(index=87)
    def MatrixSpikeBPercentRecoveryMinimum(self):
        # type: () -> float | None
        return self._values[87]

    @field_decorator(index=88)
    def MatrixSpikeConcentration(self):
        # type: () -> float | None
        return self._values[88]

    @field_decorator(index=89)
    def MatrixSpikeMaximumPercentDeviation(self):
        # type: () -> float | None
        return self._values[89]

    @field_decorator(index=90)
    def MatrixSpikeBMaximumPercentDeviation(self):
        # type: () -> float | None
        return self._values[90]

    @field_decorator(index=91)
    def MatrixSpikePercentRecoveryMaximum(self):
        # type: () -> float | None
        return self._values[91]

    @field_decorator(index=92)
    def MatrixSpikePercentRecoveryMinimum(self):
        # type: () -> float | None
        return self._values[92]

    @field_decorator(index=93)
    def MatrixTypeOverride(self):
        # type: () -> str | None
        return self._values[93]

    @field_decorator(index=94)
    def MaximumAverageResponseFactorRSD(self):
        # type: () -> float | None
        return self._values[94]

    @field_decorator(index=95)
    def MaximumBlankConcentration(self):
        # type: () -> float | None
        return self._values[95]

    @field_decorator(index=96)
    def MaximumBlankResponse(self):
        # type: () -> float | None
        return self._values[96]

    @field_decorator(index=97)
    def MaximumCCResponseFactorDeviation(self):
        # type: () -> float | None
        return self._values[97]

    @field_decorator(index=98)
    def MaximumNumberOfHits(self):
        # type: () -> int | None
        return self._values[98]

    @field_decorator(index=99)
    def MaximumPercentResidual(self):
        # type: () -> float | None
        return self._values[99]

    @field_decorator(index=100)
    def MethodDetectionLimit(self):
        # type: () -> float | None
        return self._values[100]

    @field_decorator(index=101)
    def MinimumAverageResponseFactor(self):
        # type: () -> float | None
        return self._values[101]

    @field_decorator(index=102)
    def MinimumCCRelativeResponseFactor(self):
        # type: () -> float | None
        return self._values[102]

    @field_decorator(index=103)
    def MinimumPercentPurity(self):
        # type: () -> float | None
        return self._values[103]

    @field_decorator(index=104)
    def MinimumSignalToNoiseRatio(self):
        # type: () -> float | None
        return self._values[104]

    @field_decorator(index=105)
    def MolecularFormula(self):
        # type: () -> str | None
        return self._values[105]

    @field_decorator(index=106)
    def Multiplier(self):
        # type: () -> float | None
        return self._values[106]

    @field_decorator(index=107)
    def MZ(self):
        # type: () -> float | None
        return self._values[107]

    @field_decorator(index=108)
    def MZAdditional(self):
        # type: () -> str | None
        return self._values[108]

    @field_decorator(index=109)
    def MZExtractionWindowFilterLeft(self):
        # type: () -> float | None
        return self._values[109]

    @field_decorator(index=110)
    def MZExtractionWindowFilterRight(self):
        # type: () -> float | None
        return self._values[110]

    @field_decorator(index=111)
    def MZExtractionWindowUnits(self):
        # type: () -> str | None
        return self._values[111]

    @field_decorator(index=112)
    def MZScanRangeHigh(self):
        # type: () -> float | None
        return self._values[112]

    @field_decorator(index=113)
    def MZScanRangeLow(self):
        # type: () -> float | None
        return self._values[113]

    @field_decorator(index=114)
    def NeutralLossGain(self):
        # type: () -> float | None
        return self._values[114]

    @field_decorator(index=115)
    def NoiseAlgorithmType(self):
        # type: () -> str | None
        return self._values[115]

    @field_decorator(index=116)
    def NoiseOfRawSignal(self):
        # type: () -> float | None
        return self._values[116]

    @field_decorator(index=117)
    def NoiseReference(self):
        # type: () -> str | None
        return self._values[117]

    @field_decorator(index=118)
    def NoiseRegions(self):
        # type: () -> str | None
        return self._values[118]

    @field_decorator(index=119)
    def NoiseStandardDeviationMultiplier(self):
        # type: () -> float | None
        return self._values[119]

    @field_decorator(index=120)
    def NonReferenceWindowOverride(self):
        # type: () -> float | None
        return self._values[120]

    @field_decorator(index=121)
    def OutlierAlternativePeak(self):
        # type: () -> str | None
        return self._values[121]

    @field_decorator(index=122)
    def OutlierAverageResponseFactor(self):
        # type: () -> str | None
        return self._values[122]

    @field_decorator(index=123)
    def OutlierAverageResponseFactorRSD(self):
        # type: () -> str | None
        return self._values[123]

    @field_decorator(index=124)
    def OutlierBlankResponseOutsideLimit(self):
        # type: () -> str | None
        return self._values[124]

    @field_decorator(index=125)
    def OutlierCCAverageResponseFactor(self):
        # type: () -> str | None
        return self._values[125]

    @field_decorator(index=126)
    def OutlierCCRelativeResponseFactor(self):
        # type: () -> str | None
        return self._values[126]

    @field_decorator(index=127)
    def OutlierCustomCalculation(self):
        # type: () -> str | None
        return self._values[127]

    @field_decorator(index=128)
    def OutlierMethodDetectionLimit(self):
        # type: () -> str | None
        return self._values[128]

    @field_decorator(index=129)
    def OutlierMinimumCurveFitR2(self):
        # type: () -> str | None
        return self._values[129]

    @field_decorator(index=130)
    def OutlierPeakNotFound(self):
        # type: () -> str | None
        return self._values[130]

    @field_decorator(index=131)
    def OutlierRelativeResponseFactor(self):
        # type: () -> str | None
        return self._values[131]

    @field_decorator(index=132)
    def OutlierRelativeStandardError(self):
        # type: () -> str | None
        return self._values[132]

    @field_decorator(index=133)
    def OutlierResponseCheckBelowLimit(self):
        # type: () -> str | None
        return self._values[133]

    @field_decorator(index=134)
    def OutlierResponseFactor(self):
        # type: () -> str | None
        return self._values[134]

    @field_decorator(index=135)
    def PeakFilterThreshold(self):
        # type: () -> str | None
        return self._values[135]

    @field_decorator(index=136)
    def PeakFilterThresholdValue(self):
        # type: () -> float | None
        return self._values[136]

    @field_decorator(index=137)
    def PeakSelectionCriterion(self):
        # type: () -> str | None
        return self._values[137]

    @field_decorator(index=138)
    def PlatesCalculationType(self):
        # type: () -> str | None
        return self._values[138]

    @field_decorator(index=139)
    def PlatesLimit(self):
        # type: () -> int | None
        return self._values[139]

    @field_decorator(index=140)
    def PrimaryHitPeakID(self):
        # type: () -> int | None
        return self._values[140]

    @field_decorator(index=141)
    def QCLCSMaximumRecoveryA(self):
        # type: () -> float | None
        return self._values[141]

    @field_decorator(index=142)
    def QCLCSMaximumRecoveryB(self):
        # type: () -> float | None
        return self._values[142]

    @field_decorator(index=143)
    def QCLCSMinimumRecoveryA(self):
        # type: () -> float | None
        return self._values[143]

    @field_decorator(index=144)
    def QCLCSMinimumRecoveryB(self):
        # type: () -> float | None
        return self._values[144]

    @field_decorator(index=145)
    def QCMaximumDeviation(self):
        # type: () -> float | None
        return self._values[145]

    @field_decorator(index=146)
    def QCMaximumPercentRSD(self):
        # type: () -> float | None
        return self._values[146]

    @field_decorator(index=147)
    def QualifierRatioMethod(self):
        # type: () -> int | None
        return self._values[147]

    @field_decorator(index=148)
    def QuantitateByHeight(self):
        # type: () -> bool | None
        return self._values[148]

    @field_decorator(index=149)
    def QuantitationMessage(self):
        # type: () -> str | None
        return self._values[149]

    @field_decorator(index=150)
    def QValueMinimum(self):
        # type: () -> int | None
        return self._values[150]

    @field_decorator(index=151)
    def ReferenceMSPathName(self):
        # type: () -> str | None
        return self._values[151]

    @field_decorator(index=152)
    def ReferenceWindowOverride(self):
        # type: () -> float | None
        return self._values[152]

    @field_decorator(index=153)
    def RelativeISTDMultiplier(self):
        # type: () -> float | None
        return self._values[153]

    @field_decorator(index=154)
    def RelativeResponseFactorMaximumPercentDeviation(self):
        # type: () -> float | None
        return self._values[154]

    @field_decorator(index=155)
    def RelativeRetentionTimeMaximumPercentDeviation(self):
        # type: () -> float | None
        return self._values[155]

    @field_decorator(index=156)
    def RelativeStandardError(self):
        # type: () -> float | None
        return self._values[156]

    @field_decorator(index=157)
    def RelativeStandardErrorMaximum(self):
        # type: () -> float | None
        return self._values[157]

    @field_decorator(index=158)
    def ResolutionCalculationType(self):
        # type: () -> str | None
        return self._values[158]

    @field_decorator(index=159)
    def ResolutionLimit(self):
        # type: () -> float | None
        return self._values[159]

    @field_decorator(index=160)
    def ResponseCheckMinimum(self):
        # type: () -> float | None
        return self._values[160]

    @field_decorator(index=161)
    def ResponseFactorMaximumPercentDeviation(self):
        # type: () -> float | None
        return self._values[161]

    @field_decorator(index=162)
    def RetentionIndex(self):
        # type: () -> float | None
        return self._values[162]

    @field_decorator(index=163)
    def RetentionTime(self):
        # type: () -> float | None
        return self._values[163]

    @field_decorator(index=164)
    def RetentionTimeDeltaUnits(self):
        # type: () -> str | None
        return self._values[164]

    @field_decorator(index=165)
    def RetentionTimeWindow(self):
        # type: () -> float | None
        return self._values[165]

    @field_decorator(index=166)
    def RetentionTimeWindowCC(self):
        # type: () -> float | None
        return self._values[166]

    @field_decorator(index=167)
    def RetentionTimeWindowUnits(self):
        # type: () -> str | None
        return self._values[167]

    @field_decorator(index=168)
    def RightRetentionTimeDelta(self):
        # type: () -> float | None
        return self._values[168]

    @field_decorator(index=169)
    def RxUnlabeledIsotopicDilution(self):
        # type: () -> float | None
        return self._values[169]

    @field_decorator(index=170)
    def RyLabeledIsotopicDilution(self):
        # type: () -> float | None
        return self._values[170]

    @field_decorator(index=171)
    def SampleAmountLimitHigh(self):
        # type: () -> float | None
        return self._values[171]

    @field_decorator(index=172)
    def SampleAmountLimitLow(self):
        # type: () -> float | None
        return self._values[172]

    @field_decorator(index=173)
    def SampleMaximumPercentRSD(self):
        # type: () -> float | None
        return self._values[173]

    @field_decorator(index=174)
    def ScanType(self):
        # type: () -> str | None
        return self._values[174]

    @field_decorator(index=175)
    def SelectedMZ(self):
        # type: () -> float | None
        return self._values[175]

    @field_decorator(index=176)
    def SignalInstance(self):
        # type: () -> int | None
        return self._values[176]

    @field_decorator(index=177)
    def SignalName(self):
        # type: () -> str | None
        return self._values[177]

    @field_decorator(index=178)
    def SignalRetentionTimeOffset(self):
        # type: () -> float | None
        return self._values[178]

    @field_decorator(index=179)
    def SignalToNoiseMultiplier(self):
        # type: () -> float | None
        return self._values[179]

    @field_decorator(index=180)
    def SignalType(self):
        # type: () -> str | None
        return self._values[180]

    @field_decorator(index=181)
    def Smoothing(self):
        # type: () -> str | None
        return self._values[181]

    @field_decorator(index=182)
    def SmoothingFunctionWidth(self):
        # type: () -> int | None
        return self._values[182]

    @field_decorator(index=183)
    def SmoothingGaussianWidth(self):
        # type: () -> float | None
        return self._values[183]

    @field_decorator(index=184)
    def Species(self):
        # type: () -> str | None
        return self._values[184]

    @field_decorator(index=185)
    def SpectrumBaselineThreshold(self):
        # type: () -> float | None
        return self._values[185]

    @field_decorator(index=186)
    def SpectrumExtractionOverride(self):
        # type: () -> str | None
        return self._values[186]

    @field_decorator(index=187)
    def SpectrumScanInclusion(self):
        # type: () -> str | None
        return self._values[187]

    @field_decorator(index=188)
    def SpectrumPeakHeightPercentThreshold(self):
        # type: () -> float | None
        return self._values[188]

    @field_decorator(index=189)
    def SpectrumPercentSaturationThreshold(self):
        # type: () -> float | None
        return self._values[189]

    @field_decorator(index=190)
    def SpectrumQuantifierQualifierOnly(self):
        # type: () -> bool | None
        return self._values[190]

    @field_decorator(index=191)
    def Sublist(self):
        # type: () -> bool | None
        return self._values[191]

    @field_decorator(index=192)
    def SurrogateConcentration(self):
        # type: () -> float | None
        return self._values[192]

    @field_decorator(index=193)
    def SurrogateConcentrationLimitHigh(self):
        # type: () -> float | None
        return self._values[193]

    @field_decorator(index=194)
    def SurrogateConcentrationLimitLow(self):
        # type: () -> float | None
        return self._values[194]

    @field_decorator(index=195)
    def SurrogatePercentRecoveryMaximum(self):
        # type: () -> float | None
        return self._values[195]

    @field_decorator(index=196)
    def SurrogatePercentRecoveryMinimum(self):
        # type: () -> float | None
        return self._values[196]

    @field_decorator(index=197)
    def SymmetryCalculationType(self):
        # type: () -> str | None
        return self._values[197]

    @field_decorator(index=198)
    def SymmetryLimitHigh(self):
        # type: () -> float | None
        return self._values[198]

    @field_decorator(index=199)
    def SymmetryLimitLow(self):
        # type: () -> float | None
        return self._values[199]

    @field_decorator(index=200)
    def TargetCompoundIDStatus(self):
        # type: () -> str | None
        return self._values[200]

    @field_decorator(index=201)
    def ThresholdNumberOfPeaks(self):
        # type: () -> int | None
        return self._values[201]

    @field_decorator(index=202)
    def TimeReferenceFlag(self):
        # type: () -> bool | None
        return self._values[202]

    @field_decorator(index=203)
    def TimeSegment(self):
        # type: () -> int | None
        return self._values[203]

    @field_decorator(index=204)
    def Transition(self):
        # type: () -> str | None
        return self._values[204]

    @field_decorator(index=205)
    def TriggeredTransitions(self):
        # type: () -> str | None
        return self._values[205]

    @field_decorator(index=206)
    def UncertaintyRelativeOrAbsolute(self):
        # type: () -> str | None
        return self._values[206]

    @field_decorator(index=207)
    def UserAnnotation(self):
        # type: () -> str | None
        return self._values[207]

    @field_decorator(index=208)
    def UserCustomCalculation(self):
        # type: () -> float | None
        return self._values[208]

    @field_decorator(index=209)
    def UserCustomCalculationLimitHigh(self):
        # type: () -> float | None
        return self._values[209]

    @field_decorator(index=210)
    def UserCustomCalculationLimitLow(self):
        # type: () -> float | None
        return self._values[210]

    @field_decorator(index=211)
    def UserDefined(self):
        # type: () -> str | None
        return self._values[211]

    @field_decorator(index=212)
    def UserDefined1(self):
        # type: () -> str | None
        return self._values[212]

    @field_decorator(index=213)
    def UserDefined2(self):
        # type: () -> str | None
        return self._values[213]

    @field_decorator(index=214)
    def UserDefined3(self):
        # type: () -> str | None
        return self._values[214]

    @field_decorator(index=215)
    def UserDefined4(self):
        # type: () -> str | None
        return self._values[215]

    @field_decorator(index=216)
    def UserDefined5(self):
        # type: () -> str | None
        return self._values[216]

    @field_decorator(index=217)
    def UserDefined6(self):
        # type: () -> str | None
        return self._values[217]

    @field_decorator(index=218)
    def UserDefined7(self):
        # type: () -> str | None
        return self._values[218]

    @field_decorator(index=219)
    def UserDefined8(self):
        # type: () -> str | None
        return self._values[219]

    @field_decorator(index=220)
    def UserDefined9(self):
        # type: () -> str | None
        return self._values[220]

    @field_decorator(index=221)
    def UserDefinedTargetCompoundID(self):
        # type: () -> int | None
        return self._values[221]

    @field_decorator(index=222)
    def WavelengthExtractionRangeHigh(self):
        # type: () -> float | None
        return self._values[222]

    @field_decorator(index=223)
    def WavelengthExtractionRangeLow(self):
        # type: () -> float | None
        return self._values[223]

    @field_decorator(index=224)
    def WavelengthReferenceRangeHigh(self):
        # type: () -> float | None
        return self._values[224]

    @field_decorator(index=225)
    def WavelengthReferenceRangeLow(self):
        # type: () -> float | None
        return self._values[225]


class TargetCompoundDataTable(DataTableBase[TargetCompoundRow]):
    """Represents the TargetCompound table, containing TargetCompoundRow objects."""

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
    def AreaSum(self):
        # type: () -> bool | None
        return self._values[4]

    @field_decorator(index=5)
    def CellAcceleratorVoltage(self):
        # type: () -> float | None
        return self._values[5]

    @field_decorator(index=6)
    def CollisionEnergy(self):
        # type: () -> float | None
        return self._values[6]

    @field_decorator(index=7)
    def CollisionEnergyDelta(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def FragmentorVoltage(self):
        # type: () -> float | None
        return self._values[8]

    @field_decorator(index=9)
    def FragmentorVoltageDelta(self):
        # type: () -> float | None
        return self._values[9]

    @field_decorator(index=10)
    def GraphicPeakQualifierChromatogram(self):
        # type: () -> str | None
        return self._values[10]

    @field_decorator(index=11)
    def IntegrationParameters(self):
        # type: () -> str | None
        return self._values[11]

    @field_decorator(index=12)
    def IntegrationParametersModified(self):
        # type: () -> bool | None
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
    def MZExtractionWindowFilterLeft(self):
        # type: () -> float | None
        return self._values[15]

    @field_decorator(index=16)
    def MZExtractionWindowFilterRight(self):
        # type: () -> float | None
        return self._values[16]

    @field_decorator(index=17)
    def MZExtractionWindowUnits(self):
        # type: () -> str | None
        return self._values[17]

    @field_decorator(index=18)
    def OutlierPeakNotFound(self):
        # type: () -> str | None
        return self._values[18]

    @field_decorator(index=19)
    def PeakFilterThreshold(self):
        # type: () -> str | None
        return self._values[19]

    @field_decorator(index=20)
    def PeakFilterThresholdValue(self):
        # type: () -> float | None
        return self._values[20]

    @field_decorator(index=21)
    def QualifierName(self):
        # type: () -> str | None
        return self._values[21]

    @field_decorator(index=22)
    def QualifierRangeMaximum(self):
        # type: () -> float | None
        return self._values[22]

    @field_decorator(index=23)
    def QualifierRangeMinimum(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def QuantitationMessage(self):
        # type: () -> str | None
        return self._values[24]

    @field_decorator(index=25)
    def RelativeResponse(self):
        # type: () -> float | None
        return self._values[25]

    @field_decorator(index=26)
    def ScanType(self):
        # type: () -> str | None
        return self._values[26]

    @field_decorator(index=27)
    def SelectedMZ(self):
        # type: () -> float | None
        return self._values[27]

    @field_decorator(index=28)
    def ThresholdNumberOfPeaks(self):
        # type: () -> int | None
        return self._values[28]

    @field_decorator(index=29)
    def Transition(self):
        # type: () -> str | None
        return self._values[29]

    @field_decorator(index=30)
    def Uncertainty(self):
        # type: () -> float | None
        return self._values[30]

    @field_decorator(index=31)
    def UserDefined(self):
        # type: () -> str | None
        return self._values[31]


class TargetQualifierDataTable(DataTableBase[TargetQualifierRow]):
    """Represents the TargetQualifier table, containing TargetQualifierRow objects."""

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
    def Accuracy(self):
        # type: () -> float | None
        return self._values[4]

    @field_decorator(index=5)
    def AlternativePeakRTDiff(self):
        # type: () -> float | None
        return self._values[5]

    @field_decorator(index=6)
    def AlternativeTargetHit(self):
        # type: () -> str | None
        return self._values[6]

    @field_decorator(index=7)
    def Area(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def AreaCorrectionResponse(self):
        # type: () -> float | None
        return self._values[8]

    @field_decorator(index=9)
    def BaselineDraw(self):
        # type: () -> str | None
        return self._values[9]

    @field_decorator(index=10)
    def BaselineEnd(self):
        # type: () -> float | None
        return self._values[10]

    @field_decorator(index=11)
    def BaselineEndOriginal(self):
        # type: () -> float | None
        return self._values[11]

    @field_decorator(index=12)
    def BaselineStandardDeviation(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def BaselineStart(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def BaselineStartOriginal(self):
        # type: () -> float | None
        return self._values[14]

    @field_decorator(index=15)
    def CalculatedConcentration(self):
        # type: () -> float | None
        return self._values[15]

    @field_decorator(index=16)
    def CapacityFactor(self):
        # type: () -> float | None
        return self._values[16]

    @field_decorator(index=17)
    def CCISTDResponseRatio(self):
        # type: () -> float | None
        return self._values[17]

    @field_decorator(index=18)
    def CCResponseRatio(self):
        # type: () -> float | None
        return self._values[18]

    @field_decorator(index=19)
    def EstimatedConcentration(self):
        # type: () -> str | None
        return self._values[19]

    @field_decorator(index=20)
    def FinalConcentration(self):
        # type: () -> float | None
        return self._values[20]

    @field_decorator(index=21)
    def FullWidthHalfMaximum(self):
        # type: () -> float | None
        return self._values[21]

    @field_decorator(index=22)
    def GroupNumber(self):
        # type: () -> int | None
        return self._values[22]

    @field_decorator(index=23)
    def Height(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def IntegrationEndTime(self):
        # type: () -> float | None
        return self._values[24]

    @field_decorator(index=25)
    def IntegrationEndTimeOriginal(self):
        # type: () -> float | None
        return self._values[25]

    @field_decorator(index=26)
    def IntegrationMetricQualityFlags(self):
        # type: () -> str | None
        return self._values[26]

    @field_decorator(index=27)
    def IntegrationQualityMetric(self):
        # type: () -> str | None
        return self._values[27]

    @field_decorator(index=28)
    def IntegrationStartTime(self):
        # type: () -> float | None
        return self._values[28]

    @field_decorator(index=29)
    def IntegrationStartTimeOriginal(self):
        # type: () -> float | None
        return self._values[29]

    @field_decorator(index=30)
    def ISTDConcentrationRatio(self):
        # type: () -> float | None
        return self._values[30]

    @field_decorator(index=31)
    def ISTDResponsePercentDeviation(self):
        # type: () -> float | None
        return self._values[31]

    @field_decorator(index=32)
    def ISTDResponseRatio(self):
        # type: () -> float | None
        return self._values[32]

    @field_decorator(index=33)
    def ManuallyIntegrated(self):
        # type: () -> bool | None
        return self._values[33]

    @field_decorator(index=34)
    def MassAbundanceScore(self):
        # type: () -> float | None
        return self._values[34]

    @field_decorator(index=35)
    def MassAccuracy(self):
        # type: () -> float | None
        return self._values[35]

    @field_decorator(index=36)
    def MassAccuracyScore(self):
        # type: () -> float | None
        return self._values[36]

    @field_decorator(index=37)
    def MassMatchScore(self):
        # type: () -> float | None
        return self._values[37]

    @field_decorator(index=38)
    def MassSpacingScore(self):
        # type: () -> float | None
        return self._values[38]

    @field_decorator(index=39)
    def MatrixSpikePercentDeviation(self):
        # type: () -> float | None
        return self._values[39]

    @field_decorator(index=40)
    def MatrixSpikePercentRecovery(self):
        # type: () -> float | None
        return self._values[40]

    @field_decorator(index=41)
    def MZ(self):
        # type: () -> float | None
        return self._values[41]

    @field_decorator(index=42)
    def Noise(self):
        # type: () -> float | None
        return self._values[42]

    @field_decorator(index=43)
    def NoiseRegions(self):
        # type: () -> str | None
        return self._values[43]

    @field_decorator(index=44)
    def OutlierAccuracy(self):
        # type: () -> str | None
        return self._values[44]

    @field_decorator(index=45)
    def OutlierBelowLimitOfDetection(self):
        # type: () -> str | None
        return self._values[45]

    @field_decorator(index=46)
    def OutlierBelowLimitOfQuantitation(self):
        # type: () -> str | None
        return self._values[46]

    @field_decorator(index=47)
    def OutlierBlankConcentrationOutsideLimit(self):
        # type: () -> str | None
        return self._values[47]

    @field_decorator(index=48)
    def OutlierCapacityFactor(self):
        # type: () -> str | None
        return self._values[48]

    @field_decorator(index=49)
    def OutlierCCISTDResponseRatio(self):
        # type: () -> str | None
        return self._values[49]

    @field_decorator(index=50)
    def OutlierCCResponseRatio(self):
        # type: () -> str | None
        return self._values[50]

    @field_decorator(index=51)
    def OutlierCCRetentionTime(self):
        # type: () -> str | None
        return self._values[51]

    @field_decorator(index=52)
    def OutlierFullWidthHalfMaximum(self):
        # type: () -> str | None
        return self._values[52]

    @field_decorator(index=53)
    def OutlierIntegrationQualityMetric(self):
        # type: () -> str | None
        return self._values[53]

    @field_decorator(index=54)
    def OutlierISTDResponse(self):
        # type: () -> str | None
        return self._values[54]

    @field_decorator(index=55)
    def OutlierISTDResponsePercentDeviation(self):
        # type: () -> str | None
        return self._values[55]

    @field_decorator(index=56)
    def OutlierLibraryMatchScore(self):
        # type: () -> str | None
        return self._values[56]

    @field_decorator(index=57)
    def OutlierMassAccuracy(self):
        # type: () -> str | None
        return self._values[57]

    @field_decorator(index=58)
    def OutlierMassMatchScore(self):
        # type: () -> str | None
        return self._values[58]

    @field_decorator(index=59)
    def OutlierMatrixSpikeGroupRecovery(self):
        # type: () -> str | None
        return self._values[59]

    @field_decorator(index=60)
    def OutlierMatrixSpikeOutOfLimits(self):
        # type: () -> str | None
        return self._values[60]

    @field_decorator(index=61)
    def OutlierMatrixSpikeOutsidePercentDeviation(self):
        # type: () -> str | None
        return self._values[61]

    @field_decorator(index=62)
    def OutlierMatrixSpikePercentRecovery(self):
        # type: () -> str | None
        return self._values[62]

    @field_decorator(index=63)
    def OutlierOutOfCalibrationRange(self):
        # type: () -> str | None
        return self._values[63]

    @field_decorator(index=64)
    def OutlierPlates(self):
        # type: () -> str | None
        return self._values[64]

    @field_decorator(index=65)
    def OutlierPurity(self):
        # type: () -> str | None
        return self._values[65]

    @field_decorator(index=66)
    def OutlierQCLCSRecoveryOutOfLimits(self):
        # type: () -> str | None
        return self._values[66]

    @field_decorator(index=67)
    def OutlierQCOutOfLimits(self):
        # type: () -> str | None
        return self._values[67]

    @field_decorator(index=68)
    def OutlierQCOutsideRSD(self):
        # type: () -> str | None
        return self._values[68]

    @field_decorator(index=69)
    def OutlierQValue(self):
        # type: () -> str | None
        return self._values[69]

    @field_decorator(index=70)
    def OutlierRelativeRetentionTime(self):
        # type: () -> str | None
        return self._values[70]

    @field_decorator(index=71)
    def OutlierResolutionFront(self):
        # type: () -> str | None
        return self._values[71]

    @field_decorator(index=72)
    def OutlierResolutionRear(self):
        # type: () -> str | None
        return self._values[72]

    @field_decorator(index=73)
    def OutlierRetentionTime(self):
        # type: () -> str | None
        return self._values[73]

    @field_decorator(index=74)
    def OutlierSampleAmountOutOfLimits(self):
        # type: () -> str | None
        return self._values[74]

    @field_decorator(index=75)
    def OutlierSampleOutsideRSD(self):
        # type: () -> str | None
        return self._values[75]

    @field_decorator(index=76)
    def OutlierSaturationRecovery(self):
        # type: () -> str | None
        return self._values[76]

    @field_decorator(index=77)
    def OutlierSignalToNoiseRatioBelowLimit(self):
        # type: () -> str | None
        return self._values[77]

    @field_decorator(index=78)
    def OutlierSurrogateOutOfLimits(self):
        # type: () -> str | None
        return self._values[78]

    @field_decorator(index=79)
    def OutlierSurrogatePercentRecovery(self):
        # type: () -> str | None
        return self._values[79]

    @field_decorator(index=80)
    def OutlierSymmetry(self):
        # type: () -> str | None
        return self._values[80]

    @field_decorator(index=81)
    def Plates(self):
        # type: () -> int | None
        return self._values[81]

    @field_decorator(index=82)
    def Purity(self):
        # type: () -> float | None
        return self._values[82]

    @field_decorator(index=83)
    def QValueComputed(self):
        # type: () -> int | None
        return self._values[83]

    @field_decorator(index=84)
    def QValueSort(self):
        # type: () -> int | None
        return self._values[84]

    @field_decorator(index=85)
    def ReferenceLibraryMatchScore(self):
        # type: () -> float | None
        return self._values[85]

    @field_decorator(index=86)
    def RelativeRetentionTime(self):
        # type: () -> float | None
        return self._values[86]

    @field_decorator(index=87)
    def ResolutionFront(self):
        # type: () -> float | None
        return self._values[87]

    @field_decorator(index=88)
    def ResolutionRear(self):
        # type: () -> float | None
        return self._values[88]

    @field_decorator(index=89)
    def ResponseRatio(self):
        # type: () -> float | None
        return self._values[89]

    @field_decorator(index=90)
    def RetentionIndex(self):
        # type: () -> float | None
        return self._values[90]

    @field_decorator(index=91)
    def RetentionTime(self):
        # type: () -> float | None
        return self._values[91]

    @field_decorator(index=92)
    def RetentionTimeDifference(self):
        # type: () -> float | None
        return self._values[92]

    @field_decorator(index=93)
    def RetentionTimeDifferenceKey(self):
        # type: () -> int | None
        return self._values[93]

    @field_decorator(index=94)
    def RetentionTimeOriginal(self):
        # type: () -> float | None
        return self._values[94]

    @field_decorator(index=95)
    def SampleRSD(self):
        # type: () -> float | None
        return self._values[95]

    @field_decorator(index=96)
    def SaturationRecoveryRatio(self):
        # type: () -> float | None
        return self._values[96]

    @field_decorator(index=97)
    def SelectedGroupRetentionTime(self):
        # type: () -> float | None
        return self._values[97]

    @field_decorator(index=98)
    def SelectedTargetRetentionTime(self):
        # type: () -> float | None
        return self._values[98]

    @field_decorator(index=99)
    def SignalToNoiseRatio(self):
        # type: () -> float | None
        return self._values[99]

    @field_decorator(index=100)
    def SurrogatePercentRecovery(self):
        # type: () -> float | None
        return self._values[100]

    @field_decorator(index=101)
    def Symmetry(self):
        # type: () -> float | None
        return self._values[101]

    @field_decorator(index=102)
    def TargetResponse(self):
        # type: () -> float | None
        return self._values[102]

    @field_decorator(index=103)
    def TargetResponseOriginal(self):
        # type: () -> float | None
        return self._values[103]

    @field_decorator(index=104)
    def UserCustomCalculation(self):
        # type: () -> float | None
        return self._values[104]

    @field_decorator(index=105)
    def UserCustomCalculation1(self):
        # type: () -> float | None
        return self._values[105]

    @field_decorator(index=106)
    def UserCustomCalculation2(self):
        # type: () -> float | None
        return self._values[106]

    @field_decorator(index=107)
    def UserCustomCalculation3(self):
        # type: () -> float | None
        return self._values[107]

    @field_decorator(index=108)
    def UserCustomCalculation4(self):
        # type: () -> float | None
        return self._values[108]

    @field_decorator(index=109)
    def Width(self):
        # type: () -> float | None
        return self._values[109]


class PeakDataTable(DataTableBase[PeakRow]):
    """Represents the Peak table, containing PeakRow objects."""

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
    def PeakID(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def QualifierID(self):
        # type: () -> int | None
        return self._values[4]

    @field_decorator(index=5)
    def Area(self):
        # type: () -> float | None
        return self._values[5]

    @field_decorator(index=6)
    def BaselineEnd(self):
        # type: () -> float | None
        return self._values[6]

    @field_decorator(index=7)
    def BaselineEndOriginal(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def BaselineStandardDeviation(self):
        # type: () -> float | None
        return self._values[8]

    @field_decorator(index=9)
    def BaselineStart(self):
        # type: () -> float | None
        return self._values[9]

    @field_decorator(index=10)
    def BaselineStartOriginal(self):
        # type: () -> float | None
        return self._values[10]

    @field_decorator(index=11)
    def CoelutionScore(self):
        # type: () -> float | None
        return self._values[11]

    @field_decorator(index=12)
    def FullWidthHalfMaximum(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def Height(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def IntegrationEndTime(self):
        # type: () -> float | None
        return self._values[14]

    @field_decorator(index=15)
    def IntegrationEndTimeOriginal(self):
        # type: () -> float | None
        return self._values[15]

    @field_decorator(index=16)
    def IntegrationMetricQualityFlags(self):
        # type: () -> str | None
        return self._values[16]

    @field_decorator(index=17)
    def IntegrationQualityMetric(self):
        # type: () -> str | None
        return self._values[17]

    @field_decorator(index=18)
    def IntegrationStartTime(self):
        # type: () -> float | None
        return self._values[18]

    @field_decorator(index=19)
    def IntegrationStartTimeOriginal(self):
        # type: () -> float | None
        return self._values[19]

    @field_decorator(index=20)
    def ManuallyIntegrated(self):
        # type: () -> bool | None
        return self._values[20]

    @field_decorator(index=21)
    def MassAccuracy(self):
        # type: () -> float | None
        return self._values[21]

    @field_decorator(index=22)
    def MZ(self):
        # type: () -> float | None
        return self._values[22]

    @field_decorator(index=23)
    def Noise(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def NoiseRegions(self):
        # type: () -> str | None
        return self._values[24]

    @field_decorator(index=25)
    def OutlierQualifierCoelutionScore(self):
        # type: () -> str | None
        return self._values[25]

    @field_decorator(index=26)
    def OutlierQualifierFullWidthHalfMaximum(self):
        # type: () -> str | None
        return self._values[26]

    @field_decorator(index=27)
    def OutlierQualifierIntegrationQualityMetric(self):
        # type: () -> str | None
        return self._values[27]

    @field_decorator(index=28)
    def OutlierQualifierMassAccuracy(self):
        # type: () -> str | None
        return self._values[28]

    @field_decorator(index=29)
    def OutlierQualifierOutOfLimits(self):
        # type: () -> str | None
        return self._values[29]

    @field_decorator(index=30)
    def OutlierQualifierResolutionFront(self):
        # type: () -> str | None
        return self._values[30]

    @field_decorator(index=31)
    def OutlierQualifierResolutionRear(self):
        # type: () -> str | None
        return self._values[31]

    @field_decorator(index=32)
    def OutlierQualifierSignalToNoiseRatio(self):
        # type: () -> str | None
        return self._values[32]

    @field_decorator(index=33)
    def OutlierQualifierSymmetry(self):
        # type: () -> str | None
        return self._values[33]

    @field_decorator(index=34)
    def OutlierSaturationRecovery(self):
        # type: () -> str | None
        return self._values[34]

    @field_decorator(index=35)
    def QualifierResponseRatio(self):
        # type: () -> float | None
        return self._values[35]

    @field_decorator(index=36)
    def QualifierResponseRatioOriginal(self):
        # type: () -> float | None
        return self._values[36]

    @field_decorator(index=37)
    def ResolutionFront(self):
        # type: () -> float | None
        return self._values[37]

    @field_decorator(index=38)
    def ResolutionRear(self):
        # type: () -> float | None
        return self._values[38]

    @field_decorator(index=39)
    def RetentionTime(self):
        # type: () -> float | None
        return self._values[39]

    @field_decorator(index=40)
    def RetentionTimeOriginal(self):
        # type: () -> float | None
        return self._values[40]

    @field_decorator(index=41)
    def SaturationRecoveryRatio(self):
        # type: () -> float | None
        return self._values[41]

    @field_decorator(index=42)
    def SignalToNoiseRatio(self):
        # type: () -> float | None
        return self._values[42]

    @field_decorator(index=43)
    def Symmetry(self):
        # type: () -> float | None
        return self._values[43]

    @field_decorator(index=44)
    def UserCustomCalculation(self):
        # type: () -> float | None
        return self._values[44]


class PeakQualifierDataTable(DataTableBase[PeakQualifierRow]):
    """Represents the PeakQualifier table, containing PeakQualifierRow objects."""

    pass


class CalibrationRow(RowBase):
    """Represents a row for the Calibration table."""

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
    def LevelID(self):
        # type: () -> int | None
        return self._values[3]

    @field_decorator(index=4)
    def CalibrationSTDAcquisitionDateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[4]

    @field_decorator(index=5)
    def CalibrationSTDPathName(self):
        # type: () -> str | None
        return self._values[5]

    @field_decorator(index=6)
    def CalibrationType(self):
        # type: () -> str | None
        return self._values[6]

    @field_decorator(index=7)
    def LevelAverageCounter(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def LevelConcentration(self):
        # type: () -> float | None
        return self._values[8]

    @field_decorator(index=9)
    def LevelEnable(self):
        # type: () -> bool | None
        return self._values[9]

    @field_decorator(index=10)
    def LevelLastUpdateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[10]

    @field_decorator(index=11)
    def LevelName(self):
        # type: () -> str | None
        return self._values[11]

    @field_decorator(index=12)
    def LevelResponse(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def LevelResponseFactor(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def LevelRSD(self):
        # type: () -> float | None
        return self._values[14]


class CalibrationDataTable(DataTableBase[CalibrationRow]):
    """Represents the Calibration table, containing CalibrationRow objects."""

    pass
