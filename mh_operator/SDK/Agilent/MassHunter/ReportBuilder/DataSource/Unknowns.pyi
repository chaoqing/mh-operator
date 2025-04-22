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
from . import (
    FieldFormat,
    ICustomCommandGroup,
    ICustomUI,
    IDataSource,
    IDataSourceDesigner,
    IDataSourceGraphicsEdit,
    IDataSourceGraphicsParameter,
    IDataSourceTableFormat,
)

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns

class BindingName(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Analysis: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName = (
        ...
    )  # static # readonly
    AuxiliaryMethod: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName
    ) = ...  # static # readonly
    Batch: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName = (
        ...
    )  # static # readonly
    Component: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName = (
        ...
    )  # static # readonly
    DeconvolutionMethod: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName
    ) = ...  # static # readonly
    Hit: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName = (
        ...
    )  # static # readonly
    IdentificationMethod: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName
    ) = ...  # static # readonly
    IonPeak: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName = (
        ...
    )  # static # readonly
    LibrarySearchMethod: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName
    ) = ...  # static # readonly
    Peak: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName = (
        ...
    )  # static # readonly
    PeakQualifier: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName = (
        ...
    )  # static # readonly
    Sample: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName = (
        ...
    )  # static # readonly
    SelectedSample: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName = (
        ...
    )  # static # readonly
    TargetCompound: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName = (
        ...
    )  # static # readonly
    TargetMatchMethod: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName
    ) = ...  # static # readonly
    TargetQualifier: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.BindingName
    ) = ...  # static # readonly

class ComponentSpectrumGraphics(
    System.IDisposable,
    Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.IComponentSpectrumGraphics,
):  # Class
    def __init__(
        self,
        dataSource: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.UnknownsDataSource,
    ) -> None: ...
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        hitId: Optional[int],
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
    ICustomUI,
):  # Class
    def __init__(self) -> None: ...

    DataSourceType: System.Type  # readonly

    def GetFieldNames(self, dataName: str) -> List[str]: ...
    def GetDataNames(self) -> List[str]: ...
    def CanExecuteSystemCommand(
        self,
        app: Agilent.MassHunter.ReportBuilder.Application.IApplication,
        systemCommand: str,
        parameter: Any,
        canExecute: bool,
    ) -> bool: ...
    def DefaultFieldFormat(
        self, dataName: str, fieldName: str, format: FieldFormat
    ) -> bool: ...
    def GetGraphicsNames(self) -> List[str]: ...
    def GetDisplayName(self, name: str) -> str: ...
    def GetParameters(self, name: str) -> List[IDataSourceGraphicsParameter]: ...
    def ExecuteSystemCommand(
        self,
        app: Agilent.MassHunter.ReportBuilder.Application.IApplication,
        systemCommand: str,
        parameter: Any,
    ) -> bool: ...
    def Dispose(self) -> None: ...
    def GetCustomCommandGroups(
        self, application: Agilent.MassHunter.ReportBuilder.Application.IApplication
    ) -> List[ICustomCommandGroup]: ...
    def GetCustomUI(self) -> T: ...

class EicPeaksGraphics(
    System.IDisposable,
    Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.IEicPeaksGraphics,
):  # Class
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        x: float,
        y: float,
        width: float,
        height: float,
        parameters: List[System.Collections.Generic.KeyValuePair[str, Any]],
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def Dispose(self) -> None: ...

class ExtractedSpectrumGraphics(
    Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.IExtractedSpectrumGraphics,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataSource: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.UnknownsDataSource,
    ) -> None: ...
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def Dispose(self) -> None: ...

class GraphicsName(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    ComponentSpectrum: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.GraphicsName
    ) = ...  # static # readonly
    EicPeaks: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.GraphicsName = (
        ...
    )  # static # readonly
    ExtractedSpectrum: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.GraphicsName
    ) = ...  # static # readonly
    HitLibrarySpectrum: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.GraphicsName
    ) = ...  # static # readonly
    IonPeaks: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.GraphicsName = (
        ...
    )  # static # readonly
    MolecularStructure: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.GraphicsName
    ) = ...  # static # readonly
    SampleChromatogram: (
        Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.GraphicsName
    ) = ...  # static # readonly

class HitLibrarySpectrumGraphics(
    Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.IHitLibrarySpectrumGraphics,
    System.IDisposable,
):  # Class
    def __init__(
        self,
        dataSource: Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.UnknownsDataSource,
    ) -> None: ...
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        hitId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def Dispose(self) -> None: ...

class IComponentSpectrumGraphics(object):  # Interface
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        hitId: Optional[int],
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

class IEicPeaksGraphics(object):  # Interface
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

class IExtractedSpectrumGraphics(object):  # Interface
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

class IHitLibrarySpectrumGraphics(object):  # Interface
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        hitId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

class IIonPeaksGraphics(object):  # Interface
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

class IMolecularStructureGraphics(object):  # Interface
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        hitId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...

class ISampleChromatogramGraphics(object):  # Interface
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

class IUnknownsDataSource(IDataSource):  # Interface
    FixedGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IFixedGraphics
    )
    SelectedSamples: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
    ]

class IonPeaksGraphics(
    System.IDisposable,
    Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.IIonPeaksGraphics,
):  # Class
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        x: float,
        y: float,
        width: float,
        height: float,
        parameters: List[System.Collections.Generic.KeyValuePair[str, Any]],
    ) -> None: ...
    @overload
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def Dispose(self) -> None: ...

class MolecularStructureGraphics(
    Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.IMolecularStructureGraphics,
    System.IDisposable,
):  # Class
    def Draw(
        self,
        canvas: Agilent.MassHunter.ReportBuilder.Engine.IGraphicsCanvas,
        batchId: int,
        sampleId: int,
        deconvolutionMethodId: int,
        componentId: int,
        hitId: int,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None: ...
    def Dispose(self) -> None: ...

class SampleChromatogramGraphics(
    System.IDisposable,
    Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.ISampleChromatogramGraphics,
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
    def Dispose(self) -> None: ...

class UnknownsDataSource(
    System.IDisposable,
    Agilent.MassHunter.ReportBuilder.DataSource.Unknowns.IUnknownsDataSource,
    IDataSource,
):  # Class
    def __init__(
        self,
        uiContext: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.UIContext,
    ) -> None: ...

    FixedGraphics: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.ReportScript.IFixedGraphics
    )
    SelectedSamples: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
    ]

    def CreateDesigner(self) -> IDataSourceDesigner: ...
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
    def GetFieldCaption(self, dataName: str, fieldName: str) -> str: ...
    def Select(
        self,
        context: Agilent.MassHunter.ReportBuilder.Engine.IReportContext,
        dataBinding: Agilent.MassHunter.ReportBuilder.Template.IDataBinding,
    ) -> List[Any]: ...
    def LocalizeFieldValue(self, dataName: str, fieldName: str, value_: Any) -> str: ...
    def GetFieldFormat(self, dataName: str, fieldName: str) -> str: ...
    def Dispose(self) -> None: ...
