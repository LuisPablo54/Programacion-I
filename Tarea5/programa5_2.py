#Tarea 5_2 Secuencia con ford
#Luis Pablo López Iracheta 192301-9
primeraSecuencia = []
segundaSecuencia = [3]
terceraSecuencia = []
cuartaSecuencia = [19]

# Primer arreglo de numeros
for S_Uno in range(1, 8):
    primeraSecuencia.append(S_Uno)
print(primeraSecuencia)

# Segundo arreglo de numeros
for S_Dos in range(8, 23, 5):
    segundaSecuencia.append(S_Dos)
print(segundaSecuencia)

# Tercer arreglo de numeros
for S_Tres in range(20, -11, -6):
    terceraSecuencia.append(S_Tres)
print(terceraSecuencia)

# Cuarto arreglo de numeros
for S_Cuatro in range(27, 52, 8):
    cuartaSecuencia.append(S_Cuatro)
print(cuartaSecuencia)

print("Fin del programa")
