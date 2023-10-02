#Calcula si es mayor de edad

edad = int(input("¿Cuál es tu edad?: "))

'''
CASO DE 1 ALTERNATIVA
if (edad >= 18):
    print("Es mayor de edad")
else:
    print("Es menor de edad")
'''

#Alternativa 2
if (edad > 18):
    print(f"Es mayor de edad, tienres: {edad} años")
else:
    if (edad == 18):
        print("Tienes 18 años")
    else:
        print(f"Es menor de edad, tienres: {edad} años")


#Caso de licencia de conducir
if (edad < 18):
    permisoTutor = input("Tines periso de tu tutor (si/no)? ")


    if (edad >=16 and permisoTutor == "si"):
        print("Puedes tramitar tu licencia")

    else:
        print("No puedes realizar el tramite")

    print("Fin del programa")
else: 
    print("Puedes tramitar tu licencia")