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

#sin terminar el H, i, J por ahora.
#Agregar un menu también para verificar cada opción.

def cargar_matriz() -> list[list[int]]:  # opcion a
    #Carga una matriz de forma manual, tamaño y elementos enteros, no recibe parametros, retorna una matriz de números enteros.
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

def ordenar_filas(matriz: list[list[int]]) -> list[list[int]]: # opcion b
    for fila in matriz:
        fila.sort()  # ordena cada fila en forma ascendente
    return matriz

def intercambiar_filas(matriz: list[list[int]], fila1: int, fila2: int) -> None: #opcion c
    #ajustado -1 para coincidir con los indices.
    fila1 -= 1
    fila2 -= 1
    # Verificar que los índices de las filas sean válidos
    if not (fila1 >= 0 and fila1 < len(matriz) and fila2 >= 0 and fila2 < len(matriz)):
        print("Error: Uno o ambos números de fila son inválidos.")
    else:
        # Intercambiar las filas
        matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def intercambiar_columnas(matriz: list[list[int]], col1: int, col2: int) -> None: #Opcion d
    #ajustado -1 para coincidir con los indices.
    col1 -= 1
    col2 -= 1
    # Verificar que los índices de las columnas sean válidos
    if not (col1 >= 0 and col1 < len(matriz[0]) and col2 >= 0 and col2 < len(matriz[0])):
        print("Error: Uno o ambos números de columna son inválidos.")
    else:
        # Recorrer cada fila e intercambiar los elementos en las columnas {col1} y {col2}
        for fila in matriz:
            fila[col1], fila[col2] = fila[col2], fila[col1]

def transponer_matriz(matriz: list[list[int]]) -> list[list[int]]: #opcion e
    largo = len(matriz)  #Tamaño de la matriz (las filas tienen el mismo largo)

    # Crear la matriz transpuesta intercambiando los indices
    matriz_transpuesta = [[matriz[j][i] for j in range(largo)] for i in range(largo)]
    return matriz_transpuesta

def promedio_fila(matriz: list[list[int]], numero_fila: int) -> float:#Opción f
    numero_fila -= 1 #ajustado -1 para coincidir con los indices.
    # Verificar que el índice de la fila sea válido
    if numero_fila < 0 or numero_fila >= len(matriz):
        raise IndexError("El número de fila esta fuera del rango.")

    fila = matriz[numero_fila]
    promedio = sum(fila) / len(fila)

    return promedio

def porcentaje_impares_columna(matriz: list[list[int]], columna: int) -> float:#opción g
    columna -= 1 #ajusta el indice

    #verificar que el índice de la columna sea válido
    if columna < 0 or columna >= len(matriz[0]):
        raise IndexError("El número de columna esta fuera de rango.")

    # Calcular el porcentaje de elementos impares
    porcentaje_impares = (sum(i % 2 != 0 for i in matriz[columna]) / len(matriz[columna])) * 100

    return porcentaje_impares
