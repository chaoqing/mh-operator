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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse

class CommandLineAlias:  # Class
    def __init__(
        self,
        aliasAttr: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineSwitchAliasAttribute,
        cmdLineSwitch: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineSwitch,
    ) -> None: ...

    Attribute: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineSwitchAliasAttribute
    )  # readonly
    Supplied: bool
    SwitchObject: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineSwitch
    )  # readonly

    def AddValue(self, value_: str) -> None: ...

class CommandLineException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...
    def GetObjectData(
        self,
        info: System.Runtime.Serialization.SerializationInfo,
        context: System.Runtime.Serialization.StreamingContext,
    ) -> None: ...

class CommandLineParameterType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    AllowMultiple: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineParameterType
    ) = ...  # static # readonly
    HasParameter: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineParameterType
    ) = ...  # static # readonly
    Optional: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineParameterType
    ) = ...  # static # readonly
    ParameterIsOptional: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineParameterType
    ) = ...  # static # readonly

class CommandLineParser:  # Class
    def __init__(self) -> None: ...
    def DisplayOptionDescriptions(
        self,
        type: System.Type,
        resourceManager: System.Resources.ResourceManager,
        writer: System.IO.TextWriter,
        width: int,
    ) -> None: ...
    def Parse(self, parameters: List[str], objCmdLine: Any) -> None: ...

class CommandLineSwitch:  # Class
    def __init__(
        self,
        switchAttribute: Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineSwitchAttribute,
        memberInfo: System.Reflection.MemberInfo,
    ) -> None: ...

    Attribute: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineSwitchAttribute
    )  # readonly
    HasValues: bool  # readonly
    Supplied: bool
    ValueCount: int  # readonly

    def AddValue(self, value_: str) -> None: ...
    def Notify(self, objCmdLine: Any) -> None: ...

class CommandLineSwitchAliasAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, alias: str) -> None: ...

    Alias: str  # readonly

class CommandLineSwitchAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, key: str) -> None: ...

    AllowsParameter: bool  # readonly
    Description: str
    Hidden: bool
    Key: str  # readonly
    ParameterName: str
    ParameterType: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.CommandLineParse.CommandLineParameterType
    )
