"""
Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía.
"""

from typing import Tuple


def descomponer_correo(correo: str) -> Tuple:
    """
    Precondición: Recibe una cadena de caracteres que representa una dirección de correo electrónico.
    Argumentos: Un string `correo` que contiene una dirección de correo en el formato usuario@dominio.subdominio1.subdominio2...
    Postcondición: Retorna una tupla con las partes que componen la dirección de correo.
    Si el formato es inválido, retorna una tupla vacía.
    """

    if correo.count("@") != 1 or " " in correo:
        return ()

    try:
        local, dominio = correo.split("@")
        if not local or not dominio:
            return ()
        partes_dominio = dominio.split(".")

    except ValueError:
        return ()

    else:
        return (local, *partes_dominio)


def main() -> None:
    while True:
        correo = input(
            "Ingrese una dirección de correo electrónico (enter para salir): "
        )

        if not correo:
            break

        partes = descomponer_correo(correo)

        if partes:
            print(f"Las partes del correo son: {partes}")
        else:
            print("La dirección de correo ingresada es inválida.")


if __name__ == "__main__":
    main()
