#Ejercico 5


numero = float(input("Numero a redondear: "))
redondeo = int(input("Cantidad de decimas: "))

valor = (numero + (0.5 / (10 ** redondeo)))* (10 ** redondeo)
valorEntero = int(valor)
resultado = valorEntero / (10 ** redondeo)

print(f"El numero redondeado es: {resultado}")

print("Fin del programa")
