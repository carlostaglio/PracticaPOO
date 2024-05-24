#Debe instalarse la librería zope
from zope.interface import Interface

class ILista(Interface):
    def insertarElemento(self, posicion: int) -> None:
        pass
    def agregarElemento(self, elemento: object) -> None:
        pass
    def mostrarElemento(self, posicion: int) -> None:
        pass