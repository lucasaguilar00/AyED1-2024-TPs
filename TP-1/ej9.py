"""
Resolver el siguiente problema utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando 
que la ocupación del camión no debe ser inferior al 80%; en caso contrario el camión no serán 
despachado por su alto costo.
"""

import random as rn


def cant_naranja():
    """
    La función obtiende dentro de esta una cantidad de naranjas y retorna 2 datos
    (naranjas para cajon y naranjas para jugo) segun su peso.
    """
    cantidad = int(input("Ingrese la cantidad de naranjas cosechadas"))
    para_cajon = 0
    para_jugo = 0
    for _ in range(cantidad):
        peso_naranja = rn.randint(150, 350)
        if peso_naranja >= 200 and peso_naranja <= 300:
            para_cajon += 1
        else:
            para_jugo += 1
    return para_cajon, para_jugo


def cant_cajones(naranjas):
    # Función para saber cuantos cajones de naranja hay y cuantas naranjas sobran para proximo reparto.
    cajones = 0
    while naranjas >= 100:
        cajones += 1
        naranjas -= 100
    proximo_reparto = naranjas
    return cajones, proximo_reparto


def max_carga(cajones):
    # Retorna los camiones necesarios y cuantos cajones sobran para proxima carga
    peso_total = cajones * (100 * 300)
    camiones = 0
    capacidad_camion = 500000
    capacidad_minima = capacidad_camion * 0.8
    while peso_total >= capacidad_minima:
        camiones += 1
        peso_total -= capacidad_camion
    cajones_sobra = peso_total / (100 * 300)
    return camiones, cajones_sobra


x_cajon, x_jugo = cant_naranja()
cantidad_cajones, prox_reparto = cant_cajones(x_cajon)
camion, cajones_prox_reparto = max_carga(cantidad_cajones)

print(f"Se pueden llenar {x_cajon} cajones, y {x_jugo} naranjas son para jugo.")
print(
    f"Para el proximo reparto hay {prox_reparto} naranjas sueltas y {cajones_prox_reparto} cajones."
)
