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

from . import CustomUI, QuickReport, Screening

# Discovered Generic TypeVars:
T = TypeVar("T")
from . import (
    DataSourceGraphicsParameter,
    FieldFormat,
    GraphicsParameterAcceptsFieldValue,
    GraphicsParameterType,
    IDataSource,
    IDataSourceDesigner,
    IDataSourceGraphicsEdit,
    IDataSourceGraphicsParameter,
    IDataSourceTableFormat,
    IReportPreview,
)

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.DataSource.Quant

class CompoundCalibrationGraphics(
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.ICompoundCalibrationGraphics,
    System.IDisposable,
):  # Class
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def Dispose(self) -> None: ...

class CompoundPeakGraphics(
    System.IDisposable,
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.ICompoundPeakGraphics,
):  # Class
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...
    def DrawOriginal(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def Dispose(self) -> None: ...

class DataSourceDesigner(
    IDataSourceDesigner,
    System.IDisposable,
    IDataSourceGraphicsEdit,
    IDataSourceTableFormat,
    IReportPreview,
):  # Class
    def __init__(self) -> None: ...

    DataSourceType: System.Type  # readonly

    def GetFieldNames(self, dataName: str) -> List[str]: ...
    def GetDataNames(self) -> List[str]: ...
    def SetupPreview(
        self, parameterPath: str, parent: System.Windows.Window, alwaysShowUI: bool
    ) -> bool: ...
    def DefaultFieldFormat(
        self, dataName: str, fieldName: str, format: FieldFormat
    ) -> bool: ...
    def GetGraphicsNames(self) -> List[str]: ...
    def GeneratePreview(
        self,
        templatePath: str,
        template: Agilent.MassHunter.ReportBuilder.Template.IReportTemplate,
        parameterFile: str,
        outputPath: str,
    ) -> None: ...
    def GetDisplayName(self, name: str) -> str: ...
    def GetParameters(self, name: str) -> List[IDataSourceGraphicsParameter]: ...
    def Dispose(self) -> None: ...
    def GetCustomUI(self) -> T: ...

class DataSourceFactory:  # Class
    @staticmethod
    def CreateDataSource(
        template: Agilent.MassHunter.ReportBuilder.Template.IReportTemplate,
        presentationState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.PresentationState,
        dtstart: System.DateTime,
    ) -> Agilent.MassHunter.ReportBuilder.DataSource.Quant.IQuantDataSourceBase: ...

class GraphicsParameter(
    IDataSourceGraphicsParameter, DataSourceGraphicsParameter
):  # Class
    def __init__(
        self,
        graphicsName: str,
        name: str,
        category: str,
        displayName: str,
        parameterType: GraphicsParameterType,
        acceptsFieldValue: GraphicsParameterAcceptsFieldValue,
    ) -> None: ...

    GraphicsName: str

    def GetCustomEditor(
        self,
        application: Agilent.MassHunter.ReportBuilder.Application.IApplication,
        editorBaseType: System.Type,
    ) -> Any: ...
    @staticmethod
    def LoadGraphicsParameters(
        document: System.Xml.XPath.XPathDocument,
        graphicsName: str,
        rmgr: System.Resources.ResourceManager,
    ) -> List[IDataSourceGraphicsParameter]: ...

class ICompoundCalibrationGraphics(object):  # Interface
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

class ICompoundPeakGraphics(object):  # Interface
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...
    def DrawOriginal(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

class IPeakOverlayGraphics(object):  # Interface
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...

class IPeakSpectrumGraphics(object):  # Interface
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        minmz: Optional[float],
        maxmz: Optional[float],
    ) -> None: ...

class IQualifierPeakGraphics(object):  # Interface
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...
    def DrawOriginal(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

class IQuantDataSource(
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.IQuantDataSourceBase,
    IDataSource,
    System.IDisposable,
):  # Interface
    CompoundCalibrationGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.ICompoundCalibrationGraphics
    )  # readonly
    CompoundPeakGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.ICompoundPeakGraphics
    )  # readonly
    PeakOverlayGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.IPeakOverlayGraphics
    )  # readonly
    PeakSpectrumGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.IPeakSpectrumGraphics
    )  # readonly
    QualifierPeakGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.IQualifierPeakGraphics
    )  # readonly
    SampleGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.ISampleGraphics
    )  # readonly

class IQuantDataSourceBase(IDataSource, System.IDisposable):  # Interface
    BatchFile: str  # readonly
    BatchFolder: str  # readonly
    CompoundFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IDataFilter
    )
    DataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet
    )  # readonly
    FixedGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IFixedGraphics
    )
    PresentationState: (
        Agilent.MassHunter.Quantitative.UIModel.IPresentationState
    )  # readonly
    SampleFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IDataFilter
    )

class ISampleGraphics(object):  # Interface
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        deviceName: str,
        ordinalNumber: int,
        signalName: str,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        deviceName: str,
        ordinalNumber: int,
        signalName: str,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...

class MSScanTypeRow:  # Class
    def __init__(self) -> None: ...

    BatchID: int
    MSScanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType
    SampleID: int

class PeakLabelTypesEditor(System.Drawing.Design.UITypeEditor):  # Class
    def __init__(
        self, application: Agilent.MassHunter.ReportBuilder.Application.IApplication
    ) -> None: ...
    def EditValue(
        self,
        context: System.ComponentModel.ITypeDescriptorContext,
        provider: System.IServiceProvider,
        value_: Any,
    ) -> Any: ...
    def GetEditStyle(
        self, context: System.ComponentModel.ITypeDescriptorContext
    ) -> System.Drawing.Design.UITypeEditorEditStyle: ...

class PeakOverlayGraphics(
    System.IDisposable,
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.IPeakOverlayGraphics,
):  # Class
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...
    def Dispose(self) -> None: ...

class PeakSpectrumGraphics(
    System.IDisposable,
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.IPeakSpectrumGraphics,
):  # Class
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        minmz: Optional[float],
        maxmz: Optional[float],
    ) -> None: ...
    def Dispose(self) -> None: ...

class QualifierPeakGraphics(
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.IQualifierPeakGraphics,
    System.IDisposable,
):  # Class
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...
    def DrawOriginal(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        compoundId: int,
        qualifierId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def Dispose(self) -> None: ...

class QuantDataSource(
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.IQuantDataSource,
    System.IDisposable,
    IDataSource,
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.IQuantDataSourceBase,
):  # Class
    def __init__(
        self,
        presentationState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.PresentationState,
        reportTime: System.DateTime,
    ) -> None: ...

    BatchFile: str  # readonly
    BatchFolder: str  # readonly
    CompoundCalibrationGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.ICompoundCalibrationGraphics
    )  # readonly
    CompoundFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IDataFilter
    )
    CompoundPeakGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.ICompoundPeakGraphics
    )  # readonly
    DataSet: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantitationDataSet
    )  # readonly
    FixedGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IFixedGraphics
    )
    PeakOverlayGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.IPeakOverlayGraphics
    )  # readonly
    PeakSpectrumGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.IPeakSpectrumGraphics
    )  # readonly
    PresentationState: (
        Agilent.MassHunter.Quantitative.UIModel.IPresentationState
    )  # readonly
    QualifierPeakGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.IQualifierPeakGraphics
    )  # readonly
    ReportStartTime: System.DateTime
    SampleFilter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.QuantDataProvider.IDataFilter
    )
    SampleGraphics: (
        Agilent.MassHunter.ReportBuilder.DataSource.Quant.ISampleGraphics
    )  # readonly

    def DrawGraphics(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        x: float,
        y: float,
        width: float,
        height: float,
        name: str,
        parameters: List[System.Collections.Generic.KeyValuePair[str, Any]],
    ) -> None: ...
    def SelectSignals(
        self,
        context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext,
        dataBinding: Agilent.MassHunter.ReportBuilder.Template.IDataBinding,
    ) -> List[Any]: ...
    def GetFieldCaption(self, bindingName: str, fieldName: str) -> str: ...
    def Select(
        self,
        context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext,
        dataBinding: Agilent.MassHunter.ReportBuilder.Template.IDataBinding,
    ) -> List[Any]: ...
    def SelectMSScanTypes(
        self,
        context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext,
        dataBiding: Agilent.MassHunter.ReportBuilder.Template.IDataBinding,
    ) -> List[Any]: ...
    def LocalizeFieldValue(self, dataName: str, fieldName: str, value_: Any) -> str: ...
    def GetFieldFormat(self, bindingName: str, fieldName: str) -> str: ...
    def Dispose(self) -> None: ...

class SampleGraphics(
    System.IDisposable,
    Agilent.MassHunter.ReportBuilder.DataSource.Quant.ISampleGraphics,
):  # Class
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        scanType: Agilent.MassSpectrometry.DataAnalysis.MSScanType,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        deviceName: str,
        ordinalNumber: int,
        signalName: str,
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        x: float,
        y: float,
        width: float,
        height: float,
        deviceName: str,
        ordinalNumber: int,
        signalName: str,
        minx: Optional[float],
        maxx: Optional[float],
        miny: Optional[float],
        maxy: Optional[float],
    ) -> None: ...
    def Dispose(self) -> None: ...

class SetupPreviewWindow(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Window,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IWindowService,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

    BatchFile: str
    BatchFolder: str
    InstrumentType: Agilent.MassSpectrometry.DataAnalysis.Quantitative.InstrumentType
    MaxNumPages: int

    def InitializeComponent(self) -> None: ...

class SignalRow:  # Class
    def __init__(self) -> None: ...

    BatchID: int
    DeviceName: str  # readonly
    OrdinalNumber: int  # readonly
    SampleID: int
    SignalName: str  # readonly
