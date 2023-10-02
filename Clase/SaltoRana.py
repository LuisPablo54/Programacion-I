#Una rana debe de recorrer una 100 metros minimo, determina los saltos necesario para llegar si la rana se cansa 
#un 0.9 en cada salto

n = 1
d = 0
s = 15

while (d < 100):
    d = d + s  #Operacion para saltar
    s = s * .9 #Cansancio de la rana
    print(f"distnacia: {d}, saltos: {n}, distancia de salto: {s}")

    n = n + 1 #Incremento para contar los saltos
print("Fin del program")

