import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('Personaje.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.ImaIzq = {0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76)}
        self.ImaDer = {0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76)}
        self.ImaArri = {0: (0, 228, 52, 76), 1: (52, 228, 52, 76), 2: (156, 228, 52, 76)}
        self.ImaAba = {0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76)}

    def darCuadroImagen(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def acortarIma(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.darCuadroImagen(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def actualizar(self, direction):
        if direction == 'izq':
            self.acortarIma(self.ImaIzq)
            self.rect.x -= 5
        if direction == 'der':
            self.acortarIma(self.ImaDer)
            self.rect.x += 5
        if direction == 'arri':
            self.acortarIma(self.ImaArri)
            self.rect.y -= 5
        if direction == 'aba':
            self.acortarIma(self.ImaAba)
            self.rect.y += 5

        if direction == 'EstaAlaIzq':
            self.acortarIma(self.ImaIzq[0])
        if direction == 'EstaAlaDer':
            self.acortarIma(self.ImaDer[0])
        if direction == 'EstaAArri':
            self.acortarIma(self.ImaArri[0])
        if direction == 'EstaAAba':
            self.acortarIma(self.ImaAba[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def manejoDeEvento(self, event):
        if event.type == pygame.QUIT:
            JuegoTerminado = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.actualizar('izq')
            if event.key == pygame.K_RIGHT:
                self.actualizar('der')
            if event.key == pygame.K_UP:
                self.actualizar('arri')
            if event.key == pygame.K_DOWN:
                self.actualizar('aba')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.actualizar('EstaAlaIzq')
            if event.key == pygame.K_RIGHT:
                self.actualizar('EstaAlaDer')
            if event.key == pygame.K_UP:
                self.actualizar('EstaAArri')
            if event.key == pygame.K_DOWN:
                self.actualizar('EstaAAba')