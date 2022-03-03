import os
import webbrowser
import re


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
