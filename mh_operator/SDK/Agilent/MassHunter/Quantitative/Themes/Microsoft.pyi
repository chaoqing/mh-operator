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

# Stubs for namespace: Agilent.MassHunter.Quantitative.Themes.Microsoft

class CloseWindowCommand(System.Windows.Input.ICommand):  # Class
    def __init__(self) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Execute(self, parameter: Any) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class DialogWindowBehavior:  # Class
    LeftMouseButtonDrag: System.Windows.DependencyProperty  # static # readonly

    @staticmethod
    def GetLeftMouseButtonDrag(
        obj: System.Windows.DependencyObject,
    ) -> System.Windows.UIElement: ...
    @staticmethod
    def SetLeftMouseButtonDrag(
        obj: System.Windows.DependencyObject, window: System.Windows.UIElement
    ) -> None: ...

class ToolbarMenuItem(
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Input.ICommandSource,
    System.Windows.Markup.IQueryAmbient,
    MS.Internal.Controls.IGeneratorHost,
    System.Windows.Media.Animation.IAnimatable,
    System.ComponentModel.ISupportInitialize,
    System.Windows.IInputElement,
    System.Windows.Controls.MenuItem,
    System.Windows.IFrameworkInputElement,
    System.Windows.Markup.IAddChild,
    System.Windows.Controls.Primitives.IContainItemStorage,
    System.Windows.Markup.IHaveResources,
):  # Class
    def __init__(self) -> None: ...

    HeaderVisibilityProperty: System.Windows.DependencyProperty  # static # readonly
    IconVisibilityProperty: System.Windows.DependencyProperty  # static # readonly

    HeaderVisibility: System.Windows.Visibility
    IconVisibility: System.Windows.Visibility
