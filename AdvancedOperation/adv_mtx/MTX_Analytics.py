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


def isSquareMatrix(mtx: Matrix) -> bool:
    sz = mtx.getSizeDict()
    return sz["#rows"] == sz["#cols"]


def isInUpperTriangularForm(mtx: Matrix) -> bool:
    raise NotYetImplementedException
    # if not isSquareMatrix(mtx):
    #   return False
    # sz = mtx.getSizeDict()
    # for idxR in range(sz["#rows"]):
    #   for idxC in range(sz["#cols"]):
    #      if idxC < idxR:
    #         if mtx.getValue(idxR, idxC) != 0:
    #            return False
    # return True


def isInLowerTriangularForm(mtx: Matrix) -> bool:
    raise NotYetImplementedException
    # if not isSquareMatrix(mtx):
    #   return False
    # sz = mtx.getSizeDict()
    # for idxR in range(sz["#rows"]):
    #   for idxC in range(0, idxR):
    #      if idxC > idxR:
    #         if mtx.getValue(idxR, idxC) != 0:
    #            return False
    # return True
