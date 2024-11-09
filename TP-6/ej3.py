"""
. Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>

GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atletas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >

MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo.
"""

def grabar_rango_alturas() -> None:
    """
    Precondición: Ninguna.
    Argumentos: Guarda en un archivo las alturas de los ateltas separados por el deporte que juegan.
    Postcondición: Guarda las alturas en un archivo 'alturas_atletas.txt'.
    """
    try:
        with open('alturas_atletas.txt', 'w', encoding='utf-8') as archivo:
            while True:
                deporte = input("Ingrese el deporte (o 's' para terminar): ").strip()
                if deporte.lower() == 's':
                    break

                archivo.write({deporte} + '\n')

                while True:
                    try:
                        altura = int(input(f"Ingrese la altura del atleta en {deporte} (o '-1' para cambiar de deporte): "))
                    except ValueError:
                        print("Debe ingresar un valor numérico válido para la altura.")
                    else:
                        if altura == -1:
                            break

                        if 50 <= altura <= 250:
                            archivo.write(f"{altura}\n")
                        else:
                            print("Dato inválido. La altura debe estar entre 50 y 250 cm.")

    except Exception as e:
        print(f"Hubo un error - {e}")
    else:
        print("Se completo el registro de alturas.")

def main() -> None:
    grabar_rango_alturas()


if __name__ == "__main__":
    main()