class Departamento:
    __id: int
    __nombre_propietario: str
    __numero_piso: int
    __numero_departamento: str
    __cant_habitaciones: int
    __cant_banios: int
    __superficie_cubierta: float

    def __init__(self, id: int, nombre_propietario: str, numero_piso: int, numero_departamento: int, cant_habitaciones: int, cant_banios: int, superficie_cubierta: float):
        self.__id = id
        self.__nombre_propietario = nombre_propietario
        self.__numero_piso = numero_piso
        self.__numero_departamento = numero_departamento
        self.__cant_habitaciones = cant_habitaciones
        self.__cant_banios = cant_banios
        self.__superficie_cubierta = superficie_cubierta
    
    def __repr__(self) -> str:
        return "Departamento: " + str(self.__id)

    def getId(self) -> int:
        return self.__id
    def getNombrePropietario(self) -> str:
        return self.__nombre_propietario
    def getNumeroPiso(self) -> int:
        return self.__numero_piso
    def getNumeroDepartamento(self) -> int:
        return self.__numero_departamento
    def getCantHabitaciones(self) -> int:
        return self.__cant_habitaciones
    def getCantBanios(self) -> int:
        return self.__cant_banios
    def getSuperficieCubierta(self) -> float:
        return self.__superficie_cubierta