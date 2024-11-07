"""
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""

from typing import Dict, List, Tuple

def eliminarclaves(diccionario: Dict, lista_claves: List)-> Tuple[Dict, int]:
    """
    Precondición: Recibe un diccionario y una lista con claves.
    Argumentos: Busca en el diccionario las claves que coincidan con las de la lista y las elimina,
    cuenta cuantas claves fueron eliminadas
    Postcondición: Retorna una tupla con el diccionario modificado y el número de claves eliminadas.
    """
    eliminadas = 0

    for clave in lista_claves:
        if clave in diccionario:
            diccionario.pop(clave)
            eliminadas += 1

    return diccionario, eliminadas

def main() -> None:
    """
    Función principal para verificar el comportamiento de `eliminar_claves`.
    """
    diccionario = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
    }
    lista_claves = ['b', 'c', 'e', 'f', 'h']

    print(f"Diccionario original: {diccionario}")

    diccionario_modificado, claves_eliminadas = eliminarclaves(diccionario, lista_claves)

    if claves_eliminadas:
        print(f"Diccionario modificado:\n{diccionario_modificado}")
        print(f"Se eliminaron {claves_eliminadas} claves.")
    else:
        print("No se eliminaron claves.")

if __name__ == "__main__":
    main()
