import pygame
import y

pygame.init()
pantalla = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Trigon Fusionado")
reloj = pygame.time.Clock()
y = y.Personaje((500, 400))
JuegoTerminado = False

while JuegoTerminado == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            JuegoTerminado = True

    y.manejoDeEvento(event)
    pantalla.fill(pygame.Color('black'))
    pantalla.blit(y.image, y.rect)

    pygame.display.flip()
    reloj.tick(20)

pygame.quit ()