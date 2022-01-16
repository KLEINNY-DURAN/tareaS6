#Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.

def lenUltimaPalabra_kmdt(frase):
   if len(frase)==0:
       return 0
   cantidad_kmdt=0
   for i in range(len(frase)):
       if frase[i]!=' ':
           cantidad_kmdt+=1
       else:
           if i<len(frase)-1 and frase[i+1]!=' ':
               cantidad_kmdt=0
   return cantidad_kmdt