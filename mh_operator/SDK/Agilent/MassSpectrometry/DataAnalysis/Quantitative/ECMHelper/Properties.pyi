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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.ECMHelper.Properties

class Resources:  # Class
    BatchFileBin: System.Drawing.Bitmap  # static # readonly
    ButtonLabel_Close: str  # static # readonly
    ButtonLabel_Verify: str  # static # readonly
    ButtonOk_New: str  # static # readonly
    ButtonOk_Open: str  # static # readonly
    ButtonOk_Save: str  # static # readonly
    Checkout: System.Drawing.Bitmap  # static # readonly
    CheckoutByme: System.Drawing.Bitmap  # static # readonly
    Culture: System.Globalization.CultureInfo  # static
    Err_CannotLogin: str  # static # readonly
    Err_CannotValidateUser: str  # static # readonly
    Exp_BatchFileNotFoundInZip: str  # static # readonly
    Exp_CannotFindPDFPrintConfiguration: str  # static # readonly
    Exp_CannotReadBatchInformation: str  # static # readonly
    Exp_ExtractElement: str  # static # readonly
    Exp_FolderNotExist: str  # static # readonly
    File: System.Drawing.Bitmap  # static # readonly
    Folder_6222: System.Drawing.Icon  # static # readonly
    Method: System.Drawing.Bitmap  # static # readonly
    Msg_FailedToCheckout: str  # static # readonly
    Msg_FailedToUndoCheckout: str  # static # readonly
    Msg_FileAlreadyCheckedout: str  # static # readonly
    Msg_FileAlreadyExists: str  # static # readonly
    Msg_FileAlreadyExistsReplace: str  # static # readonly
    Msg_FileNotFoundCheck: str  # static # readonly
    Msg_LoggingIn: str  # static # readonly
    Msg_NoPrivilegeToCheckout: str  # static # readonly
    Msg_NoPrivilegeToReadFolders: str  # static # readonly
    Msg_NoPrivilegeToUndoCheckout: str  # static # readonly
    ResourceManager: System.Resources.ResourceManager  # static # readonly
    Sample: System.Drawing.Icon  # static # readonly
    Title_NewFile: str  # static # readonly
    Title_OpenFile: str  # static # readonly
    Title_SaveFileAs: str  # static # readonly
    Title_ValidateUser: str  # static # readonly
    UnknownsFile: System.Drawing.Bitmap  # static # readonly
