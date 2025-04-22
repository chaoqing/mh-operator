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

from .Model import IMainWindow

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Remoting

class Client(System.MarshalByRefObject, System.IDisposable):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
        isWpf: bool,
    ) -> None: ...
    def GenerateTICLibrarySearchReport(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...
    def AnalyzeSample(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...
    def GenerateAreaPercentageReport(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...
    def Debug(self) -> None: ...
    def Connect(self) -> None: ...
    def AnalyzeCompound(
        self,
        uiState: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIScriptIF.IUIState,
    ) -> None: ...
    def Dispose(self) -> None: ...

class Server(System.MarshalByRefObject, System.IDisposable):  # Class
    def __init__(self, mainWindow: IMainWindow) -> None: ...
    def SaveAnalysis(self) -> None: ...
    def NewAnalysis(self, batchFolder: str, analysisName: str) -> bool: ...
    def SetSampleProperties(
        self,
        parameters: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleColumnValuesParameter
        ],
    ) -> None: ...
    def RemoveLibraryMethod(self, batchID: int, sampleID: int) -> None: ...
    def Dispose(self) -> None: ...
    def Ready(self) -> None: ...
    def Register(self) -> None: ...
    def ImportQuantBatch(self, batchFolder: str, batchFileName: str) -> None: ...
    def SelectSamples(
        self,
        samples: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.SampleRowID
        ],
    ) -> None: ...
    def SetMethods(
        self,
        batchID: int,
        sampleID: int,
        deconvolutionMethodValues: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
        identificationMethodvalues: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
        librarySearchMethodValues: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.KeyValue
        ],
    ) -> None: ...
    def Debug(self) -> None: ...
    def GetNewAnalysisName(self, batchFolder: str, baseName: str) -> str: ...
    def ImportQuantMethodFromBatch(
        self, batchFolder: str, batchFileName: str
    ) -> None: ...
    def AnalyzeSamples(
        self,
        samples: List[
            Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.Command.SampleRowIDParameter
        ],
    ) -> None: ...
    def SelectNearestComponent(self, rt: float) -> None: ...
    def SelectMatchedCompound(
        self, batchId: int, sampleId: int, compoundId: int
    ) -> bool: ...
    def AddSample(self, dataFileName: str) -> Optional[int]: ...
    def LoadMethodToAllSamples(self, methodPath: str) -> None: ...
    def Analyze(self) -> None: ...
    def SetAreaPercentColumnsVisible(self) -> None: ...
    def SetCulture(self, ci: System.Globalization.CultureInfo) -> None: ...
