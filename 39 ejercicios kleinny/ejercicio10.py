#Requerir al usuario que ingrese un número entero positivo e imprimir todos los números correlativos entre el ingresado por el usuario y uno menos del doble del mismo.

n_kmdt=int(input("Número: "))
for x in range(n_kmdt, n_kmdt*2):
    print(x)