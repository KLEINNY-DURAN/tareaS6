#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.


pares_kmdt=0
n_kmdt=int(input("Número (-1 para terminar el programa): "))
while n_kmdt!=-1:
    if n_kmdt%2 == 0:
        pares_kmdt+=1
    suma_kmdt=0
    while n_kmdt!=0:
        digito_kmdt=n_kmdt%10
        suma_kmdt+=digito_kmdt
        n_kmdt=n_kmdt//10
    print("Suma de sus dígitos:", suma_kmdt)
    n_kmdt=int(input("Número (-1 para terminar el programa): "))
print("Se ingresaron", pares_kmdt, "números pares")