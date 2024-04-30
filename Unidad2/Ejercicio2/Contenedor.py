from CajaAhorro import CajaAhorro

class Contenedor:
    __lista:list

    def __init__(self) -> None:
        self.__lista=[]

    def obetenerLista(self) -> list:
        """Retorna la lista de cajas de ahorro"""
        return self.__lista
    
    def agregarCuenta(self, cuenta:CajaAhorro) -> None:
        """Agrega un objeto de la clase CajaAhorro a la lista"""
        self.__lista.append(cuenta)
    
    def obetenerDatos(self, cuil:str) -> str:
        """Retorna los datos de una cuenta dado su cuil, en caso de no encontrarla retorna un mensaje de error"""
        i=0
        while i < len(self.__lista) and self.__lista[i].obtenerCUIL() != cuil:
            i+=1
        if i < len(self.__lista):
            nombre=self.__lista[i].obtenerNombre()
            apellido=self.__lista[i].obtenerApellido()
            saldo=self.__lista[i].obtenerSaldo()
            datos=f"Titular de la cuenta: {nombre} {apellido} \nSaldo: $ {round(saldo,2)}"
            return datos
        else:
            return "CUIL no válido"
        