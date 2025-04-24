# -*- coding: utf-8 -*-
import datetime

from .Base import RowBase, TableBase


class BatchRow(RowBase):
    """Represents a row for the Batch table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    TargetBatchDataPath = None  # type: str
    TargetBatchFileName = None  # type: str
    AppSchemaVersion = None  # type: int
    SchemaVersion = None  # type: int
    DataVersion = None  # type: int
    BatchState = None  # type: str
    AnalystName = None  # type: str
    AnalysisTimeStamp = None  # type: datetime.datetime
    FeatureDetection = None  # type: bool
    ReferenceWindow = None  # type: float
    ReferenceWindowPercentOrMinutes = None  # type: str
    NonReferenceWindow = None  # type: float
    NonReferenceWindowPercentOrMinutes = None  # type: str
    CorrelationWindow = None  # type: float
    ApplyMultiplierTarget = None  # type: bool
    ApplyMultiplierSurrogate = None  # type: bool
    ApplyMultiplierISTD = None  # type: bool
    ApplyMultiplierMatrixSpike = None  # type: bool
    IgnorePeaksNotFound = None  # type: bool
    RelativeISTD = None  # type: bool
    AuditTrail = None  # type: bool
    RefLibraryPathFileName = None  # type: str
    RefLibraryPatternPathFileName = None  # type: str
    LibraryMethodPathFileName = None  # type: str
    ReferencePatternLibraryPathFileName = None  # type: str
    CCMaximumElapsedTimeInHours = None  # type: float
    BracketingType = None  # type: str
    StandardAddition = None  # type: bool
    DynamicBackgroundSubtraction = None  # type: bool
    DAMethodPathFileNameOrigin = None  # type: str
    DAMethodLastAppliedTimeStamp = None  # type: datetime.datetime
    CalibrationLastUpdatedTimeStamp = None  # type: datetime.datetime
    AnalyzeQuantVersion = None  # type: str

    def __init__(self, *args, **kwargs):
        super(BatchRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 34

    def __repr__(self):
        return (
            "<BatchRow:"
            + " BatchID={}".format(self.BatchID)
            + " TargetBatchDataPath={}".format(self.TargetBatchDataPath)
            + " TargetBatchFileName={}".format(self.TargetBatchFileName)
            + " AppSchemaVersion={}".format(self.AppSchemaVersion)
            + " SchemaVersion={}".format(self.SchemaVersion)
            + " ...>"
        )


class BatchDataTable(TableBase):
    """Represents the Batch table, containing BatchRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[BatchRow]
        super(BatchDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> BatchRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("BatchDataTable", len(self.rows))


class SampleRow(RowBase):
    """Represents a row for the Sample table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    AcqDateTime = None  # type: datetime.datetime
    AcqDateTimeLocal = None  # type: Any
    AcqMethodFileName = None  # type: str
    AcqMethodPathName = None  # type: str
    AcqOperator = None  # type: str
    Barcode = None  # type: str
    Comment = None  # type: str
    DataFileName = None  # type: str
    DataPathName = None  # type: str
    Dilution = None  # type: float
    ExpectedBarCode = None  # type: str
    InjectorVolume = None  # type: float
    InstrumentName = None  # type: str
    InstrumentType = None  # type: str
    ISTDDilution = None  # type: float
    MatrixSpikeDilution = None  # type: float
    MatrixSpikeGroup = None  # type: str
    MatrixType = None  # type: str
    PlateCode = None  # type: str
    PlatePosition = None  # type: str
    RackCode = None  # type: str
    RackPosition = None  # type: str
    SampleAmount = None  # type: float
    SampleInformation = None  # type: str
    SampleGroup = None  # type: str
    SampleName = None  # type: str
    SamplePosition = None  # type: str
    SamplePrepFileName = None  # type: str
    SamplePrepPathName = None  # type: str
    SampleType = None  # type: str
    SamplingDateTime = None  # type: datetime.datetime
    SamplingTime = None  # type: float
    SurrogateDilution = None  # type: float
    TotalSampleAmount = None  # type: float
    TrayName = None  # type: str
    TuneFileLastTimeStamp = None  # type: datetime.datetime
    TuneFileName = None  # type: str
    TunePathName = None  # type: str
    UserDefined = None  # type: str
    UserDefined1 = None  # type: str
    UserDefined2 = None  # type: str
    UserDefined3 = None  # type: str
    UserDefined4 = None  # type: str
    UserDefined5 = None  # type: str
    UserDefined6 = None  # type: str
    UserDefined7 = None  # type: str
    UserDefined8 = None  # type: str
    UserDefined9 = None  # type: str
    Vial = None  # type: int
    AnalysisState = None  # type: str
    GraphicsSampleChromatogram = None  # type: str

    def __init__(self, *args, **kwargs):
        super(SampleRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 53

    def __repr__(self):
        return (
            "<SampleRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " AcqDateTime={}".format(self.AcqDateTime)
            + " AcqDateTimeLocal={}".format(self.AcqDateTimeLocal)
            + " AcqMethodFileName={}".format(self.AcqMethodFileName)
            + " ...>"
        )


class SampleDataTable(TableBase):
    """Represents the Sample table, containing SampleRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[SampleRow]
        super(SampleDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> SampleRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("SampleDataTable", len(self.rows))


class ComponentRow(RowBase):
    """Represents a row for the Component table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    DeconvolutionMethodID = None  # type: int
    ComponentID = None  # type: int
    PrimaryHitID = None  # type: int
    ModelIonPeakID = None  # type: int
    ComponentName = None  # type: str
    BasePeakID = None  # type: int
    IsManuallyIntegrated = None  # type: bool
    IsBackgroundSubtracted = None  # type: bool
    BestHit = None  # type: bool
    BestHitOverridden = None  # type: bool
    Area = None  # type: float
    EndX = None  # type: float
    Height = None  # type: float
    IsAccurateMass = None  # type: bool
    RetentionTime = None  # type: float
    RetentionIndex = None  # type: float
    SpectrumAbundances = None  # type: str
    SpectrumMZs = None  # type: str
    StartX = None  # type: float
    XArray = None  # type: str
    YArray = None  # type: str
    ShapeQuality = None  # type: float
    DeconvolutedHeight = None  # type: float
    AreaPercent = None  # type: float
    AreaPercentMax = None  # type: float
    Visible = None  # type: bool
    UserDefined = None  # type: str
    UserCustomCalculation = None  # type: float
    GraphicsComponentSpectrum = None  # type: str
    TargetedDeconvolution_IdentificationMethodID = None  # type: int
    TargetedDeconvolution_LibrarySearchMethodID = None  # type: int
    TargetedDeconvolution_LibraryEntryID = None  # type: int

    def __init__(self, *args, **kwargs):
        super(ComponentRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 34

    def __repr__(self):
        return (
            "<ComponentRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " DeconvolutionMethodID={}".format(self.DeconvolutionMethodID)
            + " ComponentID={}".format(self.ComponentID)
            + " PrimaryHitID={}".format(self.PrimaryHitID)
            + " ...>"
        )


class ComponentDataTable(TableBase):
    """Represents the Component table, containing ComponentRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[ComponentRow]
        super(ComponentDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> ComponentRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("ComponentDataTable", len(self.rows))


class HitRow(RowBase):
    """Represents a row for the Hit table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    DeconvolutionMethodID = None  # type: int
    ComponentID = None  # type: int
    HitID = None  # type: int
    AgilentID = None  # type: str
    IdentificationMethodID = None  # type: int
    LibrarySearchMethodID = None  # type: int
    LibraryEntryID = None  # type: int
    TargetCompoundID = None  # type: int
    CASNumber = None  # type: str
    CompoundName = None  # type: str
    EstimatedConcentration = None  # type: float
    Formula = None  # type: str
    KEGGID = None  # type: str
    LibraryMatchScore = None  # type: float
    LibraryRetentionIndex = None  # type: float
    LibraryRetentionTime = None  # type: float
    LibraryCompoundDescription = None  # type: str
    MolecularWeight = None  # type: float
    RTMismatchPenalty = None  # type: float
    RetentionIndex = None  # type: float
    MassMatchScore = None  # type: float
    MassAbundanceScore = None  # type: float
    MassAccuracyScore = None  # type: float
    MassSpacingScore = None  # type: float
    Visible = None  # type: bool
    BlankSubtracted = None  # type: bool
    RemovedDuplicateMZs = None  # type: str
    ResponseFactorForEstimation = None  # type: float
    MonoIsotopicMass = None  # type: float
    NumberOfExactMasses = None  # type: int
    UserDefined = None  # type: str
    UserCustomCalculation = None  # type: float
    GraphicsHitLibrarySpectrum = None  # type: str

    def __init__(self, *args, **kwargs):
        super(HitRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 35

    def __repr__(self):
        return (
            "<HitRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " DeconvolutionMethodID={}".format(self.DeconvolutionMethodID)
            + " ComponentID={}".format(self.ComponentID)
            + " HitID={}".format(self.HitID)
            + " ...>"
        )


class HitDataTable(TableBase):
    """Represents the Hit table, containing HitRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[HitRow]
        super(HitDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> HitRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("HitDataTable", len(self.rows))


class IonPeakRow(RowBase):
    """Represents a row for the IonPeak table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    DeconvolutionMethodID = None  # type: int
    ComponentID = None  # type: int
    IonPeakID = None  # type: int
    TargetCompoundID = None  # type: int
    TargetQualifierID = None  # type: int
    Area = None  # type: float
    DeconvolutedArea = None  # type: float
    DeconvolutedHeight = None  # type: float
    EndX = None  # type: float
    FullWidthHalfMaximum = None  # type: float
    Height = None  # type: float
    IonPolarity = None  # type: str
    MZ = None  # type: float
    PeakStatus = None  # type: str
    RetentionTime = None  # type: float
    Saturated = None  # type: bool
    ScanType = None  # type: str
    SelectedMZ = None  # type: float
    Sharpness = None  # type: float
    SignalToNoiseRatio = None  # type: float
    StartX = None  # type: float
    Symmetry = None  # type: float
    XArray = None  # type: str
    YArray = None  # type: str
    UserCustomCalculation = None  # type: float

    def __init__(self, *args, **kwargs):
        super(IonPeakRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 27

    def __repr__(self):
        return (
            "<IonPeakRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " DeconvolutionMethodID={}".format(self.DeconvolutionMethodID)
            + " ComponentID={}".format(self.ComponentID)
            + " IonPeakID={}".format(self.IonPeakID)
            + " ...>"
        )


class IonPeakDataTable(TableBase):
    """Represents the IonPeak table, containing IonPeakRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[IonPeakRow]
        super(IonPeakDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> IonPeakRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("IonPeakDataTable", len(self.rows))


class DeconvolutionMethodRow(RowBase):
    """Represents a row for the DeconvolutionMethod table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    DeconvolutionMethodID = None  # type: int
    Algorithm = None  # type: str
    ChromRangeHigh = None  # type: float
    ChromRangeLow = None  # type: float
    EICPeakThreshold = None  # type: float
    EICSNRThreshold = None  # type: float
    ExcludedMZs = None  # type: str
    LeftMZDelta = None  # type: float
    ModelShapePercentile = None  # type: float
    MZDeltaUnits = None  # type: str
    RetentionTimeBinSize = None  # type: float
    RightMZDelta = None  # type: float
    UseIntegerMZValues = None  # type: bool
    MaxSpectrumPeaksPerChromPeak = None  # type: int
    SpectrumPeakThreshold = None  # type: float
    UseLargestPeakShape = None  # type: bool
    WindowSizeFactor = None  # type: float
    TICAnalysis = None  # type: bool
    ChromPeakThreshold = None  # type: float
    ChromSNRThreshold = None  # type: float
    UseAreaFilterAbsolute = None  # type: bool
    AreaFilterAbsolute = None  # type: float
    UseAreaFilterRelative = None  # type: bool
    AreaFilterRelative = None  # type: float
    UseHeightFilterAbsolute = None  # type: bool
    HeightFilterAbsolute = None  # type: float
    UseHeightFilterRelative = None  # type: bool
    HeightFilterRelative = None  # type: float
    MaxNumPeaks = None  # type: int
    LargestPeaksRankedBy = None  # type: str
    RefineComponents = None  # type: bool
    MaxNumStoredIonPeaks = None  # type: int
    Integrator = None  # type: str
    Screening = None  # type: bool
    TargetedDeconvolution = None  # type: bool
    MinShapeQuality = None  # type: float
    MinNumPeaks = None  # type: int
    TICAnalysisSignalType = None  # type: str

    def __init__(self, *args, **kwargs):
        super(DeconvolutionMethodRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 40

    def __repr__(self):
        return (
            "<DeconvolutionMethodRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " DeconvolutionMethodID={}".format(self.DeconvolutionMethodID)
            + " Algorithm={}".format(self.Algorithm)
            + " ChromRangeHigh={}".format(self.ChromRangeHigh)
            + " ...>"
        )


class DeconvolutionMethodDataTable(TableBase):
    """Represents the DeconvolutionMethod table, containing DeconvolutionMethodRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[DeconvolutionMethodRow]
        super(DeconvolutionMethodDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> DeconvolutionMethodRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("DeconvolutionMethodDataTable", len(self.rows))


class LibrarySearchMethodRow(RowBase):
    """Represents a row for the LibrarySearchMethod table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    IdentificationMethodID = None  # type: int
    LibrarySearchMethodID = None  # type: int
    LibraryFile = None  # type: str
    LibraryPath = None  # type: str
    LibraryType = None  # type: str
    ScreeningEnabled = None  # type: bool
    ScreeningType = None  # type: str
    NISTCompatibility = None  # type: bool
    PureWeightFactor = None  # type: float
    SearchOrder = None  # type: int
    RTCalibration = None  # type: str
    RTMatchFactorType = None  # type: str
    RTMaxPenalty = None  # type: float
    RTPenaltyType = None  # type: str
    RTRange = None  # type: float
    RTRangeNoPenalty = None  # type: float
    SpectrumThreshold = None  # type: float
    RemoveDuplicateHits = None  # type: bool
    AccurateMassTolerance = None  # type: float

    def __init__(self, *args, **kwargs):
        super(LibrarySearchMethodRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 21

    def __repr__(self):
        return (
            "<LibrarySearchMethodRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " IdentificationMethodID={}".format(self.IdentificationMethodID)
            + " LibrarySearchMethodID={}".format(self.LibrarySearchMethodID)
            + " LibraryFile={}".format(self.LibraryFile)
            + " ...>"
        )


class LibrarySearchMethodDataTable(TableBase):
    """Represents the LibrarySearchMethod table, containing LibrarySearchMethodRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[LibrarySearchMethodRow]
        super(LibrarySearchMethodDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> LibrarySearchMethodRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("LibrarySearchMethodDataTable", len(self.rows))


class IdentificationMethodRow(RowBase):
    """Represents a row for the IdentificationMethod table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    IdentificationMethodID = None  # type: int
    MaxHitCount = None  # type: int
    MaxMZ = None  # type: float
    MinMatchScore = None  # type: float
    MinMZ = None  # type: float
    RatioPercentUncertainty = None  # type: float
    MultiLibrarySearchType = None  # type: str
    LibrarySearchType = None  # type: str
    PerformExactMass = None  # type: bool
    ExactMassAllowMultiplyChargedIons = None  # type: bool
    ExactMassMaxIonsPerSpectrum = None  # type: int
    ExactMassMinRelativeAbundance = None  # type: float
    ExactMassMZDelta = None  # type: float
    ExactMassMinMZDelta = None  # type: float
    ExactMassPeakSelectionWeighting = None  # type: str

    def __init__(self, *args, **kwargs):
        super(IdentificationMethodRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 17

    def __repr__(self):
        return (
            "<IdentificationMethodRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " IdentificationMethodID={}".format(self.IdentificationMethodID)
            + " MaxHitCount={}".format(self.MaxHitCount)
            + " MaxMZ={}".format(self.MaxMZ)
            + " ...>"
        )


class IdentificationMethodDataTable(TableBase):
    """Represents the IdentificationMethod table, containing IdentificationMethodRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[IdentificationMethodRow]
        super(IdentificationMethodDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> IdentificationMethodRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("IdentificationMethodDataTable", len(self.rows))


class TargetCompoundRow(RowBase):
    """Represents a row for the TargetCompound table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    CompoundID = None  # type: int
    AgilentID = None  # type: str
    AverageResponseFactor = None  # type: float
    CASNumber = None  # type: str
    CellAcceleratorVoltage = None  # type: float
    CollisionEnergy = None  # type: float
    CompoundApproved = None  # type: bool
    CompoundGroup = None  # type: str
    CompoundName = None  # type: str
    CompoundType = None  # type: str
    ConcentrationUnits = None  # type: str
    FragmentorVoltage = None  # type: float
    Integrator = None  # type: str
    InstrumentType = None  # type: str
    IonPolarity = None  # type: str
    IonSource = None  # type: str
    ISTDCompoundID = None  # type: int
    ISTDConcentration = None  # type: float
    ISTDFlag = None  # type: bool
    KEGGID = None  # type: str
    LeftRetentionTimeDelta = None  # type: float
    LibraryMatchScore = None  # type: float
    MatrixSpikeConcentration = None  # type: float
    MolecularFormula = None  # type: str
    Multiplier = None  # type: float
    MZ = None  # type: float
    MZAdditional = None  # type: str
    MZExtractionWindowUnits = None  # type: str
    MZExtractionWindowFilterLeft = None  # type: float
    MZExtractionWindowFilterRight = None  # type: float
    MZScanRangeHigh = None  # type: float
    MZScanRangeLow = None  # type: float
    NoiseOfRawSignal = None  # type: float
    PrimaryHitPeakID = None  # type: str
    QuantitateByHeight = None  # type: bool
    ReferenceMSPathName = None  # type: str
    RelativeISTDMultiplier = None  # type: float
    RetentionTime = None  # type: float
    RetentionTimeDeltaUnits = None  # type: str
    RetentionTimeWindow = None  # type: float
    RetentionTimeWindowUnits = None  # type: str
    RightRetentionTimeDelta = None  # type: float
    ScanType = None  # type: str
    SelectedMZ = None  # type: float
    UncertaintyRelativeOrAbsolute = None  # type: str
    UserDefined = None  # type: str
    UserDefined1 = None  # type: str
    UserDefined2 = None  # type: str
    UserDefined3 = None  # type: str
    UserDefined4 = None  # type: str
    CompoundMath = None  # type: str
    UserAnnotation = None  # type: str
    UserCustomCalculation = None  # type: float
    RetentionIndex = None  # type: float
    ID = None  # type: int

    def __init__(self, *args, **kwargs):
        super(TargetCompoundRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 57

    def __repr__(self):
        return (
            "<TargetCompoundRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " CompoundID={}".format(self.CompoundID)
            + " AgilentID={}".format(self.AgilentID)
            + " AverageResponseFactor={}".format(self.AverageResponseFactor)
            + " ...>"
        )


class TargetCompoundDataTable(TableBase):
    """Represents the TargetCompound table, containing TargetCompoundRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[TargetCompoundRow]
        super(TargetCompoundDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> TargetCompoundRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("TargetCompoundDataTable", len(self.rows))


class PeakRow(RowBase):
    """Represents a row for the Peak table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    CompoundID = None  # type: int
    PeakID = None  # type: int
    Area = None  # type: float
    CalculatedConcentration = None  # type: float
    CoelutionScore = None  # type: float
    FinalConcentration = None  # type: float
    FullWidthHalfMaximum = None  # type: float
    Height = None  # type: float
    IntegrationMetricQualityFlags = None  # type: str
    IntegrationStartTime = None  # type: float
    IntegrationEndTime = None  # type: float
    Noise = None  # type: float
    ManuallyIntegrated = None  # type: bool
    MassAccuracy = None  # type: float
    MassMatchScore = None  # type: float
    MatrixSpikePercentRecovery = None  # type: float
    MZ = None  # type: float
    Plates = None  # type: int
    QValueComputed = None  # type: int
    RetentionIndex = None  # type: float
    RetentionTime = None  # type: float
    RetentionTimeDifference = None  # type: float
    ResolutionFront = None  # type: float
    ResolutionRear = None  # type: float
    SaturationRecoveryRatio = None  # type: float
    SignalToNoiseRatio = None  # type: float
    SurrogatePercentRecovery = None  # type: float
    Symmetry = None  # type: float
    TargetResponse = None  # type: float
    UserCustomCalculation = None  # type: float
    UserCustomCalculation1 = None  # type: float
    UserCustomCalculation2 = None  # type: float
    UserCustomCalculation3 = None  # type: float
    UserCustomCalculation4 = None  # type: float
    Width = None  # type: float
    ReferenceLibraryMatchScore = None  # type: float
    Purity = None  # type: float

    def __init__(self, *args, **kwargs):
        super(PeakRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 39

    def __repr__(self):
        return (
            "<PeakRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " CompoundID={}".format(self.CompoundID)
            + " PeakID={}".format(self.PeakID)
            + " Area={}".format(self.Area)
            + " ...>"
        )


class PeakDataTable(TableBase):
    """Represents the Peak table, containing PeakRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[PeakRow]
        super(PeakDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> PeakRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("PeakDataTable", len(self.rows))


class TargetQualifierRow(RowBase):
    """Represents a row for the TargetQualifier table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    CompoundID = None  # type: int
    QualifierID = None  # type: int
    CollisionEnergy = None  # type: float
    FragmentorVoltage = None  # type: float
    MZ = None  # type: float
    MZExtractionWindowUnits = None  # type: str
    MZExtractionWindowFilterLeft = None  # type: float
    MZExtractionWindowFilterRight = None  # type: float
    RelativeResponse = None  # type: float
    SelectedMZ = None  # type: float
    Uncertainty = None  # type: float

    def __init__(self, *args, **kwargs):
        super(TargetQualifierRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 13

    def __repr__(self):
        return (
            "<TargetQualifierRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " CompoundID={}".format(self.CompoundID)
            + " QualifierID={}".format(self.QualifierID)
            + " CollisionEnergy={}".format(self.CollisionEnergy)
            + " ...>"
        )


class TargetQualifierDataTable(TableBase):
    """Represents the TargetQualifier table, containing TargetQualifierRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[TargetQualifierRow]
        super(TargetQualifierDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> TargetQualifierRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("TargetQualifierDataTable", len(self.rows))


class PeakQualifierRow(RowBase):
    """Represents a row for the PeakQualifier table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    CompoundID = None  # type: int
    QualifierID = None  # type: int
    PeakID = None  # type: int
    Area = None  # type: float
    FullWidthHalfMaximum = None  # type: float
    Height = None  # type: float
    Noise = None  # type: str
    ManuallyIntegrated = None  # type: bool
    QualifierResponseRatio = None  # type: float
    RetentionTime = None  # type: float
    SignalToNoiseRatio = None  # type: float
    Symmetry = None  # type: float

    def __init__(self, *args, **kwargs):
        super(PeakQualifierRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 14

    def __repr__(self):
        return (
            "<PeakQualifierRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " CompoundID={}".format(self.CompoundID)
            + " QualifierID={}".format(self.QualifierID)
            + " PeakID={}".format(self.PeakID)
            + " ...>"
        )


class PeakQualifierDataTable(TableBase):
    """Represents the PeakQualifier table, containing PeakQualifierRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[PeakQualifierRow]
        super(PeakQualifierDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> PeakQualifierRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("PeakQualifierDataTable", len(self.rows))


class AnalysisRow(RowBase):
    """Represents a row for the Analysis table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    AnalysisID = None  # type: int
    SchemaVersion = None  # type: int
    AnalystName = None  # type: str
    AnalysisTime = None  # type: datetime.datetime
    DataVersion = None  # type: int
    ReportTime = None  # type: datetime.datetime
    StoreResultsPerSample = None  # type: bool
    AppVersion = None  # type: str
    BatchPath = None  # type: str
    AnalysisFileName = None  # type: str

    def __init__(self, *args, **kwargs):
        super(AnalysisRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 10

    def __repr__(self):
        return (
            "<AnalysisRow:"
            + " AnalysisID={}".format(self.AnalysisID)
            + " SchemaVersion={}".format(self.SchemaVersion)
            + " AnalystName={}".format(self.AnalystName)
            + " AnalysisTime={}".format(self.AnalysisTime)
            + " DataVersion={}".format(self.DataVersion)
            + " ...>"
        )


class AnalysisDataTable(TableBase):
    """Represents the Analysis table, containing AnalysisRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[AnalysisRow]
        super(AnalysisDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> AnalysisRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("AnalysisDataTable", len(self.rows))


class TargetMatchMethodRow(RowBase):
    """Represents a row for the TargetMatchMethod table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    TargetMatchMethodID = None  # type: int
    TargetFinalConcentrationRequired = None  # type: bool
    TargetResponseRequired = None  # type: bool
    TargetQualifierIonRatiosWithinRangeRequired = None  # type: bool
    TargetQualifierIonRequired = None  # type: bool
    HitContainsQuantifierIon = None  # type: bool
    HitContainsQualifierIons = None  # type: bool
    HitQualifierRatioWithinRange = None  # type: bool
    HitWithinTargetRTWindow = None  # type: bool
    ManualResponseFactor = None  # type: float
    MatchCompoundName = None  # type: bool
    MatchCASNumber = None  # type: bool
    HitConcentrationEstimation = None  # type: str

    def __init__(self, *args, **kwargs):
        super(TargetMatchMethodRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 15

    def __repr__(self):
        return (
            "<TargetMatchMethodRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " TargetMatchMethodID={}".format(self.TargetMatchMethodID)
            + " TargetFinalConcentrationRequired={}".format(
                self.TargetFinalConcentrationRequired
            )
            + " TargetResponseRequired={}".format(self.TargetResponseRequired)
            + " ...>"
        )


class TargetMatchMethodDataTable(TableBase):
    """Represents the TargetMatchMethod table, containing TargetMatchMethodRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[TargetMatchMethodRow]
        super(TargetMatchMethodDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> TargetMatchMethodRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("TargetMatchMethodDataTable", len(self.rows))


class AuxiliaryMethodRow(RowBase):
    """Represents a row for the AuxiliaryMethod table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    MZExtractIons = None  # type: str
    MZExtractionWindowFilterLeft = None  # type: float
    MZExtractionWindowFilterRight = None  # type: float
    MZExtractionWindowUnits = None  # type: str

    def __init__(self, *args, **kwargs):
        super(AuxiliaryMethodRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 6

    def __repr__(self):
        return (
            "<AuxiliaryMethodRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " MZExtractIons={}".format(self.MZExtractIons)
            + " MZExtractionWindowFilterLeft={}".format(
                self.MZExtractionWindowFilterLeft
            )
            + " MZExtractionWindowFilterRight={}".format(
                self.MZExtractionWindowFilterRight
            )
            + " ...>"
        )


class AuxiliaryMethodDataTable(TableBase):
    """Represents the AuxiliaryMethod table, containing AuxiliaryMethodRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[AuxiliaryMethodRow]
        super(AuxiliaryMethodDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> AuxiliaryMethodRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("AuxiliaryMethodDataTable", len(self.rows))


class BlankSubtractionMethodRow(RowBase):
    """Represents a row for the BlankSubtractionMethod table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    BlankSubtractionMethodID = None  # type: int
    PerformBlankSubtraction = None  # type: bool
    PeakThresholdType = None  # type: str
    PeakThreshold = None  # type: float
    RTWindowType = None  # type: str
    RTWindow = None  # type: float
    RTWindowFWHM = None  # type: float

    def __init__(self, *args, **kwargs):
        super(BlankSubtractionMethodRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 9

    def __repr__(self):
        return (
            "<BlankSubtractionMethodRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " BlankSubtractionMethodID={}".format(self.BlankSubtractionMethodID)
            + " PerformBlankSubtraction={}".format(self.PerformBlankSubtraction)
            + " PeakThresholdType={}".format(self.PeakThresholdType)
            + " ...>"
        )


class BlankSubtractionMethodDataTable(TableBase):
    """Represents the BlankSubtractionMethod table, containing BlankSubtractionMethodRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[BlankSubtractionMethodRow]
        super(BlankSubtractionMethodDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> BlankSubtractionMethodRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("BlankSubtractionMethodDataTable", len(self.rows))


class ExactMassRow(RowBase):
    """Represents a row for the ExactMass table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    DeconvolutionMethodID = None  # type: int
    ComponentID = None  # type: int
    HitID = None  # type: int
    ExactMassID = None  # type: int
    MassSource = None  # type: float
    MassExact = None  # type: float
    MassDeltaPpm = None  # type: float
    MassDeltaMda = None  # type: float
    FragmentFormula = None  # type: str
    Abundance = None  # type: float
    RelativeAbundance = None  # type: float
    Charge = None  # type: int
    IsUnique = None  # type: bool

    def __init__(self, *args, **kwargs):
        super(ExactMassRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 15

    def __repr__(self):
        return (
            "<ExactMassRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " DeconvolutionMethodID={}".format(self.DeconvolutionMethodID)
            + " ComponentID={}".format(self.ComponentID)
            + " HitID={}".format(self.HitID)
            + " ...>"
        )


class ExactMassDataTable(TableBase):
    """Represents the ExactMass table, containing ExactMassRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[ExactMassRow]
        super(ExactMassDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> ExactMassRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("ExactMassDataTable", len(self.rows))
