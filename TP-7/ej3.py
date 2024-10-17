"""
Escribir una función que devuelva la suma de los N primeros números naturales
"""


def suma_numeros(numero: int) -> int:
    """
    Precondición: Recibe un número natural
    Argumentos: Verifica que sea un número válido
    Postcondición: Retorna la suma de los primeros "N" números naturales
    """

    if numero < 1:
        raise ValueError("El número debe ser un número entero positivo.")

    return sum(range(1, numero + 1))


if __name__ == "__main__":
    while True:
        try:
            numeros = int(
                input(
                    "Ingrese un número para sumar los primeros 'N' numeros naturales: "
                )
            )
            suma = suma_numeros(numeros)
            print(f"La suma de los primeros {numeros} numeros naturales da: {suma}")
        except ValueError:
            print("Error - Ingreso un dato inválido, ingrese un número natural.")
