class Piso:
    def __init__(self, nombre, r, c, f, s, patrones):
        self.nombre = nombre
        self.r = r
        self.c = c
        self.f = f
        self.s = s
        self.patrones = patrones

    # setters
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setFilas(self, r):
        self.r = r

    def getFilas(self):
        return self.r

    def setCols(self, c):
        self.c = c

    # getters
    def getCols(self):
        return self.c

    def setCostoFlip(self, f):
        self.f = f

    def getCostoFlip(self):
        return self.f

    def setCostoSwitch(self, s):
        self.s = s

    def getCostoSwitch(self):
        return self.s
