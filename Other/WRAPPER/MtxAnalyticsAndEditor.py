from BasicOperation.matrix.Matrix import Matrix, MTX_makeComplex
from AdvancedOperation.adv_mtx.MTX_Analytics import *

from BasicOperation.vector.Vector import Vector

from BasicOperation.complex.CPX_input import COMPLEX_getInput as CPX_getInput

from BasicOperation.conversion import *


from Other.CommonPrints import *
from Other.StringCreator import STR_makeSpecLen
from Other.input import *

import time


def Analytics_n_Editor(mtx: Matrix) -> Matrix | Vector:
    print(r"                   __                           ____    __             __             ")
    print(r" /'\_/`\          /\ \__         __            /\  _`\ /\ \__         /\ \__          ")
    print(r"/\      \     __  \ \ ,_\  _ __ /\_\   __  _   \ \,\L\_\ \ ,_\    __  \ \ ,_\   ____  ")
    print(r"\ \ \__\ \  /'__`\ \ \ \/ /\`'__\/\ \ /\ \/'\   \/_\__ \\ \ \/  /'__`\ \ \ \/  /',__\ ")
    print(r" \ \ \_/\ \/\ \L\.\_\ \ \_\ \ \/ \ \ \\/>  </     /\ \L\ \ \ \_/\ \L\.\_\ \ \_/\__, `\ ")
    print(r"  \ \_\\ \_\ \__/.\_\\ \__\\ \_\  \ \_\/\_/\_\    \ `\____\ \__\ \__/.\_\\ \__\/\____/")
    print(r"   \/_/ \/_/\/__/\/_/ \/__/ \/_/   \/_/\//\/_/     \/_____/\/__/\/__/\/_/ \/__/\/___/ ")
    time.sleep(0.5)
    size = mtx.getSizeDict()
    size["#rows"] += -1
    size["#cols"] += -1
    for i in range(3):
        print(fullHashLine())
    while True:
        print(getAnalyticString(mtx))
        print("Choose one of the following options")
        print("-1: Exit")
        print(" 0: Return")
        print(" 1: Edit one position")
        print(" 2: Edit one row")
        print(" 3: Edit one column")
        print(" 4: Return a Vector (row/col)")
        if mtx.isComplex():
            print(" 5: Reduce to NonComplex")
        else:
            print(" 5: Make Complex")
        chosen = FLOAT_getRangedInput(-1, 5, forceInt=True)
        match chosen:
            case -1:
                print(exitString())
                exit()
            case 0:
                return mtx
            case 1:
                print("Enter Row Index ")
                idxR = FLOAT_getRangedInput(0, size["#rows"], forceInt=True)
                print("Enter Column Index")
                idxC = FLOAT_getRangedInput(0, size["#cols"], forceInt=True)
                print(f"Enter new Value for pos {idxR}, {idxC}")
                if mtx.isComplex():
                    newVal = CPX_getInput()
                else:
                    newVal = FLOAT_getInput(forceInt=False, unsigned=False)
                mtx.changeElement(idxR, idxC, newVal)
            case 2:
                print("Enter Row Index ")
                idxR = FLOAT_getRangedInput(0, size["#rows"], forceInt=True)
                for idxC in range(size["#cols"]):
                    print(f"Enter new Value for pos {idxR}, {idxC}")
                    if mtx.isComplex():
                        newVal = CPX_getInput()
                    else:
                        newVal = FLOAT_getInput(forceInt=False, unsigned=False)
                    mtx.changeElement(idxR, idxC, newVal)
            case 3:
                print("Enter Column Index")
                idxC = FLOAT_getRangedInput(0, size["#cols"], forceInt=True)
                for idxR in range(size["#rows"]):
                    print(f"Enter new Value for pos {idxR}, {idxC}")
                    if mtx.isComplex():
                        newVal = CPX_getInput()
                    else:
                        newVal = FLOAT_getInput(forceInt=False, unsigned=False)
                    mtx.changeElement(idxR, idxC, newVal)
            case 4:
                print("Export Row or Column? (row/col):")
                op = STR_getInput(["row", "col"], printOptions=False)
                if op == "row":
                    print("Which Row should be Exported?")
                    idx = FLOAT_getRangedInput(0, size["#rows"], True)
                    return row(mtx, idx)
                else:
                    print("Which Column should be Exported?")
                    idx = FLOAT_getRangedInput(0, size["#cols"], True)
                    return col(mtx, idx)
            case 5:
                if mtx.isComplex():
                    mtx.reduce(force=True)
                else:
                    mtx = MTX_makeComplex(mtx)
        print(fullHashLine())




def getAnalyticString(mtx: Matrix) -> str:
    print("The given Matrix is:")
    print(mtx)
    print(fullDottedLine())
    line1 = "Dimensia   : "
    line2 = "isSymmetric: "
    size = mtx.getSizeDict()
    line1 += f"{size['#rows']} x {size['#cols']}"
    try:
        line1 = STR_makeSpecLen(line1, 20)
    except WrongTypeException:
        lngHalf = len(line1)
    else:
        lngHalf = 20
    line2 += f"{isSymmetric(mtx)}"
    line2 = STR_makeSpecLen(line2, lngHalf)
    line1 += f"|isComplex  : {mtx.isComplex()}"
    if mtx.isComplex():
        line2 += f"|isHermitsch: {isHermitsch(mtx)}"
    else:
        line2 += f"|isScewSymm : {isScewSymmetric(mtx)}"
    return f"{line1}\n{line2}\n{fullLine()}"

