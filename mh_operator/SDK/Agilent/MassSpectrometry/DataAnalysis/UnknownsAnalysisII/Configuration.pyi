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

# Discovered Generic TypeVars:
T = TypeVar("T")

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration

class ApplicationSettings(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationElementSectionBase
):  # Class
    def __init__(self) -> None: ...

    AvailableIntegrators: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.IntegratorType
    ]  # readonly
    DumpLogOnNormalExit: bool  # readonly
    EnableAccurateMassExtension: bool  # readonly
    ErrorReportEmailAddress: str  # readonly
    ScriptReferences: System.Collections.Specialized.StringCollection  # readonly

class ChromatogramSettings(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.PlotUserSettingsSectionBase
):  # Class
    def __init__(self) -> None: ...

    AllowPeakLabelsOverlap: bool
    AutoScaleAfter: float
    AutoScrollX: bool
    AvailablePeakLabelNames: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationStringArrayElement
    )  # readonly
    BlankComponentColor: System.Drawing.Color
    ComponentsColor: System.Drawing.Color
    DefaultAllowPeakLabelsOverlap: bool  # readonly
    DefaultAutoScaleAfter: float  # readonly
    DefaultAutoScrollX: bool  # readonly
    DefaultBlankComponentColor: System.Drawing.Color  # readonly
    DefaultComponentsColor: System.Drawing.Color  # readonly
    DefaultEicColors: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationColorArrayElement
    )  # readonly
    DefaultMaxNumRowsPerPage: int  # readonly
    DefaultPeakLabelsVisible: bool  # readonly
    DefaultSelectedComponentsColor: System.Drawing.Color  # readonly
    DefaultShowComponents: bool  # readonly
    DefaultShowEics: bool  # readonly
    DefaultShowLegend: bool  # readonly
    DefaultShowPeakLabelNames: bool  # readonly
    DefaultShowPeakLabelUnits: bool  # readonly
    DefaultShowSelectedComponents: bool  # readonly
    DefaultShowTic: bool  # readonly
    DefaultSimColor: System.Drawing.Color  # readonly
    DefaultTicColor: System.Drawing.Color  # readonly
    DefaultVerticalPeakLabels: bool  # readonly
    DefaultVisiblePeakLabelColumnNames: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationStringArrayElement
    )  # readonly
    EicColors: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationColorArrayElement
    )  # readonly
    MaxNumRowsPerPage: int
    PeakLabelsVisible: bool
    SelectedComponentsColor: System.Drawing.Color
    ShowComponents: bool
    ShowEics: bool
    ShowLegend: bool
    ShowPeakLabelNames: bool
    ShowPeakLabelUnits: bool
    ShowSelectedComponents: bool
    ShowTic: bool
    SimColor: System.Drawing.Color
    TicColor: System.Drawing.Color
    VerticalPeakLabels: bool
    VisiblePeakLabelColumnNames: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationStringArrayElement
    )  # readonly

class ColorScheme:  # Class
    def __init__(self) -> None: ...

    DisplayName: str
    GraphicsColors: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.GraphicsColorScheme
    )
    Name: str

    def Activate(self) -> None: ...

class ColorSchemeSet:  # Class
    def __init__(self) -> None: ...

    ColorScheme: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColorScheme
    ]

    @staticmethod
    def Load() -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColorSchemeSet
    ): ...
    def GetColorScheme(
        self, name: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColorScheme
    ): ...
    def GetDefaultColorScheme(
        self, isOpenLAB: bool
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColorScheme
    ): ...

class ColumnFormatItem:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        column: str,
        format: Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat,
    ) -> None: ...

    Column: str
    Format: Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat
    _Format: str

class ColumnFormats:  # Class
    def __init__(self) -> None: ...

    Formats: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnFormatItem
    ]

    def HasAccurateMassFormat(self, column: str) -> bool: ...
    def Initialize(self) -> None: ...
    def GetDefaultFormat(
        self, column: str, isAccurateMass: bool
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat: ...
    def SaveFormats(self) -> None: ...
    def SetFormat(
        self,
        column: str,
        isAccurateMass: bool,
        value_: Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat,
    ) -> None: ...
    def Clear(self) -> None: ...
    def GetFormat(
        self, column: str, isAccurateMass: bool
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat: ...

class ColumnWidthItem:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, column: str, width: int) -> None: ...

    Column: str
    Width: int

class ColumnWidths:  # Class
    def __init__(self) -> None: ...
    def __getitem__(self, column: str) -> Optional[int]: ...
    def __setitem__(self, column: str, value_: Optional[int]) -> None: ...
    Widths: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidthItem
    ]

class EicPeaksSettings(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.PlotUserSettingsSectionBase
):  # Class
    def __init__(self) -> None: ...

    DefaultShowTic: bool  # readonly
    DefaultTicColor: System.Drawing.Color  # readonly
    ShowTic: bool
    TicColor: System.Drawing.Color

class GraphicsColorScheme:  # Class
    def __init__(self) -> None: ...

    BackColor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    ComponentColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    ForeColor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    IonPeakColors: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    ]
    SpectrumColor: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor
    )
    TicColor: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Configuration.XmlColor

    def Activate(self) -> None: ...

class IonPeaksSettings(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.PlotUserSettingsSectionBase
):  # Class
    def __init__(self) -> None: ...

    ComponentColor: System.Drawing.Color
    DefaultComponentColor: System.Drawing.Color  # readonly
    DefaultIonPeakColors: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationColorArrayElement
    )  # readonly
    DefaultNumVisibleIonPeaks: int  # readonly
    DefaultShowComponent: bool  # readonly
    DefaultShowTic: bool  # readonly
    DefaultTicColor: System.Drawing.Color  # readonly
    IonPeakColors: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationColorArrayElement
    )  # readonly
    MaxNumVisibleIonPeaks: int  # readonly
    NumVisibleIonPeaks: int
    ShowComponent: bool
    ShowTic: bool
    TicColor: System.Drawing.Color

class NumericFormat(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericFormat
):  # Class
    def __init__(
        self,
        formats: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnFormats,
    ) -> None: ...

    IsAccurateMass: bool

class PlotUserSettingsSectionBase(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.UserSettingsSectionBase
):  # Class
    def __init__(self) -> None: ...

    BackgroundColor: System.Drawing.Color
    DefaultBackgroundColor: System.Drawing.Color  # readonly
    DefaultFontBold: bool  # readonly
    DefaultFontFamily: str  # readonly
    DefaultFontItalic: bool  # readonly
    DefaultFontSize: float  # readonly
    DefaultForegroundColor: System.Drawing.Color
    DefaultGridlinesColor: System.Drawing.Color  # readonly
    DefaultShowGridlines: bool  # readonly
    FontBold: bool
    FontFamily: str
    FontItalic: bool
    FontSize: float
    ForegroundColor: System.Drawing.Color
    GridlinesColor: System.Drawing.Color
    PrintPageSettings: str
    ShowGridlines: bool

class SpectrumSettings(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.PlotUserSettingsSectionBase
):  # Class
    def __init__(self) -> None: ...

    AllowPeakLabelsOverlap: bool
    DefaultAllowPeakLabelsOverlap: bool  # readonly
    DefaultFoundExactMassColor: System.Drawing.Color  # readonly
    DefaultHeadToTail: bool  # readonly
    DefaultSelectedExactMassColor: System.Drawing.Color  # readonly
    DefaultShowExtractedSpectrum: bool  # readonly
    DefaultShowPeakLabels: bool  # readonly
    DefaultSpectrumColor: System.Drawing.Color  # readonly
    DefaultVerticalPeakLabels: bool  # readonly
    FoundExactMassColor: System.Drawing.Color
    HeadToTail: bool
    SelectedExactMassColor: System.Drawing.Color
    ShowExtractedSpectrum: bool
    ShowPeakLabels: bool
    SpectrumColor: System.Drawing.Color
    VerticalPeakLabels: bool

class StructureSettings(
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.UserSettingsSectionBase
):  # Class
    def __init__(self) -> None: ...

    PrintPageSettings: str

class UAConfiguration:  # Class
    ApplicationSettings: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ApplicationSettings
    )  # readonly
    ChromatogramSettings: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ChromatogramSettings
    )  # readonly
    EicPeaksSettings: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.EicPeaksSettings
    )  # readonly
    Initialized: bool  # readonly
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.UAConfiguration
    )  # static # readonly
    IonPeaksSettings: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.IonPeaksSettings
    )  # readonly
    Location: str  # readonly
    SpectrumSettings: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.SpectrumSettings
    )  # readonly
    StructureSettings: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.StructureSettings
    )  # readonly
    UserSettings: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.UserSettings
    )  # readonly

    def Initialize(self) -> None: ...
    @overload
    @staticmethod
    def GetHeaderText(table: str, column: str) -> str: ...
    @overload
    @staticmethod
    def GetHeaderText(column: str) -> str: ...
    @staticmethod
    def _GetHeaderText(column: str) -> str: ...
    def Save(self) -> None: ...

class UserSettings(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationElementSectionBase
):  # Class
    def __init__(self) -> None: ...

    AlwaysReanalyze: bool
    ColumnFormats: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnFormats
    )  # readonly
    ColumnWidthsAdvancedAuxiliary: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsAdvancedBlankSubtraction: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsAdvancedDeconvolution: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsAdvancedIdentification: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsAdvancedLibrarySearch: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsAdvancedTargetMatch: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsAnalysisMessageTable: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsComponentTable: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsHitTable: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsLoadMethodDialog: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsSampleTable: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ColumnWidthsTargetTable: (
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Configuration.ColumnWidths
    )
    ExportComponentsAllComponents: bool
    ExportComponentsTo: str
    GenerateReportNow: bool
    LastAnalysisFolder: str
    LastEnableAuditTrail: bool
    LastExportFolder: str
    LastLayoutFolder: str
    LastLibraryFolder: str
    LastMethodFolder: str
    LastMethodPane: str
    LastQueryFolder: str
    LastRTCalibrationFolder: str
    LastReportMethod: str
    LastScriptFolder: str
    LinqDebug: bool
    LinqTraceCode: bool
    LoadMethodDialogClientSize: System.Drawing.Size
    MethodAdvancedDialogClientSize: System.Drawing.Size
    NonHitAutoCompoundNames: bool
    NonHitCompoundNameAddIndex: bool
    NonHitCompoundNamePrefix: str
    OpenReportFolder: bool
    PrintLandscape: bool
    RecentAnalysisFiles: System.Collections.Specialized.StringCollection  # readonly
    ReportAllSamples: bool
    ShowAdvancedMethod: bool
    StartQueueViewer: bool
    VisibleColumnsComponentTable: System.Collections.Specialized.StringCollection
    VisibleColumnsExactMassTable: System.Collections.Specialized.StringCollection
    VisibleColumnsSampleTable: System.Collections.Specialized.StringCollection
    VisibleColumnsTargetTable: System.Collections.Specialized.StringCollection

    def GetValue(self, name: str, defaultValue: T) -> T: ...
    def GetOpenReportFolder(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> bool: ...
    def SetValue(self, name: str, value_: T) -> None: ...

class UserSettingsSectionBase(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.ConfigurationElementSectionBase
):  # Class
    def __init__(self) -> None: ...

    StandardFontSizes: List[Any]  # static # readonly

    @staticmethod
    def SetPlotFont(
        plot: Agilent.MassSpectrometry.GUI.Plot.PlotControl,
        fontFamily: str,
        size: float,
        bold: bool,
        italic: bool,
    ) -> None: ...
