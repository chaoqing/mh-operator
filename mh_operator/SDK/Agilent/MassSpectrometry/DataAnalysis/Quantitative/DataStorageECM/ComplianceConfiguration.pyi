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

from . import ComplianceECM

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DataStorageECM.ComplianceConfiguration

class ComplianceConfigurationEdit(
    System.IDisposable,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.ComplianceUI.IComplianceConfigurationEdit,
):  # Class
    def __init__(self, compliance: ComplianceECM) -> None: ...

    CommandPrivilegePrefix: str = ...  # static # readonly
    PreviousPrivilegePrefix: str = ...  # static # readonly
    PrivilegeGroupName: str = ...  # static # readonly

    CanEditRoles: bool  # readonly
    ComplianceECM: ComplianceECM  # readonly

    def Save(
        self,
        config: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration,
    ) -> None: ...
    def Load(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration
    ): ...
    def ResetToDefault(
        self,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ComplianceConfiguration
    ): ...
    def PreprocessNewRoleName(self, roleName: str) -> str: ...
    def GetAvailableRoles(self) -> List[str]: ...
    def ConvertPrivilegeName(self, commandName: str) -> str: ...
    def Dispose(self) -> None: ...
    def Run(self, args: List[str]) -> None: ...
