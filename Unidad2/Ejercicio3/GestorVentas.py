import numpy as np

class GestorVentas:
    __arreglo:np.ndarray

    def __init__(self) -> None:
        self.__arreglo=np.zeros((5,7),dtype=float)
        #Forma alternativa para generar un arreglo bidimensional
        #self.__arreglo=[[0 for i in range(7)] for i in range (5)]

    def mostrarArreglo(self):
        print(*self.__arreglo, sep="\n")

    def obtenerArreglo(self) -> np.ndarray:
        """Retorna el arreglo de facturacion de tamaño 5x7"""
        return self.__arreglo
    
    def acumularImporte(self, sucursal:int, dia:int, importe:float) -> None:
        """Acumula el importe de facturación para un día y sucursal dados"""
        if sucursal >=1 and sucursal <=5 and dia >=1 and dia <=7 and importe > 0:
            self.__arreglo[sucursal-1][dia-1]+=importe
        else:
            print ("Alguno de los valores no es válido")

    def totalSucursal(self, sucursal:int) -> float:
        """Retorna el total de facturación para una sucursal dado su número"""
        total=0
        if sucursal >=1 and sucursal <=5:
            for montoDia in self.__arreglo[sucursal-1]:
                total+=montoDia
            return total
        else:
            print ("Número de sucursal no válido")
            return -1
        
    def mayorFactDia(self, dia:int) -> int:
        """Retorna el número de sucursal de aquella con mmayor facturación para un día dado"""
        maximo=0
        indice=-1
        if dia >=1 and dia <=7:
            for i in range(len(self.__arreglo)):
                if self.__arreglo[i][dia-1] > maximo:
                    maximo=self.__arreglo[i][dia-1]
                    indice=i
            return indice + 1
        else:
            print ("Número de día no válido")
            return indice
        
    def menorFact(self) -> int:
        """Retorna el número de sucursal de aquella que tuvo la menor facturación de la semana"""
        minimo=999999999
        indice=-1
        for i in range(len(self.__arreglo)):
            total=0
            for montoDia in self.__arreglo[i]:
                total+=montoDia
            if montoDia < minimo:
                minimo=montoDia
                indice=i
        return indice+1
        
    def totalSemana(self) -> float:
        """Retorna el total de facturación de la semana"""
        total=0
        for sucursal in self.__arreglo:
            for montoDia in sucursal:
                total+=montoDia
        return total
    
