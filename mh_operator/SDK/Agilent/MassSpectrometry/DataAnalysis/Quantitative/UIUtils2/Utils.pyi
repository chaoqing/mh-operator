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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils

class ContainsOperator(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class EqualOperator(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class FindOperator:  # Class
    def Match(self, value1: Any, value2: Any) -> bool: ...
    @staticmethod
    def Create(
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType,
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
    ): ...
    @staticmethod
    def RequiresValue(
        type: Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType,
    ) -> bool: ...

class FindOperatorType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Contains: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType
    ) = ...  # static # readonly
    Equal: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType
    ) = ...  # static # readonly
    Greater: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType
    ) = ...  # static # readonly
    GreaterEqual: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType
    ) = ...  # static # readonly
    IsNull: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType
    ) = ...  # static # readonly
    Less: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType
    ) = ...  # static # readonly
    LessEqual: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType
    ) = ...  # static # readonly
    NotContains: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType
    ) = ...  # static # readonly
    NotEqual: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType
    ) = ...  # static # readonly
    NotNull: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperatorType
    ) = ...  # static # readonly

class GreaterEqualOperator(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class GreaterOperator(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class IsNullOperator(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class LessEqualOperator(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class LessOperator(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class NotContainsOperator(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class NotEqualOperator(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...

class NotNullOperator(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.UIUtils2.Utils.FindOperator
):  # Class
    def __init__(self) -> None: ...
    def Match(self, value1: Any, value2: Any) -> bool: ...
