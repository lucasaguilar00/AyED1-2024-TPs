"""
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""


def ultimos_n_caracteres(string: str, n: int) -> str:
    """
    Devuelve una subcadena con los últimos N caracteres de la cadena dada.

    Precondiciones:
    cadena es una cadena de caracteres.
    n debe ser un entero mayor o igual a 0.

    Postcondiciones:
    Devuelve una subcadena con los últimos N caracteres de la cadena.
    """
    if n < 0:
        raise ValueError("El número debe ser mayor o igual a 0")

    return string[-n:] if n <= len(string) else string


if __name__ == "__main__":
    cadena = input("Ingrese una palabra: ")
    ultimos = int(
        input("Ingrese el número de los ultimos caracteres que desea obtener: ")
    )
    print(ultimos_n_caracteres(cadena, ultimos))
