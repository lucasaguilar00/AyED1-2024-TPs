"""
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas
en cada una de sus plantas durante una semana. De este modo, cada columna representa 
el día de la semana y cada fila a una de sus fábricas. Ejemplo:

Se solicita:
a. Crear una matriz con datos generados al azar para N fábricas durante una
semana, considerando que la capacidad máxima de fabricación es de 150
unidades por día y puede suceder que en ciertos días no se fabrique ninguna.
b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
e. Crear una lista por comprensión que contenga la menor cantidad fabricada
por cada fábrica. 
"""

import random as rn


def generar_matriz(num_fabricas: int, num_dias: int) -> list[list[int]]:  # opción a
    """
    Precondiciones:
    num_fabricas debe ser un entero positivo
    num_dias debe ser un entero positivo

    Postcondiciones:
    devuelve una matriz del tamaño de num_fabricas x num_dias con datos aleatorios 
    de bicicletas producidas, y cada valor está en el rango de 0 a 150
    """
    return [[rn.randint(0, 150) for _ in range(num_dias)] for _ in range(num_fabricas)]


def totales_fabricas(matriz: list[list[int]]) -> list[int]:  # opción b
    """
    Precondiciones:
    la matriz debe ser una lista de listas de enteros

    Postcondiciones:
    devuelve una lista con la cantidad total de bicicletas fabricadas por cada fábrica.
    """
    return [sum(fabrica) for fabrica in matriz]


def fabrica_max_produccion(matriz: list[list[int]]) -> tuple[str, int]:
    """
    Precondiciones:
    la matriz debe ser una lista de listas de enteros

    Postcondiciones:
    devuelve una tupla y esta contiene el índice de la fábrica que más produjo en un día
    junto a el nombre del día correspondiente
    """
    max_produccion = max(
        (produccion, i, j)
        for i, fabrica in enumerate(matriz)
        for j, produccion in enumerate(fabrica)
    )
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    return max_produccion[1], dias[max_produccion[2]]


def dia_mas_productivo(matriz: list[list[int]]) -> tuple[str, int]:
    """
    Precondiciones:
    la matriz debe ser una lista de listas de enteros

    Postcondiciones:
    devuelve una tupla que contiene el nombre del día más productivo y el total de producción 
    en ese día, siempre considerando todas las fábricas
    """
    total_dias = [sum(fabrica[j] for fabrica in matriz) for j in range(len(matriz[0]))]
    dia_productivo = total_dias.index(max(total_dias))
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    return dias[dia_productivo], total_dias[dia_productivo]


def menores_producciones(matriz: list[list[int]]) -> list[int]:
    """
    Precondiciones:
    la matriz debe ser una lista de listas de enteros

    Postcondiciones:
    devuelve una lista con la menor cantidad de bicicletas fabricada por cada fábrica
    """
    return [min(fabrica) for fabrica in matriz]


def menu():
    opciones = [
        "Cargar una matriz con datos al azar",
        "Muestra el total de bicicletas fabricadas por fabrica",
        "Fabrica que más produjo en un día",
        "Día más productivo teniendo en cuenta todas las fabricas",
        "Menor cantidad fabricada por fabrica",
        "Salir",
    ]

    num_fabricas = rn.randint(3, 6)
    num_dias = 7
    matriz = []
    while True:
        print("\nMenú de opciones:")
        for num, opcion in enumerate(opciones):
            print(f"{num + 1}. {opcion}.")
        op = input("\nIngrese una opción: ")

        if op == "1":
            matriz = generar_matriz(num_fabricas, num_dias)
            print("\nMatriz de producción:")
            for i, fabrica in enumerate(matriz, 1):
                print(f"Fabrica {i}: {fabrica}.")
            input("\nPress enter para continuar ")

        elif op == "2":
            if not matriz:
                print("\nPrimero debe cargar una matriz.")
            else:
                totales = totales_fabricas(matriz)
                print("\nCantidad total de bicicletas fabricadas por cada fábrica:")
                for i, total in enumerate(totales):
                    print(f"Fábrica {i}: {total} bicicletas")
                input("\nPress enter para continuar ")

        elif op == "3":
            if not matriz:
                print("\nPrimero debe cargar una matriz.")
            else:
                fabrica, dia = fabrica_max_produccion(matriz)
                print(
                    f"\nLa fábrica que más produjo en un solo día es la fábrica {fabrica}, en el día {dia}."
                )
                input("\nPress enter para continuar ")

        elif op == "4":
            if not matriz:
                print("\nPrimero debe cargar una matriz.")
            else:
                dia_productivo, produccion = dia_mas_productivo(matriz)
                print(
                    f"\nEl día más productivo es el día {dia_productivo} con un total de {produccion} bicicletas."
                )
                input("\nPress enter para continuar ")

        elif op == "5":
            if not matriz:
                print("\nPrimero debe cargar una matriz.")
            else:
                menores = menores_producciones(matriz)
                print("\nMenor cantidad fabricada por cada fábrica:")
                for i, menor in enumerate(menores):
                    print(f"Fábrica {i+1}: {menor} bicicletas")
                input("\nPress enter para continuar ")

        elif op == "6":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
