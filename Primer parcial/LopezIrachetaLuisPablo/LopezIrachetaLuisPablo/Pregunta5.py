#Pregunta 5
#Luis Pablo López Iracheta 192301-9

primeraVariable = int(input("Primer valor: "))
segundaVariable = int(input("Primer valor: "))

operacion = primeraVariable % segundaVariable

if operacion > 0:
    print(f"El {segundaVariable} NO es un multiplo de {primeraVariable}")
else:
    print(f"El {segundaVariable} es un multiplo de {primeraVariable}")
    

print("Fin del programa")
