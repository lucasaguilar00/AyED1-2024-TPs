"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
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
            anio = int(input("Ingrese el año: "))

        except ValueError:
            print("\nError - Dato inválido. Ingrese números válidos.\n")

        else:
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                dias_por_mes[1] = 29  # Año bisiesto, febrero tiene 29 días
            else:
                dias_por_mes[1] = 28

            if 1 <= mes <= 12 and 1 <= dia <= dias_por_mes[mes - 1]:
                return (anio, mes, dia)
            else:
                print("\nFecha inválida. Intente nuevamente.\n")


def sumar_dias(fecha: Tuple[int, int, int], sumar_dias: int) -> Tuple[int, int, int]:
    """
    Precondición: Recibe una tupla que debe contener la fecha en formato (año, mes, día) con INT
    y el parametro sumar_dias que también es INT.

    Argumentos: Suma los días a la fecha obtenida en el parametro .

    Postcondición: Retorna una tupla con la fecha actualizada.
    """
    anio, mes, dia = fecha

    dias_x_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while sumar_dias > 0:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_x_mes[1] = 29
        else:
            dias_x_mes[1] = 28

        dias_restantes_mes = dias_x_mes[mes - 1] - dia

        if sumar_dias <= dias_restantes_mes:
            dia += sumar_dias
            sumar_dias = 0  # break

        else:
            sumar_dias -= dias_restantes_mes + 1
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1

    return (anio, mes, dia)


def ingresar_horario() -> Tuple[int, int]:
    """
    Precondición: Nada
    Argumentos: Ingresa un horario y verifica que sea válido.
    Postcondición: Retorna una tupla con (hora, minuto)
    """

    while True:
        try:
            hora = int(input("Ingrese la hora: "))
            minuto = int(input("Ingrese el minuto: "))

        except ValueError:
            print("Error - Dato inválido. Por favor, ingrese números enteros.")

        else:
            if hora >= 0 and hora < 24 and minuto >= 0 and minuto < 60:
                return (hora, minuto)
            else:
                print("Horario no válido. Por favor, intente nuevamente.")


def diferencia_horarios(
    primer_horario: Tuple[int, int], segundo_horario: Tuple[int, int]
) -> Tuple[int, int]:
    """
    Precondición: Recibe dos parametros que son tuplas que contienen números enteros representando (hora, minuto).
    Argumentos: Calcula la diferencia entre los dos horarios.
    Postcondición: Retorna una tupla con la diferencia de horas y minutos.
    """
    hora_1, minuto_1 = primer_horario
    hora_2, minuto_2 = segundo_horario

    # si la primer hora es mayor, se entiende que se refiere al día anterior.
    if (hora_1, minuto_1) > (hora_2, minuto_2):
        hora_2 += 24

    minutos_diferencia = ((hora_2 * 60) + minuto_2) - ((hora_1 * 60) + minuto_1)
    horas = minutos_diferencia // 60
    minutos = minutos_diferencia % 60
    return (horas, minutos)


def main() -> None:
    while True:

        print("Ingresar fecha:\n")
        fecha = ingresar_fecha()
        print(f"\nLa fecha ingresada es: {fecha}")

        print("Sumar días a la fecha:\n")
        while True:
            try:
                dias_a_sumar = int(input("Ingrese la cantidad de días a sumar: "))
                break
            except ValueError:
                print("\nError - Dato inválido. Ingrese un número entero.\n")

        nueva_fecha = sumar_dias(fecha, dias_a_sumar)
        print(
            f"\nLa nueva fecha después de sumar {dias_a_sumar} días es: {nueva_fecha}"
        )

        print("Calcular la diferencia entre dos horarios:\n")

        print("Ingreso del primer horario:")
        horario1 = ingresar_horario()
        print("Ingreso del segundo horario:")
        horario2 = ingresar_horario()

        diferencia = diferencia_horarios(horario1, horario2)
        print(
            f"La diferencia entre los horarios:{horario1[0]}:{horario1[1]} y {horario2[0]}:{horario2[1]} es de {diferencia[0]} horas y {diferencia[1]} minutos"
        )

        salir = input("Ingrese '0' para salir, enter para continuar: ")
        if salir == "0":
            break


if __name__ == "__main__":
    main()
