#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.


frase_kmdt=input("Frase: ")
l_kmdt=input("Letra para buscar su posición: ")
i_kmdt=0
while i_kmdt!=len(frase_kmdt):
    if l_kmdt!=frase_kmdt[i_kmdt]:
        print("No se encontró en la posición", i_kmdt)
        i_kmdt+=1
        continue
    print("Se encontró en la posición", i_kmdt)
    break