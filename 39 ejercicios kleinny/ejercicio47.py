#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.


mayor_kmdt=-1
n_kmdt=int(input("Número positivo:"))
while n_kmdt>=0:
   if n_kmdt>mayor_kmdt:
       mayor_kmdt=n_kmdt
   n_kmdt=int(input("Número positivo:"))
print("Mayor número ingresado:", mayor_kmdt)