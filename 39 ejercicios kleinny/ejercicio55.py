#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.


cantidad_kmdt=0
n_kmdt=int(input("Número: "))
while n_kmdt!=0:
 primo_kmdt=True
 for i in range(2,n_kmdt):
   if n_kmdt%i==0:
     primo_kmdt=False
     break
 if primo_kmdt:
   cantidad_kmdt+=1
 n_kmdt=int(input("Número: "))
print("primos: ", cantidad_kmdt)