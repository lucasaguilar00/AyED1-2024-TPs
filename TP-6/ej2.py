"""
Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria.
"""
def dividir_archivo_texto(nombre_archivo: str, tamanio_parte: int) -> None:
    """
    Precondición: Recibe el nombre del archivo en formato STR, y el tamaño que cada parte en formato INT.
    Argumentos: Divide un archivo de texto en partes  de 'tamanio_parte' y los guarda en diferentes archivos con el subfijo que corresponda.
    Postcondición: Nada.
    """


    nombre_base, extension = nombre_archivo.rsplit('.', 1) 
    try:
        with open(nombre_archivo, 'rt', encoding='utf-8') as archivo:
            prefijo = 1

            while True:
                contenido = archivo.read(tamanio_parte)
                if not contenido:
                    break

                nombre_parte = f"{nombre_base}_{prefijo}.{extension}"
                with open(nombre_parte, 'wt', encoding='utf-8') as archivo_parte:
                    archivo_parte.write(contenido)
                prefijo += 1

    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")

    except Exception as e:
        print(f"Hubo un error - {e}")

    else:
        print(f"El archivo se ha dividido de forma exitosa en {prefijo - 1} partes.")


def main()-> None:
    try:
        nombre_archivo = input("Ingrese el nombre del archivo a dividir: ")
        tamano_parte = int(input("Ingrese el tamaño máximo de cada parte en caracteres: "))
        dividir_archivo_texto(nombre_archivo, tamano_parte)
    except ValueError:
        print("Error - El tamaño máximo debe ser un número entero.")
    except Exception as e:
        print(f"Hubo un error - {e}")

if __name__ == "__main__":
    main()
