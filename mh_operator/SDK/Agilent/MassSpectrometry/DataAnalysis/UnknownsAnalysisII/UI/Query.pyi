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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Query

class LinqQuery(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Query.QueryBase,
):  # Class
    def __init__(self, uiContext: UIContext, queryFile: str) -> None: ...
    def GetColumnFormat(
        self, column: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat: ...
    def GetColumnLabel(self, column: str) -> str: ...
    def RunQuery(self) -> Any: ...

class LinqQueryBase(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Query.QueryBase,
):  # Class
    ColumnFormats: List[
        System.Collections.Generic.KeyValuePair[
            str, Agilent.MassSpectrometry.DataAnalysis.Quantitative.INumericCustomFormat
        ]
    ]  # readonly
    ColumnLabels: List[System.Collections.Generic.KeyValuePair[str, str]]  # readonly

    def RunQuery(self) -> Any: ...

class LinqQueryCompilerOption:  # Class
    def __init__(self) -> None: ...

    Name: str
    Value: str

class LinqQueryOptions:  # Class
    def __init__(self) -> None: ...

    CompilerOptions: List[
        Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Query.LinqQueryCompilerOption
    ]
    Imports: List[str]
    Language: str
    Name: str
    References: List[str]

class QueryBase(System.IDisposable):  # Class
    def Dispose(self) -> None: ...
    def RunQuery(self) -> Any: ...

class QueryForm(
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
    def __init__(self, uiContext: UIContext) -> None: ...
    def Clear(self) -> None: ...
    def RunQuery(self, queryFile: str) -> None: ...

class SqlQuery(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.UnknownsAnalysisII.UI.Query.QueryBase,
):  # Class
    def __init__(self, uiContext: UIContext, queryFile: str) -> None: ...
    def RunQuery(self) -> Any: ...
