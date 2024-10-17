"""
Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
utilizar cadenas de caracteres.
"""


def contar_digitos(digito: int) -> int:
    """
    Precondición: El valor recibido tiene que ser un número entero
    Argumentos: Calcula la cantidad de digitos que posee el número ingresado
    Postcondición: Retorna la cantidad de digitos
    """

    if digito == 0:
        return 1

    digito = abs(digito)
    digitos = 0

    while digito > 0:
        digito //= 10
        digitos += 1

    return digitos


if __name__ == "__main__":
    while True:
        try:
            numero = int(input("Ingrese un número para contar cuantos digitos tiene: "))
            cant_digitos = contar_digitos(numero)

            print(f"El número {numero} posee {cant_digitos} digitos.")
        except ValueError:
            print("Ingrese un valor que sea númerico.")
