"""
Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones.
"""

def obtener_nombre_mes(numero_mes: int) -> str:
    """
    Precondición: Debe recibir un número entero que corresponda a un mes
    Argumentos: Busca en la lista de meses el número que corresponde
    Postcondición: Retorna una cadena con el mes correspondiente o 
    una cadena vacía si no corresponde a un mes
    """
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    try:
        return meses[numero_mes - 1]
    except IndexError:
        return ""

if __name__ == "__main__":
    while True:
        try:
            mes = int(input("Ingrese el número del mes (0 para salir): "))
            if mes == 0:
                break
            cadena_mes = obtener_nombre_mes(mes)
            if cadena_mes:
                print(f"El número {mes}, corresponde al mes {cadena_mes}.")
            else:
                print(f"El número {mes} no corresponde a ningún mes.")
        except ValueError:
            print("Error, ingresó un valor no válido, intente nuevamente.")