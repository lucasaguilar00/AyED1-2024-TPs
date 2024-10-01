"""Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2
Oros"... ]. Imprimir la lista por pantalla.
"""


def crear_baraja_espanola() -> list:
    """
    Crea una lista de naipes de la baraja española con listas por comprensión

    Postcondiciones:
    Devuelve una lista de cadenas que representan los naipes.
    """
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    # Generar los naipes del 1 al 7 y su representacion (10, 11, 12)
    naipes = [f"{numero} {palo}" for palo in palos for numero in range(1, 8)] + [
        f"{figura} {palo}"
        for palo in palos
        for figura in ["Sota de", "Caballo de", "Rey de"]
    ]
    return naipes


if __name__ == "__main__":
    baraja = crear_baraja_espanola()
    print(baraja)
