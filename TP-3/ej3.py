"""
Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N^2), 
de tal forma que ningún número se repita. Imprimir la matriz por pantalla
"""

import random as rn

def generar_matriz_aleatoria(n: int)-> list[list[int]]:
    """
    Precondiciones:
    n debe ser un número entero positivo

    Postcondiciones:
    devuelve una matriz cuadrada de tamaño n x n cargada con números enteros ÚNICOS random en el rango de 0 a 'n' elevado al cuadrado
    """
    numeros = list(range(n * n))
    rn.shuffle(numeros) #Mezcla la lista para que sea totalmente aleatorio

    matriz = [numeros[i * n:(i + 1) * n] for i in range(n)]
    return matriz

if __name__ == "__main__":
    print(generar_matriz_aleatoria(int(input("Ingresar el tamaño de la matriz: "))))