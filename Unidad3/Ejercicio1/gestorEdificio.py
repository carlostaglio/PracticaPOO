import csv
from pathlib import Path
import os
from edificio import Edificio

class GestorEdificio:
    __listaEdificios: list

    def __init__(self):
        self.__listaEdificios = []

    def getListaEdificios(self) -> list:
        return self.__listaEdificios
    
    def cargarDatos(self):
        directorio = os.path.dirname(os.path.realpath(__file__))
        file = open(directorio + "\\EdificioNorte.csv", "r")
        reader = csv.reader(file, delimiter=";")
        aux = 0
        for fila in reader:
            if aux != fila[0]:
                aux = fila[0]
                edificio = Edificio(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                self.__listaEdificios.append(edificio)
            else:
                self.__listaEdificios[int(aux) - 1].agregarDepartamento(int(fila[1]), fila[2], int(fila[3]), int(fila[4]), int(fila[5]), int(fila[6]), float(fila[7]))
        print("Datos de los edificios cargados")
        file.close()
    
    def mostrarPropietariosEdificio(self, nombre: str) -> None:
        encontrado = False
        i = 0
        while i < len(self.__listaEdificios) and not encontrado:
            if self.__listaEdificios[i].getNombre() == nombre:
                encontrado = True
                self.__listaEdificios[i].mostrarPropietarios()
            i += 1
        if not encontrado:
            print("Edificio no encontrado\n")
    
    def getSuperficieCubierta(self, id: int) -> None:
        encontrado = False
        i = 0
        while i < len(self.__listaEdificios) and not encontrado:
            if self.__listaEdificios[i].getId() == id:
                encontrado = True
                print("Superficie total cubierta del edificio: {:.2f} m2\n".format(self.__listaEdificios[i].getSuperficieCubierta()))
            i += 1
        if not encontrado:
            print("Edificio no encontrado\n")

    def informarSuperfCubiertaPropietario(self, nombre: str) -> None:
        for edificio in self.__listaEdificios:
            edificio.informarSupCubPropietario(nombre)
            
    def cantidadDepartamentosCondicion(self, id: int, num_piso: int) -> None:
        encontrado = False
        i = 0
        while i < len(self.__listaEdificios) and not encontrado:
            if self.__listaEdificios[i].getId() == id:
                encontrado = True
                cantidad = self.__listaEdificios[i].cantDeptosCondicion(num_piso)
                if cantidad != -1:
                    print("Cantidad de departamentos del edificio {} piso {} con 3 dormitorios y más de un baño: {}".format(id, num_piso, cantidad))
            i += 1
        if not encontrado:
            print("Edificio no encontrado\n")
