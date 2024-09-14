"""
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones 
relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""

import random as rn
from functools import reduce


def cargar_lista(var: list) -> list:
    # Vacia la lista si esta cargada y le agrega elementos nuevos con números enteros de 1 a 10.
    var.clear()
    var.extend([rn.randint(1, 10) for _ in range(rn.randint(1, 10))])
    return var


def normalizar_lista(var: list) -> list:
    total = reduce(
        lambda a, b: a + b, var
    )  # Suma todos los elementos que contiene la lista
    if total == 0:
        raise ValueError("La suma de todos los elementos no puede ser 0.")
    return [i / total for i in var]  # normaliza cada elemento de la lista


def verificar_programa():
    lista = []
    cargar_lista(lista)
    # Carga una lista random
    print("La lista original es:")
    print(lista)

    try:
        lista_normalizada = normalizar_lista(lista)
        print("La lista normalizada es:")
        print(lista_normalizada)
        print(
            f"La suma de los elementos de la lista es: {reduce(lambda a,b: a + b, lista_normalizada)}"
        )
        # Muestra que la suma de la nueva lista normalizada da como total 1.0
    except ValueError:
        print("No se puede normalizar una lista que su suma total es 0.")
        # Posible error por si es una lista que no se puede normalizar (Este caso no, porque funciona con random)


if __name__ == "__main__":
    verificar_programa()
