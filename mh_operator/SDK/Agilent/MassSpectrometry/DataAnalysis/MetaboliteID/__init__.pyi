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

from . import OS, Controls, GlycanStructure

# Discovered Generic TypeVars:
TItem = TypeVar("TItem")
from . import IAtom, IBond, IMolecularStructure, Molecule
from .Controls import OpenFileDialogEx

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID

class Atom(
    IAtom, System.IEquatable[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom]
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, orig: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom
    ) -> None: ...

    Alias: str
    AtomMappingNumber: int
    Attributes: Dict[
        str, Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomAttribute
    ]  # readonly
    Charge: int
    ChargeValue: int
    Coords: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomLocation
    ExactChangeFlag: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ExactChangeOption
    )
    HODesignator: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.HODesignatorOption
    HydrogenCount: int
    Index: int
    InversionFlag: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.InversionOption
    IsotopeMass: int
    MassDifference: int
    Radical: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Radical
    StereoCareBox: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StereoCareBoxOption
    )
    StereoParity: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StereoParityType
    Symbol: str
    Valence: int

    def Equals(
        self, other: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom
    ) -> bool: ...
    def ToString(self) -> str: ...
    def Clone(self) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom: ...

class AtomAttribute:  # Class
    @overload
    def __init__(
        self, orig: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomAttribute
    ) -> None: ...
    @overload
    def __init__(self, stringValue: str) -> None: ...
    @overload
    def __init__(self, intValue: int) -> None: ...
    @overload
    def __init__(self, doubleValue: float) -> None: ...
    @overload
    def __init__(self, objectValue: Any) -> None: ...

    DoubleValue: float
    IntValue: int
    ObjectValue: Any
    StringValue: str

    def Clone(
        self,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomAttribute: ...

class AtomCollection(
    Sequence[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom],
    System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom
    ],
    List[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom],
    Iterable[Any],
    Sequence[Any],
    Iterable[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom],
    List[Any],
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, source: Iterable[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom]
    ) -> None: ...

    Center: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomLocation  # readonly

    def GetIndexForAtom(
        self, atom: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom
    ) -> int: ...

class AtomHighlightSet:  # Class
    def __init__(
        self,
        atoms: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomCollection,
        color: System.Drawing.Color,
    ) -> None: ...

    AtomCollection: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomCollection
    )  # readonly
    Color: System.Drawing.Color  # readonly

class AtomHighlightSets(
    Sequence[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomHighlightSet],
    List[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomHighlightSet],
    System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomHighlightSet
    ],
    Iterable[Any],
    Iterable[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomHighlightSet],
    Sequence[Any],
    List[Any],
):  # Class
    def __init__(self) -> None: ...
    def GetAtomColor(
        self,
        atom: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom,
        backgroundColor: System.Drawing.Color,
    ) -> System.Drawing.Color: ...

class AtomLocation:  # Class
    def __init__(self) -> None: ...

    X: float
    Y: float
    Z: float

class AtomTreeNode(
    System.IEquatable[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom],
    IAtom,
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom,
):  # Class
    def __init__(
        self, atom: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom
    ) -> None: ...
    def EnumSubTrees(
        self,
        listener: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.SubTreeListenerDelegate,
    ) -> None: ...
    @overload
    def AddChild(
        self, atom: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Atom
    ) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode: ...
    @overload
    def AddChild(
        self, atomNode: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode
    ) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode: ...

class AtomTreeNodeCollection(
    System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode
    ],
    Iterable[Any],
    List[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode],
    Sequence[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode],
    Iterable[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode],
    List[Any],
    Sequence[Any],
):  # Class
    def __init__(self) -> None: ...

class AtomTreeNodeSet(
    Iterable[Any],
    Iterable[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode],
    Sequence[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode],
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Set[
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode
    ],
):  # Class
    def __init__(self) -> None: ...

class Bond(
    IBond, System.IEquatable[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Bond]
):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, orig: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Bond
    ) -> None: ...
    @overload
    def __init__(self, indexAtom1: int, indexAtom2: int) -> None: ...

    IndexAtom1: int
    IndexAtom2: int
    Order: int  # readonly
    ReactingCenterStatus: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    )
    Stereo: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondStereo
    Topology: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondTopology
    Type: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondType

    def Equals(
        self, other: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Bond
    ) -> bool: ...
    def ToString(self) -> str: ...
    def Clone(self) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Bond: ...

class BondCollection(
    System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Bond
    ],
    List[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Bond],
    Iterable[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Bond],
    Iterable[Any],
    Sequence[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Bond],
    Sequence[Any],
    List[Any],
):  # Class
    def __init__(self) -> None: ...

class BondHighlightSet:  # Class
    def __init__(
        self,
        bonds: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondCollection,
        color: System.Drawing.Color,
    ) -> None: ...

    BondCollection: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondCollection
    )  # readonly
    Color: System.Drawing.Color  # readonly

class BondHighlightSets(
    Iterable[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondHighlightSet],
    List[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondHighlightSet],
    System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondHighlightSet
    ],
    Iterable[Any],
    Sequence[Any],
    Sequence[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondHighlightSet],
    List[Any],
):  # Class
    def __init__(self) -> None: ...
    def GetBondColor(
        self, bond: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Bond
    ) -> System.Drawing.Color: ...

class BondStereo(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    CisOrTrans: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondStereo = (
        ...
    )  # static # readonly
    Down: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondStereo = (
        ...
    )  # static # readonly
    Either: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondStereo = (
        ...
    )  # static # readonly
    NotStereo: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondStereo = (
        ...
    )  # static # readonly
    Up: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondStereo = (
        ...
    )  # static # readonly

class BondTopology(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Chain: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondTopology = (
        ...
    )  # static # readonly
    Either: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondTopology = (
        ...
    )  # static # readonly
    Ring: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondTopology = (
        ...
    )  # static # readonly

class BondType(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Any: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondType = (
        ...
    )  # static # readonly
    Aromatic: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondType = (
        ...
    )  # static # readonly
    Double: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondType = (
        ...
    )  # static # readonly
    DoubleOrAromatic: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondType = (
        ...
    )  # static # readonly
    Single: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondType = (
        ...
    )  # static # readonly
    SingleOrAromatic: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondType = (
        ...
    )  # static # readonly
    SingleOrDouble: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondType = (
        ...
    )  # static # readonly
    Triple: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.BondType = (
        ...
    )  # static # readonly

class ExactChangeOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    MustMatch: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ExactChangeOption = (
        ...
    )  # static # readonly
    NotApplied: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ExactChangeOption = (
        ...
    )  # static # readonly

class HODesignatorOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    NoHAtomsAllowed: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.HODesignatorOption
    ) = ...  # static # readonly
    NotSpecified: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.HODesignatorOption
    ) = ...  # static # readonly

class InversionOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Inverted: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.InversionOption = (
        ...
    )  # static # readonly
    NotApplied: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.InversionOption = (
        ...
    )  # static # readonly
    Retained: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.InversionOption = (
        ...
    )  # static # readonly

class MolFileReader:  # Class
    GlycoCTGlycanExtension: str = ...  # static # readonly
    KeggGlycanExtension: str = ...  # static # readonly
    LinucsGlycanExtension: str = ...  # static # readonly
    MOLExtension: str = ...  # static # readonly

    @staticmethod
    def ReadFromFile(
        path: str,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure: ...
    @overload
    @staticmethod
    def ReadFromStream(
        sr: System.IO.TextReader,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure: ...
    @overload
    @staticmethod
    def ReadFromStream(
        sr: System.IO.StreamReader,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure: ...

class MolFileWriter:  # Class
    @overload
    @staticmethod
    def WriteToStream(
        stream: System.IO.Stream,
        structure: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure,
    ) -> None: ...
    @overload
    @staticmethod
    def WriteToStream(
        writer: System.IO.TextWriter,
        structure: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure,
    ) -> None: ...
    @staticmethod
    def WriteToFile(
        path: str,
        structure: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure,
    ) -> None: ...

class MolecularStructure(IMolecularStructure):  # Class
    Comment: str  # readonly
    DateAndTime: System.DateTime  # readonly
    DimCode: str  # readonly
    Energy: float  # readonly
    ExtendedProperties: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StructurePropertyDictionary
    )  # readonly
    HasCharge: bool  # readonly
    IsValid: bool
    Molecule: Molecule  # readonly
    Name: str  # readonly
    ProgramName: str  # readonly
    RegistryNumber: int  # readonly
    ScalingFactor1: int  # readonly
    ScalingFactor2: float  # readonly
    TotalCharge: int  # readonly
    UserInitials: str  # readonly

    def ExportToFile(
        self,
        initialDirectory: str,
        proposedName: str,
        owner: System.Windows.Forms.IWin32Window,
    ) -> bool: ...

class MolecularStructureViewer(
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

    BackColorEmpty: System.Drawing.Color
    FontScalingFactor: float
    LateralOffsetCutoffLength: float
    MaxFontSize: float
    MinFontSize: float
    ShowHAtoms: bool
    Structure: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure

    def CopyToClipboard(self) -> None: ...
    def CopyToClipboardAdvanced(self) -> None: ...
    def DrawStructure(self, graphics: System.Drawing.Graphics) -> None: ...

class Radical(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    Doublet: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Radical = (
        ...
    )  # static # readonly
    NoRadical: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Radical = (
        ...
    )  # static # readonly
    Singlet: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Radical = (
        ...
    )  # static # readonly
    Triplet: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Radical = (
        ...
    )  # static # readonly

class ReactingCenterStatusOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    BondMadeOrBroken: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    ) = ...  # static # readonly
    BondMadeOrBrokenChanged: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    ) = ...  # static # readonly
    BondOrderChange: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    ) = ...  # static # readonly
    Center: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    ) = ...  # static # readonly
    CenterOrBondMadeOrBroken: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    ) = ...  # static # readonly
    CenterOrBondMadeOrBrokenChanged: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    ) = ...  # static # readonly
    CenterOrBondOrderChange: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    ) = ...  # static # readonly
    NoChange: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    ) = ...  # static # readonly
    NotACenter: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    ) = ...  # static # readonly
    Unmarked: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.ReactingCenterStatusOption
    ) = ...  # static # readonly

class SDFFileReader:  # Class
    SDFExtension: str = ...  # static # readonly

    @overload
    @staticmethod
    def ReadFromFile(
        path: str,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure
    ]: ...
    @overload
    @staticmethod
    def ReadFromFile(
        path: str, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure: ...
    @overload
    @staticmethod
    def ReadFromStream(
        sr: System.IO.TextReader,
    ) -> List[
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure
    ]: ...
    @overload
    @staticmethod
    def ReadFromStream(
        sr: System.IO.StreamReader, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure: ...

class SDFFileWriter:  # Class
    @overload
    @staticmethod
    def WriteToStream(
        stream: System.IO.Stream,
        structures: List[
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure
        ],
    ) -> None: ...
    @overload
    @staticmethod
    def WriteToStream(
        writer: System.IO.TextWriter,
        structures: List[
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure
        ],
    ) -> None: ...
    @overload
    @staticmethod
    def WriteToStream(
        stream: System.IO.Stream,
        structures: List[
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure
        ],
        indices: List[int],
    ) -> None: ...
    @overload
    @staticmethod
    def WriteToStream(
        writer: System.IO.TextWriter,
        structures: List[
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure
        ],
        indices: List[int],
    ) -> None: ...
    @overload
    @staticmethod
    def WriteToFile(
        path: str,
        structures: List[
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure
        ],
    ) -> None: ...
    @overload
    @staticmethod
    def WriteToFile(
        path: str,
        structures: List[
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.MolecularStructure
        ],
        indices: List[int],
    ) -> None: ...

class Set(Generic[TItem], Iterable[Any], Iterable[TItem], Sequence[TItem]):  # Class
    def __init__(self) -> None: ...

    Count: int  # readonly
    IsReadOnly: bool  # readonly

    def AsReadOnly(self) -> Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.Set: ...
    def Contains(self, item: TItem) -> bool: ...
    def CopyTo(self, array: List[TItem], arrayIndex: int) -> None: ...
    def GetEnumerator(self) -> Iterator[TItem]: ...
    def Add(self, item: TItem) -> None: ...
    def Clear(self) -> None: ...
    def Remove(self, item: TItem) -> bool: ...

class StereoCareBoxOption(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Ignore: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StereoCareBoxOption = (
        ...
    )  # static # readonly
    MustMatch: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StereoCareBoxOption
    ) = ...  # static # readonly

class StereoParityType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Even: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StereoParityType = (
        ...
    )  # static # readonly
    NotStereo: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StereoParityType = (
        ...
    )  # static # readonly
    Odd: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StereoParityType = (
        ...
    )  # static # readonly
    Unmarked: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StereoParityType = (
        ...
    )  # static # readonly

class StructureFieldInfo:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, fieldName: str) -> None: ...

    ExternalRegistry: str
    InternalRegistry: str
    Name: str
    Number: int

    def GetHashCode(self) -> int: ...
    def Equals(self, obj: Any) -> bool: ...

class StructureOpenFileDialog(
    System.Windows.Forms.UnsafeNativeMethods.IOleInPlaceObject,
    System.Windows.Forms.IWin32Window,
    System.Windows.Forms.Layout.IArrangedElement,
    System.Windows.Forms.UnsafeNativeMethods.IPersistStreamInit,
    System.Windows.Forms.ISupportOleDropSource,
    System.Windows.Forms.IBindableComponent,
    System.Windows.Forms.IDropTarget,
    OpenFileDialogEx,
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
    System.Windows.Forms.UnsafeNativeMethods.IOleControl,
):  # Class
    def __init__(self) -> None: ...

    StructureIndex: int  # readonly

    def OnFileNameChanged(self, filePath: str) -> None: ...
    def OnClosingDialog(self) -> None: ...
    def OnFolderNameChanged(self, folderName: str) -> None: ...

class StructurePropertyDictionary(
    Mapping[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StructureFieldInfo, str],
    Iterable[Any],
    Dict[Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StructureFieldInfo, str],
    System.Runtime.Serialization.IDeserializationCallback,
    Sequence[Any],
    System.Runtime.Serialization.ISerializable,
    Dict[Any, Any],
    Sequence[
        System.Collections.Generic.KeyValuePair[
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StructureFieldInfo, str
        ]
    ],
    Iterable[
        System.Collections.Generic.KeyValuePair[
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.StructureFieldInfo, str
        ]
    ],
):  # Class
    def __init__(self) -> None: ...
    def __getitem__(self, fieldname: str) -> str: ...

class SubTreeListenerDelegate(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        root: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode,
        leaves: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNodeSet,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        root: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNode,
        leaves: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.AtomTreeNodeSet,
    ) -> None: ...
