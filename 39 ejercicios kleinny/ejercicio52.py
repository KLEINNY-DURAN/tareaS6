#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
#Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.


total_kmdt=0
monto_kmdt=float(input("Monto de una venta: $"))
while monto_kmdt!=0:
    if monto_kmdt<0:
        print("Monto no válido.")
    else:
        total_kmdt+=monto_kmdt
    monto_kmdt=float(input("Monto de una venta: $"))
if total_kmdt>1000:
    total_kmdt-=total_kmdt*0.1
print("Monto total a pagar: $", total_kmdt)