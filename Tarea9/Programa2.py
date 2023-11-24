#Tarea 9_2 Numeros maximos y minmos
#Luis Pablo López Iracheta 192301-9
def MaximoMinimo(numero):
    numeroMinimo = numero[:]
    numeroMinimo.sort()

    numeroMaximo = numero[:]
    numeroMaximo.sort(reverse=True)
    print(f"Lista original: {numero}")
    print(f"El numero menor es: {numeroMinimo[0]}")
    print(f"El numero mayor es: {numeroMaximo[0]}")

numero = [3, 5, 2, 8,]
resultado = MaximoMinimo(numero)

