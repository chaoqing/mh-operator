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

from .DataAccess import (
    LibraryAccessBase,
    LibraryAccessReportSearch,
    SearchConditions,
    SuggestedConversionType,
)
from .Utils import CompoundKey, SpectrumKey

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands

class AppContext(
    Agilent.MassSpectrometry.CommandModel.Model.ICommandHistory, System.IDisposable
):  # Class
    def __init__(
        self,
        compliance: Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance,
    ) -> None: ...

    Compliance: (
        Agilent.MassSpectrometry.DataAnalysis.Quantitative.Compliance.ICompliance
    )  # readonly
    Format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat  # readonly
    IsCommandRunning: bool  # readonly
    IsDirty: bool  # readonly
    IsOpen: bool  # readonly
    IsReadOnly: bool  # readonly
    IsScriptRunning: bool  # readonly
    LibraryAccess: LibraryAccessBase  # readonly
    LibraryName: str  # readonly
    LockObject: Any  # readonly

    def Search(
        self,
        conditions: SearchConditions,
        reportSearch: LibraryAccessReportSearch,
        abort: System.Threading.WaitHandle,
    ) -> None: ...
    def CreateLibrary(
        self, path: str, format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat
    ) -> None: ...
    def ConvertLibrary(
        self,
        infoType: Agilent.MassSpectrometry.DataAnalysis.LibraryRTInfoType,
        destination: str,
    ) -> None: ...
    def CloseLibrary(self) -> None: ...
    def ClearSearch(self) -> None: ...
    def SaveAs(
        self,
        library: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        conversion: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.ConversionType,
    ) -> None: ...
    def Dispose(self) -> None: ...
    def OpenLibrary(
        self,
        path: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        revisionNumber: str,
        readOnly: bool,
    ) -> None: ...
    def RunScript(
        self,
        script: System.IO.TextReader,
        customStub: System.MarshalByRefObject,
        debug: bool,
        language: str,
        referenceAssemblies: List[str],
        imports: List[str],
    ) -> None: ...
    def Save(self) -> None: ...

    CommandEnd: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandEventArgs
    ]  # Event
    CommandStart: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandEventArgs
    ]  # Event
    CompoundCountChanged: System.EventHandler  # Event
    CompoundPropertiesChanged: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CompoundPropertiesChangedEventArgs
    ]  # Event
    ConversionSuggested: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.ConversionSuggestedEventArgs
    ]  # Event
    LibraryClosed: System.EventHandler  # Event
    LibraryClosing: System.EventHandler  # Event
    LibraryCreated: System.EventHandler  # Event
    LibraryCreating: System.EventHandler  # Event
    LibraryOpened: System.EventHandler  # Event
    LibraryOpening: System.EventHandler  # Event
    LibraryPropertiesChanged: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.LibraryPropertiesChangedEventArgs
    ]  # Event
    SpectrumCountChanged: System.EventHandler  # Event
    SpectrumPropertiesChanged: System.EventHandler[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.SpectrumPropertiesChangedEventArgs
    ]  # Event

class CalcMonoisotopicMass(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        compounds: List[CompoundKey],
        species: str,
        replace: bool,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class CloseLibrary(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
    ) -> None: ...

    IsDirtyCommand: bool  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class CommandBase(
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
    Agilent.MassSpectrometry.CommandModel.CommandBase,
):  # Class
    Context: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext
    )  # readonly
    IsDirtyCommand: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

class CommandEventArgs(System.EventArgs):  # Class
    def __init__(
        self,
        command: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
        ex: System.Exception,
    ) -> None: ...

    Command: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase
    )  # readonly
    Exception: System.Exception  # readonly

class CommandException(
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
    System.Exception,
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, message: str) -> None: ...
    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None: ...

class CompoundPropertiesChangedEventArgs(System.EventArgs):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        properties: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CompoundProperty
        ],
    ) -> None: ...

    Properties: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CompoundProperty
    ]  # readonly

class CompoundProperty(System.MarshalByRefObject):  # Class
    def __init__(self, compoundId: int, name: str, value_: Any) -> None: ...

    CompoundId: int  # readonly
    Name: str  # readonly
    OldValue: Any  # readonly
    Value: Any

class ConversionSuggestedEventArgs(System.EventArgs):  # Class
    def __init__(self, type: SuggestedConversionType) -> None: ...

    ConversionType: SuggestedConversionType  # readonly

class ConversionType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    RI: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.ConversionType = (
        ...
    )  # static # readonly
    RTL: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.ConversionType = (
        ...
    )  # static # readonly
    RTLandRI: (
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.ConversionType
    ) = ...  # static # readonly

class ConvertLibrary(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        infoType: Agilent.MassSpectrometry.DataAnalysis.LibraryRTInfoType,
        destination: str,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class CreateLibrary(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        path: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
    ) -> None: ...

    IsDirtyCommand: bool  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class Delete(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        compounds: List[CompoundKey],
        compoundProperties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CompoundProperty
        ],
        spectra: List[SpectrumKey],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        compounds: List[CompoundKey],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        compoundProperties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CompoundProperty
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        spectra: List[SpectrumKey],
    ) -> None: ...

    Reversible: bool  # readonly

    def DeleteSpectrum(self, key: SpectrumKey) -> None: ...
    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def DeleteCompound(self, key: CompoundKey) -> None: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def DeleteCompoundProperty(self, key: CompoundKey, property: str) -> None: ...

class FilterSpectrumPeaks(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        spectrumKeys: List[SpectrumKey],
        relativeHeight: Optional[float],
        largestPeaks: Optional[int],
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class ImportJCAMP(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        files: List[str],
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class LibraryPropertiesChangedEventArgs(System.EventArgs):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        properties: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.LibraryProperty
        ],
    ) -> None: ...

    Properties: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.LibraryProperty
    ]  # readonly

class LibraryProperty:  # Class
    def __init__(self, name: str, value_: Any) -> None: ...

    Name: str  # readonly
    OldValue: Any  # readonly
    Value: Any

class NewCompound(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        properties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CompoundProperty
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
    ) -> None: ...

    CompoundId: int  # readonly
    Reversible: bool  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, name: str, value_: Any) -> None: ...

class NewSpectrum(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        compoundId: int,
        properties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.SpectrumProperty
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        compoundId: int,
    ) -> None: ...

    Reversible: bool  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(self, name: str, value_: Any) -> None: ...

class OpenLibrary(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        path: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        readOnly: bool,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        path: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        revisionNumber: str,
        readOnly: bool,
    ) -> None: ...

    IsDirtyCommand: bool  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class Paste(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        compoundProperties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CompoundProperty
        ],
        newCompounds: List[CompoundKey],
        spectrumProperties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.SpectrumProperty
        ],
        newSpectra: List[SpectrumKey],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
    ) -> None: ...

    Reversible: bool  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def SetSpectrumProperties(
        self,
        properties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.SpectrumProperty
        ],
    ) -> None: ...
    def NewSpectrum(
        self,
        compoundId: int,
        spectrumId: int,
        properties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.SpectrumProperty
        ],
    ) -> None: ...
    def SetCompoundProperty(self, compoundId: int, name: str, value_: Any) -> None: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def NewCompound(
        self,
        properties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CompoundProperty
        ],
    ) -> int: ...

class RedoCommand(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
    ) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SaveLibrary(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
    ) -> None: ...

    IsDirtyCommand: bool  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SaveLibraryAs(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        path: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
        conversion: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.ConversionType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        path: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MSLibraryFormat,
    ) -> None: ...

    IsDirtyCommand: bool  # readonly
    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetCompoundProperty(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        properties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CompoundProperty
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        compoundId: int,
        name: str,
        value_: Any,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetLibraryProperty(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        properties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.LibraryProperty
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def Redo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class SetSpectrumProperty(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        properties: List[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.SpectrumProperty
        ],
    ) -> None: ...
    @overload
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        compoundId: int,
        spectrumId: int,
        name: str,
        value_: Any,
    ) -> None: ...

    Reversible: bool  # readonly

    def Redo(self) -> Any: ...
    def Undo(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Do(self) -> Any: ...
    def SetProperty(
        self, compoundId: int, spectrumId: int, name: str, value_: Any
    ) -> None: ...

class SpectrumPropertiesChangedEventArgs(System.EventArgs):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self,
        properties: Iterable[
            Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.SpectrumProperty
        ],
    ) -> None: ...

    Properties: Iterable[
        Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.SpectrumProperty
    ]  # readonly

class SpectrumProperty(System.MarshalByRefObject):  # Class
    def __init__(
        self, compoundId: int, spectrumId: int, name: str, value_: Any
    ) -> None: ...

    CompoundId: int  # readonly
    Name: str  # readonly
    OldValue: Any  # readonly
    SpectrumId: int  # readonly
    Value: Any

class SynthesizeSpectra(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
        compounds: List[CompoundKey],
        replace: bool,
        species: List[str],
    ) -> None: ...

    Reversible: bool  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...

class UndoCommand(
    Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.CommandBase,
    System.IDisposable,
    Agilent.MassSpectrometry.CommandModel.Model.ICommand,
):  # Class
    def __init__(
        self,
        context: Agilent.MassSpectrometry.DataAnalysis.LibraryEdit.Commands.AppContext,
    ) -> None: ...

    Reversible: bool  # readonly
    Type: Agilent.MassSpectrometry.CommandModel.Model.CommandType  # readonly

    def Do(self) -> Any: ...
    def GetParameters(self) -> List[Any]: ...
    def Undo(self) -> Any: ...
