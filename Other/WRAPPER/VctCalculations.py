from BasicOperation.vector.Vector import Vector
from BasicOperation.vector.VCT_input import VECTOR_getInput as VCT_getInput
from AdvancedOperation.adv_vctCalc.ADV_VCT_Calc import *

from BasicOperation.matrix.Matrix import Matrix
from BasicOperation.matrix.MTX_input import MATRIX_getInput as MTX_getInput

from BasicOperation.complex.CPX_input import COMPLEX_getInput as CPX_getInput
from BasicOperation.mixedCalc import *

from AdvancedOperation.cache.Cache import Cache
from AdvancedOperation.cache.FilteredCache import FilteredVectorCache

from Other.Exceptions import *
from Other.input import *
from Other.CommonPrints import *

def VCT_CALC(vct: Vector, ch: Cache = None) -> Vector | Matrix:
    print(r"/^^         /^^         /^^           /^^              /^^                /^^            /^^                   ")
    print(r" /^^       /^^          /^^        /^^   /^^           /^^                /^^            /^^                   ")
    print(r"  /^^     /^^     /^^^/^/^ /^     /^^          /^^     /^^   /^^^/^^  /^^ /^^   /^^    /^/^ /^   /^^    /^ /^^^")
    print(r"   /^^   /^^    /^^     /^^       /^^        /^^  /^^  /^^ /^^   /^^  /^^ /^^ /^^  /^^   /^^   /^^  /^^  /^^   ")
    print(r"    /^^ /^^    /^^      /^^       /^^       /^^   /^^  /^^/^^    /^^  /^^ /^^/^^   /^^   /^^  /^^    /^^ /^^   ")
    print(r"     /^^^^      /^^     /^^        /^^   /^^/^^   /^^  /^^ /^^   /^^  /^^ /^^/^^   /^^   /^^   /^^  /^^  /^^   ")
    print(r"      /^^         /^^^   /^^         /^^^^    /^^ /^^^/^^^   /^^^  /^^/^^/^^^  /^^ /^^^   /^^    /^^    /^^^   ")
    print(fullHashLine())
    while True:
        chosen = chooseOptions(vct)
        match chosen:
            case -1:
                print(exitString())
                exit()
            case 0:
                return vct
            case 1:
                other: Vector = None
                if ch:
                    useCache = BOOL_getInput(msg="Choose from Chache? (y/n)")
                else:
                    useCache = False
                if useCache:
                    fltrd = FilteredVectorCache(unfiltered=ch, lng=len(vct))
                    if fltrd.containsNoVectors():
                        print("Cache contains no fitting Vectors\nCreate a new One")
                    else:
                        other = fltrd.chooseVector()
                if not other:
                    other = VCT_getInput(1, len(vct))
                print(f"Calculating {vct} + {other}")
                vct += other
                vct.reduce(force=False)
                print(fullHashLine())
            case 2:
                useCpx = BOOL_getInput(msg="Complex Number? (y/n)")
                if useCpx:
                    unit = CPX_getInput()
                else:
                    unit = FLOAT_getInput()
                print(f"Calculating ({unit}) * {vct}")
                vct = UNIT_VCT_Multiplication(unit, vct)
                vct.reduce(force=False)
                print(fullHashLine())
            case 3:
                other: Vector = None
                if ch:
                    useCache = BOOL_getInput(msg="Choose from Chache? (y/n)")
                else:
                    useCache = False
                if useCache:
                    fltrd = FilteredVectorCache(unfiltered=ch, lng=len(vct))
                    if fltrd.containsNoVectors():
                        print("Cache contains no fitting Vectors\nCreate a new One")
                    else:
                        other = fltrd.chooseVector()
                if not other:
                    other = VCT_getInput(1, len(vct))
                print(f"Calculating dyadic({vct}, {other})")
                mtx = dyadicProduct(vct, other)
                print(f"=\n{mtx}")
                return mtx
            case 4:
                mtx: Matrix = None
                if ch:
                    useCache = BOOL_getInput(msg="Choose from Chache? (y/n)")
                else:
                    useCache = False
                if useCache:
                    fltrd = FilteredVectorCache(unfiltered=ch, lng=len(vct))
                    if fltrd.containsNoMatrixs():
                        print("Cache contains no fitting Matrixes\nCreate a new One")
                    else:
                        mtx = fltrd.chooseMatrix()
                if not mtx:
                    mtx = MTX_getInput(complexity=1, rows=0, cols=len(vct))
                print(f"Calculating:\n{mtx}\n\ntimes\n\n{vct}")
                vct = MTX_VCT_Multiplication(mtx, vct)
                vct.reduce(force=False)





def chooseOptions(vct: Vector) -> int:
    print(f"The given Vector: {vct}")
    print(fullLine())
    print("-1: Exit")
    print(" 0: Return")
    print(" 1: Addition")
    print(" 2: Unit Multiplication")
    print(" 3: DyadicProduct (will print then return the Matrix)")
    print(" 4: Matrix-Vector-Multiplication")
    print(" 5: Show Euclidean Dot Product")
    return FLOAT_getRangedInput(-1, 5, forceInt=True)

if __name__ == "__main__":
    VCT_CALC(Vector(3, False))