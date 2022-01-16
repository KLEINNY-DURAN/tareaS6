#Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.


letra_kmdt=input("Letra:")
if len(letra_kmdt)!=1:
    print("Debe ser sólo una letra")
else:
 letra_kmdt in "aeiou"
print("Es vocal")