import random

from AdvancedOperation.cache.Cache import Cache

from BasicOperation.vector.VCT_input import VECTOR_createRandom as VCT_createRandom
from BasicOperation.matrix.MTX_input import MATRIX_createRandom as MTX_createRandom

from Other.input import *

def cacheEditor(ch: Cache) -> Cache:
    min = -5
    max = 5
    mxLng = 5
    while True:
        print("-2: Append n random sized Vectors")
        print("-1: Append n fixed Size Vectors")
        print(" 0: Return or change min/max")
        print(" 1: Append n fixed #Row Matrixes")
        print(" 2: Append n fixed #Col Matrixes")
        print(" 3: Append n fixed size Matrixes")
        print(" 4: Append n random sized Matrixes")
        chosen = FLOAT_getRangedInput(-2, 4, forceInt=True)
        match chosen:
            case -2:
                print("How Many?")
                n = FLOAT_getInput(forceInt=True, unsigned=True)
                ch = append_n_random_Vectors(ch, n, mxLng, min, max)
            case -1:
                print("How Many?")
                n = FLOAT_getInput(True, True)
                print("Which Length?")
                sz = INT_getBiggerInput(min=1, msg="#####: ")
                ch = append_n_sized_Vectors(ch, n, sz, min, max)
            case 0:
                opt = STR_getInput(["return", "change"], True)
                if opt == "return":
                    return ch
                else:
                    print("Enter new min:")
                    min = FLOAT_getInput()
                    print("Enter new max:")
                    max = FLOAT_getInput()
                    print("Enter new Max Length:")
                    mxLng = INT_getBiggerInput(2, msg="####: ")
            case 1:
                print("How Many?")
                n = FLOAT_getInput(forceInt=True, unsigned=True)
                print("How many Rows?")
                rw = INT_getBiggerInput(2, msg="####: ")
                ch = append_n_fixedRow_Matrixs(ch, n, rw, mxLng, min, max)
            case 2:
                print("How Many?")
                n = FLOAT_getInput(forceInt=True, unsigned=True)
                print("How many Columns?")
                cl = INT_getBiggerInput(2, msg="####: ")
                ch = append_n_fixedRow_Matrixs(ch, n, mxLng, cl, min, max)
            case 3:
                print("How Many?")
                n = FLOAT_getInput(forceInt=True, unsigned=True)
                print("How many Rows?")
                rw = INT_getBiggerInput(2, msg="####: ")
                print("How many Columns?")
                cl = INT_getBiggerInput(2, msg="####: ")
                ch = append_n_fixedRow_Matrixs(ch, n, rw, cl, min, max)
            case 4:
                print("How Many?")
                n = FLOAT_getInput(forceInt=True, unsigned=True)
                ch = append_n_fixedRow_Matrixs(ch, n, mxLng, mxLng, min, max)

def append_n_random_Vectors(ch: Cache, num:int, mxLng: int, min: float, max: float) -> Cache:
    for i in range(num):
        ch.appendVector(VCT_createRandom(random.randint(1, mxLng), False, min, max))
    return ch

def append_n_sized_Vectors(ch: Cache, num: int, size: int, min: float, max: float) -> Cache:
    for i in range(num):
        ch.appendVector(VCT_createRandom(size, False, min, max))
    return ch

def append_n_fixedRow_Matrixs(ch: Cache, num: int, fixR: int, mxLng: int, min: float, max: float) -> Cache:
    for i in range(num):
        ch.appendMatrix(MTX_createRandom(fixR, random.randint(2, mxLng), makeComplex=False, min=min, max=max))
    return ch

def append_n_fixedCol_Matrixs(ch: Cache, num: int, fixC: int, mxLng: int, min: float, max: float) -> Cache:
    for i in range(num):
        ch.appendMatrix(MTX_createRandom(random.randint(2, mxLng), fixC, makeComplex=False, min=min, max=max))
    return ch

def append_n_fixedSize_Matrixs(ch: Cache, num: int, fixR: int, fixC: int, min: float, max: float) -> Cache:
    for i in range(num):
        ch.appendMatrix(MTX_createRandom(fixR, fixC, makeComplex=False, min=min, max=max))
    return ch

def append_n_random_Matrixs(ch: Cache, num: int, mxLng: int, min: float, max: float) -> Cache:
    for i in range(num):
        ch.appendMatrix(MTX_createRandom(random.randint(2, mxLng), random.randint(2, mxLng), makeComplex=False, min=min, max=max))
    return ch

