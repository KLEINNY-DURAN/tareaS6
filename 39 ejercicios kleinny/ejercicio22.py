#Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).

def sumaDigitos_kmdt(numero):
    suma_kmdt=0
    while numero!=0:
        digito_kmdt=numero%10
        suma_kmdt=suma_kmdt+digito_kmdt
        numero=numero//10
    return suma_kmdt

#programa principal
num_kmdt=int(input("Número a procesar: "))
while num_kmdt!=0:
    print("Suma:",sumaDigitos_kmdt(num_kmdt))
    num_kmdt=int(input("Número a procesar: "))