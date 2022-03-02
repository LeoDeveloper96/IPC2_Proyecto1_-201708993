class Nodo:
    def __init__(self, datos=None, siguiente=None):
        self.datos = datos
        self.siguiente = siguiente

    def setDatos(self, datos):
        self.datos = datos

    def getDatos(self):
        return self.datos
