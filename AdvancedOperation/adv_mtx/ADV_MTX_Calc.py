from BasicOperation.matrix.Matrix import Matrix
from AdvancedOperation.adv_mtx.MTX_Analytics import *
from BasicOperation.complex.ComplexNum import ComplexNum as Complex
from BasicOperation.mixedCalc import *

from Other.Exceptions import *

def determinant(mtx: Matrix) -> Complex | float | int:
    raise NotYetImplementedException



def getDiagonalEntries(mtx: Matrix) -> list[Complex | float | int]:
    if not isSquareMatrix(mtx):
        raise NotCompatibleException
    rtn: list[Complex | float | int] = []
    for idx in range(mtx.getRows()):
        rtn.append(mtx.getValue(idx, idx))
    return rtn