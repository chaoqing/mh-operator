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

from . import Caches, DataHandlers, Extensions, Interfaces, Providers, Utilities

# Discovered Generic TypeVars:
TProvider = TypeVar("TProvider")
TRoot = TypeVar("TRoot")
from .AcamlObjectModel import IACAML
from .Interfaces import DataChangeLevel, IProviderLookupCache

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure

class AsyncFulltextIndexCompletedEvent(
    Agilent.OpenLab.Framework.Common.Notification.InfrastructureEventBase[
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.AsyncFulltextIndexCompletedEventArgs
    ],
    Agilent.OpenLab.Framework.Common.Notification.IInfrastructureEvent,
):  # Class
    def __init__(self) -> None: ...

class AsyncFulltextIndexCompletedEventArgs(System.EventArgs):  # Class
    DocId: System.Guid  # readonly

class AsyncLoadingCompletedEvent(
    Agilent.OpenLab.Framework.Common.Notification.IInfrastructureEvent,
    Agilent.OpenLab.Framework.Common.Notification.InfrastructureEventBase[
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.AsyncLoadingCompletedEventArgs
    ],
):  # Class
    def __init__(self) -> None: ...

class AsyncLoadingCompletedEventArgs(System.EventArgs):  # Class
    AcamlObject: IACAML  # readonly
    DocId: System.Guid  # readonly

class AsyncValidationCompletedEvent(
    Agilent.OpenLab.Framework.Common.Notification.InfrastructureEventBase[
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.AsyncValidationCompletedEventArgs
    ],
    Agilent.OpenLab.Framework.Common.Notification.IInfrastructureEvent,
):  # Class
    def __init__(self) -> None: ...

class AsyncValidationCompletedEventArgs(System.EventArgs):  # Class
    DocId: System.Guid  # readonly
    IsValid: bool  # readonly
    Message: str  # readonly

class DataChangedEventArgs(System.EventArgs):  # Class
    ChangeLevel: DataChangeLevel
    DocId: System.Guid  # readonly

class NotificationService(
    Agilent.OpenLab.Framework.Common.Notification.NotificationServiceBase
):  # Class
    def __init__(self) -> None: ...

    Instance: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.NotificationService
    )  # static # readonly

class ProviderLookupCacheBase(Generic[TRoot, TProvider], IProviderLookupCache):  # Class
    DocId: System.Guid  # readonly

    def DirtyDictionaryCount(self) -> int: ...
    def Reset(self) -> None: ...
    def Clear(self) -> None: ...
    def HasDirtyDictionaries(self) -> bool: ...

class ReadyForDataModificationsEvent(
    Agilent.OpenLab.Framework.Common.Notification.IInfrastructureEvent,
    Agilent.OpenLab.Framework.Common.Notification.InfrastructureEventBase[
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.ReadyForDataModificationsEventArgs
    ],
):  # Class
    def __init__(self) -> None: ...
    def Subscribe(
        self,
        action: System.Action[
            Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.ReadyForDataModificationsEventArgs
        ],
    ) -> None: ...

class ReadyForDataModificationsEventArgs(System.EventArgs):  # Class
    DocId: System.Guid  # readonly

class TraceDataAccess(Agilent.OpenLab.Framework.Diagnostics.TraceBase):  # Class
    TraceSourceNameModule: str = ...  # static # readonly

    Log: (
        Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.TraceDataAccess
    )  # static # readonly
