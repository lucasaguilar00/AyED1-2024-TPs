from typing import List

"""
Dados dos números enteros no negativos, devolver el resultado de calcular el Máximo Común Divisor (también llamado Divisor Común Mayor) basándose en las siguientes propiedades:
MCD(X, X) = X
MCD(X, Y) = MCD(Y, X)
Si X > Y => MCD(X, Y) = MCD(X–Y, Y).
Utilizando la función anterior calcular el MCD de todos los elementos de una lista de
números enteros, sabiendo que MCD(X,Y,Z) = MCD(MCD(X,Y),Z). No se permite
utilizar iteraciones en ninguna etapa del proceso.
"""


def mcd(x: int, y: int) -> int:
    """
    Precondición: los parametros 'x' e 'y' son números enteros no negativos.
    Argumento: calcula el MCD de 'x' e 'y' utilizando restas sucesivas.
    Postcondición: retorna el MCD de ambos parámetros.
    """
    if x == y:
        return x
    elif x > y:
        return mcd(x - y, y)
    else:
        return mcd(y, x)


def mcd_lista(lista: List[int]) -> int:
    """
    Precondición: la lista 'numeros' contiene al menos un número entero.
    Argumento: calcula el MCD de una lista de números enteros no negativos.
    Postcondición: retorna el MCD de todos los números en la lista.
    """
    if len(lista) == 1:
        return lista[0]
    else:
        return mcd(lista[0], mcd_lista(lista[1:]))


def cargar_numeros() -> List[int]:
    """
    Precondición: nada
    Argumento: permite al usuario agregar números enteros en una lista hasta que ingrese -1.
    Postcondición: retorna una lista de números enteros.
    """
    lista_num = []
    while True:
        try:
            num_lista = int(
                input("Ingrese un número para agregar a la lista (-1 para salir): ")
            )
        except ValueError:
            print("Error - Ingrese un número entero válido.")
            continue

        if num_lista == -1:
            break
        lista_num.append(num_lista)

    return lista_num


if __name__ == "__main__":
    numeros = cargar_numeros()

    if len(numeros) == 0:
        print("La lista está vacía, no se puede calcular el MCD.")
    else:
        resultado = mcd_lista(numeros)
        print(f"El Máximo Común Divisor de la lista:\n{numeros}\nes: {resultado}.")
