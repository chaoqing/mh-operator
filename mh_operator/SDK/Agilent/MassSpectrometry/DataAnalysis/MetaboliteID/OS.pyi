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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS

class ButtonStyle(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    BS_3STATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_AUTO3STATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_AUTOCHECKBOX: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle
    ) = ...  # static # readonly
    BS_AUTORADIOBUTTON: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle
    ) = ...  # static # readonly
    BS_BITMAP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_BOTTOM: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_CENTER: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_CHECKBOX: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_DEFPUSHBUTTON: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle
    ) = ...  # static # readonly
    BS_FLAT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_GROUPBOX: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_ICON: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_LEFT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_LEFTTEXT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_MULTILINE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_NOTIFY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_OWNERDRAW: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_PUSHBOX: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_PUSHBUTTON: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_PUSHLIKE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_RADIOBUTTON: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle
    ) = ...  # static # readonly
    BS_RIGHT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_RIGHTBUTTON: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle
    ) = ...  # static # readonly
    BS_TEXT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_TOP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_TYPEMASK: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_USERBUTTON: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly
    BS_VCENTER: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ButtonStyle = (
        ...
    )  # static # readonly

class ChildFromPointFlags(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CWP_ALL: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ChildFromPointFlags
    ) = ...  # static # readonly
    CWP_SKIPDISABLED: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ChildFromPointFlags
    ) = ...  # static # readonly
    CWP_SKIPINVISIBLE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ChildFromPointFlags
    ) = ...  # static # readonly
    CWP_SKIPTRANSPARENT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ChildFromPointFlags
    ) = ...  # static # readonly

class ComboBoxStyles(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CBS_AUTOHSCROLL: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly
    CBS_DISABLENOSCROLL: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly
    CBS_DROPDOWN: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly
    CBS_DROPDOWNLIST: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly
    CBS_HASSTRINGS: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly
    CBS_LOWERCASE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly
    CBS_NOINTEGRALHEIGHT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly
    CBS_OEMCONVERT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly
    CBS_OWNERDRAWFIXED: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly
    CBS_OWNERDRAWVARIABLE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly
    CBS_SIMPLE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles = (
        ...
    )  # static # readonly
    CBS_SORT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles = (
        ...
    )  # static # readonly
    CBS_UPPERCASE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ComboBoxStyles
    ) = ...  # static # readonly

class DefaultViewType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Details: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DefaultViewType = (
        ...
    )  # static # readonly
    Icons: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DefaultViewType = (
        ...
    )  # static # readonly
    List: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DefaultViewType = (
        ...
    )  # static # readonly
    Thumbnails: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DefaultViewType
    ) = ...  # static # readonly
    Tiles: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DefaultViewType = (
        ...
    )  # static # readonly

class DialogChangeProperties(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CDM_FIRST: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeProperties
    ) = ...  # static # readonly
    CDM_GETFILEPATH: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeProperties
    ) = ...  # static # readonly
    CDM_GETFOLDERIDLIST: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeProperties
    ) = ...  # static # readonly
    CDM_GETFOLDERPATH: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeProperties
    ) = ...  # static # readonly
    CDM_GETSPEC: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeProperties
    ) = ...  # static # readonly
    CDM_HIDECONTROL: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeProperties
    ) = ...  # static # readonly
    CDM_SETCONTROLTEXT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeProperties
    ) = ...  # static # readonly
    CDM_SETDEFEXT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeProperties
    ) = ...  # static # readonly

class DialogChangeStatus(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CDN_FILEOK: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeStatus
    ) = ...  # static # readonly
    CDN_FIRST: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeStatus
    ) = ...  # static # readonly
    CDN_FOLDERCHANGE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeStatus
    ) = ...  # static # readonly
    CDN_HELP: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeStatus
    ) = ...  # static # readonly
    CDN_INITDONE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeStatus
    ) = ...  # static # readonly
    CDN_SELCHANGE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeStatus
    ) = ...  # static # readonly
    CDN_SHAREVIOLATION: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeStatus
    ) = ...  # static # readonly
    CDN_TYPECHANGE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.DialogChangeStatus
    ) = ...  # static # readonly

class FolderViewMode(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Default: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.FolderViewMode = (
        ...
    )  # static # readonly
    Details: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.FolderViewMode = (
        ...
    )  # static # readonly
    Icon: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.FolderViewMode = (
        ...
    )  # static # readonly
    List: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.FolderViewMode = (
        ...
    )  # static # readonly
    SmallIcon: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.FolderViewMode = (
        ...
    )  # static # readonly
    Thumbnails: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.FolderViewMode = (
        ...
    )  # static # readonly
    Thumbstrip: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.FolderViewMode = (
        ...
    )  # static # readonly
    Title: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.FolderViewMode = (
        ...
    )  # static # readonly

class HitTest(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    HTBORDER: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTBOTTOM: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTBOTTOMLEFT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTBOTTOMRIGHT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTCAPTION: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTCLIENT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTCLOSE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTERROR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTGROWBOX: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTHELP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTHSCROLL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTLEFT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTMAXBUTTON: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTMENU: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTMINBUTTON: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTNOWHERE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTOBJECT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTREDUCE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTRIGHT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTSIZE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTSIZEFIRST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTSIZELAST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTSYSMENU: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTTOP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTTOPLEFT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTTOPRIGHT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTTRANSPARENT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTVSCROLL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly
    HTZOOM: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.HitTest = (
        ...
    )  # static # readonly

class ImeNotify(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    IMN_CHANGECANDIDATE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_CLOSECANDIDATE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_CLOSESTATUSWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_GUIDELINE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify = (
        ...
    )  # static # readonly
    IMN_OPENCANDIDATE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_OPENSTATUSWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_PRIVATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify = (
        ...
    )  # static # readonly
    IMN_SETCANDIDATEPOS: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_SETCOMPOSITIONFONT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_SETCOMPOSITIONWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_SETCONVERSIONMODE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_SETOPENSTATUS: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_SETSENTENCEMODE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly
    IMN_SETSTATUSWINDOWPOS: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ImeNotify
    ) = ...  # static # readonly

class Msg(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    WM_ACTIVATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_ACTIVATEAPP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_AFXFIRST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_AFXLAST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_APP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_ASKCBFORMATNAME: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CANCELJOURNAL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CANCELMODE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CAPTURECHANGED: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CHANGECBCHAIN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CHAR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CHARTOITEM: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CHILDACTIVATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CLEAR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CLOSE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_COMMAND: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_COMMNOTIFY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_COMPACTING: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_COMPAREITEM: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CONTEXTMENU: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_COPY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_COPYDATA: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CREATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CTLCOLOR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CTLCOLORBTN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CTLCOLORDLG: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CTLCOLOREDIT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CTLCOLORLISTBOX: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CTLCOLORMSGBOX: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CTLCOLORSCROLLBAR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CTLCOLORSTATIC: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_CUT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_DEADCHAR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_DELETEITEM: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_DESTROY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_DESTROYCLIPBOARD: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_DEVICECHANGE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_DEVMODECHANGE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_DISPLAYCHANGE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_DRAWCLIPBOARD: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_DRAWITEM: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_DROPFILES: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_ENABLE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_ENDSESSION: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_ENTERIDLE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_ENTERMENULOOP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_ENTERSIZEMOVE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_ERASEBKGND: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_EXITMENULOOP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_EXITSIZEMOVE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_FONTCHANGE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_GETDLGCODE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_GETFONT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_GETHOTKEY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_GETICON: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_GETMINMAXINFO: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_GETOBJECT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_GETTEXT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_GETTEXTLENGTH: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_HANDHELDFIRST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_HANDHELDLAST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_HELP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_HOTKEY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_HSCROLL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_HSCROLLCLIPBOARD: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_ICONERASEBKGND: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_CHAR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_COMPOSITION: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_COMPOSITIONFULL: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg
    ) = ...  # static # readonly
    WM_IME_CONTROL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_ENDCOMPOSITION: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_KEYDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_KEYLAST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_KEYUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_NOTIFY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_REQUEST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_SELECT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_SETCONTEXT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_IME_STARTCOMPOSITION: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg
    ) = ...  # static # readonly
    WM_INITDIALOG: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_INITMENU: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_INITMENUPOPUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_INPUTLANGCHANGE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_INPUTLANGCHANGEREQUEST: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg
    ) = ...  # static # readonly
    WM_KEYDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_KEYLAST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_KEYUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_KILLFOCUS: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_LBUTTONDBLCLK: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_LBUTTONDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_LBUTTONUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MBUTTONDBLCLK: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MBUTTONDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MBUTTONUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDIACTIVATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDICASCADE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDICREATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDIDESTROY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDIGETACTIVE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDIICONARRANGE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDIMAXIMIZE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDINEXT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDIREFRESHMENU: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDIRESTORE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDISETMENU: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MDITILE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MEASUREITEM: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MENUCHAR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MENUCOMMAND: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MENUDRAG: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MENUGETOBJECT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MENURBUTTONUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MENUSELECT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MOUSEACTIVATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MOUSEHOVER: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MOUSELEAVE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MOUSEMOVE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MOUSEWHEEL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MOVE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_MOVING: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCACTIVATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCCALCSIZE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCCREATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCDESTROY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCHITTEST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCLBUTTONDBLCLK: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCLBUTTONDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCLBUTTONUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCMBUTTONDBLCLK: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCMBUTTONDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCMBUTTONUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCMOUSEMOVE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCPAINT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCRBUTTONDBLCLK: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCRBUTTONDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCRBUTTONUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCXBUTTONDBLCLK: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCXBUTTONDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NCXBUTTONUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NEXTDLGCTL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NEXTMENU: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NOTIFY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NOTIFYFORMAT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_NULL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PAINT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PAINTCLIPBOARD: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PAINTICON: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PALETTECHANGED: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PALETTEISCHANGING: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PARENTNOTIFY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PASTE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PENWINFIRST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PENWINLAST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_POWER: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PRINT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_PRINTCLIENT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_QUERYDRAGICON: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_QUERYENDSESSION: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_QUERYNEWPALETTE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_QUERYOPEN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_QUEUESYNC: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_QUIT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_RBUTTONDBLCLK: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_RBUTTONDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_RBUTTONUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_REFLECT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_RENDERALLFORMATS: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_RENDERFORMAT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SETCURSOR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SETFOCUS: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SETFONT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SETHOTKEY: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SETICON: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SETREDRAW: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SETTEXT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SETTINGCHANGE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SHOWWINDOW: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SIZE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SIZECLIPBOARD: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SIZING: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SPOOLERSTATUS: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_STYLECHANGED: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_STYLECHANGING: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SYNCPAINT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SYSCHAR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SYSCOLORCHANGE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SYSCOMMAND: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SYSDEADCHAR: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SYSKEYDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_SYSKEYUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_TCARD: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_THEME_CHANGED: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_TIMECHANGE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_TIMER: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_UNDO: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_UNINITMENUPOPUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_USER: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_USERCHANGED: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_VKEYTOITEM: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_VSCROLL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_VSCROLLCLIPBOARD: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_WINDOWPOSCHANGED: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_WINDOWPOSCHANGING: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_WININICHANGE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_XBUTTONDBLCLK: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_XBUTTONDOWN: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly
    WM_XBUTTONUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.Msg = (
        ...
    )  # static # readonly

class SWP_Flags(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    SWP_DRAWFRAME: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SWP_Flags = (
        ...
    )  # static # readonly
    SWP_FRAMECHANGED: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SWP_Flags
    ) = ...  # static # readonly
    SWP_HIDEWINDOW: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SWP_Flags = (
        ...
    )  # static # readonly
    SWP_NOACTIVATE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SWP_Flags = (
        ...
    )  # static # readonly
    SWP_NOMOVE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SWP_Flags = (
        ...
    )  # static # readonly
    SWP_NOOWNERZORDER: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SWP_Flags
    ) = ...  # static # readonly
    SWP_NOREPOSITION: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SWP_Flags
    ) = ...  # static # readonly
    SWP_NOSIZE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SWP_Flags = (
        ...
    )  # static # readonly
    SWP_NOZORDER: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SWP_Flags = (
        ...
    )  # static # readonly
    SWP_SHOWWINDOW: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SWP_Flags = (
        ...
    )  # static # readonly

class SetWindowPosFlags(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    SWP_ASYNCWINDOWPOS: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_DEFERERASE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_DRAWFRAME: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_FRAMECHANGED: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_HIDEWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_NOACTIVATE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_NOCOPYBITS: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_NOMOVE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_NOOWNERZORDER: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_NOREDRAW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_NOREPOSITION: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_NOSENDCHANGING: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_NOSIZE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_NOZORDER: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly
    SWP_SHOWWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.SetWindowPosFlags
    ) = ...  # static # readonly

class StaticControlStyles(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    SS_BITMAP: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_BLACKFRAME: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_BLACKRECT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_CENTER: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_CENTERIMAGE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_EDITCONTROL: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_ELLIPSISMASK: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_ENDELLIPSIS: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_ENHMETAFILE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_ETCHEDFRAME: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_ETCHEDHORZ: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_ETCHEDVERT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_GRAYFRAME: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_GRAYRECT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_ICON: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_LEFT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_LEFTNOWORDWRAP: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_NOPREFIX: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_NOTIFY: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_OWNERDRAW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_PATHELLIPSIS: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_REALSIZECONTROL: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_REALSIZEIMAGE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_RIGHT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_RIGHTJUST: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_SIMPLE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_SUNKEN: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_TYPEMASK: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_USERITEM: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_WHITEFRAME: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_WHITERECT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly
    SS_WORDELLIPSIS: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.StaticControlStyles
    ) = ...  # static # readonly

class WindowExStyles(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    WS_EX_ACCEPTFILES: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_APPWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_CLIENTEDGE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_CONTEXTHELP: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_CONTROLPARENT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_DLGMODALFRAME: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_LAYERED: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_LEFT: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles = (
        ...
    )  # static # readonly
    WS_EX_LEFTSCROLLBAR: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_LTRREADING: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_MDICHILD: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_NOPARENTNOTIFY: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_OVERLAPPEDWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_PALETTEWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_RIGHT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_RIGHTSCROLLBAR: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_RTLREADING: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_STATICEDGE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_TOOLWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_TOPMOST: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_TRANSPARENT: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly
    WS_EX_WINDOWEDGE: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowExStyles
    ) = ...  # static # readonly

class WindowStyles(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    WS_BORDER: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_CAPTION: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_CHILD: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_CHILDWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles
    ) = ...  # static # readonly
    WS_CLIPCHILDREN: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles
    ) = ...  # static # readonly
    WS_CLIPSIBLINGS: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles
    ) = ...  # static # readonly
    WS_DISABLED: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_DLGFRAME: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_GROUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_HSCROLL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_ICONIC: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_MAXIMIZE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_MAXIMIZEBOX: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles
    ) = ...  # static # readonly
    WS_MINIMIZE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_MINIMIZEBOX: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles
    ) = ...  # static # readonly
    WS_OVERLAPPED: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles
    ) = ...  # static # readonly
    WS_OVERLAPPEDWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles
    ) = ...  # static # readonly
    WS_POPUP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_POPUPWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles
    ) = ...  # static # readonly
    WS_SIZEBOX: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_SYSMENU: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_TABSTOP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_THICKFRAME: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles
    ) = ...  # static # readonly
    WS_TILED: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_TILEDWINDOW: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles
    ) = ...  # static # readonly
    WS_VISIBLE: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly
    WS_VSCROLL: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.WindowStyles = (
        ...
    )  # static # readonly

class ZOrderPos(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    HWND_BOTTOM: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ZOrderPos = (
        ...
    )  # static # readonly
    HWND_NOTOPMOST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ZOrderPos = (
        ...
    )  # static # readonly
    HWND_TOP: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ZOrderPos = (
        ...
    )  # static # readonly
    HWND_TOPMOST: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.OS.ZOrderPos = (
        ...
    )  # static # readonly
