#Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

anioInicio_kmdt=int(input("Año inicial:"))
anioFin_kmdt=int(input("Año final:"))
for anio_kmdt in range(anioInicio_kmdt, anioFin_kmdt+1):
   if not anio_kmdt%10==0:
       continue
   if not anio_kmdt%4==0:
       continue
   if anio_kmdt%100!=0 or anio_kmdt%400==0:
       print(anio_kmdt) 