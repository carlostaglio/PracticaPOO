import datetime

from publicacion import Publicacion

class Libro(Publicacion):
    __autor: str
    __fecha_edicion: datetime.datetime
    __cant_paginas: int

    def __init__(self, titulo: str, categoria: str, precio_base: float, autor: str, fecha_edicion: str, cant_paginas: int):
        super().__init__(titulo, categoria, precio_base)
        self.__autor = autor
        self.__fecha_edicion = datetime.datetime.strptime(fecha_edicion, "%d-%m-%Y")
        self.__cant_paginas = cant_paginas

    def getAutor(self) -> str:
        return self.__autor
    def getFechaEdicion(self) -> datetime.datetime:
        return self.__fecha_edicion
    def getCantPaginas(self) -> int:
        return self.__cant_paginas
    
    def getAntiguedad(self) -> int:
        now = datetime.datetime.now()
        return now.year - self.__fecha_edicion.year
    
    def getImporte(self) -> float:
        return self.getPrecioBase() - (self.getPrecioBase() * self.getAntiguedad() /100)