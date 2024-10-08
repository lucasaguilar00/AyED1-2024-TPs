"""
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo.
"""

from math import sqrt

def calcular_raiz_cuadrada()-> None:
    """
    Precondición: Nada
    Argumentos: Calcula la raíz cuadrada de un número positivo
    Postcondición: Nada
    """
    while True:
        try:
            numero = int(input("Ingrese un número para calcular su raíz cuadrada: "))
            if numero < 0:
                raise ValueError("\nError - No se puede calcular la raíz cuadrada de un número negativo.")

            raiz_cuadrada = sqrt(numero)
            return numero, raiz_cuadrada

        except ValueError as e:
            print(f"\nError: {e}. Intente nuevamente.")

if __name__ == "__main__":
    numero_calcular, resultado = calcular_raiz_cuadrada()
    print(f"La raíz cuadrada de {numero_calcular} es {resultado:.2f}")