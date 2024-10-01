"""
Realizar una función que reciba como parámetros dos cadenas de caracteres 
conteniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
"""


def sumar_cadenas(cadena_a: str, cadena_b: str) -> float:
    """
    Precondición: Ambas cadenas deben contener números reales
    Argumento: Suma dos cadenas que contienen números reales.
    Postcondición: Devuelve la suma de ambos números reales o -1
    en el caso de que alguna cadena sea inválida
    """
    try:
        numero_a = float(cadena_a)
        numero_b = float(cadena_b)
        return numero_a + numero_b

    except ValueError:
        return -1


# Programa principal para probar la función
if __name__ == "__main__":
    """
    Pre: Nada
    Post: Nada
    """
    string_a = input("Ingrese el primer número real: ")
    string_b = input("Ingrese el segundo número real: ")

    resultado = sumar_cadenas(string_a, string_b)

    if resultado == -1:
        print(
            f"Error: Resultado {resultado}, alguna de las cadenas no contiene un número válido."
        )
    else:
        print(f"La suma de los números es: {resultado}")
