"""
Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club 
"""

from os import system, name
import re


def limpiar_pantalla() -> None:
    # Función para limpiar pantalla.
    if name == "posix":
        system("clear")
    else:
        system("cls")


def verificar_codigo(clave: str) -> bool:
    # patrón que debe verificar, que tenga 5 dígitos numéricos en formato string
    patron = "^\\d{5}$"
    return bool(re.match(patron, clave))


def registro_visitas() -> dict:
    visita = {}
    while True:
        salir = input("Enter para continuar, 0 para salir: ")
        if salir == "0":
            print("Saliendo.")
            break

        limpiar_pantalla()
        socio = input("Ingrese su número de socio de 5 digitos: ")
        if not verificar_codigo(socio):
            print("\nIngrese una clave válida de 5 dígitos.\n")
            continue

        if socio in visita:
            visita[socio] += 1
        else:
            visita[socio] = 1
    return visita


def mostrar_registro(visita: dict) -> None:
    # Muestra el registro de visitas por socio.
    for socio, cantidad in visita.items():
        print(f"El socio {socio} hizo {cantidad} visitas.")


def dar_baja(visita: dict) -> None:
    # Elimina todos los registros de un socio dado de baja y muestra el registro actualizado.
    baja = input("\nIngrese el número de socio a dar de baja: ")
    if baja in visita:
        del visita[baja]
        print(f"\nSocio {baja} dado de baja.")
    else:
        print(f"\nEl socio {baja} no está registrado.")

    print(f"\nRegistro actualizado:\n{mostrar_registro(visita)}")


def main() -> None:
    visitas = registro_visitas()
    print("\nRegistro inicial:")
    mostrar_registro(visitas)

    dar_baja(visitas)


if __name__ == "__main__":
    main()
