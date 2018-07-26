import pygame
import player
import player2

#inicializar modulos de pygame
pygame.init()
# Dimensiones de la pantalla
ancho_ventana = 1000
alto_ventana = 600
#Crear pantalla
pantalla = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("TRIGON FUCIONADO")
#reloj
clock = pygame.time.Clock()
#Ubicacion del personaje en la pantalla
player = player.Personaje((ancho_ventana/4, alto_ventana/4))
player2 = player2.Personaje2((ancho_ventana/2,alto_ventana/2))

#Salidad del bucle principal
game_over = False

#fuente de texto para ecribir en pantalla
fuente1 = pygame.font.SysFont("Arial",20,True,False)
#Escribir tiempo en pantalla
tiempo=fuente1.render("Tiempo:",0,(255,255,255))

#Inicio de musica de fondo
pygame.mixer.Sound("MusicaFondo.wav").play()
#sprites

#Funcion Principal
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    #eventos del jugador 1
    player.manejoDeEvento(event)
    player2.manejoDeEvento2(event)
    #color de fondo
    pantalla.fill(pygame.Color('black'))
    #pintar personaje
    pantalla.blit(player.image, player.rect)
    pantalla.blit(player2.image,player2.rect)
    pygame.display.flip()
    #contador (tiempo)
    pantalla.blit(tiempo,(5,5))#mensaje tiempo
    segundos = round(pygame.time.get_ticks()/1000)
    segundos = str(segundos)
    contador = fuente1.render(segundos,0,(0,0,230))
    pantalla.blit(contador,(85,6))

    #Actualizar pantalla
    pygame.display.update()

    clock.tick(20)

pygame.quit ()
