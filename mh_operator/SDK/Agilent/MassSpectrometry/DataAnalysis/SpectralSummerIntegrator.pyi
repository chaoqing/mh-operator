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
    ICollectionElement,
    IConvertibleValueContainer,
    IParameter,
    IParameterSet,
    IPeakList,
    IPSetPeakFind,
    ParameterSet,
)

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.SpectralSummerIntegrator

class IPSetSpectralSummerIntegrator(
    IPSetPeakFind,
    IParameterSet,
    IParameter,
    ICollectionElement,
    System.ICloneable,
    Iterable[Any],
):  # Interface
    BaselineOffsetEnd: float
    BaselineOffsetStart: float
    EndIntegration: float
    EndIntegrationUnitIsMinutes: bool
    FixedBaselineOffset: float
    RTWindowBaselineOffset: float
    SetRTatHighestPointInPeak: bool
    StartIntegration: float
    StartIntegrationUnitIsMinutes: bool
    UseAbsoluteTimes: bool
    UseLowestPointAsBaselineOffset: bool
    UseLowestPointInRTWindowAsBaselineOffset: bool
    UseRelativeDeltasFromRT: bool

class LocalSpectralSummerIntegrator:  # Class
    def __init__(self) -> None: ...
    def FindPeaks(
        self,
        xArray: List[float],
        yArray: List[float],
        useLowestPointAsBaselineOffset: bool,
        fixedBaselineOffset: float,
        useAbsoluteTimes: bool,
        useRelativeDeltasFromRT: bool,
        startIntegration: float,
        endIntegration: float,
        startIntegrationUnitIsMinutes: bool,
        endIntegrationUnitIsMinutes: bool,
        useLowestPointInRTWindowAsBaselineOffset: bool,
        rtWindowBaselineOffset: float,
        setRTatHighestPointInPeak: bool,
    ) -> IPeakList: ...

class PSetSpectralSummerIntegrator(
    ParameterSet,
    IParameter,
    Agilent.MassSpectrometry.DataAnalysis.SpectralSummerIntegrator.IPSetSpectralSummerIntegrator,
    IPSetPeakFind,
    System.ICloneable,
    Iterable[Any],
    IConvertibleValueContainer,
    IParameterSet,
    ICollectionElement,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        source: Agilent.MassSpectrometry.DataAnalysis.SpectralSummerIntegrator.PSetSpectralSummerIntegrator,
    ) -> None: ...

    keyBaselineOffsetEnd: str  # static # readonly
    keyBaselineOffsetStart: str  # static # readonly
    keyEndIntegration: str  # static # readonly
    keyEndIntegrationUnitIsMinutes: str  # static # readonly
    keyFixedBaselineOffset: str  # static # readonly
    keyRTWindowBaselineOffset: str  # static # readonly
    keySetRTatHighestPointInPeak: str  # static # readonly
    keyStartIntegration: str  # static # readonly
    keyStartIntegrationUnitIsMinutes: str  # static # readonly
    keyUseAbsoluteTimes: str  # static # readonly
    keyUseLowestPointAsBaselineOffset: str  # static # readonly
    keyUseLowestPointInRTWindowAsBaselineOffset: str  # static # readonly
    keyUseRelativeDeltasFromRT: str  # static # readonly

    BaselineOffsetEnd: float
    BaselineOffsetStart: float
    EndIntegration: float
    EndIntegrationUnitIsMinutes: bool
    FixedBaselineOffset: float
    RTWindowBaselineOffset: float
    SetRTatHighestPointInPeak: bool
    StartIntegration: float
    StartIntegrationUnitIsMinutes: bool
    UseAbsoluteTimes: bool
    UseLowestPointAsBaselineOffset: bool
    UseLowestPointInRTWindowAsBaselineOffset: bool
    UseRelativeDeltasFromRT: bool
