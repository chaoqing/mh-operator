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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.QuantAnalysis.Properties

class Resources:  # Class
    AppName: str  # static # readonly
    CmdSwitchDesc_AccountName: str  # static # readonly
    CmdSwitchDesc_Application: str  # static # readonly
    CmdSwitchDesc_Batch: str  # static # readonly
    CmdSwitchDesc_ConnectionTicket: str  # static # readonly
    CmdSwitchDesc_DefineConstant: str  # static # readonly
    CmdSwitchDesc_Domain: str  # static # readonly
    CmdSwitchDesc_Help: str  # static # readonly
    CmdSwitchDesc_Instrument: str  # static # readonly
    CmdSwitchDesc_Password: str  # static # readonly
    CmdSwitchDesc_Script: str  # static # readonly
    CmdSwitchDesc_Server: str  # static # readonly
    CmdSwitchDesc_User: str  # static # readonly
    Culture: System.Globalization.CultureInfo  # static
    ErrMsg_BatchFileNotFound: str  # static # readonly
    ErrMsg_BatchFolderContainsMultipleBatchFiles: str  # static # readonly
    ErrMsg_BatchFolderNotContainsBatchFile: str  # static # readonly
    ErrMsg_ConfigurationError: str  # static # readonly
    ErrMsg_Error: str  # static # readonly
    ErrMsg_FailedToInitializeConfiguration: str  # static # readonly
    ErrMsg_FailedToInitializeLogFile: str  # static # readonly
    ErrMsg_InvalidApplicationType: str  # static # readonly
    ErrMsg_InvalidInstrumentType: str  # static # readonly
    ErrMsg_LogonNotRequired: str  # static # readonly
    ErrMsg_LogonRequired: str  # static # readonly
    ErrMsg_ScriptFileNotFound: str  # static # readonly
    ErrMsg_SpecifyUserNameAndPassword: str  # static # readonly
    ErrMsg_TrialLicenseError: str  # static # readonly
    ErrMsg_TrialLicenseExpired: str  # static # readonly
    ErrMsg_UnknownParameter: str  # static # readonly
    Label_AppFlavor: str  # static # readonly
    Label_Flavor: str  # static # readonly
    Label_OK: str  # static # readonly
    Label_TrialVersion: str  # static # readonly
    Label_TrialVersionExpires: str  # static # readonly
    Msg_AppLocked_EnterUserNameAndPassword: str  # static # readonly
    Msg_LoggingIn: str  # static # readonly
    QuantitativeAnalysisDeskTop: System.Drawing.Icon  # static # readonly
    ResourceManager: System.Resources.ResourceManager  # static # readonly
    Title_LoggingIn: str  # static # readonly
    Usage: str  # static # readonly
