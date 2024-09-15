"""
Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
ingresa se anuncia en la recepción indicando su número de afiliado (número entero
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado. 
"""
from os import system, name
import re

def limpiar_pantalla() -> None:
    # Función para limpiar pantalla.
    if name == "posix":
        system("clear")
    else:
        system("cls")

def verificar_codigo(codigo: str) -> bool:
    # patrón que debe verificar, que tenga 4 dígitos numéricos en formato string
    patron = "^\\d{4}$"
    return bool(re.match(patron, codigo))

def separar_pacientes(pacientes: list) -> list: #Opción A.1
    # Separa los pacientes en urgencias y turnos
    tipo_ingreso = [
        [p for p in pacientes if p[1] == 0],  # Emergencia
        [p for p in pacientes if p[1] == 1]   # Turno
    ]
    return tipo_ingreso

def mostrar_listados(urgencias: list, turnos: list) -> None: #Opción A.2
    print("\nPacientes atendidos por urgencia:")
    print([p[0] for p in urgencias])

    print("\nPacientes atendidos por turno:")
    print([p[0] for p in turnos])

def buscar_afiliado(pacientes: list) -> None: #Opción B
    while True:
        afiliado = input("\nIngrese el número de afiliado a buscar (o -1 para salir): ")

        if afiliado == "-1":
            break

        if not verificar_codigo(afiliado):
            #verifica que sea un número válido
            print("\n-1Número de afiliado inválido.")
            continue

        # Cuenta las veces que el afiliado fue atendido por urgencia y por turno
        urgencias_count = sum(1 for p in pacientes if p[0] == afiliado and p[1] == 0)
        turnos_count = sum(1 for p in pacientes if p[0] == afiliado and p[1] == 1)

        print(f"\nNúmero de veces que el afiliado {afiliado} fue atendido por urgencia: {urgencias_count}")
        print(f"Número de veces que el afiliado {afiliado} fue atendido por turno: {turnos_count}")
        input("Enter para continuar.")

def menu_opciones(pacientes: list) -> None:
    while True:
        limpiar_pantalla()
        print("\nMenú de opciones:")
        print("1. Mostrar listado de pacientes.")
        print("2. Buscar número de afiliado.")
        print("3. Salir.")

        opcion = input("\nIngrese una opción: ")
        if opcion == "3":
            print("\nSaliendo del programa..")
            break
        elif opcion == "1":
            urgencias, turnos = separar_pacientes(pacientes)
            mostrar_listados(urgencias, turnos)
            input("Enter para continuar.")
        elif opcion == "2":
            buscar_afiliado(pacientes)
        else:
            print("Opción inválida, intente nuevamente.")

def ingresante() -> None:
    pacientes = []
    while True:
        paciente = input("Ingrese su número de afiliado (4 dígitos): ")
        if not verificar_codigo(paciente):
            print("\nIngrese un número válido de 4 dígitos.\n")
            continue

        print("\nOpciones de ingreso.\n 0. Por emergencia.\n 1. Con turno.\n -1. Para finalizar e ir a las otras opciones.\n")
        ingreso = input("Ingrese una opción: ")

        if ingreso == "-1":
            print("Programa finalizado.")
            break
        if ingreso not in ["0", "1"]:
            print("Opción inválida. Ingrese 0 para urgencia o 1 si posee turno.")
            continue

        limpiar_pantalla()
        pacientes.append((paciente, int((ingreso))))
    menu_opciones(pacientes)

if __name__ == "__main__":
    ingresante()
