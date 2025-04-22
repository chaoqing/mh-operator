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

# Stubs for namespace: Agilent.MassSpectrometry.Acquisition

class DevicesConstants:  # Class
    Delay: str = ...  # static # readonly
    DeviceID: str = ...  # static # readonly
    DeviceName: str = ...  # static # readonly
    DeviceType: str = ...  # static # readonly
    DisplayName: str = ...  # static # readonly
    DriverVersion: str = ...  # static # readonly
    FirmwareVersion: str = ...  # static # readonly
    ModelNumber: str = ...  # static # readonly
    OrdinalNumber: str = ...  # static # readonly
    SerialNumber: str = ...  # static # readonly
    StoredDataType: str = ...  # static # readonly
    VendorID: str = ...  # static # readonly

class DevicesManager:  # Class
    def __init__(self) -> None: ...
    def Write(self) -> None: ...
    def GetDeviceID(self, Name: str, OrdinalNumber: int) -> int: ...
    def Init(self, acqDataPath: str) -> None: ...
    def Close(self) -> None: ...
    @overload
    def AddDevice(
        self,
        Name: str,
        ModelNumber: str,
        OrdinalNumber: int,
        SerialNumber: str,
        Type: int,
        StoredDataType: int,
        Delay: float,
        VendorId: int,
        DriverVersion: str,
        FirmwareVersion: str,
    ) -> None: ...
    @overload
    def AddDevice(
        self,
        Name: str,
        ModelNumber: str,
        OrdinalNumber: int,
        SerialNumber: str,
        Type: int,
        StoredDataType: int,
        Delay: float,
        VendorId: int,
    ) -> None: ...

class ILCDataWriter(object):  # Interface
    def SetFirmwareVersion(self, FirmwareVersion: str) -> None: ...
    def Open(self, DataFileName: str) -> None: ...
    def AddSignal(
        self,
        Name: str,
        Description: str,
        XStart: float,
        XDelta: float,
        YAxisLabel: str,
        YArray: List[float],
    ) -> None: ...
    def EndRCSpectraDevice(self) -> None: ...
    def EndDevice(self) -> None: ...
    def SetDriverVersion(self, DriverVersion: str) -> None: ...
    def StartRCDevice(
        self, DeviceName: str, ModelNumber: str, OrdinalNumber: int, SerialNumber: str
    ) -> None: ...
    def Close(self) -> None: ...
    def EndRCDevice(self) -> None: ...
    def AddSpectrum(
        self, ScanTime: float, SamplingPeriod: float, XStart: float, YArray: List[float]
    ) -> None: ...
    def AddChromatogram(
        self,
        Name: str,
        Description: str,
        XStart: float,
        XDelta: float,
        YAxisLabel: str,
        YArray: List[float],
    ) -> None: ...
    def SetDeviceVendor(self, Vendor: int) -> None: ...
    def StartDevice(
        self,
        DeviceName: str,
        ModelNumber: str,
        OrdinalNumber: int,
        SerialNumber: str,
        DeviceTypeID: int,
    ) -> None: ...

class LCDataWriter(Agilent.MassSpectrometry.Acquisition.ILCDataWriter):  # Class
    def __init__(self) -> None: ...
