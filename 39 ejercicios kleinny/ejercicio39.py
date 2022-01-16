#Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).


numero_kmdt=int(input("Número:"))
if numero_kmdt<0:
    numero_kmdt=numero_kmdt*-1
print("Valor absoluto:", numero_kmdt)