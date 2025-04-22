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

# Stubs for namespace: Agilent.MassHunter.ReportBuilder.DataSource.Quant.CustomUI.GraphicsControls

class SampleGraphicsControl(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.UserControl,
    System.Windows.IInputElement,
    System.Windows.Markup.IHaveResources,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Markup.IAddChild,
):  # Class
    def __init__(self) -> None: ...
    def InitializeComponent(self) -> None: ...
