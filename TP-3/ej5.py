"""
Desarrollar un programa que permita realizar reservas en una sala de cine de N
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas
en un mismo programa:

mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y
se volverá a invocar luego de la misma con los estados actualizados.

reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la
sala en caso de estar disponible dicha butaca. La función devolverá True/False
si logró o no reservar la butaca.

cargar_sala: Recibirá una matriz como parámetro y la cargará con valores
aleatorios para simular una sala con butacas ya reservadas.

butacas_libres: Recibirá como parámetro la matriz y retornará cuántas butacas desocupadas hay en la sala.

butacas_contiguas: Buscará la secuencia más larga de butacas libres contiguas en una misma fila y devolverá las coordenadas de inicio de la misma. 
"""

import random as rn

def mostrar_butacas(sala: list[list[str]]) -> None:
    """
    Precondición: recibe una matriz con listas con strings
    
    muestra el estado actual de las butacas en la sala.
    'L' representa una butaca libre y 'R' una reservada.
    
    Postcondición: No retorna nada.
    """
    print("Estado de la sala:")
    for fila in sala:
        print(" ".join(fila))

def reservar(sala: list[list[str]], fila: int, butaca: int) -> bool:
    """
    Precondición: Recibe una matriz con listas con strings, y dos variables enteras que representan la fila y butaca a reservar. 
    Intenta reservar una butaca y si está libre, la reserva y devuelve True
    Si ya está reservada, devuelve False
    
    postcndición: Retorna un booleano dependiendo el resultado de la reserva.
    """
    if sala[fila][butaca] == 'L':
        sala[fila][butaca] = 'R'
        return True
    return False

def cargar_sala(sala: list[list[str]]) -> None:
    """
    Precondición: Recibe una matriz con listas con strings, que representan las filas y butacas libres.
    
    Carga la sala con valores aleatorios simulando butacas ya reservadas ('R') o libres ('L').
    
    Postcondición: No retorna nada, cambia los valores de las butacas dentro de la función.
    """
    for i in range(len(sala)):
        for j in range(len(sala[i])):
            sala[i][j] = rn.choice(['L', 'R'])

def butacas_libres(sala: list[list[str]]) -> int:
    """
    Precondición: Recibe una matriz con listas con strings
    Devuelve la cantidad de butacas libres ('L') en la sala.
    
    Postcondición: Retorna un número entero que son las butacas libres.
    """
    libres = sum(fila.count('L') for fila in sala)
    return libres

def butacas_contiguas(sala: list[list[str]]) -> tuple[int, int, int]:
    """
    Precondición: Recibe una matriz con listas con strings
    
    Busca la secuencia más larga de butacas libres contiguas en una misma fila
    
    Postcondición: Retorna una tupla con la fila y las coordenadas de inicio y fin de la secuencia
    Si no hay butacas libres contiguas, devuelve (-1, -1, -1)
    """
    fila_max, inicio_max, longitud_max = -1, -1, 0

    for i, fila in enumerate(sala):
        inicio = -1
        longitud = 0
        for j, butaca in enumerate(fila):
            if butaca == 'L':
                if inicio == -1:
                    inicio = j
                longitud += 1
            else:
                if longitud > longitud_max:
                    fila_max, inicio_max, longitud_max = i, inicio, longitud
                inicio = -1
                longitud = 0
        if longitud > longitud_max:
            fila_max, inicio_max, longitud_max = i, inicio, longitud

    if fila_max != -1:
        return fila_max, inicio_max, inicio_max + longitud_max - 1
    return -1, -1, -1

def main()-> None:
    n = int(input("Ingrese el número de filas de la sala: "))
    m = int(input("Ingrese el número de butacas por fila: "))

    #crea la matriz de la sala
    sala = [['L' for _ in range(m)] for _ in range(n)]

    # carga la sala con reservas aleatorias
    cargar_sala(sala)
    mostrar_butacas(sala)

    #Intenta reservar
    fila = int(input("Ingrese la fila a reservar: "))
    butaca = int(input("Ingrese la butaca a reservar: "))

    if reservar(sala, fila, butaca):
        print("Reserva exitosa.")
    else:
        print("La butaca ya fue reservada, no se pudo realizar la reserva.")

    # muestra el estado actualizado de la sala
    mostrar_butacas(sala)

    # muestra la cantidad de butacas libres
    libres = butacas_libres(sala)
    print(f"Butacas libres en la sala: {libres}")

    # busca la secuencia más larga de butacas contiguas
    fila_contigua, inicio, fin = butacas_contiguas(sala)
    if fila_contigua != -1:
        print(f"La secuencia más larga de butacas libres contiguas es: Fila {fila_contigua}, de la butaca {inicio} a la {fin}.")
    else:
        print("No hay secuencias de butacas libres contiguas.")

if __name__ == "__main__":
    main()