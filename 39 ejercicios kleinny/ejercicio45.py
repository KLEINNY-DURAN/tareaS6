#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.


total_kmdt=0
nro_kmdt=int(input("Número: "))
while nro_kmdt != 0:
    total_kmdt+=nro_kmdt
    nro_kmdt=int(input("Número: "))