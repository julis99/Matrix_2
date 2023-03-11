from BasicOperation.matrix.Matrix import Matrix
from BasicOperation.vector.Vector import Vector

def row(mtx: Matrix, rw: int) -> Vector:
    """:returns a Vector with entries of the requested row"""
    rtn = Vector(sz := mtx.getSizeDict()["#cols"], isComplex=mtx.isComplex())
    for idx in range(sz):
        rtn.changeElement(idx, mtx.getValue(rw, idx))
    return rtn

def col(mtx: Matrix, cl: int) -> Vector:
    """:returns a Vector with entries of the requested column"""
    rtn = Vector(sz := mtx.getSizeDict()["#rows"], isComplex=mtx.isComplex())
    for idx in range(sz):
        rtn.changeElement(idx, mtx.getValue(idx, cl))
    return rtn
