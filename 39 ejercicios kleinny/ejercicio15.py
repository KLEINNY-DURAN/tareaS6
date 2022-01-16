#Escribir un programa que muestre la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.

total_kmdt=0
for i in range(101):
    if total_kmdt%3 == 0:
        total_kmdt=total_kmdt+i
print("Sumatoria de los múltiplos de 3:", total_kmdt)