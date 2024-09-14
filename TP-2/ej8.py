"""
Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200
"""

import random as rn


"""
def cargar_lista(x: list) -> list:  # Opción a
    # Carga una lista con elementos y los datos al azar
    x.clear()
    for _ in range(rn.randint(1, 15)):
        x.append(rn.randint(100, 200))
    return x
"""


def cargar_lista() -> list:  # Opción a
    # Carga una lista con elementos y los datos al azar
    lista_x = [rn.randint(100, 200) for _ in range(rn.randint(1, 15))]
    return lista_x


def lista_impares(a: list) -> list:

    return [i for i in a if i >= 100 and i <= 200 and i % 2 != 0]


lista = []

if __name__ == "__main__":
    while True:
        op = input(
            "Para detener el programa ingrese 0, para continuar cualquier tecla: "
        )
        if op == "0":
            print("Saliendo del programa.")
            break

        lista = cargar_lista()

        print("La lista original es:\n")
        print(f"{lista}\n")

        impares = lista_impares(lista)
        print(
            "La lista con los números impares entre 100 y 200 que contenia la lista anterior es:\n"
        )
        print(impares)
