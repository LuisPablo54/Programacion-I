#Tarea 2_4 Obperaciones
#Luis Pablo López Iracheta 192301-9

#Enter the number that I will round the decimals
numberDecimals = float(input("Ingrese un numero con decimal: "))
round = int(input("Ingrese la cantidad de decimales a redondear: "))

# I do the rounding operation
numberDecimals = numberDecimals + (5 / (10 ** (round + 1)))
operatio = (numberDecimals * (10 ** round))
operatio = int(operatio)
operatio = operatio / (10 ** round)

print(f"El numero a redondear queda como: {operatio}")
print("Fin del programa")

