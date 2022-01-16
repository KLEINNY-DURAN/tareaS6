#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.


suma_kmdt=0
n_kmdt=int(input("Número positivo:"))
while n_kmdt!=0:
    digito_kmdt=n_kmdt%10
    suma_kmdt+=digito_kmdt
    n_kmdt=n_kmdt//10
print("Suma de los dígitos:", suma_kmdt)