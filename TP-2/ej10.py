"""
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. El proceso deberá realizarse utilizando
la función filter(). Imprimir las dos listas por pantalla. 
"""

import random as rn


def cargar_lista() -> list:  # Opción a
    # Carga una lista con elementos y los datos al azar
    lista_x = [rn.randint(1, 100) for _ in range(rn.randint(1, 100))]
    return lista_x


if __name__ == "__main__":
    while True:
        salir = input(
            "Ingrese 0 para salir, presione cualquier otra tecla para continuar: "
        )
        if salir == "0":
            print("Saliendo..")
            break

        lista = cargar_lista()
        lista_impares = list(filter(lambda i: i % 2 != 0, lista))
        # casteo el objeto a lista y utiliza una funcion lambda para filtrar solamente los números impares

        print(f"La primer lista es:\n{lista}\n")
        print(f"La lista con los números impares es:\n{lista_impares}")
