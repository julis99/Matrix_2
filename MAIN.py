from AdvancedOperation.cache.Cache import Cache
from AdvancedOperation.cache.CacheEditor import cacheEditor

from BasicOperation.matrix.Matrix import Matrix
from BasicOperation.matrix.MTX_input import MATRIX_getInput as MTX_getInput

from BasicOperation.vector.Vector import Vector
from BasicOperation.vector.VCT_input import VECTOR_getInput as VCT_getInput

from BasicOperation.complex.ComplexNum import ComplexNum as Complex
from BasicOperation.complex.CPX_input import COMPLEX_getInput as CPX_getInput

from Other.input import *
from Other.CommonPrints import *
from Other.WRAPPER import MtxAnalyticsAndEditor, ModulusElMtxMult, VctCalculations
from Other.ConsoleClearer import ConsoleClear as CS_clear

import time as STD_time

def MAIN():
    printHeader()
    itm = getItem()
    ch = cacheEditor(Cache())
    while True:
        if isinstance(itm, Matrix):
            ch.appendMatrix(mtx=itm)
            printMatrixOptions(itm.isComplex())
            top = int(not itm.isComplex())
            chosen = FLOAT_getRangedInput(-2, 1 + top, forceInt=True)
            match chosen:
                case -2:
                    ch.appendMatrix(itm)
                case -1:
                    ch.appendMatrix(itm)
                    itm = ch.chooseElement()
                case 0:
                    itm = MtxAnalyticsAndEditor.Analytics_n_Editor(itm)
        if isinstance(itm, Vector):
            ch.appendVector(vct=itm)
            printVectorOptions(itm.isComplex())
            chosen = FLOAT_getRangedInput(-2, 1, forceInt=True)
            match chosen:
                case -2:
                    ch.appendVector(itm)
                case -1:
                    ch.appendVector(itm)
                    itm = ch.chooseElement()
                case 0:
                    pass
                case 1:
                    itm = VctCalculations.VCT_CALC(itm, ch)


            



def getItem() -> Matrix | Vector:
    print("What do you want to use")
    print("'matrix' -- Will let you create a Matrix")
    print("'vector' -- Will let you create a Vector")
    tsk = STR_getInput(["matrix", "vector"], printOptions=False)
    match tsk:
        case "matrix":
            return MTX_getInput(complexity=1)
        case "vector":
            return VCT_getInput(complexity=1)

def printHeader():
    print(r"  __  __       _        _         _____      _        ___    ___  ")
    print(r" |  \/  |     | |      (_)       / ____|    | |      |__ \  / _ \ ")
    print(r" | \  / | __ _| |_ _ __ ___  __ | |     __ _| | ___     ) || | | |")
    print(r" | |\/| |/ _` | __| '__| \ \/ / | |    / _` | |/ __|   / / | | | |")
    print(r" | |  | | (_| | |_| |  | |>  <  | |___| (_| | | (__   / /_ | |_| |")
    print(r" |_|  |_|\__,_|\__|_|  |_/_/\_\  \_____\__,_|_|\___| |____(_)___/ ")
    print(r"                                                                  ")
    for i in range(2):
        print(fullHashLine())
    print(r"              \\\\\ VERSION 2.4.3 /////")
    for i in range(3):
        print(fullHashLine())
    CS_clear(1)

def printMatrixOptions(isComplex: bool):
    print(fullHashLine())
    print("Choose one of the following Options:")
    print("-2: Put Matrix into Cache")
    print("-1: Put Matrix into Cache and retrieve new element")
    print(" 0: Matrix Analytics and Matrix Editor")
    print(" 1: Matrix Calculations (has Access to Cache)")
    if not isComplex:
        print(" 2: Modulus Elementary Matrix Mult. (cuts to Int)")

def printVectorOptions(isComplex: bool):
    print(fullHashLine())
    print("Choose one of the following Options:")
    print("-2: Put Vector into Cache")
    print("-1: Put Vector into Cache and retrieve new element")
    print(" 0: Vector Analytics and Matrix Editor")
    print(" 1: Vector Calculations (has Access to Cache)")

MAIN()
