from CajaAhorro import CajaAhorro

def stringValido(campo: str) -> str:
    string = ""
    while len(string) == 0:
        string = input("Ingrese " + campo + ": ")
    return string

def intValido(campo: str) -> int:
    entero = ""
    while not entero.isdigit():
        entero = input("Ingrese " + campo + ": ")
    return int(entero)

def floatValido(campo: str) -> int:
    valor = ""
    while not valor.isdigit():
        flotante = input("Ingrese " + campo + ": ")
        valor = flotante.replace(".", "")
    return float(flotante)

def crearCaja() -> CajaAhorro:
    """Crea una caja de ahorro con los valores solicitados al usuario"""
    num = intValido("número de cuenta")
    cuil = stringValido("CUIL en formato **-12345678-*")
    nombre = stringValido("nombre del titular")
    apellido = stringValido("apellido")
    saldo = floatValido("saldo de la cuenta")
    return CajaAhorro(num, cuil, apellido, nombre, saldo)

def test() -> None:
    """Función de testing"""

    #Instanciación de tres cajas de ahorro de ejemplo
    caja1=CajaAhorro(1,"20-12345678-6", "Perez", "Juan", 10000)
    caja2=CajaAhorro(2,"23-12345678-4", "Martínez", "María", 20000)
    caja3=crearCaja()
    #Incorporación de los objetos CajaAhorro de ejemplo en el contenedor
    print("Cajas de ahorro creadas")
    print("\nCaja 1: ")
    caja1.mostrarDatos()
    print("Extracción de $20000")
    valor = caja1.extraer(20000)
    if valor != -1:
        print("Saldo restante: $", valor)
    else:
        print("No pudo realizarse la extracción")
    print("Depósito de $10000")
    caja1.depositar(10000)
    caja1.mostrarDatos()
    if caja1.validarCUIL(caja1.obtenerCUIL()):
        print("CUIL válido")
    else:
        print("CUIL no válido")

    print("\nCaja 2: ")
    caja2.mostrarDatos()
    print("Extracción de $20000")
    valor = caja2.extraer(20000)
    if valor != -1:
        print("Saldo restante: $", valor)
    else:
        print("No pudo realizarse la extracción")
    print("Depósito de $0")
    caja2.depositar(0)
    caja2.mostrarDatos()
    if caja2.validarCUIL(caja2.obtenerCUIL()):
        print("CUIL válido")
    else:
        print("CUIL no válido")

    print("\nCaja 3: ")
    caja3.mostrarDatos()
    print("Extracción de $20000")
    valor = caja3.extraer(20000)
    if valor != -1:
        print("Saldo restante: $", valor)
    else:
        print("No pudo realizarse la extracción")
    print("Depósito de $ -1")
    caja3.depositar(-1)
    caja3.mostrarDatos()
    if caja3.validarCUIL(caja3.obtenerCUIL()):
        print("CUIL válido")
    else:
        print("CUIL no válido")


