"""
Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado.
"""

from typing import Dict


def crear_dict(numero: int) -> Dict[int, int]:
    """
    Precondición:Recibe un número entero como parametro.
    Argumentos: Crea un diccionario con la tabla de multiplicar del parametro obtenido
    Postcondición: Retorna un diccionario con clave:valor = números enteros
    """
    return {i: numero * i for i in range(1, 13)}


if __name__ == "__main__":
    while True:
        try:
            tabla = int(input("Ingrese el número para hacer la tabla del: "))
        except ValueError:
            print("Error - Ingrese un número entero válido.")
        else:
            break
    diccionario_tabla = crear_dict(tabla)
    for index, resultado in diccionario_tabla.items():
        print(f"{tabla} x {index} = {resultado}")
