"""
7. Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""


def es_bisiesto(a: int):
    # verifica si el año es bisiesto mediante un calculo que tienen en comun
    return a % 4 == 0 and (a % 400 == 0 or a % 100 != 0)


def verifica_fecha(d: int, m: int, a: int):
    # Verifica que la fecha sea válida teniendo en cuenta los años bisiestos
    dias_al_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m < 1 or m > 12:
        return False
    if es_bisiesto(a) == True:
        dias_al_mes[1] = 29
    if d < 1 or d > dias_al_mes[m - 1]:
        return False
    else:
        return True


def diasiguiente(d: int, m: int, a: int):
    # Recibe como parametro dia, mes, año. Devuelve la fecha del día siguiente
    dias_al_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if es_bisiesto(a):
        dias_al_mes[1] = 29

    if d == dias_al_mes[m - 1]:
        d = 1
        if m == 12:
            m = 1
            a += 1
        else:
            m += 1
    else:
        d += 1
    return d, m, a


def sumar_dias(d: int, m: int, a: int, n: int):
    # Recibe una fecha y retorna otra fecha "X" días después.
    for _ in range(n):
        d, m, a = diasiguiente(d, m, a)
    return d, m, a


def diferencia_fechas(d1: int, m1: int, a1: int, d2: int, m2: int, a2: int):
    # Utiliza un contador para saber cuantos días hay entre dos fechas
    dias = 0
    while (d1, m1, a1) != (d2, m2, a2):
        d1, m1, a1 = diasiguiente(d1, m1, a1)
        dias += 1
    return dias


def op():
    print("Op1: Fecha siguiente")
    print("Op2:")
    print("Op3: Cuantos días hay entre dos fechas")


def main():
    op()
    opcion = input("Ingrese una opción(0 salir.): ")
    if opcion == "1":
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))
        if verifica_fecha(dia, mes, anio):
            print(diasiguiente(dia, mes, anio))
        else:
            print("La fecha es invalida.")
    elif opcion == "2":
        dia = int(input("Ingrese el día: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))
        suma = int(input("Ingrese la cantidad de días que desea sumar: "))
        if verifica_fecha(dia, mes, anio):
            print(sumar_dias(dia, mes, anio, suma))
        else:
            print("La fecha es invalida.")
    elif opcion == "3":
        print("Datos de la primer fecha:")
        dia_a = int(input("Ingrese el día: "))
        mes_a = int(input("Ingrese el mes: "))
        anio_a = int(input("Ingrese el año: "))
        print("Datos de la segunda fecha:")
        dia_b = int(input("Ingrese el día: "))
        mes_b = int(input("Ingrese el mes: "))
        anio_b = int(input("Ingrese el año: "))
        diferencia = diferencia_fechas(dia_a, mes_a, anio_a, dia_b, mes_b, anio_b)
        print(f"La diferencia es de {diferencia} días.")
    elif opcion == "0":
        print("Saliendo...")
