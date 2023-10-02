#Tarea 4_3 Tornillo 2D inversa
#Luis Pablo López Iracheta 192301-9

TornilloX = float(input("Cual es la posición en x del tornillo: "))
print(f"Guardado: x = {TornilloX}")
TornilloY = float(input("Cual es la posición en y del tornillo: "))
print(f"Guardado: x = {TornilloX}, y = {TornilloY}")

Y = ((TornilloY ) // 15) #La posición en Y 
X = ((TornilloX ) // 15) #La posición en X 

#Determino el numero de tornillo 
n = (Y * 8) + X

print(f"El numero de tornillo es {n}")

print(f"Fin del programa")