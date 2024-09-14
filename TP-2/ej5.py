"""
Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función. 
"""

import random as rn

def lista_ordenada(var: list) -> bool:
    # Verifica si la lista esta ordenada

    if len(var) <= 1:
        return True
    # Si la lista esta vacia o tiene un solo elemento se considera ordenada.

    for i in range(len(var) - 1):
        if var[i] > var[i + 1]:
            return False
            # Si en un caso no se cumple que el indice anterior es menor al siguiente deja de estar ordenada.
    return True


numero_random = []
letra_random = []
lista1 = [1, 2, 3, 4]
lista2 = [2, 3, 1, 4]
lista3 = ["a", "b", "c", "d"]
lista4 = ["c", "a", "d", "b"]
#Listas de prueba

def main():
    while True:
        print("Programa para saber si la lista esta ordenada.")
        print()
        print("True = Ordenada  //  False = Desordenada")
        print()

        numero_random.clear()
        letra_random.clear()
        # Limpia las listas para iniciar de nuevo

        for _ in range(rn.randint(1, 5)):
            numero_random.append(rn.randint(1, 9))
        # Genera números al azar a la lista vacia

        for _ in range(rn.randint(1, 5)):
            letra_random.append(chr(rn.randint(97, 122)))
        # Genera letras al azar a la lista vacia

        #Prueba de listas predefinidas
        print(lista1)
        print(lista_ordenada(lista1))
        print()

        print(lista2)
        print(lista_ordenada(lista2))
        print()

        print(lista3)
        print(lista_ordenada(lista3))
        print()

        print(lista4)
        print(lista_ordenada(lista4))
        print()

        #Prueba con listas generadas aleatoriamente
        print(numero_random)
        print(lista_ordenada(numero_random))
        print()

        print(letra_random)
        print(lista_ordenada(letra_random))
        print()
        salir = input("Si desea salir del programa ingrese (0): ")
        if salir == "0":
            print()
            print("Saliendo del programa.")
            break

if __name__ == "__main__":
    main()