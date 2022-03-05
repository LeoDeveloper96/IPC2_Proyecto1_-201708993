def aEstrella(self, a, b):
    if a in self.vertices and b in self.vertices:
        self.vertices[a].costo = 0
        self.vertices[a].costoF = self.vertices[a].heuristica

    for v in self.vertices:
        if v != a:
            self.vertices[v].costo = float('inf')
            self.vertices[v].costoF = float('inf')
        self.vertices[v].padre = None

    abierto = [a]

    while len(abierto) > 0:
        actual = self.minimoH(abierto)
        if actual == b:
            return self.camino(a, b)
        abierto.remove(actual)
        self.vertices[actual].visitado = True

        for v in self.vertices[actual].vecinos:
            if not self.vertices[v[0]].visitado:
                if self.vertices[v[0]].id not in abierto:
                    abierto.append(v[0])
                if self.vertices[actual].costo + v[1] < self.vertices[v[0]].costo:
                    self.vertices[v[0]].padre = actual
                    self.vertices[v[0]].costo = self.vertices[actual].costo + v[1]
                    self.vertices[v[0]].costoF = self.vertices[v[0]].costo + self.vertices[v[0]].heuristica


def camino(self, a, b):
    camino = []
    actual = b
    while actual is not None:
        camino.insert(0, actual)
        actual = self.vertices[actual].padre
    return camino


def minimoH(self, l):
    if len(l) > 0:
        m = self.vertices[l[0]].costoF
        v = l[0]
        for e in l:
            if m > self.vertices[e].costoF:
                m = self.vertices[e].costoF
                v = e
        return v
