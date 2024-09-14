"""
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado. 
"""

"""
def lista_multiplos_() -> list:
    inicio = int(input("Ingrese el número donde inicia de la lista: "))
    final = int(input("Ingrese el número donde finaliza de la lista: "))
    lista = []
    for i in range(inicio, final):
        if i % 7 == 0 and i % 5 != 0:
            lista.append(i)
    return lista
"""


def lista_multiplos() -> list:
    inicio = int(input("Ingrese el número donde inicia de la lista: "))
    final = int(input("Ingrese el número donde finaliza de la lista: "))
    lista = [i for i in range(inicio, final) if i % 7 == 0 and i % 5 != 0]
    return lista


if __name__ == "__main__":
    while True:
        salir = input("Ingrese 0 para salir, cualquier tecla para continuar: ")
        if salir == "0":
            print("Saliendo..")
            break
        print(lista_multiplos())
