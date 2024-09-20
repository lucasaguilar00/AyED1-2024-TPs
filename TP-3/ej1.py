"""
1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar
su funcionamiento, imprimiendo la matriz luego de invocar a cada función:

a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.

NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
sea el valor ingresado.
"""

# sin terminar el H, i, J por ahora.


def cargar_matriz() -> list[list[int]]:  # opcion a
    """
    Precondiciones:
    idk

    Postcondiciones:
    carga una matriz de números enteros de tamaño N x N que ingresa el usuario y devuelve la matriz que se generó
    """
    # Carga una matriz de forma manual, tamaño y elementos enteros, no recibe parametros, retorna una matriz de números enteros.
    n = int(
        input(
            "Ingrese el tamaño de la matriz (La lista interna comparte el mismo tamaño): "
        )
    )

    # Bucle para ingresar los datos fila por fila
    print()
    matriz = [
        [int(input(f"Fila {i+1}, ingrese el elemento {j+1}: ")) for j in range(n)]
        for i in range(n)
    ]

    return matriz


def ordenar_filas(matriz: list[list[int]]):  # opcion b
    """
    Precondiciones:
    matriz es una lista de listas que contiene números enteros

    Postcondiciones:
    ordena cada fila de la matriz de forma ascendente
    """
    for fila in matriz:
        fila.sort()  # ordena cada fila en forma ascendente


def intercambiar_filas(
    matriz: list[list[int]], fila1: int, fila2: int
) -> None:  # opcion c
    """
    Precondiciones:
    matriz es una lista de listas que contiene números enteros
    fila1 y fila2 son enteros que representan los indices de las filas

    Postcondiciones:
    intercambia las filas 'fila1' y 'fila2' en la matriz.
    si los índices son inválidos, se avisa mediante un mensaje de error
    """
    # ajustado -1 para coincidir con los indices.
    fila1 -= 1
    fila2 -= 1
    # Verificar que los índices de las filas sean válidos
    if not (fila1 >= 0 and fila1 < len(matriz) and fila2 >= 0 and fila2 < len(matriz)):
        print("Error: Uno o ambos números de fila son inválidos.")
    else:
        # Intercambiar las filas
        matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]


def intercambiar_columnas(
    matriz: list[list[int]], col1: int, col2: int
) -> None:  # Opcion d
    """
    Precondiciones:
    matriz es una lista de listas que contiene núeros enteros
    col1 y col2 son enteros que representan índices de columnas

    Postcondiciones:
    intercambia los elementos en las columnas 'col1' y 'col2' de la matriz.
    si los índices son inválidos, se avisa mediante un mensaje de error
    """
    # ajustado -1 para coincidir con los indices.
    col1 -= 1
    col2 -= 1
    # Verificar que los índices de las columnas sean válidos
    if not (
        col1 >= 0 and col1 < len(matriz[0]) and col2 >= 0 and col2 < len(matriz[0])
    ):
        print("Error: Uno o ambos números de columna son inválidos.")
    else:
        # Recorrer cada fila e intercambiar los elementos en las columnas {col1} y {col2}
        for fila in matriz:
            fila[col1], fila[col2] = fila[col2], fila[col1]


def transponer_matriz(matriz: list[list[int]]) -> list[list[int]]:  # opcion e
    """
    Precondiciones:
    matriz es una lista de listas que contiene númerosenteros

    Postcondiciones:
    devuelve una nueva matriz que es la transpuesta de la matriz original,
    intercambiando filas por columnas.
    """
    largo = len(matriz)  # Tamaño de la matriz (las filas tienen el mismo largo)

    # Crear la matriz transpuesta intercambiando los indices
    matriz_transpuesta = [[matriz[j][i] for j in range(largo)] for i in range(largo)]
    return matriz_transpuesta


def promedio_fila(matriz: list[list[int]], numero_fila: int) -> float:  # Opción f
    """
    Precondiciones:
    matriz es una lista de listas que contiene números enteros
    numero_fila es un int que representa el índice de la fila

    Postcondiciones:
    devuelve el promedio de los elementos en la fila especificada
    si el índice de la fila es inválido, se lanza una excepción
    """
    numero_fila -= 1  # ajustado -1 para coincidir con los indices.
    # Verificar que el índice de la fila sea válido
    if numero_fila < 0 or numero_fila >= len(matriz):
        raise IndexError("El número de fila esta fuera del rango.")

    fila = matriz[numero_fila]
    promedio = sum(fila) / len(fila)

    return promedio


def porcentaje_impares_columna(
    matriz: list[list[int]], columna: int
) -> float:  # opción g
    """
    Precondiciones:
    matriz es una lista de listas que contiene números enteros
    columna es un número entero que representa el índice de la columna

    Postcondiciones:
    devuelve el porcentaje de elementos impares en la columna especificada
    Si el índice de la columna es inválido, se lanza una excepción
    """
    columna -= 1  # ajusta el indice

    # verificar que el índice de la columna sea válido
    if columna < 0 or columna >= len(matriz[0]):
        raise IndexError("El número de columna esta fuera de rango.")

    # Calcular el porcentaje de elementos impares
    porcentaje_impares = (
        sum(i % 2 != 0 for i in matriz[columna]) / len(matriz[columna])
    ) * 100

    return porcentaje_impares


def menu():
    opciones = [
        "Cargar una matriz de NxN",
        "Ordenar listas de manera ascendente",
        "Intercambiar filas de la matriz",
        "Intercambiar columnas de la matriz",
        "Trasponer matriz",
        "Calcular promedio de una fila",
        "Calcular porcentaje de elementos impares en una fila",
        "Determinar si la matriz es simétrica con respecto a su diagonal principal",
        "Determinar si la matriz es simétrica con respecto a su diagonal secundaria",
        "Determinar qué columnas de la matriz son palíndromos (capicúas)",
        "Salir",
    ]
    matrix = []

    while True:
        print("\nMenú de opciones:")
        for num, opcion in enumerate(opciones):
            print(f"{num + 1}. {opcion}.")
        op = input("\nIngrese una opción: ")
        if op == "1":
            try:
                matrix = cargar_matriz()
                for fila in matrix:
                    print(fila)
            except ValueError:
                print("El valor ingresado no es válido.\n")
        elif op == "2":
            if matrix:
                ordenar_filas(matrix)
                print("Matriz con filas ordenadas de forma ascendente:")
                for fila in matrix:
                    print(fila)
            else:
                print("La matriz esta vacia.")
        elif op == "3":
            if matrix:
                fila1 = int(input("Ingrese el número de la primera fila: "))
                fila2 = int(input("Ingrese el número de la segunda fila: "))
                intercambiar_filas(matrix, fila1, fila2)
                for fila in matrix:
                    print(fila)
            else:
                print("La matriz esta vacia.")
        elif op == "4":
            if matrix:
                col1 = int(input("Ingrese el número de la primera columna: "))
                col2 = int(input("Ingrese el número de la segunda columna: "))
                intercambiar_columnas(matrix, col1, col2)
                for fila in matrix:
                    print(fila)
            else:
                print("La matriz esta vacia.")
        elif op == "5":
            if matrix:
                matrix = transponer_matriz(matrix)
                for fila in matrix:
                    print(fila)
            else:
                print("La matriz esta vacia.")
        elif op == "6":
            if matrix:
                fila = int(
                    input("Ingrese el número de la fila para calcular su promedio: ")
                )
                promedio = promedio_fila(matrix, fila)
                print(f"El promedio de la fila {fila} es: {promedio}")
            else:
                print("La matriz esta vacia.")
        elif op == "7":
            if matrix:
                columna = int(input("Ingrese el número de la columna: "))
                porcentaje = porcentaje_impares_columna(matrix, columna)
                print(
                    f"El porcentaje de elementos impares en la columna {columna} es: {porcentaje}%"
                )
            else:
                print("La matriz esta vacia.")
        elif op == "8":
            pass
        elif op == "9":
            pass
        elif op == "10":
            pass
        elif op == "11":  # Salir
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
