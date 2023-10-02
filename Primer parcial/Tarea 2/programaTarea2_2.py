#Tarea 2_1 Tiempo
#Luis Pablo López Iracheta 192301-9

tiempo_s = int(input("El tiempo que desea calcular (segundos): "))
horas = 3600
minutos = 60

#Operaciones

Thoras = tiempo_s // horas
resuido = tiempo_s % horas

Tminutos = resuido // minutos
resuido = resuido % minutos

segundos = resuido

print(f"""
Horas: {Thoras}
minutos: {Tminutos}
segundos: {segundos}
 """)

print('Fin del programa')
