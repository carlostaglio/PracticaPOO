
class CajaAhorro():
    __nroCuenta: str
    __cuil: str
    __apellido: str
    __nombre: str
    __saldo: float

    def __init__(self, num: int, cuil: str, apellido: str, nombre: str, saldo: float):
        self.__nroCuenta = num
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo
    
    def obtenerCUIL(self) -> str:
        """Retorna el CUIL del titular de la cuenta"""
        return self.__cuil
    
    def obtenerNombre(self) -> str:
        """Retorna el nombre del titular de la cuenta"""
        return self.__nombre
    
    def obtenerApellido(self) -> str:
        """Retorna el apellido del titular de la cuenta"""
        return self.__apellido
    
    def obtenerSaldo(self) -> float:
        """Retorna el saldo disponible"""
        return self.__saldo

    def mostrarDatos(self) -> None:
        """Muestra los datos de la cuenta"""
        print("Cuenta número:", self.__nroCuenta)
        print(f"Titular: {self.__apellido} {self.__nombre}")
        print("Número de CUIL:", self.__cuil)
        print("Saldo disponible: $", round(self.__saldo, 2))

    def extraer(self, importe: float) -> float:
        """Realiza la extracción de dinero de la cuenta dado un importe y retorna el saldo restante en caso exitoso y -1 en caso de error"""
        if self.__saldo >= importe and importe > 0:
            self.__saldo -= importe
            print("Operación exitosa")
            return self.__saldo
        else:
            print("Saldo insuficiente")
            return -1

    def depositar(self, importe: float) -> None:
        """Realiza el depósito de dinero de la cuenta dado un importe"""
        if importe > 0:
            self.__saldo += importe
        else:
            print("Valor del importe a depositar incorrecto")

    def validarCUIL(self, cuil: str) -> bool:
        """Verifica si el cuil ingresado es válido. Retorna verdadero en caso afirmativo y falso en caso negatvo"""
        cuil = cuil.replace("-","") #Remover guiones
        if len(cuil) == 11 and cuil.isdecimal(): #Verifica si los valores del CUIL son números
            if cuil[:2] == '23':
                validez = cuil[-1] in ("4", "9") #Verdadero si el último valor del cuil es "4" o "9"
            elif cuil[:2] in ("20", "27", "30"):
                mult=[5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
                total=0
                for i in range(len(cuil)-1):
                    total = total + int(cuil[i]) * mult[i]
                resto = total % 11
                if resto == 0:
                    validez = str(resto) == cuil[-1]
                elif resto == 1 and cuil[:2] != "30":
                    validez = False #Ya que los primeros dos dígitos no son "23"
                else:
                    z = 11 - resto
                    validez = str(z) == cuil[-1]
            else:
                print("Valor XY incorrecto")
                validez = False
        else:
            print("Longitud del CUIL incorrecta")
            validez = False
        return validez