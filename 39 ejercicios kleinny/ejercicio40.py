#Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación, imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Si no es así, imprimir “no hay coincidencia”.


nombre1_kmdt=input("Un nombre: ")
nombre2_kmdt=input("Otro nombre: ")
posicion_final_nombre1_kmdt=len(nombre1_kmdt)-1
posicion_final_nombre2_kmdt=len(nombre2_kmdt)-1
if nombre1_kmdt[0] == nombre2_kmdt[0] or nombre1_kmdt[posicion_final_nombre1_kmdt] == nombre2_kmdt[posicion_final_nombre2_kmdt]:
    print("coincidencia")
else:
    print("no hay coincidencia")