#Existen varias tecnicas para realizar un videjuego
#Una de esas tenicas, para las imagenes, es la llamada 2ble buffer

#La cual consiste en crear un copia deigital de la imagen que trabajamos
#Conn la que se cambia lo que nesesitamos y al finalizar se cambia por la imagen
#Que el usuaria ve 

import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Pelota")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Pelota
ball_radius = 20
ball_color = (255, 255, 0)
ball_speed = [5, 5]  # velocidad en x e y

ball = pygame.draw.circle(screen, ball_color, (width // 2, height // 2), ball_radius)

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar la posición de la pelota
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Rebotar en los bordes
    if ball.left < 0 or ball.right > width:
        ball_speed[0] = -ball_speed[0]
    if ball.top < 0 or ball.bottom > height:
        ball_speed[1] = -ball_speed[1]

    # Dibujar la pelota y la pantalla
    screen.fill(black)
    pygame.draw.circle(screen, ball_color, (ball.x, ball.y), ball_radius)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(30)
