#Tarea 1.2 Formula general
#Luis Pablo López Iracheta 192301-9
#Importo liberia de matematicas

import math   

#Declaro y valores:
a = 20
b = 16
c = 3

#Realizo operación

raiz_formula = (math.sqrt((b ** 2) - 4 * (a * c)))

#Resultado para positivo y negativo

furmulaPositovo = ((-b) + raiz_formula) / (2 * a)
formulaNegativo = ((-b) - raiz_formula) / (2 * a)

print(f"Resultado positivo {furmulaPositovo}")
print(f"Resultado positivo {formulaNegativo}")

print("Fin del pograma")
