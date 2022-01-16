#Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

frase_kmdt=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiou":
  if x in frase_kmdt:
    print(x)