from BasicOperation.matrix.Matrix import Matrix
from BasicOperation.matrix.ElementaryMatrixFactory import ElementaryMatrixFactory as EMF
from BasicOperation.vector.Vector import Vector


class ModulusGaussSystem:
    def __init__(self, mtx: Matrix, mod: int):
        self.mtx = mtx
        self.mod = mod
        self.size = mtx.getSizeDict()["#rows"]
        self.elfac = EMF(initiator=mod)

