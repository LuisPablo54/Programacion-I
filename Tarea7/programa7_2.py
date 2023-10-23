#Tarea 7_2 Busqueda exhautiva
#Luis Pablo López Iracheta 192301-9

#NO ME LA CREO, ME VOLVIO A TOCAR PASAR!!!!
#Las librerias
import math 
import matplotlib.pyplot as plt

#Datos
distanci_final = 0
angulo_G = 0
velocidadInicial_m_s = 400
gravedad_m_s = 9.81

#Ejes
distancia_Y = []
angulos_X = []

print("  Grados  | Distancia ")
print("----------|-----------")



while distanci_final < 9980:
    #Convierto el angulo en radianes
    angulo_rad = math.radians(angulo_G)

    #Optengo el coseno y seno del angulo en radianes
    coseno_rad = math.cos(angulo_rad)
    seno_rad = math.sin(angulo_rad) 
   

    #Furmula para la distancia
    distanci_final = ((2 * (velocidadInicial_m_s ** 2) * coseno_rad * seno_rad ) / gravedad_m_s)
    
    print(" %6.2f   |  %6.2f  "%(angulo_G ,distanci_final))

    #Guardar y aumentar los datos
    distancia_Y.append(distanci_final)
    angulos_X.append(angulo_G)
    angulo_G = angulo_G + 0.1

#Ajuste de ciclo
angulo_G = angulo_G - 0.1
#Grafica y sus propiedades
plt.plot(angulos_X, distancia_Y, "g-", label ="Distancia - Ángulo")
plt.ylabel("Distancia [m]") 
plt.xlabel("Ángulo [grados]")
plt.legend()
plt.title('Bala de cañon')
plt.gca().set_facecolor('#EAEAF2')
plt.grid(True)

valor_destacado_x = angulo_G
valor_destacado_y = distanci_final



plt.scatter(angulo_G, distanci_final, color='red', marker='*', label='Valor destacado')
plt.annotate(f'({angulo_G:.3f}, {distanci_final:.3f})', (valor_destacado_x, valor_destacado_y), textcoords="offset points", xytext=(10, 10), ha="center")



plt.show()