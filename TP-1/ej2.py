"""Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función"""

def es_bisiesto(anio):
    #verifica si el año es bisiesto mediante un calculo que cumplen estos
    if anio % 4 == 0 and (anio % 400 == 0 or anio % 100 != 0):
        return True
    else:
        return False

def verifica_fecha(dia, mes, anio):
    dias_al_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if mes < 1 or mes > 12:
        return False
    if es_bisiesto(anio) == True:
        dias_al_mes[1] = 29
    if dia < 1 or dia > dias_al_mes[mes-1]:
        return False
    else:
        return True

def verificacion_funcion():
    fechas_de_prueba = [
        [29, 29, 31, 1, 31, 0, 2],
        [2, 2, 6, 7, 12, 3, 13],
        [2024, 2023, 2024, 2019, 2000, 1999, 2020]
    ]
    
    for i in range(len(fechas_de_prueba[0])):
        dia = fechas_de_prueba[0][i]
        mes = fechas_de_prueba[1][i]
        anio = fechas_de_prueba[2][i]
        
        es_valido = verifica_fecha(dia, mes, anio)
        
        if es_valido == True:
            print(f"{dia}/{mes}/{anio} es una fecha valida")
        else:
            print(f"{dia}/{mes}/{anio} es una fecha invalida")

verificacion_funcion()
while True: 
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    valido = verifica_fecha(dia, mes, anio)
    print(valido)
    salir = input("Para salir ingrese 0: ")
    if salir == "0":
        break