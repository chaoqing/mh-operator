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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.ToolHandlers

class CompoundTableToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class EditToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class FileToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class FindToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolTextBoxHandler,
):  # Class
    def __init__(self) -> None: ...

class HelpToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class SpectrumPlotToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolComboBoxHandler,
):  # Class
    def __init__(self) -> None: ...

class ToolsToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...

class ViewToolHandler(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Toolbar2.IToolHandler
):  # Class
    def __init__(self) -> None: ...
