from abc import ABC, abstractmethod

class Publicacion(ABC):
    __titulo: str
    __categoria: str
    __precio_base: float

    def __init__(self, titulo: str, categoria: str, precio_base: float):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precio_base = precio_base
    
    def getTitulo(self) -> str:
        return self.__titulo
    def getCategoria(self) -> str:
        return self.__categoria
    def getPrecioBase(self) -> float:
        return self.__precio_base
    
    @abstractmethod
    def getImporte(self) -> float:
        pass
    