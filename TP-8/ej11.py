"""
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""

from typing import Dict


def contar_vocales(palabra: str) -> Dict[str, int]:
    """
    Precondición: El parametro palabra es una str.
    Argumentos: Cuenta cuántas vocales contiene una palabra.
    Postcondición: Retorna un diccionario con las vocales como claves y la cantidad repetida de cada una.
    """
    vocales = "aeiou"
    cuenta_vocales = {vocal: 0 for vocal in vocales}

    for caracter in palabra.lower():
        if caracter in cuenta_vocales:
            cuenta_vocales[caracter] += 1

    return cuenta_vocales


def procesar_frase(frase: str) -> None:
    """
    Precondición: Frase es un conjunto de strings.
    Argumentos: Lee la frase para luego llamar a la funcion contar_vocales
    por cada palabra de esta misma y muestra en pantalla el resultado de la palabra correspondiente.
    Postcondición: Nada
    """

    palabras = frase.split()

    for palabra in palabras:
        cuenta_vocales = contar_vocales(palabra)
        print(f"Palabra: {palabra}\nVocales: {cuenta_vocales}\n")


def main() -> None:
    while True:
        frase = input("Ingrese su frase: ")
        procesar_frase(frase)
        salir = input("Salir 's' o 'n': ")
        if salir.lower() == "s":
            break
