# Encontar x3 + x = 100
operacion = 0
x = 0
print("     x     |  Lado Izq ")
print("-----------|-----------")

while (operacion < 5):
    operacion = (x ** 3)+ x
    x = x + 0.005
    #print("x",x,"operacion",operacion)
    print("%10.4f | %10.4f"%(x,operacion))
