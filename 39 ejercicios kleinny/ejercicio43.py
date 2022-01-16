#Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.


anio_kmdt=int(input("Año:"))
if anio_kmdt%4 == 0:
    if anio_kmdt%100 != 0 or anio_kmdt%400 == 0:
        print("Bisiesto")
    else:
        print("No bisiesto")
else:
    print("No bisiesto")