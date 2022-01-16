#Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo: "r":5, "%":3, "a":8, "9":1.
#¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, incluyendo el valor 0 para las letras que no aparecieron?

kmdt_contadores={}
for i in range(50):
   cadena_kmdt=input("Cadena de caracteres: ")
   for caracter_kmdt in cadena_kmdt:
       if caracter_kmdt not in kmdt_contadores:
           kmdt_contadores[caracter_kmdt]=1
       else:
           kmdt_contadores[caracter_kmdt]+=1
print("Frecuencia de cada carácter")
for caracter_kmdt, cantidad_kmdt in kmdt_contadores.items():
   print(caracter_kmdt, ": ", cantidad_kmdt)

#Para contabilizar sólo letras (mayúsculas y minúsculas por separado):
kmdt_contadores={}
alfabeto_kmdt="abcdefghijklmnñopqrstuvwxyz"
for letra in alfabeto_kmdt+alfabeto_kmdt.upper():
    kmdt_contadores[letra]=0
for i in range(50):
   cadena_kmdt=input("Cadena de caracteres: ")
   for caracter_kmdt in cadena_kmdt:
       if caracter_kmdt.lower() in alfabeto_kmdt:
           kmdt_contadores[caracter_kmdt]+=1
print("Frecuencia de cada letra")
for caracter_kmdt, cantidad_kmdt in kmdt_contadores.items():
   print(caracter_kmdt, ": ", cantidad_kmdt)