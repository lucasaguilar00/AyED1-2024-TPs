"""
Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.
"""

from typing import Tuple


def ingresar_fecha() -> Tuple[int, int, int]:
    """
    Precondición: Nada
    Argumentos:El usuario ingresa una fecha y se verifica que sea válida.
    Postcondición: Retorna una tupla con el (año, mes, día) cuando la fecha es correcta.
    """

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while True:
        try:
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Año (formato de 2 o 4 dígitos): "))

        except ValueError:
            print("\nError - Dato inválido. Ingrese números válidos.\n")

        else:
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                dias_por_mes[1] = 29  # Año bisiesto, febrero tiene 29 días
            else:
                dias_por_mes[1] = 28

            if (
                mes >= 1
                and mes <= 12
                and dia >= 1
                and dia <= dias_por_mes[mes - 1]
                and anio < 2100
            ):
                return (dia, mes, anio)
            else:
                print("\nFecha inválida. Intente nuevamente.\n")


def fecha_formato_extendido(fecha: Tuple[int, int, int]) -> str:
    """
    Precondición: La tupla fecha debe contener valores enteros representando (día, mes, año).
    Argumentos: Obtiene una fecha y segun el año de corte obtiene la fecha en formato extendido.
    Postcondición: Retorna una cadena con la fecha en formato extendido
    """

    while True:
        try:
            anio_corte = int(input("\nIngrese el año de corte: "))
        except ValueError:
            print("\nError - Dato inválido. Ingrese un número entero.\n")
        else:
            break

    meses_string = (
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    )

    dia, mes, anio = fecha

    if anio >= 0 and anio <= 99:
        if anio <= anio_corte:
            anio += 2000
        else:
            anio += 1900

    return f"{dia} de {meses_string[mes - 1]} de {anio}"


def main() -> None:
    print("Ingrese la fecha:\n")
    fecha = ingresar_fecha()

    fecha_extendida = fecha_formato_extendido(fecha)

    print(
        f"\nLa fecha {fecha[0]}/{fecha[1]}/{fecha[2]} en formato extendido es: {fecha_extendida}"
    )


if __name__ == "__main__":
    main()
