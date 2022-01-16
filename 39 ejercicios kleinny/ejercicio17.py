#Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

n1_kmdt=0
n2_kmdt=1
print(n1_kmdt)
print(n2_kmdt)
for i in range(8):
    n3_kmdt=n1_kmdt+n2_kmdt
    print(n3_kmdt)
    n1_kmdt=n2_kmdt
    n2_kmdt=n3_kmdt