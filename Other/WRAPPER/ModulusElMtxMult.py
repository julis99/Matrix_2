from BasicOperation.matrix.Matrix import Matrix
from BasicOperation.matrix.ElementaryMatrixFactory import ElementaryMatrixFactory as EMF
from BasicOperation.matrix.MTX_input import MATRIX_getInput as MTX_getInput, MATRIX_reduceToInt as MTX_redToInt

from BasicOperation.vector.Vector import Vector
from BasicOperation.vector.VCT_input import VECTOR_getInput as VCT_getInput

from BasicOperation.mixedCalc import MTX_VCT_Multiplication

from Other.input import FLOAT_getInput as INT_getInput, STR_getInput, FLOAT_getRangedInput as INT_getRangedInput
from Other.CommonPrints import *
from Other.MatrixFromFile.txtToMatrix import txtToModMatrix as TXT_Input

def MOD_EMM_main(mtx: Matrix = None, mod: int = 0) -> Matrix:
    print(r".-..-.         .-.      .-.                 .--. .-.                  .--.        .-.        ")
    print(r": `' :         : :      : :                : .--': :                 : .--'       : :        ")
    print(r": .. : .--.  .-' :.-..-.: :  .-..-. .--.   : `;  : :   .--. ,-.,-.,-.: :    .--.  : :   .--. ")
    print(r": :; :' .; :' .; :: :; :: :_ : :; :`._-.'  : :__ : :_ ' '_.': ,. ,. :: :__ ' .; ; : :_ '  ..'")
    print(r":_;:_;`.__.'`.__.'`.__.'`.__;`.__.'`.__.'  `.__.'`.__;`.__.':_;:_;:_;`.__.'`.__,_;`.__;`.__.'")
    if not mtx:
        mtx = MTX_getInput(complexity=0)
    mtx = MTX_redToInt(mtx)
    if not int:
        mod = INT_getInput(forceInt=True, unsigned=True)
    while mod % 2 == 0:
        print("Modulus has to be odd")
        mod = INT_getInput(forceInt=True, unsigned=True)
    mtx %= mod
    eFac = EMF(initiator=mod)
    print(fullHashLine())
    sz = mtx.getSizeDict()["#rows"]
    solVct = MOD_EMM_getSolutingVectors(sz, mod)
    while True:
        eMtx = eFac.createIdentityMatrix(sz)
        print(f"The given Matrix is:\n{mtx}\n\nIt will calculate under modulus {mod}")
        print("You have the following Options:")
        print(" return: Returns the Matrix currently given")
        print(" exit  : Exits the program entirely")
        print(" add   : Create a Addition Matrix and use it on the given Matrix")
        print(" switch: Create a Switch Matrix and use it")
        print(" mult  : Create a Multiplication Matrix and use it")
        print(" sols  : Show current state of 'right side'-Vectors")
        options: list[str] = ["return", "exit", "add", "switch", "mult", "sols"]
        opt = STR_getInput(options, printOptions=False)
        match opt:
            case "return":
                return mtx
            case "exit":
                exit()
            case "add":
                print("Enter idx of row that should be added to another")
                added = INT_getRangedInput(0, sz - 1, forceInt=True)
                print("Enter idx of row that should be added on")
                toAddTo = INT_getRangedInput(0, sz - 1, forceInt=True)
                print("Enter the factor")
                fct = INT_getInput(forceInt=True, unsigned=False)
                eMtx = eFac.createAdditionMatrix(sz, toAddTo, added, fct)
            case "switch":
                print("Enter index of rows that should be switched")
                rowA = INT_getRangedInput(0, sz - 1, forceInt=True)
                rowB = INT_getRangedInput(0, sz - 1, forceInt=True)
                eMtx = eFac.createSwitchMatrix(sz, rowA, rowB)
            case "mult":
                print("Enter index of row that should be multiplied")
                rw = INT_getRangedInput(0, sz - 1, forceInt=True)
                print("Enter Factor of multiplication")
                fct = INT_getInput(forceInt=True, unsigned=False)
                eMtx = eFac.createMultiplicationMatrix(sz, rw, fct)
            case "sols":
                prt = ""
                for idx in range(sz):
                    for vct in solVct:
                        prt += f"   |{vct[idx]}|"
                    prt += "\n"
                print("The right side Vectors are\n" + prt)
                continue
        mtx = eMtx * mtx
        mtx %= mod
        for idx in range(len(solVct)):
            solVct[idx] = MTX_VCT_Multiplication(eMtx, solVct[idx]) % mod



def MOD_EMM_getSolutingVectors(size: int, mod: int) -> list[Vector]:
    """:returns a list of vectors which are the right side of a Linear Equation System"""
    rtn = []
    print("Do you need 'right side vectors'? (y / n)")
    if STR_getInput(["y", "n"], printOptions=False) == "n":
        return []
    zero = Vector(size, False)
    while True:
        print("The entered Vector will be right side of the given Equation System")
        print("So all operations performed are also done to this Vector")
        vct = VCT_getInput(0, size)
        if vct == zero: #If the entered Vector is the 0-Vector
            return rtn
        vct %= mod
        print(vct)
        rtn.append(vct)


if __name__ == "__main__":
    MOD_EMM_main()


