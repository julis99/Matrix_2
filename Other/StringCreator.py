from BasicOperation.complex.ComplexNum import ComplexNum as complex
from Other.Exceptions import *


def FLOAT_cutStringToSpecLen(num: float, lng: int) -> str:
    """:returns str of input num with specific length (cuts behind)"""
    rtn = str(num)
    if len(rtn) >= lng:
        return rtn[:lng]
    else:
        for idx in range(len(rtn), lng):
            rtn += " "
        return rtn


def COMPLEX_cutStringToSpecLen(cpx: complex, lng: int) -> str:
    """:returns str of input complexNum cuts it to desired length"""
    partLng = (lng - 4) // 2
    rStr = FLOAT_cutStringToSpecLen(num=cpx.getReal(), lng=partLng)
    iStr = FLOAT_cutStringToSpecLen(num=cpx.getImag(), lng=partLng)
    return f"{rStr} + {iStr}i"

def STR_makeSpecLen(wrd: str, lng: int) -> str:
    add = ""
    if len(wrd) > lng:
        raise WrongTypeException
    for idx in range(lng - len(wrd)):
        add += " "
    return wrd + add
