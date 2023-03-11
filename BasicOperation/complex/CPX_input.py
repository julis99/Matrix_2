from Other.input import *
from Other.Exceptions import *
import random

def COMPLEX_getInput() -> Complex:
    """Forces User to Enter a Pair for Complex Number Creation"""
    while True:
        try:
            r = float(input("     Enter the Real Part:"))
            break
        except ValueError:
            continue
    while True:
        try:
            i = float(input("     Enter the Imaginary Part:"))
            break
        except ValueError:
            continue
    return Complex(real=r, imag=i)

def COMPLEX_createRandom(min: float, max: float) -> Complex:
    rPart = random.uniform(min, max)
    iPart = random.uniform(min, max)
    return Complex(rPart, iPart)

def cast_to_Complex(string: str) -> Complex:
    """accepts String of the format [a] + [b]i and gets them to Complex"""
    a, b = map(str, string.strip().split('+')[:2])
    a = float(a)
    b = float(b[:-1])
    return Complex(a, b)
