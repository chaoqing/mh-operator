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


class LibraryRow(RowBase):
    """Represents a row for the Library table."""

    @field_decorator(index=0)
    def LibraryID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def AccurateMass(self):
        # type: () -> bool | None
        return self._values[1]

    @field_decorator(index=2)
    def CreationDateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[2]

    @field_decorator(index=3)
    def Description(self):
        # type: () -> str | None
        return self._values[3]

    @field_decorator(index=4)
    def LastEditDateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[4]

    @field_decorator(index=5)
    def LibraryName(self):
        # type: () -> str | None
        return self._values[5]

    @field_decorator(index=6)
    def LibrarySource(self):
        # type: () -> str | None
        return self._values[6]


class LibraryDataTable(DataTableBase[LibraryRow]):
    """Represents the Library table, containing LibraryRow objects."""

    pass


class CompoundRow(RowBase):
    """Represents a row for the Compound table."""

    @field_decorator(index=0)
    def LibraryID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def CompoundID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def AlternateNames(self):
        # type: () -> str | None
        return self._values[2]

    @field_decorator(index=3)
    def BoilingPoint(self):
        # type: () -> float | None
        return self._values[3]

    @field_decorator(index=4)
    def CASNumber(self):
        # type: () -> str | None
        return self._values[4]

    @field_decorator(index=5)
    def CompoundName(self):
        # type: () -> str | None
        return self._values[5]

    @field_decorator(index=6)
    def Description(self):
        # type: () -> str | None
        return self._values[6]

    @field_decorator(index=7)
    def Formula(self):
        # type: () -> str | None
        return self._values[7]

    @field_decorator(index=8)
    def LastEditDateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[8]

    @field_decorator(index=9)
    def MeltingPoint(self):
        # type: () -> float | None
        return self._values[9]

    @field_decorator(index=10)
    def MolecularWeight(self):
        # type: () -> float | None
        return self._values[10]

    @field_decorator(index=11)
    def MolFile(self):
        # type: () -> str | None
        return self._values[11]

    @field_decorator(index=12)
    def MonoisotopicMass(self):
        # type: () -> float | None
        return self._values[12]

    @field_decorator(index=13)
    def RetentionIndex(self):
        # type: () -> float | None
        return self._values[13]

    @field_decorator(index=14)
    def RetentionTimeRTL(self):
        # type: () -> float | None
        return self._values[14]

    @field_decorator(index=15)
    def UserDefined(self):
        # type: () -> str | None
        return self._values[15]


class CompoundDataTable(DataTableBase[CompoundRow]):
    """Represents the Compound table, containing CompoundRow objects."""

    pass


class SpectrumRow(RowBase):
    """Represents a row for the Spectrum table."""

    @field_decorator(index=0)
    def LibraryID(self):
        # type: () -> int | None
        return self._values[0]

    @field_decorator(index=1)
    def CompoundID(self):
        # type: () -> int | None
        return self._values[1]

    @field_decorator(index=2)
    def SpectrumID(self):
        # type: () -> int | None
        return self._values[2]

    @field_decorator(index=3)
    def AbundanceValues(self):
        # type: () -> str | None
        return self._values[3]

    @field_decorator(index=4)
    def AcqRetentionTime(self):
        # type: () -> float | None
        return self._values[4]

    @field_decorator(index=5)
    def BasePeakAbundance(self):
        # type: () -> float | None
        return self._values[5]

    @field_decorator(index=6)
    def BasePeakMZ(self):
        # type: () -> float | None
        return self._values[6]

    @field_decorator(index=7)
    def CollisionEnergy(self):
        # type: () -> float | None
        return self._values[7]

    @field_decorator(index=8)
    def HighestMz(self):
        # type: () -> float | None
        return self._values[8]

    @field_decorator(index=9)
    def IonizationEnergy(self):
        # type: () -> float | None
        return self._values[9]

    @field_decorator(index=10)
    def IonizationType(self):
        # type: () -> str | None
        return self._values[10]

    @field_decorator(index=11)
    def IonPolarity(self):
        # type: () -> str | None
        return self._values[11]

    @field_decorator(index=12)
    def InstrumentType(self):
        # type: () -> str | None
        return self._values[12]

    @field_decorator(index=13)
    def LastEditDateTime(self):
        # type: () -> datetime.datetime | None
        return self._values[13]

    @field_decorator(index=14)
    def LowestMz(self):
        # type: () -> float | None
        return self._values[14]

    @field_decorator(index=15)
    def MzSignature(self):
        # type: () -> str | None
        return self._values[15]

    @field_decorator(index=16)
    def MzSignatureBinWidth(self):
        # type: () -> float | None
        return self._values[16]

    @field_decorator(index=17)
    def MzValues(self):
        # type: () -> str | None
        return self._values[17]

    @field_decorator(index=18)
    def NumberOfPeaks(self):
        # type: () -> int | None
        return self._values[18]

    @field_decorator(index=19)
    def Origin(self):
        # type: () -> str | None
        return self._values[19]

    @field_decorator(index=20)
    def Owner(self):
        # type: () -> str | None
        return self._values[20]

    @field_decorator(index=21)
    def SampleID(self):
        # type: () -> str | None
        return self._values[21]

    @field_decorator(index=22)
    def ScanType(self):
        # type: () -> str | None
        return self._values[22]

    @field_decorator(index=23)
    def SelectedMZ(self):
        # type: () -> float | None
        return self._values[23]

    @field_decorator(index=24)
    def SeparationType(self):
        # type: () -> str | None
        return self._values[24]

    @field_decorator(index=25)
    def Species(self):
        # type: () -> str | None
        return self._values[25]

    @field_decorator(index=26)
    def UPlusAValues(self):
        # type: () -> str | None
        return self._values[26]

    @field_decorator(index=27)
    def UserDefined(self):
        # type: () -> str | None
        return self._values[27]


class SpectrumDataTable(DataTableBase[SpectrumRow]):
    """Represents the Spectrum table, containing SpectrumRow objects."""

    pass
