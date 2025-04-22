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
TEvent = TypeVar("TEvent")
TEventArgs = TypeVar("TEventArgs")

# Stubs for namespace: Agilent.OpenLab.Framework.Common.Notification

class IInfrastructureEvent(object):  # Interface
    def Reset(self) -> None: ...

class InfrastructureEventBase(
    Generic[TEventArgs],
    Agilent.OpenLab.Framework.Common.Notification.IInfrastructureEvent,
):  # Class
    Actions: List[System.Action[TEventArgs]]  # readonly

    def Unsubscribe(self, action: System.Action[TEventArgs]) -> None: ...
    def Reset(self) -> None: ...
    def Subscribe(self, action: System.Action[TEventArgs]) -> None: ...

class NotificationServiceBase:  # Class
    def Subscribe(self, action: System.Action[TEventArgs]) -> None: ...
    def Unsubscribe(self, action: System.Action[TEventArgs]) -> None: ...
    def Raise(self, args: TEventArgs) -> None: ...
    def Get(self) -> TEvent: ...
