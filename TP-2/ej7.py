"""
Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes.
"""

# REVISAR

import random as rn


def cargar_lista(x: list) -> list:  # Opción a
    # Carga una lista con elementos y los datos al azar
    x.clear()
    for _ in range(rn.randint(3, 8)):
        x.append(rn.randint(1, 9))
    return x


def intercalar(a: list, b: list) -> None:
    largo_min = min(len(a), len(b))

    a[1::2] = b[:largo_min]

    if len(b) > len(a):
        a.extend(b[largo_min:])


lista1 = []
lista2 = []

"""
if __name__ == "__main__":
    while True:
        op = input("Para detener el programa ingrese 0, para continuar cualquier tecla: ")
        if op == "0":
            print("Saliendo del programa.")
            break
        cargar_lista(lista1)
        cargar_lista(lista2)
        print(f"La lista 1 es: {lista1}\n")
        print(f"La lista 2 es: {lista2}\n")
        intercalar(lista1, lista2)
        print(lista1)
"""
