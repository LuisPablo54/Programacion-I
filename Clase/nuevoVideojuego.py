import pygame
import sys

x = 100
y = 300
vx = 320
vy = 0
ay = 400
screen = pygame.display.set_mode((800, 600))
amarillo = (255, 255, 0)
deltaT = 0.05

salida = False

while salida == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x = x + vx * deltaT
    yOriginal = vy
    vy = yOriginal + ay * deltaT
    vyPromedio = (yOriginal + vy ) / 2
    y = y + vyPromedio * deltaT

    

    if x >= 800:
        vx = vx * -1
    if x <= 0 :
        vx = vx * -1
    if y >= 600 and vy > 0:
        vy = vy * -1
    
    pygame.draw.circle(screen, amarillo, (x,y), 5)

    pygame.display.flip()