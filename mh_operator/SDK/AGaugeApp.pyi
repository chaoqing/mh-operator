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

# Stubs for namespace: AGaugeApp

class AGauge(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.Control,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
):  # Class
    def __init__(self) -> None: ...

    AllowDrop: bool
    AutoSize: bool
    BackColor: System.Drawing.Color
    BackgroundImageLayout: System.Windows.Forms.ImageLayout
    BaseArcColor: System.Drawing.Color
    BaseArcRadius: int
    BaseArcStart: int
    BaseArcSweep: int
    BaseArcWidth: int
    CapColors: List[System.Drawing.Color]
    CapPosition: System.Drawing.Point
    CapText: str
    Cap_Idx: int
    CapsPosition: List[System.Drawing.Point]
    CapsText: List[str]
    Center: System.Drawing.Point
    Font: System.Drawing.Font
    ForeColor: bool
    ImeMode: bool
    MaxValue: float
    MinValue: float
    NeedleColor1: AGaugeApp.AGauge.NeedleColorEnum
    NeedleColor2: System.Drawing.Color
    NeedleRadius: int
    NeedleType: int
    NeedleWidth: int
    RangeColor: System.Drawing.Color
    RangeEnabled: bool
    RangeEndValue: float
    RangeInnerRadius: int
    RangeOuterRadius: int
    RangeStartValue: float
    Range_Idx: int
    RangesColor: List[System.Drawing.Color]
    RangesEnabled: List[bool]
    RangesEndValue: List[float]
    RangesInnerRadius: List[int]
    RangesOuterRadius: List[int]
    RangesStartValue: List[float]
    ScaleLinesInterColor: System.Drawing.Color
    ScaleLinesInterInnerRadius: int
    ScaleLinesInterOuterRadius: int
    ScaleLinesInterWidth: int
    ScaleLinesMajorColor: System.Drawing.Color
    ScaleLinesMajorInnerRadius: int
    ScaleLinesMajorOuterRadius: int
    ScaleLinesMajorStepValue: float
    ScaleLinesMajorWidth: int
    ScaleLinesMinorColor: System.Drawing.Color
    ScaleLinesMinorInnerRadius: int
    ScaleLinesMinorNumOf: int
    ScaleLinesMinorOuterRadius: int
    ScaleLinesMinorWidth: int
    ScaleNumbersColor: System.Drawing.Color
    ScaleNumbersFormat: str
    ScaleNumbersRadius: int
    ScaleNumbersRotation: int
    ScaleNumbersStartScaleLine: int
    ScaleNumbersStepScaleLines: int
    Value: float

    ValueInRangeChanged: AGaugeApp.AGauge.ValueInRangeChangedDelegate  # Event

    # Nested Types

    class NeedleColorEnum(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        Blue: AGaugeApp.AGauge.NeedleColorEnum = ...  # static # readonly
        Gray: AGaugeApp.AGauge.NeedleColorEnum = ...  # static # readonly
        Green: AGaugeApp.AGauge.NeedleColorEnum = ...  # static # readonly
        Magenta: AGaugeApp.AGauge.NeedleColorEnum = ...  # static # readonly
        Red: AGaugeApp.AGauge.NeedleColorEnum = ...  # static # readonly
        Violet: AGaugeApp.AGauge.NeedleColorEnum = ...  # static # readonly
        Yellow: AGaugeApp.AGauge.NeedleColorEnum = ...  # static # readonly

    class ValueInRangeChangedDelegate(
        System.MulticastDelegate,
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> None: ...
        def BeginInvoke(
            self,
            sender: Any,
            e: AGaugeApp.AGauge.ValueInRangeChangedEventArgs,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(
            self, sender: Any, e: AGaugeApp.AGauge.ValueInRangeChangedEventArgs
        ) -> None: ...

    class ValueInRangeChangedEventArgs(System.EventArgs):  # Class
        def __init__(self, valueInRange: int) -> None: ...

        valueInRange: int
