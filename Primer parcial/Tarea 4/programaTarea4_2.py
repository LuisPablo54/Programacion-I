#Tarea 2_5 Tornillo 2D
#Luis Pablo López Iracheta 192301-9

Tornillo = int(input("Cual tornillo (0-23): "))


posicionY = 7.5 + ((Tornillo // 8) * 15)

posicionX = 7.5 + ((Tornillo % 8) * 15)

print(f"El valor en coordenadas seria: x = {posicionX}, y = {posicionY}")
print("Fin del programa")