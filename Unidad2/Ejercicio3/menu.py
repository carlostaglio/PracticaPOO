from GestorVentas import GestorVentas
def menu():
    gestor=GestorVentas()
    print("Gestor creado: ")
    gestor.mostrarArreglo()
    opcion="0"
    while opcion != "7":
        print("""Menu de opciones: 
1. Cargar factura
2. Calcular total facturado para una sucursal
3. Mostrar la sucursal con mayor facturación para un día
4. Mostrar la sucursal con menor facturación
5. Calcular el total facturado de la semana
6. Mostrar arreglo
7. Salir
""")
        opcion=input("Ingrese número de opción: ")
        if opcion == "1":
            try:
                dia=int(input("Ingrese número de día (1 a 7): "))
                sucursal=int(input("Ingrese número de sucursal (1 a 5): "))
                importe=float(input("Ingrese importe de facturación: "))
                gestor.acumularImporte(sucursal, dia, importe)
            except:
                print("Valor no válido")
        elif opcion == "2":
            try:
                sucursal=int(input("Ingrese número de sucursal (1 a 5): "))
                total=gestor.totalSucursal(sucursal)
                if total != -1:
                    print(f"Total facturado por la sucursal {sucursal}: $ {round(total,2)}")
            except:
                print("Valor no válido")
        elif opcion == "3":
            try:
                dia=int(input("Ingrese número de día (1 a 7): "))
                sucursal=gestor.mayorFactDia(dia)
                if total != -1:
                    print(f"Sucursal con mayor facturación para el día {dia}: {sucursal}")

            except:
                print("Valor no válido")
        elif opcion == "4":
            print(f"Sucursal con menor facturación de la semana: {gestor.menorFact()}")
        elif opcion == "5":
            print(f"Total facturado de la semana: $ {round(gestor.totalSemana(),2)}")
        elif opcion == "6":
            gestor.mostrarArreglo()
        elif opcion == "7":
            print("Programa finalizado")
        else:
            print("Opción no válida")

