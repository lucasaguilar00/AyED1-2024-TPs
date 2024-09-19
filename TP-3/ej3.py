"""
Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N^2), 
de tal forma que ningún número se repita. Imprimir la matriz por pantalla
"""

import random as rn

def generar_matriz_aleatoria(n: int)-> list[list[int]]:
    numeros = list(range(n * n))
    rn.shuffle(numeros) #Mezcla la lista para que sea totalmente aleatorio

    matriz = [numeros[i * n:(i + 1) * n] for i in range(n)]
    return matriz

if __name__ == "__main__":
    print(generar_matriz_aleatoria(int(input("Ingresar el tamaño de la matriz: "))))