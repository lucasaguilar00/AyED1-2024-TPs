"""
Realizar una función que devuelva el resto de dos números enteros, utilizando restas sucesivas.
"""


def resto(a: int, b: int) -> int:
    """
    Precondición: Los parametros 'a' y 'b' deben ser números enteros, 'b' no puede ser 0.
    Argumento: Resta 'b' de 'a' de forma sucesiva hasta no poder restar más, para obtener el resto de ambos parametros.
    Postcondición: Retorna un número entero que es el resto de ambos parametros.
    """

    signo_divisor = 1 if b > 0 else -1

    a = abs(a)
    b = abs(b)

    while a >= b:
        a -= b

    if signo_divisor == -1:
        return -a

    return a


if __name__ == "__main__":
    while True:
        try:
            dividendo = int(input("Ingrese un número: "))
            divisor = int(input("Ingrese por cuanto quiere dividir: "))
            if divisor == 0:
                print("El divisor no puede ser cero.")
                continue
        except ValueError as e:
            print(f"Error - Ingrese un dato númerico que sea válido. {e}")
            continue

        resultado_resto = resto(dividendo, divisor)

        print(f"El resto de '{dividendo}' y '{divisor}' es = {resultado_resto} ")
