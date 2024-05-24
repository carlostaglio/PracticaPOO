from publicacion import Publicacion

class Nodo:
    __publicacion: Publicacion
    __siguiente: object

    def __init__(self, publicacion: Publicacion):
        self.__publicacion = publicacion
        self.__siguiente = None
    
    def setSiguiente(self, siguiente: object) -> None:
        self.__siguiente = siguiente
    
    def getSiguiente(self) -> object:
        return self.__siguiente
    
    def getDato(self) -> Publicacion:
        return self.__publicacion