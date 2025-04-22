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

# Discovered Generic TypeVars:
T = TypeVar("T")

# Stubs for namespace: System.Windows.Interactivity

class AttachableCollection(
    System.Windows.FreezableCollection[T],
    Generic[T],
    Iterable[T],
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Collections.Specialized.INotifyCollectionChanged,
    Iterable[Any],
    System.ComponentModel.INotifyPropertyChanged,
    List[Any],
    System.Windows.Interactivity.IAttachedObject,
    List[T],
    Sequence[T],
    Sequence[Any],
):  # Class
    def Attach(self, dependencyObject: System.Windows.DependencyObject) -> None: ...
    def Detach(self) -> None: ...

class Behavior(
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Animation.Animatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    def Attach(self, dependencyObject: System.Windows.DependencyObject) -> None: ...
    def Detach(self) -> None: ...

class BehaviorCollection(
    Iterable[System.Windows.Interactivity.Behavior],
    System.Windows.ISealable,
    System.Windows.Interactivity.AttachableCollection[
        System.Windows.Interactivity.Behavior
    ],
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    Iterable[Any],
    List[System.Windows.Interactivity.Behavior],
    List[Any],
    Sequence[System.Windows.Interactivity.Behavior],
    System.Collections.Specialized.INotifyCollectionChanged,
    System.ComponentModel.INotifyPropertyChanged,
    System.Windows.Interactivity.IAttachedObject,
    Sequence[Any],
):  # Class
    ...

class Behavior(
    System.Windows.ISealable,
    Generic[T],
    System.Windows.Interactivity.Behavior,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    ...

class CustomPropertyValueEditor(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Element: System.Windows.Interactivity.CustomPropertyValueEditor = (
        ...
    )  # static # readonly
    ElementBinding: System.Windows.Interactivity.CustomPropertyValueEditor = (
        ...
    )  # static # readonly
    PropertyBinding: System.Windows.Interactivity.CustomPropertyValueEditor = (
        ...
    )  # static # readonly
    StateName: System.Windows.Interactivity.CustomPropertyValueEditor = (
        ...
    )  # static # readonly
    Storyboard: System.Windows.Interactivity.CustomPropertyValueEditor = (
        ...
    )  # static # readonly

class CustomPropertyValueEditorAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(
        self,
        customPropertyValueEditor: System.Windows.Interactivity.CustomPropertyValueEditor,
    ) -> None: ...

    CustomPropertyValueEditor: (
        System.Windows.Interactivity.CustomPropertyValueEditor
    )  # readonly

class DefaultTriggerAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    @overload
    def __init__(
        self, targetType: System.Type, triggerType: System.Type, parameter: Any
    ) -> None: ...
    @overload
    def __init__(
        self, targetType: System.Type, triggerType: System.Type, parameters: List[Any]
    ) -> None: ...

    Parameters: Iterable[Any]  # readonly
    TargetType: System.Type  # readonly
    TriggerType: System.Type  # readonly

    def Instantiate(self) -> System.Windows.Interactivity.TriggerBase: ...

class DependencyObjectHelper:  # Class
    @staticmethod
    def GetSelfAndAncestors(
        dependencyObject: System.Windows.DependencyObject,
    ) -> Iterable[System.Windows.DependencyObject]: ...

class EventObserver(System.IDisposable):  # Class
    def __init__(
        self,
        eventInfo: System.Reflection.EventInfo,
        target: Any,
        handler: System.Delegate,
    ) -> None: ...
    def Dispose(self) -> None: ...

class EventTrigger(
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.EventTriggerBase,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, eventName: str) -> None: ...

    EventNameProperty: System.Windows.DependencyProperty  # static # readonly

    EventName: str

class EventTriggerBase(
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Interactivity.TriggerBase,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    SourceNameProperty: System.Windows.DependencyProperty  # static # readonly
    SourceObjectProperty: System.Windows.DependencyProperty  # static # readonly

    Source: Any  # readonly
    SourceName: str
    SourceObject: Any

class EventTriggerBase(
    System.Windows.ISealable,
    Generic[T],
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.EventTriggerBase,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    Source: T  # readonly

class IAttachedObject(object):  # Interface
    AssociatedObject: System.Windows.DependencyObject  # readonly

    def Attach(self, dependencyObject: System.Windows.DependencyObject) -> None: ...
    def Detach(self) -> None: ...

class Interaction:  # Class
    @staticmethod
    def GetBehaviors(
        obj: System.Windows.DependencyObject,
    ) -> System.Windows.Interactivity.BehaviorCollection: ...
    @staticmethod
    def GetTriggers(
        obj: System.Windows.DependencyObject,
    ) -> System.Windows.Interactivity.TriggerCollection: ...

class InvokeCommandAction(
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.TriggerAction[System.Windows.DependencyObject],
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    def __init__(self) -> None: ...

    CommandParameterProperty: System.Windows.DependencyProperty  # static # readonly
    CommandProperty: System.Windows.DependencyProperty  # static # readonly

    Command: System.Windows.Input.ICommand
    CommandName: str
    CommandParameter: Any

class PreviewInvokeEventArgs(System.EventArgs):  # Class
    def __init__(self) -> None: ...

    Cancelling: bool

class TargetedTriggerAction(
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Interactivity.TriggerAction,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    TargetNameProperty: System.Windows.DependencyProperty  # static # readonly
    TargetObjectProperty: System.Windows.DependencyProperty  # static # readonly

    TargetName: str
    TargetObject: Any

class TargetedTriggerAction(
    System.Windows.ISealable,
    Generic[T],
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Interactivity.TargetedTriggerAction,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    ...

class TriggerAction(
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Animation.Animatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    IsEnabledProperty: System.Windows.DependencyProperty  # static # readonly

    IsEnabled: bool

    def Attach(self, dependencyObject: System.Windows.DependencyObject) -> None: ...
    def Detach(self) -> None: ...

class TriggerActionCollection(
    Sequence[System.Windows.Interactivity.TriggerAction],
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    List[System.Windows.Interactivity.TriggerAction],
    Iterable[Any],
    Iterable[System.Windows.Interactivity.TriggerAction],
    List[Any],
    System.Windows.Interactivity.AttachableCollection[
        System.Windows.Interactivity.TriggerAction
    ],
    System.Collections.Specialized.INotifyCollectionChanged,
    System.ComponentModel.INotifyPropertyChanged,
    System.Windows.Interactivity.IAttachedObject,
    Sequence[Any],
):  # Class
    ...

class TriggerAction(
    System.Windows.ISealable,
    Generic[T],
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Interactivity.TriggerAction,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    ...

class TriggerBase(
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Animation.Animatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    ActionsProperty: System.Windows.DependencyProperty  # static # readonly

    Actions: System.Windows.Interactivity.TriggerActionCollection  # readonly

    def Attach(self, dependencyObject: System.Windows.DependencyObject) -> None: ...
    def Detach(self) -> None: ...

    PreviewInvoke: System.EventHandler[
        System.Windows.Interactivity.PreviewInvokeEventArgs
    ]  # Event

class TriggerBase(
    System.Windows.ISealable,
    Generic[T],
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Interactivity.TriggerBase,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Interactivity.IAttachedObject,
):  # Class
    ...

class TriggerCollection(
    Iterable[System.Windows.Interactivity.TriggerBase],
    Sequence[System.Windows.Interactivity.TriggerBase],
    System.Windows.ISealable,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Collections.Specialized.INotifyCollectionChanged,
    System.Windows.Interactivity.AttachableCollection[
        System.Windows.Interactivity.TriggerBase
    ],
    Iterable[Any],
    List[Any],
    System.ComponentModel.INotifyPropertyChanged,
    System.Windows.Interactivity.IAttachedObject,
    List[System.Windows.Interactivity.TriggerBase],
    Sequence[Any],
):  # Class
    ...

class TypeConstraintAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, constraint: System.Type) -> None: ...

    Constraint: System.Type  # readonly
