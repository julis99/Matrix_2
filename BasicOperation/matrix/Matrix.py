from BasicOperation.complex.ComplexNum import ComplexNum as Complex, conjugate
from Other.StringCreator import *

from Other.Exceptions import *

class Matrix:
    def __init__(self, rows: int, cols: int, isComplex:bool=False):
        self.rows = rows
        self.cols = cols
        self.isCpx = isComplex
        self.values = []
        for idxR in range(rows):
            tmp = []
            for idxC in range(cols):
                if self.isCpx:
                    tmp.append(Complex(0, 0))
                else:
                    tmp.append(0)
            self.values.append(tmp)

    def __str__(self) -> str:
        rtn = ""
        if self.isCpx:
            for row in self.values:
                rtn += f"[{COMPLEX_cutStringToSpecLen(row[0], 15)}"
                for idxC in range(1, len(row)):
                    rtn += f"| {COMPLEX_cutStringToSpecLen(row[idxC], 15)}"
                rtn += "]\n"
        else:
            for row in self.values:
                rtn += f"[{FLOAT_cutStringToSpecLen(row[0], 15)}"
                for idxC in range(1, len(row)):
                    rtn += f", {FLOAT_cutStringToSpecLen(row[idxC], 15)}"
                rtn += "]\n"
        return rtn

    def __add__(self, other):
        """Addition like LinA 1.23"""
        sSize = MatrixSize(self)
        oSize = MatrixSize(other)
        if not sSize == oSize:
            raise NotCompatibleException
        rtn = Matrix(self.rows, self.cols, self.isComplex() or other.isComplex())
        A = MTX_typeCompatibilizor(self, other.isComplex())
        B = MTX_typeCompatibilizor(other, self.isComplex())
        for idxR in range(self.rows):
            for idxC in range(self.cols):
                tmp = A.getValue(idxR, idxC) + B.getValue(idxR, idxC)
                rtn.changeElement(idxR, idxC, tmp)
        return rtn

    def __mul__(self, other):
        """Multiplication like LinA 1.25"""
        if not self.cols == other.getRows():
            raise NotCompatibleException
        rtn = Matrix(self.rows, other.getCols(), self.isComplex() or other.isComplex())
        sTmp = MTX_typeCompatibilizor(self, other.isComplex())
        oTmp = MTX_typeCompatibilizor(other, self.isComplex())
        for idxR in range(self.rows):
            for idxC in range(other.getCols()):
                if self.isComplex() or other.isComplex:
                    vl = Complex(0, 0)
                else:
                    vl = 0
                for idxW in range(sTmp.getCols()):
                    vl += sTmp.getValue(idxR, idxW) * oTmp.getValue(idxW, idxC)
                rtn.changeElement(idxR, idxC, vl)
        return rtn

    def __mod__(self, other: int):
        """cuts to Int!"""
        if self.isCpx:
            raise NotCompatibleException
        rtn = Matrix(self.rows, self.cols)
        for idxR in range(self.rows):
            for idxC in range(self.cols):
                rtn.changeElement(idxR, idxC, int(self.getValue(idxR, idxC)) % other)
        return rtn

    def __eq__(self, other):
        if self.getSizeDict() != other.getSizeDict():
            return False
        for idxR in range(self.rows):
            for idxC in range(self.cols):
                if self.getValue(idxR, idxC) != other.getValue(idxR, idxC):
                    return False
        return True

    def getSizeDict(self) -> dict:
        """:returns dict with '#rows' as number of rows and '#cols' as number of columns"""
        return {"#rows": self.rows, "#cols": self.cols}

    def getValue(self, row: int, col: int):
        return self.values[row][col]

    def changeElement(self, row: int, col: int, newValue):
        if isinstance(newValue, Complex) and self.isCpx:
            self.values[row][col] = newValue
        elif (isinstance(newValue, float) or isinstance(newValue, int)) and not self.isCpx:
            self.values[row][col] = newValue
        else:
            raise WrongTypeException

    def isComplex(self):
        return self.isCpx

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def reduce(self, force=False):
        if not self.isCpx:
            return
        if not force:
            for row in self.values:
                for cpx in row:
                    if not cpx.hasZeroImaginary():
                        return
        self.isCpx = False
        for idxR in range(self.rows):
            for idxC in range(self.cols):
                self.changeElement(idxR, idxC, self.values[idxR][idxC].getReal())

    def transpose(self):
        rtn = Matrix(self.cols, self.rows, self.isComplex())
        for idxR in range(self.rows):
            for idxC in range(self.cols):
                rtn.changeElement(row=idxC, col=idxR, newValue=self.getValue(idxR, idxC))
        return rtn

    def adjungate(self):
        rtn = self.transpose()
        for idxR in range(self.cols):
            for idxC in range(self.rows):
                rtn.changeElement(idxR, idxC, conjugate(rtn.getValue(idxR, idxC)))
        return rtn



class MatrixSize:
    def __init__(self, mtx: Matrix):
        tmp = mtx.getSizeDict()
        self.rows = tmp["#rows"]
        self.cols = tmp["#cols"]

    def __eq__(self, other):
        return self.rows == other.rows and self.cols == other.cols

    def getRows(self) -> int:
        return self.rows

    def getCols(self) -> int:
        return self.cols

def MTX_typeCompatibilizor(A: Matrix, makeCpx: bool):
    if makeCpx:
        return MTX_makeComplex(A)
    else:
        return A


def MTX_makeComplex(A: Matrix) -> Matrix:
    """Turns any matrix into a Complex one, the imaginary part is set to 0"""
    if A.isComplex():
        return A
    else:
        aSize = A.getSizeDict()
        rtn = Matrix(aSize["#rows"], aSize["#cols"], True)
        for idxR in range(aSize["#rows"]):
            for idxC in range(aSize["#cols"]):
                rtn.changeElement(idxR, idxC, Complex(A.getValue(idxR, idxC), 0))
        return rtn


