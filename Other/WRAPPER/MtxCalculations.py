from BasicOperation.vector.Vector import Vector
from BasicOperation.vector.VCT_input import VECTOR_getInput as VCT_getInput

from BasicOperation.matrix.Matrix import Matrix, MatrixSize
from BasicOperation.matrix.MTX_input import MATRIX_getInput as MTX_getInput
from AdvancedOperation.adv_mtx.ADV_MTX_Calc import *
from AdvancedOperation.adv_mtx.MTX_Analytics import *

from BasicOperation.complex.CPX_input import COMPLEX_getInput as CPX_getInput
from BasicOperation.mixedCalc import *

from AdvancedOperation.cache.Cache import Cache
from AdvancedOperation.cache.FilteredCache import FilteredMatrixCache

from Other.Exceptions import *
from Other.input import *
from Other.CommonPrints import *

def MTX_CALC(mtx: Matrix, ch: Cache = None) -> Vector | Matrix:
    print(r"_//       _//_/// _//////_//      _//          _//         _/       _//          _//   ")
    print(r"_/ _//   _///     _//     _//   _//         _//   _//     _/ //     _//       _//   _//")
    print(r"_// _// _ _//     _//      _// _//         _//           _/  _//    _//      _//       ")
    print(r"_//  _//  _//     _//        _//           _//          _//   _//   _//      _//       ")
    print(r"_//   _/  _//     _//      _// _//         _//         _////// _//  _//      _//       ")
    print(r"_//       _//     _//     _//   _//         _//   _// _//       _// _//       _//   _//")
    print(r"_//       _//     _//    _//      _//         _////  _//         _//_////////   _////  ")
    print(fullHashLine())
    while True:
        mSZ = MatrixSize(mtx)
        match chooseOptions(mtx):
            case - 1:
                print(exitString())
                exit()
            case 0:
                return mtx
            case 1:
                other: Matrix = None
                if ch:
                    useCache = BOOL_getInput(msg="Choose from Cache? (y/n)")
                else:
                    useCache = False
                if useCache:
                    fltrd = FilteredMatrixCache(unfiltered=ch, mtxS=mSZ)
                    if fltrd.containsNoExactMatchMtx():
                        print ("Cache contains no fitting Vectors \nCreate a new One")
                    else:
                        other = fltrd.chooseForExactMatch()
                if not other:
                    other = MTX_getInput(complexity=1, rows=mSZ.getRows(), cols=mSZ.getCols())
                print(f"Calculating\n{mtx}\n\n   +   \n\n{other}")
                mtx += other
                mtx.reduce(force=False)
                print(fullHashLine())
            case 2:
                if BOOL_getInput(msg="Complex Number? (y/n)"):
                    unit = CPX_getInput()
                else:
                    unit = FLOAT_getInput()
                print(f"Calculating:\n{unit}\n\n   *   \n\n{mtx}")
                mtx = UNIT_MTX_Multiplication(unit, mtx)
                mtx.reduce(force=False)
                print(fullHashLine())
            case 3:
                other: Matrix = None
                if ch:
                    useCache = BOOL_getInput(msg="Choose from Cache? (y/n)")
                else:
                    useCache = False
                if useCache:
                    fltrd = FilteredMatrixCache(unfiltered=ch, mtxS=mSZ)
                    if fltrd.containsNoColMatchMtx():
                        print("Cache contains no fitting Matrix's \nCreate a new One")
                    else:
                        other = fltrd.chooseForColMatch()
                if not other:
                    other = MTX_getInput(complexity=1, rows=0, cols=mSZ.getRows())
                print(f"Calculating:\n{other}\n   *   \n\n{mtx}")
                mtx = other * mtx
                mtx.reduce(force=False)
                print(fullHashLine())
            case 4:
                other: Matrix = None
                if ch:
                    useCache = BOOL_getInput(msg="Choose from Cache? (y/n)")
                else:
                    useCache = False
                if useCache:
                    fltrd = FilteredMatrixCache(unfiltered=ch, mtxS=mSZ)
                    if fltrd.containsNoRowMatchMtx():
                        print("Cache contains no fitting Matrix's \nCreate a new One")
                    else:
                        other = fltrd.chooseForRowMatch()
                if not other:
                    other = MTX_getInput(complexity=1, rows=mSZ.getCols(), cols=0)
                print(f"Calculatin:\n{mtx}\n   *   \n\n{other}")
                mtx = mtx * other
                print(fullHashLine())
            case 5:
                vct: Vector = None
                if ch:
                    useCache = BOOL_getInput(msg="Choose from Cache? (y/n)")
                else:
                    useCache = False
                if useCache:
                    fltrd = FilteredMatrixCache(unfiltered=ch, mtxS= mSZ)
                    if fltrd.containsNoVectors():
                        print("Cache contains no fitting Vectors\nCreate a new One")
                    else:
                        vct = fltrd.chooseVector()
                if not vct:
                    vct = VCT_getInput(complexity=1, size=mSZ.getCols())
                print(f"Calculating and Returning:\n{mtx}\n    *    \n\n{vct}")
                print(fullDottedLine())
                vct = MTX_VCT_Multiplication(mtx, vct)
                print(f"Returning {vct}")
                return vct
            case 6:
                try:
                    det = determinant(mtx)
                    print(f"The determinant of the given Matrix is {det}")
                except NotYetImplementedException:
                    print("The Feature is not yet implemented...\n   Visit MatrixCalc.org for help")
                print(fullHashLine())
            case 7:
                if mtx.isComplex():
                    adj = BOOL_getInput(msg="Adjungate? (y/n)")
                else:
                    adj = False
                if adj:
                    mtx = mtx.adjungate()
                else:
                    mtx = mtx.transpose()


def chooseOptions(mtx: Matrix) -> int:
    print(f"The following Matrix is given:\n{mtx}")
    print(fullLine())
    print("-1: Exit")
    print(" 0: Return")
    print(" 1: Addition")
    print(" 2: Unit Multiplication")
    print(" 3: Left Multiplication (other * given)")
    print(" 4: Right Multiplication (given * other)")
    print(" 5: Matrix-Vector-Multiplication")
    print(" 6: Show Determinant")
    print(" 7: Transpose / Adjungate")
    return FLOAT_getRangedInput(-1, 7, forceInt=True)


if __name__ == "__main__":
    MTX_CALC(Matrix(3, 3, False))