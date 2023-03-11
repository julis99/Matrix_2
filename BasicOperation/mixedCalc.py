from BasicOperation.matrix.Matrix import Matrix, MTX_typeCompatibilizor
from BasicOperation.vector.Vector import Vector, VCT_typeCompatibilizor
from BasicOperation.complex.ComplexNum import ComplexNum as Complex, ComplexAdapter

from Other.Exceptions import *

def UNIT_MTX_Multiplication(unit: float | int| Complex, input: Matrix) -> Matrix:
    """Calculates like LinA 1.23 (Equation (1.8))"""
    size = input.getSizeDict()
    rtn = Matrix(rows=size["#rows"], cols=size["#cols"], isComplex=input.isComplex() or isinstance(unit, Complex))
    mtx = MTX_typeCompatibilizor(input, isinstance(unit, Complex))
    unit = ComplexAdapter(unit, input.isComplex())
    for idxR in range(size["#rows"]):
        for idxC in range(size["#cols"]):
            rtn.changeElement(idxR, idxC, unit * mtx.getValue(idxR, idxC))
    return rtn

def UNIT_VCT_Multiplication(unit: float | int | Complex, input: Vector) -> Vector:
    """Calculates like LinA 3.1 (Equation (3.3))"""
    rtn = Vector(lng=len(input),isComplex=input.isComplex() or isinstance(unit, Complex))
    vct = VCT_typeCompatibilizor(input, isinstance(unit, Complex))
    unit = ComplexAdapter(unit, input.isComplex())
    for idx in range(len(vct)):
        rtn.changeElement(idx, unit * vct[idx])
    return rtn

def MTX_VCT_Multiplication(mtx: Matrix, vct: Vector) -> Vector:
    """Calculates like LinA  1.24"""
    mSz = mtx.getSizeDict()
    if mSz["#cols"] != len(vct):
        raise NotCompatibleException
    rtn = Vector(mSz["#rows"], isComplex=mtx.isComplex() or vct.isComplex())
    mtx = MTX_typeCompatibilizor(mtx, vct.isComplex())
    vct = VCT_typeCompatibilizor(vct, mtx.isComplex())
    for idxR in range(mSz["#rows"]):
        tmp = ComplexAdapter(0, mtx.isComplex() or vct.isComplex())
        for idxC in range(len(vct)):
            tmp += mtx.getValue(idxR, idxC) * vct[idxC]
        rtn.changeElement(idxR, tmp)
    return rtn


