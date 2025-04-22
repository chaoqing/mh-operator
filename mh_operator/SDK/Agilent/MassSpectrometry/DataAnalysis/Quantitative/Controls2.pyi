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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2

class ColorComboBox(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.OwnerDrawComboBox,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
):  # Class
    def __init__(self) -> None: ...

    SelectedColor: Optional[System.Drawing.Color]  # readonly

    def Initialize(
        self,
        items: List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.ColorComboBoxItem
        ],
    ) -> None: ...
    def SetSelectedColor(self, color: System.Drawing.Color) -> None: ...

class ColorComboBoxItem(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.OwnerDrawComboBoxItem
):  # Class
    def __init__(self, color: System.Drawing.Color, text: str) -> None: ...

    Color: System.Drawing.Color
    Text: str

    def Draw(
        self,
        parent: System.Windows.Forms.Control,
        e: System.Windows.Forms.DrawItemEventArgs,
    ) -> None: ...
    @staticmethod
    def GetStandardColorItems() -> (
        List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.ColorComboBoxItem
        ]
    ): ...

class ColorListDialog(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...
    def Initialize(
        self,
        defaultColors: Iterable[System.Drawing.Color],
        colors: Iterable[System.Drawing.Color],
    ) -> None: ...
    def GetColors(self) -> List[System.Drawing.Color]: ...

class ColumnGroupGrid(
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UserControl,
):  # Class
    def __init__(self) -> None: ...

    DataGridView: System.Windows.Forms.DataGridView  # readonly
    DisplayRectangle: System.Drawing.Rectangle  # readonly

    def AddGroup(self, group: str, caption: str) -> None: ...
    def GroupExists(self, group: str) -> bool: ...
    def GetColumnGroup(self, column: str) -> str: ...
    def ClearGroups(self) -> None: ...
    def SetColumnGroup(self, column: str, group: str) -> None: ...
    def GetGroupCaption(self, group: str) -> str: ...

class DataGridViewPathNameCell(
    System.IDisposable, System.ICloneable, System.Windows.Forms.DataGridViewTextBoxCell
):  # Class
    def PositionEditingControl(
        self,
        setLocation: bool,
        setSize: bool,
        cellBounds: System.Drawing.Rectangle,
        cellClip: System.Drawing.Rectangle,
        cellStyle: System.Windows.Forms.DataGridViewCellStyle,
        singleVerticalBorderAdded: bool,
        singleHorizontalBorderAdded: bool,
        isFirstDisplayedColumn: bool,
        isFirstDisplayedRow: bool,
    ) -> None: ...

class FontFamilyComboBox(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.OwnerDrawComboBox,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
):  # Class
    def __init__(self) -> None: ...

    SelectedFont: System.Drawing.FontFamily

    def Initialize(
        self,
        items: List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.FontFamilyComboBoxItem
        ],
    ) -> None: ...

class FontFamilyComboBoxItem(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.OwnerDrawComboBoxItem
):  # Class
    def __init__(self, fontFamily: System.Drawing.FontFamily) -> None: ...

    FontFamily: System.Drawing.FontFamily  # readonly

    def Draw(
        self,
        parent: System.Windows.Forms.Control,
        e: System.Windows.Forms.DrawItemEventArgs,
    ) -> None: ...
    @staticmethod
    def GetStandardItems() -> (
        List[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.FontFamilyComboBoxItem
        ]
    ): ...

class HatchStyleComboBox(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.OwnerDrawComboBox,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
):  # Class
    def __init__(self) -> None: ...

    SelectedHatchStyle: Optional[System.Drawing.Drawing2D.HatchStyle]

class HatchStyleComboBoxItem(
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.OwnerDrawComboBoxItem
):  # Class
    def __init__(
        self, hs: Optional[System.Drawing.Drawing2D.HatchStyle], text: str
    ) -> None: ...

    HatchStyle: Optional[System.Drawing.Drawing2D.HatchStyle]
    Text: str

    def Draw(
        self,
        parent: System.Windows.Forms.Control,
        e: System.Windows.Forms.DrawItemEventArgs,
    ) -> None: ...

class IPropertyPage(object):  # Interface
    Control: System.Windows.Forms.Control  # readonly
    DisplayName: str
    IsDirty: bool  # readonly

    def SetActive(self) -> None: ...
    def DoDefault(self) -> None: ...
    def Apply(self) -> None: ...

    PageChanged: System.EventHandler  # Event

class IWizard(object):  # Interface
    ActivePage: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IWizardPage
    ActivePageIndex: int
    Count: int  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IWizardPage: ...
    Title: str

    def AddPages(
        self,
        pages: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IWizardPage
        ],
    ) -> None: ...
    def SetButtons(
        self,
        buttons: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.WizardButtons,
    ) -> None: ...
    def AddPage(
        self,
        page: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IWizardPage,
    ) -> None: ...

class IWizardPage(System.IDisposable):  # Interface
    Control: System.Windows.Forms.Control  # readonly
    Description: str  # readonly
    PageSize: System.Drawing.Size  # readonly
    Title: str  # readonly

    def OnFinish(self) -> bool: ...
    def OnNext(self) -> bool: ...
    def OnBack(self) -> bool: ...
    def DeactivatePage(self) -> None: ...
    def ActivatePage(
        self,
        wizard: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IWizard,
    ) -> None: ...

class LineStyleLabel(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.Label,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
):  # Class
    def __init__(self) -> None: ...

    Color: System.Drawing.Color
    DashStyle: System.Drawing.Drawing2D.DashStyle
    NoDisplayText: str
    ShowLine: bool

class OwnerDrawComboBox(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.ComboBox,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
):  # Class
    def __init__(self) -> None: ...

class OwnerDrawComboBoxItem:  # Class
    def Draw(
        self,
        parent: System.Windows.Forms.Control,
        e: System.Windows.Forms.DrawItemEventArgs,
    ) -> None: ...

class PropertySheet(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

    IsDirty: bool  # readonly
    SelectedPageIndex: int

    def AddRange(
        self,
        pages: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage
        ],
    ) -> None: ...
    def Add(
        self,
        page: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IPropertyPage,
    ) -> None: ...

class SeparatorControl(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.Control,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
):  # Class
    def __init__(self) -> None: ...

class SimpleAboutBox(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

    AppName: str
    BuildNumber: str
    Copyright: str
    Image: System.Drawing.Image
    PatchNumber: str
    VersionNumber: str

class TitledContainer(
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.UserControl,
):  # Class
    def __init__(self) -> None: ...

    DisplayRectangle: System.Drawing.Rectangle  # readonly
    Title: str

class Wizard(
    System.Windows.Forms.Layout.IArrangedElement,
    Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IWizard,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IContainerControl,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.Form,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.Windows.Forms.IWin32Window,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.IDisposable,
    System.ComponentModel.ISynchronizeInvoke,
):  # Class
    def __init__(self) -> None: ...

    ActivePage: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IWizardPage
    ActivePageIndex: int
    Count: int  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IWizardPage: ...
    Title: str

    def AddPages(
        self,
        pages: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IWizardPage
        ],
    ) -> None: ...
    def SetButtons(
        self,
        buttons: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.WizardButtons,
    ) -> None: ...
    def AddPage(
        self,
        page: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.IWizardPage,
    ) -> None: ...

class WizardButtons(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    EnableBack: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.WizardButtons
    ) = ...  # static # readonly
    EnableCancel: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.WizardButtons
    ) = ...  # static # readonly
    EnableFinish: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.WizardButtons
    ) = ...  # static # readonly
    EnableNext: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Controls2.WizardButtons
    ) = ...  # static # readonly

class XmlTreeViewControl(
    System.IDisposable,
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject2,
    System.ComponentModel.ISynchronizeInvoke,
    System.ComponentModel.IComponent,
    System.Windows.Forms.UnsafeNativeMethods.IQuickActivate,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceActiveObject,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStorage,
    System.Windows.Forms.UnsafeNativeMethods.IPersistPropertyBag,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.UnsafeNativeMethods.IOleObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.UnsafeNativeMethods.IPersist,
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.UnsafeNativeMethods.IViewObject,
    System.Windows.Forms.IDropTarget,
    System.Windows.Forms.UnsafeNativeMethods.IOleWindow,
    System.Windows.Forms.TreeView,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.Layout.IArrangedElement,
):  # Class
    def __init__(self) -> None: ...

    Document: System.Xml.XPath.IXPathNavigable
