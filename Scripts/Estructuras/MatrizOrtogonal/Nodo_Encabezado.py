class Nodo_Encabezado:

    def __init__(self, id):
        self.id: int = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None

   # iterar sobre la lista
    def __iter__(self):
        nodo = self.acceso
        while nodo:
            yield nodo
            nodo = nodo.derecha
