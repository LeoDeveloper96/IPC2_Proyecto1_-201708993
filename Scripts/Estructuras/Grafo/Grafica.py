from Scripts.Estructuras.Grafo.Vertice import Vertice


class Grafica:

    def __init__(self):
        self.vertices = {}

    # h es la heuristica
    def agregarVertice(self, id, h=0):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id, h)

    #donde p es el peso
    def agregarArista(self, a, b, p):

        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)

    def imprimirGrafica(self):
        for v in self.vertices:
            print("El costo del vértice " + str(self.vertices[v].id) + " con heuristica " + str(
                self.vertices[v].heuristica) + " es " + str(self.vertices[v].costo) + " llegando desde " + str(
                self.vertices[v].padre))





