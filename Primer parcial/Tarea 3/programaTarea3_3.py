#Tarea 3_3 Mayo de 3 datos
#Luis Pablo López Iracheta 192301-9

a = float(input("Valor de primer valor: "))
b = float(input("Valor de segundo valor: "))
c = float(input("Valor de tercer valor: "))

if (a > b) and (a > c):
    print(f"El primer valor es el mayor {a}")
if (b > a) and (b > c):
    print(f"El segundo valor es el mayor {b}")
if (c > a) and (c > b):
    print(f"El tercer valor es el mayor {c}")

else:
    print(f"Los tres numeros son iguales: {a}, {b} y {c}")

print("Fin del programa")
