"""
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo 
una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres 
de la cadena original. 
Escribir también un programa para verificar el comportamiento de la misma. Hacer tres 
versiones de la función, para cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
"""


def filtrar_palabras_ciclo(frase: str, n: int) -> str:  # Función A ciclos normales
    """
    Precondición: Obtiene una variable frase que es una string
    y la varible n que contiene un entero positivo
    Postcondición: devuelve una cadena de palabras con 'n' o más caracteres
    del parametro obtenido en frase.
    """
    palabras = frase.split()
    resultado = []

    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)

    return ", ".join(resultado)


def filtrar_palabras_comprension(
    frase: str, n: int
) -> str:  # Función B lista por comprensión
    """
    Precondición: Obtiene una variable frase que es una string
    y la varible n que contiene un entero positivo
    Postcondición: devuelve una cadena de palabras con 'n' o más caracteres
    del parametro obtenido en frase.
    """
    return ", ".join([palabra for palabra in frase.split() if len(palabra) >= n])


def filtrar_palabras_filter(frase: str, n: int) -> str:  # Función C con función filter
    """
    Precondición: Obtiene una variable frase que es una string
    y la varible n que contiene un entero positivo
    Postcondición: devuelve una cadena de palabras con 'n' o más caracteres
    del parametro obtenido en frase.
    """
    return ", ".join(filter(lambda palabra: len(palabra) >= n, frase.split()))


def main() -> None:
    """
    Esta función verifica las funciónes anteriores pasandole los parametros correspondientes e imprimiendo los resultados,
    la funcion 'main' no obtiene parametros ni retorna nada.
    """
    frases_filtrar = input("Ingrese la frase a filtrar: ")
    # Verificación de que el largo mínimo sea un número positivo
    while True:
        try:
            largo_string = int(input("\nIngrese el largo mínimo de la string: "))
            if largo_string > 0:
                break
            else:
                print("\nEl número debe ser positivo, intente nuevamente.")
        except ValueError:
            print("\nIngresó un carácter no válido, ingrese un número positivo.")

    print(
        f"\nResultado obtenido utilizando ciclos normales:\n{filtrar_palabras_ciclo(frases_filtrar, largo_string)}\n"
    )
    print(
        f"Resultado obtenido utilizando listas por comprensión:\n{filtrar_palabras_comprension(frases_filtrar, largo_string)}\n"
    )
    print(
        f"Resultado utilizando la función filter:\n{filtrar_palabras_filter(frases_filtrar, largo_string)}"
    )


if __name__ == "__main__":
    main()
