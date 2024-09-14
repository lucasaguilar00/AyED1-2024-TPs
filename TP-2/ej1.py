"""
1. Desarrollar cada una de las siguientes funciones y escribir un programa que 
permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:

a. Cargar una lista con números al azar de cuatro dígitos. 
La cantidad de elementos también será un número al azar de dos dígitos.

b. Calcular y devolver el producto de todos los elementos de la lista anterior.

c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.

d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]
"""

import random as rn
from functools import reduce

def cargar_lista(x: list) -> list:  # Opción a
    # Carga una lista con elementos y los datos al azar
    x.clear()
    for _ in range(rn.randint(10, 99)):
        x.append(rn.randint(1000, 9999))
    return x


# calcular_producto_ = reduce(lambda a, b: a * b, lista)


def multiplicar(a: int, b: int) -> int:  # Opción b.1
    return a * b


def calcular_producto(x: list) -> int:  # Opcion b
    return reduce(multiplicar, x)


def eliminar_valor(x: list, b: int) -> list:  # Opción c
    # Recorre la lista buscando el valor igresado como parametro para eliminarlo de la lista
    i = 0
    while i < len(x):
        if x[i] == b:
            x.pop(i)
        else:
            i += 1
    return x


def es_capicua(x: list) -> bool:  # Opción d
    # Recorre la lista comparando los indices de ambos lados de 1 en 1 para saber si es capicua
    izquierda = 0
    derecha = len(x) - 1
    while izquierda < derecha:
        if x[izquierda] != x[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True


def opciones():
    print()
    print("Opciones.")
    print("1- Cargar la lista con números al azar")
    print("2- Calcular el producto de los elementos de la lista.")
    print("3- Ingresar un valor que desea eliminar en la lista")
    print("4- Saber si la lista es capicua")
    print("5- Vaciar la lista")
    print("0- Salir.")

lista = []

def menu():
    while True:
        opciones()
        print()
        op = input("Ingrese una opcion: ")
        print()
        if op == "1":
            cargar_lista(lista)
            print(lista)
        elif op == "2":
            if lista:
                producto = calcular_producto(lista)
                print(lista)
                print()
                print(
                    f"El producto de todos los elementos de la lista es = {producto}."
                )
            else:
                print("La lista esta vacía.")
        elif op == "3":
            print("La lista actual: ")
            print(lista)
            print()
            buscar = int(input("Ingrese el valor que desea eliminar: "))
            eliminar_valor(lista, buscar)
            print()
            print("La lista después de eliminar el valor es la siguiente:")
            print()
            print(lista)
        elif op == "4":
            if es_capicua(lista):
                print("Es capicua.")
            else:
                print("No es capicua.")
        elif op == "5":
            lista.clear()
            print("La lista quedo vacía.")
        elif op == "0":
            print("Saliendo.")
            break
        else:
            print("No ingreso una opción válida.")


if __name__ == "__main__":
    menu()
