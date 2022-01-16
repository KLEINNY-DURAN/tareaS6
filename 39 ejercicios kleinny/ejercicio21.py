#Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".

def validar_kmdt(email):
    caracterBuscado_kmdt="@"
    emailValido_kmdt=False
    for c_kmdt in email:
        if c_kmdt==caracterBuscado_kmdt:
            return True
    return False

#programa principal
direccion_kmdt=input("Tu email: ")
if validar_kmdt(direccion_kmdt):
    print("Dirección válida")
else:
    print("Dirección inválida")