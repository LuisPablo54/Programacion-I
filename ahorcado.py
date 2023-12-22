#Proyecto Final - Programación

#Integrantes:

#Rodrigo Mendoza Rodriguez
#Luis Pablo López Iracheta


#Aqui importamos la libreria random para una funcion de alatoriedad que usaremos adelante
import random as rdn


#Banco de palabras: son las listas que contienen las posibles palabras a a elegir
AnimalesFacil = ["perro","vaca","delfin","caballo","gato","leon","panda","jirafa","pez","jaguar"]

ColoresFacil = ["amarillo","verde","rojo","violeta","turquesa","marron","naranja","aguamarina","dorado","blanco",]

DeportesFacil = ["atletismo","esgrima","ciclismo","golf","natacion","tenis","baloncesto","boxeo","futbol","hockey"]

PaisesIntermedio = ["turquia","qatar","suecia","argentina","ucrania","brasil","canada","dinamarca","francia","polonia"]

ComidasIntermedio = ["guacamaya","torta","mole","pozole","palomitas","crepas","paella","poutine","tacos","tofu","pescado"]

MarcasIntermedio = ["adidas","honda","sony","whatsapp","canon","pinterest","facebook","airbnb","starbucks","youtube"]

FlorDificil = ["hortensia","azalea","pensamiento","orquidea","margarita","hibisco","bugambilia","lavanda","dalia","azucena"]

CiudadesDificil = ["villahermosa","aguascalientes","poroy","batman","bankok","xbox","copenhague","melbourne","amsterdam"]

InglesDificil = ["chemical","bought","nonplussed","whom","account","conversation","friend","group","indeed","international"]

#Dibujo del ahorcado: una lista con 7 elementos que basicamente son dibujos echos con simbolos
dibujos = ['''
     +----¬
     |    |
     |      
     |      
     |      
     |     
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    O
     |     
     |     
     |     
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    O 
     |    | 
     |     
     |
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    O 
     |   /| 
     |     
     |     
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    O 
     |   /|\ 
     |     
     |  
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    O 
     |   /|\ 
     |   / 
     |
    =========
    /       \ ''', '''
     +----¬
     |    |
     |    0 
     |   /|\ 
     |   / \ 
     |
    =========
    /       \ ''']

#Programa del ahorcado

#Primero algo de formalidad, pedir su mobre y iniciar el juego
nombre = str(input("Nombre del jugador: "))
print(f"\nPerfecto {nombre}, empezando el juego de arcado: \n")

#Primero vamos a elegir con que plabara vamos a trabajar, para eso nos basamos en las preferencias del usuario
#Lo de nuevo juego true y flase, solo es para lograr hacer un bucle, por si el usuario
#no elige una opcion existente le vuelva a preguntar hasta que eliga una que si existe
nuevojuego = True
while nuevojuego == True:
    nuevojuego = False
    print("Primero, ¿Que dificultad deseas?")
    print("\n Dificil \n Intermedio \n Facil \n")
    dificultad = input()
    #.Lower => es para pasar todas las letras de la variable a minusculas
    dificultad = dificultad.lower()
    #.strip => Elimina todos los espacios antes o despues en la cadena de texto
    dificultad = dificultad.strip()
    #aqui ya inician las deciciones, depende de la dificultat que desee el usuario
    if dificultad == "dificil":
          print("\nBuscas reto eh?, pero antes elige de que tematica quieres jugar \n")
          print("\n Flores \n Ciudades \n Ingles \n")
          tematicaDificil = input()
          tematicaDificil = tematicaDificil.lower()
          tematicaDificil = tematicaDificil.strip()
          #Una vez elegida la dificultad, elige la tematica
          # y la variable diccionario pasa a valer la lista del banco de palabras elegida
          if tematicaDificil == "flores":
              diccionario = FlorDificil
          elif tematicaDificil == "ciudades":
              diccionario = CiudadesDificil
          elif tematicaDificil == "ingles":
              diccionario = InglesDificil
          else:
              #Aqui creamos una interrupcion en el progrma como un error
              # que le mostrara la cadena de texto escrita.
              raise Exception("Esa categoria no existe, por favor selecciona una correcta") 
          
    #Continuamos con los siguientes bloques que son como el primero pero con diferentes categorias
    elif dificultad == "intermedio":
          print("\nBuena opcion, siempre en equilibrio, vamos a elegir tematica \n")
          print("\n Paises \n Comidas \n Marcas \n")
          tematicaIntermedia = input()
          tematicaIntermedia = tematicaIntermedia.lower()
          tematicaIntermedia = tematicaIntermedia.strip()
          if tematicaIntermedia == "paises":
              diccionario = PaisesIntermedio
          elif tematicaIntermedia == "comidas":
              diccionario = ComidasIntermedio
          elif tematicaIntermedia == "marcas":
              diccionario = MarcasIntermedio
          else:
              raise Exception("Esa categoria no existe, por favor selecciona una correcta")
    elif dificultad == "facil":
          print("\nVienes a relajarte, perfercto, dime ¿Que tematica quieres? \n")
          print("\n Animales \n Colores \n Deportes \n")
          tematicaFacil = input()
          tematicaFacil = tematicaFacil.lower()
          tematicaFacil = tematicaFacil.strip()
          if tematicaFacil == "animales":
              diccionario = AnimalesFacil
          elif tematicaFacil == "colores":
              diccionario = ColoresFacil
          elif tematicaFacil == "deportes":
              diccionario = DeportesFacil
          else:
              raise Exception("Esa categoria no existe, por favor selecciona una correcta")
    #como mencione lo de true y false solo es por si el usuario elige una categoria inexistente
    # que "nuevojuego" valga otra vez true y con el "continue" se vuelva a ejecutar desde el primer bucle
    else:
        print("\n La opcion seleccionada no esta disponible, de favor corrige tu escritura \n")
        nuevojuego = True
        continue
print("\n \n Buena elección ", nombre,", comencemos con el juego")

#------------------------------------------------------------------------
#Esta funcion con la ayuda de la libreria random, y el randint toma un valor entre 0 y la longitud
# de la lista diccionario -1 para despues regresar la palabra sacandola por el valor obtenido de la lista
def Palabra_al_Azar(diccionario):
    palabraOculta = rdn.randint(0, len(diccionario) - 1)
    return diccionario[palabraOculta]
#Aqui somplemente la funcion actualiza que numero en la lista de dibujos va a llmar depende
# de cuantos erorres lleve el usuario, al inicio lleva 0 por lo que imprime el primer elemento
def Diseño_ahorcado():
    print(dibujos[len(letras_incorrectas)],"\n")

#-------------------------------------------------------------------------

#1: llama a la funcion previa para que saber si aun tienes intentos, imprimir la lista casillas y
# las letras incorrectas que llevas, con el asterisco se desglosan los elementos de la lista, asi mostrandolos
def Tablero():
    Diseño_ahorcado()
    if len(letras_incorrectas) < 6:
        print(*casillas)
        print("\n Letras incorrectas que llevas: ", *letras_incorrectas)
#2: Esta funcion es para que el usuario solo pueda meter una letra no mas, no simbolos, etc.
def Letra_Valida():
    if letra in "abcdefghijklmnñopqrstuvxyzw" and len(letra) == 1:
        return True
    elif len(letra) > 1:
        print("\n \n \n \n ingresa solo una letra a la vez")
        return False
    elif letra not in "abcdefghijklmnñopqrstuvxyzw":
        print("\n \n \n \n Solamente se aceptan letras del abedecario, Prueba otra vez")
        return False
#3: Esta funcion es para ver si la letra ingrsada ya fue ingresada previamente
def Letra_Repetida():
    if letra in letras_incorrectas:
        print("\n \n \n Ya te equivocaste con esa letra")
        return True
    elif letra in casillas:
        print("\n \n \n Ya atinaste esa letra")   
        return True
    else:
        return False

#4: basicamente si todavia te quedan "intentos" que chece si descubirste una letra, y si no
# que la anexe a la lista de letras incorrectas, pero si era la ultima letra por descubir y si
# le atinaste, entonces que ya te ponga que fue la ultima.
def comprobar():
    if len(letras_incorrectas) < 6:
        if letra in palabra:
            print("\n \n \n \n Perfecto le atinaste a una!\n")
        elif Victoria() == True:
            print("\n \n \n \n Perfecto, le atinaste a la ultima")
        else:
            print("\n \n \n \n Esa letra no era, intentalo de nuevo :(\n")
            letras_incorrectas.append(letra)
#5: Comprobamos si la letra esta en la palabra para sutituirla por el guion =>
# basicamente si el elemento de la lista de la palabra con indice "i" (desde el 0 hasta la longitud de la palabra)
# es igual a la letra del usuario, entonces en la lista "casillas" que tiene el mismo indice "i",
# va a ser remplazado por la letra del usuario.
def actualizar_casillas():
    for i in range(len(palabra)):
        if palabra[i] == letra:
            casillas[i] = letra
#6: aqui podemos comprobar si ya no quedan guiones bajos en la lista casillas porque ya todos fueron
# cambiados por letras, entonces ganaste y refresa true porque vamos a aplicar un blucle en el bloque
# del juego en si, asi como al inicio con el de elegir dificultad.
def Victoria():
    if " _" not in casillas:
        print("Felicidades ", nombre,"!!! Descubriste la palabra por completo, que listo que sos")
        print("La palabra era", palabra)
        return True
#7: Simplemente si la lista de letras incorrectas alcanza 6 elementos en ella, quiere decir
# que te quedaste sin intentos y pues perdiste
def Perder():
    if len(letras_incorrectas) == 6:
        print("F en el chat ¡Lo siento", nombre,"! ¡Has perdido! la palabra a adivinar era: " ,palabra)
        return True
#8: Aqui solo ingresamos esta funcion para usarla en el bucle del juego para que,
# cuando pierdas no se cierre tan abruptamente el programa.
def Tablero_Final():
    Diseño_ahorcado()
    if len(letras_incorrectas) < 6:
        print(*casillas)



#-------------------------------------------------------------------------
#Bucle del juego en si:
    
#Primero sacamos la plabra oculta del juego con la primera fucion vista, con ayuda de random
palabra = Palabra_al_Azar(diccionario)
#La lista casillas van a ser tantos guiones como la cantidad de letras de la palabra
casillas = [ " _" ]*len(palabra)
#metemos la lista letras incorrectas, su valor incial seria 0,
#con esto mas adelante imprimiriamos el dibujo con indice 0 (osea el primer dibujo)
letras_incorrectas = []
#Aqui volvemos a aplicar lo de true y false para hacer un bucle, ya que la variable comprobacion
#va ser con la que salgamos o sigamos dentro del bucle.


#Primero se le da un valor de verdadero, asi mientras (while) "confirmacion" sea verdadera, se ejecuta el bucle
confirmacion = True
while confirmacion == True:
    
    #Llamamos la funcion #1, para que imprima el dibujo del ahorcado con indice 0 (el primero seria)
    Tablero()
    #Simlemente le pedimos al usuario que iongrese una letra, la pasamos a minusculas y le quitamos los espacios.
    letra = input("\nAhora ¿Con cual letra quiere probar su suerte?  ")
    letra = letra.lower()
    letra = letra.strip()
    print("-------------------------------------------------------------------------------------------------------")
    #Ahora si con la funcion #2 vemos si el usuario solo ingreso una letra y no simbolos, dos letras, etc.
    #Pero tambien vemos si la letra no esta repetida, cuando se cumplen las dos condiciones se ejecuta el bloque
    if Letra_Valida() == True and Letra_Repetida() == False:
        #Primero con la funcion #4 vemos si la letra esta o no en la plabra
        comprobar()
        #Despues si es que la letra si esta en la palabra esta suplanta el guion depende de en que lugar esta la la letra en la palabra
        actualizar_casillas()
        #Comprobamos si el usuario gano con la funcion #6
        if Victoria() == True:
            #Metemos la funcion #8 ya que es el ultimo tablero
            Tablero_Final()
            input(":D\n \nPresiona enter para terminar. ")
            #dandole valor de falso ya no se ejecutaria el blucle y salimos de el.
            confirmacion = False
        #Ahora si no gano, vemos si perdio, si es asi se imprime el 7 dibujo de la lista, osea el de ahorcado colgado
        if Perder() == True:
            Tablero()
            #Dandole enter es para que no se cierre el programa tan bruscamente y el usuario le de enter para terminarlo
            input("D:\n \nPresiona enter para terminar. ")
            confirmacion = False
                
    #Si en el "if" no se fue por ninguna quiere decir que sigue jugando asi que, le ponemos que lo intente otra vez
    # y con el "continue" el bloque principal se volveria a ejecutar, pidiendo una letra, comprobando, etc.
    else:
        print("intentalo de nuevo ", nombre)
        confirmacion = True
        continue
    
#---------------------------------------------------------------------------