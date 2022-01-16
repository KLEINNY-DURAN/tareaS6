#Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def validarDNI_kmdt(dni):
   cantidad_kmdt=0
   while dni!=0:
       cantidad_kmdt+=1
       dni//=10
   return cantidad_kmdt==7 or cantidad_kmdt==8