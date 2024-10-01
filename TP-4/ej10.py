"""
Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función.
"""

from typing import Tuple


def reemplazar_palabra(
    string: str, reemplazar: str, nueva_palabra: str
) -> Tuple[str, int]:
    """
    Precondición: Recibe una cadena de caracteres, una palabra a reemplazar(str) y una palabra
    reemplazante(str), ambas no deben estar vacias
    Arg: Reemplaza todas las apariciones de la palabra que sean igual a 'reemplazar' por 'nueva_palabra'
    en la cadena dada. Devuelve la cadena modificada y la cantidad de reemplazos realizados.
    Postcondición: Devuelve una tupla con la cadena modificada y el número de reemplazos que se realizaron.
    """

    palabras = string.split()  # divide cada palabra en un indice diferente de una lista

    reemplazos = 0

    # lista con las palabras que se va a convertir en la cadena resultante final.
    lista_palabras = []

    for palabra in palabras:
        if palabra == reemplazar:
            lista_palabras.append(nueva_palabra)
            reemplazos += 1
        else:
            lista_palabras.append(palabra)

    cadena_final = " ".join(lista_palabras)

    return cadena_final, reemplazos


def main() -> None:
    """
    Precondicion: nada
    Postcondición: nada
    """

    frase = "Tengo un perro negro y le gusta correr por el patio mientras juega con otros perros y busca su pelota"

    print(frase)
    buscar = input("\nIngrese la palabra que desea reemplazar: ")

    reemplazo = input("\nIngrese la palabra que la va a reemplazar: ")

    frase_modificada, cantidad_reemplazos = reemplazar_palabra(frase, buscar, reemplazo)

    print(f"\nnLa frase original era:\n{frase}")
    print(f"\La frase modificada es:\n{frase_modificada}")
    print(f"\nLa cantidad de reemplazos que hubo: {cantidad_reemplazos}")


if __name__ == "__main__":
    main()
