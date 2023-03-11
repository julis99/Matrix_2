from BasicOperation.matrix.Matrix import Matrix
from BasicOperation.matrix.MTX_input import MATRIX_reduceToInt as MTX_toIntEntries
from BasicOperation.complex.CPX_input import cast_to_Complex

from Other.Exceptions import *

def txtToComplexMatrix() -> Matrix:
    with open('mtx_cpx.txt', 'r') as f:
        lines = f.readlines()
        lists = []
        current_list = []
        for line in lines:
            numbers = [cast_to_Complex(x) for x in line.strip().split(',')]
            current_list.extend(numbers)
            lists.append(current_list)
            current_list = []
        try:
            rtn = Matrix(len(lists), len(lists[0]), isComplex=True)
            for idxR in range(len(lists)):
                for idxC in range(len(lists[idxR])):
                    rtn.changeElement(idxR, idxC, lists[idxR][idxC])
            rtn.reduce(force=False)
            return rtn
        except:
            raise NotValidInputException

def txtToModMatrix() -> Matrix:
    with open('mtx_mod.txt', 'r') as f:
        lines = f.readlines()
        values = []
        currentValues = []
        for line in lines:
            watched = [int(x) for x in line.strip().split(',')]
            currentValues.extend(watched)
            values.append(currentValues)
            currentValues = []
    try:
        rtn = Matrix(len(values), len(values[0]), isComplex=False)
        for idxR in range(len(values)):
            for idxC in range(len(values[idxR])):
                rtn.changeElement(idxR, idxC, values[idxR][idxC])
        return MTX_toIntEntries(rtn)
    except:
        raise  NotValidInputException







