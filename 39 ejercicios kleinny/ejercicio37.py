#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales.


a_kmdt=int(input("Un número:"))
b_kmdt=int(input("Otro número:"))
if a_kmdt<b_kmdt:
    print("El primero es menor")
elif b_kmdt<a_kmdt:
    print("El segundo es menor")
else:
    print("Son iguales")