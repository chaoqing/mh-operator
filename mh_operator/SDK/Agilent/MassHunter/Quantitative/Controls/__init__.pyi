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

from . import FileDialog, NewBatch, OpenBatch, SaveAs, SplashScreen

# Stubs for namespace: Agilent.MassHunter.Quantitative.Controls

class BindingProxy(System.Windows.ISealable, System.Windows.Freezable):  # Class
    def __init__(self) -> None: ...

    DataProperty: System.Windows.DependencyProperty  # static # readonly

    Data: Any

class BindingUtils:  # Class
    @staticmethod
    def ClearAllDescendentBindings(
        dependencyObject: System.Windows.DependencyObject,
    ) -> None: ...
    @staticmethod
    def EnumerateVisualChildren(
        dependencyObject: System.Windows.DependencyObject,
    ) -> Iterable[System.Windows.DependencyObject]: ...
    @staticmethod
    def EnumerateVisualDescendents(
        dependencyObject: System.Windows.DependencyObject,
    ) -> Iterable[System.Windows.DependencyObject]: ...

class DelegateCommand(System.Windows.Input.ICommand):  # Class
    @overload
    def __init__(self, exec: System.Action) -> None: ...
    @overload
    def __init__(
        self, exec: System.Action, canExec: System.Func[Any, bool]
    ) -> None: ...
    def CanExecute(self, parameter: Any) -> bool: ...
    def Execute(self, parameter: Any) -> None: ...
    def NotifyCanExecuteChanged(self, e: System.EventArgs) -> None: ...

    CanExecuteChanged: System.EventHandler  # Event

class DropDownButton(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    System.Windows.Input.ICommandSource,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Controls.Primitives.ToggleButton,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...

    Items: System.Windows.Controls.ItemCollection  # readonly

    def InitializeComponent(self) -> None: ...

class Extensions:  # Class
    @staticmethod
    def FormatWith(s: str, args: List[Any]) -> str: ...

class HeaderedSeparator(
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.Control,
    System.Windows.IInputElement,
    System.Windows.Markup.IQueryAmbient,
    System.ComponentModel.ISupportInitialize,
    System.Windows.Markup.IHaveResources,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.IFrameworkInputElement,
):  # Class
    def __init__(self) -> None: ...

    HeaderProperty: System.Windows.DependencyProperty  # static

    Header: str

class HintedTextBox(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    System.Windows.Controls.ITextBoxViewHost,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Controls.TextBox,
    System.Windows.Markup.IComponentConnector,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...

    EnterKeyCommandParameterProperty: (
        System.Windows.DependencyProperty
    )  # static # readonly
    EnterKeyCommandProperty: System.Windows.DependencyProperty  # static # readonly
    HintTextColorProperty: System.Windows.DependencyProperty  # static # readonly
    HintTextProperty: System.Windows.DependencyProperty  # static # readonly

    EnterKeyCommand: System.Windows.Input.ICommand
    EnterKeyCommandParameter: Any
    HintText: str
    HintTextColor: System.Windows.Media.Color

    def InitializeComponent(self) -> None: ...

class IApplicationMenu2010Content(object):  # Interface
    def SetSize(self, width: float, height: float) -> None: ...

class ImageConverter(System.Windows.Data.IValueConverter):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, color: System.Windows.Media.Color) -> None: ...

    Color: System.Windows.Media.Color

    @overload
    @staticmethod
    def ConvertImage(
        image: System.Windows.Media.Imaging.BitmapSource,
        color: System.Windows.Media.Color,
    ) -> System.Windows.Media.Imaging.BitmapSource: ...
    @overload
    @staticmethod
    def ConvertImage(
        image: System.Windows.Media.Imaging.BitmapSource,
    ) -> System.Windows.Media.Imaging.BitmapSource: ...
    def ConvertBack(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...
    def Convert(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...

class InverseBooleanConverter(System.Windows.Data.IValueConverter):  # Class
    def __init__(self) -> None: ...
    def ConvertBack(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...
    def Convert(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...

class InverseBooleanToVisibilityConverter(System.Windows.Data.IValueConverter):  # Class
    def __init__(self) -> None: ...
    def ConvertBack(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...
    def Convert(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...

class PathTrimmingConverter(System.Windows.Data.IMultiValueConverter):  # Class
    def __init__(self) -> None: ...
    def ConvertBack(
        self,
        value_: Any,
        targetTypes: List[System.Type],
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> List[Any]: ...
    def Convert(
        self,
        values: List[Any],
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...

class ResxStringConverter(System.Windows.Data.IValueConverter):  # Class
    def __init__(self) -> None: ...
    def ConvertBack(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...
    def Convert(
        self,
        value_: Any,
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...

class ResxStringLocalizer:  # Class
    def __init__(self, pathBase: str) -> None: ...
    def GetString(
        self, name: str, culture: System.Globalization.CultureInfo
    ) -> str: ...

class SHFILEINFO:  # Struct
    dwAttributes: int
    hIcon: System.IntPtr
    iIcon: int
    szDisplayName: str
    szTypeName: str

class ShellFileInfo:  # Class
    def __init__(self) -> None: ...

    CSIDL_DRIVES: int = ...  # static # readonly
    SHGFI_DISPLAYNAME: int = ...  # static # readonly
    SHGFI_ICON: int = ...  # static # readonly
    SHGFI_LARGEICON: int = ...  # static # readonly
    SHGFI_SMALLICON: int = ...  # static # readonly

    @staticmethod
    def GetFileInfo(
        pathname: str, flags: int
    ) -> Agilent.MassHunter.Quantitative.Controls.SHFILEINFO: ...
    @staticmethod
    def GetFileInfoFromExtension(ext: str) -> System.IntPtr: ...

    # Nested Types

    class NativeMethods:  # Class
        def __init__(self) -> None: ...
        @staticmethod
        def SHGetFileInfo(
            pszPath: str,
            dwFileAttributes: int,
            psfi: Agilent.MassHunter.Quantitative.Controls.SHFILEINFO,
            cbSizeFileInfo: int,
            uFlags: int,
        ) -> System.IntPtr: ...
        @staticmethod
        def DestroyIcon(handle: System.IntPtr) -> bool: ...
        @staticmethod
        def ExtractIconEx(
            szFileName: str,
            nIconIndex: int,
            phiconLarge: List[System.IntPtr],
            phiconSmall: List[System.IntPtr],
            nIcons: int,
        ) -> int: ...
        @staticmethod
        def SHGetFolderPath(
            hwndOwner: System.IntPtr,
            nFolder: int,
            hToken: System.IntPtr,
            dwFlags: int,
            pszPath: System.Text.StringBuilder,
        ) -> int: ...

class SplitToolButton(
    System.Windows.Markup.IQueryAmbient,
    System.Windows.Media.Composition.DUCE.IResource,
    System.Windows.Markup.IHaveResources,
    System.Windows.Input.ICommandSource,
    System.Windows.Markup.IAddChild,
    System.Windows.Media.Animation.IAnimatable,
    System.Windows.Markup.IComponentConnector,
    System.Windows.Controls.Primitives.ToggleButton,
    System.Windows.IInputElement,
    System.Windows.IFrameworkInputElement,
    System.ComponentModel.ISupportInitialize,
):  # Class
    def __init__(self) -> None: ...

    Items: System.Windows.Controls.ItemCollection  # readonly

    def InitializeComponent(self) -> None: ...

class TextInputToVisibilityConverter(System.Windows.Data.IMultiValueConverter):  # Class
    def __init__(self) -> None: ...
    def ConvertBack(
        self,
        value_: Any,
        targetTypes: List[System.Type],
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> List[Any]: ...
    def Convert(
        self,
        values: List[Any],
        targetType: System.Type,
        parameter: Any,
        culture: System.Globalization.CultureInfo,
    ) -> Any: ...

class WpfWin32Window(System.Windows.Forms.IWin32Window):  # Class
    def __init__(self, wpfWindow: System.Windows.Window) -> None: ...

    Handle: System.IntPtr  # readonly
