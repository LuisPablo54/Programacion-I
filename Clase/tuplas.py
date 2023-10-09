#Creamos un programa con tuplas, listas y cadenas de texto

A = (1, 2, 3, 4, 5, 6, 7)

#A = "ABCDEFJHI"

print("La tupla es: ", A)

primero = A[0]
print("Primero", primero)

tercero = A[2]
print("Tercero", tercero)


ultimo = A[-1]
print("Ultimo", ultimo)

#Optener una rebanada de la tupla
rebanada = A[0:4]
print("La rebanada es: ", rebanada)


#Igual, quiere decir desde el princio
'''
rebanada = A[ :4]
print("La rebanada es: ", rebanada)'''

#La ultima rebanada
rebanada = A[4: len(A)]
print("Los ultimos son: ", rebanada)

for index in range (0, len(A)):
    print("index: ", index, "A [index]", A[index])

#Barrer una lista
print("Barriendo una lista usando index: ")
for i in range(0, len(A)):
    print("i: ", i, "A[i]: ", A[i])

print("Barriendo una lista directamente: ")
for elemento in A:
    print(elemento)


#Operadores de la tupla
print("Operadores de una tupa:")
B = (1, 2, 3, 4)
C = A + B
print("C es igual a: ", C)

Btriplicado = B * 3
print("B triplicado: ", Btriplicado)

#Diferencia entre una tupla y una lista

miTupla = (1, 2, 3, 4)
miLista = [1, 2, 3, 4]




