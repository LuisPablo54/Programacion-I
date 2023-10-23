#Tarea 7_1 Coete
#Luis Pablo López Iracheta 192301-9

#NO ME LA CREO, ME VOLVIO A TOCAR PASAR!!!!
import math 
import matplotlib.pyplot as plt

#Formula: d = ((2 * (v0 ** 2) * cos(angulo) * sin (angulo) ) / 9.81m_s)

#Datos
gravedad_m_s = 9.81
angulo_G = 0
velocidadInicial_m_s = 400

#Ejes
distancia_Y = []
angulos_X = []

print("  Grados  | Distancia ")
print("----------|-----------")



while angulo_G < 91:
    #Convierto el angulo en radianes
    angulo_rad = math.radians(angulo_G)

    #Optengo el coseno y seno del angulo en radianes
    coseno_rad = math.cos(angulo_rad)
    seno_rad = math.sin(angulo_rad) 
   

    #Furmula para la distancia
    distancia = ((2 * (velocidadInicial_m_s ** 2) * coseno_rad * seno_rad ) / gravedad_m_s)
    
    print(" %6.2f   |  %6.2f  "%(angulo_G ,distancia))
    
    #Guardar y aumentar los datos
    distancia_Y.append(distancia)
    angulos_X.append(angulo_G)
    angulo_G = angulo_G + 5

#Grafica y sus propiedades
plt.plot(angulos_X, distancia_Y, "go--", label ="Distancia - Ángulo")
plt.ylabel("Distancia [m]") 
plt.xlabel("Ángulo [grados]")
plt.legend()
plt.title('Bala de cañon')
plt.gca().set_facecolor('#EAEAF2')
plt.grid(True)
plt.show()