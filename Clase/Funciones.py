#Funciones con lisatas
#Todas las funciones tiene que tener un 'return' incluso vacio
def miLista (x): #Un alias
    x = x * 2
    return x

def clonandoLista (x): # Un clon
    print("x: ", x)
    y = x[:] #Colando la lista en y
    y[0] = y[0] * 5 #Multiplico el primer valor por 5
    return y

#Valores de return, puedo incluso haber varios valores de return en una función
def Maximo(a, b):
    if a > b:
        resultado = a
    else:
        resultado = b

    return resultado #Return es como un brake

    print("Esto no se va a ejecutar")
    

a = [1, 2, 3, 4]
y = miLista(a)
d = clonandoLista(a)



print("y: ", y)
print("a: ", a)
print("d: ", d)

print("El valor maximo es", Maximo(10, 20))
