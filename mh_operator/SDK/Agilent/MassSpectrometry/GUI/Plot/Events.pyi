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

from . import IGraphics, Pane, ZoomInfo

# Stubs for namespace: Agilent.MassSpectrometry.GUI.Plot.Events

class DrawPaneEventArgs(System.EventArgs):  # Class
    @overload
    def __init__(
        self,
        pane: Pane,
        paneRectangle: System.Drawing.Rectangle,
        g: System.Drawing.Graphics,
    ) -> None: ...
    @overload
    def __init__(
        self, pane: Pane, paneRectangle: System.Drawing.Rectangle, g: IGraphics
    ) -> None: ...

    Graphics: System.Drawing.Graphics  # readonly
    IGraphics: IGraphics  # readonly
    Pane: Pane  # readonly
    PaneRectangle: System.Drawing.Rectangle  # readonly

class PaneEventArgs(System.EventArgs):  # Class
    def __init__(self, pane: Pane) -> None: ...

    Pane: Pane  # readonly

class ZoomHistoryEventArgs(System.EventArgs):  # Class
    def __init__(self, zoomInfoOld: ZoomInfo, zoomInfoNew: ZoomInfo) -> None: ...

    NewZoomInfo: ZoomInfo  # readonly
    OldZoomInfo: ZoomInfo  # readonly
