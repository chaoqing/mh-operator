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

from . import UIContext

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Common

class LibrarySearchSite(
    Agilent.MassHunter.Quantitative.UIModel.ILibraryAppSite,
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UILibrary.ILibraryAppSite,
):  # Class
    def __init__(self, uiContext: UIContext) -> None: ...

    LibraryApp: Agilent.MassHunter.Quantitative.UIModel.ILibraryApp  # readonly

    def OnToolClicked(self, name: str) -> None: ...
    def SearchLibrary(
        self, batchID: int, sampleID: int, deconvolutionMethodID: int, componentID: int
    ) -> None: ...
    def ShowWindow(self) -> None: ...
    def Dispose(self) -> None: ...
    def OnCloseWindow(self) -> None: ...
