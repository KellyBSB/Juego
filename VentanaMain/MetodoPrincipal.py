import pygame
import MovimientoPersonajeVentana
pygame.init()
pantalla = pygame.display.set_mode((1000,800))
pygame.display.set_caption("TrigonFusionado")
reloj = pygame.time.Clock()
MovimientoPersonajeVentana = MovimientoPersonajeVentana.Personaje((500, 400))
JuegoTerminado = False
while JuegoTerminado == False:
	for evento in pygame.evento.get():
		if evento.type == pygame.QUIT:
			JuegoTerminado = True
	MovimientoPersonajeVentana.manejoDeEvento(evento)
	pantalla.fill(pygame.Color('black'))
	pantalla.blit(MovimientoPersonajeVentana.image, MovimientoPersonajeVentana.rect)
	pygame.display.flip()
	reloj.tick(10)

pygame.quit()