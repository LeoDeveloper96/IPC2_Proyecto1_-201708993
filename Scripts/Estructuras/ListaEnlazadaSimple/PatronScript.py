import os
import webbrowser
import re

from Scripts.Estructuras.MatrizOrtogonal.MatrizDispersa import MatrizDispersa


class Patron:
    def __init__(self, cod, patron):
        self.cod = cod
        self.patron = patron

    def getPatron(self):
        return self.patron

    def setCod(self, cod):
        self.cod = cod

    def setPatron(self, patron):
        self.patron = patron

    def getCod(self):
        return self.cod


def nuevoPatron(self, nuevo_piso, nuevo_cod):
    # aqui busco el piso segun el nuevo nombre
    piso_seleccionado = self.lista_pisos.buscarPiso(nuevo_piso)
    patron = self.lista_pisos.buscarPatron(piso_seleccionado, nuevo_cod)
    self.nuevo_piso = piso_seleccionado
    self.nuevo_patron = patron


def mostrarPatron(self, piso, cod):
    contenido = ""
    piso_seleccionado = None
    patron_seleccionado = None
    if (self.nuevo_patron and self.nuevo_piso) is None:
        piso_seleccionado = self.lista_pisos.buscarPiso(piso)
        patron_seleccionado = self.lista_pisos.buscarPatron(piso_seleccionado, cod)
        self.piso_original = piso_seleccionado
        self.patron_original = patron_seleccionado
    else:
        piso_seleccionado = self.nuevo_piso
        patron_seleccionado = self.nuevo_patron
        piso = piso_seleccionado.datos.nombre
    contenido += "graph " + str(piso) + "{" + "\n"
    contenido += "node [shape=plain] \n splines=false \n"
    contador_struct = 1
    contenido += "struct" + str(contador_struct) + " [label=<" + "\n"
    contenido += "<TABLE BORDER=" + "\"" + "0" + "\"" + " CELLBORDER=" + "\"" + "1" + "\"" + " CELLSPACING=" + "\"" + "0" + "\"" + " CELLPADDING=" + "\"" + "0" + "\"" + ">" + "\n"
    contenido += "<TR>" + "\n"
    filas = int(piso_seleccionado.datos.r)
    columnas = int(piso_seleccionado.datos.c)
    patron = re.sub('\n', '', patron_seleccionado.datos.patron)
    contador_puerto = 0
    contador = 1
    patron_separado = re.findall('.{' + str(columnas) + '}', patron)
    for fila in patron_separado:
        for caracter in fila:
            if caracter.lower() == "w":
                contenido += "<TD PORT=\"f" + str(
                    contador_puerto) + "\" bgcolor=\"white\" width=\"25\" height=\"25\" fixedsize=\"true\"></TD>\n"
                contador_puerto += 1
            else:
                contenido += "<TD PORT=\"f" + str(
                    contador_puerto) + "\" bgcolor=\"black\" width=\"25\" height=\"25\" fixedsize=\"true\"></TD>\n"
                contador_puerto += 1
        contador += 1
        contenido += "</TR> \n"
        contenido += "</TABLE >>];\n \n"
        if contador <= filas:
            contador_struct += 1
            contenido += "struct" + str(contador_struct) + " [label=<" + "\n"
            contenido += "<TABLE BORDER=" + "\"" + "0" + "\"" + " CELLBORDER=" + "\"" + "1" + "\"" + " CELLSPACING=" + "\"" + "0" + "\"" + " CELLPADDING=" + "\"" + "0" + "\"" + ">" + "\n"
            contenido += "<TR>" + "\n"
        else:
            break

    contador1 = 0
    contador2 = columnas
    for i in range(1, contador_struct):
        for j in range(contador1, contador2):
            contenido += "struct" + str(i) + ":f" + str(j) + " -- struct" + str(i + 1) + ":f" + str(
                j + columnas) + "[style=invis];" + "\n"
    contador1 = contador2
    contador2 = contador1 + columnas
    contenido += "\n" + "}"
    contenido += "\n"
    ruta = os.getcwd()
    file = open(ruta + "\\Graficas\\grafico.dot", "w+")
    file.write(contenido)
    file.close()
    os.system('cmd /C "dot -Tpng ' + ruta + '\\Graficas\\grafico.dot -o ' + ruta + '\\Graficas\\grafico.png"')
    webbrowser.open(ruta + '\\Graficas\\grafico.png')


def costoMin(self):
    costo_f = int(self.piso_original.datos.f)
    costo_s = int(self.piso_original.datos.s)
    num_switch = 0
    negras_mat1 = 0
    negras_mat2 = 0
    cols = int(self.piso_original.datos.c)
    fils = int(self.piso_original.datos.r)

    # calculo el numero de flips
    for c in re.sub("\n", "", self.patron_original.datos.patron):
        if c.lower() == "b":
            negras_mat1 += 1

    for c in re.sub("\n", "", self.nuevo_patron.datos.patron):
        if c.lower() == "b":
            negras_mat2 += 1

    num_flips = abs(negras_mat1 - negras_mat2)

    # calculo el numero de switch
    patron1 = re.sub("\n", "", self.patron_original.datos.patron)
    patron2 = re.sub("\n", "", self.nuevo_patron.datos.patron)
    matriz1 = crearMatriz(patron1, cols, fils)
    marcarIncorrectas(matriz1, patron2)
    num_switch = calculoSwitch(self,matriz1, patron2)

    # la respuesta final
    return (num_flips * costo_f) + (num_switch * costo_s)


def calculoSwitch(self,mat,patron2):
    switch = 0
    contador = 0
    # si la matriz tiene mas de una fila
    if mat.filas.size > 1:
        for fila in mat.filas:
            for col in fila:
                if not col.correcto:
                    caracter = col.caracter.lower()
                    # reviso que la columna en cualquier direccion, excepto diagonal, no esté vacia, sea invalida y tenga
                    # el color opuesto
                    if col.derecha is not None and (col.derecha.correcto == False and col.caracter.lower() != col.derecha.caracter.lower()):
                        # marco las casillas como corregidas
                        col.correcto = True
                        col.derecha.correcto = True
                        # intercambio los valores
                        col.caracter = col.derecha.caracter
                        col.derecha.caracter = caracter
                        # esto cuenta como un intercambio
                        switch += 1
                        # Escribo la instruccion correspondiente
                        self.instrucciones += " Intercambiar las celdas " + "(" + str(col.coordenadaX)+", " + str(col.coordenadaY)+")" + "por: " + "(" + str(col.derecha.coordenadaX)+", " + str(col.derecha.coordenadaY)+")"+"\n"
                    elif col.izquierda is not None and (col.izquierda.correcto == False and col.caracter.lower() != col.izquierda.caracter.lower()):
                        col.correcto = True
                        col.izquierda.correcto = True
                        col.caracter = col.izquierda.caracter
                        col.izquierda.caracter = caracter
                        switch += 1
                        self.instrucciones += " Intercambiar las celdas " + "(" + str(col.coordenadaX) + ", " + str(
                            col.coordenadaY) + ")" + "por: " + "(" + str(col.izquierda.coordenadaX) + ", " + str(
                            col.izquierda.coordenadaY) + ")" + "\n"
                    elif col.arriba is not None and (col.arriba.correcto == False and col.caracter.lower() != col.arriba.caracter.lower()):
                        col.correcto = True
                        col.arriba.correcto = True
                        col.caracter = col.arriba.caracter
                        col.arriba.caracter = caracter
                        switch += 1
                        self.instrucciones += " Intercambiar las celdas " + "(" + str(col.coordenadaX) + ", " + str(
                            col.coordenadaY) + ")" + "por: " + "(" + str(col.arriba.coordenadaX) + ", " + str(
                            col.arriba.coordenadaY) + ")" + "\n"
                    elif col.abajo is not None and (col.abajo.correcto == False and col.caracter.lower() != col.abajo.caracter.lower()):
                        col.correcto = True
                        col.abajo.correcto = True
                        col.caracter = col.abajo.caracter
                        col.abajo.caracter = caracter
                        switch += 1
                        self.instrucciones += " Intercambiar las celdas " + "(" + str(col.coordenadaX) + ", " + str(
                            col.coordenadaY) + ")" + "por: " + "(" + str(col.abajo.coordenadaX) + ", " + str(
                            col.abajo.coordenadaY) + ")" + "\n"
                    # esto es un flip
                    else:
                        self.instrucciones += "Hacerle flip a la celda: " + "("+str(col.coordenadaX)+", "+str(col.coordenadaY)+")"+"\n"
                        if col.caracter.lower() == "w":
                            col.caracter = "b"
                        else:
                            col.caracter = "w"
                        col.correcto = True
    #   si la matriz es de 1xn
    else:
        for fila in mat.filas:
            for col in fila:
                if col.caracter.lower() != patron2[contador].lower():
                    switch += 1
                contador += 1

    #     escribo la cadena de instrucciones para matrices de 1xn
        contador2 = 0
        for fila in mat.filas:
            for col in fila:
                if not col.correcto:
                    caracter = col.caracter.lower()
                    # reviso que la col de la derecha no esté vacia y que tenga el color opuesto
                    if col.derecha is not None and col.caracter.lower() != col.derecha.caracter.lower():
                        col.correcto = True
                        col.caracter = col.derecha.caracter
                        col.derecha.caracter = caracter
                        if col.derecha.caracter.lower() != patron2[contador2+1].lower():
                            col.derecha.correcto = False
                        else:
                            col.derecha.correcto = True
                        self.instrucciones += "Intercambiar las celdas " + "("+str(col.coordenadaX) + ", " + str(col.coordenadaY) + ")" + " por: " + "(" + str(col.derecha.coordenadaX) + ", " + str(col.derecha.coordenadaY) + ")" + "\n"
                    else:
                        self.instrucciones += "Hacerle flip a la celda: " + "(" + str(col.coordenadaX) + ", " + str(
                            col.coordenadaY) + ")" + "\n"
                        col.correcto = True
                else:
                    continue
                contador2 += 1
    return switch


def marcarIncorrectas(mat1, patron2):
    contador = 0
    for fila in mat1.filas:
        for col in fila:
            if col.caracter.lower() != patron2[contador].lower():
                col.correcto = False
            contador += 1


def crearMatriz(patron, cols, fils):
    contador = 0
    mat = MatrizDispersa()
    for i in range(1, fils + 1):
        for j in range(1, cols + 1):
            mat.insert(i, j, patron[contador])
            contador += 1
    return mat
