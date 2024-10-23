"""
Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.
"""


def producto(a: int, b: int) -> int:
    """
    Precondición: Los parametros 'a' y 'b' deben ser números enteros
    Argumento: Suma 'a' por si mismo de forma sucesiva 'b' veces, para obtener el producto de ambos parametros.
    Postcondición: Retorna un número entero que es el producto de ambos parametros.
    """
    resultado = 0

    for _ in range(abs(b)):
        resultado += a

    if b < 0:
        resultado = -resultado

    return resultado


if __name__ == "__main__":
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            multiplicador = int(input("Ingrese por cuanto quiere multiplicarlo: "))
        except ValueError:
            print("Ingrese un dato númerico que sea válido.")
            continue

        resultado_producto = producto(numero, multiplicador)

        print(
            f"El producto de '{numero}' y '{multiplicador}' es = {resultado_producto} "
        )
