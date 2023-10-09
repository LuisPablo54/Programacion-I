#Tarea 5_2 Secuencia con ford
#Luis Pablo López Iracheta 192301-9

alturaOriginal_m = 5
alturaRelativa_m = 0
velocidadOriginal_m_s = 10
gravedad = -9.81
tiempo_s = 0

print("  Tiempo  |  Altura  ")
print("----------|-----------")
#Inicio del ciclo
#Formula: y = y0 + v0 * t + ((a * t2) / 2)
while (alturaRelativa_m >= 0):
    velocidadPorTiempo = velocidadOriginal_m_s * tiempo_s
    aceleracionPorTiempo = (gravedad * (tiempo_s ** 2)) / 2
    alturaRelativa_m = (alturaOriginal_m + velocidadPorTiempo + aceleracionPorTiempo)
    print("%6.1f    | %6.2f"%(tiempo_s,alturaRelativa_m))
    tiempo_s = tiempo_s + 0.1

print("Fin del programa")