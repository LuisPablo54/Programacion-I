#Tarea 6_1
#Luis Pablo López Iracheta 192301-9


#Empezar a preguntar sobre los numeros
numerosIngresados = 0
miLista = []

while numerosIngresados < 10:
    numero = float(input("Numero a ingresar: "))
    miLista.append(numero)
    print("Guardando....")
    print("Listo")
    numerosIngresados = numerosIngresados + 1

print(miLista)

#Encontamos el mayor
mayor = menor = miLista[0]


for numero in miLista:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")

#Promedio:
suma = 0
contador = 0

for numero in miLista:
    suma += numero  # Suma el número actual a la suma
    contador += 1  # Incrementa el contador

# Calcula el promedio
promedio = suma / contador

print(f"Promedio: {promedio} ")