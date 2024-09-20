"""
Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
"""

import random as rn


def cargar_lista(var: list) -> list:  # Opción A
    """
    Precondiciones:
    var debe ser una lista vacía o contener elementos

    Postcondiciones:
    Se carga la lista con un número N de elementos aleatorios (entre 1 y 100)
    donde N es un entero positivo que ingresa el usuario
    Devuelve la lista modificada
    """
    # Carga lista con la cantidad de indices que desea con números random.
    while True:
        try:
            # Utiliza try para prevenir un posible error que detenga el programa
            elementos = int(input("Ingrese la cantidad de elementos que desea tener: "))
            if elementos > 0:
                for _ in range(elementos):
                    var.append(rn.randint(1, 100))
                return var
            else:
                print("Introduzca un número mayor a 0.")
        except ValueError:
            print("Ingrese un número entero válido")


def hay_repetidos(var: list) -> bool:  # Opción B
    """
    Precondiciones:
    la lista es de números enteros.

    Postcondiciones:
    Devuelve True si la lista contiene algún elemento repetido,
    o False si es lo contrario
    """
    # Verifica si hay un elemento repetido en la lista comparando el largo de la lista con un set que no permite datos repetidos.
    return len(var) != len(set(var))


def lista_unicos(var: list) -> list:  # Opción C
    """
    Precondiciones:
    la lista es de números enteros.
    Postcondiciones:
    devuelve una nueva lista que contiene los elementos únicos de la lista,
    sin importar el orden
    """
    # Devuelve la lista sin elementos repetidos
    return list(set(var))


def opciones():
    print("Menú de opciones.")
    print("")
    print("1-Cargar lista al azar (Elegir la cantidad de elementos).")
    print("2-Informar si la lista tiene elementos repetidos.")
    print("3-Obtener la lista con elementos únicos.")
    print("4-Vaciar lista.")
    print("0.Salir")


lista = []  # Inicio lista vacía


def menu():
    while True:
        opciones()
        print("")
        op = input("Ingresa una opción.")
        print("")
        if op == "1":
            cargar_lista(lista)
            print(lista)
        elif op == "2":
            rep = hay_repetidos(lista)
            print(rep)
            if rep:
                print("Hay elementos repetidos")
            else:
                print("No hay elementos repetidos.")
        elif op == "3":
            new_lista = lista_unicos(lista)
            print("La antigua lista es:")
            print(lista)
            print("")
            print("La nueva lista es:")
            print(new_lista)
        elif op == "4":
            lista.clear()
            print("La lista ha sido vaciada.")
        elif op == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
