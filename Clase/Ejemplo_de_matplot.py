import matplotlib.pyplot as plt
y = [10, 12, 13, 14, 13] #Primera funcion
y2 = [20, 24, 26, 28, 26] #Segunda funcion
tiempo= [0, 0.1, 0.2, 0.3, 0.4] #Tiempo en x


plt.plot(tiempo, y, "go--", label ="Y") #Grafica 1
plt.plot(tiempo, y2, "ro-", label = "Y2") #Grafica 3
#plt.plot(tiempo, y, "go-") Lineas continuas
#plt.plot(tiempo, y, "gx") Con una x en cada numero
#plt.plot(tiempo, y, "g^") Triangulo

#Etiquetas
plt.ylabel("y [m]") 
plt.xlabel("x [s]")
plt.legend()

plt.show()

