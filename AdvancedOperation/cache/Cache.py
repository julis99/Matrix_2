from BasicOperation.matrix.Matrix import Matrix
from BasicOperation.vector.Vector import Vector
from BasicOperation.complex.ComplexNum import ComplexNum as Complex

from Other.Exceptions import *
from Other.input import FLOAT_getRangedInput, STR_getInput

class Cache:
    def __init__(self):
        self.mtxs: list[Matrix] = []
        self.vcts: list[Vector] = []

    def getMatrixList(self) -> list[Matrix]:
        return self.mtxs

    def getVectorList(self) -> list[Vector]:
        return self.vcts

    def appendMatrix(self, mtx: Matrix):
        if not self.mtxs.__contains__(mtx):
            self.mtxs.append(mtx)

    def appendVector(self, vct: Vector):
        if not self.vcts.__contains__(vct):
            self.vcts.append(vct)

    def popMatrix(self) -> Matrix:
        if len(self.mtxs) > 0:
            return self.mtxs.pop()
        raise CacheEmptyException

    def popVector(self) -> Vector:
        if len(self.vcts) > 0:
            return self.vcts.pop()
        raise CacheEmptyException

    def returnMatrix(self, idx: int) -> Matrix:
        if len(self.mtxs) > idx > 0:
            return self.mtxs[idx]

    def returnVector(self, idx: int) -> Vector:
        if len(self.vcts) > idx > 0:
            return self.vcts[idx]

    def chooseMatrix(self) -> Matrix:
        print("Choose one of the following Matrix's")
        for idx, mtx in enumerate(self.mtxs):
            print(f"+++Matrix {idx}: ++++++")
            print(mtx)
            print()
        rIdx = FLOAT_getRangedInput(0, len(self.mtxs) - 1, forceInt=True)
        return self.mtxs[rIdx]

    def chooseVector(self) -> Vector:
        print("Choose one of the following Vectors\n\n")
        for idx, vct in enumerate(self.vcts):
            print(f"++Vector {idx}: {vct}")
            print()
        rIdx = FLOAT_getRangedInput(0, len(self.vcts) - 1, forceInt=True)
        return self.vcts[rIdx]

    def chooseElement(self) -> Matrix | Vector:
        print("What do you want? (1: matrix / 2: vector)")
        opt = STR_getInput(["1", "2", "matrix", "vector"], printOptions=False)
        if ["1", "matrix"].__contains__(opt):
            return self.chooseMatrix()
        if ["2", "vector"].__contains__(opt):
            return self.chooseVector()
        else:
            return self.chooseElement()

    def clear(self):
        self.mtxs = []
        self.vcts = []
