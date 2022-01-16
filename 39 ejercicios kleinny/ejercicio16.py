#Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.

numero_kmdt=int(input("Número:"))
fac=1
if numero_kmdt!=0:
    for i in range(1,numero_kmdt+1):
        fac=fac*i
print("Factorial:", fac)