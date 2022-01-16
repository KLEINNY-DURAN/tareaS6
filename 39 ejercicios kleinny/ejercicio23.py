#Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2.

def sumaDigitos_kmdt(numero):
    suma_kmdt=0
    while numero!=0:
        digito_kmdt=numero%10
        suma_kmdt=suma_kmdt+digito_kmdt
        numero=numero//10
    return suma_kmdt

#programa principal
sumatoria_kmdt=0
num_kmdt=int(input("Número a procesar: "))
while num_kmdt!=0:
    print("Suma:",sumaDigitos_kmdt(num_kmdt))
    sumatoria_kmdt=sumatoria_kmdt+num_kmdt
    num_kmdt=int(input("Número a procesar: "))
print("Sumatoria:", sumatoria_kmdt)
print("Dígitos:", sumaDigitos_kmdt(sumatoria_kmdt))