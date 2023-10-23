#Tarea 7_4 Logaritmo
#Luis Pablo López Iracheta 192301-9

#NO ME LA CREO, ME VOLVIO A TOCAR PASAR!!!!
#Las librerias
import math

#Logaritmo natural de (1 + 0.8)

x = float(input("Ingresa el numero que quieres: "))
resultado = 0


for i in range(1, 101):
    resultado += ((-1) ** (i + 1)) * ((x ** i) / i)

print(f'El resultado de {x} es: {resultado:.3f}')
