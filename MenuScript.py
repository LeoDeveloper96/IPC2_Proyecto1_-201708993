from ListaEnlazadaScript import ListaEnlazada
from PisoScript import Piso
import re
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from PatronScript import Patron
from pip._vendor.distlib.compat import raw_input
import os


class Menu:
    lista_pisos = ListaEnlazada()

    def menu(self):
        print("\n")
        print("1 Cargar Archivo")
        print("2 Opciones Patron")
        print("3 Seleccionar Nuevo codigo")
        print("4 Mostrar instrucciones")
        print("5 Salir")
        entrada = input("Ingrese un numero 1-5" + "\n")
        patron = "[1-5]{1}"
        if re.search(patron, entrada):
            if entrada == "1":
                self.cargarArchivo()
                self.menu()
            elif entrada == "2":
                self.subMenu1()
            elif entrada == "3":
                self.cargarArchivo()
                self.menu()
            elif entrada == "4":
                pass
            elif entrada == "5":
                raw_input("Presione una tecla" + "\n")
        else:
            self.menu()

    def subMenu1(self):
        print("\n")
        print("-----------------------------------------")
        print("1 Mostrar listado de pisos y patrones disponibles")
        print("2 Mostrar patron")
        print("3 Seleccionar nuevo patron")
        print("4 Regresar al menu principal...")
        entrada = input("Ingrese un numero 1-4" + "\n")
        patron = "[1-4]{1}"
        if re.search(patron, entrada):
            if entrada == "1":
                self.mostrarPisos()
                self.subMenu1()
            elif entrada == "2":
                piso = input("\n" + "Ingrese el nombre del piso" + "\n")
                cod = input("Ingrese el codigo del patron" + "\n")
                self.mostrarPatron(piso, cod)
            elif entrada == "3":
                piso = input("\n" + "Ingrese el nombre del piso" + "\n")
                cod = input("Ingrese el nuevo codigo del patron" + "\n")
                self.nuevoPatron(piso,cod)
                self.subMenu1()
            elif entrada == "4":
                print("\n")
                print("-----------------------------------------")
                self.menu()
            else:
                self.menu()

    def mostrarPisos(self):
        for piso in self.lista_pisos:
            print(piso.datos.nombre)
            for patron in piso.datos.patrones:
                print("--->" + patron.datos.cod)

    def nuevoPatron(self, piso, cod):
        pass

    def subMenu2(self):
        print("\n")
        print("-----------------------------------------")
        print("1 Seleccionar nuevo piso y patron")
        print("2 Costo minimo nuevo patron")
        print("3 Mostrar instrucciones nuevo patron")
        print("4 Regresar al menu anterior...")
        entrada = input("Ingrese un numero 1-4" + "\n")
        patron = "[1-6]{1}"
        if re.search(patron, entrada):
            if entrada == "1":
                self.cargarArchivo()
            elif entrada == "2":
                pass
            elif entrada == "3":
                pass
            elif entrada == "4":
                print("\n")
                print("-----------------------------------------")
                self.subMenu1()
        else:
            self.subMenu1()

    def mostrarPatron(self, piso, cod):
        contenido = ""
        piso_seleccionado = None
        patron_seleccionado = None
        iterador = self.lista_pisos.cabeza
        while iterador:
            if iterador.datos.nombre == piso:
                piso_seleccionado = iterador
                break
            iterador = iterador.siguiente

        # obtengo el patron seleccionado
        iterador = piso_seleccionado.datos.patrones.cabeza
        while iterador:
            if iterador.datos.cod == cod:
                patron_seleccionado = iterador
                break
            iterador = iterador.siguiente

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
        patron_separado = re.findall('.{'+str(columnas) + '}', patron)
        a = 1
        for fila in patron_separado:
            for caracter in fila:
                if caracter.lower() == "w":
                    contenido += "<TD PORT=\"f" + str(contador_puerto) + "\" bgcolor=\"white\" width=\"25\" height=\"25\" fixedsize=\"true\"></TD>\n"
                    contador_puerto += 1
                else:
                    contenido += "<TD PORT=\"f" + str(contador_puerto) + "\" bgcolor=\"black\" width=\"25\" height=\"25\" fixedsize=\"true\"></TD>\n"
                    contador_puerto += 1
            contador += 1
            contenido += "</TR> \n"
            contenido +="</TABLE >>];\n \n"
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
        file = open("grafico.dot", "w+")
        file.write(contenido)
        file.close()
        os.system('cmd /k "dot -Tpng grafico.dot -o grafico.png"')
        os.system('cmd /k "grafico.png"')

    def cargarArchivo(self):
        root = tk.Tk()
        root.withdraw()
        nombre_archivo = filedialog.askopenfilename(initialdir="/", title="Seleccionar un archivo",
                                                    filetypes=(("texto", "*.xml"), ("todos", "*.*")))
        try:
            with open(nombre_archivo, "r", encoding="utf8") as archivo:
                arbol = ET.parse(nombre_archivo, parser=ET.XMLParser(encoding='iso-8859-5'))
                raiz = arbol.getroot()
                pisos = raiz.findall('piso')
                for piso in pisos:
                    patrones = ListaEnlazada()
                    nombre_piso = piso.attrib['nombre']
                    r = piso.find('R').text
                    c = piso.find('C').text
                    f = piso.find('F').text
                    s = piso.find('S').text
                    et_patrones = piso.find('patrones').findall('patron')
                    for patron in et_patrones:
                        codigo = patron.attrib['codigo']
                        patron = patron.text
                        patrones.append(Patron(codigo, patron))
                    self.lista_pisos.append(Piso(nombre_piso, r, c, f, s, patrones))
        except FileNotFoundError:
            print("archivo no encontrado")
