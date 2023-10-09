#Tarea 5_1 Secuencia
#Luis Pablo López Iracheta 192301-9

primeraSecuencia = []
segundaSecuencia = [3]
terceraSecuencia = [20]
cuartaSecuencia = [19]

S_Uno = 0
S_Dos = 3
S_Tres = 20
S_Cuatro = 19


#Primer arreglo de numeros
while (S_Uno < 7):
    S_Uno = S_Uno + 1
    primeraSecuencia.append(S_Uno) 
print(primeraSecuencia )

#Segundo arreglo de numeros
while (S_Dos < 23):
    S_Dos = S_Dos + 5
    segundaSecuencia.append(S_Dos) 
print(segundaSecuencia)


#Tercer arreglo de numeros
while (S_Tres > -10):
    S_Tres = S_Tres - 6
    terceraSecuencia.append(S_Tres) 
print(terceraSecuencia)

#Cuarto arreglo de numeros
while (S_Cuatro < 51):
    S_Cuatro = S_Cuatro + 8
    cuartaSecuencia.append(S_Cuatro) 
print(cuartaSecuencia)

print("Fin del programa")