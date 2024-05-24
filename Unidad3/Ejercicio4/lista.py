from nodo import Nodo
from publicacion import Publicacion
from libro import Libro
from audiolibro import Audiolibro

class Lista:
    __comienzo: Nodo

    def __init__(self):
        self.__comienzo = None

    def __agregarNodo(self, publicacion: Publicacion) -> Nodo:
        nodo = Nodo(publicacion)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def agregarPublicacion(self) -> None:
        tipo = input("Ingrese 1 para agregar un libro o 2 para agregar un audiolibro: ")
        if tipo != "1" and tipo != "2":
            print("El valor ingresado debe ser 1 o 2")
        else:
            titulo = input("Ingrese título: ")
            categoria = input("Ingrese categoría: ")
            autor = input("Ingrese nombre del autor: ")
            precio_base = input("Ingrese precio base: ")
            fecha_edicion = input("Ingrese fecha de edición en formato 'dd-mm-aaaa': ")
            cant_paginas = input("Ingrese la cantidad de páginas: ")
            try:
                precio_base = float(precio_base)
                cant_paginas = int(cant_paginas)
                if tipo == "1":
                    publicacion = Libro(titulo, categoria, precio_base, autor, fecha_edicion, cant_paginas)
                else:
                    tiempo_repr_minutos = int(input("Ingrese el tiempo de representación en minutos: "))
                    narrador = input("Ingrese nombre del narrador: ")
                    publicacion = Audiolibro(titulo, categoria, precio_base, autor, fecha_edicion, cant_paginas, tiempo_repr_minutos, narrador)
                self.__agregarNodo(publicacion)
                print("Publicación creada")
            except:
                print("Debe ingresar valores válidos")
                
    def informarTipo(self, posicion: int) -> None:
        if posicion > 0:
            i = 1
            aux = self.__comienzo
            encontrado = False
            while aux != None and not encontrado:
                if posicion == i:
                    encontrado = True
                    if isinstance(aux.getDato(), Libro):
                        print("La publicación es un libro")
                    elif isinstance(aux.getDato(), Audiolibro):
                        print("La publicación es un audiolibro")
                    else:
                        print("Es una publicación...")
                else:
                    i += 1
                    aux = aux.getSiguiente()
            if not encontrado:
                print("No se encontró una publicación en la posición ingresada")
        else:
            print("El valor de la posición debe ser mayor a cero")

    def informarCantTipos(self) -> None:
        libros = 0
        audiolibros = 0
        aux = self.__comienzo
        while aux != None:
            if isinstance(aux.getDato(), Libro):
                libros += 1
            elif isinstance(aux.getDato(), Audiolibro):
                audiolibros += 1
            else:
                print("Hay una publicación...")
            aux = aux.getSiguiente()
        print("En la lista de publicaciones hay {} libros y {} audiolibros".format(libros, audiolibros))
    
    def listarDatos(self) -> None:
        if self.__comienzo == None:
            print("La lista está vacía")
        else:
            aux = self.__comienzo
            while aux != None:
                publicacion = aux.getDato()
                if isinstance(aux.getDato(), Libro):
                    print("Libro título {}, categoría {}, importe: $ {:.2f}".format(publicacion.getTitulo(), publicacion.getCategoria(), publicacion.getImporte()))
                elif isinstance(aux.getDato(), Audiolibro):
                    print("Audiolibro título {}, categoría {}, importe: $ {:.2f}".format(publicacion.getTitulo(), publicacion.getCategoria(), publicacion.getImporte()))
                else:
                    print("Hay una publicación...")
                aux = aux.getSiguiente()