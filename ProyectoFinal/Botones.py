import pygame 
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        
        pantalla.blit(self.imagen_actual,self.rect)

def Menu():
    pygame.init() # inicializar el modulo
    pantalla = pygame.display.set_mode([500, 500])
    #creo un reloj para controlar los fps
    reloj1=pygame.time.Clock()
    
    imagen1_1_Jugador=pygame.image.load("Boton1Jugador2.png")
    imagen2_1_Jugador=pygame.image.load("Boton1jugador.png")
    imagen1_2_Jugador=pygame.image.load("Boton2Jugador2.png")
    imagen2_2_Jugador=pygame.image.load("Boton2jugador.png")    
    imagen1_Puntuacion=pygame.image.load("Boton1Puntuacion2.png")
    imagen2_Puntuacion=pygame.image.load("BotonPuntuacion.png")    

    boton1=Boton(imagen1_1_Jugador,imagen2_1_Jugador,200,100)
    boton2=Boton(imagen1_2_Jugador,imagen2_2_Jugador,200,200)
    boton3=Boton(imagen1_Puntuacion,imagen2_Puntuacion,200,300)
    cursor1=Cursor()
    
    blanco=(255,255,255) # color blanco en RGB
    rojo=(200,0,0)
    azul=(0,0,200)
    colordefondo=blanco
    
    
    salir=False
    #LOOP PRINCIPAL
    while salir!=True:
        #recorro todos los eventos producidos
        #en realidad es una lista
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    colordefondo=rojo
                if cursor1.colliderect(boton2.rect):
                    colordefondo=azul
                if cursor1.colliderect(boton3.rect):
                    colordefondo=azul
            
            # pygame.QUIT( cruz de la ventana)
            if event.type == pygame.QUIT:
                salir=True
        
        reloj1.tick(20)#operacion para que todo corra a 20fps
        pantalla.fill(colordefondo) # pinto la superficie de blanco        
        cursor1.update()
        boton1.update(pantalla,cursor1)
        boton2.update(pantalla, cursor1)
        boton3.update(pantalla, cursor1)

        
        pygame.display.update() #actualizo el display
        
    pygame.quit()
    
Menu() 