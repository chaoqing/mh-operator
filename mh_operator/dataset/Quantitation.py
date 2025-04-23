# -*- coding: utf-8 -*-
import datetime

from .Base import RowBase, TableBase


class BatchRow(RowBase):
    """Represents a row for the Batch table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    AcqDateTime = None  # type: datetime.datetime
    AcqDateTimeLocal = None  # type: Any
    AcqMethodFileName = None  # type: str
    AcqMethodPathName = None  # type: str
    AcqOperator = None  # type: str
    BalanceOverride = None  # type: str
    Barcode = None  # type: str
    CalibrationReferenceSampleID = None  # type: int
    Comment = None  # type: str
    Completed = None  # type: bool
    DADateTime = None  # type: datetime.datetime
    DAMethodFileName = None  # type: str
    DAMethodPathName = None  # type: str
    DataFileName = None  # type: str
    DataPathName = None  # type: str
    Dilution = None  # type: float
    DualInjector = None  # type: bool
    DualInjectorAcqDateTime = None  # type: datetime.datetime
    DualInjectorBarcode = None  # type: str
    DualInjectorExpectedBarcode = None  # type: str
    DualInjectorVial = None  # type: int
    DualInjectorVolume = None  # type: float
    EquilibrationTime = None  # type: float
    ExpectedBarcode = None  # type: str
    GraphicSampleChromatogram = None  # type: str
    InjectionsPerPosition = None  # type: int
    InjectorVolume = None  # type: float
    InstrumentName = None  # type: str
    InstrumentType = None  # type: str
    ISTDDilution = None  # type: float
    LevelName = None  # type: str
    Locked = None  # type: bool
    MatrixSpikeDilution = None  # type: float
    MatrixSpikeGroup = None  # type: str
    MatrixType = None  # type: str
    OutlierCCTime = None  # type: str
    PlateCode = None  # type: str
    PlatePosition = None  # type: str
    QuantitationMessage = None  # type: str
    RackCode = None  # type: str
    RackPosition = None  # type: str
    RunStartValvePositionDescription = None  # type: str
    RunStartValvePositionNumber = None  # type: str
    RunStopValvePositionDescription = None  # type: str
    RunStopValvePositionNumber = None  # type: str
    SampleAmount = None  # type: float
    SampleApproved = None  # type: bool
    SampleGroup = None  # type: str
    SampleInformation = None  # type: str
    SampleName = None  # type: str
    SamplePosition = None  # type: str
    SamplePrepFileName = None  # type: str
    SamplePrepPathName = None  # type: str
    SampleType = None  # type: str
    SamplingDateTime = None  # type: datetime.datetime
    SamplingTime = None  # type: float
    SequenceFileName = None  # type: str
    SequencePathName = None  # type: str
    SurrogateDilution = None  # type: float
    TotalSampleAmount = None  # type: float
    TuneFileLastTimeStamp = None  # type: datetime.datetime
    TuneFileName = None  # type: str
    TunePathName = None  # type: str
    TrayName = None  # type: str
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

    def __init__(self, *args, **kwargs):
        super(BatchRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 77

    def __repr__(self):
        return (
            "<BatchRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " AcqDateTime={}".format(self.AcqDateTime)
            + " AcqDateTimeLocal={}".format(self.AcqDateTimeLocal)
            + " AcqMethodFileName={}".format(self.AcqMethodFileName)
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


class TargetCompoundRow(RowBase):
    """Represents a row for the TargetCompound table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    CompoundID = None  # type: int
    AccuracyLimitMultiplierLOQ = None  # type: float
    AccuracyMaximumPercentDeviation = None  # type: float
    AgilentID = None  # type: str
    AlternativePeakCriteria = None  # type: str
    AlternativePeakID = None  # type: int
    AreaCorrectionFactor = None  # type: float
    AreaCorrectionSelectedMZ = None  # type: float
    AreaCorrectionMZ = None  # type: float
    AverageRelativeRetentionTime = None  # type: float
    AverageResponseFactor = None  # type: float
    AverageResponseFactorRSD = None  # type: float
    BlankResponseOffset = None  # type: float
    CalibrationRangeFilter = None  # type: str
    CalibrationReferenceCompoundID = None  # type: int
    CapacityFactorLimit = None  # type: float
    CASNumber = None  # type: str
    CCISTDResponseRatioLimitHigh = None  # type: float
    CCISTDResponseRatioLimitLow = None  # type: float
    CCResponseRatioLimitHigh = None  # type: float
    CCResponseRatioLimitLow = None  # type: float
    CellAcceleratorVoltage = None  # type: float
    CoelutionScoreLimit = None  # type: float
    CollisionEnergy = None  # type: float
    CollisionEnergyDelta = None  # type: float
    ColumnVoidTime = None  # type: float
    CompoundApproved = None  # type: bool
    CompoundGroup = None  # type: str
    CompoundMath = None  # type: str
    CompoundName = None  # type: str
    CompoundType = None  # type: str
    ConcentrationUnits = None  # type: str
    CurveFit = None  # type: str
    CurveFitFormula = None  # type: str
    CurveFitLimitHigh = None  # type: float
    CurveFitLimitLow = None  # type: float
    CurveFitMinimumR2 = None  # type: float
    CurveFitOrigin = None  # type: str
    CurveFitR2 = None  # type: float
    CurveFitStatus = None  # type: str
    CurveFitWeight = None  # type: str
    DilutionHighestConcentration = None  # type: float
    DilutionPattern = None  # type: str
    DynamicTargetCompoundID = None  # type: int
    DynamicTargetRank = None  # type: int
    ExpectedConcentration = None  # type: float
    FragmentorVoltage = None  # type: float
    FragmentorVoltageDelta = None  # type: float
    FullWidthHalfMaximumLimitHigh = None  # type: float
    FullWidthHalfMaximumLimitLow = None  # type: float
    GraphicPeakChromatogram = None  # type: str
    GraphicPeakQualifiers = None  # type: str
    GraphicPeakSpectrum = None  # type: str
    GraphicTargetCompoundCalibration = None  # type: str
    ID = None  # type: int
    IntegrationParameters = None  # type: str
    IntegrationParametersModified = None  # type: bool
    Integrator = None  # type: str
    IonPolarity = None  # type: str
    IonSource = None  # type: str
    ISTDCompoundID = None  # type: int
    ISTDConcentration = None  # type: float
    ISTDFlag = None  # type: bool
    ISTDResponseLimitHigh = None  # type: float
    ISTDResponseLimitLow = None  # type: float
    ISTDResponseMaximumPercentDeviation = None  # type: float
    ISTDResponseMinimumPercentDeviation = None  # type: float
    KEGGID = None  # type: str
    LeftRetentionTimeDelta = None  # type: float
    LibraryMatchScore = None  # type: float
    LibraryMatchScoreMinimum = None  # type: float
    LibraryRetentionIndex = None  # type: float
    LibraryRetentionTime = None  # type: float
    LimitOfDetection = None  # type: float
    LimitOfQuantitation = None  # type: float
    LinearResponseRangeMax = None  # type: float
    LinearResponseRangeMin = None  # type: float
    MassAccuracyLimit = None  # type: float
    MassMatchScoreMinimum = None  # type: float
    MatrixAConcentrationLimitHigh = None  # type: float
    MatrixAConcentrationLimitLow = None  # type: float
    MatrixBConcentrationLimitHigh = None  # type: float
    MatrixBConcentrationLimitLow = None  # type: float
    MatrixSpikeBConcentration = None  # type: float
    MatrixSpikeBPercentRecoveryMaximum = None  # type: float
    MatrixSpikeBPercentRecoveryMinimum = None  # type: float
    MatrixSpikeConcentration = None  # type: float
    MatrixSpikeMaximumPercentDeviation = None  # type: float
    MatrixSpikeBMaximumPercentDeviation = None  # type: float
    MatrixSpikePercentRecoveryMaximum = None  # type: float
    MatrixSpikePercentRecoveryMinimum = None  # type: float
    MatrixTypeOverride = None  # type: str
    MaximumAverageResponseFactorRSD = None  # type: float
    MaximumBlankConcentration = None  # type: float
    MaximumBlankResponse = None  # type: float
    MaximumCCResponseFactorDeviation = None  # type: float
    MaximumNumberOfHits = None  # type: int
    MaximumPercentResidual = None  # type: float
    MethodDetectionLimit = None  # type: float
    MinimumAverageResponseFactor = None  # type: float
    MinimumCCRelativeResponseFactor = None  # type: float
    MinimumPercentPurity = None  # type: float
    MinimumSignalToNoiseRatio = None  # type: float
    MolecularFormula = None  # type: str
    Multiplier = None  # type: float
    MZ = None  # type: float
    MZAdditional = None  # type: str
    MZExtractionWindowFilterLeft = None  # type: float
    MZExtractionWindowFilterRight = None  # type: float
    MZExtractionWindowUnits = None  # type: str
    MZScanRangeHigh = None  # type: float
    MZScanRangeLow = None  # type: float
    NeutralLossGain = None  # type: float
    NoiseAlgorithmType = None  # type: str
    NoiseOfRawSignal = None  # type: float
    NoiseReference = None  # type: str
    NoiseRegions = None  # type: str
    NoiseStandardDeviationMultiplier = None  # type: float
    NonReferenceWindowOverride = None  # type: float
    OutlierAlternativePeak = None  # type: str
    OutlierAverageResponseFactor = None  # type: str
    OutlierAverageResponseFactorRSD = None  # type: str
    OutlierBlankResponseOutsideLimit = None  # type: str
    OutlierCCAverageResponseFactor = None  # type: str
    OutlierCCRelativeResponseFactor = None  # type: str
    OutlierCustomCalculation = None  # type: str
    OutlierMethodDetectionLimit = None  # type: str
    OutlierMinimumCurveFitR2 = None  # type: str
    OutlierPeakNotFound = None  # type: str
    OutlierRelativeResponseFactor = None  # type: str
    OutlierRelativeStandardError = None  # type: str
    OutlierResponseCheckBelowLimit = None  # type: str
    OutlierResponseFactor = None  # type: str
    PeakFilterThreshold = None  # type: str
    PeakFilterThresholdValue = None  # type: float
    PeakSelectionCriterion = None  # type: str
    PlatesCalculationType = None  # type: str
    PlatesLimit = None  # type: int
    PrimaryHitPeakID = None  # type: int
    QCLCSMaximumRecoveryA = None  # type: float
    QCLCSMaximumRecoveryB = None  # type: float
    QCLCSMinimumRecoveryA = None  # type: float
    QCLCSMinimumRecoveryB = None  # type: float
    QCMaximumDeviation = None  # type: float
    QCMaximumPercentRSD = None  # type: float
    QualifierRatioMethod = None  # type: int
    QuantitateByHeight = None  # type: bool
    QuantitationMessage = None  # type: str
    QValueMinimum = None  # type: int
    ReferenceMSPathName = None  # type: str
    ReferenceWindowOverride = None  # type: float
    RelativeISTDMultiplier = None  # type: float
    RelativeResponseFactorMaximumPercentDeviation = None  # type: float
    RelativeRetentionTimeMaximumPercentDeviation = None  # type: float
    RelativeStandardError = None  # type: float
    RelativeStandardErrorMaximum = None  # type: float
    ResolutionCalculationType = None  # type: str
    ResolutionLimit = None  # type: float
    ResponseCheckMinimum = None  # type: float
    ResponseFactorMaximumPercentDeviation = None  # type: float
    RetentionIndex = None  # type: float
    RetentionTime = None  # type: float
    RetentionTimeDeltaUnits = None  # type: str
    RetentionTimeWindow = None  # type: float
    RetentionTimeWindowCC = None  # type: float
    RetentionTimeWindowUnits = None  # type: str
    RightRetentionTimeDelta = None  # type: float
    RxUnlabeledIsotopicDilution = None  # type: float
    RyLabeledIsotopicDilution = None  # type: float
    SampleAmountLimitHigh = None  # type: float
    SampleAmountLimitLow = None  # type: float
    SampleMaximumPercentRSD = None  # type: float
    ScanType = None  # type: str
    SelectedMZ = None  # type: float
    SignalInstance = None  # type: int
    SignalName = None  # type: str
    SignalRetentionTimeOffset = None  # type: float
    SignalToNoiseMultiplier = None  # type: float
    SignalType = None  # type: str
    Smoothing = None  # type: str
    SmoothingFunctionWidth = None  # type: int
    SmoothingGaussianWidth = None  # type: float
    Species = None  # type: str
    SpectrumBaselineThreshold = None  # type: float
    SpectrumExtractionOverride = None  # type: str
    SpectrumScanInclusion = None  # type: str
    SpectrumPeakHeightPercentThreshold = None  # type: float
    SpectrumPercentSaturationThreshold = None  # type: float
    SpectrumQuantifierQualifierOnly = None  # type: bool
    Sublist = None  # type: bool
    SurrogateConcentration = None  # type: float
    SurrogateConcentrationLimitHigh = None  # type: float
    SurrogateConcentrationLimitLow = None  # type: float
    SurrogatePercentRecoveryMaximum = None  # type: float
    SurrogatePercentRecoveryMinimum = None  # type: float
    SymmetryCalculationType = None  # type: str
    SymmetryLimitHigh = None  # type: float
    SymmetryLimitLow = None  # type: float
    TargetCompoundIDStatus = None  # type: str
    ThresholdNumberOfPeaks = None  # type: int
    TimeReferenceFlag = None  # type: bool
    TimeSegment = None  # type: int
    Transition = None  # type: str
    TriggeredTransitions = None  # type: str
    UncertaintyRelativeOrAbsolute = None  # type: str
    UserAnnotation = None  # type: str
    UserCustomCalculation = None  # type: float
    UserCustomCalculationLimitHigh = None  # type: float
    UserCustomCalculationLimitLow = None  # type: float
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
    UserDefinedTargetCompoundID = None  # type: int
    WavelengthExtractionRangeHigh = None  # type: float
    WavelengthExtractionRangeLow = None  # type: float
    WavelengthReferenceRangeHigh = None  # type: float
    WavelengthReferenceRangeLow = None  # type: float

    def __init__(self, *args, **kwargs):
        super(TargetCompoundRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 226

    def __repr__(self):
        return (
            "<TargetCompoundRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " CompoundID={}".format(self.CompoundID)
            + " AccuracyLimitMultiplierLOQ={}".format(self.AccuracyLimitMultiplierLOQ)
            + " AccuracyMaximumPercentDeviation={}".format(
                self.AccuracyMaximumPercentDeviation
            )
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


class TargetQualifierRow(RowBase):
    """Represents a row for the TargetQualifier table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    CompoundID = None  # type: int
    QualifierID = None  # type: int
    AreaSum = None  # type: bool
    CellAcceleratorVoltage = None  # type: float
    CollisionEnergy = None  # type: float
    CollisionEnergyDelta = None  # type: float
    FragmentorVoltage = None  # type: float
    FragmentorVoltageDelta = None  # type: float
    GraphicPeakQualifierChromatogram = None  # type: str
    IntegrationParameters = None  # type: str
    IntegrationParametersModified = None  # type: bool
    IonPolarity = None  # type: str
    MZ = None  # type: float
    MZExtractionWindowFilterLeft = None  # type: float
    MZExtractionWindowFilterRight = None  # type: float
    MZExtractionWindowUnits = None  # type: str
    OutlierPeakNotFound = None  # type: str
    PeakFilterThreshold = None  # type: str
    PeakFilterThresholdValue = None  # type: float
    QualifierName = None  # type: str
    QualifierRangeMaximum = None  # type: float
    QualifierRangeMinimum = None  # type: float
    QuantitationMessage = None  # type: str
    RelativeResponse = None  # type: float
    ScanType = None  # type: str
    SelectedMZ = None  # type: float
    ThresholdNumberOfPeaks = None  # type: int
    Transition = None  # type: str
    Uncertainty = None  # type: float
    UserDefined = None  # type: str

    def __init__(self, *args, **kwargs):
        super(TargetQualifierRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 32

    def __repr__(self):
        return (
            "<TargetQualifierRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " CompoundID={}".format(self.CompoundID)
            + " QualifierID={}".format(self.QualifierID)
            + " AreaSum={}".format(self.AreaSum)
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


class PeakRow(RowBase):
    """Represents a row for the Peak table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    CompoundID = None  # type: int
    PeakID = None  # type: int
    Accuracy = None  # type: float
    AlternativePeakRTDiff = None  # type: float
    AlternativeTargetHit = None  # type: str
    Area = None  # type: float
    AreaCorrectionResponse = None  # type: float
    BaselineDraw = None  # type: str
    BaselineEnd = None  # type: float
    BaselineEndOriginal = None  # type: float
    BaselineStandardDeviation = None  # type: float
    BaselineStart = None  # type: float
    BaselineStartOriginal = None  # type: float
    CalculatedConcentration = None  # type: float
    CapacityFactor = None  # type: float
    CCISTDResponseRatio = None  # type: float
    CCResponseRatio = None  # type: float
    EstimatedConcentration = None  # type: str
    FinalConcentration = None  # type: float
    FullWidthHalfMaximum = None  # type: float
    GroupNumber = None  # type: int
    Height = None  # type: float
    IntegrationEndTime = None  # type: float
    IntegrationEndTimeOriginal = None  # type: float
    IntegrationMetricQualityFlags = None  # type: str
    IntegrationQualityMetric = None  # type: str
    IntegrationStartTime = None  # type: float
    IntegrationStartTimeOriginal = None  # type: float
    ISTDConcentrationRatio = None  # type: float
    ISTDResponsePercentDeviation = None  # type: float
    ISTDResponseRatio = None  # type: float
    ManuallyIntegrated = None  # type: bool
    MassAbundanceScore = None  # type: float
    MassAccuracy = None  # type: float
    MassAccuracyScore = None  # type: float
    MassMatchScore = None  # type: float
    MassSpacingScore = None  # type: float
    MatrixSpikePercentDeviation = None  # type: float
    MatrixSpikePercentRecovery = None  # type: float
    MZ = None  # type: float
    Noise = None  # type: float
    NoiseRegions = None  # type: str
    OutlierAccuracy = None  # type: str
    OutlierBelowLimitOfDetection = None  # type: str
    OutlierBelowLimitOfQuantitation = None  # type: str
    OutlierBlankConcentrationOutsideLimit = None  # type: str
    OutlierCapacityFactor = None  # type: str
    OutlierCCISTDResponseRatio = None  # type: str
    OutlierCCResponseRatio = None  # type: str
    OutlierCCRetentionTime = None  # type: str
    OutlierFullWidthHalfMaximum = None  # type: str
    OutlierIntegrationQualityMetric = None  # type: str
    OutlierISTDResponse = None  # type: str
    OutlierISTDResponsePercentDeviation = None  # type: str
    OutlierLibraryMatchScore = None  # type: str
    OutlierMassAccuracy = None  # type: str
    OutlierMassMatchScore = None  # type: str
    OutlierMatrixSpikeGroupRecovery = None  # type: str
    OutlierMatrixSpikeOutOfLimits = None  # type: str
    OutlierMatrixSpikeOutsidePercentDeviation = None  # type: str
    OutlierMatrixSpikePercentRecovery = None  # type: str
    OutlierOutOfCalibrationRange = None  # type: str
    OutlierPlates = None  # type: str
    OutlierPurity = None  # type: str
    OutlierQCLCSRecoveryOutOfLimits = None  # type: str
    OutlierQCOutOfLimits = None  # type: str
    OutlierQCOutsideRSD = None  # type: str
    OutlierQValue = None  # type: str
    OutlierRelativeRetentionTime = None  # type: str
    OutlierResolutionFront = None  # type: str
    OutlierResolutionRear = None  # type: str
    OutlierRetentionTime = None  # type: str
    OutlierSampleAmountOutOfLimits = None  # type: str
    OutlierSampleOutsideRSD = None  # type: str
    OutlierSaturationRecovery = None  # type: str
    OutlierSignalToNoiseRatioBelowLimit = None  # type: str
    OutlierSurrogateOutOfLimits = None  # type: str
    OutlierSurrogatePercentRecovery = None  # type: str
    OutlierSymmetry = None  # type: str
    Plates = None  # type: int
    Purity = None  # type: float
    QValueComputed = None  # type: int
    QValueSort = None  # type: int
    ReferenceLibraryMatchScore = None  # type: float
    RelativeRetentionTime = None  # type: float
    ResolutionFront = None  # type: float
    ResolutionRear = None  # type: float
    ResponseRatio = None  # type: float
    RetentionIndex = None  # type: float
    RetentionTime = None  # type: float
    RetentionTimeDifference = None  # type: float
    RetentionTimeDifferenceKey = None  # type: int
    RetentionTimeOriginal = None  # type: float
    SampleRSD = None  # type: float
    SaturationRecoveryRatio = None  # type: float
    SelectedGroupRetentionTime = None  # type: float
    SelectedTargetRetentionTime = None  # type: float
    SignalToNoiseRatio = None  # type: float
    SurrogatePercentRecovery = None  # type: float
    Symmetry = None  # type: float
    TargetResponse = None  # type: float
    TargetResponseOriginal = None  # type: float
    UserCustomCalculation = None  # type: float
    UserCustomCalculation1 = None  # type: float
    UserCustomCalculation2 = None  # type: float
    UserCustomCalculation3 = None  # type: float
    UserCustomCalculation4 = None  # type: float
    Width = None  # type: float

    def __init__(self, *args, **kwargs):
        super(PeakRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 110

    def __repr__(self):
        return (
            "<PeakRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " CompoundID={}".format(self.CompoundID)
            + " PeakID={}".format(self.PeakID)
            + " Accuracy={}".format(self.Accuracy)
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


class PeakQualifierRow(RowBase):
    """Represents a row for the PeakQualifier table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    CompoundID = None  # type: int
    PeakID = None  # type: int
    QualifierID = None  # type: int
    Area = None  # type: float
    BaselineEnd = None  # type: float
    BaselineEndOriginal = None  # type: float
    BaselineStandardDeviation = None  # type: float
    BaselineStart = None  # type: float
    BaselineStartOriginal = None  # type: float
    CoelutionScore = None  # type: float
    FullWidthHalfMaximum = None  # type: float
    Height = None  # type: float
    IntegrationEndTime = None  # type: float
    IntegrationEndTimeOriginal = None  # type: float
    IntegrationMetricQualityFlags = None  # type: str
    IntegrationQualityMetric = None  # type: str
    IntegrationStartTime = None  # type: float
    IntegrationStartTimeOriginal = None  # type: float
    ManuallyIntegrated = None  # type: bool
    MassAccuracy = None  # type: float
    MZ = None  # type: float
    Noise = None  # type: float
    NoiseRegions = None  # type: str
    OutlierQualifierCoelutionScore = None  # type: str
    OutlierQualifierFullWidthHalfMaximum = None  # type: str
    OutlierQualifierIntegrationQualityMetric = None  # type: str
    OutlierQualifierMassAccuracy = None  # type: str
    OutlierQualifierOutOfLimits = None  # type: str
    OutlierQualifierResolutionFront = None  # type: str
    OutlierQualifierResolutionRear = None  # type: str
    OutlierQualifierSignalToNoiseRatio = None  # type: str
    OutlierQualifierSymmetry = None  # type: str
    OutlierSaturationRecovery = None  # type: str
    QualifierResponseRatio = None  # type: float
    QualifierResponseRatioOriginal = None  # type: float
    ResolutionFront = None  # type: float
    ResolutionRear = None  # type: float
    RetentionTime = None  # type: float
    RetentionTimeOriginal = None  # type: float
    SaturationRecoveryRatio = None  # type: float
    SignalToNoiseRatio = None  # type: float
    Symmetry = None  # type: float
    UserCustomCalculation = None  # type: float

    def __init__(self, *args, **kwargs):
        super(PeakQualifierRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 45

    def __repr__(self):
        return (
            "<PeakQualifierRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " CompoundID={}".format(self.CompoundID)
            + " PeakID={}".format(self.PeakID)
            + " QualifierID={}".format(self.QualifierID)
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


class CalibrationRow(RowBase):
    """Represents a row for the Calibration table."""

    # --- Class Attributes with Type Hints (for static analysis) ---
    BatchID = None  # type: int
    SampleID = None  # type: int
    CompoundID = None  # type: int
    LevelID = None  # type: int
    CalibrationSTDAcquisitionDateTime = None  # type: datetime.datetime
    CalibrationSTDPathName = None  # type: str
    CalibrationType = None  # type: str
    LevelAverageCounter = None  # type: float
    LevelConcentration = None  # type: float
    LevelEnable = None  # type: bool
    LevelLastUpdateTime = None  # type: datetime.datetime
    LevelName = None  # type: str
    LevelResponse = None  # type: float
    LevelResponseFactor = None  # type: float
    LevelRSD = None  # type: float

    def __init__(self, *args, **kwargs):
        super(CalibrationRow, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return 15

    def __repr__(self):
        return (
            "<CalibrationRow:"
            + " BatchID={}".format(self.BatchID)
            + " SampleID={}".format(self.SampleID)
            + " CompoundID={}".format(self.CompoundID)
            + " LevelID={}".format(self.LevelID)
            + " CalibrationSTDAcquisitionDateTime={}".format(
                self.CalibrationSTDAcquisitionDateTime
            )
            + " ...>"
        )


class CalibrationDataTable(TableBase):
    """Represents the Calibration table, containing CalibrationRow objects."""

    def __init__(self, *args, **kwargs):
        self.rows = []  # type: list[CalibrationRow]
        super(CalibrationDataTable, self).__init__(*args, **kwargs)

    def __len__(self):
        # type: () -> int
        return len(self.rows)

    def __iter__(self):
        # type: () -> iter
        return iter(self.rows)

    def __getitem__(self, index):
        # type: (int) -> CalibrationRow
        return self.rows[index]

    def __repr__(self):
        return "<{}: {} rows>".format("CalibrationDataTable", len(self.rows))
