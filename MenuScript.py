from ListaEnlazadaScript import ListaEnlazada
import re
from pip._vendor.distlib.compat import raw_input
import webbrowser
import os
import re
import Archivo


class Menu:
    lista_pisos = ListaEnlazada()
    nuevo_patron = None
    nuevo_piso = None

    def menu(self):
        print("\n")
        print("1 Cargar Archivo")
        print("2 Opciones Patron")
        print("3 Salir")
        entrada = input("Ingrese un numero 1-5" + "\n")
        patron = "[1-5]{1}"
        if re.search(patron, entrada):
            if entrada == "1":
                self.mostrarPisos()
                Archivo.cargarArchivo(self)
                self.menu()
            elif entrada == "2":
                self.subMenu1()
            elif entrada == "3":
                raw_input("Presione una tecla" + "\n")
        else:
            self.menu()

    def subMenu1(self):
        print("\n")
        print("-----------------------------------------")
        print("1 Mostrar listado de pisos y patrones disponibles")
        print("2 Graficar patron")
        print("3 Seleccionar nuevo patron")
        print("4 Costo cambio")
        print("5 Instrucciones cambio")
        print("6 Regresar al menu principal...")
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
                self.subMenu1()
            elif entrada == "3":
                nuevo_piso = input("\n" + "Ingrese el nombre del piso" + "\n")
                nuevo_cod = input("Ingrese el nuevo codigo del patron" + "\n")
                self.nuevoPatron(nuevo_piso, nuevo_cod)
                self.subMenu1()
            elif entrada == "6":
                print("\n")
                print("-----------------------------------------")
                self.menu()
            else:
                self.menu()

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
                Archivo.cargarArchivo(self)
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
        piso_seleccionado = self.lista_pisos.buscarLista(piso)
        patron_seleccionado = self.lista_pisos.buscarPatron(piso_seleccionado, cod)
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
        a = 1
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
        file = open("grafico.dot", "w+")
        file.write(contenido)
        file.close()
        os.system('cmd /C "dot -Tpng grafico.dot -o grafico.png"')
        ruta = os.getcwd()
        webbrowser.open(ruta + '\\grafico.png')

    def mostrarPisos(self):
        for piso in self.lista_pisos:
            print(piso.datos.nombre)
            for patron in piso.datos.patrones:
                print("--->" + patron.datos.cod)

    def nuevoPatron(self, nuevo_piso, nuevo_cod):
        # aqui busco el piso segun el nuevo nombre
        piso_seleccionado = self.lista_pisos.buscarLista(nuevo_piso)
        patron = self.lista_pisos.buscarPatron(piso_seleccionado, nuevo_cod)
        self.nuevo_piso = piso_seleccionado
        self.nuevo_patron = patron
