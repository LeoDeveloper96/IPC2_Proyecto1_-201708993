class Vertice:

    def __init__(self, i, h=0):
        self.id = i
        self.heuristica = h
        self.vecinos = []
        self.visitado = False
        self.padre = None
        self.costo = float('inf')
        self.costoF = float('inf')

    def agregarVecino(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append([v, p])

