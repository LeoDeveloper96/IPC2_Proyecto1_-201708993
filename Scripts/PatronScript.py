import os
import webbrowser
import re
import numpy as np


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
    matriz1 = None
    matriz2 = None
    if int(self.piso_original.datos.r) == 1:
        matriz1 = np.array(list(patron1))
        matriz2 = np.array(list(patron2))
    else:
        # blanco = 0
        # negro  = 1
        patron1 = convertirPatron(patron1)
        patron2 = convertirPatron(patron2)
        matriz1 = np.matrix(re.sub("", " ", '; '.join(patron1[i:i + int(self.piso_original.datos.c)] for i in range(0, len(patron1), int(self.piso_original.datos.c)))))
        matriz2 = np.matrix(re.sub("", " ", '; '.join(patron2[i:i + int(self.piso_original.datos.c)] for i in range(0, len(patron2), int(self.piso_original.datos.c)))))

    return (num_flips * costo_f) + (num_switch * costo_s)


def convertirPatron(patron):
    patron = str(patron).lower()
    patron = re.sub('w', '0', patron)
    patron = re.sub('b', '1', patron)
    return patron
