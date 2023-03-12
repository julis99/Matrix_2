from AdvancedOperation.cache.Cache import Cache
from BasicOperation.matrix.Matrix import Matrix, MatrixSize
from BasicOperation.vector.Vector import Vector
from Other.input import FLOAT_getRangedInput


class FilteredMatrixCache:
    """:var byRow: Contains ALL Vectors that have #rows == refererenced #cols
    :var byCol: Contains ALL Vectors that have #cols == refererenced #rows"""
    def __init__(self, unfiltered: Cache, mtxS: MatrixSize):
        self.allowed = mtxS
        self.byRow: list[Matrix] = []
        self.byCol: list[Matrix] = []
        self.byExactMatch: list[Matrix] = []
        self.matchingVectors: list[Vector] = []
        for mtx in unfiltered.getMatrixList():
            if mtx.getRows() == mtxS.getCols():
                self.byRow.append(mtx)
            if mtx.getCols() == mtxS.getRows():
                self.byCol.append(mtx)
            if MatrixSize(mtx) == mtxS:
                self.byExactMatch.append(mtx)
        for vct in unfiltered.getVectorList():
            if len(vct) == mtxS.cols:
                self.matchingVectors.append(vct)

    def chooseForRowMatch(self) -> Matrix:
        print("Choose one of the following Matrix's")
        for idx, mtx in enumerate(self.byRow):
            print(f"+++Matrix {idx}: ++++++")
            print(mtx)
            print()
        rIdx = FLOAT_getRangedInput(0, len(self.byRow) - 1, forceInt=True)
        return self.byRow[rIdx]

    def chooseForColMatch(self) -> Matrix:
        print("Choose one of the following Matrix's")
        for idx, mtx in enumerate(self.byCol):
            print(f"+++Matrix {idx}: ++++++")
            print(mtx)
            print()
        rIdx = FLOAT_getRangedInput(0, len(self.byCol) - 1, forceInt=True)
        return self.byCol[rIdx]

    def chooseForExactMatch(self) -> Matrix:
        print("Choose one of the following Matrix's")
        for idx, mtx in enumerate(self.byExactMatch):
            print(f"+++Matrix {idx}: ++++++")
            print(mtx)
            print()
        rIdx = FLOAT_getRangedInput(0, len(self.byExactMatch) - 1, forceInt=True)
        return self.byExactMatch[rIdx]

    def chooseVector(self) -> Vector:
        print("Choose one of the following Vectors\n\n")
        for idx, vct in enumerate(self.matchingVectors):
            print(f"++Vector {idx}: {vct}")
            print()
        rIdx = FLOAT_getRangedInput(0, len(self.matchingVectors) - 1, forceInt=True)
        return self.matchingVectors[rIdx]

    def containsNoRowMatchMtx(self) -> bool:
        if not self.byRow:
            return True
        return False

    def containsNoColMatchMtx(self) -> bool:
        if not self.byCol:
            return True
        return False

    def containsNoExactMatchMtx(self) -> bool:
        if not self.byExactMatch:
            return True
        return False

    def containsNoVectors(self) -> bool:
        if not self.matchingVectors:
            return True
        return False

class FilteredVectorCache:
    def __init__(self, unfiltered: Cache, lng = int):
        """:var matchingMatrixs The Matrixes from Cache which can be used for Matrix-Vector-Multiplication"""
        self.allowed = lng
        self.matchingVectors: list[Vector] = []
        self.matchingMatrixs: list[Matrix] = []
        for vct in unfiltered.getVectorList():
            if len(vct) == lng:
                self.matchingVectors.append(vct)
        for mtx in unfiltered.getMatrixList():
            if mtx.getCols() == lng:
                self.matchingMatrixs.append(mtx)

    def chooseMatrix(self) -> Matrix:
        print("Choose one of the following Matrix's")
        for idx, mtx in enumerate(self.matchingMatrixs):
            print(f"+++Matrix {idx}: ++++++")
            print(mtx)
            print()
        rIdx = FLOAT_getRangedInput(0, len(self.matchingMatrixs) - 1, forceInt=True)
        return self.matchingMatrixs[rIdx]

    def chooseVector(self) -> Vector:
        print("Choose one of the following Vectors\n\n")
        for idx, vct in enumerate(self.matchingVectors):
            print(f"++Vector {idx}: {vct}")
            print()
        rIdx = FLOAT_getRangedInput(0, len(self.matchingVectors) - 1, forceInt=True)
        return self.matchingVectors[rIdx]

    def containsNoVectors(self) -> bool:
        if not self.matchingVectors:
            return True
        return False

    def containsNoMatrixs(self) -> bool:
        if not self.matchingMatrixs:
            return True
        return False

