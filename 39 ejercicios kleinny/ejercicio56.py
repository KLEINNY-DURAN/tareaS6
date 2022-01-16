#Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.


frase_kmdt=input("Frase: ").strip()
cantidad_kmdt=0
len_p_mas_larga_kmdt=0
while len(frase_kmdt) != 0:
    cantidad_kmdt=cantidad_kmdt+1
    i=frase_kmdt.find(" ")
    if i != -1:
        palabra_kmdt=frase_kmdt[0:i]
        while i < len(frase_kmdt) and frase_kmdt[i] == " ":
            i=i+1
        frase_kmdt=frase_kmdt[i:]
    else:
        palabra_kmdt=frase_kmdt
        frase_kmdt=""
    if len(palabra_kmdt) > len_p_mas_larga_kmdt:
        len_p_mas_larga_kmdt=len(palabra_kmdt)
        p_mas_larga_kmdt=palabra_kmdt
if cantidad_kmdt > 0:
    print("Palabra más larga:", p_mas_larga_kmdt)
print("Cantidad de palabras:", cantidad_kmdt)
