"""
El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda
"""

from typing import List


def crear_lista() -> List[int]:
    """
    Precondición: Nada
    Argumentos: Crea una lista con datos números
    Postcondición: Retorna una lista con números enteros
    """
    lista = []
    print("Cargar lista.")
    while True:
        try:
            numero = int(input("Ingrese un número (-1 para salir): "))
            if numero == -1:
                return lista
            lista.append(numero)
        except ValueError:
            print("Error - Intente nuevamente con un valor numérico válido.")


def buscar_indice():
    lista_nueva = crear_lista()
    errores = 0

    while errores < 3:
        try:
            buscar = int(input("Ingrese el número que desea buscar: "))
            indice = lista_nueva.index(buscar)
            print(f"El índice de {buscar} es: {indice}.")
        except ValueError:
            print("Error - El número no se encuentra en la lista.")
            errores += 1
            if errores >= 3:
                print("Ocurrieron 3 errores, finalizando programa.")
                break


if __name__ == "__main__":
    buscar_indice()
