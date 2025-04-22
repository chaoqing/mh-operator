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

# Stubs for namespace: Agilent.OpenLab.Framework.DataAccess.AcamlInfrastructure.Extensions

class ExtensionsIDataFileRefType:  # Class
    @staticmethod
    def GetPath(
        dataFileRef: Agilent.OpenLab.Framework.DataAccess.AcamlObjectModel.IDataFileRefType,
        pathHelper: Agilent.OpenLab.Framework.Infrastructure.Storage.Interfaces.IPathHelper,
        rootPath: str,
    ) -> str: ...
