"""Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro 
de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes 
(detalladas en la tabla de abajo)  se solicita desarrollar una función que reciba como parámetro 
la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes. 
Realizar también un programa para verificar  el comportamiento de la función. 
Cantidad de viajes          Valor del pasaje
1 a 20                      Averiguar en Internet el valor actualizado  ($650-.)
21 a 30                     20% de descuento sobre tarifa máxima
31 a 40                     30% de descuento sobre tarifa máxima
Más de 40                   40% de descuento sobre tarifa máxima
"""


def gastos_subte(cant_viajes):
    """
    Calcula el gasto total de los viajes realizados teniendo en cuenta que se aplican descuentos
    decrecientes según el número de viajes
    """
    gastado = 0
    precio = 650
    for i in range(1, cant_viajes + 1):
        if i <= 20:
            gastado += precio
        elif i <= 30:
            gastado += precio * 0.8
        elif i <= 40:
            gastado += precio * 0.7
        elif i > 40:
            gastado += precio * 0.6
    return gastado


def verif_funcion():
    # Verificacion de la funcion "gastos_subte(cant_viajes) con diferentes valores (cantidad de viajes).
    viajes_prueba = [2, 10, 20, 25, 30, 35, 40, 45, 50]
    for i in range(len(viajes_prueba)):
        print(
            f"Usted a realizado {viajes_prueba[i]} viajes, gastando un total de ${gastos_subte(viajes_prueba[i])}-. pesos."
        )


verif_funcion()
while True:
    viajes = int(
        input("Ingrese la cantidad de viajes que realizo en el mes (0 para salir): ")
    )
    print(f"Usted a gastado ${gastos_subte(viajes)}-.")
    salir = input("Ingrese 0 para salir: ")
    if viajes == "0":
        break
