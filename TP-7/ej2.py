"""
Desarrollar una función que reciba un número binario y lo devuelva convertido a
base decimal.
"""
def bin_a_decimal(binario: int) -> int:
    """
    Precondición: debe recibir un número binario
    Argumentos: Convierte el número binario a decimal
    Postcondición: Retorna el número decimal correspondiente
    """
    decimal = 0
    potencia = 0

    while binario > 0:

        num = binario % 10    # Obtiene el último número

        decimal += num * (2 ** potencia) #se multiplica el numero * "2" elevado a la posicion del numero (derecha a izquierda)

        binario //= 10    # Saca el último número

        potencia += 1   # Eleva la potencia por la siguiente posición

    return decimal

if __name__ == "__main__":
    while True:
        try:
            num_bin = int(input("Ingrese un número binario: "))
            num_decimal = bin_a_decimal(num_bin)

            print(f"El número binario {num_bin}, en decimal es el número {num_decimal}.")

        except ValueError:
            print("Ingrese un dato número que sea válido.")