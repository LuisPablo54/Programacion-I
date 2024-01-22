#Numero ramdom y contarlos

import random

#Genero la listas vacia
lista = []

for i in range(0, 16):
    lista.append(0)

for i in range(32):
    numero =random.randint(1, 15)
    lista[numero] += 1
    #print(numero)

#Imprimo la lista
print("Resultados")
for i in range (0, 16):
    print(i, ":", lista[i])
print("Fin")

#Lista de baraja
miLista = []
for i in range (1, 7):
    miLista.append(i)

print("Lista:", lista)

for posiscipon in range(0, 6):
    nuevaPos = random.randint(0,5)
    (lista[posiscipon], lista[nuevaPos]) = (lista[nuevaPos], lista[posiscipon])

print("Lista recuelta: ", lista)
