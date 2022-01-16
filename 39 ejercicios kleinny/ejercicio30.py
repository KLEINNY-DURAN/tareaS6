#El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?

def maximo_kmdt(a,b):
  if x_kmdt>y_kmdt:
    return x_kmdt
  else:
    return y_kmdt

def minimo_kmdt(a,b):
  if x_kmdt<y_kmdt:
    return x_kmdt
  else:
    return y_kmdt

#programa principal
x_kmdt=int(input("Un número: "))
y_kmdt=int(input("Otro número: "))
print(maximo_kmdt(x_kmdt-3, minimo_kmdt(x_kmdt+2, y_kmdt-5)))