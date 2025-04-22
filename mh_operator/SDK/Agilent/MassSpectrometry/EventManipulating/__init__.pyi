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

from . import Model
from .Model import IEventContext, IEventManipulator, IRubberBand

# Stubs for namespace: Agilent.MassSpectrometry.EventManipulating

class EventContext(System.IDisposable, IEventContext):  # Class
    def __init__(self) -> None: ...

    ControlCount: int  # readonly
    StackCount: int  # readonly
    Top: IEventManipulator  # readonly

    def RegisterControl(self, ctrl: System.Windows.Forms.Control) -> None: ...
    def RevokeControl(self, ctrl: System.Windows.Forms.Control) -> None: ...
    def Pop(self, em: IEventManipulator) -> None: ...
    def Peek(self, index: int) -> IEventManipulator: ...
    def Dispose(self) -> None: ...
    def Push(self, em: IEventManipulator) -> None: ...

class EventManipulator(System.IDisposable, IEventManipulator):  # Class
    EventContext: IEventContext  # readonly
    IsOnStack: bool  # readonly
    RubberBand: IRubberBand

    def OnMouseDown(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseDoubleClick(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnEnd(self) -> None: ...
    def OnMouseMove(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnMouseUp(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnKeyDown(self, sender: Any, e: System.Windows.Forms.KeyEventArgs) -> None: ...
    def OnMouseWheel(
        self, sender: Any, e: System.Windows.Forms.MouseEventArgs
    ) -> None: ...
    def OnStart(self) -> None: ...
    def Pop(self) -> None: ...
    def OnResume(self) -> None: ...
    def Dispose(self) -> None: ...
    def OnDoubleClick(self, sender: Any, e: System.EventArgs) -> None: ...
    def OnKeyUp(self, sender: Any, e: System.Windows.Forms.KeyEventArgs) -> None: ...
    def Push(self) -> None: ...
    def OnSuspend(self) -> None: ...

class RubberBand(IRubberBand, System.IDisposable):  # Class
    Control: System.Windows.Forms.Control  # readonly
    LastPoint: System.Drawing.Point  # readonly

    def Erase(self) -> None: ...
    def Dispose(self) -> None: ...
    def MoveTo(
        self, ctrl: System.Windows.Forms.Control, point: System.Drawing.Point
    ) -> None: ...
