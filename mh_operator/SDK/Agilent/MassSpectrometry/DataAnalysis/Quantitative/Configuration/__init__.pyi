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

from . import (
    ChromatogramAutoScaleType,
    ChromatogramPeakLabelType,
    CurveFitOrigin,
    CurveFitType,
    CurveFitWeighting,
    GridExportMode,
    InstrumentType,
    IntegratorType,
    INumericCustomFormat,
    MethodEditTaskMode,
    OutlierColumns,
    PlotTitleElement,
    Properties,
    QualifierInfoLabelType,
    ScanType,
)
from .Compliance import IDataStorage

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration

class CalCurveConfiguration:  # Class
    AssistantDisabledPointColor: System.Drawing.Color  # static
    AssistantDisabledPointLineColor: System.Drawing.Color  # static
    AssistantPointColor: System.Drawing.Color  # static
    AssistantPointLineColor: System.Drawing.Color  # static
    AutoScaleToEnabledPoints: bool  # static
    AxisTitleConcentration: str  # static # readonly
    AxisTitleISTDResponse: str  # static # readonly
    AxisTitleRelativeConcentration: str  # static # readonly
    AxisTitleRelativeResponse: str  # static # readonly
    AxisTitleResponse: str  # static # readonly
    BackColor: System.Drawing.Color  # static
    CCFillColor: System.Drawing.Color  # static
    CCLineColor: System.Drawing.Color  # static
    CurrentCalibrationSampleMarkerColor: System.Drawing.Color  # static
    CurrentSampleMarkerColor: System.Drawing.Color  # static
    CurveColor: System.Drawing.Color  # static
    DefaultAutoScaleToEnabledPoints: bool  # static # readonly
    DefaultBackColor: System.Drawing.Color  # static # readonly
    DefaultCCFillColor: System.Drawing.Color  # static # readonly
    DefaultCCLineColor: System.Drawing.Color  # static # readonly
    DefaultCurrentCalibrationSampleMarkerColor: (
        System.Drawing.Color
    )  # static # readonly
    DefaultCurrentSampleMarkerColor: System.Drawing.Color  # static # readonly
    DefaultCurveColor: System.Drawing.Color  # static # readonly
    DefaultForeColor: System.Drawing.Color  # static # readonly
    DefaultGridlinesColor: System.Drawing.Color  # static # readonly
    DefaultGridlinesVisible: bool  # static # readonly
    DefaultIstdResponsesColor: System.Drawing.Color  # static # readonly
    DefaultPointColor: System.Drawing.Color  # static # readonly
    DefaultPointSize: int  # static # readonly
    DefaultQCFillColor: System.Drawing.Color  # static # readonly
    DefaultQCLineColor: System.Drawing.Color  # static # readonly
    DefaultRelativeConcentration: bool  # static # readonly
    DefaultShowCC: bool  # static # readonly
    DefaultShowCurrentSampleMarker: bool  # static # readonly
    DefaultShowIstdResponses: bool  # static # readonly
    DefaultShowQC: bool  # static # readonly
    DefaultShowStandardDeviationBars: bool  # static # readonly
    DefaultStandardDeviationBarColor: System.Drawing.Color  # static # readonly
    DisabledPointColor: System.Drawing.Color  # static
    DisabledPointLineColor: System.Drawing.Color  # static
    FontSize: float  # static
    ForeColor: System.Drawing.Color  # static
    GridlinesColor: System.Drawing.Color  # static
    GridlinesVisible: bool  # static
    IstdResponsesColor: System.Drawing.Color  # static
    PaneBorderColor: System.Drawing.Color  # static
    PaneBorderWidth: int  # static
    PointColor: System.Drawing.Color  # static
    PointLineColor: System.Drawing.Color  # static
    PointSize: int  # static
    PrintLandscape: bool  # static
    PrintPageSettings: str  # static
    QCFillColor: System.Drawing.Color  # static
    QCLineColor: System.Drawing.Color  # static
    RelativeConcentration: bool  # static
    ShowCC: bool  # static
    ShowCoefficients: bool  # static
    ShowCurrentSampleMarker: bool  # static
    ShowIstdResponse: bool  # static
    ShowQC: bool  # static
    ShowStandardDeviationBars: bool  # static
    StandardDeviationBarColor: System.Drawing.Color  # static
    XLogScale: bool  # static
    YLogScale: bool  # static

    @staticmethod
    def CopyTo(configuration: System.Configuration.Configuration) -> None: ...
    @staticmethod
    def CopyFrom(configuration: System.Configuration.Configuration) -> None: ...
    @staticmethod
    def GetAvailableCurveFitTypes() -> List[CurveFitType]: ...
    @staticmethod
    def GetAvailableCurveFitWeightings() -> List[CurveFitWeighting]: ...
    @staticmethod
    def SetAssistantVisibleColumns(columns: List[str]) -> None: ...
    @staticmethod
    def GetAvailableCurveFitOrigins() -> List[CurveFitOrigin]: ...
    @staticmethod
    def GetAssistantVisibleColumns() -> List[str]: ...

class ChromSpecConfiguration:  # Class
    AbundanceLabelFormat: str  # static
    AlternatePeakFillColor: System.Drawing.Color  # static
    BackColor: System.Drawing.Color  # static
    ChromatogramLineWidth: int  # static
    DeconvolutedComponentColors: List[System.Drawing.Color]  # static
    DefaultAbundanceLabelFormat: str  # static # readonly
    DefaultAlternatePeakFillColor: System.Drawing.Color  # static # readonly
    DefaultBackColor: System.Drawing.Color  # static # readonly
    DefaultChromatogramLineWidth: int  # static # readonly
    DefaultDeconvolutedComponentColors: List[System.Drawing.Color]  # static # readonly
    DefaultFillAllQualifierPeaks: bool  # static # readonly
    DefaultFillOutofLimitQualifierPeaks: bool  # static # readonly
    DefaultFillPeaksTransparency: int  # static # readonly
    DefaultFillTargetPeaksInQualifiers: bool  # static # readonly
    DefaultForeColor: System.Drawing.Color  # static # readonly
    DefaultGridlinesColor: System.Drawing.Color  # static # readonly
    DefaultGridlinesVisible: bool  # static # readonly
    DefaultMIOutlierQualifierTitleColor: System.Drawing.Color  # static # readonly
    DefaultMaxColumnsPerPage: int  # static # readonly
    DefaultNoiseRegionsColor: System.Drawing.Color  # static # readonly
    DefaultNormalizeQualifiers: bool  # static # readonly
    DefaultNormalizeQuantifier: bool  # static # readonly
    DefaultOverrideSpectrum: bool  # static # readonly
    DefaultPrecursorColor: System.Drawing.Color  # static # readonly
    DefaultPrecursorFill: bool  # static # readonly
    DefaultPrecursorSize: int  # static # readonly
    DefaultPrimaryPeakAcceptedFillColor: System.Drawing.Color  # static # readonly
    DefaultPrimaryPeakInspectFillColor: System.Drawing.Color  # static # readonly
    DefaultPrimaryPeakManualIntegratedFillColor: (
        System.Drawing.Color
    )  # static # readonly
    DefaultPrimaryPeakRejectedFillColor: System.Drawing.Color  # static # readonly
    DefaultQualifierColors: List[System.Drawing.Color]  # static # readonly
    DefaultQualifierInfoLabelType: QualifierInfoLabelType  # static # readonly
    DefaultQualifiersTransparency: int  # static # readonly
    DefaultReferenceRetentionTimeColor: System.Drawing.Color  # static # readonly
    DefaultReferenceRetentionTimeDashStyle: (
        System.Drawing.Drawing2D.DashStyle
    )  # static # readonly
    DefaultReferenceWindowColor: System.Drawing.Color  # static # readonly
    DefaultReferenceWindowDashStyle: (
        System.Drawing.Drawing2D.DashStyle
    )  # static # readonly
    DefaultShowBaselineCalculationPoints: bool  # static # readonly
    DefaultShowBaselines: bool  # static # readonly
    DefaultShowChromatogramPeakLabelCaption: bool  # static # readonly
    DefaultShowChromatogramPeakLabelUnits: bool  # static # readonly
    DefaultShowComponentSpectrum: bool  # static # readonly
    DefaultShowDeconvolutedComponents: bool  # static # readonly
    DefaultShowDefaultChromTitle: bool  # static # readonly
    DefaultShowMassIndicators: bool  # static # readonly
    DefaultShowMatchScores: bool  # static # readonly
    DefaultShowNoiseRegions: bool  # static # readonly
    DefaultShowOriginalBaselines: bool  # static # readonly
    DefaultShowPatternSpectra: bool  # static # readonly
    DefaultShowQualifierAnnotations: bool  # static # readonly
    DefaultShowQualifierCoelutionScore: bool  # static # readonly
    DefaultShowReferenceLibrarySource: bool  # static # readonly
    DefaultShowReferenceRetentionTime: bool  # static # readonly
    DefaultShowReferenceSpectrum: bool  # static # readonly
    DefaultShowReferenceWindow: bool  # static # readonly
    DefaultShowTimeSegmentBorder: bool  # static # readonly
    DefaultShowUncertaintyBand: bool  # static # readonly
    DefaultSpectrumLineWidth: int  # static # readonly
    DefaultTimeSegmentBorderColor: System.Drawing.Color  # static # readonly
    DefaultUncertaintyBandDashStyle: (
        System.Drawing.Drawing2D.DashStyle
    )  # static # readonly
    DefaultWrapTitle: bool  # static # readonly
    FillAllQualifierPeaks: bool  # static
    FillOutofLimitQualifierPeaks: bool  # static
    FillPeaks: bool  # static
    FillPeaksTransparency: int  # static
    FillTargetPeaksInQualifiers: bool  # static
    FontSize: float  # static
    ForeColor: System.Drawing.Color  # static
    GridlinesColor: System.Drawing.Color  # static
    GridlinesVisible: bool  # static
    IstdOverlayAutoScaleType: ChromatogramAutoScaleType  # static
    IstdPeakAutoScaleType: ChromatogramAutoScaleType  # static
    IstdSpectrumAutoScaleType: ChromatogramAutoScaleType  # static
    MIOutlierQualifierTitleColor: System.Drawing.Color  # static
    MaxColumnsPerPage: int  # static
    NoiseRegionsColor: System.Drawing.Color  # static
    NormalizeQualifiers: bool  # static
    NormalizeQuantifier: bool  # static
    OriginalBaselineColor: System.Drawing.Color  # static
    OriginalBaselineWidth: float  # static
    OverlayAutoScaleType: ChromatogramAutoScaleType  # static
    Overlay_BackColor: System.Drawing.Color  # static
    Overlay_FontSize: float  # static
    Overlay_ForeColor: System.Drawing.Color  # static
    Overlay_GridlinesColor: System.Drawing.Color  # static
    Overlay_GridlinesVisible: bool  # static
    Overlay_ShowTimeSegmentBorder: bool  # static
    Overlay_TimeSegmentBorderColor: System.Drawing.Color  # static
    OverrideSpectrum: bool  # static
    PaneBorderColor: System.Drawing.Color  # static
    PaneBorderWidth: int  # static
    PlotColor: System.Drawing.Color  # static
    PrecursorColor: System.Drawing.Color  # static
    PrecursorFill: bool  # static
    PrecursorSize: int  # static
    PrimaryPeakAcceptedFillColor: System.Drawing.Color  # static
    PrimaryPeakInspectFillColor: System.Drawing.Color  # static
    PrimaryPeakManualIntegratedFillColor: System.Drawing.Color  # static
    PrimaryPeakRejectedFillColor: System.Drawing.Color  # static
    PrintLandscape: bool  # static
    PrintPageSettings: str  # static
    QualifierColors: List[System.Drawing.Color]  # static
    QualifierInfoLabelType: QualifierInfoLabelType  # static
    QualifiersTransparency: int  # static
    ReferenceRetentionTimeColor: System.Drawing.Color  # static
    ReferenceRetentionTimeDashStyle: System.Drawing.Drawing2D.DashStyle  # static
    ReferenceWindowColor: System.Drawing.Color  # static
    ReferenceWindowDashStyle: System.Drawing.Drawing2D.DashStyle  # static
    SelectedPaneBorderColor: System.Drawing.Color  # static
    ShowBaselineCalculationPoints: bool  # static
    ShowBaselines: bool  # static
    ShowChromatogram: bool  # static
    ShowChromatogramPeakLabelCaption: bool  # static
    ShowChromatogramPeakLabelUnits: bool  # static
    ShowComponentSpectrum: bool  # static
    ShowDeconvolutedComponents: bool  # static
    ShowDefaultChromTitle: bool  # static
    ShowIstd: bool  # static
    ShowManualIntegratoinHandles: bool  # static
    ShowMassIndicators: bool  # static
    ShowMatchScores: bool  # static
    ShowNoiseRegions: bool  # static
    ShowOriginalBaselines: bool  # static
    ShowPatternSpectra: bool  # static
    ShowPeakLabels: bool  # static
    ShowQualifierAnnotations: bool  # static
    ShowQualifierCoelutionScore: bool  # static
    ShowQualifiers: bool  # static
    ShowReferenceLibrarySource: bool  # static
    ShowReferenceRetentionTime: bool  # static
    ShowReferenceSpectrum: bool  # static
    ShowReferenceWindow: bool  # static
    ShowSpectrum: bool  # static
    ShowTimeSegmentBorder: bool  # static
    ShowUncertaintyBand: bool  # static
    SpectrumAutoScaleType: ChromatogramAutoScaleType  # static
    SpectrumLineWidth: int  # static
    Spectrum_BackColor: System.Drawing.Color  # static
    Spectrum_FontSize: float  # static
    Spectrum_ForeColor: System.Drawing.Color  # static
    Spectrum_GridlinesColor: System.Drawing.Color  # static
    Spectrum_GridlinesVisible: bool  # static
    TargetPeakAutoScaleType: ChromatogramAutoScaleType  # static
    TimeSegmentBorderColor: System.Drawing.Color  # static
    UncertaintyBandDashStyle: System.Drawing.Drawing2D.DashStyle  # static
    WrapTitle_Chromatogram: bool  # static
    WrapTitle_Overlay: bool  # static
    WrapTitle_Spectrum: bool  # static

    @staticmethod
    def CopyTo(config: System.Configuration.Configuration) -> None: ...
    @staticmethod
    def CopyFrom(config: System.Configuration.Configuration) -> None: ...
    @staticmethod
    def GetChromatogramPeakLabels() -> List[ChromatogramPeakLabelType]: ...
    @staticmethod
    def GetDefaultChromatogramPeakLabels() -> List[ChromatogramPeakLabelType]: ...
    @staticmethod
    def SetChromatogramPeakLabels(types: List[ChromatogramPeakLabelType]) -> None: ...
    @staticmethod
    def GetCaptionFromPeakLabelType(
        type: ChromatogramPeakLabelType, instrumentType: InstrumentType
    ) -> str: ...
    @staticmethod
    def SetChromTitleElements(elements: List[PlotTitleElement]) -> None: ...
    @staticmethod
    def GetChromTitleElements() -> List[PlotTitleElement]: ...
    @staticmethod
    def GetDefaultChromTitleElements() -> List[PlotTitleElement]: ...

class ChromatogramInformationConfiguration:  # Class
    AutoScaleAfter: float  # static
    BackColor: System.Drawing.Color  # static
    DefaultBackColor: System.Drawing.Color  # static # readonly
    DefaultForeColor: System.Drawing.Color  # static # readonly
    DefaultGridlinesColor: System.Drawing.Color  # static # readonly
    DefaultGridlinesVisible: bool  # static # readonly
    DefaultLinkXAxes: bool  # static # readonly
    DefaultLinkYAxes: bool  # static # readonly
    DefaultMaxNumRowsPerPage: int  # static # readonly
    DefaultPeakLabelsAllowOverlap: bool  # static # readonly
    DefaultPeakLabelsAnchorOnly: bool  # static # readonly
    DefaultPeakLabelsCaption: bool  # static # readonly
    DefaultPeakLabelsUnits: bool  # static # readonly
    DefaultPeakLabelsVertical: bool  # static # readonly
    ForeColor: System.Drawing.Color  # static
    GridlinesColor: System.Drawing.Color  # static
    GridlinesVisible: bool  # static
    HeadToTail: bool  # static
    LastCodec: str  # static
    LastExportFileName: str  # static
    LinkXAxes: bool  # static
    LinkYAxes: bool  # static
    MaxNumRowsPerPage: int  # static
    Overlay: bool  # static
    PaneBorderColor: System.Drawing.Color  # static
    PaneBorderWidth: int  # static # readonly
    PeakLabelsAllowOverlap: bool  # static
    PeakLabelsAnchorOnly: bool  # static
    PeakLabelsCaption: bool  # static
    PeakLabelsUnits: bool  # static
    PeakLabelsVertical: bool  # static
    PrintLandscape: bool  # static
    PrintPageSettings: str  # static
    SelectedPaneBorderColor: System.Drawing.Color  # static
    ShowDefaultTitle: bool  # static
    SynchronizeNavigation: bool  # static

    @staticmethod
    def GetTitleElements() -> List[PlotTitleElement]: ...
    @staticmethod
    def GetChromatogramPeakLabels() -> List[ChromatogramPeakLabelType]: ...
    @staticmethod
    def GetDefaultChromatogramPeakLabels() -> List[ChromatogramPeakLabelType]: ...
    @staticmethod
    def SetChromatogramPeakLabels(types: List[ChromatogramPeakLabelType]) -> None: ...
    @staticmethod
    def GetDefaultTitleElements() -> List[PlotTitleElement]: ...
    @staticmethod
    def SetTitleElements(elements: List[PlotTitleElement]) -> None: ...

class ColorScheme:  # Class
    def __init__(self) -> None: ...

    ColorSchemeChanged: System.EventHandler  # static

    DisplayName: str
    GraphicsColors: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.GraphicsColorScheme
    )
    GridColors: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.GridColorScheme
    )
    Name: str
    StyleFile: str

    def IsActive(self) -> bool: ...
    def ToString(self) -> str: ...
    def Activate(self) -> None: ...

class ColorSchemeSet:  # Class
    def __init__(self) -> None: ...

    ColorScheme: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.ColorScheme
    ]

    @staticmethod
    def Load() -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.ColorSchemeSet
    ): ...
    def GetColorScheme(
        self, name: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.ColorScheme
    ): ...
    def GetDefaultColorScheme(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.ColorScheme
    ): ...

class CompoundAtAGlanceConfiguration:  # Class
    BackColor: System.Drawing.Color  # static
    DefaultBackColor: System.Drawing.Color  # static # readonly
    DefaultForeColor: System.Drawing.Color  # static # readonly
    DefaultGridlinesColor: System.Drawing.Color  # static # readonly
    DefaultGridlinesVisible: bool  # static # readonly
    FontSize: float  # static
    ForeColor: System.Drawing.Color  # static
    GridlinesColor: System.Drawing.Color  # static
    GridlinesVisible: bool  # static
    PaneBorderColor: System.Drawing.Color  # static
    PrintLandscape: bool  # static
    PrintPageSettings: str  # static
    SelectedPaneBorderColor: System.Drawing.Color  # static

class DefaultColorScheme:  # Class
    def __init__(self) -> None: ...

    Application: str
    Instrument: str
    Name: str

class GraphicsColorScheme:  # Class
    def __init__(self) -> None: ...

    BackColor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    ForeColor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    PlotColor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    QualifierColors: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    ]

    def IsActive(self) -> bool: ...
    def Activate(self) -> None: ...

class GridColorScheme:  # Class
    def __init__(self) -> None: ...

    ActiveCellBackColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    ActiveCellBackColor2: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    ActiveCellForeColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    ActiveCellForeColor2: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    ActiveCellHighlightBackColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    ActiveCellHighlightBackColor2: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    ActiveCellHighlightForeColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    ActiveCellHighlightForeColor2: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    BackColor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    BorderColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    CellBackColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    CellForeColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    DisplayName: str
    HeaderBackColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    HeaderForeColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    Name: str
    OutlierBackColorHigh: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    OutlierBackColorLow: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    OutlierForeColorHigh: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    OutlierForeColorLow: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    QuantErrorBackColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    QuantErrorForeColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )

    def IsActive(self) -> bool: ...
    def ToString(self) -> str: ...
    def Activate(self) -> None: ...

class GridConfiguration:  # Class
    ActiveCellBackColor: System.Drawing.Color  # static
    ActiveCellBackColor2: System.Drawing.Color  # static
    ActiveCellForeColor: System.Drawing.Color  # static
    ActiveCellForeColor2: System.Drawing.Color  # static
    ActiveCellHighlightBackColor: System.Drawing.Color  # static
    ActiveCellHighlightBackColor2: System.Drawing.Color  # static
    ActiveCellHighlightForeColor: System.Drawing.Color  # static
    ActiveCellHighlightForeColor2: System.Drawing.Color  # static
    BackColor: System.Drawing.Color  # static
    BorderColor: System.Drawing.Color  # static
    CellBackColor: System.Drawing.Color  # static
    CellForeColor: System.Drawing.Color  # static
    CellPadding: int  # static
    DefaultFontSize: float  # static
    DefaultFontSizePercent: float  # static # readonly
    FontSizePercent: float  # static
    HeaderBackColor: System.Drawing.Color  # static
    HeaderForeColor: System.Drawing.Color  # static
    HeaderStyle: str  # static
    HeaderWrapText: bool  # static # readonly

    @overload
    @staticmethod
    def GetColumnCaption(
        sectionName: str,
        relationName: str,
        columnName: str,
        instrumentType: InstrumentType,
    ) -> str: ...
    @overload
    @staticmethod
    def GetColumnCaption(
        sectionName: str,
        relationName: str,
        columnName: str,
        instrumentType: InstrumentType,
        culture: System.Globalization.CultureInfo,
    ) -> str: ...
    @staticmethod
    def SetAvailableSampleTypes(sampleTypes: List[str]) -> None: ...
    @staticmethod
    def SetColumnHidden(relationName: str, columnName: str, hidden: bool) -> None: ...
    @staticmethod
    def GetColumnAction(relationName: str, columnName: str) -> str: ...
    @staticmethod
    def GetTableCaption(sectionName: str, relationName: str) -> str: ...
    @staticmethod
    def GetVisibleColumns(
        sectionName: str,
        relationName: str,
        defaultVisibleColumns: bool,
        defaultValues: List[str],
    ) -> List[str]: ...
    @staticmethod
    def IsColumnHidden(
        relationName: str, columnName: str, instrumentType: InstrumentType
    ) -> bool: ...
    @staticmethod
    def GetColumnGroupCaption(relationName: str) -> str: ...
    @staticmethod
    def GetScanTypes(instrumentType: InstrumentType) -> List[ScanType]: ...
    @staticmethod
    def SetVisibleColumns(
        sectionName: str, relationName: str, columnNames: Iterable[str]
    ) -> None: ...
    @staticmethod
    def IsSampleTypeHidden(sampleType: str) -> bool: ...
    @staticmethod
    def GetColumnTooltipText(
        sectionName: str, relationName: str, columnName: str, instrument: InstrumentType
    ) -> str: ...
    @staticmethod
    def SetColumnCaption(
        sectionName: str,
        relationName: str,
        columnName: str,
        instrumentType: InstrumentType,
        value_: str,
    ) -> None: ...
    @staticmethod
    def GetCompoundListColumnGroupCaption(relationName: str) -> str: ...
    @staticmethod
    def GetAvailableSampleTypes() -> List[str]: ...
    @staticmethod
    def GetScanTypeCaption(
        instrumentType: InstrumentType, scanType: ScanType
    ) -> str: ...
    @staticmethod
    def SetSampleTypeCaption(sampleType: str, caption: str) -> None: ...
    @overload
    @staticmethod
    def GetSampleTypeCaption(sampleType: str, appType: str) -> str: ...
    @overload
    @staticmethod
    def GetSampleTypeCaption(
        sampleType: str, appType: str, culture: System.Globalization.CultureInfo
    ) -> str: ...

class MethodTableConfiguration:  # Class
    SectionName: str = ...  # static # readonly

    AllowColumnMoving: bool  # static
    ApplyMethodAnalyze: str  # static
    AssistantWidthRatio: float  # static
    AvailableSpecies: str  # static
    DisableAnalyzeBatch: bool  # static # readonly
    EnableHeaderClickSorting: bool  # static
    GenieIntegratorDefaultAreaReject: float  # static # readonly
    GenieIntegratorDefaultPeakWidth: float  # static # readonly
    GenieIntegratorDefaultShoulderDetection: bool  # static # readonly
    GenieIntegratorDefaultThreshold: float  # static # readonly
    GenieIntegratorDefaultUseDataScaleFactor: bool  # static # readonly
    GroupByTimeSegment: bool  # static
    MethodFromLibrary_CreateTargetsPerSpectrum: bool  # static
    MethodFromLibrary_NumQualifiers: int  # static
    MethodFromLibrary_RTCalibration: str  # static
    MethodFromLibrary_SumQualifiers: bool  # static
    MethodFromLibrary_TargetIonMode: str  # static
    MethodFromLibrary_UseRTCalibration: bool  # static
    ShowAssistantPane: bool  # static
    UsedSpecies: str  # static

    @staticmethod
    def GetColumnCaption(
        relationName: str, columnName: str, instrumentType: InstrumentType
    ) -> str: ...
    @staticmethod
    def GetMarkedColumns(
        tableName: str, task: MethodEditTaskMode, instrument: InstrumentType
    ) -> List[str]: ...
    @staticmethod
    def GetConcentrationUnits() -> List[str]: ...
    @staticmethod
    def SetSort(
        band: str, values: List[System.Collections.Generic.KeyValuePair[str, str]]
    ) -> None: ...
    @staticmethod
    def GetDefaultVisibleColumns(
        tableName: str,
        task: MethodEditTaskMode,
        instrument: InstrumentType,
        systemDefault: bool,
    ) -> List[str]: ...
    @staticmethod
    def GetTableVisible(
        tableName: str, task: MethodEditTaskMode, instrument: InstrumentType
    ) -> bool: ...
    @staticmethod
    def GetVisibleColumns(
        tableName: str,
        task: MethodEditTaskMode,
        outlier: Optional[OutlierColumns],
        instrument: InstrumentType,
        useSystemDefaultIfNotExist: bool,
    ) -> List[str]: ...
    @staticmethod
    def SetVisibleColumns(
        tableName: str,
        task: MethodEditTaskMode,
        outlier: Optional[OutlierColumns],
        instrument: InstrumentType,
        columns: List[str],
    ) -> None: ...
    @staticmethod
    def GetColumnTooltipText(
        relationName: str, columnName: str, instrument: InstrumentType
    ) -> str: ...
    @staticmethod
    def GetSort(
        band: str,
    ) -> List[System.Collections.Generic.KeyValuePair[str, str]]: ...
    @staticmethod
    def GetVisibleIntegrators() -> List[IntegratorType]: ...

class MetricsPlotConfiguration:  # Class
    BackColor: System.Drawing.Color  # static
    ForeColor: System.Drawing.Color  # static
    GridlinesColor: System.Drawing.Color  # static # readonly
    GridlinesVisible: bool  # static # readonly
    PaneBorderColor: System.Drawing.Color  # static
    PaneBorderWidth: int  # static
    PrintLandscape: bool  # static
    PrintPageSettings: str  # static

class NumberFormats(Agilent.MassHunter.Quantitative.UIModel.INumberFormats):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, defaultValues: bool) -> None: ...
    def InitCoreLibrary(self, instrumentType: InstrumentType) -> None: ...
    def GetColumns(self) -> List[str]: ...
    def SetColumnNumberFormat(
        self, instrumentType: InstrumentType, column: str, format: INumericCustomFormat
    ) -> None: ...
    def GetColumnNumberFormat(
        self, instrumentType: InstrumentType, column: str
    ) -> INumericCustomFormat: ...
    def Exists(self, instrument: InstrumentType, column: str) -> bool: ...
    def GetColumnCategory(self, column: str) -> str: ...
    def StoreFormats(self) -> None: ...

class ReportConfiguration:  # Class
    GenerateNow: bool  # static
    LastReportMethod: str  # static
    OpenReportFolder: bool  # static
    StartQueueViewer: bool  # static

class SampleDataConfiguration:  # Class
    AutoScaleAfter: float  # static
    BackColor: System.Drawing.Color  # static
    CompoundColors: List[System.Drawing.Color]  # static
    CompoundCurveColor: System.Drawing.Color  # static
    DeconvolutionComponentColors: List[System.Drawing.Color]  # static
    DefaultAutoScaleAfter: float  # static # readonly
    DefaultBackColor: System.Drawing.Color  # static # readonly
    DefaultCompoundColors: List[System.Drawing.Color]  # static # readonly
    DefaultCompoundCurveColor: System.Drawing.Color  # static # readonly
    DefaultDeconvolutionComponentColors: List[System.Drawing.Color]  # static # readonly
    DefaultForeColor: System.Drawing.Color  # static # readonly
    DefaultGridlinesColor: System.Drawing.Color  # static # readonly
    DefaultGridlinesVisible: bool  # static # readonly
    DefaultNormalize: bool  # static # readonly
    DefaultOverlayISTDCompounds: bool  # static # readonly
    DefaultOverlayTargetCompounds: bool  # static # readonly
    DefaultPeakLabelsAllowOverlap: bool  # static # readonly
    DefaultPeakLabelsVertical: bool  # static # readonly
    DefaultPrecursorColor: System.Drawing.Color  # static # readonly
    DefaultPrecursorFill: bool  # static # readonly
    DefaultPrecursorSize: int  # static # readonly
    DefaultShowChromatogramPeakLabelCaption: bool  # static # readonly
    DefaultShowChromatogramPeakLabelUnits: bool  # static # readonly
    DefaultShowSignalLabels: bool  # static # readonly
    DefaultShowTargetCompound: bool  # static # readonly
    DefaultShowTic: bool  # static # readonly
    DefaultShowTimeSegmentBorder: bool  # static # readonly
    DefaultSignalColors: List[System.Drawing.Color]  # static # readonly
    DefaultSpectrumColor: System.Drawing.Color  # static # readonly
    DefaultTargetPeakLabelsOnTIC: bool  # static # readonly
    DefaultTicColor: System.Drawing.Color  # static # readonly
    DefaultTimeSegmentBorderColor: System.Drawing.Color  # static # readonly
    FontSize: float  # static
    ForeColor: System.Drawing.Color  # static
    GridlinesColor: System.Drawing.Color  # static
    GridlinesVisible: bool  # static
    Normalize: bool  # static
    OverlayISTDCompounds: bool  # static
    OverlayTargetCompounds: bool  # static
    PaneBorderColor: System.Drawing.Color  # static
    PaneBorderWidth: int  # static
    PeakLabelsAllowOverlap: bool  # static
    PeakLabelsVertical: bool  # static
    PrecursorColor: System.Drawing.Color  # static
    PrecursorFill: bool  # static
    PrecursorSize: int  # static
    PrintLandscape: bool  # static
    PrintPageSettings: str  # static
    SelectedMassMarkerColor: System.Drawing.Color  # static
    SelectedPaneBorderColor: System.Drawing.Color  # static
    SelectedTimeRangeMarkerColor: System.Drawing.Color  # static
    ShowChromatogramPeakLabelCaption: bool  # static
    ShowChromatogramPeakLabelUnits: bool  # static
    ShowSignalLabels: bool  # static
    ShowTargetCompound: bool  # static
    ShowTic: bool  # static
    ShowTimeSegmentBorder: bool  # static
    SignalColors: List[System.Drawing.Color]  # static
    SpectrumColor: System.Drawing.Color  # static
    TargetPeakLabelsOnTIC: bool  # static
    TicColor: System.Drawing.Color  # static
    TimeSegmentBorderColor: System.Drawing.Color  # static

    @staticmethod
    def CopyTo(config: System.Configuration.Configuration) -> None: ...
    @staticmethod
    def CopyFrom(config: System.Configuration.Configuration) -> None: ...
    @staticmethod
    def GetDefaultOverlaySignals(instrumentType: InstrumentType) -> bool: ...
    @staticmethod
    def SetOverlayAllSignals(instrumentType: InstrumentType, value_: bool) -> None: ...
    @staticmethod
    def GetChromatogramPeakLabels() -> List[ChromatogramPeakLabelType]: ...
    @staticmethod
    def GetDefaultChromatogramPeakLabels() -> List[ChromatogramPeakLabelType]: ...
    @staticmethod
    def SetChromatogramPeakLabels(types: List[ChromatogramPeakLabelType]) -> None: ...
    @staticmethod
    def GetOverlayAllSignals(instrumentType: InstrumentType) -> bool: ...

class ScriptConfiguration:  # Class
    CommandLogFilePath: str  # static # readonly
    CommandLogLanguage: str  # static # readonly
    CommandLogSwitch: bool  # static # readonly
    ScriptFolder: str  # static # readonly

class UIConfiguration:  # Class
    GroupName: str = ...  # static # readonly

    AnalysisDynamicToolCommand: str  # static
    AppStyle: str  # static
    AvailableDateTimeFormats: List[str]  # static # readonly
    ColorScheme: str  # static
    CompoundSortType: str  # static
    DefaultColorScheme: str  # static # readonly
    DefaultFontSize: float  # static # readonly
    DefaultGraphicsPaneBorderColor: System.Drawing.Color  # static # readonly
    DefaultGraphicsSelectedPaneBorderColor: System.Drawing.Color  # static # readonly
    DefaultShowManualIntegratoinHandles: bool  # static # readonly
    DockAllowFlexDocking: bool  # static
    DockAllowFloating: bool  # static
    DockShowPinButton: bool  # static
    DockWindowStyle: str  # static # readonly
    ExportFileFilterIndex: int  # static
    ExportFileMode: GridExportMode  # static
    ExportFileOpenFile: bool  # static
    ExportGraphicsAllPanes: bool  # static
    ExportGraphicsFitToPage: bool  # static
    ExportGraphicsImageFormat: System.Drawing.Imaging.ImageFormat  # static
    ExportGraphicsLastFolder: str  # static
    ExportGraphicsPageHeight: float  # static
    ExportGraphicsPageWidth: float  # static
    ExportGraphicsScale: float  # static
    ExportGraphicsSizeUnits: str  # static
    GraphicsBackColor: System.Drawing.Color  # static
    GraphicsDefaultBackColor: System.Drawing.Color  # static # readonly
    GraphicsDefaultForeColor: System.Drawing.Color  # static # readonly
    GraphicsDefaultGridlinesColor: System.Drawing.Color  # static # readonly
    GraphicsDefaultGridlinesVisible: bool  # static # readonly
    GraphicsDefaultPlotColor: System.Drawing.Color  # static # readonly
    GraphicsDefaultShowTimeSegmentBorder: bool  # static # readonly
    GraphicsDefaultTimeSegmentBorderColor: System.Drawing.Color  # static # readonly
    GraphicsForeColor: System.Drawing.Color  # static
    GraphicsGridlinesColor: System.Drawing.Color  # static
    GraphicsGridlinesVisible: bool  # static
    GraphicsPaneBorderColor: System.Drawing.Color  # static
    GraphicsPaneBorderWidth: int  # static
    GraphicsPlotColor: System.Drawing.Color  # static
    GraphicsPrecursorFillColor: System.Drawing.Color  # static
    GraphicsPrecursorLineColor: System.Drawing.Color  # static
    GraphicsPrecursorSize: int  # static
    GraphicsSelectedPaneBorderColor: System.Drawing.Color  # static
    InitialScript: str  # static # readonly
    LastBatchFolder: str  # static
    LastEnableAuditTrail: bool  # static
    LastFileFolder: str  # static
    LastLibraryMethodPath: str  # static
    LastLibraryPath: str  # static
    LastMethodBatchFolder: str  # static
    LastMethodFolder: str  # static
    LastRTCalibrationFile: str  # static
    LastReportGraphicsSettingsFolder: str  # static
    LastReportTemplateFolder: str  # static
    LastSampleFolder: str  # static
    LockApplicationInterval: int  # static # readonly
    LockNumberFormats: bool  # static # readonly
    ManualIntegrationHandleTransparency: int  # static # readonly
    MaxFontSize: float  # static # readonly
    MinFontSize: float  # static # readonly
    NavigatorPaneStyle: str  # static # readonly
    NavigatorPaneViewStyle: str  # static # readonly
    NumberFormatFile: str  # static # readonly
    PrintMargins: List[float]  # static
    QualAppPath: str  # static
    ToolbarCustomize: bool  # static
    ToolbarStyle: str  # static
    UseSureMassLabels: bool  # static # readonly
    WindowPosition: System.Drawing.Rectangle  # static
    WindowState: System.Windows.Forms.FormWindowState  # static

    @staticmethod
    def SetUserEnumValue(
        group: str, section: str, settings: str, value_: System.Enum
    ) -> None: ...
    @staticmethod
    def CopyTo(
        groupName: str, sectionName: str, config: System.Configuration.Configuration
    ) -> None: ...
    @staticmethod
    def CopyFrom(
        groupName: str, sectionName: str, config: System.Configuration.Configuration
    ) -> None: ...
    @overload
    @staticmethod
    def SetUserValue(group: str, section: str, settings: str, value_: str) -> None: ...
    @overload
    @staticmethod
    def SetUserValue(group: str, section: str, setting: str, value_: bool) -> None: ...
    @overload
    @staticmethod
    def SetUserValue(group: str, section: str, setting: str, value_: int) -> None: ...
    @overload
    @staticmethod
    def SetUserValue(group: str, section: str, setting: str, value_: int) -> None: ...
    @overload
    @staticmethod
    def SetUserValue(
        group: str, section: str, setting: str, color: System.Drawing.Color
    ) -> None: ...
    @overload
    @staticmethod
    def SetUserValue(
        groupName: str, sectionName: str, settingName: str, value_: float
    ) -> None: ...
    @overload
    @staticmethod
    def SetUserValue(
        groupName: str, sectionName: str, settingName: str, value_: System.Guid
    ) -> None: ...
    @staticmethod
    def GetRecentReportMethods() -> List[str]: ...
    @staticmethod
    def AddRecentBatch(
        dataStorage: IDataStorage, batchPath: str, batchFile: str
    ) -> None: ...
    @staticmethod
    def RemoveRecentBatch(
        dataStorage: IDataStorage, folder: str, file: str
    ) -> None: ...
    @staticmethod
    def SetToolbarVisible(paneId: str, toolbarId: str, value_: bool) -> None: ...
    @staticmethod
    def GetRecentBatches() -> List[str]: ...
    @staticmethod
    def ClearRecentBatches() -> None: ...
    @staticmethod
    def GetUserEnumValue(
        group: str,
        section: str,
        settings: str,
        type: System.Type,
        defaultValue: System.Enum,
    ) -> System.Enum: ...
    @overload
    @staticmethod
    def GetUserValue(
        group: str, section: str, settings: str, defaultValue: str
    ) -> str: ...
    @overload
    @staticmethod
    def GetUserValue(
        group: str, section: str, setting: str, defaultValue: bool
    ) -> bool: ...
    @overload
    @staticmethod
    def GetUserValue(
        group: str, section: str, setting: str, defaultValue: int
    ) -> int: ...
    @overload
    @staticmethod
    def GetUserValue(
        group: str, section: str, setting: str, defaultValue: int
    ) -> int: ...
    @overload
    @staticmethod
    def GetUserValue(
        group: str, section: str, setting: str, defaultValue: System.Drawing.Color
    ) -> System.Drawing.Color: ...
    @overload
    @staticmethod
    def GetUserValue(
        groupName: str, sectionName: str, settingName: str, defaultValue: float
    ) -> float: ...
    @overload
    @staticmethod
    def GetUserValue(
        groupName: str, sectionName: str, settingName: str, defaultValue: System.Guid
    ) -> System.Guid: ...
    @staticmethod
    def ClearRecentReportMethods() -> None: ...
    @staticmethod
    def SetMaxRecentBatches(max: int) -> None: ...
    @staticmethod
    def AddRecentReportMethod(path: str) -> None: ...
    @staticmethod
    def GetLocalValue(
        group: str, section: str, setting: str, defaultValue: bool
    ) -> bool: ...
    @staticmethod
    def GetToolbarVisible(paneId: str, toolbarId: str, defaultValue: bool) -> bool: ...

class WorktableConfiguration(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.GridConfiguration
):  # Class
    def __init__(self) -> None: ...

    SectionName: str = ...  # static # readonly

    AllowColumnMoving: bool  # static
    AutoReviewInterval: int  # static
    DefaultOutlierBackColor: System.Drawing.Color  # static # readonly
    DefaultOutlierBackColorHigh: System.Drawing.Color  # static # readonly
    DefaultOutlierBackColorLow: System.Drawing.Color  # static # readonly
    DefaultOutlierForeColor: System.Drawing.Color  # static # readonly
    DefaultOutlierForeColorHigh: System.Drawing.Color  # static # readonly
    DefaultOutlierForeColorLow: System.Drawing.Color  # static # readonly
    DefaultSingleCompoundView: Optional[bool]  # static
    DefaultTableViewMode: str  # static
    EnableHeaderClickSorting: bool  # static
    FixSampleColumns: bool  # static
    GroupSeparatorWidth: int  # static
    OutlierBackColor: System.Drawing.Color  # static
    OutlierBackColorHigh: System.Drawing.Color  # static
    OutlierBackColorLow: System.Drawing.Color  # static
    OutlierForeColor: System.Drawing.Color  # static
    OutlierForeColorHigh: System.Drawing.Color  # static
    OutlierForeColorLow: System.Drawing.Color  # static
    QuantErrorBackColor: System.Drawing.Color  # static
    QuantErrorForeColor: System.Drawing.Color  # static
    ReSortMIColumn: bool  # static
    SingleCompoundView: bool  # static
    TableViewMode: str  # static

    @staticmethod
    def GetColumnCaption(
        relationName: str, columnName: str, instrumentType: InstrumentType
    ) -> str: ...
    @staticmethod
    def IsColumnEditable(relationName: str, columnName: str) -> bool: ...
    @staticmethod
    def SetOutlierEnabled(name: str, enabled: bool) -> None: ...
    @staticmethod
    def GetDefaultVisibleColumns(
        relationName: str,
        isCompoundList: bool,
        isFlatMode: bool,
        isSingleCompound: bool,
        defaultValues: List[str],
    ) -> List[str]: ...
    @staticmethod
    def GetVisibleColumns(
        relationName: str,
        isCompoundList: bool,
        isFlatMode: bool,
        isSingleCompound: bool,
        defaultValues: List[str],
    ) -> List[str]: ...
    @staticmethod
    def SetVisibleColumns(
        relationName: str,
        isCompoundList: bool,
        isFlatMode: bool,
        isSingleCompound: bool,
        columnNames: Iterable[str],
    ) -> None: ...
    @staticmethod
    def GetOutlierCategoryCaption(category: str) -> str: ...
    @staticmethod
    def ClearColumnCaptionCache() -> None: ...
    @staticmethod
    def GetColumnTooltipText(
        relationName: str, columnName: str, instrument: InstrumentType
    ) -> str: ...
    @staticmethod
    def GetOutlierEnabled(name: str) -> bool: ...
    @staticmethod
    def GetOutlierVisible(name: str) -> bool: ...
    @staticmethod
    def GetSystemDefaultVisibleColumns(
        relationName: str, isCompoundList: bool, isFlat: bool, isSingle: bool
    ) -> List[str]: ...
    @staticmethod
    def SetDefaultVisibleColumns(
        relationName: str,
        isCompoundList: bool,
        isFlatMode: bool,
        isSingleCompound: bool,
        columns: List[str],
    ) -> None: ...
    @staticmethod
    def SetOutlierVisible(name: str, value_: bool) -> None: ...
    @staticmethod
    def GetOutlierCaption(outlier: str, application: str) -> str: ...

class XmlColor:  # Struct
    def __init__(self, color: System.Drawing.Color) -> None: ...

    Color: System.Drawing.Color
    Default: str

    @staticmethod
    def ToColor(value_: str) -> System.Drawing.Color: ...
    def ToString(self) -> str: ...
    @staticmethod
    def FromColor(color: System.Drawing.Color) -> str: ...
