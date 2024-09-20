"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?
"""


def int_a_romano(numero: int) -> str:
    """
    Convierte un número entero entre 0 y 3999 en su equivalente a número romano.

    Precondiciones:
    el numero debe estar en el rango de 0 a 3999

    Postcondiciones:
    Devuelve una string equivalente al número romano
    """
    if numero < 0 or numero > 3999:
        raise ValueError("El número debe estar entre 0 y 3999")

    numeros_romanos = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    resultado = []
    for valor, romano in numeros_romanos:
        while numero >= valor:
            resultado.append(romano)
            numero -= valor

    return "".join(resultado)


if __name__ == "__main__":
    convertir = int(
        input("Ingrese el número que desea convertir a número romano 'max 3999': ")
    )
    num_romano = int_a_romano(convertir)
    print(num_romano)
