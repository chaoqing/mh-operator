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

# Stubs for namespace: Agilent.MassSpectrometry.EventManipulating.Model

class IEventContext(System.IDisposable):  # Interface
    ControlCount: int  # readonly
    StackCount: int  # readonly
    Top: Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator  # readonly

    def RegisterControl(self, ctrl: System.Windows.Forms.Control) -> None: ...
    def RevokeControl(self, ctrl: System.Windows.Forms.Control) -> None: ...
    def Pop(
        self,
        manipulator: Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    ) -> None: ...
    def Peek(
        self, index: int
    ) -> Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator: ...
    def Push(
        self,
        manipulator: Agilent.MassSpectrometry.EventManipulating.Model.IEventManipulator,
    ) -> None: ...

class IEventManipulator(System.IDisposable):  # Interface
    RubberBand: Agilent.MassSpectrometry.EventManipulating.Model.IRubberBand

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
    def OnResume(self) -> None: ...
    def OnKeyUp(self, sender: Any, e: System.Windows.Forms.KeyEventArgs) -> None: ...
    def OnDoubleClick(self, sender: Any, e: System.EventArgs) -> None: ...
    def OnSuspend(self) -> None: ...

class IRubberBand(System.IDisposable):  # Interface
    def Erase(self) -> None: ...
    def MoveTo(
        self, ctrl: System.Windows.Forms.Control, position: System.Drawing.Point
    ) -> None: ...
