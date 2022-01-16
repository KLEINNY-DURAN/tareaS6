#Sin ejecutar el siguiente programa, determinar cuál es la salida en pantalla si se ingresan los valores x=6, y=7:

def coordenadaZ_kmdt(x,y):
  x=x+10
  y=y+15
  return x+y

#programa principal
x_kmdt=int(input("Coordenada eje x: "))
y_kmdt=int(input("Coordenada eje y: "))
for i in range(3):
  z_kmdt=coordenadaZ_kmdt(x_kmdt,y_kmdt)
  x_kmdt=x_kmdt+1
  y_kmdt=y_kmdt+1
print(x_kmdt," . ",y_kmdt)