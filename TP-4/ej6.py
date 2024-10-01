"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento 
de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""


def extraer_subcadena_rebanadas(string: str, posicion: int, caracteres: int) -> str:
    """
    Precondición: Recibe una cadena de caracteres, una posicion 'número entero positivo',
    y una cantidad de caracteres que desea extraer 'número entero positivo'..
    La posicion y la cantidad de caracteres no deben ser mayor al largo de la cadena de caracteres 'string'.

    Arg: La función extrae una subcadena de caracteres de una cadena utilizando rebanadas

    Postcondicion: Retorna la extracción de la cadena de caracteres.
    """
    return string[posicion - 1 : posicion + caracteres - 1]


def extraer_subcadena(string: str, posicion: int, caracteres: int) -> str:
    """
    Precondición: Recibe una cadena de caracteres, una posicion 'número entero positivo',
    y una cantidad de caracteres que desea extraer 'número entero positivo'..
    La posicion y la cantidad de caracteres no deben ser mayor al largo de la cadena de caracteres 'string'.

    Arg: La función extrae una subcadena de caracteres de una cadena
    mediante la concatenacion de strings

    Postcondicion: Retorna la extracción de la cadena de caracteres.
    """
    subcadena = ""
    for i in range(posicion - 1, posicion + caracteres - 1):
        subcadena += string[i]
    return subcadena


def main() -> None:
    """
    Precondición: nada
    Arg: Función principal para verificar el comportamiento de ambas
    funciones de extraccion de subcadenas de forma manual
    Postcondición: nada
    """
    while True:
        cadena = input("Ingrese una cadena de caracteres: ")

        # obtiene la posición y cantidad de caracteres que desea extraer
        try:
            posicion = int(input("\nIngresa la posición de inicio: "))
            cantidad = int(input("\nIngresa la cantidad de caracteres a extraer: "))
        except ValueError:
            print("\nEntrada inválida. Por favor, ingresa números enteros.")
            continue

        print("\nCadena actual:", cadena)
        # verifica la funcion que utiliza rebanadas
        subcadena_rebanada = extraer_subcadena_rebanadas(cadena, posicion, cantidad)
        print(f"Subcadena (con rebanadas): '{subcadena_rebanada}'")

        # Verificar la función que es sin rebanadas
        subcadena_sin_rebanada = extraer_subcadena(cadena, posicion, cantidad)
        print(f"Subcadena: '{subcadena_sin_rebanada}'")

        # Preguntar si el usuario desea continuar o salir
        salir = input(
            "\nSi desea salir ingresa 'si', cualquier tecla para continuar: "
        ).lower()
        if salir == "si":
            print("Saliendo.")
            break


if __name__ == "__main__":
    main()
