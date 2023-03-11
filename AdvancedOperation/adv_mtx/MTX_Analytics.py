from BasicOperation.matrix.Matrix import Matrix
from BasicOperation.mixedCalc import *

from Other.Exceptions import *

def isSymmetric(mtx: Matrix) -> bool:
    trs = mtx.transpose()
    return mtx == trs

def isHermitsch(mtx: Matrix) -> bool:
    adj = mtx.adjungate()
    return mtx == adj

def isScewSymmetric(mtx: Matrix) -> bool:
    trs = mtx.transpose()
    trs = UNIT_MTX_Multiplication(-1, trs)
    return mtx == trs


