"""
Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""

from typing import Dict


def crear_dict() -> Dict[int, int]:
    """
    Precondición: Nada
    Argumentos: Crea un diccionario con un rango de valores númericos como clave y el valor es el mismo ** 2
    Postcondición: Retorna el diccionario creado con números y sus cuadrados
    """
    return {i: i**2 for i in range(1, 21)}


if __name__ == "__main__":
    diccionario = crear_dict()
    print(diccionario)
