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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.Quantitative.SecureFileSystem

class LsaUtility:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def SetRight(accountName: str, privilegeName: str) -> int: ...
    @staticmethod
    def FreeSid(pSid: System.IntPtr) -> None: ...

class PasswordUtility:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def EncryptPassword(password: str) -> str: ...
    @staticmethod
    def DecryptPassword(encrypted: str) -> System.Security.SecureString: ...

class SecureFolder:  # Class
    def __init__(self) -> None: ...

    CustomerHome: str  # static # readonly

    @staticmethod
    def GetSecureFolder(rootFolder: str) -> str: ...
    @staticmethod
    def GetUserFolder(rootFolder: str) -> str: ...
    @staticmethod
    def SetupFolders(userName: str, domainName: str, rootFolder: str) -> None: ...
    @staticmethod
    def GetCacheFolder(rootFolder: str) -> str: ...

class UserUtilities:  # Class
    def __init__(self) -> None: ...

    DefaultDomainName: str = ...  # static # readonly
    DefaultSecureUserName: str = ...  # static # readonly

    @staticmethod
    def SaveUserInfo(
        userName: str,
        domainName: str,
        password: System.Security.SecureString,
        file: str,
    ) -> None: ...
    @staticmethod
    def DecryptSecure(cipher: str) -> System.Security.SecureString: ...
    @staticmethod
    def Encrypt(value_: System.Security.SecureString) -> str: ...
    @staticmethod
    def CreateNewUser(
        userName: str, password: System.Security.SecureString, description: str
    ) -> None: ...
    @staticmethod
    def LoadUserInfo(
        file: str,
        userName: str,
        domainName: str,
        password: System.Security.SecureString,
    ) -> None: ...
    @staticmethod
    def GetUserFileInfoPath(rootFolder: str) -> str: ...
    @staticmethod
    def GenerateNewPassword(
        minLength: int,
        minUppercase: int,
        minLowercase: int,
        minDigits: int,
        minNonAlphanumeric: int,
    ) -> System.Security.SecureString: ...
