from ListaEnlazadaScript import ListaEnlazada
from pip._vendor.distlib.compat import raw_input
import re
import Archivo
import PisoScript
import PatronScript


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
                PisoScript.mostrarPisos(self)
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
                PisoScript.mostrarPisos(self)
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
