"""
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio.
"""

from typing import Tuple


def encaja_ficha(ficha_a: Tuple[int, int], ficha_b: Tuple[int, int]) -> bool:
    """
    Precondición: Recibe como parametro dos tuplas que contienen 2 números enteros cada una.
    Argumentos: Verifica si comparten al menos una coincidencia en algun dato de la tupla
    Postcondición: Retorna un booleano con el resultado.
    """
    set_ficha1 = set(ficha_a)
    set_ficha2 = set(ficha_b)

    return not set_ficha1.isdisjoint(set_ficha2)


def main() -> None:
    """
    Precondición: Nada
    Argumentos: Crea una prueba para válidar la función.
    Postcondición: Nada
    """
    while True:
        try:
            primer_ficha = tuple(
                map(
                    int,
                    input(
                        "Ingrese los valores de la primera ficha (separados por un espacio): "
                    ).split(),
                )
            )
            segunda_ficha = tuple(
                map(
                    int,
                    input(
                        "Ingrese los valores de la segunda ficha (separados por un espacio): "
                    ).split(),
                )
            )
        except ValueError:
            print(
                "Error - Asegúrese de ingresar dos números enteros separados por un espacio."
            )

        else:
            break

    print(f"Ficha 1: {primer_ficha} \nFicha 2: {segunda_ficha}")

    if encaja_ficha(primer_ficha, segunda_ficha):
        print("Las fichas encajan.")
    else:
        print("Las fichas no encajan.")


if __name__ == "__main__":
    main()
