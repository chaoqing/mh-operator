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

from . import MolecularStructure

# Stubs for namespace: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure

class BottomHalfDiamond(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class Circle(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class DiagonalSquare(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class Diamond(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class GlycanGlycoCTParser(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanParser
):  # Class
    def __init__(self) -> None: ...
    def ParseStructureSpec(
        self, structureSpec: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree
    ): ...

class GlycanKeggParser(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanParser
):  # Class
    def __init__(self) -> None: ...
    def ParseStructureSpec(
        self, structureSpec: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree
    ): ...

class GlycanLinucsParser(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanParser
):  # Class
    def __init__(self) -> None: ...
    def ParseStructureSpec(
        self, structureSpec: str
    ) -> (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree
    ): ...

class GlycanShape(object):  # Interface
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class GlycanStructure(
    Agilent.MassSpectrometry.DataAnalysis.IMolecularStructure, MolecularStructure
):  # Class
    def __init__(self) -> None: ...

    pen: System.Drawing.Pen  # static

    Direction: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanStructure.DrawingOrientation
    )
    GlycanStructureContextMenu: System.Windows.Forms.ContextMenu  # readonly
    ShowLinkage: bool
    StructureSpec: str
    UseSymbols: bool

    def ReadStructureSpecFromFile(self, filename: str) -> None: ...
    def ReadStructureSpecFromStream(self, sr: System.IO.TextReader) -> None: ...
    def PaintStructure(
        self, g: System.Drawing.Graphics, ctrl: System.Windows.Forms.Control
    ) -> None: ...

    # Nested Types

    class DrawingOrientation(
        System.IConvertible, System.IComparable, System.IFormattable
    ):  # Struct
        BottomToTop: (
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanStructure.DrawingOrientation
        ) = ...  # static # readonly
        LeftToRight: (
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanStructure.DrawingOrientation
        ) = ...  # static # readonly
        RightToLeft: (
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanStructure.DrawingOrientation
        ) = ...  # static # readonly
        TopToBottom: (
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanStructure.DrawingOrientation
        ) = ...  # static # readonly

class GlycanSymbol:  # Class
    def __init__(
        self,
        shape: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape,
        color: System.Drawing.Color,
        pen: System.Drawing.Pen,
    ) -> None: ...

    Color: System.Drawing.Color
    Label: str
    Pen: System.Drawing.Pen
    Shape: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
    )

    def Draw(
        self, g: System.Drawing.Graphics, rect: System.Drawing.Rectangle, rotation: int
    ) -> None: ...

class GlycanTree:  # Class
    def __init__(self) -> None: ...

    AmbiguousNode: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanNode
    )
    Edges: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanEdge
    ]
    GlycanId: str
    HeadNode: (
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanNode
    )
    Nodes: System.Collections.Generic.List[
        Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanNode
    ]
    ParseError: bool

    # Nested Types

    class GlycanEdge:  # Class
        def __init__(self) -> None: ...

        ChildLinkage: str
        ChildNode: (
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanNode
        )
        ParentLinkage: str
        ParentNode: (
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanNode
        )

    class GlycanNode:  # Class
        def __init__(self) -> None: ...

        BottomLabel: str
        Bounds: System.Drawing.Rectangle
        Children: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanNode
        ]
        Id: str
        Name: str
        ParentEdge: (
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanEdge
        )
        Parents: System.Collections.Generic.List[
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanNode
        ]
        RightAngleOnly: bool
        SortKey: str
        Symbol: (
            Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanSymbol
        )
        TopLabel: str

        def InsertNodeBefore(
            self,
            child: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanNode,
            tree: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree,
        ) -> None: ...
        def InsertNodeAfter(
            self,
            parent: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree.GlycanNode,
            tree: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree,
            linkage: str,
        ) -> None: ...
        def RemoveNode(
            self,
            tree: Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanTree,
        ) -> None: ...
        def RemoveLinkage(self, str: str, showLinkage: bool) -> str: ...

class GlycanUtils:  # Class
    def __init__(self) -> None: ...

    pen: System.Drawing.Pen  # static

    @staticmethod
    def stripName(s: str) -> str: ...

class LeftBracket(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class LeftCurlyBracket(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class LeftHalfDiamond(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class Pentangle(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class RightBracket(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class RightHalfDiamond(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class RotatedTriangle(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class Square(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class Squiggle(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class SquiggleCircle(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class Star(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class TopHalfDiamond(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...

class Triangle(
    Agilent.MassSpectrometry.DataAnalysis.MetaboliteID.GlycanStructure.GlycanShape
):  # Class
    def __init__(self) -> None: ...
    def Draw(
        self,
        g: System.Drawing.Graphics,
        c: System.Drawing.Color,
        pen: System.Drawing.Pen,
        label: str,
        rect: System.Drawing.Rectangle,
        rotation: int,
    ) -> None: ...
    def NeedsRotation(self) -> bool: ...
