#Tarea 9_1 Programa de numeros enteros:
#Luis Pablo López Iracheta 192301-9
def Entero(x):
    lista = []
    for i in range(1, x + 1):
        lista.append(i)
    return lista


numeroEntero = int(input("Número entero: "))
resultado = Entero(numeroEntero)

print(resultado)


