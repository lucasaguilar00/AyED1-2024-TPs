"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento.
"""

def es_capicua(cadena: str) -> bool:
    #$ecorre la cadena comparando el primer y el último carácter mientras avanza hacia el centro de la string
    largo = len(cadena)
    for i in range(largo // 2):
        if cadena[i] != cadena[largo - 1 - i]:
            return False
    return True


def verificar_capicua():
    while True:
        cadena = input("Ingrese una palabra para verificar si es capicúa (0 para salir): ")
        if cadena == "0":
            break
        if es_capicua(cadena):
            print(f"La cadena '{cadena}' es capicúa.")
        else:
            print(f"La cadena '{cadena}' no es capicúa.")


if __name__ == "__main__":
    verificar_capicua()