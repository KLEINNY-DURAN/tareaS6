#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.


positivos_kmdt=0
n_kmdt=int(input("Número (0 para terminar): "))
while n_kmdt!=0:
    if n_kmdt>0:
        positivos_kmdt+=1
    n_kmdt=int(input("Número (0 para terminar): "))
print("Cantidad de positivos:", positivos_kmdt)