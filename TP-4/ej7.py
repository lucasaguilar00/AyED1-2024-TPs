"""
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. 
Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""


def eliminar_subcadena_rebanadas(string: str, posicion: int, caracteres: int) -> str:
    """
    Precondición: Recibe una cadena de caracteres, una posicion 'número entero positivo',
    y una cantidad de caracteres que desea eliminar 'número entero positivo'..
    La posicion y la cantidad de caracteres no deben ser mayor al largo de la cadena de caracteres 'string'.

    Arg: La función elimina una subcadena de caracteres de una cadena utilizando rebanadas

    Postcondicion: Retorna la cadena original sin la subcadena seleccionada.
    """
    return string[: posicion - 1] + string[posicion + caracteres :]


def eliminar_subcadena(string: str, posicion: int, caracteres: int) -> str:
    """
    Precondición: Recibe una cadena de caracteres, una posicion 'número entero positivo',
    y una cantidad de caracteres que desea eliminar 'número entero positivo'..
    La posicion y la cantidad de caracteres no deben ser mayor al largo de la cadena de caracteres 'string'.

    Arg: La función elimina una subcadena de caracteres de una cadena
    mediante la concatenacion de strings

    Postcondicion: Retorna la cadena sin la subcadena seleccionada
    """
    subcadena = ""
    for i in range(len(string)):
        if i < posicion - 1 or i > posicion + caracteres - 1:
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
            cantidad = int(input("\nIngresa la cantidad de caracteres a eliminar: "))
        except ValueError:
            print("\nEntrada inválida. Por favor, ingresa números enteros.")
            continue

        print("\nCadena actual:", cadena)
        # verifica la funcion que utiliza rebanadas
        cadena_rebanada = eliminar_subcadena_rebanadas(cadena, posicion, cantidad)
        print(f"Nueva cadena (con rebanadas): '{cadena_rebanada}'")

        # Verificar la función que es sin rebanadas
        cadena_sin_rebanada = eliminar_subcadena(cadena, posicion, cantidad)
        print(f"Nueva cadena: '{cadena_sin_rebanada}'")

        # Preguntar si el usuario desea continuar o salir
        salir = input(
            "\nSi desea salir ingresa 'si', cualquier tecla para continuar: "
        ).lower()
        if salir == "si":
            print("Saliendo.")
            break


if __name__ == "__main__":
    main()
