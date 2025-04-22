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

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.MFS

class AdductIon(Agilent.MassSpectrometry.DataAnalysis.MFS.IAdductIon):  # Class
    AdductType: Agilent.MassSpectrometry.DataAnalysis.MFS.AdductType  # readonly
    Formula: str  # readonly
    Mass: float  # readonly

    @overload
    @staticmethod
    def CreateInstance(
        isotope: Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.IAdductIon: ...
    @overload
    @staticmethod
    def CreateInstance(
        molecularFormula: Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.IAdductIon: ...
    def ToString(self) -> str: ...
    @staticmethod
    def GetAdductByType(
        adductType: Agilent.MassSpectrometry.DataAnalysis.MFS.AdductType,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.IAdductIon: ...

class AdductType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    H: Agilent.MassSpectrometry.DataAnalysis.MFS.AdductType = ...  # static # readonly
    K: Agilent.MassSpectrometry.DataAnalysis.MFS.AdductType = ...  # static # readonly
    NH4: Agilent.MassSpectrometry.DataAnalysis.MFS.AdductType = ...  # static # readonly
    Na: Agilent.MassSpectrometry.DataAnalysis.MFS.AdductType = ...  # static # readonly

class AssayColumnsType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eAssayColumns_Complete: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.AssayColumnsType
    ) = ...  # static # readonly
    eAssayColumns_Concise: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.AssayColumnsType
    ) = ...  # static # readonly
    eAssayColumns_TIDs: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayColumnsType = (
        ...
    )  # static # readonly

class AssayDescriptionType:  # Class
    def __init__(self) -> None: ...

    CIDCountActive: int
    CIDCountActiveSpecified: bool
    CIDCountAll: int
    CIDCountAllSpecified: bool
    CIDCountInactive: int
    CIDCountInactiveSpecified: bool
    CIDCountInconclusive: int
    CIDCountInconclusiveSpecified: bool
    CIDCountProbe: int
    CIDCountProbeSpecified: bool
    CIDCountUnspecified: int
    CIDCountUnspecifiedSpecified: bool
    Comment: List[str]
    Description: List[str]
    HasScore: bool
    LastDataChange: int
    LastDataChangeSpecified: bool
    Method: str
    Name: str
    NumberOfTIDs: int
    Protocol: List[str]
    Revision: int
    RevisionSpecified: bool
    SIDCountActive: int
    SIDCountActiveSpecified: bool
    SIDCountAll: int
    SIDCountAllSpecified: bool
    SIDCountInactive: int
    SIDCountInactiveSpecified: bool
    SIDCountInconclusive: int
    SIDCountInconclusiveSpecified: bool
    SIDCountProbe: int
    SIDCountProbeSpecified: bool
    SIDCountUnspecified: int
    SIDCountUnspecifiedSpecified: bool
    Targets: List[Agilent.MassSpectrometry.DataAnalysis.MFS.AssayTargetType]
    Version: int
    VersionSpecified: bool

class AssayDownloadCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class AssayDownloadCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayDownloadCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayDownloadCompletedEventArgs,
    ) -> None: ...

class AssayFormatType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eAssayFormat_ASN_Binary: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.AssayFormatType
    ) = ...  # static # readonly
    eAssayFormat_ASN_Text: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayFormatType = (
        ...
    )  # static # readonly
    eAssayFormat_CSV: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayFormatType = (
        ...
    )  # static # readonly
    eAssayFormat_XML: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayFormatType = (
        ...
    )  # static # readonly

class AssayOutcomeFilterType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eAssayOutcome_Active: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.AssayOutcomeFilterType
    ) = ...  # static # readonly
    eAssayOutcome_All: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.AssayOutcomeFilterType
    ) = ...  # static # readonly
    eAssayOutcome_Inactive: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.AssayOutcomeFilterType
    ) = ...  # static # readonly
    eAssayOutcome_Inconclusive: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.AssayOutcomeFilterType
    ) = ...  # static # readonly
    eAssayOutcome_Unspecified: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.AssayOutcomeFilterType
    ) = ...  # static # readonly

class AssayTargetType:  # Class
    def __init__(self) -> None: ...

    Name: str
    gi: int

class BlobFormatType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eBlobFormat_ASNB: Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType = (
        ...
    )  # static # readonly
    eBlobFormat_ASNT: Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType = (
        ...
    )  # static # readonly
    eBlobFormat_CSV: Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType = (
        ...
    )  # static # readonly
    eBlobFormat_HTML: Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType = (
        ...
    )  # static # readonly
    eBlobFormat_Other: Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType = (
        ...
    )  # static # readonly
    eBlobFormat_PNG: Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType = (
        ...
    )  # static # readonly
    eBlobFormat_SDF: Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType = (
        ...
    )  # static # readonly
    eBlobFormat_Text: Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType = (
        ...
    )  # static # readonly
    eBlobFormat_Unspecified: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType
    ) = ...  # static # readonly
    eBlobFormat_XML: Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType = (
        ...
    )  # static # readonly

class ChemSpiderInfoRecord:  # Class
    CSID: str  # readonly
    ChemSpiderFormula: str  # readonly
    InChI: str  # readonly
    IntCSID: int  # readonly
    MonoisotopicMass: float  # readonly
    Name: str  # readonly
    SMILES: str  # readonly

class ChemSpiderSearch:  # Class
    def __init__(self) -> None: ...
    @overload
    def Do(
        self,
        request: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderSearchByMassRequest,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderSearchByMassResult: ...
    @overload
    def Do(
        self,
        request: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderSearchByFormulaRequest,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderSearchByFormulaResult: ...

class ChemSpiderSearchByFormulaRequest:  # Class
    @overload
    def __init__(self, formulaString: str) -> None: ...
    @overload
    def __init__(
        self, formula: Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula
    ) -> None: ...

    FormulaString: str  # readonly
    MolecularFormula: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula
    )  # readonly

class ChemSpiderSearchByFormulaResult:  # Class
    def __init__(
        self,
        request: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderSearchByFormulaRequest,
        csidList: List[str],
        resultRecords: List[
            Agilent.MassSpectrometry.DataAnalysis.MFS.ExtendedCompoundInfo
        ],
    ) -> None: ...
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderInfoRecord: ...
    RecordCount: int  # readonly
    SearchRequest: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderSearchByFormulaRequest
    )  # readonly

class ChemSpiderSearchByMassRequest:  # Class
    @overload
    def __init__(
        self,
        mass: float,
        massRange: float,
        allowedElements: System.Collections.Generic.HashSet[str],
    ) -> None: ...
    @overload
    def __init__(
        self,
        mass: float,
        massRange: float,
        allowedElements: System.Collections.Generic.HashSet[str],
        maxCharge: int,
        useC13: bool,
    ) -> None: ...

    AllowedElements: System.Collections.Generic.HashSet[str]  # readonly
    Mass: float  # readonly
    MassRange: float  # readonly
    MaxCharge: int  # readonly

    def MassRangeContains(self, mass: float) -> bool: ...

class ChemSpiderSearchByMassResult:  # Class
    def __init__(
        self,
        request: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderSearchByMassRequest,
        csidList: List[str],
        resultRecords: List[
            Agilent.MassSpectrometry.DataAnalysis.MFS.ExtendedCompoundInfo
        ],
    ) -> None: ...

    FormulaCount: int  # readonly
    def __getitem__(
        self, index: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderInfoRecord: ...
    RecordCount: int  # readonly
    SearchRequest: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderSearchByMassRequest
    )  # readonly

    def GetFormulas(
        self,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula
    ]: ...
    def GetMassList(self) -> System.Collections.Generic.List[float]: ...
    def GetFormulaByMass(
        self, mass: float
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula: ...

class ChemicalElement:  # Class
    AtomicNumber: int  # readonly
    ElementType: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum
    )  # readonly
    Name: str  # readonly
    Symbol: str  # readonly
    Valence: int  # readonly

class ChemicalElementEnum(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    Ac: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ag: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Al: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Am: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ar: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    As: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    At: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Au: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    B: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ba: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Be: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Bh: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Bi: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Bk: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Br: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    C: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ca: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Cd: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ce: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Cf: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Cl: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Cm: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Cn: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Co: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Cr: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Cs: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Cu: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Db: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ds: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Dy: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Er: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Es: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Eu: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    F: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Fe: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Fm: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Fr: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ga: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Gd: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ge: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    H: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    He: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Hf: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Hg: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ho: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Hs: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    I: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    In: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ir: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    K: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Kr: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    La: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Li: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Lr: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Lu: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Md: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Mg: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Mn: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Mo: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Mt: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    N: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Na: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Nb: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Nd: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ne: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ni: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    No: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Np: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    O: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Os: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    P: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Pa: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Pb: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Pd: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Pm: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Po: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Pr: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Pt: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Pu: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ra: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Rb: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Re: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Rf: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Rg: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Rh: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Rn: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ru: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    S: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Sb: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Sc: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Se: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Sg: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Si: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Sm: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Sn: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Sr: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ta: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Tc: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Te: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Th: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Ti: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Tl: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Tm: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    U: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Uuh: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Uuo: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Uup: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Uuq: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Uus: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Uut: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    V: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    W: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Xe: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Y: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Yb: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Zn: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly
    Zr: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElementEnum = (
        ...
    )  # static # readonly

class ColumnDescriptionType:  # Class
    def __init__(self) -> None: ...

    ActiveConcentration: bool
    ActiveConcentrationSpecified: bool
    Description: List[str]
    Heading: Agilent.MassSpectrometry.DataAnalysis.MFS.HeadingType
    Name: str
    TID: int
    TIDSpecified: bool
    TestedConcentration: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.TestedConcentrationType
    )
    Type: str
    Unit: str

class CompressType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eCompress_BZip2: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType = (
        ...
    )  # static # readonly
    eCompress_GZip: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType = (
        ...
    )  # static # readonly
    eCompress_None: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType = (
        ...
    )  # static # readonly

class DataBlobType:  # Class
    def __init__(self) -> None: ...

    BlobFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.BlobFormatType
    BlobFormatSpecified: bool
    Data: List[int]
    eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType
    eCompressSpecified: bool

class DownloadCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    DataBlob: Agilent.MassSpectrometry.DataAnalysis.MFS.DataBlobType  # readonly
    Result: str  # readonly

class DownloadCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.DownloadCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.DownloadCompletedEventArgs,
    ) -> None: ...

class ECompression(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eGzip: Agilent.MassSpectrometry.DataAnalysis.MFS.ECompression = (
        ...
    )  # static # readonly

class EntrezKey:  # Class
    def __init__(self) -> None: ...

    db: str
    key: str
    webenv: str

class ExtendedCompoundInfo:  # Class
    def __init__(self) -> None: ...

    ALogP: float
    AverageMass: float
    CSID: int
    CommonName: str
    InChI: str
    InChIKey: str
    MF: str
    MolecularWeight: float
    MonoisotopicMass: float
    NominalMass: float
    SMILES: str
    XLogP: float

class FormatType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eFormat_ASNB: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType = (
        ...
    )  # static # readonly
    eFormat_ASNT: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType = (
        ...
    )  # static # readonly
    eFormat_Image: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType = (
        ...
    )  # static # readonly
    eFormat_InChI: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType = (
        ...
    )  # static # readonly
    eFormat_SDF: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType = (
        ...
    )  # static # readonly
    eFormat_SMILES: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType = (
        ...
    )  # static # readonly
    eFormat_Thumbnail: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType = (
        ...
    )  # static # readonly
    eFormat_XML: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType = (
        ...
    )  # static # readonly

class FragmentGenerator:  # Class
    def __init__(
        self, cpdFormula: Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula
    ) -> None: ...
    def IsValidFragmentMassEI(self, massEI: float, mzDeltaPpm: float) -> bool: ...
    @overload
    def GetFragments(
        self,
        molWeight: int,
        allowedElements: List[
            Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElement
        ],
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula
    ]: ...
    @overload
    def GetFragments(
        self, molWeight: int
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula
    ]: ...
    def IsValidFragmentMassESI(self, massESI: float, mzDeltaPpm: float) -> bool: ...

class GetAssayColumnDescriptionCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: Agilent.MassSpectrometry.DataAnalysis.MFS.ColumnDescriptionType  # readonly

class GetAssayColumnDescriptionCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetAssayColumnDescriptionCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetAssayColumnDescriptionCompletedEventArgs,
    ) -> None: ...

class GetAssayColumnDescriptionsCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: List[
        Agilent.MassSpectrometry.DataAnalysis.MFS.ColumnDescriptionType
    ]  # readonly

class GetAssayColumnDescriptionsCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetAssayColumnDescriptionsCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetAssayColumnDescriptionsCompletedEventArgs,
    ) -> None: ...

class GetAssayDescriptionCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    DataBlob: Agilent.MassSpectrometry.DataAnalysis.MFS.DataBlobType  # readonly
    Result: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayDescriptionType  # readonly

class GetAssayDescriptionCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetAssayDescriptionCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetAssayDescriptionCompletedEventArgs,
    ) -> None: ...

class GetCompressedRecordsSdfCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: List[int]  # readonly

class GetCompressedRecordsSdfCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetCompressedRecordsSdfCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetCompressedRecordsSdfCompletedEventArgs,
    ) -> None: ...

class GetDatabasesCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: List[str]  # readonly

class GetDatabasesCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetDatabasesCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetDatabasesCompletedEventArgs,
    ) -> None: ...

class GetDownloadUrlCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class GetDownloadUrlCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetDownloadUrlCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetDownloadUrlCompletedEventArgs,
    ) -> None: ...

class GetEntrezKeyCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey  # readonly

class GetEntrezKeyCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetEntrezKeyCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetEntrezKeyCompletedEventArgs,
    ) -> None: ...

class GetEntrezUrlCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class GetEntrezUrlCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetEntrezUrlCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetEntrezUrlCompletedEventArgs,
    ) -> None: ...

class GetExtendedCompoundInfoArrayCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: List[
        Agilent.MassSpectrometry.DataAnalysis.MFS.ExtendedCompoundInfo
    ]  # readonly

class GetExtendedCompoundInfoArrayCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetExtendedCompoundInfoArrayCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetExtendedCompoundInfoArrayCompletedEventArgs,
    ) -> None: ...

class GetExtendedCompoundInfoCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: Agilent.MassSpectrometry.DataAnalysis.MFS.ExtendedCompoundInfo  # readonly

class GetExtendedCompoundInfoCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetExtendedCompoundInfoCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetExtendedCompoundInfoCompletedEventArgs,
    ) -> None: ...

class GetIDListCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: List[int]  # readonly

class GetIDListCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetIDListCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetIDListCompletedEventArgs,
    ) -> None: ...

class GetListItemsCountCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: int  # readonly

class GetListItemsCountCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetListItemsCountCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetListItemsCountCompletedEventArgs,
    ) -> None: ...

class GetOperationStatusCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType  # readonly

class GetOperationStatusCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetOperationStatusCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetOperationStatusCompletedEventArgs,
    ) -> None: ...

class GetRecordMolCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class GetRecordMolCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetRecordMolCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetRecordMolCompletedEventArgs,
    ) -> None: ...

class GetRecordsSdfCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class GetRecordsSdfCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetRecordsSdfCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetRecordsSdfCompletedEventArgs,
    ) -> None: ...

class GetStandardizedCIDCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: int  # readonly

class GetStandardizedCIDCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetStandardizedCIDCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetStandardizedCIDCompletedEventArgs,
    ) -> None: ...

class GetStandardizedStructureBase64CompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: List[int]  # readonly

class GetStandardizedStructureBase64CompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetStandardizedStructureBase64CompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetStandardizedStructureBase64CompletedEventArgs,
    ) -> None: ...

class GetStandardizedStructureCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class GetStandardizedStructureCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetStandardizedStructureCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetStandardizedStructureCompletedEventArgs,
    ) -> None: ...

class GetStatusMessageCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class GetStatusMessageCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetStatusMessageCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.GetStatusMessageCompletedEventArgs,
    ) -> None: ...

class HeadingType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    TID: Agilent.MassSpectrometry.DataAnalysis.MFS.HeadingType = (
        ...
    )  # static # readonly
    outcome: Agilent.MassSpectrometry.DataAnalysis.MFS.HeadingType = (
        ...
    )  # static # readonly
    score: Agilent.MassSpectrometry.DataAnalysis.MFS.HeadingType = (
        ...
    )  # static # readonly

class IAdductIon(object):  # Interface
    AdductType: Agilent.MassSpectrometry.DataAnalysis.MFS.AdductType  # readonly
    Formula: str  # readonly
    Mass: float  # readonly

class IDExchangeCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    DownloadKey: str  # readonly
    Result: str  # readonly

class IDExchangeCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.IDExchangeCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.IDExchangeCompletedEventArgs,
    ) -> None: ...

class IDOperationType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eIDOperation_Same: Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType = (
        ...
    )  # static # readonly
    eIDOperation_SameConnectivity: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType
    ) = ...  # static # readonly
    eIDOperation_SameIsotope: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType
    ) = ...  # static # readonly
    eIDOperation_SameParent: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType
    ) = ...  # static # readonly
    eIDOperation_SameParentConnectivity: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType
    ) = ...  # static # readonly
    eIDOperation_SameParentIsotope: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType
    ) = ...  # static # readonly
    eIDOperation_SameParentStereo: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType
    ) = ...  # static # readonly
    eIDOperation_SameStereo: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType
    ) = ...  # static # readonly
    eIDOperation_Similar2D: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType
    ) = ...  # static # readonly
    eIDOperation_Similar3D: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType
    ) = ...  # static # readonly

class IDOutputFormatType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eIDOutputFormat_Entrez: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOutputFormatType
    ) = ...  # static # readonly
    eIDOutputFormat_FileList: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOutputFormatType
    ) = ...  # static # readonly
    eIDOutputFormat_FilePair: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDOutputFormatType
    ) = ...  # static # readonly

class IIsotopePattern(object):  # Interface
    IsotopeCompositions: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MFS.IsotopeComposition
    ]  # readonly
    IsotopeCompositionsByMass: System.Collections.Generic.SortedList[
        float, Agilent.MassSpectrometry.DataAnalysis.MFS.IsotopeComposition
    ]  # readonly
    MostAbundantIsotopeComposition: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IsotopeComposition
    )  # readonly
    NIsotopeCompositions: int  # readonly

    def GetRelativeAbundanceByMass(
        self,
        mass: System.Collections.Generic.List[float],
        relativeAbundance: System.Collections.Generic.List[float],
    ) -> None: ...

class IdentitySearchCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class IdentitySearchCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.IdentitySearchCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.IdentitySearchCompletedEventArgs,
    ) -> None: ...

class IdentitySearchOptions:  # Class
    def __init__(self) -> None: ...

    ToWebEnv: str
    eIdentity: Agilent.MassSpectrometry.DataAnalysis.MFS.IdentityType

class IdentityType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eIdentity_AnyTautomer: Agilent.MassSpectrometry.DataAnalysis.MFS.IdentityType = (
        ...
    )  # static # readonly
    eIdentity_SameConnectivity: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IdentityType
    ) = ...  # static # readonly
    eIdentity_SameIsotope: Agilent.MassSpectrometry.DataAnalysis.MFS.IdentityType = (
        ...
    )  # static # readonly
    eIdentity_SameIsotopeNonconflictStereo: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IdentityType
    ) = ...  # static # readonly
    eIdentity_SameNonconflictStereo: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IdentityType
    ) = ...  # static # readonly
    eIdentity_SameStereo: Agilent.MassSpectrometry.DataAnalysis.MFS.IdentityType = (
        ...
    )  # static # readonly
    eIdentity_SameStereoIsotope: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IdentityType
    ) = ...  # static # readonly

class InputAssayCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class InputAssayCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputAssayCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputAssayCompletedEventArgs,
    ) -> None: ...

class InputEntrezCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class InputEntrezCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputEntrezCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputEntrezCompletedEventArgs,
    ) -> None: ...

class InputListCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class InputListCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputListCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputListCompletedEventArgs,
    ) -> None: ...

class InputListStringCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class InputListStringCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputListStringCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputListStringCompletedEventArgs,
    ) -> None: ...

class InputListTextCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class InputListTextCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputListTextCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputListTextCompletedEventArgs,
    ) -> None: ...

class InputStructureBase64CompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class InputStructureBase64CompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputStructureBase64CompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputStructureBase64CompletedEventArgs,
    ) -> None: ...

class InputStructureCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class InputStructureCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputStructureCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.InputStructureCompletedEventArgs,
    ) -> None: ...

class IonizationType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    EI: Agilent.MassSpectrometry.DataAnalysis.MFS.IonizationType = (
        ...
    )  # static # readonly
    ESI: Agilent.MassSpectrometry.DataAnalysis.MFS.IonizationType = (
        ...
    )  # static # readonly

class Isotope:  # Class
    Element: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElement  # readonly
    IsMostAbundant: bool  # readonly
    IsotopeSymbol: str  # readonly
    Mass: float  # readonly
    MassDefect: float  # readonly
    MassNumber: int  # readonly
    RelativeAbundance: float  # readonly

class IsotopeComposition:  # Class
    def __init__(
        self, formula: Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula
    ) -> None: ...

    Mass: float  # readonly
    RelativeAbundance: float  # readonly

    def Replace(
        self,
        oldIsotope: Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope,
        newIsotope: Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.IsotopeComposition: ...
    def ToString(self) -> str: ...

class IsotopePattern(
    Agilent.MassSpectrometry.DataAnalysis.MFS.IIsotopePattern
):  # Class
    @overload
    def __init__(
        self,
        formula: Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula,
        minRelativeAbundance: float,
    ) -> None: ...
    @overload
    def __init__(
        self,
        formula: Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula,
        dominantIsotopePatternOnly: bool,
        minRelativeAbundance: float,
    ) -> None: ...

    IsotopeCompositions: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MFS.IsotopeComposition
    ]  # readonly
    IsotopeCompositionsByMass: System.Collections.Generic.SortedList[
        float, Agilent.MassSpectrometry.DataAnalysis.MFS.IsotopeComposition
    ]  # readonly
    MostAbundantIsotopeComposition: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IsotopeComposition
    )  # readonly
    NIsotopeCompositions: int  # readonly

    def GetRelativeAbundanceByMass(
        self,
        mass: System.Collections.Generic.List[float],
        relativeAbundance: System.Collections.Generic.List[float],
    ) -> None: ...
    def GetResolutionAveragedIsotopeSpectrum(
        self,
        adduct: Agilent.MassSpectrometry.DataAnalysis.MFS.IAdductIon,
        mzResolutionPpm: float,
        mzValues: List[float],
        abundanceValues: List[float],
    ) -> None: ...

class IsotopeTable:  # Class
    ELECTRON_MASS: float  # static # readonly
    PROTON_MASS: float  # static # readonly

    @overload
    @staticmethod
    def GetMostAbundantIsotope(
        element: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElement,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope: ...
    @overload
    @staticmethod
    def GetMostAbundantIsotope(
        symbol: str,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope: ...
    @overload
    @staticmethod
    def GetIsotope(
        element: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElement,
        massNumber: int,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope: ...
    @overload
    @staticmethod
    def GetIsotope(
        symbol: str, massNumber: int
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope: ...
    @staticmethod
    def GetHeaviestIsotope(
        element: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElement,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope: ...
    @staticmethod
    def GetElementBySymbol(
        symbol: str,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElement: ...
    @overload
    @staticmethod
    def GetIsotopesForElement(
        element: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElement,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope
    ]: ...
    @overload
    @staticmethod
    def GetIsotopesForElement(
        symbol: str,
    ) -> System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope
    ]: ...

class LimitsType:  # Class
    def __init__(self) -> None: ...

    ListKey: str
    maxRecords: int
    maxRecordsSpecified: bool
    seconds: int
    secondsSpecified: bool

class MFSException(
    System.ApplicationException,
    System.Runtime.InteropServices._Exception,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, msg: str) -> None: ...

class MFSearchCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class MFSearchCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.MFSearchCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.MFSearchCompletedEventArgs,
    ) -> None: ...

class MFSearchOptions:  # Class
    def __init__(self) -> None: ...

    AllowOtherElements: bool
    ToWebEnv: str

class MassSpecAPI(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.Web.Services.Protocols.SoapHttpClientProtocol,
):  # Class
    def __init__(self) -> None: ...
    def EndSearchByMassAsync1(self, asyncResult: System.IAsyncResult) -> str: ...
    @overload
    def GetRecordsSdfAsync(self, rid: str, token: str) -> None: ...
    @overload
    def GetRecordsSdfAsync(self, rid: str, token: str, userState: Any) -> None: ...
    @overload
    def SearchByFormulaAsync1Async(
        self, formula: str, dbs: List[str], token: str
    ) -> None: ...
    @overload
    def SearchByFormulaAsync1Async(
        self, formula: str, dbs: List[str], token: str, userState: Any
    ) -> None: ...
    @overload
    def SearchByMassAsync1Async(
        self, mass: float, range: float, dbs: List[str], token: str
    ) -> None: ...
    @overload
    def SearchByMassAsync1Async(
        self, mass: float, range: float, dbs: List[str], token: str, userState: Any
    ) -> None: ...
    def GetDatabases(self) -> List[str]: ...
    def BeginSearchByMassAsync1(
        self,
        mass: float,
        range: float,
        dbs: List[str],
        token: str,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    @overload
    def GetDatabasesAsync(self) -> None: ...
    @overload
    def GetDatabasesAsync(self, userState: Any) -> None: ...
    def EndGetRecordMol(self, asyncResult: System.IAsyncResult) -> str: ...
    @overload
    def GetRecordMolAsync(self, csid: str, calc3d: bool, token: str) -> None: ...
    @overload
    def GetRecordMolAsync(
        self, csid: str, calc3d: bool, token: str, userState: Any
    ) -> None: ...
    @overload
    def SearchByFormula2Async(self, formula: str) -> None: ...
    @overload
    def SearchByFormula2Async(self, formula: str, userState: Any) -> None: ...
    def BeginSearchByFormula2(
        self, formula: str, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def BeginGetExtendedCompoundInfo(
        self, CSID: int, token: str, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def BeginGetRecordsSdf(
        self, rid: str, token: str, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def BeginGetDatabases(
        self, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    @overload
    def GetExtendedCompoundInfoAsync(self, CSID: int, token: str) -> None: ...
    @overload
    def GetExtendedCompoundInfoAsync(
        self, CSID: int, token: str, userState: Any
    ) -> None: ...
    def BeginGetCompressedRecordsSdf(
        self,
        rid: str,
        token: str,
        eComp: Agilent.MassSpectrometry.DataAnalysis.MFS.ECompression,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def GetExtendedCompoundInfo(
        self, CSID: int, token: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.ExtendedCompoundInfo: ...
    def EndSearchByMass(self, asyncResult: System.IAsyncResult) -> List[str]: ...
    @overload
    def GetExtendedCompoundInfoArrayAsync(
        self, CSIDs: List[int], token: str
    ) -> None: ...
    @overload
    def GetExtendedCompoundInfoArrayAsync(
        self, CSIDs: List[int], token: str, userState: Any
    ) -> None: ...
    def GetCompressedRecordsSdf(
        self,
        rid: str,
        token: str,
        eComp: Agilent.MassSpectrometry.DataAnalysis.MFS.ECompression,
    ) -> List[int]: ...
    def SearchByMass2(self, mass: float, range: float) -> List[str]: ...
    def SearchByFormula(self, formula: str, dbs: List[str]) -> List[str]: ...
    def GetRecordMol(self, csid: str, calc3d: bool, token: str) -> str: ...
    def BeginSearchByMass2(
        self, mass: float, range: float, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    @overload
    def SearchByMass2Async(self, mass: float, range: float) -> None: ...
    @overload
    def SearchByMass2Async(self, mass: float, range: float, userState: Any) -> None: ...
    def BeginSearchByFormulaAsync1(
        self,
        formula: str,
        dbs: List[str],
        token: str,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def EndGetExtendedCompoundInfoArray(
        self, asyncResult: System.IAsyncResult
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MFS.ExtendedCompoundInfo]: ...
    def EndGetDatabases(self, asyncResult: System.IAsyncResult) -> List[str]: ...
    @overload
    def GetCompressedRecordsSdfAsync(
        self,
        rid: str,
        token: str,
        eComp: Agilent.MassSpectrometry.DataAnalysis.MFS.ECompression,
    ) -> None: ...
    @overload
    def GetCompressedRecordsSdfAsync(
        self,
        rid: str,
        token: str,
        eComp: Agilent.MassSpectrometry.DataAnalysis.MFS.ECompression,
        userState: Any,
    ) -> None: ...
    def GetRecordsSdf(self, rid: str, token: str) -> str: ...
    def EndSearchByFormula(self, asyncResult: System.IAsyncResult) -> List[str]: ...
    def BeginSearchByFormula(
        self,
        formula: str,
        dbs: List[str],
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def EndGetRecordsSdf(self, asyncResult: System.IAsyncResult) -> str: ...
    def SearchByFormula2(self, formula: str) -> List[str]: ...
    def BeginGetExtendedCompoundInfoArray(
        self,
        CSIDs: List[int],
        token: str,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def CancelAsync(self, userState: Any) -> None: ...
    def EndGetCompressedRecordsSdf(
        self, asyncResult: System.IAsyncResult
    ) -> List[int]: ...
    def BeginSearchByMass(
        self,
        mass: float,
        range: float,
        dbs: List[str],
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    @overload
    def SearchByMassAsync(self, mass: float, range: float, dbs: List[str]) -> None: ...
    @overload
    def SearchByMassAsync(
        self, mass: float, range: float, dbs: List[str], userState: Any
    ) -> None: ...
    @overload
    def SearchByMassAsync(
        self, mass: float, range: float, dbs: List[str], token: str
    ) -> str: ...
    def SearchByMass(self, mass: float, range: float, dbs: List[str]) -> List[str]: ...
    def EndSearchByFormula2(self, asyncResult: System.IAsyncResult) -> List[str]: ...
    def GetExtendedCompoundInfoArray(
        self, CSIDs: List[int], token: str
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MFS.ExtendedCompoundInfo]: ...
    def EndSearchByMass2(self, asyncResult: System.IAsyncResult) -> List[str]: ...
    @overload
    def SearchByFormulaAsync(self, formula: str, dbs: List[str]) -> None: ...
    @overload
    def SearchByFormulaAsync(
        self, formula: str, dbs: List[str], userState: Any
    ) -> None: ...
    @overload
    def SearchByFormulaAsync(self, formula: str, dbs: List[str], token: str) -> str: ...
    def EndSearchByFormulaAsync1(self, asyncResult: System.IAsyncResult) -> str: ...
    def BeginGetRecordMol(
        self,
        csid: str,
        calc3d: bool,
        token: str,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def EndGetExtendedCompoundInfo(
        self, asyncResult: System.IAsyncResult
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.ExtendedCompoundInfo: ...

    GetCompressedRecordsSdfCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetCompressedRecordsSdfCompletedEventHandler
    )  # Event
    GetDatabasesCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetDatabasesCompletedEventHandler
    )  # Event
    GetExtendedCompoundInfoArrayCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetExtendedCompoundInfoArrayCompletedEventHandler
    )  # Event
    GetExtendedCompoundInfoCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetExtendedCompoundInfoCompletedEventHandler
    )  # Event
    GetRecordMolCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetRecordMolCompletedEventHandler
    )  # Event
    GetRecordsSdfCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetRecordsSdfCompletedEventHandler
    )  # Event
    SearchByFormula2Completed: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByFormula2CompletedEventHandler
    )  # Event
    SearchByFormulaAsync1Completed: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByFormulaAsync1CompletedEventHandler
    )  # Event
    SearchByFormulaCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByFormulaCompletedEventHandler
    )  # Event
    SearchByMass2Completed: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByMass2CompletedEventHandler
    )  # Event
    SearchByMassAsync1Completed: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByMassAsync1CompletedEventHandler
    )  # Event
    SearchByMassCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByMassCompletedEventHandler
    )  # Event

class MatrixFormatType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eMatrixFormat_CSV: Agilent.MassSpectrometry.DataAnalysis.MFS.MatrixFormatType = (
        ...
    )  # static # readonly
    eMatrixFormat_IdIdScore: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.MatrixFormatType
    ) = ...  # static # readonly

class MolecularFormula:  # Class
    @overload
    def __init__(
        self,
        compoundRecord: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemSpiderInfoRecord,
    ) -> None: ...
    @overload
    def __init__(self, formula: str) -> None: ...
    @overload
    def __init__(self, formula: str, compoundName: str) -> None: ...
    @overload
    def __init__(
        self,
        isotopes: List[Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope],
        counts: List[int],
    ) -> None: ...

    Charge: int  # readonly
    ChemicalElements: List[
        Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElement
    ]  # readonly
    CsidOrigin: str  # readonly
    DegreeOfUnsaturation: float  # readonly
    DeuteriumCount: int  # readonly
    ElementalComposition: Dict[
        Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElement, int
    ]  # readonly
    Elements: System.Collections.Generic.HashSet[str]  # readonly
    HasNonStandardIsotopes: bool  # readonly
    HasUnsupportedIsotopes: bool  # readonly
    HydrogenCount: int  # readonly
    IsCharged: bool  # readonly
    IsotopeComposition: Dict[
        Agilent.MassSpectrometry.DataAnalysis.MFS.Isotope, int
    ]  # readonly
    MaxMonoisotopicMass: float  # readonly
    MaxMonoisotopicMassEI: float  # readonly
    MonoisotopicMass: float  # readonly
    MonoisotopicMassEI: float  # readonly
    SimpleFormula: str  # readonly
    StandardFormulaFormat: str  # readonly

    def GetAtomCountFor(
        self, element: Agilent.MassSpectrometry.DataAnalysis.MFS.ChemicalElement
    ) -> int: ...
    def IsContainedIn(
        self,
        parent: Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula,
        ignoreIsotopes: bool,
    ) -> bool: ...

    # Nested Types

    class MassComparer(
        System.Collections.Generic.IComparer[
            Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula
        ]
    ):  # Class
        def __init__(self) -> None: ...
        def Compare(
            self,
            x: Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula,
            y: Agilent.MassSpectrometry.DataAnalysis.MFS.MolecularFormula,
        ) -> int: ...

class PCIDType(System.IConvertible, System.IComparable, System.IFormattable):  # Struct
    eID_AID: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType = (
        ...
    )  # static # readonly
    eID_CID: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType = (
        ...
    )  # static # readonly
    eID_ConformerID: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType = (
        ...
    )  # static # readonly
    eID_InChI: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType = (
        ...
    )  # static # readonly
    eID_InChIKey: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType = (
        ...
    )  # static # readonly
    eID_SID: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType = (
        ...
    )  # static # readonly
    eID_SourceID: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType = (
        ...
    )  # static # readonly
    eID_TID: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType = (
        ...
    )  # static # readonly

class PUG(
    System.IDisposable,
    System.ComponentModel.IComponent,
    System.Web.Services.Protocols.SoapHttpClientProtocol,
):  # Class
    def __init__(self) -> None: ...
    def InputAssay(
        self,
        AID: int,
        Columns: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayColumnsType,
        ListKeyTIDs: str,
        ListKeySCIDs: str,
        OutcomeFilter: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayOutcomeFilterType,
        OutcomeFilterSpecified: bool,
    ) -> str: ...
    def GetStandardizedStructureBase64(
        self, StrKey: str, format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType
    ) -> List[int]: ...
    def InputStructureBase64(
        self,
        structure: List[int],
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
    ) -> str: ...
    def MFSearch(
        self,
        MF: str,
        mfOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.MFSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
    ) -> str: ...
    def BeginGetDownloadUrl(
        self, DownloadKey: str, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def Standardize(self, StrKey: str) -> None: ...
    def BeginIdentitySearch(
        self,
        StrKey: str,
        idOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.IdentitySearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def EndGetOperationStatus(
        self, asyncResult: System.IAsyncResult
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType: ...
    @overload
    def DownloadAsync(
        self,
        ListKey: str,
        eFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        Use3D: bool,
        Use3DSpecified: bool,
        N3DConformers: int,
        N3DConformersSpecified: bool,
        SynchronousSingleRecord: bool,
        SynchronousSingleRecordSpecified: bool,
    ) -> None: ...
    @overload
    def DownloadAsync(
        self,
        ListKey: str,
        eFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        Use3D: bool,
        Use3DSpecified: bool,
        N3DConformers: int,
        N3DConformersSpecified: bool,
        SynchronousSingleRecord: bool,
        SynchronousSingleRecordSpecified: bool,
        userState: Any,
    ) -> None: ...
    def InputList(
        self, ids: List[int], idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType
    ) -> str: ...
    @overload
    def GetOperationStatusAsync(self, AnyKey: str) -> None: ...
    @overload
    def GetOperationStatusAsync(self, AnyKey: str, userState: Any) -> None: ...
    def EndGetStatusMessage(self, asyncResult: System.IAsyncResult) -> str: ...
    @overload
    def InputListTextAsync(
        self, ids: str, idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType
    ) -> None: ...
    @overload
    def InputListTextAsync(
        self,
        ids: str,
        idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        userState: Any,
    ) -> None: ...
    def BeginGetIDList(
        self,
        ListKey: str,
        Start: int,
        StartSpecified: bool,
        Count: int,
        CountSpecified: bool,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    @overload
    def InputStructureBase64Async(
        self,
        structure: List[int],
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
    ) -> None: ...
    @overload
    def InputStructureBase64Async(
        self,
        structure: List[int],
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        userState: Any,
    ) -> None: ...
    def EndDownload(
        self,
        asyncResult: System.IAsyncResult,
        DataBlob: Agilent.MassSpectrometry.DataAnalysis.MFS.DataBlobType,
    ) -> str: ...
    def EndInputListString(self, asyncResult: System.IAsyncResult) -> str: ...
    @overload
    def GetIDListAsync(
        self,
        ListKey: str,
        Start: int,
        StartSpecified: bool,
        Count: int,
        CountSpecified: bool,
    ) -> None: ...
    @overload
    def GetIDListAsync(
        self,
        ListKey: str,
        Start: int,
        StartSpecified: bool,
        Count: int,
        CountSpecified: bool,
        userState: Any,
    ) -> None: ...
    def BeginIDExchange(
        self,
        InputListKey: str,
        Operation: Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType,
        OutputType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        OutputSourceName: str,
        OutputFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.IDOutputFormatType,
        ToWebEnv: str,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def EndInputAssay(self, asyncResult: System.IAsyncResult) -> str: ...
    @overload
    def SimilaritySearch2DAsync(
        self,
        StrKey: str,
        simOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.SimilaritySearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
    ) -> None: ...
    @overload
    def SimilaritySearch2DAsync(
        self,
        StrKey: str,
        simOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.SimilaritySearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
        userState: Any,
    ) -> None: ...
    def GetAssayColumnDescriptions(
        self, AID: int
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MFS.ColumnDescriptionType]: ...
    def EndGetStandardizedCID(self, asyncResult: System.IAsyncResult) -> int: ...
    def BeginInputStructureBase64(
        self,
        structure: List[int],
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    @overload
    def GetAssayColumnDescriptionsAsync(self, AID: int) -> None: ...
    @overload
    def GetAssayColumnDescriptionsAsync(self, AID: int, userState: Any) -> None: ...
    def GetAssayDescription(
        self,
        AID: int,
        GetVersion: bool,
        GetVersionSpecified: bool,
        GetCounts: bool,
        GetCountsSpecified: bool,
        GetFullDataBlob: bool,
        GetFullDataBlobSpecified: bool,
        eFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        eFormatSpecified: bool,
        DataBlob: Agilent.MassSpectrometry.DataAnalysis.MFS.DataBlobType,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.AssayDescriptionType: ...
    def EndGetEntrezKey(
        self, asyncResult: System.IAsyncResult
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey: ...
    def EndInputList(self, asyncResult: System.IAsyncResult) -> str: ...
    @overload
    def GetListItemsCountAsync(self, ListKey: str) -> None: ...
    @overload
    def GetListItemsCountAsync(self, ListKey: str, userState: Any) -> None: ...
    def GetDownloadUrl(self, DownloadKey: str) -> str: ...
    def EndSubstructureSearch(self, asyncResult: System.IAsyncResult) -> str: ...
    def SimilaritySearch2D(
        self,
        StrKey: str,
        simOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.SimilaritySearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
    ) -> str: ...
    @overload
    def SubstructureSearchAsync(
        self,
        StrKey: str,
        ssOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.StructureSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
    ) -> None: ...
    @overload
    def SubstructureSearchAsync(
        self,
        StrKey: str,
        ssOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.StructureSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
        userState: Any,
    ) -> None: ...
    @overload
    def GetStandardizedCIDAsync(self, StrKey: str) -> None: ...
    @overload
    def GetStandardizedCIDAsync(self, StrKey: str, userState: Any) -> None: ...
    def GetListItemsCount(self, ListKey: str) -> int: ...
    @overload
    def InputListAsync(
        self, ids: List[int], idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType
    ) -> None: ...
    @overload
    def InputListAsync(
        self,
        ids: List[int],
        idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        userState: Any,
    ) -> None: ...
    def EndGetAssayColumnDescription(
        self, asyncResult: System.IAsyncResult
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.ColumnDescriptionType: ...
    def BeginSubstructureSearch(
        self,
        StrKey: str,
        ssOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.StructureSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def BeginGetAssayColumnDescription(
        self,
        AID: int,
        Heading: Agilent.MassSpectrometry.DataAnalysis.MFS.HeadingType,
        TID: int,
        TIDSpecified: bool,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def GetStandardizedStructure(
        self, StrKey: str, format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType
    ) -> str: ...
    def EndMFSearch(self, asyncResult: System.IAsyncResult) -> str: ...
    def BeginAssayDownload(
        self,
        AssayKey: str,
        AssayFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayFormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    @overload
    def SuperstructureSearchAsync(
        self,
        StrKey: str,
        ssOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.StructureSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
    ) -> None: ...
    @overload
    def SuperstructureSearchAsync(
        self,
        StrKey: str,
        ssOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.StructureSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
        userState: Any,
    ) -> None: ...
    @overload
    def InputEntrezAsync(
        self, EntrezKey: Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey
    ) -> None: ...
    @overload
    def InputEntrezAsync(
        self,
        EntrezKey: Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey,
        userState: Any,
    ) -> None: ...
    def BeginGetStatusMessage(
        self, AnyKey: str, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def BeginSimilaritySearch2D(
        self,
        StrKey: str,
        simOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.SimilaritySearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def EndStandardize(self, asyncResult: System.IAsyncResult, StrKey: str) -> None: ...
    def BeginInputEntrez(
        self,
        EntrezKey: Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    @overload
    def StandardizeAsync(self, StrKey: str) -> None: ...
    @overload
    def StandardizeAsync(self, StrKey: str, userState: Any) -> None: ...
    @overload
    def IDExchangeAsync(
        self,
        InputListKey: str,
        Operation: Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType,
        OutputType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        OutputSourceName: str,
        OutputFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.IDOutputFormatType,
        ToWebEnv: str,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
    ) -> None: ...
    @overload
    def IDExchangeAsync(
        self,
        InputListKey: str,
        Operation: Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType,
        OutputType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        OutputSourceName: str,
        OutputFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.IDOutputFormatType,
        ToWebEnv: str,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        userState: Any,
    ) -> None: ...
    def EndGetDownloadUrl(self, asyncResult: System.IAsyncResult) -> str: ...
    def BeginGetEntrezUrl(
        self,
        EntrezKey: Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def BeginGetAssayColumnDescriptions(
        self, AID: int, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    @overload
    def GetStandardizedStructureAsync(
        self, StrKey: str, format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType
    ) -> None: ...
    @overload
    def GetStandardizedStructureAsync(
        self,
        StrKey: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        userState: Any,
    ) -> None: ...
    def GetStandardizedCID(self, StrKey: str) -> int: ...
    def EndSuperstructureSearch(self, asyncResult: System.IAsyncResult) -> str: ...
    def GetAssayColumnDescription(
        self,
        AID: int,
        Heading: Agilent.MassSpectrometry.DataAnalysis.MFS.HeadingType,
        TID: int,
        TIDSpecified: bool,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.ColumnDescriptionType: ...
    def BeginInputListString(
        self,
        strids: List[str],
        idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        SourceName: str,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def InputEntrez(
        self, EntrezKey: Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey
    ) -> str: ...
    @overload
    def GetDownloadUrlAsync(self, DownloadKey: str) -> None: ...
    @overload
    def GetDownloadUrlAsync(self, DownloadKey: str, userState: Any) -> None: ...
    def EndGetStandardizedStructure(self, asyncResult: System.IAsyncResult) -> str: ...
    def BeginStandardize(
        self, StrKey: str, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def GetStatusMessage(self, AnyKey: str) -> str: ...
    def EndInputListText(self, asyncResult: System.IAsyncResult) -> str: ...
    @overload
    def IdentitySearchAsync(
        self,
        StrKey: str,
        idOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.IdentitySearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
    ) -> None: ...
    @overload
    def IdentitySearchAsync(
        self,
        StrKey: str,
        idOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.IdentitySearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
        userState: Any,
    ) -> None: ...
    def EndGetAssayDescription(
        self,
        asyncResult: System.IAsyncResult,
        DataBlob: Agilent.MassSpectrometry.DataAnalysis.MFS.DataBlobType,
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.AssayDescriptionType: ...
    def InputStructure(
        self,
        structure: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
    ) -> str: ...
    def EndInputStructure(self, asyncResult: System.IAsyncResult) -> str: ...
    def IDExchange(
        self,
        InputListKey: str,
        Operation: Agilent.MassSpectrometry.DataAnalysis.MFS.IDOperationType,
        OutputType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        OutputSourceName: str,
        OutputFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.IDOutputFormatType,
        ToWebEnv: str,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        DownloadKey: str,
    ) -> str: ...
    def BeginGetStandardizedCID(
        self, StrKey: str, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    def IdentitySearch(
        self,
        StrKey: str,
        idOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.IdentitySearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
    ) -> str: ...
    def EndGetListItemsCount(self, asyncResult: System.IAsyncResult) -> int: ...
    def BeginGetEntrezKey(
        self, ListKey: str, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    @overload
    def GetAssayColumnDescriptionAsync(
        self,
        AID: int,
        Heading: Agilent.MassSpectrometry.DataAnalysis.MFS.HeadingType,
        TID: int,
        TIDSpecified: bool,
    ) -> None: ...
    @overload
    def GetAssayColumnDescriptionAsync(
        self,
        AID: int,
        Heading: Agilent.MassSpectrometry.DataAnalysis.MFS.HeadingType,
        TID: int,
        TIDSpecified: bool,
        userState: Any,
    ) -> None: ...
    @overload
    def GetAssayDescriptionAsync(
        self,
        AID: int,
        GetVersion: bool,
        GetVersionSpecified: bool,
        GetCounts: bool,
        GetCountsSpecified: bool,
        GetFullDataBlob: bool,
        GetFullDataBlobSpecified: bool,
        eFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        eFormatSpecified: bool,
    ) -> None: ...
    @overload
    def GetAssayDescriptionAsync(
        self,
        AID: int,
        GetVersion: bool,
        GetVersionSpecified: bool,
        GetCounts: bool,
        GetCountsSpecified: bool,
        GetFullDataBlob: bool,
        GetFullDataBlobSpecified: bool,
        eFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        eFormatSpecified: bool,
        userState: Any,
    ) -> None: ...
    def SubstructureSearch(
        self,
        StrKey: str,
        ssOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.StructureSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
    ) -> str: ...
    def ScoreMatrix(
        self,
        ListKey: str,
        SecondaryListKey: str,
        ScoreType: Agilent.MassSpectrometry.DataAnalysis.MFS.ScoreTypeType,
        MatrixFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.MatrixFormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        N3DConformers: int,
        N3DConformersSpecified: bool,
        No3DParent: bool,
        No3DParentSpecified: bool,
    ) -> str: ...
    def BeginGetStandardizedStructureBase64(
        self,
        StrKey: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    @overload
    def InputStructureAsync(
        self,
        structure: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
    ) -> None: ...
    @overload
    def InputStructureAsync(
        self,
        structure: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        userState: Any,
    ) -> None: ...
    @overload
    def AssayDownloadAsync(
        self,
        AssayKey: str,
        AssayFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayFormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
    ) -> None: ...
    @overload
    def AssayDownloadAsync(
        self,
        AssayKey: str,
        AssayFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayFormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        userState: Any,
    ) -> None: ...
    def BeginGetAssayDescription(
        self,
        AID: int,
        GetVersion: bool,
        GetVersionSpecified: bool,
        GetCounts: bool,
        GetCountsSpecified: bool,
        GetFullDataBlob: bool,
        GetFullDataBlobSpecified: bool,
        eFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        eFormatSpecified: bool,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def CancelAsync(self, userState: Any) -> None: ...
    def EndGetIDList(self, asyncResult: System.IAsyncResult) -> List[int]: ...
    @overload
    def GetStandardizedStructureBase64Async(
        self, StrKey: str, format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType
    ) -> None: ...
    @overload
    def GetStandardizedStructureBase64Async(
        self,
        StrKey: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        userState: Any,
    ) -> None: ...
    def EndSimilaritySearch2D(self, asyncResult: System.IAsyncResult) -> str: ...
    def BeginSuperstructureSearch(
        self,
        StrKey: str,
        ssOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.StructureSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def EndGetEntrezUrl(self, asyncResult: System.IAsyncResult) -> str: ...
    def EndInputEntrez(self, asyncResult: System.IAsyncResult) -> str: ...
    def BeginInputList(
        self,
        ids: List[int],
        idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def EndGetAssayColumnDescriptions(
        self, asyncResult: System.IAsyncResult
    ) -> List[Agilent.MassSpectrometry.DataAnalysis.MFS.ColumnDescriptionType]: ...
    def SuperstructureSearch(
        self,
        StrKey: str,
        ssOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.StructureSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
    ) -> str: ...
    def BeginDownload(
        self,
        ListKey: str,
        eFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        Use3D: bool,
        Use3DSpecified: bool,
        N3DConformers: int,
        N3DConformersSpecified: bool,
        SynchronousSingleRecord: bool,
        SynchronousSingleRecordSpecified: bool,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    @overload
    def InputAssayAsync(
        self,
        AID: int,
        Columns: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayColumnsType,
        ListKeyTIDs: str,
        ListKeySCIDs: str,
        OutcomeFilter: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayOutcomeFilterType,
        OutcomeFilterSpecified: bool,
    ) -> None: ...
    @overload
    def InputAssayAsync(
        self,
        AID: int,
        Columns: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayColumnsType,
        ListKeyTIDs: str,
        ListKeySCIDs: str,
        OutcomeFilter: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayOutcomeFilterType,
        OutcomeFilterSpecified: bool,
        userState: Any,
    ) -> None: ...
    def BeginGetListItemsCount(
        self, ListKey: str, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    @overload
    def GetEntrezKeyAsync(self, ListKey: str) -> None: ...
    @overload
    def GetEntrezKeyAsync(self, ListKey: str, userState: Any) -> None: ...
    def GetEntrezUrl(
        self, EntrezKey: Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey
    ) -> str: ...
    def GetOperationStatus(
        self, AnyKey: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType: ...
    def EndIDExchange(
        self, asyncResult: System.IAsyncResult, DownloadKey: str
    ) -> str: ...
    @overload
    def InputListStringAsync(
        self,
        strids: List[str],
        idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        SourceName: str,
    ) -> None: ...
    @overload
    def InputListStringAsync(
        self,
        strids: List[str],
        idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        SourceName: str,
        userState: Any,
    ) -> None: ...
    def BeginGetStandardizedStructure(
        self,
        StrKey: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def GetEntrezKey(
        self, ListKey: str
    ) -> Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey: ...
    def BeginInputAssay(
        self,
        AID: int,
        Columns: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayColumnsType,
        ListKeyTIDs: str,
        ListKeySCIDs: str,
        OutcomeFilter: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayOutcomeFilterType,
        OutcomeFilterSpecified: bool,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def InputListString(
        self,
        strids: List[str],
        idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        SourceName: str,
    ) -> str: ...
    def GetIDList(
        self,
        ListKey: str,
        Start: int,
        StartSpecified: bool,
        Count: int,
        CountSpecified: bool,
    ) -> List[int]: ...
    @overload
    def GetEntrezUrlAsync(
        self, EntrezKey: Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey
    ) -> None: ...
    @overload
    def GetEntrezUrlAsync(
        self,
        EntrezKey: Agilent.MassSpectrometry.DataAnalysis.MFS.EntrezKey,
        userState: Any,
    ) -> None: ...
    def EndGetStandardizedStructureBase64(
        self, asyncResult: System.IAsyncResult
    ) -> List[int]: ...
    def BeginGetOperationStatus(
        self, AnyKey: str, callback: System.AsyncCallback, asyncState: Any
    ) -> System.IAsyncResult: ...
    @overload
    def ScoreMatrixAsync(
        self,
        ListKey: str,
        SecondaryListKey: str,
        ScoreType: Agilent.MassSpectrometry.DataAnalysis.MFS.ScoreTypeType,
        MatrixFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.MatrixFormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        N3DConformers: int,
        N3DConformersSpecified: bool,
        No3DParent: bool,
        No3DParentSpecified: bool,
    ) -> None: ...
    @overload
    def ScoreMatrixAsync(
        self,
        ListKey: str,
        SecondaryListKey: str,
        ScoreType: Agilent.MassSpectrometry.DataAnalysis.MFS.ScoreTypeType,
        MatrixFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.MatrixFormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        N3DConformers: int,
        N3DConformersSpecified: bool,
        No3DParent: bool,
        No3DParentSpecified: bool,
        userState: Any,
    ) -> None: ...
    def InputListText(
        self, ids: str, idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType
    ) -> str: ...
    @overload
    def GetStatusMessageAsync(self, AnyKey: str) -> None: ...
    @overload
    def GetStatusMessageAsync(self, AnyKey: str, userState: Any) -> None: ...
    def EndAssayDownload(self, asyncResult: System.IAsyncResult) -> str: ...
    @overload
    def MFSearchAsync(
        self,
        MF: str,
        mfOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.MFSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
    ) -> None: ...
    @overload
    def MFSearchAsync(
        self,
        MF: str,
        mfOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.MFSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
        userState: Any,
    ) -> None: ...
    def EndInputStructureBase64(self, asyncResult: System.IAsyncResult) -> str: ...
    def EndIdentitySearch(self, asyncResult: System.IAsyncResult) -> str: ...
    def BeginMFSearch(
        self,
        MF: str,
        mfOptions: Agilent.MassSpectrometry.DataAnalysis.MFS.MFSearchOptions,
        limits: Agilent.MassSpectrometry.DataAnalysis.MFS.LimitsType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def BeginScoreMatrix(
        self,
        ListKey: str,
        SecondaryListKey: str,
        ScoreType: Agilent.MassSpectrometry.DataAnalysis.MFS.ScoreTypeType,
        MatrixFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.MatrixFormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        N3DConformers: int,
        N3DConformersSpecified: bool,
        No3DParent: bool,
        No3DParentSpecified: bool,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def BeginInputListText(
        self,
        ids: str,
        idType: Agilent.MassSpectrometry.DataAnalysis.MFS.PCIDType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def EndScoreMatrix(self, asyncResult: System.IAsyncResult) -> str: ...
    def AssayDownload(
        self,
        AssayKey: str,
        AssayFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.AssayFormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
    ) -> str: ...
    def BeginInputStructure(
        self,
        structure: str,
        format: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        callback: System.AsyncCallback,
        asyncState: Any,
    ) -> System.IAsyncResult: ...
    def Download(
        self,
        ListKey: str,
        eFormat: Agilent.MassSpectrometry.DataAnalysis.MFS.FormatType,
        eCompress: Agilent.MassSpectrometry.DataAnalysis.MFS.CompressType,
        eCompressSpecified: bool,
        Use3D: bool,
        Use3DSpecified: bool,
        N3DConformers: int,
        N3DConformersSpecified: bool,
        SynchronousSingleRecord: bool,
        SynchronousSingleRecordSpecified: bool,
        DataBlob: Agilent.MassSpectrometry.DataAnalysis.MFS.DataBlobType,
    ) -> str: ...

    AssayDownloadCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.AssayDownloadCompletedEventHandler
    )  # Event
    DownloadCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.DownloadCompletedEventHandler
    )  # Event
    GetAssayColumnDescriptionCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetAssayColumnDescriptionCompletedEventHandler
    )  # Event
    GetAssayColumnDescriptionsCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetAssayColumnDescriptionsCompletedEventHandler
    )  # Event
    GetAssayDescriptionCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetAssayDescriptionCompletedEventHandler
    )  # Event
    GetDownloadUrlCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetDownloadUrlCompletedEventHandler
    )  # Event
    GetEntrezKeyCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetEntrezKeyCompletedEventHandler
    )  # Event
    GetEntrezUrlCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetEntrezUrlCompletedEventHandler
    )  # Event
    GetIDListCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetIDListCompletedEventHandler
    )  # Event
    GetListItemsCountCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetListItemsCountCompletedEventHandler
    )  # Event
    GetOperationStatusCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetOperationStatusCompletedEventHandler
    )  # Event
    GetStandardizedCIDCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetStandardizedCIDCompletedEventHandler
    )  # Event
    GetStandardizedStructureBase64Completed: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetStandardizedStructureBase64CompletedEventHandler
    )  # Event
    GetStandardizedStructureCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetStandardizedStructureCompletedEventHandler
    )  # Event
    GetStatusMessageCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.GetStatusMessageCompletedEventHandler
    )  # Event
    IDExchangeCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IDExchangeCompletedEventHandler
    )  # Event
    IdentitySearchCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.IdentitySearchCompletedEventHandler
    )  # Event
    InputAssayCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.InputAssayCompletedEventHandler
    )  # Event
    InputEntrezCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.InputEntrezCompletedEventHandler
    )  # Event
    InputListCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.InputListCompletedEventHandler
    )  # Event
    InputListStringCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.InputListStringCompletedEventHandler
    )  # Event
    InputListTextCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.InputListTextCompletedEventHandler
    )  # Event
    InputStructureBase64Completed: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.InputStructureBase64CompletedEventHandler
    )  # Event
    InputStructureCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.InputStructureCompletedEventHandler
    )  # Event
    MFSearchCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.MFSearchCompletedEventHandler
    )  # Event
    ScoreMatrixCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.ScoreMatrixCompletedEventHandler
    )  # Event
    SimilaritySearch2DCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.SimilaritySearch2DCompletedEventHandler
    )  # Event
    StandardizeCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.StandardizeCompletedEventHandler
    )  # Event
    SubstructureSearchCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.SubstructureSearchCompletedEventHandler
    )  # Event
    SuperstructureSearchCompleted: (
        Agilent.MassSpectrometry.DataAnalysis.MFS.SuperstructureSearchCompletedEventHandler
    )  # Event

class ScoreMatrixCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class ScoreMatrixCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.ScoreMatrixCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.ScoreMatrixCompletedEventArgs,
    ) -> None: ...

class ScoreTypeType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eScoreType_FeatureOpt3D: Agilent.MassSpectrometry.DataAnalysis.MFS.ScoreTypeType = (
        ...
    )  # static # readonly
    eScoreType_ShapeOpt3D: Agilent.MassSpectrometry.DataAnalysis.MFS.ScoreTypeType = (
        ...
    )  # static # readonly
    eScoreType_Sim2DSubs: Agilent.MassSpectrometry.DataAnalysis.MFS.ScoreTypeType = (
        ...
    )  # static # readonly

class SearchByFormula2CompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: List[str]  # readonly

class SearchByFormula2CompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByFormula2CompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByFormula2CompletedEventArgs,
    ) -> None: ...

class SearchByFormulaAsync1CompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class SearchByFormulaAsync1CompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByFormulaAsync1CompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByFormulaAsync1CompletedEventArgs,
    ) -> None: ...

class SearchByFormulaCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: List[str]  # readonly

class SearchByFormulaCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByFormulaCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByFormulaCompletedEventArgs,
    ) -> None: ...

class SearchByMass2CompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: List[str]  # readonly

class SearchByMass2CompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByMass2CompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByMass2CompletedEventArgs,
    ) -> None: ...

class SearchByMassAsync1CompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class SearchByMassAsync1CompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByMassAsync1CompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByMassAsync1CompletedEventArgs,
    ) -> None: ...

class SearchByMassCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: List[str]  # readonly

class SearchByMassCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByMassCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SearchByMassCompletedEventArgs,
    ) -> None: ...

class SimilaritySearch2DCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class SimilaritySearch2DCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SimilaritySearch2DCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SimilaritySearch2DCompletedEventArgs,
    ) -> None: ...

class SimilaritySearchOptions:  # Class
    def __init__(self) -> None: ...

    ToWebEnv: str
    threshold: int

class StandardizeCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    StrKey: str  # readonly

class StandardizeCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.StandardizeCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.StandardizeCompletedEventArgs,
    ) -> None: ...

class StatusType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eStatus_DataError: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType = (
        ...
    )  # static # readonly
    eStatus_HitLimit: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType = (
        ...
    )  # static # readonly
    eStatus_InputError: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType = (
        ...
    )  # static # readonly
    eStatus_Queued: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType = (
        ...
    )  # static # readonly
    eStatus_Running: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType = (
        ...
    )  # static # readonly
    eStatus_ServerError: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType = (
        ...
    )  # static # readonly
    eStatus_Stopped: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType = (
        ...
    )  # static # readonly
    eStatus_Success: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType = (
        ...
    )  # static # readonly
    eStatus_TimeLimit: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType = (
        ...
    )  # static # readonly
    eStatus_Unknown: Agilent.MassSpectrometry.DataAnalysis.MFS.StatusType = (
        ...
    )  # static # readonly

class StereoType(
    System.IConvertible, System.IComparable, System.IFormattable
):  # Struct
    eStereo_Exact: Agilent.MassSpectrometry.DataAnalysis.MFS.StereoType = (
        ...
    )  # static # readonly
    eStereo_Ignore: Agilent.MassSpectrometry.DataAnalysis.MFS.StereoType = (
        ...
    )  # static # readonly
    eStereo_NonConflicting: Agilent.MassSpectrometry.DataAnalysis.MFS.StereoType = (
        ...
    )  # static # readonly
    eStereo_Relative: Agilent.MassSpectrometry.DataAnalysis.MFS.StereoType = (
        ...
    )  # static # readonly

class StructureSearchOptions:  # Class
    def __init__(self) -> None: ...

    ChainsMatchRings: bool
    ChainsMatchRingsSpecified: bool
    MatchCharges: bool
    MatchChargesSpecified: bool
    MatchIsotopes: bool
    MatchIsotopesSpecified: bool
    MatchTautomers: bool
    MatchTautomersSpecified: bool
    RingsNotEmbedded: bool
    RingsNotEmbeddedSpecified: bool
    SingeDoubleBondsMatch: bool
    SingeDoubleBondsMatchSpecified: bool
    StripHydrogen: bool
    StripHydrogenSpecified: bool
    ToWebEnv: str
    eStereo: Agilent.MassSpectrometry.DataAnalysis.MFS.StereoType
    eStereoSpecified: bool

class SubstructureSearchCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class SubstructureSearchCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SubstructureSearchCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SubstructureSearchCompletedEventArgs,
    ) -> None: ...

class SuperstructureSearchCompletedEventArgs(
    System.ComponentModel.AsyncCompletedEventArgs
):  # Class
    Result: str  # readonly

class SuperstructureSearchCompletedEventHandler(
    System.MulticastDelegate,
    System.ICloneable,
    System.Runtime.Serialization.ISerializable,
):  # Class
    def __init__(self, object: Any, method: System.IntPtr) -> None: ...
    def EndInvoke(self, result: System.IAsyncResult) -> None: ...
    def BeginInvoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SuperstructureSearchCompletedEventArgs,
        callback: System.AsyncCallback,
        object: Any,
    ) -> System.IAsyncResult: ...
    def Invoke(
        self,
        sender: Any,
        e: Agilent.MassSpectrometry.DataAnalysis.MFS.SuperstructureSearchCompletedEventArgs,
    ) -> None: ...

class TestedConcentrationType:  # Class
    def __init__(self) -> None: ...

    Concentration: float
    Unit: str
