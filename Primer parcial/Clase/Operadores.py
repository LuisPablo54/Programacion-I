#Clase 2 Operadores

a = 10 + 80

b = a -50

c = a*b
#división flotante - siempre
d = a/b
#divicion entera - siempre
e = a//b
#modulo (residuo de divicón)
m = a%b

print('a es la suma: ', a)
print('b = a - 50: ', b)
print('c = a * b', c)
print('d = a/b: ', d)
print('e = a//b: ', e)
print('m = a%b: ' , m)
print('find del programa')

'''
        Precedenciad e los operadores
'''
#p = 20+5 / 10*2+6 Lo que NO
#Lo que SI:

t = (20+5) / ((10*2)+6)


#Un plus: pero queda en texto
p = "{:.4f}".format(((20+5)/((10*2)+6)))

print(f'El valor de p en tipo texto = {p}')
print('El valor de p en tipo flotante ',t)

'''
        Operadores logicos
'''
A = 10
B = 20
C = 30

resultado = (a==b)

print(resultado)

#Nunca usar este operador dentro de un print, solo en clase
print('a!=b',a!=b)

