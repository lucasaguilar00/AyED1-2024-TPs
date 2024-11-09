"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de 
apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con 
la cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe –> ITALIA.TXT
Pérez, Juan –> ESPAÑA.TXT
Smith, John –> descartar
El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor. 
"""
def origen_apellido(last_name: str, person: str, countries: dict) -> None:
    """
    Precondición: Recibe como parametro el apellido de la persona en formato STR, El nombre completo
    de la persona en formato STR, y  un DICT con las terminaciones de los apellidos junto a sus paises de origen

    Argumentos: Segun la terminación del apellido determina de que origen pertenece y lo guarda en el archivo correspondiente a su país.

    Postcondición: nada
    """
    for clave, valor in countries.items():
        if last_name.endswith(clave):

            try:
                with open(valor, 'a', encoding='utf-8') as arch_origen:
                    arch_origen.write(person.strip() + '\n')

            except Exception as e:
                print(f"Error al escribir en el archivo '{valor}': {e}")

            else:
                print("Se han escrito los datos exitosamente.")
                return None

def main()-> None:
    paises = {
        'ian' : 'armenia.txt',
        'ini' : 'italia.txt',
        'ez' : 'españa.txt'
    }

    try:
        with open('personas.txt', 'r', encoding='utf-8') as archivo:
            for persona in archivo:
                apellido = persona.split(',')[0].strip()
                origen_apellido(apellido, persona, paises)

    except FileNotFoundError:
        print("El archivo que intenta abrir no se encontró.")
    except Exception as e:
        print(f"Hubo un error - {e}")

if __name__ == "__main__":
    main()
