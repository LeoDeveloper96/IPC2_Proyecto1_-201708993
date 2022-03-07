from Scripts.Algoritmos.QuickSort import quickSort
from Scripts.Estructuras.ListaEnlazadaSimple import PisoScript, PatronScript
from Scripts.Estructuras.ListaEnlazadaSimple.ListaEnlazadaScript import ListaEnlazada
from pip._vendor.distlib.compat import raw_input
import re
import copy

from Scripts.Utilidades import Archivo


class Menu:
    lista_pisos = ListaEnlazada()
    patron_original = None
    piso_original = None
    nuevo_patron = None
    nuevo_piso = None
    instrucciones = ""

    def menu(self):
        print("\n")
        print("1 Cargar Archivo")
        print("2 Opciones Patron")
        print("3 Salir")
        entrada = input("Ingrese un numero 1-5" + "\n")
        patron = "[1-3]{1}"

        # cláusula de guarda
        if not re.search(patron, entrada): return self.menu()

        if entrada == "1":
            Archivo.cargarArchivo(self)
            self.menu()
        elif entrada == "2":
            self.subMenu1()
        elif entrada == "3":
            raw_input("Presione una tecla" + "\n")

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
        patron = "[1-6]{1}"

        if not re.search(patron, entrada): return self.menu()

        if entrada == "1":
            PisoScript.mostrarPisos(quickSort(copy.deepcopy(self.lista_pisos)))
            self.subMenu1()
        elif entrada == "2":
            piso = ""
            cod = ""
            if (self.nuevo_patron and self.nuevo_piso) is None:
                piso = input("\n" + "Ingrese el nombre del piso" + "\n")
                cod = input("Ingrese el codigo del patron" + "\n")
            else:
                piso = self.nuevo_piso
                cod = self.nuevo_patron.datos.cod
            PatronScript.mostrarPatron(self, piso, cod)
            self.subMenu1()
        elif entrada == "3":
            nuevo_piso = input("\n" + "Ingrese el nombre del piso" + "\n")
            nuevo_cod = input("Ingrese el nuevo codigo del patron" + "\n")
            PatronScript.nuevoPatron(self, nuevo_piso, nuevo_cod)
            self.subMenu1()
        elif entrada == "4":
            print("El costo min es: " + str(PatronScript.costoMin(self)) + "\n")
            self.subMenu1()
        elif entrada == "5":
            self.subMenu2()
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
        print("1 Mostrar en consola")
        print("2 Guardar en archivo")
        print("3 Volver al menu anterior")
        entrada = input("Ingrese un numero 1-3" + "\n")
        patron = "[1-3]{1}"

        if not re.search(patron, entrada): return self.subMenu1()

        if entrada == "1":
            print(self.instrucciones)
            self.subMenu2()
        elif entrada == "2":
            nombre = input("Ingrese el nombre del archivo con su extensión" + "\n")
            Archivo.crearArchivo(self, nombre)
            self.subMenu1()
        elif entrada == "3":
            self.subMenu1()
