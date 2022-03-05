from Scripts.Estructuras.ListaEnlazadaSimple.NodoScript import Nodo


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # insertar al principio
    def preppend(self, datos):
        nodo = Nodo(datos, self.cabeza)
        self.cabeza = nodo

    # insertar al final
    def append(self, datos):
        if self.cabeza is None:
            self.cabeza = Nodo(datos, None)
            return
        iterador = self.cabeza
        while iterador.siguiente:
            iterador = iterador.siguiente
        iterador.siguiente = Nodo(datos, None)

    # devuelve el tamaño de la lista
    def get_length(self):
        contador = 0
        iterador = self.cabeza
        while iterador:
            contador += 1
            iterador = iterador.siguiente
        return contador

    def eliminar_pos(self, indice):
        if indice < 0 or indice > self.get_length():
            raise Exception("Indice invalido")
        if indice == 0:
            self.cabeza = self.cabeza.siguiente
            return
        conteo = 0
        iterador = self.cabeza
        while iterador:
            if conteo == indice - 1:
                iterador.siguiente = iterador.siguiente.siguiente
                break
            iterador = iterador.siguiente
            conteo += 1

    def insertar_pos(self, indice, datos):
        if indice < 0 or indice > self.get_length():
            raise Exception("Indice invalido")
        if indice == 0:
            self.preppend(datos)
            return
        contador = 0
        iterador = self.cabeza
        while iterador:
            if contador == indice - 1:
                nodo = Nodo(datos, iterador.siguiente)
                iterador.siguiente = nodo
                break

            iterador = iterador.siguiente
            contador += 1

    # iterar sobre la lista
    def __iter__(self):
        nodo = self.cabeza
        while nodo:
            yield nodo
            nodo = nodo.siguiente

    # buscar un piso en la lista por nombre, devuelve un objeto tipo Piso
    def buscarPiso(self, dato):
        position = 0
        encontrado = 0
        nodo = None
        if self.cabeza is None:
            print("No existe la lista")
        else:
            nodo_temp = self.cabeza
            while nodo_temp is not None:
                position = position + 1
                if nodo_temp.datos.nombre == dato:
                    nodo = nodo_temp
                    encontrado = 1
                    break
                nodo_temp = nodo_temp.siguiente
        if encontrado == 0:
            print("El valor no existe en la lista")
        else:
            # devuelvo el piso
            return nodo

    # buscar un patron en la lista por nombre, devuelve un objeto tipo Patron
    def buscarPatron(self, piso, cod):
        patron_seleccionado = None
        iterador = piso.datos.patrones.cabeza
        while iterador:
            if iterador.datos.cod == cod:
                patron_seleccionado = iterador
                break
            iterador = iterador.siguiente
        return patron_seleccionado
