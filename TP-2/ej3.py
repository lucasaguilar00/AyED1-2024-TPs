"""
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista. 
"""

lista = []  # lista vacia


def cargar_lista(var: list) -> list:
    while True:
        try:
            # Utiliza try para prevenir un posible error que detenga el programa
            elementos = int(input("Ingrese la cantidad de elementos que desea tener: "))
            if elementos > 1:
                for i in range(elementos):
                    cuadrado = (i + 1) ** 2
                    var.append(cuadrado)
                return var
            else:
                print("Introduzca un número mayor a 1")
        except ValueError:
            print("Ingrese un número entero válido")


def ultimos_elementos(var: list) -> list:
    # Devuelve los ultimos 10 elementos de la lista, o si tiene menos de 10 la lista entera
    return var[-10:]


def menu():
    while True:
        print("Opciones")
        print()
        print("1- Crear lista con los cuadrados del número 1 hasta el..: ")
        print("2- Imprimir los últimos 10 valores de la lista.")
        print("3- Vaciar lista.")
        print("0. Salir.")
        op = input("Ingrese una opción: ")
        if op == "1":
            cargar_lista(lista)
            print("La lista es la siguiente:")
            print(lista)
        elif op == "2":
            print("Los ultimos 10 valores de la lista son:")
            print(ultimos_elementos(lista))
        elif op == "3":
            lista.clear()
            print("La lista se ha vaciado.")
        elif op == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    menu()
