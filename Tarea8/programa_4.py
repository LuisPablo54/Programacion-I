#Tarea 8_4 Numero mayor de tres
#Luis Pablo López Iracheta 192301-9

'''
888888888888888888888888888888888
88888___88888888888888888___88888
8888_____888888888888888_____8888
8888_____888888888888888_____8888
8888_____888888888888888_____8888
8888_____888888888888888_____8888
8888_____888888888888888_____8888
8888_____888888888888888_____8888
8888_____88____888____88_____8888
8888_____8______8______8_____8888
8888_____8______8______8_____8888
8888_____8______8______8_____8888
8888_____8______8______8_____8888
8888_____8____8888888888888888888
8888_____8___88_____________88888
8888_____8__88_______________8888
8888______888_________________888
8888________88_________________88
8888__________88_______________88
8888____________88_____________88
8888_____________88___________888
8888______________8___________888
8888_______________8__________888
8888_______________8_________8888
88888_______________________88888
888888_____________________888888
888888888888888888888888888888888
No puede ser que me toco pasar otra vez, ya ponga otro 
metodo de seleccion porfa :(

'''

def Mayor(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        return numero2
    elif numero3 > numero1 and numero3 > numero2:
        return numero3
    else:
        return "Los tres valores son iguales"


primerNumero = float(input("Primer numero: "))
segundoNumero = float(input("Segundo numero: "))
tercerNumero = float(input("tercer numero: "))

mayorNumero = Mayor(primerNumero, segundoNumero, tercerNumero)

print("El numero mayor de los tres es: ", mayorNumero)


