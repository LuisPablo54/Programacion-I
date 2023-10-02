#Tarea 2_3 Decimal
#Luis Pablo López Iracheta 192301-9

#Enter the number that I will round the decimals
numberDecimals = float(input("Ingrese un numero con decimal: "))


# I do the rounding operation
numberDecimals = numberDecimals + 0.5 
operatio = (numberDecimals * 10)
operatio = int(operatio)
operatio = operatio / 10

print(f"El numero a redondear queda como: {operatio}")
print("Fin del programa")
