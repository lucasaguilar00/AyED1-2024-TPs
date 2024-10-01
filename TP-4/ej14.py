"""
Se solicita crear un programa para leer direcciones de correo electrónico y verificar
si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que
una dirección sea considerada válida el nombre de usuario debe poseer solamente
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe
tener al menos un carácter y tiene que finalizar con .com o .com.ar.

Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mostrar 
un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente,
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas.
"""

import re


def email_valido(email: str) -> bool:
    """
    Precondición: email es una cadena de caracteres.

    Arg: Verifica que la dirección email que se brinda sea valida
    teniendo en cuenta los argumentos del patron.

    Postcondición: Retorna True o False si es válido o no.
    """
    # expresión regular para validar correo
    patron = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(com|com\.ar)$"
    return bool(re.match(patron, email))


def main():
    """
    Precondición: None
    Postcondición: None
    """
    emails = []

    while True:
        correo_electronico = input(
            "Ingrese una dirección de correo electrónico (para finalizar presione enter): "
        )

        if correo_electronico == "":
            print("Saliendo.")
            break

        if email_valido(correo_electronico):
            print("Es válida.\n")
            emails.append(correo_electronico.lower())
        else:
            print(f"\nLa dirección '{correo_electronico}' no es válida.\n")

    # Extraer dominios y eliminarlos duplicados
    dominios = {email for email in emails}

    # Mostrar dominios ordenados alfabéticamente
    print("\nLista ordenada y sin repeticiones de los emails válidos:")
    i = 1
    for dominio in sorted(dominios):
        print(f"{i}. {dominio}")
        i += 1


if __name__ == "__main__":
    main()
