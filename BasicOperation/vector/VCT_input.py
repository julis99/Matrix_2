import random

from Other.input import *
import BasicOperation.complex.CPX_input as complex


def VECTOR_getInput(complexity: int=0, size:int = 0) -> Vector:
    """Forces user to Create a Vector
    :parameter complexity (1: asks whether Complex; 2: forces complex; anything else will force non-complex"""
    if size == 0:
        size = INT_getBiggerInput(min=1, msg="Enter Length of Vector: ")
    if complexity == 1:
        makeComplex = BOOL_getInput(msg="With Complex numbers? (y/n)")
    elif complexity == 2:
        makeComplex = True
    else:
        makeComplex = False
    rtn = Vector(lng=size, isComplex=makeComplex)
    for idx in range(len(rtn)):
        print(f"   Enter Value for {idx} pos:")
        if makeComplex:
            tmp = complex.COMPLEX_getInput()
        else:
            tmp = FLOAT_getInput()
        rtn.changeElement(idx, tmp)
    print(f"Returning {rtn}")
    return rtn

def VECTOR_createRandom(lng: int, makeComplex: bool, min: float, max: float) -> Vector:
    rtn = Vector(lng, makeComplex)
    for idx in range(lng):
        if makeComplex:
            rtn.changeElement(idx, complex.COMPLEX_createRandom(min, max))
        else:
            rtn.changeElement(idx, random.uniform(min, max))
    return rtn