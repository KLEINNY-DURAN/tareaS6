#Crear un programa para gestionar datos de los socios de un club, permitiendo:
#-Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados:
#Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
#Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
#Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
#-Informar cantidad de socios del club.
#-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
#-Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.
#-Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
#-Imprimir el listado de socios completo.

def cargardeSocios(socios):
   numero_kmdt=int(input("Número de socio (0 para cortar): "))
   while numero_kmdt!=0:
       nombre_kmdt=input("Nombre y apellido: ")
       fecha_kmdt=input("Fecha de ingreso (DDMMAAAA): ")
       cuota_kmdt=input("¿Cuota al día? s/n: ")
       socios[numero_kmdt]=[nombre_kmdt,fecha_kmdt,cuota_kmdt.lower()=="s"]
       numero_kmdt=int(input("Número de socio (0 para cortar): "))
   return socios

def modificar_Fecha(socios, fecha_anterior, fecha_nueva):
   for datos in socios.values():
       if datos[1]==fecha_anterior:
           datos[1]=fecha_nueva
   return socios

def numero_Socio(socios, nombre):
   for numero_kmdt,datos in socios.items():
       if datos[0].lower()==nombre.lower():
           return numero_kmdt
   return 0

def formato_Fecha(fecha):
   return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]

def imprimir_Listado(socios):
   for numero_kmdt,datos in socios.items():
       print("-Número:",numero_kmdt)
       print("-Nombre:",datos[0])
       print("-Ingresó:", formato_Fecha(datos[1]))
       if datos[2]:
           print("-Cuota al día")
       else:
           print("-En deuda")

socios_activos_kmdt={1:["Amanda Núñez","17032009",True], 2:["Bárbara Molina","17032009",True], 3:["Lautaro Campos","17032009",True]}

print("***Cargar socios")
socios_activos_kmdt=cargardeSocios(socios_activos_kmdt)

print("El club tiene", len(socios_activos_kmdt), "socios")

print("***Registrar pago de cuotas")
numero_kmdt=int(input("Número de socio: "))
socios_activos_kmdt[numero_kmdt][2]=True

print("***Modificando fecha de ingreso...")
socio_activo_kmdt=modificar_Fecha(socios_activos_kmdt, "13032018", "14032018")

print("***Eliminar socio")
nombre_kmdt=input("Nombre y apellido: ")
numero_kmdt=numero_Socio(socios_activos_kmdt, nombre_kmdt)
if numero_kmdt in socios_activos_kmdt:
    del socios_activos_kmdt[numero_kmdt]

imprimir_Listado(socios_activos_kmdt)