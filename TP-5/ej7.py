"""
Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que 
tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más.
"""

import random as rn


def adivinar_numero() -> int:
    """
    Precondición: nada
    Argumentos: Genera un número random el cual te pide adivinar.
    Postcondición: Retorna un entero con la cantidad de intentos.
    """
    intentos = 0
    numero = rn.randint(1, 500)

    print(
        "Juego de adivinar\n Intenta adivinar el número que elegí entre el número 1 y el 500"
    )

    while True:
        try:
            eleccion = int(input("Ingrese un número: "))
            intentos += 1

            if eleccion == numero:
                return intentos

            if eleccion < numero:
                x = "mayor"
            else:
                x = "menor"

            print(f"El número que intentas adivinar es {x} que {eleccion}.")

        except ValueError:
            print("Ingresaste un dato inválido, cuenta como un intento erróneo.")
            intentos += 1


if __name__ == "__main__":
    n_intentos = adivinar_numero()
    print(f"Felicidades, adivinaste el número después de {n_intentos} intentos")
