
from MatricesFernando import multiplicacion  # Importa la función multiplicacion desde el módulo MatricesFernando

operacion = input("Multiplicacion (y): ")



if operacion == "y" or "Y":
    a = [
        [-1, 0, 1],
        [7, (3/2), -(13/2)],
        [3, (1/2), -(5/2)]
        ]

    b = [[11],
        [-4],
        [10]]
    
    resultado = multiplicacion(a, b)  # Llama a la función multiplicacion desde el módulo MatricesFernando
    
else:
    print("Operación no reconocida")
print("Fin del programa")