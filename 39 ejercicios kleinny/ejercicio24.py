#Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.

def primo_kmdt(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

#programa principal
numero_kmdt=int(input("Número: "))
if primo_kmdt(numero_kmdt):
    print("Es primo")
else:
    print("No es primo")