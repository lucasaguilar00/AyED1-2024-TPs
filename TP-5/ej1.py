"""
Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.
"""


def verificar_numero_natural() -> int:
    """
    Precondición: Nada
    Arg: Solicita al usuario ingresar un número natural a través del teclado y verifica que sea válido
    Postcondición: Devuelve un número natural válido y si el ingreso no es válido,
    se indica la razón exacta del error.
    """
    while True:
        try:
            valor = input("Ingrese un número natural: ")
            number = int(valor)

            if number <= 0:
                raise ValueError("El número debe ser positivo mayor a 0")

            return number

        except ValueError as error:
            print(f"Error: {error}. Intente nuevamente.")


if __name__ == "__main__":
    numero = verificar_numero_natural()
    print(f"El número ingresado: '{numero}', es correcto.")
