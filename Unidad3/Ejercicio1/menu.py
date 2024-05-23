from gestorEdificio import GestorEdificio

def menu():
    try:
        gestor = GestorEdificio()
        print("Gestor creado: ")
        gestor.cargarDatos()
        opcion="0"
        while opcion != "6":
            print("""Menu de opciones: 
1. Informar propietarios de los departamentos de un edificio
2. Informar superficie cubierta total de un edificio
3. Informar superficie total cubierta de un departamento y porcentaje respecto del total del edificio
4. Contar departamentos con 3 dormitorios y más de un baño para un edificio y piso dados
5. Mostrar datos
6. Salir
""")
            opcion=input("Ingrese número de opción: ")
            if opcion == "1":
                nombre_edif=input("Ingrese nombre del edificio: ")
                gestor.mostrarPropietariosEdificio(nombre_edif) 
            elif opcion == "2":
                id_edif = input("Ingrese número de id del edificio: ")
                if id_edif.isdigit():
                    gestor.getSuperficieCubierta(int(id_edif))
                else:
                    print("El valor ingresado debe ser un número")
            elif opcion == "3":
                nombre_prop=input("Ingrese nombre del propietario: ")
                gestor.informarSuperfCubiertaPropietario(nombre_prop)
            elif opcion == "4":
                id_edif = input("Ingrese número de id del edificio: ")
                num_piso = input("Ingrese número de piso: ")
                if id_edif.isdigit() and num_piso.isdigit():
                    gestor.cantidadDepartamentosCondicion(int(id_edif), int(num_piso))
                else:
                    print("Los valores ingresados debe ser números")
            elif opcion == "5":
                for edificio in gestor.getListaEdificios():
                    print(edificio)
            elif opcion == "6":
                print("Programa finalizado")
            else:
                print("Opción no válida\n")
    except FileNotFoundError:
        print("Error en la apertura del archivo, no se encontró en la dirección especificada")
    except ValueError:
        print("Error en el formato de los datos del archivo")
    except Exception as e:
        print("Ocurrió un error", type(e), e.message)

