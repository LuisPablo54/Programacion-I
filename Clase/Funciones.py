#Funciones con lisatas

def miLista (x): #Un alias
    x = x * 2
    return x

def clonandoLista (x): # Un clon
    print("x: ", x)
    y = x[:] #Colando la lista en y
    y[0] = y[0] * 5 #Multiplico el primer valor por 5
    return y


a = [1, 2, 3, 4]
y = miLista(a)
d = clonandoLista(a)

print("y: ", y)
print("a: ", a)
print("d: ", d)

