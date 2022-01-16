#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
#Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.


numero_kmdt=int(input("numero: "))
totalPares_kmdt=0
totalImpares_kmdt=0
while numero_kmdt!=0:
   pares_kmdt=0
   impares_kmdt=0
   while numero_kmdt!=0:   
       ultimodigito_kmdt=numero_kmdt%10
       if ultimodigito_kmdt%2==0:
           pares_kmdt+=1
           totalPares_kmdt+=1
       else:
           impares_kmdt+=1
           totalImpares_kmdt+=1
       numero_kmdt=numero_kmdt//10
   print("El número ingresado tiene ",pares_kmdt," digitos pares y ",impares_kmdt," digitos impares")
   numero_kmdt=int(input("Otro número: "))
print("Total de dígitos pares:", totalPares_kmdt)
print("Total de dígitos impares:", totalImpares_kmdt)