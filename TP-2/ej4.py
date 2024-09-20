"""
Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada.
"""

import random as rn


def cargar_lista(var: list) -> list:
    """
    Precondiciones:
    la lista puede estar vacía o contener elementos.

    Postcondiciones:
    Se vacía la lista y se carga con un número aleatorio de elementos
    (entre 1 y 20), cada uno es número entero de dos dígitos
    (entre 1 y 99) y devuelve la lista modificada
    """
    # Vacia la lista si esta cargada y le agrega elementos nuevos con números enteros de 2 digitos max
    var.clear()
    for _ in range(rn.randint(1, 20)):
        var.append(rn.randint(1, 99))
    return var


def eliminar_valores(var: list, varoles_x_eliminar: list) -> None:
    """
    Precondiciones:
    la lista debe contiene enteros.
    varoles_x_eliminar es una lista de enteros que contiene los valores a eliminar de la lista 'var'

    Postcondiciones:
    Se eliminan todos los elementos en la lista que son iguales a los valores de
    la lista varoles_x_eliminar.
    """
    # Elimina los elementos que sean iguales a los valores de la otra lista.
    for i in varoles_x_eliminar:
        while i in var:
            var.remove(i)


lista_original = []  # Lista original
valores_eliminar = []  # Lista con los valores a eliminar de la lista original

if __name__ == "__main__":
    while True:
        print("Iniciando el programa.")
        cargar_lista(lista_original)
        cargar_lista(valores_eliminar)
        # Carga las listas

        print("La lista original:")
        print(lista_original)
        print()  # Lista original

        print("La lista con valores a eliminar.")
        print(valores_eliminar)
        print()  # Lista con valores que eliminar en la original

        eliminar_valores(lista_original, valores_eliminar)
        print(lista_original)  # Lista después de eliminar los valores

        seguir = input("Sí desea parar el programa ingrese (0) .")
        if seguir == "0":
            break
