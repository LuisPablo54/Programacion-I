import matplotlib.pyplot as plt
y = [10, 12, 13, 14, 13] #Primera funcion

tiempo= [0, 0.1, 0.2, 0.3, 0.4] #Tiempo en x


plt.plot(tiempo, y, "go--", label ="Y") #Grafica 1

#plt.plot(tiempo, y, "go-") Lineas continuas
#plt.plot(tiempo, y, "gx") Con una x en cada numero
#plt.plot(tiempo, y, "g^") Triangulo

#Etiquetas
plt.ylabel("y [m]") 
plt.xlabel("x [s]")
plt.legend()

plt.show()

