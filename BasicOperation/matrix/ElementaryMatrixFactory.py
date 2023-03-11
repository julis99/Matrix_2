from BasicOperation.complex.ComplexNum import ComplexNum as Complex
from BasicOperation.matrix.MTX_input import MATRIX_reduceToInt as redToInt
from BasicOperation.matrix.Matrix import Matrix

from Other.Exceptions import *

class ElementaryMatrixFactory:
    def __init__(self, initiator: float | Complex | int):
        self.createsFloats = isinstance(initiator, float)
        self.createsComplex = isinstance(initiator, Complex)
        self.createsInt = isinstance(initiator, int)
        if self.createsInt:
            self.modulus = initiator
        else:
            self.modulus = 0

    def createIdentityMatrix(self, size: int) -> Matrix:
        id = Matrix(size, size, isComplex=self.createsComplex)
        for idx in range(size):
            if self.createsComplex:
                id.changeElement(idx, idx, Complex(1, 0))
            else:
                id.changeElement(idx, idx, 1.0)
        if self.createsInt:
            return redToInt(id)
        return id

    def createAdditionMatrix(self, size: int, rowA: int, rowB: int, scale: float | Complex | int) -> Matrix:
        """creates a Matrix which adds rowB scale Times to rowA
        :raises NotCompatibleException when scale is not the right type"""
        if (isinstance(scale, Complex) and not self.createsComplex):
            raise NotCompatibleException
        if self.createsComplex and not isinstance(scale, Complex):
            scale = Complex(scale, 0)
        if self.createsInt and not [0, 1].__contains__(self.modulus):
            scale %= self.modulus
        add = self.createIdentityMatrix(size)
        add.changeElement(rowA, rowB, scale)
        if self.createsInt:
            return redToInt(add)
        return add

    def createSwitchMatrix(self, size: int, rowA: int, rowB: int) -> Matrix:
        switch = self.createIdentityMatrix(size)
        if self.createsComplex:
            switch.changeElement(rowA, rowA, Complex(0, 0))
            switch.changeElement(rowB, rowB, Complex(0, 0))
            switch.changeElement(rowA, rowB, Complex(1, 0))
            switch.changeElement(rowB, rowA, Complex(1, 0))
            return switch
        switch.changeElement(rowA, rowA, 0)
        switch.changeElement(rowB, rowB, 0)
        switch.changeElement(rowA, rowB, 1)
        switch.changeElement(rowB, rowA, 1)
        return switch

    def createMultiplicationMatrix(self, size: int, row: int, unit: float | Complex | int) -> Matrix:
        """:raises NotCompatibleException when unit isn't the right type"""
        if (isinstance(unit, Complex) and not self.createsComplex):
            raise NotCompatibleException
        mult = self.createIdentityMatrix(size)
        if self.createsComplex and not isinstance(unit, Complex):
            unit = Complex(unit, 0)
        if self.createsInt and not [0, 1].__contains__(self.modulus):
            unit %= self.modulus
        mult.changeElement(row, row, unit)
        if self.createsInt:
            return redToInt(mult)
        return mult


