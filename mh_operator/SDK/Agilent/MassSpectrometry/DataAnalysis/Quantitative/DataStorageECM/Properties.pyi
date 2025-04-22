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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.DataStorageECM.Properties

class Resources:  # Class
    Culture: System.Globalization.CultureInfo  # static
    Exp_AnalysisNotExist: str  # static # readonly
    Exp_BatchFileIsAlreadyLocked: str  # static # readonly
    Exp_BatchFileNotFoundInZip: str  # static # readonly
    Exp_BatchNotExist: str  # static # readonly
    Exp_CannotCreateBatchInThisFolderLevel: str  # static # readonly
    Exp_CannotReadBatchInformation: str  # static # readonly
    Exp_FailedToLogonAsSecureUser: str  # static # readonly
    Exp_FailedToOpenZipFileMayBeCorrupt: str  # static # readonly
    Exp_FileAlreadyCheckedOut: str  # static # readonly
    Exp_FileAlreadyExists: str  # static # readonly
    Exp_FileNotExist: str  # static # readonly
    Exp_InvalidToken: str  # static # readonly
    Exp_LocalFileNotExist: str  # static # readonly
    Exp_LogonFailed: str  # static # readonly
    Exp_LogonFailedRequiredInformationMissing: str  # static # readonly
    Exp_ParameterNotSpecified: str  # static # readonly
    Exp_Permission: str  # static # readonly
    Exp_ReasonRequired: str  # static # readonly
    Exp_RevisionNotExist: str  # static # readonly
    Exp_UserInfoNotMatch: str  # static # readonly
    Exp_ValidUserNameAndPasswordRequired: str  # static # readonly
    FileType_AllFiles: str  # static # readonly
    FileType_BatchFiles: str  # static # readonly
    FileType_LibraryFiles: str  # static # readonly
    FileType_MethodFiles: str  # static # readonly
    FileType_SampleFiles: str  # static # readonly
    FileType_UnknownsAnalysisFiles: str  # static # readonly
    LogonInfo: str  # static # readonly
    Msg_CannotReadZipFile: str  # static # readonly
    Msg_LoggingInPleaseWait: str  # static # readonly
    Msg_PleaseLoginECM: str  # static # readonly
    Progress_Converting: str  # static # readonly
    Progress_Downloading: str  # static # readonly
    Progress_ExtractingFiles: str  # static # readonly
    Prompt_Reset: str  # static # readonly
    ResourceManager: System.Resources.ResourceManager  # static # readonly
    Title_ATMConfiguration: str  # static # readonly
    Title_Login: str  # static # readonly
    Title_NewBatch: str  # static # readonly
    Title_NewUnknownsFile: str  # static # readonly
    Title_OpenBatch: str  # static # readonly
    Title_OpenUnknownsFile: str  # static # readonly
    Title_SaveBatchAs: str  # static # readonly
    Title_SaveUnknownsFileAs: str  # static # readonly
