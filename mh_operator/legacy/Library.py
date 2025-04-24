# -*- coding: utf-8 -*-
import datetime

from .Base import RowBase, TableBase


class LibraryRow(RowBase):
    """Represents a row for the Library table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    LibraryID = None  # type: int
    AccurateMass = None  # type: bool
    CreationDateTime = None  # type: datetime.datetime
    Description = None  # type: str
    LastEditDateTime = None  # type: datetime.datetime
    LibraryName = None  # type: str
    LibrarySource = None  # type: str

    def __init__(self, *args, **kwargs):
        super(LibraryRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 7

    def __repr__(self):
        return (
            "<LibraryRow:"
            + " LibraryID={}".format(self.LibraryID)
            + " AccurateMass={}".format(self.AccurateMass)
            + " CreationDateTime={}".format(self.CreationDateTime)
            + " Description={}".format(self.Description)
            + " LastEditDateTime={}".format(self.LastEditDateTime)
            + " ...>"
        )


class LibraryDataTable(TableBase):
    """Represents the Library table, containing LibraryRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[LibraryRow]
        super(LibraryDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> LibraryRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("LibraryDataTable", len(self.rows))


class CompoundRow(RowBase):
    """Represents a row for the Compound table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    LibraryID = None  # type: int
    CompoundID = None  # type: int
    AlternateNames = None  # type: str
    BoilingPoint = None  # type: float
    CASNumber = None  # type: str
    CompoundName = None  # type: str
    Description = None  # type: str
    Formula = None  # type: str
    LastEditDateTime = None  # type: datetime.datetime
    MeltingPoint = None  # type: float
    MolecularWeight = None  # type: float
    MolFile = None  # type: str
    MonoisotopicMass = None  # type: float
    RetentionIndex = None  # type: float
    RetentionTimeRTL = None  # type: float
    UserDefined = None  # type: str

    def __init__(self, *args, **kwargs):
        super(CompoundRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 16

    def __repr__(self):
        return (
            "<CompoundRow:"
            + " LibraryID={}".format(self.LibraryID)
            + " CompoundID={}".format(self.CompoundID)
            + " AlternateNames={}".format(self.AlternateNames)
            + " BoilingPoint={}".format(self.BoilingPoint)
            + " CASNumber={}".format(self.CASNumber)
            + " ...>"
        )


class CompoundDataTable(TableBase):
    """Represents the Compound table, containing CompoundRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[CompoundRow]
        super(CompoundDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> CompoundRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("CompoundDataTable", len(self.rows))


class SpectrumRow(RowBase):
    """Represents a row for the Spectrum table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    LibraryID = None  # type: int
    CompoundID = None  # type: int
    SpectrumID = None  # type: int
    AbundanceValues = None  # type: str
    AcqRetentionTime = None  # type: float
    BasePeakAbundance = None  # type: float
    BasePeakMZ = None  # type: float
    CollisionEnergy = None  # type: float
    HighestMz = None  # type: float
    IonizationEnergy = None  # type: float
    IonizationType = None  # type: str
    IonPolarity = None  # type: str
    InstrumentType = None  # type: str
    LastEditDateTime = None  # type: datetime.datetime
    LowestMz = None  # type: float
    MzSignature = None  # type: str
    MzSignatureBinWidth = None  # type: float
    MzValues = None  # type: str
    NumberOfPeaks = None  # type: int
    Origin = None  # type: str
    Owner = None  # type: str
    SampleID = None  # type: str
    ScanType = None  # type: str
    SelectedMZ = None  # type: float
    SeparationType = None  # type: str
    Species = None  # type: str
    UPlusAValues = None  # type: str
    UserDefined = None  # type: str

    def __init__(self, *args, **kwargs):
        super(SpectrumRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 28

    def __repr__(self):
        return (
            "<SpectrumRow:"
            + " LibraryID={}".format(self.LibraryID)
            + " CompoundID={}".format(self.CompoundID)
            + " SpectrumID={}".format(self.SpectrumID)
            + " AbundanceValues={}".format(self.AbundanceValues)
            + " AcqRetentionTime={}".format(self.AcqRetentionTime)
            + " ...>"
        )


class SpectrumDataTable(TableBase):
    """Represents the Spectrum table, containing SpectrumRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[SpectrumRow]
        super(SpectrumDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> SpectrumRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("SpectrumDataTable", len(self.rows))
