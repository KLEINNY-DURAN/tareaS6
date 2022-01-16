#Escribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos fue menor que 10. Utilizar una o más funciones, según sea necesario.

def sumaDigitos_kmdt(numero):
  suma_kmdt=0
  while numero!=0:
      digito_kmdt=numero%10
      suma_kmdt=suma_kmdt+digito_kmdt
      numero=numero//10
  return suma_kmdt

#programa principal
cantidad_kmdt=0
mayor_kmdt=-1
numero_kmdt=int(input("Número positivo: "))
while numero_kmdt>=0:
    suma_kmdt=sumaDigitos_kmdt(numero_kmdt)
    if suma_kmdt > mayor_kmdt:
          mayor_kmdt=suma_kmdt
          n_mayorsuma_kmdt=numero_kmdt
    if suma_kmdt < 10:
        cantidad_kmdt+=1
    numero_kmdt=int(input("Número positivo: "))
print("Sumatoria de dígitos de",n_mayorsuma_kmdt,":",mayor_kmdt)
print("Cantidad con sumatoria menor a 10:",cantidad_kmdt)