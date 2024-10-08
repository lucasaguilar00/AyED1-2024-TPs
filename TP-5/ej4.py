"""
Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C
"""
def imprimir_numeros()-> None:
    """
    Precondición: Nada
    Imprime los números enteros entre 1 y 100000. Si se presiona Ctrl + C te pide una confirmacion para continuar
    Postcondición: Nada
    """
    try:
        print("Si presiona Ctrl + C el programa será interrumpido con un error.")
        for i in range(1, 100001):
            print(i)
    except KeyboardInterrupt:
        respuesta = input("\nSe detectó una interrupción al presionar Ctrl + C. ¿Desea detener el programa? (Si o No): ")
        if respuesta.lower() != "si":
            imprimir_numeros()
        else:
            print("Programa detenido.")
            return None

if __name__ == "__main__":
    imprimir_numeros()