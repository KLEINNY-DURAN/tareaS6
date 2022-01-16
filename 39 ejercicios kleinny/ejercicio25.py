#Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

def factorial_kmdt(numero):
   f_kmdt=1
   if numero!=0:
       for i in range(1,numero+1):
           f_kmdt=f_kmdt*i
   return f_kmdt

#programa principal
cantidad_kmdt=0
num_kmdt=int(input("Número (-1 para cortar): "))
while num_kmdt!=-1:
    print("Factorial:", factorial_kmdt(num_kmdt))
    cantidad_kmdt+=1
    num_kmdt=int(input("Número (-1 para cortar): "))
print("Se leyeron",cantidad_kmdt,"números")