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

from . import ChromRegion, Component, ComponentPerceptionParams, IDataAccess
from .FD import Feature, FeatureDetector, IFeatureSet

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.FeatureDeconvolution

class TofFeatureDeconvolution:  # Class
    def __init__(self) -> None: ...
    def RunMultiParameterDeconvolution(
        self,
        preSelectedFeatures: System.Collections.Generic.List[Feature],
        dataAccess: IDataAccess,
        cpParamsList: System.Collections.Generic.List[ComponentPerceptionParams],
    ) -> List[System.Collections.Generic.List[Component]]: ...
    @overload
    def Run(
        self,
        featureSet: IFeatureSet,
        dataAccess: IDataAccess,
        featureDetector: FeatureDetector,
        cpParams: ComponentPerceptionParams,
    ) -> System.Collections.Generic.List[Component]: ...
    @overload
    def Run(
        self,
        preSelectedFeatures: System.Collections.Generic.List[Feature],
        dataAccess: IDataAccess,
        cpParams: ComponentPerceptionParams,
    ) -> System.Collections.Generic.List[Component]: ...
    @overload
    def Run(
        self, chromRegion: ChromRegion, cpParams: ComponentPerceptionParams
    ) -> System.Collections.Generic.List[Component]: ...
