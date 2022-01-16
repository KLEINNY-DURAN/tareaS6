#Escribir un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos.
#No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.

suma_Positivos=0
cantidad_Positivos=0
suma_Negativos=0
for i in range(6):
   nro_kmdt=int(input("Número: "))
   if nro_kmdt>0:
       suma_Positivos=suma_Positivos+nro_kmdt
       cantidad_Positivos=cantidad_Positivos+1
   else:
       sumaNegativos=sumaNegativos+nro_kmdt
print("Sumatoria de los negativos: ", suma_Negativos)
if cantidad_Positivos!=0:
   print("Promedio de los positivos: ",suma_Positivos/cantidad_Positivos)
else:
   print("No se ingresaron números positivos")