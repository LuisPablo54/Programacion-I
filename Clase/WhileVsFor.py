#While vs for

print("iclo while")
i = 2
while i<10:
    print(i)
    i = i + 2
print("Fin del ciclo while")


print("Ciclo for")
for i in range(2,10,2):
    print(i)
print("Fin del ciclo for")

print("Segundo ciclo for")
for i in range(10,0,-1):
    print(i)
print("Fin del segundo ciclo for")


'''
No se hace con decimales:

for i in range(2,10,0.5):
    print(i)
print("Fin del ciclo for")
'''