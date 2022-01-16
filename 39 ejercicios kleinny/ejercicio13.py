#Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase.

frase_kmdt=input("Frase: ")
cantidad_kmdt=0
for x in frase_kmdt:
    if x in "aeiou":
        cantidad_kmdt+=1
print("Cantidad de vocales:", cantidad_kmdt)