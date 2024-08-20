"""Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10."""

def vuelto_cajero(venta, pago):
    if pago < venta:
        print("El dinero recibido es insuficiente.")
        return
    #
    vuelto = pago - venta
    if vuelto == 0:
        print("Pago con el dinero justo, no debe dar vuelto.")
        return
    #
    billetes = [
            [5000, 1000, 500, 200, 100, 50, 10],# Denominación
            [0, 0, 0, 0, 0, 0, 0]]#Cantidad
    print(f"El vuelto que se debe dar es de {vuelto}.")
    #  
    for i in range(len(billetes[0])):
        while vuelto >= billetes[0][i]:
            billetes[1][i] += 1
            vuelto -= billetes[0][i]
            
    for i in range(len(billetes[0])):
        if billetes[1][i] > 0:
            print(f"{billetes[1][i]} billete/s de ${billetes[0][i]}.")
    
    if vuelto > 0:
        print("El vuelto no puede entregarse por falta de billetes con denominación adecuada.")
        
compra = int(input("Ingrese el monto de la venta: "))
pagado = int(input("Ingrese el monto que pago el cliente: "))
vuelto_cajero(compra, pagado)