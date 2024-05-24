from lista import Lista

def menu():
    try:
        lista = Lista()
        print("Lista creada: ")
        opcion="0"
        while opcion != "5":
            print("""Menu de opciones: 
1. Agregar publicaciones a la colección
2. Informar tipo de publicación para una posición dada de la lista
3. Informar cantidad de publicaciones de cada tipo
4. Mostrar datos de todas las publicaciones de la lista
5. Salir
""")
            opcion=input("Ingrese número de opción: ")
            if opcion == "1":
                lista.agregarPublicacion()
            elif opcion == "2":
                posicion = input("Ingrese posición en la lista: ")
                if posicion.isdecimal():
                    lista.informarTipo(int(posicion))
                else:
                    print("El valor ingresado debe ser un número")
            elif opcion == "3":
                lista.informarCantTipos()
            elif opcion == "4":
                lista.listarDatos()
            elif opcion == "5":
                print("Programa finalizado")
            else:
                print("Opción no válida\n")
    except ValueError:
        print("Error en el formato de los datos")
    except Exception as e:
        print("Ocurrió un error", type(e), e.message)

