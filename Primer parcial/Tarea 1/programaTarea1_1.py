#Tarea 1.1 Objeto
#Luis Pablo López Iracheta 192301-9

#Declaro y valores:

posicionInicial_m = 10
tiempo_s = 15
velocidadInical_m_s = 10
aceleracion_m_s2 = -9.81

#Realizo la operación

posicionFinal = (posicionInicial_m) + (velocidadInical_m_s * tiempo_s) + (((aceleracion_m_s2)*(tiempo_s ** 2))/2)


print(f"La posición final respecto a mi punto de referencia es: {posicionFinal} metros")
print("Fin del programa")
