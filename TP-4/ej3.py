"""
Los números de claves de dos cajas fuertes están intercalados dentro de un número
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
para obtener ambas claves, donde la primera se construye con los dígitos ubicados
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89
"""

def extraer_claves(clave_maestra: int) -> tuple:
    #lo recibe como str y los concatena mediante join para poder separar cada clave segun iteraciones
    clave1 = ''.join(d for i, d in enumerate(clave_maestra) if i % 2 == 0)
    clave2 = ''.join(d for i, d in enumerate(clave_maestra) if i % 2 != 0)
    return clave1, clave2


def main():
    clave_maestra = input("Ingrese la clave maestra: ")
    clave1, clave2 = extraer_claves(clave_maestra)
    print(f"Clave 1: {clave1}")
    print(f"Clave 2: {clave2}")


if __name__ == "__main__":
    main()