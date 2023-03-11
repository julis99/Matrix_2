from BasicOperation.complex.ComplexNum import ComplexNum as Complex, conjugate

from Other.Exceptions import *


class Vector:
    def __init__(self, lng: int, isComplex: bool = False):
        self.isCpx = isComplex
        self.values = []
        if isComplex:
            for i in range(lng):
                self.values.append(Complex(0, 0))
        else:
            for i in range(lng):
                self.values.append(0)

    def __len__(self):
        return len(self.values)

    def __str__(self):
        rtn = f"({self.values[0]}"
        for i in range(1, len(self)):
            rtn += f", {self.values[i]}"
        rtn += ")"
        return rtn

    def __getitem__(self, item):
        return self.values[item]

    def __add__(self, other):
        if len(self) == len(other):
            rtn = Vector(len(self), isComplex=(self.isComplex() or other.isComplex()))
            if other.isComplex():
                v = VCT_makeComplex(self)
            else:
                v = self
            if self.isComplex():
                w = VCT_makeComplex(other)
            else:
                w = other
            for idx in range(len(self)):
                rtn.changeElement(idx, v[idx] + w[idx])
            return rtn
        else:
            raise NotCompatibleException

    def __mod__(self, other: int):
        """cuts to Int!"""
        if self.isCpx:
            raise NotCompatibleException
        rtn = Vector(lng=len(self), isComplex=False)
        for idx in range(len(self.values)):
            rtn.changeElement(idx, int(self.values[idx]) % other)
        return rtn

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for idx in range(len(self)):
            if self[idx] != other[idx]:
                return False
        return True

    def isComplex(self) -> bool:
        return self.isCpx

    def changeElement(self, pos: int, newValue):
        if isinstance(newValue, Complex) and self.isCpx:
            self.values[pos] = newValue
        elif (isinstance(newValue, float) or isinstance(newValue, int)) and not self.isCpx:
            self.values[pos] = newValue
        else:
            raise WrongTypeException

    def reduce(self, force:bool = False):
        if not self.isCpx:
            return
        if not force:
            for cpx in self.values:
                if not cpx.hasZeroImaginary():
                    return
        self.isCpx = False
        for idx in range(len(self)):
            self.changeElement(idx, self.values[idx].getReal())

def VCT_conjugate(vct: Vector) -> Vector:
    rtn = Vector(lng=len(vct), isComplex=vct.isComplex())
    for idx in range(len(vct)):
        rtn.changeElement(idx, conjugate(vct[idx]))
    return rtn

def VCT_typeCompatibilizor(vct: Vector, makeCpx: bool):
    if makeCpx:
        return VCT_makeComplex(vct)
    else:
        return vct

def VCT_makeComplex(vct: Vector) -> Vector:
    """Turns any vector into an Complex one, the imaginary part is set to 0"""
    if vct.isComplex():
        return vct
    else:
        rtn = Vector(lng=len(vct), isComplex=True)
        for idx in range(len(vct)):
            rtn.changeElement(idx, Complex(vct[idx], 0))
        return rtn



