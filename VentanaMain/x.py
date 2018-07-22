import pygame
import y

pygame.init()
pantalla = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Trigon Fusionado")
reloj = pygame.time.Clock()
y = y.Personaje((500, 400))
JuegoTerminado = False
#fuente de texto para ecribir en pantalla
fuente1 = pygame.font.SysFont("Arial",20,True,False)
#Escribir tiempo en pantalla
tiempo=fuente1.render("Tiempo:",0,(255,255,255))

#Inicio de musica de fondo
pygame.mixer.Sound("MusicaFondo.wav").play()

while JuegoTerminado == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            JuegoTerminado = True

    y.manejoDeEvento(event)
    pantalla.fill(pygame.Color('black'))
    pantalla.blit(y.image, y.rect)
    #contador (tiempo)
    pantalla.blit(tiempo,(5,5))#mensaje tiempo
    segundos = round(pygame.time.get_ticks()/1000)
    segundos = str(segundos)
    contador = fuente1.render(segundos,0,(0,0,230))
    pantalla.blit(contador,(85,6))

    pygame.display.flip()
    reloj.tick(20)

pygame.quit ()