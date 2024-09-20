"""
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas.
"""


def centrar_cadena(cadena: str) -> None:
    """
    Precondiciones:
    cadena es una string

    Postcondiciones:
    muestra la cadena centrada en una línea de 80 columnas
    """
    # Le resta a las 80 columnas el largo de la string y luego la centra utilizando espacios x los espacios libres
    columnas = 80
    largo_cadena = len(cadena)
    espacios = (columnas - largo_cadena) // 2
    centrado = (" " * espacios) + cadena
    print(centrado)


def main():
    while True:
        cadena = input("Escriba una cadena o '0' para salir: ")
        if cadena == 0:
            print("\nSaliendo.")
            break
        centrar_cadena(cadena)


if __name__ == "__main__":
    main()
