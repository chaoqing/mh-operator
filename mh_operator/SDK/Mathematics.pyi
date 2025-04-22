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

# Discovered Generic TypeVars:
T = TypeVar("T")
from .Agilent.MassSpectrometry.DataAnalysis import IFunction

# Stubs for namespace: Mathematics

class BinarySearch:  # Class
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def GetIndexLeftOf(list: List[Any], target: System.IComparable) -> int: ...
    @overload
    @staticmethod
    def GetIndexLeftOf(
        list: List[Any], start: int, end: int, target: System.IComparable
    ) -> int: ...

class Clustering:  # Class
    def __init__(self) -> None: ...

    NumClusters: int  # readonly

    def GetCluster(self, iCluster: int) -> List[int]: ...
    def Run(self) -> None: ...

class ClusteringMinSpanningTree(Mathematics.Clustering):  # Class
    def __init__(self, disimilarity: Mathematics.MatrixSymmetric) -> None: ...

    MinNumVectorForAuto: int  # static # readonly
    TheProjection: Mathematics.ClusteringMinSpanningTree.Projection  # readonly

    @overload
    def Run(self, iNumClusterDesired: int, iMinClusterSize: int) -> None: ...
    @overload
    def Run(self) -> None: ...

    # Nested Types

    class Projection:  # Class
        def __init__(
            self,
            engine: Mathematics.ClusteringMinSpanningTree,
            distances: Mathematics.MatrixSymmetric,
        ) -> None: ...
        def GetNodes(
            self,
        ) -> List[Mathematics.ClusteringMinSpanningTree.Projection.Node]: ...
        def GetBounds(
            self, fMinX: float, fMaxX: float, fMinY: float, fMaxY: float
        ) -> None: ...
        def GetEdges(
            self,
        ) -> List[Mathematics.ClusteringMinSpanningTree.Projection.Edge]: ...

        # Nested Types

        class Edge:  # Class
            def __init__(
                self,
                p1: Mathematics.ClusteringMinSpanningTree.Projection.Point,
                p2: Mathematics.ClusteringMinSpanningTree.Projection.Point,
                iTreeID: int,
            ) -> None: ...

            m_iTreeID: int
            m_node1: Mathematics.ClusteringMinSpanningTree.Projection.Point
            m_node2: Mathematics.ClusteringMinSpanningTree.Projection.Point

        class Node:  # Class
            def __init__(
                self,
                iTreeID: int,
                iObjectID: int,
                p: Mathematics.ClusteringMinSpanningTree.Projection.Point,
            ) -> None: ...

            m_iObjectID: int
            m_iTreeID: int
            m_point: Mathematics.ClusteringMinSpanningTree.Projection.Point

        class Point:  # Struct
            def __init__(self, fX: float, fY: float) -> None: ...

            m_fX: float
            m_fY: float

class ClusteringSequential:  # Class
    def __init__(
        self,
        input: List[Mathematics.ClusteringSequential.IElement],
        thresholds: List[IFunction],
    ) -> None: ...

    ClusterCount: int  # readonly

    @staticmethod
    def Distance(
        v1: Mathematics.Vector, v2: Mathematics.Vector, factors: Mathematics.Vector
    ) -> float: ...
    def GetCluster(
        self, clusterIndex: int
    ) -> List[Mathematics.ClusteringSequential.IElement]: ...
    def ClearClusterData(self, clusterIndex: int) -> None: ...
    def Run(self) -> None: ...

    # Nested Types

    class IElement(object):  # Interface
        DataDimension: int  # readonly
        Weight: float  # readonly

        def GetData(self, dimensionIndex: int) -> float: ...

class ClusteringSequential2dGrid(Mathematics.ClusteringSequential):  # Class
    def __init__(
        self,
        input: List[Mathematics.ClusteringSequential.IElement],
        thresholds: List[IFunction],
        ranges: List[Mathematics.RangeDouble],
        gridSizes: List[float],
    ) -> None: ...
    def Run(self) -> None: ...

class FFTSpectrum:  # Class
    @overload
    def __init__(self, aTimeSeries: List[float]) -> None: ...
    @overload
    def __init__(self, spectrum: List[float], timeSeriesLength: int) -> None: ...
    def LowPass(self, dT1: float, dT2: float) -> None: ...
    def GetTimeSeries(self) -> List[float]: ...
    def BandPass(self, dT1: float, dT2: float, dT3: float, dT4: float) -> None: ...

class FunctionXml:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def FromXml(siblings: System.Xml.XmlNodeList, name: str) -> IFunction: ...
    @staticmethod
    def ToXml(
        doc: System.Xml.XmlDocument, function: IFunction, name: str
    ) -> System.Xml.XmlElement: ...

class Graph:  # Class
    def __init__(self) -> None: ...

    AveSqDev: float  # readonly
    AverageWeight: float  # readonly

    @staticmethod
    def FindEdge(
        n1: Mathematics.Graph.Node, n2: Mathematics.Graph.Node
    ) -> Mathematics.Graph.Edge: ...

    # Nested Types

    class Edge:  # Class
        def __init__(
            self,
            node1: Mathematics.Graph.Node,
            node2: Mathematics.Graph.Node,
            fWeight: float,
        ) -> None: ...

        m_fWeight: float
        m_node1: Mathematics.Graph.Node
        m_node2: Mathematics.Graph.Node

    class Node:  # Class
        def __init__(self, iID: int) -> None: ...

        m_iID: int
        m_lstEdges: System.Collections.Generic.List[Mathematics.Graph.Edge]

        ID: int  # readonly

class HuffmanCompressedData(Generic[T]):  # Class
    @overload
    def __init__(self, symbolStream: List[T]) -> None: ...
    @overload
    def __init__(
        self,
        compressedData: List[int],
        unpacker: Mathematics.HuffmanCompressedData.UnpackSymbols[T],
    ) -> None: ...
    def GetCompressedData(
        self, packer: Mathematics.HuffmanCompressedData.PackSymbols[T]
    ) -> List[int]: ...
    def RetrieveOriginalData(self) -> List[T]: ...

    # Nested Types

    class PackSymbols(
        System.MulticastDelegate,
        Generic[T],
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> List[int]: ...
        def BeginInvoke(
            self, data: List[T], callback: System.AsyncCallback, object: Any
        ) -> System.IAsyncResult: ...
        def Invoke(self, data: List[T]) -> List[int]: ...

    class UnpackSymbols(
        System.MulticastDelegate,
        Generic[T],
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, offset: int, result: System.IAsyncResult) -> List[T]: ...
        def BeginInvoke(
            self,
            compressed: List[int],
            offset: int,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(self, compressed: List[int], offset: int) -> List[T]: ...

class HuffmanCompressor(Generic[T]):  # Class
    def __init__(self) -> None: ...
    def GetCompressedData(
        self,
        symbolStream: List[T],
        packer: Mathematics.HuffmanCompressor.PackSymbols[T],
    ) -> List[int]: ...
    def GetUncompressedData(
        self,
        compressedData: List[int],
        offset: int,
        unpacker: Mathematics.HuffmanCompressor.UnpackSymbols[T],
    ) -> List[T]: ...
    def Compress(self, symbolStream: List[T]) -> None: ...

    # Nested Types

    class PackSymbols(
        System.MulticastDelegate,
        Generic[T],
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, result: System.IAsyncResult) -> List[int]: ...
        def BeginInvoke(
            self, data: List[T], callback: System.AsyncCallback, object: Any
        ) -> System.IAsyncResult: ...
        def Invoke(self, data: List[T]) -> List[int]: ...

    class UnpackSymbols(
        System.MulticastDelegate,
        Generic[T],
        System.ICloneable,
        System.Runtime.Serialization.ISerializable,
    ):  # Class
        def __init__(self, object: Any, method: System.IntPtr) -> None: ...
        def EndInvoke(self, offset: int, result: System.IAsyncResult) -> List[T]: ...
        def BeginInvoke(
            self,
            compressed: List[int],
            offset: int,
            callback: System.AsyncCallback,
            object: Any,
        ) -> System.IAsyncResult: ...
        def Invoke(self, compressed: List[int], offset: int) -> List[T]: ...

class IClassifierDiscrimativeRule(object):  # Interface
    Reversed: Mathematics.IClassifierDiscrimativeRule  # readonly

    def Test(self, unknown: Mathematics.Vector) -> float: ...

class IClusteringSequentialElement(object):  # Interface
    DataDimension: int  # readonly
    Weight: float  # readonly

    def GetData(self, dimensionIndex: int) -> float: ...

class KernelVaringSmoother:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def Smooth(
        data: List[float],
        kernelProvider: Mathematics.KernelVaringSmoother.IKernelProvider,
        strength: float,
    ) -> List[float]: ...

    # Nested Types

    class IKernelProvider(object):  # Interface
        def GetKernel(
            self, dataIndex: int, strength: float, kernelStartOffset: int
        ) -> List[float]: ...

class ListCompressor(Generic[T]):  # Class
    def __init__(self, frequency: Dict[T, int]) -> None: ...
    def GetCompressedData(self, symbolStream: List[T]) -> List[int]: ...
    def GetUncompressedData(self, code: List[int], offset: int) -> List[T]: ...
    def Compress(self, symbolStream: List[T]) -> None: ...

class Matrix:  # Class
    @overload
    def __init__(self, rowSize: int, colSize: int) -> None: ...
    @overload
    def __init__(
        self, rowSize: int, colSize: int, rowStart: int, colStart: int
    ) -> None: ...

    ColSize: int  # readonly
    ColStart: int  # readonly
    def __getitem__(self, row: int, col: int) -> float: ...
    def __setitem__(self, row: int, col: int, value_: float) -> None: ...
    RowSize: int  # readonly
    RowStart: int  # readonly

    def SwapRow(self, row1: int, row2: int) -> None: ...
    def SingularValueDecomposition(
        self, U: Mathematics.Matrix, V: Mathematics.MatrixSquare, w: Mathematics.Vector
    ) -> None: ...
    def IsInSameSpace(self, m: Mathematics.Matrix) -> bool: ...
    def Clone(self) -> Mathematics.Matrix: ...
    def SwapCol(self, col1: int, col2: int) -> None: ...

class MatrixSquare(Mathematics.Matrix):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, rowStart: int, colStart: int) -> None: ...

    DiagonalRMS: float  # readonly
    IdentifyMatrix: Mathematics.MatrixSquare  # readonly
    Size: int  # readonly

    def InverseDot(self, b: Mathematics.Vector) -> Mathematics.Vector: ...

class MatrixSymmetric(Mathematics.MatrixSquare):  # Class
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, rowStart: int) -> None: ...
    def __getitem__(self, row: int, col: int) -> float: ...
    def __setitem__(self, row: int, col: int, value_: float) -> None: ...
    @overload
    @staticmethod
    def NormMatrix(A: Mathematics.Matrix) -> Mathematics.MatrixSymmetric: ...
    @overload
    @staticmethod
    def NormMatrix(v: Mathematics.Vector) -> Mathematics.MatrixSymmetric: ...
    def InverseDot(self, b: Mathematics.Vector) -> Mathematics.Vector: ...

class MinSpanningTree(Mathematics.Graph):  # Class
    @overload
    def __init__(self, disimilarity: Mathematics.MatrixSymmetric) -> None: ...
    @overload
    def __init__(self, n: Mathematics.Graph.Node) -> None: ...

    Edges: System.Collections.Generic.List[Mathematics.Graph.Edge]  # readonly
    Nodes: System.Collections.Generic.List[Mathematics.Graph.Node]  # readonly
    NumNodes: int  # readonly

    @staticmethod
    def CollectNeighbors(
        edge: Mathematics.Graph.Edge,
        iMaxStepsForNeighbor: int,
        lstNeighborsInBranch1: System.Collections.Generic.List[
            System.Collections.Generic.List[Mathematics.Graph.Edge]
        ],
        lstNeighborsInBranch2: System.Collections.Generic.List[
            System.Collections.Generic.List[Mathematics.Graph.Edge]
        ],
    ) -> None: ...

class PrincipalComponentAnalysis:  # Class
    def __init__(self, vectors: List[Mathematics.Vector]) -> None: ...

    SingularValues: List[float]  # readonly

    def GetVariableLoadings(self, variableIndex: int) -> List[float]: ...
    def Run(self) -> None: ...
    def GetScores(self, observationIndex: int) -> List[float]: ...
    def GetLoadingVector(self, componentIndex: int) -> List[float]: ...

class RangeDouble:  # Struct
    def __init__(self, iMin: float, iMax: float) -> None: ...

    Max: float  # readonly
    Mid: float  # readonly
    Min: float  # readonly
    Span: float  # readonly

    @staticmethod
    def Expands(
        r1: Mathematics.RangeDouble, r2: Mathematics.RangeDouble
    ) -> Mathematics.RangeDouble: ...
    def GetHashCode(self) -> int: ...
    @overload
    def Includes(self, r: Mathematics.RangeDouble) -> bool: ...
    @overload
    def Includes(self, d: float) -> bool: ...
    def Equals(self, obj: Any) -> bool: ...

class RangeInt:  # Struct
    def __init__(self, iMin: int, iMax: int) -> None: ...

    InvalidValue: Mathematics.RangeInt  # static # readonly
    Max: int  # readonly
    Mid: int  # readonly
    Min: int  # readonly
    Span: int  # readonly

    @staticmethod
    def Expands(
        r1: Mathematics.RangeInt, r2: Mathematics.RangeInt
    ) -> Mathematics.RangeInt: ...
    def GetHashCode(self) -> int: ...
    @overload
    def Includes(self, r: Mathematics.RangeInt) -> bool: ...
    @overload
    def Includes(self, i: int) -> bool: ...
    def Equals(self, obj: Any) -> bool: ...

class Regression:  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, userSpec: Mathematics.Regression.ModelSpec) -> None: ...

    ConstantZeroModel: Mathematics.Regression  # static # readonly
    def __getitem__(self, x: float) -> float: ...
    ObservationCount: int  # readonly
    Result: Mathematics.Vector  # readonly

    def Fit(self, dampingParam: float) -> None: ...
    def Clear(self) -> None: ...
    @overload
    def AddObservation(self, x: float, y: float) -> None: ...
    @overload
    def AddObservation(self, x: float, y: float, wieght: float) -> None: ...

    # Nested Types

    class ModelSpec:  # Class
        def __init__(self) -> None: ...

        equation: str
        spec: Dict[str, Any]

    class Observation:  # Struct
        def __init__(self, x: float, y: float, weight: float) -> None: ...

        Weight: float
        X: float
        Y: float

class RegressionGaussian(Mathematics.RegressionNonlinear):  # Class
    @overload
    def __init__(
        self,
        userSpe: Mathematics.Regression.ModelSpec,
        initialMode: Mathematics.Vector,
        maxIterationCount: int,
    ) -> None: ...
    @overload
    def __init__(
        self, initialMode: Mathematics.Vector, maxIterationCount: int
    ) -> None: ...

    ModelSpecification: Mathematics.Regression.ModelSpec  # static # readonly

class RegressionLegPoly(Mathematics.RegressionLinear):  # Class
    @overload
    def __init__(self, userSpec: Mathematics.Regression.ModelSpec) -> None: ...
    @overload
    def __init__(self, maxDegree: int) -> None: ...

    ModelSpecification: Mathematics.Regression.ModelSpec  # static # readonly

class RegressionLinear(Mathematics.Regression):  # Class
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, userSpec: Mathematics.Regression.ModelSpec) -> None: ...

class RegressionNonlinear(Mathematics.Regression):  # Class
    @overload
    def __init__(
        self, initialMode: Mathematics.Vector, maxIterationCount: int
    ) -> None: ...
    @overload
    def __init__(
        self,
        userSpe: Mathematics.Regression.ModelSpec,
        initialMode: Mathematics.Vector,
        maxIterationCount: int,
    ) -> None: ...

class RegressionPolynomial(Mathematics.RegressionLinear):  # Class
    @overload
    def __init__(self, userSpec: Mathematics.Regression.ModelSpec) -> None: ...
    @overload
    def __init__(self, minDegree: int, maxDegree: int) -> None: ...

    ModelSpecification: Mathematics.Regression.ModelSpec  # static # readonly

class SVMTwoClass:  # Class
    def __init__(
        self, class1: List[Mathematics.Vector], class2: List[Mathematics.Vector]
    ) -> None: ...
    def Test(self, v: Mathematics.Vector, fScore: float) -> int: ...
    def Train(self, fittingDegree: float) -> bool: ...

class SavitzkyGolayCoeffients:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def GetCoefficients(
        polynomialDegree: int, pointCountOnLeft: int, pointCountOnRight: int
    ) -> List[float]: ...

class SpecialFunction:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def IncompleteBetaFunction(fA: float, fB: float, fX: float) -> float: ...
    @staticmethod
    def LegendrePolynomial(n: int, x: float) -> float: ...
    @staticmethod
    def Gauss(x: float, A: float, x0: float, sigma: float, b: float) -> float: ...
    @staticmethod
    def SavitzkyGolay(
        maxPolynomialDegree: int, letfLength: int, rightLength: int, derivativeDeg: int
    ) -> List[float]: ...

class Statistics:  # Class
    def __init__(self) -> None: ...
    @staticmethod
    def StudentTTest(v1: List[float], v2: List[float]) -> float: ...

class SvmOverFeatured:  # Class
    def __init__(self, trainingData: List[List[Mathematics.Vector]]) -> None: ...
    def GetWVector(self, targetClassIndex: int) -> Mathematics.Vector: ...
    def GetTrainScore(self, vectorIndex: int, targetClassIndex: int) -> float: ...
    def Test(self, v: Mathematics.Vector, fScore: float) -> int: ...
    def Train(self, fFittingDegree: float) -> bool: ...
    def Sensitivity(self, targetClassIndex: int, dimentionIndex: int) -> float: ...

class Taper:  # Class
    def __init__(self, samplingX: List[float], halfTaperSpan: float) -> None: ...

    MaxTaperLength: int  # readonly

    def GetTaper(self, centerIndex: int, taperStartIndex: int) -> List[float]: ...

class Vector:  # Class
    @overload
    def __init__(self, size: int) -> None: ...
    @overload
    def __init__(self, size: int, indexStart: int) -> None: ...

    AllElements: float
    IndexStart: int  # readonly
    def __getitem__(self, index: int) -> float: ...
    def __setitem__(self, index: int, value_: float) -> None: ...
    Size: int  # readonly

    def CorelationCoefficient(self, v: Mathematics.Vector) -> float: ...
    def IsInSameSpace(self, v: Mathematics.Vector) -> bool: ...
    def Normalize(self) -> None: ...
    @staticmethod
    def MemberwiseDivide(
        v1: Mathematics.Vector, v2: Mathematics.Vector
    ) -> Mathematics.Vector: ...
    @staticmethod
    def Mapping(
        input: Mathematics.Vector, mapper: List[IFunction]
    ) -> Mathematics.Vector: ...
    @staticmethod
    def Distance(v1: Mathematics.Vector, v2: Mathematics.Vector) -> float: ...
    def Clone(self) -> Mathematics.Vector: ...
