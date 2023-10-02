import random

Apuesta = int(input("La suma a la que apuestas: "))

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

suma = dado1 + dado2

print("Dados: ", dado1, dado2)
print("Suma: ", suma)

if Apuesta == suma:
    print("Ganaste")
else: 
    print("Intente nuevamte")
