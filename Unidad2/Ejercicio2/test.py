from CajaAhorro import CajaAhorro
from Contenedor import Contenedor

def obtenerDatosCta() -> str:
    """Solicita al usuario el número de CUIL"""
    cuil=input("Ingrese número de CUIL: ")
    return cuil

def test() -> None:
    """Función de testing"""

    #Creación del objeto contenedor
    conten=Contenedor()
    #Instanciación de tres cajas de ahorro de ejemplo
    caja1=CajaAhorro(1,"20-12345678-9", "Perez", "Juan", 10000)
    caja2=CajaAhorro(2,"27-12345678-1", "Martínez", "María", 2000)
    caja3=CajaAhorro(3,"30-12345678-0", "López", "Pablo", 30000)
    #Incorporación de los objetos CajaAhorro de ejemplo en el contenedor
    conten.agregarCuenta(caja1)
    conten.agregarCuenta(caja2)
    conten.agregarCuenta(caja3)
    print("Cajas de ahorro cargadas en el sistema")

    #Solicitud de CUIL
    cuil=obtenerDatosCta()
    #LLamado al método para obtener los datos de una cuenta dado el CUIL
    print(conten.obetenerDatos(cuil))

