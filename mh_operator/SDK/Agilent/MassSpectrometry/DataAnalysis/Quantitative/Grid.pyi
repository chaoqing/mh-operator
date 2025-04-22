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

from . import GridExportMode, InstrumentType
from .Configuration import ColorScheme
from .Controls2 import IPropertyPage

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid

class BandConfig:  # Class
    def __init__(self, name: str) -> None: ...

    Caption: str
    ColumnConfigs: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.ColumnConfig
    ]  # readonly
    Hidden: bool
    def __getitem__(
        self, key: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.ColumnConfig: ...
    Name: str  # readonly
    VisibleColumnCount: int  # readonly

    def SetVisibleColumnNames(self, columnNames: Iterable[str]) -> None: ...
    def Contains(self, columnName: str) -> bool: ...
    def Clear(self) -> None: ...
    def SetColumnWidth(self, name: str, width: int) -> None: ...
    @staticmethod
    def CompareColumnsWithVisiblePosition(
        c1: Infragistics.Win.UltraWinGrid.UltraGridColumn,
        c2: Infragistics.Win.UltraWinGrid.UltraGridColumn,
    ) -> int: ...
    def GetVisibleColumnName(self, index: int) -> str: ...
    def GetColumnWidthNames(self) -> Iterable[str]: ...
    def GetColumnWidth(self, name: str) -> int: ...
    def GetColumnCaption(self, columnName: str) -> str: ...
    def CopyFrom(
        self, config: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.BandConfig
    ) -> None: ...
    def ShowColumn(self, columnName: str, columnNameAfter: str) -> None: ...
    def GetVisibleColumnNames(self) -> List[str]: ...
    def CompareColumnOrder(self, c1: str, c2: str) -> int: ...
    def SetDefault(
        self,
        configSectionName: str,
        table: System.Data.DataTable,
        readConfig: bool,
        defaultVisibleColumnsOrder: List[str],
        instrumentType: InstrumentType,
    ) -> None: ...
    def IsColumnVisible(self, column: str) -> bool: ...
    def RemoveColumn(self, columnName: str) -> None: ...
    def ReadFromBand(
        self, band: Infragistics.Win.UltraWinGrid.UltraGridBand
    ) -> None: ...
    def UpdateColumns(
        self,
        gridConfig: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridConfigBase,
        band: Infragistics.Win.UltraWinGrid.UltraGridBand,
    ) -> None: ...
    def SaveToConfigFile(self, configSectionName: str) -> None: ...
    def ClearColumnWidths(self) -> None: ...
    def IsColumnHidden(self, column: str) -> bool: ...
    def AddColumn(
        self,
        columnName: str,
        config: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.ColumnConfig,
    ) -> None: ...
    def HideColumn(self, columnName: str) -> None: ...

class ColumnAction:  # Class
    def PerformAction(
        self, cellValue: str, parent: System.Windows.Forms.Control
    ) -> None: ...
    @staticmethod
    def ParseAction(
        action: str,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.ColumnAction: ...

class ColumnConfig:  # Class
    def __init__(self, name: str) -> None: ...

    Caption: str
    Hidden: bool  # readonly
    Name: str  # readonly

    def CopyFrom(
        self,
        config: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.ColumnConfig,
    ) -> None: ...
    def SetDefault(
        self, sectionName: str, bandName: str, instrumentType: InstrumentType
    ) -> None: ...

class ColumnsDialog(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(
        self,
        grid: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridControlBase,
        masterConfig: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridConfigBase,
        bandName: str,
    ) -> None: ...

class ColumnsDialogKeyCaption:  # Class
    def __init__(self, key: str, caption: str) -> None: ...

    Caption: str  # readonly
    Key: str  # readonly

    def GetHashCode(self) -> int: ...
    def ToString(self) -> str: ...
    def Equals(self, obj: Any) -> bool: ...

class GridCellComparer(System.Collections.IComparer):  # Class
    def __init__(self) -> None: ...

    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridCellComparer
    )  # static # readonly

class GridConfigBase(System.IDisposable):  # Class
    def __getitem__(
        self, bandName: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.BandConfig: ...
    ValueListSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.ValueListSet
    )  # readonly

    def Contains(self, bandName: str) -> bool: ...
    def ApplyTo(self, grid: Infragistics.Win.UltraWinGrid.UltraGridBase) -> None: ...
    def CopyFrom(
        self,
        config: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridConfigBase,
    ) -> None: ...
    def GetTableName(self, dataset: System.Data.DataSet, name: str) -> str: ...
    def InitValueLists(
        self,
        valueLists: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.ValueListSet,
        instrumentType: InstrumentType,
        applicationType: str,
    ) -> None: ...
    def Clear(self) -> None: ...
    def ReadFromGrid(
        self, grid: Infragistics.Win.UltraWinGrid.UltraGridBase
    ) -> None: ...
    def UpdateColumnAttributes(
        self, column: Infragistics.Win.UltraWinGrid.UltraGridColumn
    ) -> None: ...
    def Clone(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridConfigBase: ...
    def SetDefault(self, readConfigFile: bool) -> None: ...
    def ReadColumnSettings(self, reader: System.Xml.XmlReader) -> None: ...
    def WriteColumnSettings(self, writer: System.Xml.XmlWriter) -> None: ...
    def Dispose(self) -> None: ...
    def UpdateNumericFormats(
        self, grid: Infragistics.Win.UltraWinGrid.UltraGrid
    ) -> None: ...
    @staticmethod
    def IsNumericType(type: System.Type) -> bool: ...

class GridControlBase(
    Infragistics.Win.IUltraControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.Layout.IArrangedElement,
    Infragistics.Win.IUIElementProvider,
    Infragistics.Win.IUltraControlElement,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISupportInitialize,
    Infragistics.Shared.Serialization.ICodeDomSerializable,
    Infragistics.Win.UIAutomation.IProvideUIAutomation,
    System.Windows.Forms.IWin32Window,
    Infragistics.Win.ISupportPresets,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    Infragistics.Win.AppStyling.ISupportAppStyling,
    Infragistics.Win.IControlElementEventProcessor,
    Infragistics.Win.IUIElementTextProvider,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    Infragistics.Win.CalcEngine.IUltraCalcParticipant,
    System.ComponentModel.ISynchronizeInvoke,
    Infragistics.Win.IValidatorClient,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    Agilent.MassHunter.Quantitative.UIModel.IGridControl,
    Infragistics.Win.Touch.ISupportTouchMetrics,
    System.ComponentModel.IComponent,
    Infragistics.Win.ISelectionManager,
    Infragistics.Win.UltraWinGrid.Design.IGridDesignInfo,
    Infragistics.Win.UltraWinGrid.UltraGrid,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    Infragistics.Win.Touch.IGestureConsumer,
    Infragistics.Shared.IUltraLicensedComponent,
    System.Windows.Forms.IBindableComponent,
    System.IDisposable,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    Infragistics.Win.AutoEditMode.IAutoEditMode,
):  # Class
    def __init__(self) -> None: ...

    AllowMovingColumns: bool
    CanCopy: bool  # readonly
    CanDelete: bool  # readonly
    CanExpandAll: bool  # readonly
    CanPaste: bool  # readonly
    CanPrint: bool  # readonly
    Exporting: bool
    FontSizePercentage: float
    IsHeaderClickSortingEnabled: bool
    IsInEditMode: bool  # readonly
    LastRawBandName: str
    LastRawColumnName: str
    UltraGrid: Infragistics.Win.UltraWinGrid.UltraGrid  # readonly

    def UpdateColors(self) -> None: ...
    def CanUndoInEditMode(self) -> bool: ...
    def FormatColumn(self, rawBandName: str, rawColumnName: str) -> None: ...
    def Sort(self, bandName: str, columnName: str, ascending: bool) -> None: ...
    def DisplayPrintPreview(self) -> None: ...
    def AutoFitColumns(self) -> None: ...
    def CollapseAll(self) -> None: ...
    def IsColumnFormattable(self, rawBandName: str, rawColumnName: str) -> bool: ...
    def GetColumnCaption(self, bandName: str, columnName: str) -> str: ...
    def LoadColumnSettings(self, file: str) -> None: ...
    def GetLogicalColumnName(self, bandName: str, columnName: str) -> str: ...
    def ShowColumn(self, bandName: str, columnName: str, columnAfter: str) -> None: ...
    def UndoInEditMode(self) -> None: ...
    def UpdateRowHeight(self) -> None: ...
    def GetLogicalBandName(self, bandName: str, columnName: str) -> str: ...
    def Copy(self) -> None: ...
    def DisplayColumnChanging(self) -> None: ...
    def ExpandAll(self) -> None: ...
    def SupportsSaveLoadColumnSettings(self) -> bool: ...
    def IsColumnVisible(self, bandName: str, columnName: str) -> bool: ...
    def DisplayColumnChanged(self) -> None: ...
    def PageSetup(self) -> None: ...
    def SaveColumnSettings(self, file: str) -> None: ...
    def Print(self, displayPrintDialog: bool) -> None: ...
    def GetColumnNames(self, bandName: str) -> List[str]: ...
    def Delete(self) -> None: ...
    def ResetColumns(self) -> None: ...
    def ResetSort(self) -> None: ...
    def SetDefaultBehavior(self) -> None: ...
    def HideColumn(self, bandName: str, columnName: str) -> None: ...
    def ShowColumnsDialog(self) -> None: ...
    def Paste(self) -> None: ...

class GridControlDrawFilterBase(Infragistics.Win.IUIElementDrawFilter):  # Class
    def __init__(self) -> None: ...
    def DrawElement(
        self,
        drawPhase: Infragistics.Win.DrawPhase,
        drawParams: Infragistics.Win.UIElementDrawParams,
    ) -> bool: ...
    def GetPhasesToFilter(
        self, drawParams: Infragistics.Win.UIElementDrawParams
    ) -> Infragistics.Win.DrawPhase: ...

class GridExcelExporter(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridExporter,
):  # Class
    def __init__(self, file: str) -> None: ...
    def Export(
        self,
        grid: Agilent.MassHunter.Quantitative.UIModel.IGridControl,
        mode: GridExportMode,
    ) -> bool: ...

class GridExporter(System.IDisposable):  # Class
    def Export(
        self,
        grid: Agilent.MassHunter.Quantitative.UIModel.IGridControl,
        mode: GridExportMode,
    ) -> bool: ...
    def Dispose(self) -> None: ...

class GridTextExporter(
    System.IDisposable,
    Infragistics.Win.UltraWinGrid.IUltraGridExporter,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridTextExporterBase,
):  # Class
    def __init__(self, writer: System.IO.TextWriter, delimiter: str) -> None: ...

class GridTextExporterBase(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridExporter,
    Infragistics.Win.UltraWinGrid.IUltraGridExporter,
):  # Class
    def Export(
        self,
        grid: Agilent.MassHunter.Quantitative.UIModel.IGridControl,
        mode: GridExportMode,
    ) -> bool: ...
    def EndExport(self, canceled: bool) -> None: ...
    def BeginExport(
        self,
        exportLayout: Infragistics.Win.UltraWinGrid.UltraGridLayout,
        rows: Infragistics.Win.UltraWinGrid.RowsCollection,
    ) -> None: ...
    def ProcessRow(
        self,
        row: Infragistics.Win.UltraWinGrid.UltraGridRow,
        processRowParams: Infragistics.Win.UltraWinGrid.ProcessRowParams,
    ) -> None: ...

class GridXmlExporter(
    System.IDisposable,
    Infragistics.Win.UltraWinGrid.IUltraGridExporter,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridTextExporterBase,
):  # Class
    def __init__(self, writer: System.Xml.XmlWriter, rootElement: str) -> None: ...

class IPlottableColumn(
    Agilent.MassHunter.Quantitative.UIModel.IPlottableColumn
):  # Interface
    ...

class IPlottableGrid(
    Agilent.MassHunter.Quantitative.UIModel.IPlottableGrid
):  # Interface
    ...

class IntegrationParametersPropertyDescriptor(
    System.ComponentModel.PropertyDescriptor
):  # Class
    def __init__(
        self, baseDescriptor: System.ComponentModel.PropertyDescriptor
    ) -> None: ...

    ComponentType: System.Type  # readonly
    IsReadOnly: bool  # readonly
    PropertyType: System.Type  # readonly

    @staticmethod
    def ConvertValue(value_: Any) -> Any: ...
    def GetValue(self, component: Any) -> Any: ...
    def CanResetValue(self, component: Any) -> bool: ...
    def SetValue(self, component: Any, value_: Any) -> None: ...
    def ShouldSerializeValue(self, component: Any) -> bool: ...
    def ResetValue(self, component: Any) -> None: ...

class NotFoundValue:  # Class
    Instance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.NotFoundValue
    )  # static # readonly

    def ToString(self) -> str: ...

class PropertyPage(
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UserControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    IPropertyPage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.IWin32Window,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        grid: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridControlBase,
        applicationType: str,
    ) -> None: ...

    DisplayName: str
    IsDirty: bool  # readonly
    SelectedColorScheme: ColorScheme  # readonly

    def Initialize(
        self,
        grid: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.GridControlBase,
        applicationType: str,
    ) -> None: ...
    def SetActive(self) -> None: ...
    def DoDefault(self) -> None: ...
    def Apply(self) -> None: ...

    ColorSchemeChanged: System.EventHandler  # Event
    PageChanged: System.EventHandler  # Event

class UrlColumnAction(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Grid.ColumnAction
):  # Class
    def PerformAction(
        self, cellValue: str, parent: System.Windows.Forms.Control
    ) -> None: ...

class ValueListSet(System.IDisposable):  # Class
    def __init__(self) -> None: ...
    def Contains(self, table: str, column: str) -> bool: ...
    @overload
    def Add(
        self, table: str, column: str, valueList: Infragistics.Win.ValueList
    ) -> None: ...
    @overload
    def Add(
        self,
        table: str,
        column: str,
        valueList: Infragistics.Win.ValueList,
        style: Infragistics.Win.UltraWinGrid.ColumnStyle,
    ) -> None: ...
    def SetColumnStyle(
        self, table: str, column: str, style: Infragistics.Win.UltraWinGrid.ColumnStyle
    ) -> None: ...
    def GetValueList(self, table: str, column: str) -> Infragistics.Win.ValueList: ...
    def GetColumnStyle(
        self, table: str, column: str
    ) -> Infragistics.Win.UltraWinGrid.ColumnStyle: ...
    def Dispose(self) -> None: ...

class XmlContentPropertyDescriptor(System.ComponentModel.PropertyDescriptor):  # Class
    def __init__(
        self, baseDescriptor: System.ComponentModel.PropertyDescriptor
    ) -> None: ...

    ComponentType: System.Type  # readonly
    IsReadOnly: bool  # readonly
    PropertyType: System.Type  # readonly

    @staticmethod
    def ConvertValue(value_: Any) -> Any: ...
    def GetValue(self, component: Any) -> Any: ...
    def CanResetValue(self, component: Any) -> bool: ...
    def SetValue(self, component: Any, value_: Any) -> None: ...
    def ShouldSerializeValue(self, component: Any) -> bool: ...
    def ResetValue(self, component: Any) -> None: ...
