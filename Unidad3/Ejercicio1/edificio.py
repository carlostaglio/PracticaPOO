from departamento import Departamento

class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __nombre_constructora: str
    __cant_pisos: int
    __cant_departamentos_piso: int
    __departamentos: list

    def __init__(self, id: int, nombre: str, direccion: str, nombre_constructora: str, cant_pisos: int, cant_departamentos_piso: int):
        self.__id = id
        self.__nombre = nombre
        self.__direccion = direccion
        self.__nombre_constructora = nombre_constructora
        self.__cant_pisos = cant_pisos
        self.__cant_departamentos_piso = cant_departamentos_piso
        self.__departamentos = []
    
    def __del__(self):
        print("Eliminando departamentos del edificio", self.__id)
        for departamento in self.__departamentos:
            del departamento
    
    def __str__(self):
        string = "Edificio: " + str(self.__id)
        string += "\nDepartamentos: " + str(self.__departamentos)
        return string


    def getId(self) -> int:
        return self.__id
    def getNombre(self) -> str:
        return self.__nombre
    def getDireccion(self) -> str:
        return self.__direccion
    def getConsultora(self) -> str:
        return self.__nombre_constructora
    def getCantPisos(self) -> int:
        return self.__cant_pisos
    def getCantDepartamentosPiso(self) -> int:
        return self.__cant_departamentos_piso
    def getDepartamentos(self) -> list:
        return self.__departamentos
    
    def agregarDepartamento(self, id: int, nombre_propietario: str, numero_piso: int, numero_departamento: int, cant_habitaciones: int, cant_banios: int, superficie_cubierta: float) -> None:
        nuevoDepartamento = Departamento(id, nombre_propietario, numero_piso, numero_departamento, cant_habitaciones, cant_banios, superficie_cubierta)
        self.__departamentos.append(nuevoDepartamento)

    def mostrarPropietarios(self) -> None:
        for departamento in self.__departamentos:
            print("Departamento {}, propietario: {}".format(departamento.getId(), departamento.getNombrePropietario()))
        print("")
    
    def getSuperficieCubierta(self) -> float:
        total = 0.
        for departamento in self.__departamentos:
            total += departamento.getSuperficieCubierta()
        return total
    
    def informarSupCubPropietario(self, nombre: str) -> None:
        encontrado = False
        for departamento in self.__departamentos:
            if departamento.getNombrePropietario() == nombre:
                encontrado = True
                superficie = departamento.getSuperficieCubierta()
                porcentaje = (superficie / self.getSuperficieCubierta()) * 100
                print("En el edificio {}, el propietario posee {:.2f} m2 de superficie cubierta, lo que corresponde a un {:.2f} % del edificio".format(self.__id, superficie, porcentaje))
        if not encontrado:
            print("El propietario no posee un departamento en el edificio {}\n".format(self.__id))
    
    def cantDeptosCondicion(self, num_piso: int) -> None:
        cant = 0
        if num_piso > 0 and num_piso <= self.__cant_pisos:
            inicio = ((num_piso -1) * self.__cant_departamentos_piso)
            for i in range(inicio, inicio + self.__cant_departamentos_piso):
                if self.__departamentos[i].getCantHabitaciones() == 3 and self.__departamentos[i].getCantBanios() > 1:
                    cant +=1
        else:
            print("Número de piso incorrecto")
            cant= -1
        return cant
