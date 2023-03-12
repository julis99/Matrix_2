from Other.input import *
import BasicOperation.complex.CPX_input as complex
import Other.CommonPrints as cp
from Other.Exceptions import *

import random

def MATRIX_getInput(complexity: int=0, rows:int = 0, cols:int = 0) -> Matrix:
    """Forces user to Create a Matrix
    :param complexity : 1: asks whether Complex; 2: forces complex; anything else will force non-complex"""
    if rows == 0:
        rows = INT_getBiggerInput(2, "Enter Number of rows: ")
    if cols == 0:
        cols = INT_getBiggerInput(2, "Enter Number of columns: ")
    if complexity == 1:
        makeComplex = BOOL_getInput(msg="With Complex numbers? (y/n)")
    elif complexity == 2:
        makeComplex = True
    else:
        makeComplex = False
    rtn = Matrix(rows, cols, makeComplex)
    print(cp.shortLine())
    for idxR in range(rows):
        for idxC in range(cols):
            print(f"Enter Value for position {idxR}, {idxC}:")
            if makeComplex:
                vl = complex.COMPLEX_getInput()
            else:
                vl = FLOAT_getInput()
            rtn.changeElement(idxR, idxC, vl)
            print(cp.shortDottedLine())
    print(f"Returning the Matrix:\n{rtn}")
    return rtn

def MATRIX_createRandom(rows: int, cols: int, makeComplex:bool, min: float, max: float) -> Matrix:
    """:returns a matrix of rows x cols with entries between min and max"""
    rtn = Matrix(rows, cols, makeComplex)
    for idxR in range(rows):
        for idxC in range(cols):
            if makeComplex:
                rtn.changeElement(idxR, idxC, complex.COMPLEX_createRandom(min, max))
            else:
                rtn.changeElement(idxR, idxC, random.uniform(min, max))
    return rtn

def MATRIX_reduceToInt(mtx: Matrix) -> Matrix:
    """cuts all entries to be int"""
    if mtx.isComplex():
        raise NotCompatibleException
    sz = mtx.getSizeDict()
    rtn = Matrix(sz["#rows"], sz["#cols"], isComplex=False)
    for idxR in range(sz["#rows"]):
        for idxC in range(sz["#cols"]):
            rtn.changeElement(idxR, idxC, int(mtx.getValue(idxR, idxC)))
    return rtn



