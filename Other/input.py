from BasicOperation.matrix.Matrix import Matrix
from BasicOperation.complex.ComplexNum import ComplexNum as Complex
from BasicOperation.vector.Vector import Vector


def BOOL_getInput(msg: str = "") -> bool:
    while True:
        rtn = input(f"         {msg} (y/n): ")
        if rtn == "y":
            return True
        if rtn == "n":
            return False


def FLOAT_getInput(forceInt: bool = False, unsigned: bool = False):
    """Forces User to input a Float/Int"""
    if unsigned:
        usgn: str = "unsigned "
    else:
        usgn: str = ""
    if forceInt:
        while True:
            try:
                rtn = int(input(f"        Enter an {usgn}integer:"))
                if unsigned:
                    return abs(rtn)
                return rtn
            except ValueError:
                print("        ==WRONG INPUT--Try Again==")
                continue
    while True:
        try:
            rtn = float(input(f"        Enter an {usgn}float:"))
            if unsigned:
                return abs(rtn)
            return rtn
        except ValueError:
            print("        ==WRONG INPUT--Try Again==")
            continue


def FLOAT_getRangedInput(min: int | float, max: int | float, forceInt: bool = False):
    if forceInt:
        while True:
            try:
                rtn = int(input(f"        Enter an Int betw {min} and {max}: "))
                if rtn >= min and rtn <= max:
                    return rtn
            except ValueError:
                print("        ==WRONG INPUT--Try Again==")
                continue
    while True:
        try:
            rtn = float(input(f"        Enter a float betw {min} and {max}: "))
            if rtn >= min and rtn <= max:
                return rtn
        except ValueError:
            print("        ==WRONG INPUT--Try Again==")
            continue

def INT_getBiggerInput(min: int, msg: str = None) -> int:
    if not msg:
        msg = f"Enter an integer not smaller than {min}:    "
    while True:
        try:
            rtn = int(input(msg))
            if rtn >= min:
                return rtn
            else:
                print(f"Input has to be bigger than {min}")
        except ValueError:
            print("        ==WRONG INPUT--Try Again==")
            continue


def STR_getInput(accepted: list[str], printOptions: bool = True) -> str:
    while True:
        if printOptions:
            print(f"Enter {accepted}")
        rtn = input("+++::")
        if accepted.__contains__(rtn):
            return rtn

def BOOL_getInput(msg: str = "(y/n)") -> bool:
    print(msg)
    bStr = STR_getInput(["y", "n"], printOptions=False)
    if bStr == "y":
        return True
    else:
        return False
