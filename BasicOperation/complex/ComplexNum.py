

class ComplexNum:
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imaginary = imag

    def __str__(self) -> str:
        return f"{self.real} + {self.imaginary}i"

    def getReal(self) -> float:
        return self.real

    def getImag(self) -> float:
        return self.imaginary

    def __add__(self, other):
        rRtn = self.real + other.getReal()
        iRtn = self.imaginary + other.getImag()
        return ComplexNum(rRtn, iRtn)

    def __mul__(self, other):
        r1 = self.real
        r2 = other.getReal()
        i1 = self.imaginary
        i2 = other.getImag()
        rRtn = (r1 * r2) - (i1 * i2)
        iRtn = (r1 * i2) + (i1 * r2)
        return ComplexNum(rRtn, iRtn)

    def __eq__(self, other):
        if isinstance(other, int | float):
            if self.getImag() != 0:
                return False
            else:
                return self.getReal() == other
        if self.real == other.getReal() and self.imaginary == other.getImag():
            return True
        return False

    def hasZeroImaginary(self):
        return self.imaginary == 0


def conjugate(num: ComplexNum | int | float) -> ComplexNum | int | float:
    if isinstance(num, ComplexNum):
        return ComplexNum(real=num.getReal(), imag=-1 * num.getImag())
    else:
        return num




def ComplexAdapter(num: float | int | ComplexNum, adapt: bool):
    if adapt and not isinstance(num, ComplexNum):
        return ComplexNum(num, 0)
    else:
        return num