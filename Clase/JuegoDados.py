import random

#Entrada del casino

credito = 1000

#Mesa de apuesta
SeguirJugando = True
while SeguirJugando:
    
    Apuesta = -1
    intentos = 3
    #Lo minimo que necesito para que le este preguntando hasta que le de un valor valido 1 a 7
    while (Apuesta < 1 or Apuesta > 12):
        Apuesta = int(input("La suma a la que apuestas: "))
        intentos = intentos - 1
        if (intentos < 1 and intentos > -1):
            print("Miserable usuario, el numero debe de ser entre 2 y 12")
        elif (intentos < -1):
            print("¡¡YA PON UN NUMERO ENTRE 1 Y 12!!")
        
    monto = float(input("Monto de la apuesta: "))
    while (monto <=0 or monto > credito):
        monto = float(input("Monto de la apuesta: "))

    #Se hace la tirada de dados
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    suma = dado1 + dado2

    print("Dados: ", dado1, dado2)
    print("Suma: ", suma)
    #Condicional para ver si gano o perdio el usuario
    if Apuesta == suma:
        print("Ganaste")
        credito += monto
    else: 
        print("Perdiste, intente nuevamte")
        credito -= monto
    #Impreción del credito que te queda
    print("Tu credito es $%9.2f"%(credito))


    respuesta = input("Desea seguir jugando [s/n]: ")
    if respuesta == "n":
        SeguirJugando = False
    if credito == 0:
        SeguirJugando = False
print("Muchas gracias por participar")
    
#Para elegir que quieres el ultimo valor en una lista,
#Puedes usar ultimo = A [leand(A)-1]