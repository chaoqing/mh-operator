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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.NLR

class Funcs(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> float: ...
    def BeginInvoke(
        self,
        x: float,
        a: List[float],
        dyda: List[float],
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(self, x: float, a: List[float], dyda: List[float]) -> float: ...

class INewtonRaphsonFunc(object):  # Interface
    def Value(self, x: float) -> float: ...
    def ValueDF(self, x: float, dfdx: float) -> float: ...

class LevenbergMarquardt:  # Class
    def __init__(
        self,
        xx: List[float],
        yy: List[float],
        ssig2: List[float],
        aa: List[float],
        funks: Agilent.MassSpectrometry.DataAnalysis.Quantitative.NLR.Funcs,
        TOL: float,
    ) -> None: ...

    ChiSquare: float  # readonly
    Covariance: List[List[float]]  # readonly
    FitParams: List[float]  # readonly

    def Fit(self) -> None: ...

class LevenbergMarquartdConvergenceException(
    System.ApplicationException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, msg: str) -> None: ...

class NewtonRaphson:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def FindRoot(
        func: Agilent.MassSpectrometry.DataAnalysis.Quantitative.NLR.INewtonRaphsonFunc,
        xLow: float,
        xHigh: float,
        xTolerance: float,
    ) -> float: ...
    @staticmethod
    def SafeFindRoot(
        func: Agilent.MassSpectrometry.DataAnalysis.Quantitative.NLR.INewtonRaphsonFunc,
        xLow: float,
        xHigh: float,
        xTolerance: float,
    ) -> float: ...

class NewtonRaphsonConvergenceException(
    System.ApplicationException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, msg: str) -> None: ...
