
letras_romanas = {
"I" : 1,
"V" : 5
}

letras = input("Ingras la letra: ").upper()

if letras in letras_romanas:
    valor_numero = letras_romanas[letras]
    print(f"El valor de número de {letras} es {valor_numero}.")
else:
    print("Error")

'''
Letras_romanas = {
    "I" : 1,
    "V" : 5
}

letras = input("Ingresa la letra: ").upper()

if letras in letras_romanas:
    valor_numero = letras_romanas[letras]  # Utiliza corchetes en lugar de paréntesis
    print(f"El valor de número de {letras} es {valor_numero}.")  # Usé f-strings para formatear la cadena
else:
    print("Error")
'''