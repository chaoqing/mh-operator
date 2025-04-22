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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing

class HeaderFooterBitmap(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing.HeaderFooterElementBase
):  # Class
    def __init__(self) -> None: ...

    File: str

    def Draw(
        self,
        graphics: System.Drawing.Graphics,
        rc: System.Drawing.Rectangle,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing.HeaderFooterParameters,
    ) -> System.Drawing.Size: ...

class HeaderFooterDefinition:  # Class
    def __init__(self) -> None: ...

    Footer: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing.HeaderFooterRegion
    )
    Header: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing.HeaderFooterRegion
    )

    def Draw(
        self,
        graphics: System.Drawing.Graphics,
        margin: System.Drawing.Rectangle,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing.HeaderFooterParameters,
    ) -> System.Drawing.Rectangle: ...

class HeaderFooterElementBase:  # Class
    def __init__(self) -> None: ...

    Height: str
    HorizontalAlignment: System.Windows.Forms.HorizontalAlignment

    def Draw(
        self,
        graphics: System.Drawing.Graphics,
        rc: System.Drawing.Rectangle,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing.HeaderFooterParameters,
    ) -> System.Drawing.Size: ...

class HeaderFooterParameters:  # Class
    def __init__(self) -> None: ...
    def Replace(self, value_: str) -> str: ...
    def SetStringMap(self, key: str, value_: Any) -> None: ...

class HeaderFooterRegion:  # Class
    def __init__(self) -> None: ...

    Elements: List[
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing.HeaderFooterElementBase
    ]
    Height: str

    def Draw(
        self,
        graphics: System.Drawing.Graphics,
        rect: System.Drawing.Rectangle,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing.HeaderFooterParameters,
    ) -> None: ...
    def GetHeightInPixel(self, graphics: System.Drawing.Graphics) -> int: ...

class HeaderFooterTextBox(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing.HeaderFooterElementBase
):  # Class
    def __init__(self) -> None: ...

    FontFamily: str
    FontSize: float
    FontStyle: System.Drawing.FontStyle
    Format: str
    Text: str

    def Draw(
        self,
        graphics: System.Drawing.Graphics,
        rc: System.Drawing.Rectangle,
        parameters: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Printing.HeaderFooterParameters,
    ) -> System.Drawing.Size: ...
