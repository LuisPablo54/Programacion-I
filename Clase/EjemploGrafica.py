import matplotlib.pyplot as plt
import math

x = []
y = []

z = []
w = []

a = 0
b = 0

while a < 30:
    esteX = a * math.cos(a)
    esteY = a * math.sin(a)
    x.append(esteX)
    y.append(esteY)
   
    a = a + 0.5

while b < 20:
    esteZ = b * math.cos(b)
    esteW = b * math.sin(b)
    z.append(esteZ)
    w.append(esteW)
   
    a = a + 0.2

plt.plot(x, y, "go-", label = "etiqueta Y")
plt.plot(z, w, "go-", label = "etiqueta Y")

plt.show()