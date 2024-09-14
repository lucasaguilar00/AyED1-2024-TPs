"""
La siguiente función permite averiguar el día de la semana para una fecha determinada. 
La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo,
1 para lunes, 2 para martes, etc. Escribir un programa para
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. Considerar que la semana
comienza en domingo.
"""

from tabulate import tabulate


def diadelasemana(dia, mes, año):
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (
        ((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)
    ) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem


def dias_en_mes(mes: int, año: int) -> int:
    # Devuelve la cantidad de dias que contiene el mes
    if mes == 2:  # Si es bisiesto
        return 29 if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) else 28

    return 30 if mes in [4, 6, 9, 11] else 31


def imprimir_calendario(mes, año):

    dias_semana = ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]
    # Días de la semana

    primer_dia = diadelasemana(
        1, mes, año
    )  # Obtengo el día de la semana del primer día del mes

    dias_mes = dias_en_mes(mes, año)  # Saber cuantos días tiene el mes

    calendario = []
    semana = [""] * primer_dia  # llenar con espacios hasta llegar al primer día

    for dia in range(1, dias_mes + 1):
        semana.append(dia)
        if len(semana) == 7:  # Cuando completamos una semana
            calendario.append(semana)
            semana = []

    if semana:  # Agrega los días restantes
        calendario.append(
            semana + [""] * (7 - len(semana))
        )  # Completar con espacios vacíos

    # Utiliza tabulate para imprimir el calendario
    print(f"Calendario del {mes}/{año}")
    print(tabulate(calendario, headers=dias_semana, tablefmt="grid"))


if __name__ == "__main__":
    while True:
        salir = input("Para continuar ingrese cualquier tecla, 0 para salir: ")
        if salir == "0":
            print("Saliendo..")
            break
        mes_ = int(input("Ingrese el mes: "))
        año_ = int(input("Ingrese el año: "))
        imprimir_calendario(mes_, año_)
