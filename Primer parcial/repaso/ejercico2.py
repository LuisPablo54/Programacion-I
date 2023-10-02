#Ejercio 2 tiempo

tiempo_s = int(input("El tiempo en segundo: "))

horas = tiempo_s // 3600
sobrante = tiempo_s % 3600

minutos = sobrante // 60
sobrante = sobrante % 60


segundo = sobrante

print(f"Horas: {horas}")
print(f"Minutos: {minutos}")
print(f"Segundos: {segundo}")

print("Fin del programa")
