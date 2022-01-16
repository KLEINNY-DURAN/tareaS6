#Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.

def primo_kmdt(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True

def frecuencia_kmdt(numero,digito):
   cantidad_kmdt=0
   while numero!=0:
       ultDigito_kmdt=numero%10
       if ultDigito_kmdt==digito:
           cantidad_kmdt+=1
       numero=numero//10
   return cantidad_kmdt

def factorial_kmdt(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f

def sumaDigitos_kmdt(numero):
  suma_kmdt=0
  while numero!=0:
      digito_kmdt=numero%10
      suma_kmdt=suma_kmdt+digito_kmdt
      numero=numero//10
  return suma_kmdt

#programa principal
mayor_kmdt=0
numero_kmdt=int(input("Número primo: "))
while primo_kmdt(numero_kmdt):
    print("Suma de los dígitos:",sumaDigitos_kmdt(numero_kmdt))
    digito_kmdt=int(input("Dígito: "))
    print("El",digito_kmdt,"aparece",frecuencia_kmdt(numero_kmdt,digito_kmdt),"veces")
    if numero_kmdt > mayor_kmdt:
          mayor_kmdt=numero_kmdt
    numero_kmdt=int(input("Número primo: "))
print("Factorial de",mayor_kmdt,":",factorial_kmdt(mayor_kmdt))