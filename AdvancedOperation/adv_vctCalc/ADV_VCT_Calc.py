from BasicOperation.vector.Vector import Vector, VCT_typeCompatibilizor as V_typeComp, VCT_conjugate as V_conjugate
from BasicOperation.matrix.Matrix import Matrix
from BasicOperation.complex.ComplexNum import ComplexNum as Complex

from Other.Exceptions import *

def dyadicProduct(vct1: Vector, vct2: Vector) -> Matrix:
    if len(vct1) != len(vct2):
        raise NotCompatibleException
    rtn = Matrix(len(vct1), len(vct1), vct1.isComplex() or vct2.isComplex())
    v = V_typeComp(vct1, vct2.isComplex())
    w = V_typeComp(vct2, vct1.isComplex())
    for idxR in range(len(v)):
        for idxC in range(len(w)):
            rtn.changeElement(idxR, idxC, v[idxR] * w[idxC])
    return rtn

def euclideanDotProduct(vct1: Vector, vct2: Vector) -> Complex | int | float:
    """2nd Vector will be conjugated (if Complex)"""
    if len(vct1) != len(vct2):
        raise NotCompatibleException
    v = V_typeComp(vct1, vct2.isComplex())
    w = V_typeComp(vct2, vct1.isComplex())
    w = V_conjugate(w)
    if v.isComplex():
        rtn = Complex(0, 0)
    else:
        rtn = 0
    for idx in range(len(vct1)):
        rtn += v[idx] * w[idx]
    return rtn



