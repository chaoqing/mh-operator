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

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Utilities.AcamlFixes

class ChangeSignalTypeForEZChromSpectraAcamlFix(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlFix
):  # Class
    def __init__(self) -> None: ...

    OrderNumber: int  # readonly

    def NeedsFix(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
    def Apply(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...

class ConsolidateMethodDefinitionsAcamlFix(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlFix
):  # Class
    def __init__(self) -> None: ...

    OrderNumber: int  # readonly

    def NeedsFix(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
    def Apply(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...

class CreateRunTypesAcamlFix(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlFix
):  # Class
    def __init__(self) -> None: ...

    OrderNumber: int  # readonly

    def NeedsFix(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
    def Apply(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...

class DataFileReferencePathAcamlFix(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlFix
):  # Class
    def __init__(self) -> None: ...

    OrderNumber: int  # readonly

    def NeedsFix(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
    def Apply(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...

class EZChromBaselineCalculationAcamlFix(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlFix
):  # Class
    def __init__(self) -> None: ...

    OrderNumber: int  # readonly

    def NeedsFix(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
    def Apply(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...

class InternalStandardAmountIdentifierAcamlFix(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlFix
):  # Class
    def __init__(self) -> None: ...

    OrderNumber: int  # readonly

    def NeedsFix(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
    def Apply(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...

class ScalePeaksAcamlFix(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlFix
):  # Class
    def __init__(self) -> None: ...

    OrderNumber: int  # readonly

    def NeedsFix(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
    def Apply(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...

class UndefinedBaselineAcamlFix(
    Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Interfaces.IAcamlFix
):  # Class
    def __init__(self) -> None: ...

    OrderNumber: int  # readonly

    def NeedsFix(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
    def Apply(
        self,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        acaml: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IACAML,
    ) -> bool: ...
