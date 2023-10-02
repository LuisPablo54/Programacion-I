#Tarea 1.3 Cambio de dinero
#Luis Pablo López Iracheta 192301-9

#Declaro varibles

retiroTotal = 1850

b500 = 500
b200 = 200
b100 = 100
b50  = 50

#Cambio de billetes de 500

cambio500 = retiroTotal // b500
sobrante = retiroTotal % b500
print(f"Cambio de billetes de $500: {cambio500} billetes")

#Cambio de billetes de 200

cambio200 = sobrante // b200
sobranteDe200 = sobrante % b200
print(f"Cambio de billetes de $200: {cambio200} billetes")

#Cambio de billetes de 100

cambio100 = sobranteDe200 // b100
sobranteDe100 = sobranteDe200 % b100
print(f"Cambio de billetes de $100: {cambio100} billetes")

#Cambio de billetes de 50

cambio50 = sobranteDe100 // b50
print(f"Cambio de billetes de $50: {cambio50} billetes")






print("Fin de programa")