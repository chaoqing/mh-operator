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
TProviderInterface = TypeVar("TProviderInterface")
from .Interfaces import IDataProviderFactory, IProvider

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Providers

class DataProviderFactory(IDataProviderFactory):  # Class
    Instance: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Providers.DataProviderFactory
    )  # static # readonly

    @overload
    def GetProviderSet(self, docId: System.Guid) -> Iterable[IProvider]: ...
    @overload
    def GetProviderSet(
        self, acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML
    ) -> Iterable[IProvider]: ...
    @overload
    def GetProvider(self, docId: System.Guid) -> TProviderInterface: ...
    @overload
    def GetProvider(
        self, acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML
    ) -> TProviderInterface: ...
    def IsRegistered(
        self, acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML
    ) -> bool: ...
    def RegisterAcaml(
        self,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
        prepareForWriteAccess: bool,
    ) -> bool: ...
