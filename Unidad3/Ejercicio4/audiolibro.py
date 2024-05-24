from libro import Libro

class Audiolibro(Libro):
    __tiempo_repr_minutos: int
    __narrador: str

    def __init__(self, titulo: str, categoria: str, precio_base: float, autor: str, fecha_edicion: str, cant_paginas: int, tiempo_repr_minutos: int, narrador: str):
        super().__init__(titulo, categoria, precio_base, autor, fecha_edicion, cant_paginas)
        self.__tiempo_repr_minutos = tiempo_repr_minutos
        self.__narrador = narrador
    
    def getTiempo(self) -> int:
        return self.__tiempo_repr_minutos
    def getNarrador(self) -> str:
        return self.__narrador
    
    def getImporte(self) -> float:
        return self.getPrecioBase() * 1.1
    
