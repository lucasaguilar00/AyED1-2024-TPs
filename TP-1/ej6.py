"""
Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite utilizar 
facilidades de Python no vistas en clase.
"""
def concatenar(a : int,b : int):
    #Concatena dos números enteros cambiandolos a string y luego los retorna como enteros otra vez.
    c = str(a) + str(b)
    return int(c)