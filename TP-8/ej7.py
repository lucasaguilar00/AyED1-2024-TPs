"""
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido 
del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.
"""
def main() -> None:
    """
    Precondición: Nada
    Argumentos: Crea un conjunto con números y el usuario elije que número eliminar, 
    luego muestra el número eliminado y el conjunto actualizado.
    Postcondición: Nada
    """

    set_numeros = set(range(10))
    print(f"El conjunto inicial:\n{set_numeros}")

    while True:
        try:

            valor = int(input("Ingrese un valor para eliminar del conjunto (-1 para finalizar): "))
            if valor == -1:
                break

            set_numeros.remove(valor)
            print(f"Conjunto después de eliminar {valor}: {set_numeros}")

        except ValueError:
            print("Error - Ingrese un número entero válido.")

        except KeyError:
            print(f"Error - El valor {valor} no está en el conjunto.")

if __name__ == "__main__":
    main()
