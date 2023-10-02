#Clase del 11 de septiembre 2023
#Calificación final
calificacion1 =float(input("Parcial 1: "))
calificacion2 =float(input("Parcial 2: "))
calificacion3 =float(input("Parcial 3: "))

proyecto = float(input("Proyecto final: "))

tareas = float(input("Calificación tarea: "))

print(f"Calificación 1: {calificacion1}")
print(f"Calificación 2: {calificacion2}")
print(f"Calificación 3: {calificacion3}")
print(f"Proyecto final: {proyecto}")

promedio = (calificacion2 + calificacion1 + calificacion3)/3



if (promedio < 6):
    print("Promedio examen: 5.0")
    promedioFinal = 5
else: 
    if (proyecto < 6):
        print("Reprobaste proyecto: 5.0")
        promedioFinal = 5
    else: 
        caliFinal = (0.35 * proyecto) + (0.2 * tareas) + (0.15 * calificacion1) + (0.15 * calificacion2) + (0.15 * calificacion3)
        print (f"Calificación juntos: {caliFinal}")
       
print(f"Optuviste un {promedio} en calificación y de proyecto {proyecto}")

print (f"Calificación juntos: {caliFinal}")
print("Fin del programa")