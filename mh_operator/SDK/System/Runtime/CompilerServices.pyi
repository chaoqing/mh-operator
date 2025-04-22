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
TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")

# Stubs for namespace: System.Runtime.CompilerServices

class ArrayTypeNameAliasAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, typeName: str, alias: str) -> None: ...

    Alias: str
    TypeName: str

class ClientNameAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, name: str) -> None: ...

    AllowConflict: bool
    AllowObfuscation: bool
    ClientName: str

class ConvertToInstanceInvocationAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    @overload
    def __init__(self, name: str, instanceIndex: int) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

    Index: int
    Name: str

class DontHideAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class DontObfuscateAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self) -> None: ...

class DynamicDefaultValueAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class EncapsulatePrivateFieldsAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self) -> None: ...

class HideAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class IWidgetExternalObject(object):  # Interface
    InternalObject: Any  # readonly

class IWidgetInternalObject(object):  # Interface
    ExternalObject: Any  # readonly

class JAVAClientNameAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.ClientNameAttribute,
):  # Class
    def __init__(self, name: str) -> None: ...

class JAVADontHideAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.DontHideAttribute,
):  # Class
    def __init__(self) -> None: ...

class JAVAMainWidgetAttribute(
    System.Runtime.CompilerServices.MainWidgetAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class JAVASuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class JAVASuppressWidgetMemberCopyAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberCopyAttribute,
):  # Class
    def __init__(self) -> None: ...

class JAVAWeakAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self) -> None: ...

class JAVAWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class JAVAWidgetDefaultBooleanAttribute(
    System.Runtime.CompilerServices.WidgetDefaultBooleanAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    def __init__(self, value_: bool) -> None: ...

class JAVAWidgetDefaultNumberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetDefaultNumberAttribute,
):  # Class
    def __init__(self, value_: float) -> None: ...

class JAVAWidgetDefaultStringAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetDefaultStringAttribute,
):  # Class
    def __init__(self, value_: str) -> None: ...

class JAVAWidgetModuleAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetModuleAttribute,
):  # Class
    def __init__(self, name: str) -> None: ...

class JSClientNameAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.ClientNameAttribute,
):  # Class
    def __init__(self, name: str) -> None: ...

class JSMainWidgetAttribute(
    System.Runtime.CompilerServices.MainWidgetAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class JSSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class JSSuppressWidgetMemberCopyAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberCopyAttribute,
):  # Class
    def __init__(self) -> None: ...

class JSWeakAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self) -> None: ...

class JSWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class JSWidgetDefaultBooleanAttribute(
    System.Runtime.CompilerServices.WidgetDefaultBooleanAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    def __init__(self, value_: bool) -> None: ...

class JSWidgetDefaultNumberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetDefaultNumberAttribute,
):  # Class
    def __init__(self, value_: float) -> None: ...

class JSWidgetDefaultStringAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetDefaultStringAttribute,
):  # Class
    def __init__(self, value_: str) -> None: ...

class JSWidgetModuleAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetModuleAttribute,
):  # Class
    def __init__(self, name: str) -> None: ...

class JSWidgetSnippetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, exampleValue: str, isCode: bool) -> None: ...
    @overload
    def __init__(self, exampleValue: bool) -> None: ...
    @overload
    def __init__(self, exampleValue: float) -> None: ...

    BeforeInitializeCode: str
    EventDelegateCode: str
    OtherInitializeProperties: List[str]

class LogicalChildrenAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class MainWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

    Name: str

class ManuallyReleasedAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self) -> None: ...

class MvcEnumSetStringEnumAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class MvcSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class NativeWidgetNamespaceAttribute(
    System.Runtime.CompilerServices.WidgetNamespaceAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self, namespace: str) -> None: ...
    @overload
    def __init__(self, namespace: str, sourceNamespace: str) -> None: ...

class OBJCClientNameAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.ClientNameAttribute,
):  # Class
    def __init__(self, name: str) -> None: ...

class OBJCMainWidgetAttribute(
    System.Runtime.CompilerServices.MainWidgetAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class OBJCSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class OBJCSuppressWidgetMemberCopyAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberCopyAttribute,
):  # Class
    def __init__(self) -> None: ...

class OBJCWeakAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self) -> None: ...

class OBJCWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class OBJCWidgetDefaultBooleanAttribute(
    System.Runtime.CompilerServices.WidgetDefaultBooleanAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    def __init__(self, value_: bool) -> None: ...

class OBJCWidgetDefaultNumberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetDefaultNumberAttribute,
):  # Class
    def __init__(self, value_: float) -> None: ...

class OBJCWidgetDefaultStringAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetDefaultStringAttribute,
):  # Class
    def __init__(self, value_: str) -> None: ...

class OBJCWidgetModuleAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetModuleAttribute,
):  # Class
    def __init__(self, name: str) -> None: ...

class ObjCFrameworkNameAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, frameworkName: str) -> None: ...

    FrameworkName: str

class ObjCUseCArrayAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self) -> None: ...

    Name: str

class ReferenceGlobalShortNamesAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class ShortNamePrefixAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self, prefix: str) -> None: ...

    Prefix: str

class SuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class SuppressWidgetMemberCopyAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class TSClientNameAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.ClientNameAttribute,
):  # Class
    def __init__(self, name: str) -> None: ...

class TSIgnoreAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    def __init__(self) -> None: ...

class TSSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class TSWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class TranslatedTypePrefixAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    @overload
    def __init__(self, prefix: str, typeNamespace: str) -> None: ...
    @overload
    def __init__(self, prefix: str) -> None: ...

    Prefix: str
    TypeNamespace: str

class TreatAsDPAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class TreatAsNumberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class TreatAsPXAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class TreatAsSPAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class UseSimpleObjCMethodNamingAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class UwpWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class UwpWidgetMemberNameAttribute(
    System.Runtime.CompilerServices.WidgetMemberNameAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    def __init__(self, name: str) -> None: ...

class UwpWidgetNamespaceAttribute(
    System.Runtime.CompilerServices.WidgetNamespaceAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self, namespace: str) -> None: ...
    @overload
    def __init__(self, namespace: str, sourceNamespace: str) -> None: ...

class WFSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class WFWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class WFWidgetCategoryAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self, category: str) -> None: ...

class WFWidgetDesignTimeHiddenAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class WFWidgetEventManagerAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(
        self,
        enumPrefix: str,
        canAccessInternals: bool,
        includeMouseElementEvents: bool,
        includeGestureEvents: bool,
    ) -> None: ...

class WFWidgetEventManagerGroupAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self, eventGroupName: str) -> None: ...

class WFWidgetMemberNameAttribute(
    System.Runtime.CompilerServices.WidgetMemberNameAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    def __init__(self, name: str) -> None: ...

class WFWidgetNamespaceAttribute(
    System.Runtime.CompilerServices.WidgetNamespaceAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self, namespace: str) -> None: ...
    @overload
    def __init__(self, namespace: str, sourceNamespace: str) -> None: ...

class WeakAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self) -> None: ...

class WfWidgetDescriptionAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self, generateDescription: bool) -> None: ...

class WfWidgetPropertyChangeIdAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self, enumName: str, internalEnumFullName: str = ...) -> None: ...

class WidgetAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

    Name: str  # readonly

class WidgetAttributeBase(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    ...

class WidgetDefaultBooleanAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, value_: bool) -> None: ...

    Value: bool

class WidgetDefaultNumberAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, value_: float) -> None: ...

    Value: float

class WidgetDefaultStringAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, value_: str) -> None: ...

    Value: str

class WidgetDependencyPropertyAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, isDependencyProperty: bool) -> None: ...

class WidgetElementAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class WidgetFlattenedMemberInfoAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self, propertyNamePattern: str = ...) -> None: ...

class WidgetFontPropertyAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(
        self,
        propertyPrefix: str,
        simpleCommentDescription: str,
        defaultFontFamily: str = ...,
        defaultFontSize: float = ...,
        defaultBold: bool = ...,
        defaultItalic: bool = ...,
    ) -> None: ...

class WidgetIgnoreDependsAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, name: str) -> None: ...

    Name: str

class WidgetIncludeDependsAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, name: str) -> None: ...

    Name: str

class WidgetMemberNameAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, name: str) -> None: ...

    Name: str

class WidgetModuleAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self, name: str) -> None: ...

    Name: str

class WidgetModuleExclusionParentAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, name: str) -> None: ...

    Name: str

class WidgetModuleParentAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, name: str) -> None: ...

    Name: str
    RestrictToSameAssembly: bool

class WidgetNamespaceAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    @overload
    def __init__(self, namespace: str) -> None: ...
    @overload
    def __init__(self, namespace: str, sourceNamespace: str) -> None: ...

class WidgetPropertyToFlattenAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(
        self, propertyPrefix: str, propertiesToSuppress: List[str] = ...
    ) -> None: ...

class WidgetUniquePrefixAttribute(
    System.Runtime.InteropServices._Attribute, System.Attribute
):  # Class
    def __init__(self, prefix: str) -> None: ...

class WidgetUtilities:  # Class
    @staticmethod
    def ToExternalObject(internalObject: Any) -> Any: ...
    @staticmethod
    def FromExternalObject(externalObject: Any) -> Any: ...
    @overload
    @staticmethod
    def Convert(
        input: System.Nullable[TInput], conversion: System.Func[TInput, TOutput]
    ) -> System.Nullable[TOutput]: ...
    @overload
    @staticmethod
    def Convert(
        input: List[TInput], converter: System.Func[TInput, TOutput]
    ) -> List[TOutput]: ...

class WpfSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class WpfWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class XamAndroidSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class XamAndroidWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class XamAndroidWidgetNamespaceAttribute(
    System.Runtime.CompilerServices.WidgetNamespaceAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self, namespace: str) -> None: ...
    @overload
    def __init__(self, namespace: str, sourceNamespace: str) -> None: ...

class XamSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class XamTwoWayPropertyAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self, isTwoWay: bool = ...) -> None: ...

class XamWPSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class XamWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class XamWidgetMemberNameAttribute(
    System.Runtime.CompilerServices.WidgetMemberNameAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    def __init__(self, name: str) -> None: ...

class XamWrapperAndroidWidgetNamespaceAttribute(
    System.Runtime.CompilerServices.WidgetNamespaceAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self, namespace: str) -> None: ...
    @overload
    def __init__(self, namespace: str, sourceNamespace: str) -> None: ...

class XamWrapperAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class XamWrapperCreateDefaultValueAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class XamWrapperIOSWidgetNamespaceAttribute(
    System.Runtime.CompilerServices.WidgetNamespaceAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self, namespace: str) -> None: ...
    @overload
    def __init__(self, namespace: str, sourceNamespace: str) -> None: ...

class XamWrapperSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class XamWrapperUwpWidgetNamespaceAttribute(
    System.Runtime.CompilerServices.WidgetNamespaceAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self, namespace: str) -> None: ...
    @overload
    def __init__(self, namespace: str, sourceNamespace: str) -> None: ...

class XamWrapperWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class XamWrapperWidgetNamespaceAttribute(
    System.Runtime.CompilerServices.WidgetNamespaceAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self, namespace: str) -> None: ...
    @overload
    def __init__(self, namespace: str, sourceNamespace: str) -> None: ...

class XamiOSEnumNameAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self, value_: str) -> None: ...

    Value: str

class XamiOSSuppressWidgetMemberAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.SuppressWidgetMemberAttribute,
):  # Class
    def __init__(self) -> None: ...

class XamiOSTreatAsDoubleAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class XamiOSTreatAsFloatAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttributeBase,
):  # Class
    def __init__(self) -> None: ...

class XamiOSWidgetAttribute(
    System.Runtime.InteropServices._Attribute,
    System.Runtime.CompilerServices.WidgetAttribute,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...

class XamiOSWidgetNamespaceAttribute(
    System.Runtime.CompilerServices.WidgetNamespaceAttribute,
    System.Runtime.InteropServices._Attribute,
):  # Class
    @overload
    def __init__(self, namespace: str) -> None: ...
    @overload
    def __init__(self, namespace: str, sourceNamespace: str) -> None: ...
