#Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar “x”.
#- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
#- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
#-Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

def NumerodeNombres(alumnos):
   nombre_kmdt=input("Nombre: ")
   while nombre_kmdt!="x":
       alumnos.add(nombre_kmdt)
       nombre_kmdt=input("Nombre: ")
   return alumnos

primaria_kmdt=set()
secundaria_kmdt=set()
print("ALUMNOS DE PRIMARIA")
primaria_kmdt=NumerodeNombres(primaria_kmdt)
print("ALUMNOS DE SECUNDARIA")
secundaria_kmdt=NumerodeNombres(secundaria_kmdt)

print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre_kmdt in primaria_kmdt|secundaria_kmdt:
   print(nombre_kmdt)

print("NOMBRES COMUNES:")
for nombre_kmdt in primaria_kmdt&secundaria_kmdt:
   print(nombre_kmdt)

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre_kmdt in primaria_kmdt-secundaria_kmdt:
   print(nombre_kmdt)