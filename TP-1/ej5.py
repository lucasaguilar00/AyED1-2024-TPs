"""
Escribir funciones lambda para:
a.Informar si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener 
multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de 
multiplicar 2 * 3.
"""

num_oblongo = lambda x: any(a * (a + 1) == x for a in range(1, x))
# Multiplica 2 números consecutivos y verifica si el resultado es igual al parametro obtenido == oblongo

print(num_oblongo(int(input("Ingrese un número para verificar si es oblongo: "))))

"""
b. Informar si un número es triangular. Un número se define como triangular si puede
expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1.Por ejemplo
10 es un número triangular porque se obtiene sumando 1+2+3+4.
"""

# num_triangular = lambda x: any((a * (a  + 1)) // 2 == x for a in range(1, x))
